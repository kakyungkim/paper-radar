---
type: moc
tags: [임상ML]
---
# 🗂 임상ML — 주제 지도(MOC)

## 핵심 흐름
(2026-W28 기준) PREDIKTOR(arXiv:2607.04557)는 환자별 조절망(DysRegNet)과 LINCS L1000 약물 교란 표현을 CLIP 방식으로 정렬해 I-SPY2 유방암 임상시험 코호트에서 제로샷 약물 반응 예측 AUROC +5.6%를 보고했다. 환자 개인화 지식 그래프를 약물 반응 예측에 결합한 아키텍처로, 실제 임상시험 코호트를 외부 검증 대상으로 삼았다는 점이 in silico 평가와 차별화된다. W27 CNS 종양 분류기 후향 검증(N=1,104)에 이어 임상 근접 검증이 이어지고, W28에서는 제로샷 약물 반응 예측이 새 초점이다. Causal ASCEND(arXiv:2607.04527)는 멀티오믹스 고차원 데이터의 인과 구조 발견으로 임상 연구 설계를 뒷받침한다. 전체 흐름은 in silico 평가에서 실제 코호트 검증으로 이동 중이다.

## 타임라인
### 2026-W28
- **2026-W28** — PREDIKTOR (arXiv:2607.04557): 환자별 조절망+교란 정렬로 I-SPY2 제로샷 AUROC +5.6% [[2026-W28]]

### 2026-W27
- **CNS 종양 DNA 메틸화 분류기(Ferreira 외)** — 새로운 ML 접근법으로 DNA 메틸화에서 CNS 종양 분류. 독립 코호트 N=1,104 후향 검증. 코드 미공개. 미동료심사(preprint). 출처: [[digest/2026-W27]] | arXiv:2607.01307

### 2026-W26
- **범용 LLM vs 임상 특화 AI(Vishwanath 외, NYU)** — GPT-4o 등 범용 LLM이 다수 의료 벤치마크에서 임상 특화 AI 도구 전반을 능가. Nature Medicine 동료심사 게재. 코드 공개. 출처: [[digest/2026-W26]] | DOI:10.1038/s41591-026-04431-5
- **DeepBD: 선천성 유전 결함 변이 진단 에이전트(Li 외)** — 그라운딩된 에이전트 워크플로우로 변이 우선순위 결정 및 희귀질환 진단 자동화. 미동료심사(preprint). 출처: [[digest/2026-W26]] | arXiv:2606.24779

### 2026-W25
- **EHR 추론 실패 실증(Basu, UCSF)** — MedAlign 313개 질의에서 Claude Sonnet hop=1 정확도 30.6% → hop=4 17.6% 단조 감소. GPT-4o·GPT-5 동일 패턴 확인. 임상 LLM 안전성 벤치마크로 즉시 활용 가능. 코드 미공개. 출처: [[digest/2026-W25]] | arXiv:2606.16890
- **xCI: 그룹 조건부 C-지수(Wang 외)** — Harrell C-지수 그룹 조건부 확장. Framingham·MESA·ARIC·Truveta EHR에서 심혈관 위험 모델 집단 편향 감지. 공정성 규제 심사 직결. 코드 미공개. 출처: [[digest/2026-W25]] | arXiv:2606.16872
- **Tabular FM 생존 분석 적응(Pham 외)** — TabPFN·TabDPT·TabICL + MTLR 헤드. MIMIC-IV C-지수 0.856(DeepSurv +1.4%), eICU 0.797. AIiH 2026 게재 확정. 코드 미공개. 출처: [[digest/2026-W25]] | arXiv:2606.12006
- **멀티모달 암 FM 벤치마킹(Hu 외)** — WSI+전사체 8개 분류 과제. 실제 상업 코호트(IH-BC, IH-NSCLC)에서 분포 이동 하 일반화·신뢰성 평가. 코드 미공개. 출처: [[digest/2026-W25]] | arXiv:2606.17115

### 2026-W24
- **Span ctDNA 변화점 검출기** — 비검출 ctDNA를 censored 관측으로 처리하는 베이지안 잠재 성장 모델. 합성 시나리오 조기 검출률 2배 향상(25% vs 11%). 코드 공개(github.com/span-ai-labs/span-detector). 출처: [[digest/2026-W24]]
- **병리 파운데이션 모델 재고** — Nature Biomedical Engineering 논평. 자연 이미지 기반 모델의 조직 형태 부적합성 주장, 병리 전용 아키텍처 필요성 제기. 출처: [[digest/2026-W24]]
