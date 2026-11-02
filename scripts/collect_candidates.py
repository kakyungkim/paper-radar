#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
collect_candidates.py — paper-radar 주간 논문 후보 수집기 (GitHub Actions용)

클라우드 루틴 세션은 arXiv/bioRxiv/medRxiv에 접근할 수 없으므로(403/DNS 차단),
인터넷이 열린 Actions 러너에서 공식 API로 지난 7일 후보와 초록 전문을 모아 저장소에 둔다.

사용 : python3 scripts/collect_candidates.py 2026-W45 [--days 7] [--end YYYY-MM-DD]
                                              [--max 60] [--offline-fixtures DIR]
출력 : vault/raw/candidates-{WEEK}.json, vault/raw/candidates-{WEEK}.md
종료 : 한 소스라도 성공하면 0, 전부 실패하면 1

외부 의존성 없음(Python 3 표준 라이브러리 + 시스템 curl).
"""

import argparse
import datetime as dt
import html
import json
import os
import re
import subprocess
import sys
import time
import urllib.parse
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DIR = os.path.join(ROOT, "vault", "raw")
SEEN_PATH = os.path.join(ROOT, "vault", "_meta", "recent-papers.jsonl")
UA = "paper-radar/1.0 (personal weekly digest; mailto:kakyung.kim@gmail.com)"

# CLAUDE.md "포커스 범위"와 맞춘 핵심 키워드 (부분 일치, 소문자)
FOCUS_TERMS = [
    "bioinformatic", "genom", "transcriptom", "single-cell", "single cell", "multi-omic",
    "multiomic", "epigenom", "proteom", "gwas", "variant", "sequencing",
    "clinical prediction", "electronic health record", "ehr", "medical imaging", "radiology",
    "pathology", "prognos", "foundation model",
    "drug discovery", "molecule generation", "molecular generation", "protein language",
    "protein structure", "protein design", "docking", "admet", "drug-target", "de novo design",
    "large language model", "llm", "biomedical",
]
BIORXIV_CORE = {"bioinformatics", "genomics", "genetics", "systems biology", "synthetic biology",
                "pharmacology and toxicology"}
BIORXIV_KEYWORD_ONLY = {"cancer biology", "immunology"}
CODE_RE = re.compile(r"(?:https?://)?(?:www\.)?(?:github\.com|gitlab\.com|zenodo\.org|figshare\.com"
                     r"|huggingface\.co)/[^\s)>\]\"',;]+")


# ---------------------------------------------------------------------------
# 네트워크
# ---------------------------------------------------------------------------
def http_get(url, retries=3):
    """curl로 가져온다(urllib는 일부 호스트에서 시간 초과). 실패 시 RuntimeError."""
    last = ""
    for i in range(retries):
        r = subprocess.run(["curl", "-sfL", "-m", "60", "-A", UA, url], capture_output=True)
        if r.returncode == 0:
            return r.stdout.decode("utf-8", "replace")
        last = f"curl 종료 코드 {r.returncode}"
        time.sleep(2 * (i + 1))
    raise RuntimeError(last)


def fetch(url, fixture, fixtures_dir):
    if fixtures_dir:
        with open(os.path.join(fixtures_dir, fixture), encoding="utf-8") as f:
            return f.read()
    return http_get(url)


# ---------------------------------------------------------------------------
# 파싱
# ---------------------------------------------------------------------------
def short_authors(names):
    names = [n.strip() for n in names if n.strip()]
    return "; ".join(names[:3] + ["et al."]) if len(names) > 3 else "; ".join(names)


def parse_biorxiv(payload, server):
    out = []
    for it in payload.get("collection", []):
        doi = it.get("doi", "")
        out.append({
            "source": server, "id": doi, "doi": doi.lower(), "arxiv_id": "",
            "title": " ".join(it.get("title", "").split()),
            "authors": short_authors(it.get("authors", "").split(";")),
            "date": it.get("date", ""), "category": it.get("category", ""), "journal": "",
            "status": "preprint", "url": f"https://doi.org/{doi}", "code_links": [],
            "abstract": " ".join(it.get("abstract", "").split()),
        })
    return out


def parse_arxiv(xml_text):
    ns = {"a": "http://www.w3.org/2005/Atom",
          "x": "http://arxiv.org/schemas/atom"}
    out = []
    for e in ET.fromstring(xml_text).findall("a:entry", ns):
        aid = re.sub(r"v\d+$", "", e.findtext("a:id", "", ns).rsplit("/abs/", 1)[-1])
        pc = e.find("x:primary_category", ns)
        names = [a.findtext("a:name", "", ns) for a in e.findall("a:author", ns)]
        out.append({
            "source": "arxiv", "id": aid, "doi": "", "arxiv_id": aid,
            "title": " ".join(e.findtext("a:title", "", ns).split()),
            "authors": short_authors(names).replace("; ", ", "),
            "date": e.findtext("a:published", "", ns)[:10],
            "category": pc.get("term") if pc is not None else "", "journal": "",
            "status": "preprint", "url": f"https://arxiv.org/abs/{aid}", "code_links": [],
            "abstract": " ".join(e.findtext("a:summary", "", ns).split()),
        })
    return out


def parse_europepmc(payload):
    out = []
    for it in payload.get("resultList", {}).get("result", []):
        abstract = " ".join(html.unescape(re.sub(r"<[^>]+>", " ", it.get("abstractText", ""))).split())
        if not abstract:
            continue
        doi = it.get("doi", "")
        names = [n.strip() for n in it.get("authorString", "").rstrip(".").split(",")]
        out.append({
            "source": "europepmc", "id": f"PMID:{it.get('pmid') or it.get('id', '')}",
            "doi": doi.lower(), "arxiv_id": "",
            "title": " ".join(it.get("title", "").split()).rstrip("."),
            "authors": short_authors(names).replace("; ", ", "),
            "date": it.get("firstPublicationDate", ""), "category": "",
            "journal": it.get("journalTitle", ""), "status": "peer-reviewed",
            "url": f"https://doi.org/{doi}" if doi else f"https://europepmc.org/article/MED/{it.get('id', '')}",
            "code_links": [], "abstract": abstract,
        })
    return out


# ---------------------------------------------------------------------------
# 필터, 점수, 중복 제거
# ---------------------------------------------------------------------------
def code_links(text):
    seen, out = set(), []
    for m in CODE_RE.findall(text or ""):
        m = m.rstrip(".")
        if m not in seen:
            seen.add(m)
            out.append(m)
    return out


def match_terms(c):
    t, a = c["title"].lower(), c["abstract"].lower()
    def has(k, s):  # 짧은 약어는 단어 경계로 (ehr가 Fehr에 걸리지 않게)
        return bool(re.search(rf"\b{re.escape(k)}\b", s)) if len(k) <= 4 else k in s
    return [(k, has(k, t), has(k, a)) for k in FOCUS_TERMS if has(k, t) or has(k, a)]


def relevant(c):
    cat = c.get("category", "").lower()
    if c["source"] == "biorxiv":
        return cat in BIORXIV_CORE or (cat in BIORXIV_KEYWORD_ONLY and bool(match_terms(c)))
    if c["source"] == "medrxiv":
        return bool(match_terms(c))
    if c["source"] == "arxiv" and not cat.startswith("q-bio"):
        return bool(match_terms(c))
    return True


def score_candidate(c):
    hits = match_terms(c)
    c["code_links"] = list(dict.fromkeys(c.get("code_links", []) + code_links(c["abstract"])))
    c["matched_terms"] = [k for k, _, _ in hits]
    c["score"] = (sum(3 for _, ti, _ in hits if ti) + sum(1 for _, _, ab in hits if ab)
                  + (2 if c["code_links"] else 0) + (1 if c["status"] == "peer-reviewed" else 0))
    return c


def load_seen(path):
    seen = {"dois": set(), "arxiv": set()}
    if not os.path.exists(path):
        return seen
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            try:
                r = json.loads(line)
            except ValueError:
                continue
            if r.get("doi"):
                seen["dois"].add(r["doi"].lower())
            if r.get("arxiv_id"):
                seen["arxiv"].add(re.sub(r"v\d+$", "", r["arxiv_id"]))
    return seen


def dedup(cands, seen):
    best = {}
    for c in cands:
        aid = re.sub(r"v\d+$", "", c.get("arxiv_id", ""))
        if (c.get("doi") and c["doi"].lower() in seen["dois"]) or (aid and aid in seen["arxiv"]):
            continue
        key = c["doi"].lower() if c.get("doi") else f"arxiv:{aid}"
        old = best.get(key)
        rank = (c["status"] == "peer-reviewed", c.get("score", 0))
        if old is None or rank > (old["status"] == "peer-reviewed", old.get("score", 0)):
            best[key] = c
    return list(best.values())


def window(end, days):
    return end - dt.timedelta(days=days - 1), end


def filter_window(cands, start, end):
    return [c for c in cands if c["date"][:10] and start.isoformat() <= c["date"][:10] <= end.isoformat()]


# ---------------------------------------------------------------------------
# 소스별 수집
# ---------------------------------------------------------------------------
def collect_rxiv(server, start, end, fx):
    out, cursor = [], 0
    while cursor < 2000:
        url = f"https://api.biorxiv.org/details/{server}/{start}/{end}/{cursor}"
        data = json.loads(fetch(url, f"{server}.json", fx))
        out += parse_biorxiv(data, server)
        msg = (data.get("messages") or [{}])[0]
        n, total = int(msg.get("count", 0) or 0), int(msg.get("total", 0) or 0)
        cursor += n  # 페이지 크기는 API가 정함(현재 30). 고정값 가정 금지
        if n == 0 or cursor >= total or fx:
            break
    return out


def collect_arxiv(start, end, fx):
    terms = "protein OR genom* OR single-cell OR drug OR molecul* OR clinical OR EHR OR biomedical"
    q = ("cat:q-bio.* OR ((cat:cs.LG OR cat:cs.AI OR cat:cs.CL) AND "
         + " AND ".join(["(" + " OR ".join(f"abs:{t}" for t in terms.split(" OR ")) + ")"]) + ")")
    out = []
    for page in range(5):
        url = ("https://export.arxiv.org/api/query?" + urllib.parse.urlencode({
            "search_query": q, "sortBy": "submittedDate", "sortOrder": "descending",
            "start": page * 100, "max_results": 100}))
        batch = parse_arxiv(fetch(url, "arxiv.xml", fx))
        out += batch
        if fx or not batch or batch[-1]["date"] < start.isoformat():
            break
        time.sleep(3)  # arXiv 예절: 요청 간 3초
    return out


def collect_europepmc(start, end, fx):
    terms = " OR ".join(f'"{t}"' for t in ["bioinformatics", "genomics", "single-cell", "multi-omics",
                                          "electronic health record", "drug discovery",
                                          "protein language model", "large language model biomedical",
                                          "clinical prediction model", "medical imaging deep learning"])
    q = f"FIRST_PDATE:[{start} TO {end}] AND SRC:MED AND HAS_ABSTRACT:y AND ({terms})"
    out, cm = [], "*"
    for _ in range(3):
        url = ("https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + urllib.parse.urlencode({
            "format": "json", "resultType": "core", "pageSize": 100, "query": q, "cursorMark": cm}))
        data = json.loads(fetch(url, "europepmc.json", fx))
        out += parse_europepmc(data)
        nxt = data.get("nextCursorMark")
        if fx or not nxt or nxt == cm or not data.get("resultList", {}).get("result"):
            break
        cm = nxt
    return out


# ---------------------------------------------------------------------------
# 출력
# ---------------------------------------------------------------------------
def render_md(week, start, end, stats, cands):
    L = [f"# paper-radar 후보 {week}", "",
         f"- 수집 창: {start} ~ {end} (Actions 자동 수집, 초록은 API 원문)",
         f"- 후보 {len(cands)}건 (점수순)", "",
         "| 소스 | 수집 | 채택 | 오류 |", "| --- | --- | --- | --- |"]
    for s, v in stats.items():
        L.append(f"| {s} | {v['fetched']} | {v['kept']} | {v['error'] or '-'} |")
    for i, c in enumerate(cands, 1):
        L += ["", f"### {i}. {c['title']}",
              f"- 출처: {c['source']} · {c['date']} · **{c['status']}**"
              + (f" · {c['journal']}" if c.get("journal") else "")
              + (f" · {c['category']}" if c.get("category") else ""),
              f"- 저자: {c['authors']}",
              f"- DOI/링크: {c['url']}",
              f"- 코드/데이터: {', '.join(c['code_links']) or '초록에 링크 없음'}",
              f"- 점수: {c['score']} (키워드: {', '.join(c['matched_terms']) or '-'})",
              "", f"> {c['abstract']}"]
    return "\n".join(L) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("week")
    ap.add_argument("--days", type=int, default=7)
    ap.add_argument("--end")
    ap.add_argument("--max", type=int, default=60)
    ap.add_argument("--offline-fixtures")
    a = ap.parse_args()
    if a.end:
        end = dt.date.fromisoformat(a.end)
    else:
        end = (dt.datetime.now(dt.timezone.utc) + dt.timedelta(hours=9)).date()
    start, end = window(end, a.days)
    fx = a.offline_fixtures
    jobs = {"biorxiv": lambda: collect_rxiv("biorxiv", start, end, fx),
            "medrxiv": lambda: collect_rxiv("medrxiv", start, end, fx),
            "arxiv": lambda: collect_arxiv(start, end, fx),
            "europepmc": lambda: collect_europepmc(start, end, fx)}
    stats, pool = {}, []
    for name, job in jobs.items():
        try:
            got = job()
            stats[name] = {"fetched": len(got), "kept": 0, "error": None}
            pool += [c for c in filter_window(got, start, end) if relevant(c)]
        except Exception as e:  # 한 소스 실패가 전체를 막지 않게
            stats[name] = {"fetched": 0, "kept": 0, "error": str(e)[:200]}
            print(f"[{name}] 실패: {e}", file=sys.stderr)
    for c in pool:
        score_candidate(c)
    final = sorted(dedup(pool, load_seen(SEEN_PATH)), key=lambda c: (-c["score"], c["date"]))[:a.max]
    for c in final:
        stats[c["source"]]["kept"] += 1
    os.makedirs(RAW_DIR, exist_ok=True)
    base = os.path.join(RAW_DIR, f"candidates-{a.week}")
    with open(base + ".json", "w", encoding="utf-8") as f:
        json.dump(final, f, ensure_ascii=False, indent=1)
    with open(base + ".md", "w", encoding="utf-8") as f:
        f.write(render_md(a.week, start, end, stats, final))
    for s, v in stats.items():
        print(f"{s}: 수집 {v['fetched']} / 채택 {v['kept']} / 오류 {v['error'] or '-'}")
    ok = any(v["error"] is None for v in stats.values())
    print(f"후보 {len(final)}건 -> {base}.md")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
