#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
render_html.py — paper-radar 주간 다이제스트 결정적 렌더러

입력 : vault/digest/YYYY-Www.md   (digest-editor 산출물, NEWSLETTER-FORMAT.md 계약 준수)
출력 : vault/html/YYYY-Www.html   (단일 HTML 논문 다이제스트)
       vault/push/YYYY-Www.md     (텔레그램용 짧은 푸시 메시지)

사용 : python3 scripts/render_html.py 2026-W24
       python3 scripts/render_html.py 2026-W24 --out-suffix .test

외부 의존성 없음(Python 3 표준 라이브러리만). LLM 토큰 0.
"""

import sys
import os
import re
import argparse

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SCRIPT_DIR)
DIGEST_DIR = os.path.join(ROOT, "vault", "digest")
HTML_DIR = os.path.join(ROOT, "vault", "html")
PUSH_DIR = os.path.join(ROOT, "vault", "push")

# ---------------------------------------------------------------------------
# 배지 매핑
# ---------------------------------------------------------------------------
BADGE_CLASS = {
    "유전체": "badge-genome",
    "임상ML": "badge-clinical",
    "신약AI": "badge-drug",
    "단백질": "badge-protein",
    "LLM-bio": "badge-llmbio",
    "기타": "badge-other",
    "preprint": "badge-preprint",
    "peer-reviewed": "badge-peer",
    "in silico": "badge-insilico",
    "후향": "badge-retro",
    "전향": "badge-prosp",
    "외부·다기관": "badge-multi",
    "RCT": "badge-rct",
}

LENS_EMOJI = {"Method": "🔬", "Clinical": "🩺", "Industry": "🏭", "Demand": "🎯"}

# ---------------------------------------------------------------------------
# 유틸: 인라인 마크다운 → HTML
# ---------------------------------------------------------------------------
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
WIKILINK_RE = re.compile(r"\s*\[\[[^\]]+\]\]\s*")


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def inline(text):
    """[t](u) → <a>, **b** → <strong>, *i* → <em>, [[wikilink]] 제거."""
    text = WIKILINK_RE.sub(" ", text)
    out = []
    pos = 0
    for m in LINK_RE.finditer(text):
        chunk = text[pos:m.start()]
        out.append(_fmt(esc(chunk)))
        out.append('<a href="%s" class="underline text-indigo-700" target="_blank">%s</a>'
                   % (m.group(2), esc(m.group(1))))
        pos = m.end()
    out.append(_fmt(esc(text[pos:])))
    return "".join(out).strip()


def _fmt(s):
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", s)
    return s


def badge_html(label, extra_cls=""):
    cls = BADGE_CLASS.get(label, "badge-other")
    return ('<span class="badge %s %s">%s</span>' % (cls, extra_cls, esc(label))).strip()


def warn(msg):
    sys.stderr.write("[render_html] 경고: %s\n" % msg)


# ---------------------------------------------------------------------------
# 마크다운 파서
# ---------------------------------------------------------------------------
def parse_markdown(md):
    lines = md.split("\n")
    doc = {
        "period": None,
        "glance": [],
        "top5": [],       # list of card dicts
        "deepdive": [],   # list of (title, paras)
        "wide": [],       # list of (bold_title, preprint_tag, body_html)
        "threads": [],
        "sources": [],    # list of (label, url)
    }

    # frontmatter
    i = 0
    if lines and lines[0].strip() == "---":
        i = 1
        while i < len(lines) and lines[i].strip() != "---":
            m = re.match(r"^period:\s*(.+)$", lines[i])
            if m:
                doc["period"] = m.group(1).strip()
            i += 1
        i += 1

    body = lines[i:]
    n = len(body)
    j = 0

    while j < n:
        line = body[j]
        s = line.strip()

        m = re.match(r"^##\s+(.+)$", line)
        if m:
            head = m.group(1).strip()
            if head == "At a Glance":
                j = _parse_glance(body, j + 1, doc)
                continue
            if head == "This Week's Top 5":
                j = _parse_top5(body, j + 1, doc)
                continue
            if head == "Deep Dive":
                j = _parse_deepdive(body, j + 1, doc)
                continue
            if "Wide Angle" in head:
                j = _parse_wide(body, j + 1, doc)
                continue
            if head == "Threads to Follow":
                j = _parse_threads(body, j + 1, doc)
                continue
            if head == "Sources":
                j = _parse_sources(body, j + 1, doc)
                continue
            j += 1
            continue
        j += 1

    return doc


def _parse_glance(body, j, doc):
    n = len(body)
    while j < n:
        s = body[j].strip()
        if re.match(r"^##\s+", body[j]):
            break
        if s and s != "---":
            doc["glance"].append(s)
        j += 1
    return j


def _parse_top5(body, j, doc):
    n = len(body)
    card = None
    while j < n:
        line = body[j]
        s = line.strip()
        if re.match(r"^##\s+", line):
            break

        # 새 카드 시작 (### 제목)
        m = re.match(r"^###\s+(.+)$", line)
        if m:
            card = {
                "title": m.group(1).strip(),
                "meta": "",        # Source · Date · preprint · DOI · code
                "key_point": "",
                "insight": "",
                "lenses": [],      # [(name, text)]
                "verify": "",
                "tags": [],        # 분야 태그 from title/meta
            }
            doc["top5"].append(card)
            j += 1
            continue

        if card is None:
            j += 1
            continue

        if s == "---" or s == "":
            j += 1
            continue

        # Key Point
        m = re.match(r"^\*\*Key Point\*\*\s*[—-]\s*(.+)$", s)
        if m:
            card["key_point"] = m.group(1).strip()
            j += 1
            continue

        # 💡 인사이트
        m = re.match(r"^💡\s*\*\*인사이트\*\*\s*[—-]\s*(.+)$", s)
        if m:
            card["insight"] = m.group(1).strip()
            j += 1
            continue

        # 렌즈 줄 (🔬 🩺 🏭 🎯)
        m = re.match(r"^(🔬|🩺|🏭|🎯)\s*(Method|Clinical|Industry|Demand):\s*(.+)$", s)
        if m:
            card["lenses"].append((m.group(2), m.group(3).strip()))
            j += 1
            continue

        # 검증 수준
        m = re.match(r"^검증\s*수준:\s*(.+)$", s)
        if m:
            card["verify"] = m.group(1).strip()
            j += 1
            continue

        # 메타 줄 (첫 번째 일반 텍스트 줄)
        if not card["meta"] and not s.startswith("#"):
            card["meta"] = s
        j += 1
    return j


def _parse_deepdive(body, j, doc):
    n = len(body)
    section_title = ""
    paras = []
    while j < n:
        line = body[j]
        s = line.strip()
        if re.match(r"^##\s+", line):
            break
        if re.match(r"^###\s+", line):
            if section_title or paras:
                doc["deepdive"].append((section_title, list(paras)))
            section_title = re.match(r"^###\s+(.+)$", line).group(1).strip()
            paras = []
            j += 1
            continue
        if s == "---":
            if section_title or paras:
                doc["deepdive"].append((section_title, list(paras)))
            section_title = ""
            paras = []
            j += 1
            continue
        if s:
            paras.append(s)
        j += 1
    if section_title or paras:
        doc["deepdive"].append((section_title, list(paras)))
    return j


def _parse_wide(body, j, doc):
    n = len(body)
    while j < n:
        line = body[j]
        s = line.strip()
        if re.match(r"^##\s+", line):
            break
        if s == "---" or s == "":
            j += 1
            continue
        # **Title: ...** · preprint — Description [Link](url)
        m = re.match(r"^\*\*(.+?)\*\*\s*(?:·\s*\*\*(preprint[^*]*)\*\*)?\s*[—-]?\s*(.*)$", s)
        if m:
            title = m.group(1).strip()
            preprint_tag = m.group(2).strip() if m.group(2) else ""
            body_text = m.group(3).strip() if m.group(3) else ""
            doc["wide"].append((title, preprint_tag, body_text))
        j += 1
    return j


def _parse_threads(body, j, doc):
    n = len(body)
    while j < n:
        line = body[j]
        s = line.strip()
        if re.match(r"^##\s+", line):
            break
        m = re.match(r"^-\s+(.+)$", s)
        if m:
            doc["threads"].append(m.group(1).strip())
        j += 1
    return j


def _parse_sources(body, j, doc):
    n = len(body)
    while j < n:
        line = body[j]
        s = line.strip()
        if re.match(r"^##\s+", line):
            break
        # markdown table row: | label | url |
        m = re.match(r"^\|([^|]+)\|([^|]+)\|([^|]*)\|?$", s)
        if m:
            cols = [c.strip() for c in [m.group(1), m.group(2), m.group(3)]]
            # header/separator 행 제외
            if cols[0].startswith("-") or cols[0].lower() in ("#", "label", ""):
                j += 1
                continue
            # 3열: | label | desc | url |  또는  | # | 제목 | url |
            label = cols[0]
            if cols[2].startswith("http"):
                title = cols[1]
                url = cols[2]
            elif cols[1].startswith("http"):
                title = cols[0]
                url = cols[1]
            else:
                title = cols[1]
                url = cols[2]
            if url.startswith("http"):
                doc["sources"].append((("%s — %s" % (label, title)).strip("— "), url))
        j += 1
    return j


# ---------------------------------------------------------------------------
# 섹션 렌더
# ---------------------------------------------------------------------------
CSS = """
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css');
    body { font-family:'Pretendard',-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif; font-size:16px; line-height:1.78; }
    .badge { font-size:11px; font-weight:700; padding:2px 9px; border-radius:9999px; display:inline-block; margin-right:4px; }
    .badge-genome   { background:#dcfce7; color:#166534; }
    .badge-clinical { background:#dbeafe; color:#1e40af; }
    .badge-drug     { background:#ede9fe; color:#5b21b6; }
    .badge-protein  { background:#fce7f3; color:#9d174d; }
    .badge-llmbio   { background:#fef9c3; color:#713f12; }
    .badge-other    { background:#f3f4f6; color:#374151; }
    .badge-preprint { background:#fef3c7; color:#92400e; }
    .badge-peer     { background:#d1fae5; color:#065f46; }
    .badge-insilico { background:#e0e7ff; color:#3730a3; }
    .badge-retro    { background:#fef9c3; color:#713f12; }
    .badge-prosp    { background:#d1fae5; color:#065f46; }
    .badge-multi    { background:#dbeafe; color:#1e40af; }
    .badge-rct      { background:#dcfce7; color:#166534; }
    .key-point { border-left:4px solid #4338ca; padding:10px 16px; background:#f5f3ff; border-radius:0 10px 10px 0; margin-top:12px; }
    .key-point .label { font-size:11px; font-weight:700; letter-spacing:0.06em; color:#4338ca; margin-bottom:4px; }
    .key-point .text { font-size:15px; font-weight:500; color:#312e81; line-height:1.7; }
    .insight { border-left:4px solid #14b8a6; padding:10px 16px; background:#f0fdfa; border-radius:0 10px 10px 0; margin-top:10px; }
    .insight .label { font-size:11px; font-weight:700; letter-spacing:0.06em; color:#0f766e; margin-bottom:4px; }
    .insight .text { font-size:15px; color:#134e4a; line-height:1.7; }
    .lens-row { display:flex; gap:8px; flex-wrap:wrap; margin-top:10px; }
    .lens-item { font-size:13.5px; color:#374151; padding:4px 10px; background:#f9fafb; border:1px solid #e5e7eb; border-radius:8px; }
    .lens-demand { font-size:13.5px; color:#92400e; padding:4px 10px; background:#fef3c7; border:1px solid #fde68a; border-radius:8px; }
    .verify-tag { font-size:12px; color:#6b7280; margin-top:8px; }
"""

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>paper-radar — {period}</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <style>{css}</style>
</head>
<body class="bg-gray-50 text-gray-900">
  <div class="max-w-3xl mx-auto px-4 py-10">
{body}
  </div>
</body>
</html>"""


def render_header(doc):
    period = esc(doc["period"] or "")
    return """    <header class="mb-8">
      <div class="flex items-center gap-3 mb-2">
        <span class="text-2xl font-bold tracking-tight text-gray-900">📄 paper-radar 주간 다이제스트</span>
        <span class="text-lg text-gray-500 font-medium">{period}</span>
      </div>
      <p class="text-xs text-gray-400">바이오인포·임상ML·신약AI 논문 주간 요약. 모든 해석은 preprint 단계에서의 분석임.</p>
    </header>""".format(period=period)


def render_glance(doc):
    if not doc["glance"]:
        return ""
    ps = "\n".join(
        '        <p class="text-[15px] leading-relaxed text-gray-800">%s</p>' % inline(g)
        for g in doc["glance"]
    )
    return """    <section class="mb-8">
      <h2 class="text-xs font-bold tracking-widest text-indigo-600 uppercase mb-3">At a Glance</h2>
      <div class="bg-indigo-50 border border-indigo-200 rounded-2xl p-5 space-y-3">
{ps}
      </div>
    </section>""".format(ps=ps)


def render_top5(doc):
    if not doc["top5"]:
        return ""
    cards = []
    for idx, card in enumerate(doc["top5"], 1):
        # 검증수준 배지
        verify_badges = ""
        if card["verify"]:
            vparts = [v.strip() for v in re.split(r"[/·,]", card["verify"])]
            verify_badges = " ".join(badge_html(v) for v in vparts if v)

        # preprint/peer 배지 from meta
        meta_badges = ""
        if "preprint" in card["meta"]:
            meta_badges = badge_html("preprint")
        elif "peer-reviewed" in card["meta"]:
            meta_badges = badge_html("peer-reviewed")

        meta_html = inline(card["meta"]) if card["meta"] else ""

        kp = ""
        if card["key_point"]:
            kp = """          <div class="key-point">
            <div class="label">KEY POINT</div>
            <div class="text">%s</div>
          </div>""" % inline(card["key_point"])

        ins = ""
        if card["insight"]:
            ins = """          <div class="insight">
            <div class="label">💡 인사이트</div>
            <div class="text">%s</div>
          </div>""" % inline(card["insight"])

        lens_html = ""
        if card["lenses"]:
            items = " ".join(
                '<span class="%s">%s %s: %s</span>' % (
                    "lens-demand" if name == "Demand" else "lens-item",
                    LENS_EMOJI.get(name, ""), esc(name), inline(text))
                for name, text in card["lenses"]
            )
            lens_html = '<div class="lens-row">%s</div>' % items

        verify_html = ""
        if verify_badges:
            verify_html = '<div class="verify-tag">검증 수준: %s</div>' % verify_badges

        cards.append("""        <div class="bg-white rounded-2xl shadow-sm border border-gray-100 p-6">
          <div class="flex items-center gap-2 mb-2 flex-wrap">
            <span class="text-xs font-bold text-gray-400">#{idx}</span>
            {meta_badges}
          </div>
          <h3 class="text-[17px] font-bold text-gray-900 leading-snug mb-2">{title}</h3>
          <p class="text-[13px] text-gray-500 mb-3">{meta}</p>
{kp}
{ins}
{lens}
{verify}
        </div>""".format(
            idx=idx,
            meta_badges=meta_badges,
            title=inline(card["title"]),
            meta=meta_html,
            kp=kp, ins=ins, lens=lens_html, verify=verify_html,
        ))

    return """    <section class="mb-10">
      <h2 class="text-xl font-bold text-gray-900 mb-5 pb-2 border-b border-gray-200">This Week's Top 5</h2>
      <div class="space-y-6">
{cards}
      </div>
    </section>""".format(cards="\n\n".join(cards))


def render_deepdive(doc):
    if not doc["deepdive"]:
        return ""
    sections = []
    for title, paras in doc["deepdive"]:
        if not paras and not title:
            continue
        paras_html = "\n          ".join(
            '<p class="text-[15px] text-gray-800 leading-relaxed">%s</p>' % inline(p)
            for p in paras if p
        )
        sections.append("""      <div class="mb-6">
        <h3 class="text-[16px] font-bold text-gray-800 mb-4">{title}</h3>
        <div class="space-y-3">
          {paras}
        </div>
      </div>""".format(title=inline(title) if title else "", paras=paras_html))

    return """    <section class="mb-10">
      <h2 class="text-xl font-bold text-gray-900 mb-5 pb-2 border-b border-gray-200">Deep Dive</h2>
{sections}
    </section>""".format(sections="\n\n".join(sections))


def render_wide(doc):
    if not doc["wide"]:
        return ""
    items = []
    for title, preprint_tag, body_text in doc["wide"]:
        tag_html = badge_html("preprint") if preprint_tag else ""
        items.append("""        <div class="flex items-start gap-3 py-4 border-b border-gray-100 last:border-0">
          <div class="flex-1">
            <p class="text-[15px] font-semibold text-gray-900 mb-1">{title} {tag}</p>
            <p class="text-[14px] text-gray-700 leading-relaxed">{body}</p>
          </div>
        </div>""".format(title=esc(title), tag=tag_html, body=inline(body_text)))

    return """    <section class="mb-10">
      <h2 class="text-xl font-bold text-gray-900 mb-5 pb-2 border-b border-gray-200">🔭 Wide Angle</h2>
      <div class="bg-white rounded-2xl border border-gray-100 shadow-sm px-6 py-2">
{items}
      </div>
    </section>""".format(items="\n".join(items))


def render_threads(doc):
    if not doc["threads"]:
        return ""
    lis = "\n".join(
        '          <li class="text-[15px] text-gray-800 leading-relaxed">%s</li>' % inline(t)
        for t in doc["threads"]
    )
    return """    <section class="mb-10">
      <h2 class="text-xl font-bold text-gray-900 mb-5 pb-2 border-b border-gray-200">Threads to Follow</h2>
      <div class="bg-white rounded-2xl border border-gray-100 shadow-sm p-6">
        <ul class="space-y-3 list-disc list-inside">
{lis}
        </ul>
      </div>
    </section>""".format(lis=lis)


def render_sources(doc):
    if not doc["sources"]:
        return ""
    rows = "\n".join(
        '              <li><a href="%s" class="text-indigo-600 underline" target="_blank">%s</a></li>'
        % (esc(url), esc(label))
        for label, url in doc["sources"]
    )
    return """    <section class="mb-10">
      <h2 class="text-xl font-bold text-gray-900 mb-5 pb-2 border-b border-gray-200">Sources</h2>
      <div class="bg-white rounded-2xl border border-gray-100 shadow-sm p-6">
        <ul class="space-y-2 text-[13.5px]">
{rows}
        </ul>
      </div>
    </section>""".format(rows=rows)


def render_footer(doc):
    period = esc(doc["period"] or "")
    return """    <footer class="border-t border-gray-200 pt-8 pb-10 text-center">
      <p class="text-sm text-gray-500 mt-4">paper-radar · {period}</p>
      <p class="text-xs text-gray-400 mt-1">바이오인포·임상ML·신약AI 논문 주간 요약. preprint 분석 포함.</p>
    </footer>""".format(period=period)


def build_html(doc):
    sections = [
        render_header(doc),
        render_glance(doc),
        render_top5(doc),
        render_deepdive(doc),
        render_wide(doc),
        render_threads(doc),
        render_sources(doc),
        render_footer(doc),
    ]
    body = "\n\n".join(s for s in sections if s)
    return HTML_TEMPLATE.format(period=doc["period"] or "", css=CSS, body=body)


# ---------------------------------------------------------------------------
# 푸시 메시지
# ---------------------------------------------------------------------------
EMOJI_NUM = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣"]


def build_push(doc):
    period = doc["period"] or ""
    lines = ["📄 paper-radar %s" % period, ""]
    if doc["glance"]:
        # At a Glance 첫 줄만
        g0 = re.sub(r"\*\*", "", doc["glance"][0])
        g0 = LINK_RE.sub(r"\1", g0)
        lines.append(g0[:120])
        lines.append("")
    for idx, card in enumerate(doc["top5"][:5]):
        title = card["title"]
        # 괄호 원제 제거
        title = re.sub(r"\s*\([^)]+\)\s*$", "", title).strip()
        # 마크다운 제거
        title = re.sub(r"\*\*|__", "", title)
        lines.append("%s %s" % (EMOJI_NUM[idx], title[:60]))
    lines.append("")
    lines.append("🔗 전체 보기: https://kakyungkim.github.io/paper-radar/%s.html" % period)
    # 첫 핵심 논문 DOI 링크
    if doc["top5"]:
        links = list(LINK_RE.finditer(doc["top5"][0].get("meta", "")))
        doi_links = [m for m in links if "doi.org" in m.group(2) or "arxiv.org" in m.group(2)]
        if doi_links:
            lines.append("🔗 핵심 원문: %s" % doi_links[0].group(2))
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# 메인
# ---------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description="paper-radar 다이제스트 HTML/푸시 렌더러")
    ap.add_argument("period", help="주차 (YYYY-Www, 예: 2026-W24)")
    ap.add_argument("--out-suffix", default="", help="출력 파일명 접미사 (예: .test)")
    args = ap.parse_args()

    if not re.match(r"^\d{4}-W\d{2}$", args.period):
        sys.stderr.write("[render_html] 오류: 주차 형식은 YYYY-Www 여야 합니다.\n")
        sys.exit(2)

    md_path = os.path.join(DIGEST_DIR, args.period + ".md")
    if not os.path.isfile(md_path):
        sys.stderr.write("[render_html] 오류: 입력 md 없음: %s\n" % md_path)
        sys.exit(1)

    with open(md_path, encoding="utf-8") as f:
        md = f.read()

    try:
        doc = parse_markdown(md)
    except Exception as e:
        sys.stderr.write("[render_html] 파싱 실패: %s\n" % e)
        sys.exit(1)

    if not doc["period"]:
        doc["period"] = args.period

    if not doc["top5"] and not doc["glance"]:
        sys.stderr.write("[render_html] 오류: 필수 섹션(At a Glance/Top 5)을 찾지 못했습니다.\n")
        sys.exit(1)

    html = build_html(doc)
    push = build_push(doc)

    suffix = args.out_suffix
    os.makedirs(HTML_DIR, exist_ok=True)
    os.makedirs(PUSH_DIR, exist_ok=True)
    html_path = os.path.join(HTML_DIR, args.period + suffix + ".html")
    push_path = os.path.join(PUSH_DIR, args.period + suffix + ".md")

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    with open(push_path, "w", encoding="utf-8") as f:
        f.write(push)

    sys.stderr.write("[render_html] 완료\n")
    sys.stderr.write("  HTML: %s (%d bytes)\n" % (html_path, len(html.encode("utf-8"))))
    sys.stderr.write("  PUSH: %s\n" % push_path)
    sys.stderr.write("  섹션: top5=%d, deepdive=%d, wide=%d, threads=%d, sources=%d\n" % (
        len(doc["top5"]), len(doc["deepdive"]), len(doc["wide"]),
        len(doc["threads"]), len(doc["sources"])))


if __name__ == "__main__":
    main()
