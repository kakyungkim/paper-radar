---
type: moc
tags: [신약AI]
---
## 2026-W42 핵심 흐름
W42 신약AI는 AlphaFold 신뢰도 점수의 계면 품질 보정이 핵심이다. pLDDT·iPTM 같은 기존 신뢰도 지표가 단백질 복합체 계면 품질을 체계적으로 오평가함을 규명하고 보정 방법을 제시한 논문(arXiv:2610.17108)은 AlphaFold2/3가 신약 타깃-리간드 계면 예측 파이프라인의 사실상 표준이 된 상황에서 실용적 인프라 수준의 기여다. 코드·데이터 공개 미확인(프리프린트). 와이드의 조건부 플로우 모델(arXiv:2610.20288)은 미관측 약물-표적 상호작용 예측 맥락에서 재등장해 신약 발굴 축 승격 후보로 주목된다. W41의 인과 추론 타깃 발굴에서 W42는 구조 예측 도구의 신뢰도 보정이라는 실용 인프라 방향으로 이동한다.
[[papers-2026-W42]] | [[2026-W42]]

---
# 🗂 신약AI — 주제 지도(MOC)

## 핵심 흐름
(2026-W36 기준) W36 신약AI는 RNA 전달 기술의 합성생물학적 재설계와 소분자 약물-표적 상호작용(DTI) 예측 방법론의 다중 척도 정밀화가 두 축이다. Schuhmacher 외(Nature, DOI:10.1038/s41586-026-10952-3)의 STV-C8은 AI 설계 합성 단백질로 구성한 RNA 전달 비히클(RNA transfer vehicle)이 in vivo 마우스에서 기능적 mRNA를 세포 내로 전달함을 보이며, LNP(지질나노입자) 기반 전달의 대안 경로를 실증했다. Nature peer-reviewed 완전 검증 논문이며 신약개발 산업 관점에서 mRNA 치료제 모달리티 다각화에 직결된다. Hao 외(arXiv:2609.02549)의 ProbeMatchDTI는 탐침(probe) 기반 다중 척도 생화학 패턴 매칭으로 DTI 예측에서 약한 결합 신호(weak interaction)를 보존하는 설계를 제시하며, BindingDB AUC 기준 기존 대비 +2.0%(초록 기준)를 보고한다. W35의 제조 최적화·아키텍처 혁신에서 W36은 전달 플랫폼 다각화와 DTI 정밀도 향상으로 이동한다.

(이전) W35 기준 mRNA 치료제 제조 병목 해결(Zheng 외, IVT RNA 수율 예측 r=0.94)과 Mol-JEPA 분자 JEPA 아키텍처(Boehringer Ingelheim 공동)가 핵심이었다.

