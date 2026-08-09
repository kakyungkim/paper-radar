---
type: moc
tags: [임상ML]
---
# 🗂 임상ML — 주제 지도(MOC)

## 핵심 흐름
(2026-W32 기준) W32 임상ML은 방법론 비판과 대규모 비큐레이션 파운데이션 모델이 동시에 등장한 주차다. Yadav 외(arXiv:2608.04046, MLHC 2026)는 생존 분석 결과를 이진화할 때 발생하는 정보 손실을 정량화해, 시간-사건 모델(time-to-event model)이 표준이 돼야 함을 peer-reviewed 논문으로 실증했다. THBKG(Siu 외, arXiv:2608.05982, Recursion Pharmaceuticals 공동)는 시간 정렬 생물의학 지식 그래프(knowledge graph, KG)를 임상 진전 예측에 적용한 최초 구현이다. NeuroVFM(Kondepudi 외, DOI:10.1038/s41591-026-04497-1, Nature Medicine)은 524만 건 비큐레이션 뇌 MRI에서 신경영상 파운데이션 모델을 학습해 다운스트림 임상 과제에 검증됐다. W31의 다중모달 EHR FM 흐름에서, W32는 방법론 관행 비판과 비큐레이션 스케일링이라는 두 방향이 명확해진 주차다.

(이전) W31 기준 자기회귀 EHR FM(arXiv:2607.22264, Imperial College London, ICML 2026 워크숍)은 구조화 EHR 코드에 ECG·흉부 X선·임상 노트를 게이트 교차 어텐션으로 통합하는 최초 체계적 비교 연구로, MIMIC-IV 후향 검증을 제시했다. W30의 의료 AI 에이전트 불확실성 정량화(UQ) 흐름에서 W31은 입력 모달리티 확장이라는 보완적 방향을 추가했다. 두 방향 모두 임상 AI 신뢰성을 높이는 구조적 흐름이다.

## 타임라인
### 2026-W32 (2026-08-03~08-09)
- [[2026-W32]] — 생존 이진화 비용(Yadav 외): 생존 결과 이진화가 초래하는 정보 손실 정량화, 시간-사건 모델 우위 peer-reviewed 실증, MLHC 2026 (arXiv:2608.04046) [preprint]
- [[2026-W32]] — THBKG(Siu 외, Recursion Pharmaceuticals 공동): 시간 정렬 생물의학 KG로 임상 진전 예측, 최초 시간 정렬 KG 구현 (arXiv:2608.05982) [preprint]
- [[2026-W32]] — NeuroVFM(Kondepudi 외): 524만 건 비큐레이션 뇌 MRI 학습 신경영상 파운데이션 모델, 다운스트림 임상 과제 검증 (DOI:10.1038/s41591-026-04497-1) [published]

### 2026-W31 (2026-07-27~08-02)
- [[2026-W31]] — EHR FM: 자기회귀 EHR 파운데이션 모델에 ECG·CXR·임상 노트 게이트 교차 어텐션 통합, MIMIC-IV 후향 검증, ICML 2026 워크숍 (arXiv:2607.22264) [preprint]

### 2026-W30 (2026-07-26)
- [[2026-W30]] — 베이즈 불확실성 추정 의료 AI 에이전트 (arXiv:2607.20582) [preprint]

### 2026-W29 (2026-07-14~19)
- [[Evo2-Probes]] (arXiv:2607.14070) — Evo 2 게놈 언어 모델 프로브로 메타게노믹스 AMR·바이오시큐리티 기능 스크리닝, 감염병 모니터링 임상 관련성 [preprint]

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
