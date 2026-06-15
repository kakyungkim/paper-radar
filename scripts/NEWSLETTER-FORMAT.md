# 다이제스트 md 구조 계약 (NEWSLETTER-FORMAT)

`vault/digest/YYYY-Www.md`가 따라야 하는 구조 계약. digest-editor가 이 양식으로 쓰고, digest-renderer가 `scripts/render_html.py`로 파싱해 HTML/푸시를 만든다. 양식을 어기면 렌더가 깨지거나 섹션이 누락된다.

> 상태: **초안 계약(설계 단계).** 첫 실행에서 digest-editor가 실제 다이제스트를 만든 뒤, 그 구조를 기준으로 이 계약과 `render_html.py`를 함께 확정한다. (econ-radar의 scripts/NEWSLETTER-FORMAT.md + render_html.py를 출발점으로 이식.)

## 프런트매터
```
---
type: digest
period: 2026-W24
tags: [논문, 주간, 관련분야]
---
```

## 섹션 순서·헤더 (영어 헤더, 본문 한국어)
1. `## At a Glance` — 3줄 리드(이번 주 핵심 흐름). 중간 재요약 금지.
2. `## This Week's Top 5` — 핵심 논문 5편. 각 논문 카드:
   - `### {한국어 제목 (원제)}`
   - 저자 줄: `저자: {1저자, 교신저자 | 소속 기관}` — 필수, 누락 금지
   - 메타 줄: `출처 · 날짜 · [preprint|peer-reviewed] · [DOI](url) · [code](url) 또는 코드 미공개 — 재현 불가`
   - `**선택 이유**` 1문장 — 왜 이번 주에 이 논문을 골랐나. "흥미롭다" 수준 반려.
   - `사회적 신호:` {HF Daily Papers #N / X 언급 XXX건 / 없음} — raw 파일의 사회적 신호 그대로
   - `**Key Point**` 1~2문장(객관)
   - `**💡 인사이트**` 1문장(주관)
   - 렌즈 줄(해당될 때): `🔬 Method` / `🩺 Clinical` / `🏭 Industry` 각 한 줄
   - `검증 수준: {in silico|후향|전향|외부·다기관|RCT}`
3. `## Deep Dive` — 1~2편 심층(소제목 + 문단).
4. `## 🔭 Wide Angle` — 핵심 밖 2~3편, 각 한 줄 요약 + 링크.
5. `## Threads to Follow` — 이어볼 흐름(불릿).
6. `## Sources` — 전체 DOI/링크 목록.

## 배지·표기 규칙 (렌더가 파싱)
- preprint/peer-reviewed, 검증 수준, 분야 태그(유전체·임상ML·신약AI·단백질·LLM-bio)는 정해진 문자열로 표기 → 렌더가 색 배지로 변환.
- 모든 논문에 DOI 또는 원문 링크 필수. 코드/데이터 링크는 있으면 표기, 없으면 "없음".

## render_html.py 입출력 (예정)
- 입력: `vault/digest/YYYY-Www.md` → 출력: `vault/html/YYYY-Www.html` + `vault/push/YYYY-Www.md`
- 사용: `python3 scripts/render_html.py 2026-W24` (`--out-suffix .test`로 미리보기)
