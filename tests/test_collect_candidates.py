# -*- coding: utf-8 -*-
"""collect_candidates.py 단위 검사 (네트워크 없음, 인라인 픽스처)."""
import os
import sys
import datetime as dt

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import collect_candidates as cc  # noqa: E402

BIORXIV = {
    "messages": [{"status": "ok", "count": 3, "total": 3}],
    "collection": [
        {"doi": "10.1101/2026.10.30.111111", "title": "Single-cell foundation model for genomics",
         "authors": "Kim, A.; Lee, B.; Park, C.; Choi, D.", "date": "2026-10-30",
         "category": "bioinformatics", "version": "1",
         "abstract": "We build a model for single-cell data. Code at https://github.com/x/y ."},
        {"doi": "10.1101/2026.10.30.222222", "title": "Zebrafish fin regeneration", "authors": "Doe, J.",
         "date": "2026-10-30", "category": "developmental biology", "version": "1", "abstract": "Fins."},
        {"doi": "10.1101/2026.10.01.333333", "title": "Old genomics paper", "authors": "Old, O.",
         "date": "2026-10-01", "category": "genomics", "version": "1", "abstract": "genomics"},
    ],
}
ARXIV = """<?xml version="1.0"?><feed xmlns="http://www.w3.org/2005/Atom">
<entry><id>http://arxiv.org/abs/2610.12345v2</id><published>2026-10-31T10:00:00Z</published>
<title>Protein language
  model for drug discovery</title><summary> A protein model for molecule design. </summary>
<author><name>A One</name></author><author><name>B Two</name></author>
<author><name>C Three</name></author><author><name>D Four</name></author>
<arxiv:primary_category xmlns:arxiv="http://arxiv.org/schemas/atom" term="cs.LG"/>
</entry></feed>"""
EPMC = {"resultList": {"result": [
    {"id": "123", "source": "MED", "doi": "10.1101/2026.10.30.111111", "title": "Single-cell foundation model for genomics.",
     "authorString": "Kim A, Lee B, Park C, Choi D.", "firstPublicationDate": "2026-10-31",
     "journalTitle": "Nature Methods", "abstractText": "<h4>Background</h4>Single-cell genomics model."},
    {"id": "124", "source": "MED", "doi": "10.1000/noabs", "title": "No abstract", "firstPublicationDate": "2026-10-31",
     "journalTitle": "J X"},
]}}


def test_parse_biorxiv():
    r = cc.parse_biorxiv(BIORXIV, "biorxiv")
    assert len(r) == 3
    assert r[0]["authors"] == "Kim, A.; Lee, B.; Park, C.; et al."
    assert r[0]["status"] == "preprint" and r[0]["url"].endswith("10.1101/2026.10.30.111111")


def test_category_filter_biorxiv():
    r = cc.parse_biorxiv(BIORXIV, "biorxiv")
    kept = [c for c in r if cc.relevant(c)]
    assert {c["doi"] for c in kept} == {"10.1101/2026.10.30.111111", "10.1101/2026.10.01.333333"}


def test_parse_arxiv():
    r = cc.parse_arxiv(ARXIV)
    assert r[0]["arxiv_id"] == "2610.12345" and r[0]["date"] == "2026-10-31"
    assert r[0]["title"] == "Protein language model for drug discovery"
    assert r[0]["category"] == "cs.LG" and r[0]["authors"].endswith("et al.")


def test_parse_europepmc():
    r = cc.parse_europepmc(EPMC)
    assert len(r) == 1  # 초록 없는 항목 제외
    assert r[0]["status"] == "peer-reviewed" and "<h4>" not in r[0]["abstract"]
    assert r[0]["journal"] == "Nature Methods"


def test_code_links():
    assert cc.code_links("see https://github.com/a/b and zenodo.org/record/1") == [
        "https://github.com/a/b", "zenodo.org/record/1"]
    assert cc.code_links("nothing here") == []


def test_score_order():
    a = {"title": "Genomics model", "abstract": "genomics genomics", "code_links": [], "status": "preprint"}
    b = dict(a, code_links=["https://github.com/a/b"])
    c = dict(b, status="peer-reviewed")
    for x in (a, b, c):
        cc.score_candidate(x)
    assert a["score"] < b["score"] < c["score"]
    assert b["score"] - a["score"] == 2 and c["score"] - b["score"] == 1
    assert "genom" in a["matched_terms"]
    # 제목 가중 x3, 초록 x1
    t = cc.score_candidate({"title": "genomics", "abstract": "", "code_links": [], "status": "preprint"})
    assert t["score"] == 3


def test_seen_and_dedup(tmp_path):
    p = tmp_path / "r.jsonl"
    p.write_text('# comment\n{"doi":"10.1101/AAA","arxiv_id":""}\n{"doi":"","arxiv_id":"2610.99999"}\n',
                 encoding="utf-8")
    seen = cc.load_seen(str(p))
    cands = [{"doi": "10.1101/aaa", "arxiv_id": "", "status": "preprint", "score": 1},
             {"doi": "", "arxiv_id": "2610.99999v3", "status": "preprint", "score": 1},
             {"doi": "10.1/new", "arxiv_id": "", "status": "preprint", "score": 1}]
    out = cc.dedup(cands, seen)
    assert [c["doi"] for c in out] == ["10.1/new"]


def test_cross_source_dedup_prefers_published():
    pre = {"doi": "10.1101/X", "arxiv_id": "", "status": "preprint", "score": 5}
    pub = {"doi": "10.1101/x", "arxiv_id": "", "status": "peer-reviewed", "score": 4}
    out = cc.dedup([pre, pub], {"dois": set(), "arxiv": set()})
    assert len(out) == 1 and out[0]["status"] == "peer-reviewed"


def test_window_filter():
    s, e = cc.window(dt.date(2026, 11, 1), 7)
    assert (s, e) == (dt.date(2026, 10, 26), dt.date(2026, 11, 1))
    r = cc.parse_biorxiv(BIORXIV, "biorxiv")
    kept = cc.filter_window(r, s, e)
    assert len(kept) == 2


def test_render_md_has_abstract():
    c = cc.parse_biorxiv(BIORXIV, "biorxiv")[0]
    cc.score_candidate(c)
    md = cc.render_md("2026-W44", dt.date(2026, 10, 26), dt.date(2026, 11, 1),
                      {"biorxiv": {"fetched": 3, "kept": 1, "error": None},
                       "arxiv": {"fetched": 0, "kept": 0, "error": "HTTP 403"}}, [c])
    assert "We build a model for single-cell data" in md
    assert "HTTP 403" in md and "2026-10-26" in md
