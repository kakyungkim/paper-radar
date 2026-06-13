---
name: weekly-paper-digest-orchestrator
description: paper-radar의 주간 논문 다이제스트 파이프라인 입구. "이번 주 논문 정리/다이제스트", "paper-radar 돌려줘", "유전체 쪽만", "방법 파트만 다시", "이 논문으로 발제 만들어줘" 같은 수집·분석·다이제스트·HTML·발제 요청에서 사용한다. 프리프린트+PubMed 기반, 영어 논문 한국어 번역, 방법·임상·산업 3렌즈로 정리하고 vault에 누적한다.
---

# weekly-paper-digest-orchestrator (1층 진행표 / 팀장)

매주 논문을 수집→분석(방법·임상·산업)→다이제스트→검수→검증→HTML·푸시로 만들고, 선택적으로 스터디 발제를 뽑아 vault에 누적하는 Agent Team을 지휘한다.

## 언제 이 스킬을 쓰나
- 초기 실행: "이번 주 논문 정리해줘", "paper-radar 돌려줘".
- 부분 재실행: "방법 파트만 다시", "HTML만 다시 렌더", "유전체 쪽만".
- 3층: "이 논문으로 발제 자료 만들어줘".

## 실행 모드 분기 (먼저 확인)
1. `date`로 현재 날짜·ISO 주차 확인(`TZ=Asia/Seoul date '+%G-W%V'`).
2. `vault/raw/`, `vault/digest/`에서 **이번 주차** 산출물이 있는지 본다.
   - 없음 → 초기 실행(전체 파이프라인). 있음+부분 요청 → 부분 재실행. "이 논문으로 발제" → 3층만.

## 팀 구성 (Agent Team)
paper-scout, method-analyst, clinical-analyst, industry-analyst, digest-editor, style-critic, claim-checker, digest-renderer, knowledge-curator. (3층: study-brief-writer, trend-synthesizer)

## 품질 기준선
- `vault/_meta/benchmarks.md`(본받을 논문 다이제스트·리뷰) 체크리스트를 품질 기준으로. `lens-guide.md`(3렌즈 정의), `korean-style-samples.md`(문체)를 의무 참조.

## 실행 흐름
1. `TeamCreate`로 팀을 만든다.
2. `TaskCreate`로 단계·의존관계 등록:
   - T1 수집(paper-scout) → `vault/raw/papers-YYYY-Www.md` (핵심 5 + 와이드 2~3, dedup: recent-papers.md)
   - T2 방법 분석(method-analyst, T1) → `vault/analysis/method-*`
   - T3 임상 분석(clinical-analyst, T1) → `vault/analysis/clinical-*`  ※ T2·T4와 병렬
   - T4 산업 분석(industry-analyst, T1) → `vault/analysis/industry-*`  ※ 병렬
   - T5 통합(digest-editor, T2·T3·T4) → `vault/digest/*` (NEWSLETTER-FORMAT 계약 준수)
   - **T5.5 문체 검수(style-critic, T5)** → `vault/digest/*` 윤문
   - **T5.7 사실 검증(claim-checker, T5.5)** → 수치 원문 대조·검증수준·preprint 표기 강제
   - T6 렌더(digest-renderer, T5.7) → `vault/html/*.html`, `vault/push/*` (`render_html.py` 실행)
   - T7 vault 정리(knowledge-curator, T5.7) → `vault/topics/*`, `recent-papers.md` 갱신
   - **T8(선택) 발제(study-brief-writer, T5.7)** → `vault/briefs/*` — 사람이 "발제" 요청 시 또는 매주 1편 제안
3. 팀원은 `TaskUpdate`로 진행/완료, `SendMessage`로 출처 보강 요청.
4. 각 산출물은 파일로 남긴다.

## 발행 정책
- 파일 생성(다이제스트·HTML·푸시·발제)은 자동.
- **외부 발송(텔레그램 채널 알림은 자동화 검토 / 블로그·리뷰·발제 외부 게시는 사람 승인 뒤)**. 절대 무단 게시하지 않는다.

## 마무리
- knowledge-curator까지 끝나면 `vault/_meta/improvement-log.md`에 주간 실행 메모(빠진 소스, 약했던 렌즈, 와이드 승격 후보).
- `TeamDelete`로 팀 정리.

## 산출물 계약
| 단계 | 파일 | 다음 단계가 읽음 |
| --- | --- | --- |
| 수집 | `vault/raw/papers-YYYY-Www.md` | 분석가 3명 |
| 분석 | `vault/analysis/{method|clinical|industry}-YYYY-Www.md` | 편집자 |
| 통합 | `vault/digest/YYYY-Www.md` | 검수·검증·렌더·큐레이터·발제 |
| 렌더 | `vault/html/*.html`, `vault/push/*.md` | 사람(읽기/발송) |
| 정리 | `vault/topics/*.md`, `recent-papers.md` | 다음 주 수집·3층 |
| 발제 | `vault/briefs/*.md` | 사람(스터디 발표) |

## 실패 시
- 한 단계 실패 시 그 단계만 재시도. 두 번 실패하면 사람에게 알리고 부분 산출물을 남긴다.
