---
type: moc
tags: [LLM-bio]
---
# 🗂 LLM-bio — 주제 지도(MOC)

## 핵심 흐름
(2026-W26 기준) 범용 LLM이 임상 벤치마크에서 특화 AI를 능가한다는 동료심사 결과가 나오면서(Vishwanath 외, Nature Medicine), "특화 모델 = 우월"이라는 통념이 흔들리기 시작했다. 동시에 Molexar처럼 분자 그래프·SMILES·3D 구조를 하나의 파운데이션 모델로 통합하는 multimodal unification 흐름이 신약 설계 영역에서 강해지고 있다. W25의 에이전트 자율 생물학 분석(CellVoyager)과 임상 LLM 실패 실증(Basu)에 이어, W26에서는 "범용 vs 특화" 구도와 "멀티모달 통합 설계"가 핵심 쟁점이다. 코드 공개율은 W26에서 2/5(Stable-Shift, NYU LLM 비교)로 소폭 회복됐다. Robin(자율 과학 발견, Nature) 와이드 논문이 반복 등장할 경우 핵심 축 승격 대상이다.

## 타임라인
### 2026-W26
- **범용 LLM vs 임상 특화 AI(Vishwanath 외, NYU)** — 범용 LLM이 의료 벤치마크에서 임상 특화 도구를 전반적으로 능가. Nature Medicine 동료심사 게재. 코드 공개. 출처: [[digest/2026-W26]] | DOI:10.1038/s41591-026-04431-5
- **Molexar: 멀티모달 분자 파운데이션 모델(Lin 외)** — 분자 그래프·SMILES·3D 구조 통합 unified 아키텍처. 신약 설계 전 단계 지원. 미동료심사(preprint). 출처: [[digest/2026-W26]] | arXiv:2606.25865

### 2026-W25
- **EHR 추론 실패 실증(Basu, UCSF)** — hop=1~4 단계에서 Claude Sonnet·GPT-4o·GPT-5 모두 단조 정확도 감소. 임상 LLM 안전성 평가 지표 제시. 코드 미공개. 출처: [[digest/2026-W25]] | arXiv:2606.16890
- **Tabular FM 생존 분석 적응(Pham 외)** — TabDPT-FT-MTLR, MIMIC-IV C-지수 0.856. AIiH 2026 게재 확정. 코드 미공개. 출처: [[digest/2026-W25]] | arXiv:2606.12006
- **scGTN(Wu 외)** — 샴 그래프 트랜스포머 scRNA-seq 클러스터링. 코드 미공개(URL 예고). 출처: [[digest/2026-W25]] | arXiv:2606.18672
- **멀티모달 암 FM 벤치마킹(Hu 외)** — WSI+전사체 8개 과제, 실제 상업 코호트 분포 이동 취약성 평가. 코드 미공개. 출처: [[digest/2026-W25]] | arXiv:2606.17115
- **CellVoyager(와이드, Alber 외)** — LLM 에이전트 자율 scRNA-seq 분석. GPT-4o·o3-mini 대비 최대 +23% 예측 정확도. Nature Methods 동료심사 게재. 출처: [[digest/2026-W25]] | DOI:10.1038/s41592-026-03029-6

### 2026-W24
- **m6A-FORM** — RNA 메틸화 파운데이션 모델. 143개 연구 2,200만 서열 사전학습, PR-AUC 0.635. 코드 미공개. 출처: [[digest/2026-W24]]
- **OCOO-T** — 흐름 매칭 기반 가상 세포 트랜스포머. 유전·화학·사이토카인 교란 반응 예측. 코드 미공개. 출처: [[digest/2026-W24]]
- **GLACIER** — 멀티모달 분자 파운데이션 모델(그래프+SMILES+기술자). 학생-교사 지식 증류. 코드 공개. 출처: [[digest/2026-W24]]
