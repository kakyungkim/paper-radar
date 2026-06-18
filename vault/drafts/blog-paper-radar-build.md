---
type: draft
status: rough-draft
created: 2026-06-16
tags: [기술블로그, paper-radar, AI에이전트, 하네스, 논문다이제스트]
---

# 논문 주간 다이제스트를 자동화하다 — paper-radar 구축기

매주 바이오인포·신약AI 관련 논문을 훑어야 하는데, 직접 하려니 시간이 너무 걸렸다. arXiv, bioRxiv, PubMed를 돌면서 뭐가 나왔는지 파악하고, 읽을 만한 걸 걸러내고, 요약하고, 어딘가에 기록해 두는 과정을 매주 반복하는 건 지속 가능하지 않다. 그래서 에이전트 팀으로 이 일을 넘겼다.

결과물은 **paper-radar** — 매주 일요일 아침 9시에 혼자 돌아가는 논문 주간 다이제스트 하네스다.

## 뭘 하는 시스템인가

매주 한 번, 이런 흐름으로 돌아간다.

```
논문 수집 (paper-scout)
  → 방법·임상·산업 3렌즈 분석 (method/clinical/industry-analyst)
  → 다이제스트 편집 (digest-editor)
  → 문체 검수 (style-critic)
  → 사실 검증 (claim-checker)
  → HTML 렌더 + 텔레그램 push 생성 (render_html.py)
  → 블로그 배포 (deploy.sh)
  → 텔레그램 채널 발송 (GitHub Actions)
  → vault 정리 (knowledge-curator)
```

각 단계가 파일을 쓰고, 다음 단계가 그 파일을 읽는다. 에이전트끼리 직접 대화하지 않는다. 파일이 계약이다.

## 핵심 설계 결정들

### 렌더러 계약 분리

처음엔 에이전트가 HTML을 직접 생성했다. 문제가 있었다. 에이전트마다 HTML 구조가 조금씩 달랐고, 스타일 수정이 필요할 때마다 에이전트 프롬프트를 고쳐야 했다.

바꾼 방식: 다이제스트는 마크다운(`vault/digest/YYYY-Www.md`)으로 쓰고, 렌더는 Python 스크립트(`scripts/render_html.py`)가 담당한다. `NEWSLETTER-FORMAT.md`가 마크다운 구조 계약을 명시한다. 에이전트는 계약을 지키는 마크다운만 쓰면 되고, HTML·CSS는 스크립트에서 관리한다. 렌더를 바꿔도 에이전트 프롬프트를 건드릴 필요가 없다.

### DOI 기반 dedup

같은 논문이 여러 버전(arXiv v1→v2→저널 게재)으로 나온다. 처음에 제목 기반으로 중복을 걸렀더니 제목이 조금 바뀐 논문이 통과됐다. DOI·arXiv ID를 기준으로 바꿨다. `vault/_meta/recent-papers.jsonl`에 줄 단위 JSON으로 기록하고, 매주 수집 시작 전에 읽어서 이미 다룬 논문을 걸러낸다.

### preprint 상태 추적

바이오 논문의 절반 이상은 처음엔 프리프린트다. 동료심사 전의 수치가 나중에 바뀌는 경우가 있다. knowledge-curator가 매주 기존 preprint 레코드를 PubMed에서 확인해 출판이 확인되면 `status: published`로 갱신하고 별도 알림을 보낸다. 독자가 "이 논문 나중에 다 바뀌었다"고 뒤늦게 아는 상황을 줄이려는 장치다.

### 딥다이브 별도 발송

5편 핵심 요약과 1~2편 심층 분석을 한 메시지에 다 때려넣으면 길어진다. 텔레그램에서 긴 메시지는 펼쳐 읽지 않는다. 주간 요약(5편 짧게)과 딥다이브(1편 길게)를 별도 메시지로 분리했다. `render_html.py`가 `YYYY-Www.md`와 `YYYY-Www-deepdive.md`를 따로 만들고, GitHub Actions에서 순서대로 발송한다.

## 벤치마킹에서 가져온 것

BRIC 한빛사, Import AI, preLights, TheSequence 등 7개 매체를 실제로 보면서 뭘 가져올 수 있는지 정리했다.

**선택 이유 1줄**: preLights가 쓰는 방식. "왜 이 논문을 골랐나"를 한 줄로 쓴다. 없으면 큐레이션인지 그냥 목록인지 구분이 안 된다.

**코드 공개 여부 배지**: Papers with Code에서 착안. 코드가 없는 논문은 재현이 안 된다. 독자가 바로 알 수 있게 빨간 배지를 붙인다.

**사회적 신호**: AlphaSignal처럼 "HuggingFace Daily Papers #3" 같은 줄을 추가한다. 해당 주에 얼마나 주목받는 논문인지 독자가 가늠할 수 있다.

## 텔레그램 자동 발송 문제

Claude Code의 클라우드 루틴(CCR)에서 `api.telegram.org`로 직접 HTTP 요청이 안 된다. 클라우드 샌드박스 환경이 외부 HTTPS를 막고 있다. 한동안 이 원인을 모르고 토큰만 계속 확인했다.

해결: 에이전트가 `vault/push/`에 파일을 쓰고 git push하면, GitHub Actions가 파일 변경을 감지해 텔레그램으로 발송한다. 자세한 구현은 별도 글에 정리했다. → [[blog-ccr-github-actions-bridge]]

## 지금 상태

매주 일요일 09:00 KST에 혼자 돌아간다. 나는 일요일 아침에 텔레그램에서 알림을 받아 읽는다. 블로그(`kakyungkim.github.io/paper-radar`)에도 자동으로 올라간다.

아직 완벽하지 않다. Nature·Cell 같은 유료 저널은 초록만 읽을 수 있고, 소속 기관 정보가 빠진 논문이 종종 나온다. 코드 미공개 논문 비율이 높은 주도 있다. 이런 건 실행 후 `improvement-log.md`에 기록하고 다음 주에 조금씩 고친다.

---

*초안. 발행 전 구체 수치·링크 보강 필요.*
