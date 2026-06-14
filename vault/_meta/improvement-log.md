---
type: meta
---
# 개선 기록 (improvement-log)

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

## 2026-W24 (설계)
- 하네스 신규 설계 완료(econ-radar 자매). 첫 실행 전.
- 확정 방침: 주간 / 핵심축=바이오인포·임상ML·신약개발AI + 🔭와이드(자유선택) / 소스=프리프린트+PubMed·저널 / 3렌즈=방법·임상·산업 / 산출물=HTML+텔레그램+발제+vault.
- 첫 실행 후 점검할 것: 프리프린트 dedup(버전 업데이트·저널 전환), paywall 저널 접근, 렌즈별 분량 균형, 와이드가 핵심축을 침범하지 않는지, 발제 1편 선정 품질.
- econ-radar에서 이식한 미해결 교훈 선반영: MOC append-only 방지("현재 상태 요약" 상단 갱신), 이중 게이트, 결정적 렌더.
