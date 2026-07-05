---
type: moc
tags: [LLM-bio]
---
# 🗂 LLM-bio — 주제 지도(MOC)

## 핵심 흐름
(2026-W27 기준) Affinage(MIT)가 PubMed 문헌 전체에서 기계적 유전자 기능 주석을 추출하는 LLM 파이프라인을 코드·API 공개와 함께 발표했다. 바이오 도메인 LLM의 실용 배포 수준을 한 단계 높인 사례로, W25 CellVoyager(자율 분석)·W26 BioHarness(증거 조립)에 이은 생물학 에이전트 LLM 흐름이 지속된다. Active-GRPO는 GRPO 강화학습을 분자 최적화 LLM에 이식해 자기 개선 추론 패턴을 신약 설계에 연결했다. 자율과학 AI(DiscoPER, W27 와이드)가 W26 Robin에 이어 2주 연속 등장했다. 코드 공개는 W27에서 Affinage 1편으로, 재현성 기준은 여전히 약하다.

## 타임라인
### 2026-W27
- **Affinage: LLM 기반 전장 유전체 기계적 유전자 주석(Di Bernardo 외, MIT)** — PubMed 문헌 전체에서 LLM으로 기계적 유전자 기능 주석 자동화. 게놈 스케일 문헌 마이닝. 코드·API 공개. 미동료심사(preprint). 출처: [[digest/2026-W27]] | arXiv:2607.02217
- **Active-GRPO: GRPO 기반 분자 최적화 LLM(Liu 외)** — GRPO 강화학습으로 LLM 자기 개선 추론을 분자 최적화에 적용. 코드 미공개. 미동료심사(preprint). 출처: [[digest/2026-W27]] | arXiv:2607.00531

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
