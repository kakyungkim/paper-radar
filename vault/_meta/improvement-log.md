---
type: meta
---
# 개선 기록 (improvement-log)

## 2026-W26 (2026-06-28)
- 수집: 핵심 5편(임상ML×2, 신약AI×2, 유전체×2 중복 포함), 와이드 3편
- 분석: method/clinical/industry 3렌즈 완료
- 검수: style-critic 22건 수정, claim-checker 수정 1건(Robin 서브에이전트 역할 오기)
- 확인 불가: arXiv 직접 접근 차단으로 p=1.91×10⁻⁴² 수치 PDF 본문 직접 확인 불가
- 코드 공개율: 5편 중 2편(Stable-Shift, NYU LLM 비교) — W25 0/5 대비 회복
- 와이드 승격 후보: Robin(자율 과학 발견, Nature) — 신약AI 핵심 축 편입 검토
- 다음 주 주시: DeepBD 코드 공개 여부, 문헌마이닝 leakage 통제 후 OR 재추정 논문

## 2026-W25

- **빠진 소스·약했던 렌즈**
  - W25 핵심 5편 전부 코드 미공개(확인). W24 대비 재현성 방어선 더 약해짐. 코드 공개 우선 선별 기준 강화 검토.
  - scGTN 핵심 수치 미기재(초록 기준). paper-scout 수집 시 핵심 수치 없는 논문 하한선 기준 설정 필요.
  - 단백질 구조 논문 이번 주도 0편. q-bio.BM 쿼리 재검토 계속 필요.
- **코드 공개율**: 핵심 5편 중 0편 공개 (W24: 2/5)
- **다음 주 개선 제안**
  1. 코드 공개 논문이 0편일 경우 경고 표시 로직 추가 검토
  2. 와이드 CellVoyager(Nature Methods peer-reviewed)는 반복 등장 시 LLM-bio 핵심 축 승격 후보
  3. xCI + Tabular FM 공정성 조합 → 다음 주 임상 ML 공정성 발제 후보
- **와이드 승격 후보**: CellVoyager(AI 에이전트 자율 생물학 분석) — LLM-bio 축

## 2026-06-16 벤치마킹 후 개선 TODO

### ✅ 즉시 적용 (2026-06-16 완료)
- **선택 이유 1줄** (preLights) — 각 논문 카드에 "선택 이유" 필드 추가. digest-editor·NEWSLETTER-FORMAT 반영.
- **코드 공개 배지** (Papers with Code) — paper-scout 선별 기준 1순위에 코드 공개 논문 우선 추가. 미공개 시 `코드 미공개 — 재현 불가` 배지(빨강). render_html.py `.badge-nocode` 추가.
- **저자·기관 전 항목 명시** — digest-editor·NEWSLETTER-FORMAT에 `저자: 1저자, 교신저자 | 소속 기관` 필수 줄 추가.

### ✅ 2026-06-16 추가 적용 (TODO → 완료)
- **TODO-A 딥다이브 분리**: render_html.py에 `build_deepdive_push()` 추가 → `vault/push/YYYY-Www-deepdive.md` 생성. GitHub Actions에서 deepdive 파일 감지 후 별도 Telegram 메시지 발송.
- **TODO-B 사회적 신호**: paper-scout 소스에 HF Daily Papers 추가. raw 양식·NEWSLETTER-FORMAT에 `사회적 신호:` 필드 추가.
- **TODO-C preprint 추적**: knowledge-curator에 preprint→published 상태 추적 단계 추가. recent-papers.jsonl 스키마에 `status` 필드 추가.
- **TODO-D Q&A**: push 메시지 말미에 "💬 궁금한 점은 리플라이로 — 매월 Q&A 정리합니다." 추가.

### 📋 향후 검토 항목

**TODO-A: 와이드 + 딥다이브 발행 분리** (TheSequence 벤치마크)
- 현재: 매주 5편 와이드 단일 구조
- 목표: 주간 5편 짧게(250단어) + 격주 1편 집중(800~1,200단어) 두 레이어
- 딥다이브는 텔레그램 별도 포스트로 공지
- 작업 범위: CCR 프롬프트 수정 + NEWSLETTER-FORMAT 딥다이브 섹션 분리 발행 로직

**TODO-B: 사회적 신호 병기** (AlphaSignal 벤치마크)
- 각 항목에 "HuggingFace Daily Papers #N" 또는 "X 언급 XXX건" 1줄 추가
- paper-scout 소스에 AlphaSignal·HF Daily Papers 추가
- 작업 범위: paper-scout.md 소스 목록 + 논문 카드 양식

**TODO-C: preprint → 출판 후 변경 추적** (preLights postLights 벤치마크)
- 선정 논문이 동료심사 통과 후 수치·주장이 달라지면 텔레그램 단독 포스트 발행
- 작업 범위: recent-papers.jsonl에 `status` 필드 추가(preprint/published) + 주간 루틴에 상태 체크 단계 추가