## 타임라인
### 2026-W42 (2026-10-12~2026-10-18)
- 2026-W42 | [[alphafold-interface-calib-2026-W42]] Calibrating AlphaFold confidence scores for interface quality — AlphaFold pLDDT·iPTM의 계면 품질 체계적 편향 보정 ([arXiv](https://arxiv.org/abs/2610.17108))
  - 핵심: 기존 신뢰도 점수가 복합체 계면 품질을 과대·과소 평가하는 패턴 규명; 보정 레이어 제안; 신약 타깃-리간드 도킹 파이프라인의 실용 인프라 기여
  - 검증: 추정 in silico (초록 미확인); preprint

### 2026-W41 (2026-10-05~2026-10-11)
- [[causalbind-2026-W41]] — CausalBind: 교차-어텐션+희소 마스킹 플러그인으로 가상 스크리닝 허위 상관 제거, LIT-PCBA BEDROC·EF@1% 개선, ICLR 2026 채택 ([arXiv](https://arxiv.org/abs/2610.07340))
  - 핵심: 결합에 인과적으로 관여하는 원자 개념만 분리하는 플러그인 구조; 새 표적(unseen target) 일반화 병목 직접 공략
  - 검증: in silico (LIT-PCBA 벤치마크); 코드 미공개
- [[entropy-reverse-causal-ad-2026-W41]] — 알츠하이머 역인과 AI: 엔트로피 유도 병목 선별+역인과 추적으로 AD 상류 타깃 발굴 ([arXiv](https://arxiv.org/abs/2610.08736))
  - 핵심: 하류 병리 표현형에서 원인 방향을 역추적; 아밀로이드 하류 전략 실패 이후 상류 타깃 전환 신호
  - 검증: 추정 in silico (초록 미확인); preprint
- [[cross-species-neural-dynamics-2026-W41]] — 교차 종 신경 역학 정렬: 마우스-인간 신경 신호 공동 잠재 공간 정렬로 임상 약효 소급 추적 ([arXiv](https://arxiv.org/abs/2610.11222))
  - 핵심: 전임상-임상 번역 실패 공략; 전향 예측 검증 없으면 현재 임상 함의 제한
  - 검증: 추정 in silico/후향 (초록 미확인); preprint

### 2026-W40 (2026-09-28~2026-10-04)
- [[dti-cross-attention-2026-W40]] — 화학·단백질 언어 모델 위계적 순차 교차 어텐션으로 DTI 예측 ([arXiv](https://arxiv.org/abs/2609.34921))
  - 핵심: SMILES 기반 화학 LM과 단백질 LM을 교차 어텐션으로 융합, 분자-서열 이중 계층 표현 학습
  - 검증: in silico
- [[struct-rl-directed-evo-2026-W40]] — 단백질 지향 진화에 구조 인식 강화학습 적용 ([arXiv](https://arxiv.org/abs/2609.39048))
  - 핵심: RL 탐색 시 단백질 3차 구조 정보를 함께 인코딩해 기능 향상 돌연변이 탐색 효율화
  - 검증: in silico

### 2026-W39 (2026-09-21~09-27)
- [[MIRCID]] — 허브 miRNA 네트워크 추론 기반 약물 기전 모델링 교차 태스크 개선, 조절망 공유 표현 학습 (arXiv:2609.21280) [preprint]

### 2026-W38 (2026-09-14~09-20)
- [[면역-월드-모델]] — 면역 다층위 동학 통합 월드 모델, 다중 인체 조직 세포 상태 예측 + 치료 가설 생성 내장 (arXiv:2609.14709) [preprint]
- [[EHR-약물재창출]] — EHR 사전학습 표현으로 약물 재창출 후보 실용적 스크리닝, 대형 인프라 불필요한 데이터 효율 접근 (arXiv:2609.19865) [preprint]

### 2026-W36 (2026-08-31~09-06)
- [[STV-C8]] — AI 설계 합성 단백질 RNA 전달 비히클, in vivo 마우스 전임상 검증, LNP 대안 경로 실증 (DOI:10.1038/s41586-026-10952-3) [peer-reviewed]
- [[ProbeMatchDTI]] — 탐침 기반 다중 척도 DTI 예측, 약한 결합 신호 보존, BindingDB AUC +2.0%(초록 기준), 코드 공개 (arXiv:2609.02549) [preprint]

### 2026-W35 (2026-08-24~08-30)
- [[mRNA 수율 DNN 최적화]] — 대규모 병렬 스크리닝+CNN으로 IVT RNA 생산량 예측(r=0.94), mRNA 제조 병목 해결 (arXiv:2608.23722) [preprint]
- [[Mol-JEPA]] — JEPA 프레임워크로 분자 14+ 모달리티 통합 표현 학습, Boehringer Ingelheim 공동, 신약 설계 벤치마크 다수 성능 보고 (arXiv:2608.22642) [preprint]

### 2026-W33 (2026-08-10~08-16)
- [[2026-W33]] — RetFold/DRR(Xu 외): 검색 증강 단백질 구조 생성의 신규성 한계 실증, 구조 AI 평가 관행 재정의 (arXiv:2608.10598) [preprint]
- [[2026-W33]] — IMPROVE DRP(Lavelle 외): 항암제 반응 모델링용 대규모 AI 표준 데이터 인프라 제시, CANDLE/IMPROVE 프레임워크 (arXiv:2608.11444) [preprint]
- [[2026-W33]] — LEN-Seek(Yeo 외): SE(3)-불변 그래프 VAE 잠재공간 기반 결합부위 유사성 고속 대규모 검색 (DOI:10.64898/2026.08.14.744759) [preprint]

### 2026-W32 (2026-08-03~08-09)
- [[2026-W32]] — 세포 표현형→분자 표현(Lin 외): 형태학적 세포 표현형에서 구조 보존형 분자 표현 학습, 표현형 스크리닝 데이터 신약 설계 연결 (arXiv:2608.02688) [preprint]
- [[2026-W32]] — THBKG(Siu 외, Recursion Pharmaceuticals 공동): 시간 정렬 생물의학 KG로 임상 진전 예측, 최초 시간 정렬 KG 구현 (arXiv:2608.05982) [preprint]
- [[2026-W32]] — EpiBench(Wang 외): 에피토프 이해 LLM 비교 첫 벤치마크, 항체 신약 개발 역량 평가 (arXiv:2608.06022) [preprint]

### 2026-W31 (2026-07-27~08-02)
- [[2026-W31]] — Vilya-2: 비정규 잔기·거대고리 펩타이드-단백질 계면 확산 트랜스포머, 59.1% sub-2Å 회복(초록 기준) (arXiv:2607.25156) [preprint]
- [[2026-W31]] — PMRD: 화학 구조·유전자 발현·세포 형태 3모달 도메인 분리 제로샷 약물 표현, KDD 2026 (arXiv:2607.25322) [preprint]
- [[2026-W31]] — SCTA: scRNA-seq 에이전트 표적 발굴 교차 실행 안정성, BioKDD 2026 (arXiv:2607.23821) [preprint]
- [[2026-W31]] — Q-Steer: 분자 LM 지연 피드백 PAVS-Q 추론-시점 조향 (와이드) (arXiv:2607.26391) [preprint]

### 2026-W30 (2026-07-26)
- [[2026-W30]] — RELIABLE-BA 신뢰도 인식 다중엔진 결합 친화도 예측 (arXiv:2607.17601) [preprint]
- [[2026-W30]] — LLM vs SBDD 공간 제약 벤치마크 (arXiv:2607.18144) [preprint]

### 2026-W29 (2026-07-14~19)
- [[Corgi-Corgi+]] (DOI:10.1038/s41467-026-75527-2) — 맥락 인식 서열-기능 모델, 인간 유전자 조절 예측으로 기능유전체 타깃 발굴 정밀화, Nature Communications [peer-reviewed]
- [[LATTICE]] (arXiv:2607.14410) — 공간 멀티오믹스 그래프 자기지도학습, TME 세포 상호작용 지도 → 면역 항암제 반응 바이오마커 [preprint]

### 2026-W28
- **2026-W28** — PREDIKTOR (arXiv:2607.04557): DysRegNet+LINCS L1000 CLIP 정렬, 정밀종양학 약물 반응 예측 [[2026-W28]]

### 2026-W27
- **Active-GRPO: GRPO 기반 분자 최적화 자기 개선 추론(Liu 외)** — GRPO 강화학습으로 LLM 적응형 모방 학습과 자기 개선 추론을 분자 최적화에 적용. 코드 미공개. 미동료심사(preprint). 출처: [[digest/2026-W27]] | arXiv:2607.00531
- **MLP-GNN 수용해도 예측 프레임워크(Bhattacharya 외)** — 화학적(MLP) + 구조적(GNN) 기여를 분리하는 가산 프레임워크로 수상 용해도(aqueous solubility) 예측. ADME 해석 가능성 향상. 미동료심사(preprint). 출처: [[digest/2026-W27]] | arXiv:2607.02212

### 2026-W26
- **유전 증거-신약 승인 연관성(Paterson 외)** — 26,278개 타깃-질환 쌍 관찰 분석. 시간 검증·변수 제거 포함. 유전 증거 보유 타깃의 승인률 우위 정량화. 미동료심사(preprint). 출처: [[digest/2026-W26]] | arXiv:2606.14823
- **Molexar: 멀티모달 분자 파운데이션 모델(Lin 외)** — 그래프·SMILES·3D 구조 통합 unified 모델. 신약 설계(분자 생성+특성 예측) 단일 아키텍처. 미동료심사(preprint). 출처: [[digest/2026-W26]] | arXiv:2606.25865

### 2026-W25
- **멀티모달 암 FM 벤치마킹(Hu 외, 간접 연관)** — WSI+전사체 결합. 암 진단 AI 배포 한계 실증. 타깃 발굴·환자 선별 파이프라인 설계에 시사점. 출처: [[digest/2026-W25]] | arXiv:2606.17115

### 2026-W24
- **GLACIER** — 분자 그래프·SMILES·물리화학 기술자를 학생-교사 지식 증류로 통합한 분자 특성 예측 파운데이션 모델. Biogen +7.6%, ExpansionRX +9.9%, ChEMBL-MT +9.5% (vs KERMT). 코드 공개(github.com/eemokey/glacier). 출처: [[digest/2026-W24]]
- **확률론적 대조 사전학습 ADME 예측기** — 재건·대조·화학 작업을 단일 확률론적 잠재 변수 목적함수로 통합. 동일 벤치마크 동일 수준 성능. 음전이 완화 설계 포함. 코드 미공개. 출처: [[digest/2026-W24]]
- **가상 바이오텍(Virtual Biotech)** — 다중에이전트 AI 프레임워크. 5만 5,984개 임상시험 자율 분석. 세포 유형 특이 유전자 표적 약물 Ph I→II 전환율 +40%, 출시 확률 +48%, 부작용 -32%. bioRxiv(미동료심사). 출처: [[digest/2026-W24]]
