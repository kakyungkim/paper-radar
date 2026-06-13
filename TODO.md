# TODO — paper-radar

## 바로 다음 (첫 가동)
- [ ] **첫 주간 실행** — `weekly-paper-digest-orchestrator`로 이번 주차 전체 파이프라인 1회. 산출물 보고 양식·렌즈 균형·dedup 점검.
- [ ] 첫 실행 다이제스트 구조를 기준으로 `scripts/NEWSLETTER-FORMAT.md` + `scripts/render_html.py` 확정(econ-radar 렌더 스크립트 이식).
- [ ] `vault/_meta/korean-style-samples.md` — 실제 한국어 과학·산업 리뷰 문장 표본 수집(현재 econ-radar 준용).
- [ ] `vault/_meta/benchmarks.md` — benchmark-scout로 본받을 논문 다이제스트 매체 조사.

## 자동화 (검증 후)
- [ ] 주간 클라우드 루틴 — 매주 1회(요일·시각 정하기, 예: 일 22:00 KST) 전체 파이프라인 자동 실행 → push → 텔레그램 알림. (econ-radar 루틴 패턴 재사용. 레포 private 전제.)
- [ ] econ-radar 텔레그램 채널 공유할지, paper-radar 전용 채널 팔지 결정.
- [ ] HTML 다이제스트 디자인(econ-radar template.html 톤 이식 — 논문 카드·검증 배지·preprint 배지).

## 설계 보강
- [ ] 🔭 와이드 단골 시드 분야 정할지(현재 자유 선택). 반복 등장 주제는 improvement-log에 승격 후보로.
- [ ] benchmark-scout·trend-synthesizer 에이전트 추가(econ-radar에서 이식).
- [ ] econ-radar ↔ paper-radar 교차 링크 규칙(산업 렌즈에서 상장사·딜 연결).
- [ ] 발제(study-brief-writer) 매주 자동 1편 제안 vs 사람 지정 — 운영해보고 결정.

## 열린 질문
- [ ] 핵심축 5편이 매주 충분히 나오나(분야 좁으면 격주 검토).
- [ ] paywall 저널 비중 — 프리프린트로 충분한지.