**TODO-D: 독자 Q&A 루프** (preLights 저자 응답 벤치마크)
- 텔레그램 포스트 말미에 "리플라이로 질문" 유도 문구 추가
- 월 1회 "독자 질문 답변" 이슈 별도 발행
- 작업 범위: send_push.py 템플릿 + CCR 월간 루틴 신설 여부 검토

하네스를 실제로 돌린 뒤 빠진 소스, 약했던 렌즈, 고칠 점, 와이드 승격 후보를 여기에 남긴다. 다음 개선의 근거다.

## 양식
```
## YYYY-Www
- 무엇이: (예: arXiv q-bio 신착에서 단백질 구조 논문 누락)
- 왜: (검색 누락 / 소스 미포함 / 렌즈 약함)
- 어떻게 고칠지: (paper-scout 소스 목록 보강 등)
- 와이드 승격 후보: (반복 등장 주제)
```

## 2026-06-14 (W24 첫 실행)
- **빠진 소스·약했던 렌즈**
  - 저자 소속 미기재 비율 높음 — 9편 중 대부분 소속 불명. paper-scout가 arXiv 초록에서 소속 파싱을 시도했으나 기재 안 된 경우가 많았다. 향후 Semantic Scholar API로 소속 보강 검토.
  - Nature/Cell 등 유료 저널 접근 미흡 — 이번 주 1편(Nature Biomedical Engineering) 포함됐으나 본문 접근 불가, 초록 기반 요약에 그쳤다. 기관 접근 또는 PubMed Central 오픈 아카이빙 여부 우선 확인 루틴 추가 필요.
  - 단백질 구조 주제 0편 — 이번 주 arXiv에서 AlphaFold/ESMFold 계열 논문이 없지는 않았을 것이나 검색 쿼리에 포착되지 않음. `q-bio.BM` 쿼리 폭 재검토.
- **코드 미공개 논문 수**: 핵심 5편 중 3편 미공개(m6A-FORM, OCOO-T, ADME 대조 사전학습). 재현성 방어선 약함.
- **다음 주 개선 제안**
  1. paper-scout 쿼리에 `q-bio.BM` + `protein structure` + `fold` 추가해 단백질 주제 공백 메우기.
  2. 코드 공개 여부를 핵심 선별 기준 중 하나로 명시(동점 시 공개 우선).
  3. 소속 파싱: Semantic Scholar `/paper` 엔드포인트로 arXiv ID 조회 → `authors[].affiliations` 필드 보강.
  4. 와이드 4편 중 Virtual Biotech(멀티에이전트 AI)와 OmniBioTwin(디지털 트윈)은 반복 등장 가능성 높음 — 신약AI MOC와 임상ML MOC에 포함 후 다음 주 등장 시 핵심 승격 검토.

## 2026-06-15 (benchmarks.md 품질 기준선 도입)
- **변경 내용**: BRIC 한빛사·사이언스타임즈·Import AI·Asimov Press·The Batch·Owl Posting·HuggingFace Daily Papers 7개 매체 실조사 → `vault/_meta/benchmarks.md` 신규. "바로 반영할 체크리스트" 7항목 + "깊이 장치" 표 + 안티패턴 목록 도출.
- **하네스 반영**:
  - `digest-editor`: "품질 기준선" 섹션 추가 — benchmarks.md 체크리스트 7항목 의무 대조, 깊이 장치 2~3개 선택 적용.
  - `style-critic`: 0순위에 benchmarks.md "하지 말아야 할 것" 추가 — korean-style-samples.md(문체) + benchmarks.md(안티패턴) 이중 체크.
  - `method-analyst`: 깊이 장치 참조 추가 (메커니즘 핵심 가정·문제의식 선행·기존 한계→해결).
  - `clinical-analyst`: 깊이 장치 참조 추가 (수요 렌즈·기존 한계→해결·검증 수준).
  - `industry-analyst`: 깊이 장치 참조 추가 (수요 렌즈·역사적 맥락·화제성 신호).
- **동기**: 논문 해설 문체가 경제지 문체와 달리 "초록 번역" 함정에 빠지기 쉬움. BRIC 한빛사("문제의식 선행"), Import AI("Why it matters 고정 장치")를 각 에이전트에 맞게 이식.

## 2026-W24 (설계)
- 하네스 신규 설계 완료(econ-radar 자매). 첫 실행 전.
- 확정 방침: 주간 / 핵심축=바이오인포·임상ML·신약개발AI + 🔭와이드(자유선택) / 소스=프리프린트+PubMed·저널 / 3렌즈=방법·임상·산업 / 산출물=HTML+텔레그램+발제+vault.
- 첫 실행 후 점검할 것: 프리프린트 dedup(버전 업데이트·저널 전환), paywall 저널 접근, 렌즈별 분량 균형, 와이드가 핵심축을 침범하지 않는지, 발제 1편 선정 품질.
- econ-radar에서 이식한 미해결 교훈 선반영: MOC append-only 방지("현재 상태 요약" 상단 갱신), 이중 게이트, 결정적 렌더.
