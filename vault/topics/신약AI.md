---
type: moc
tags: [신약AI]
---
# 🗂 신약AI — 주제 지도(MOC)

## 핵심 흐름
(2026-W28 기준) PREDIKTOR(arXiv:2607.04557)가 DysRegNet 환자 조절망과 LINCS L1000 교란 표현을 CLIP으로 정렬해 I-SPY2 유방암 코호트에서 약물 반응 제로샷 예측을 시연했다. 환자 개인화 지식 그래프와 유전자 수준 교란 데이터를 결합한 정밀종양학(precision oncology) 접근법으로, 타깃-환자 매핑 단계를 강화한다. W27의 분자 최적화(Active-GRPO, RL 기반)·ADME 예측(MLP-GNN)에 이어, W28에서는 임상시험 약물 반응 예측으로 초점이 이동했다. MolBasic(와이드, arXiv:2607.03007)은 SMILES-그래프 상호 번역으로 분자 LLM의 구조 이해를 강화한다. 자율과학 AI 에이전트 흐름(W26 Robin, W27 DiscoPER 2주 연속)은 W28에서 미등장으로 소강 상태다.

## 타임라인
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
