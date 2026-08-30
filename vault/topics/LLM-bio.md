---
type: moc
tags: [LLM-bio]
---
# 🗂 LLM-bio — 주제 지도(MOC)

## 핵심 흐름
(2026-W35 기준) W35 LLM-bio는 분자 멀티모달 파운데이션 모델의 아키텍처 혁신과 공간 전사체 파운데이션 모델의 확장이 핵심이다. Rottach 외(arXiv:2608.22642)의 Mol-JEPA는 JEPA(Joint Embedding Predictive Architecture) 프레임워크를 분자 표현에 처음 도입해, 기존 대조 학습 방식에서 문제가 됐던 모달리티 붕괴(modality collapse)와 화학적으로 비유효한 증강(augmentation) 문제를 원리적으로 회피한다. Boehringer Ingelheim 공동 연구로 제약산업 직결 적용이 가시화된다. Xiao 외(arXiv:2608.26208)의 GITIII-scale은 팬-암 공간 전사체와 scRNA-seq를 통합하는 계층적 그래프 트랜스포머 파운데이션 모델로, TME(종양 미세환경) 세포 상태-니치 표현 학습에 특화된다. W32의 스케일링·신호 추출·진단에서 W35는 분자 표현 아키텍처 혁신과 다중 오믹스 파운데이션 모델 확장으로 이동한다.

(이전) W32 기준 단일세포 생성 AR 트랜스포머 스케일링(Sharipov 외)과 세포 표현형-분자 표현 연결(Lin 외), EpiBench 항체 LLM 평가, 유전체 LM 표현 진단(Datta 외) 4편이 스케일링·신호 추출·평가 세 방향으로 분화됐다.

## 타임라인
### 2026-W35 (2026-08-24~08-30)
- [[Mol-JEPA]] — JEPA 프레임워크 분자 도메인 최초 적용, 14+ 모달리티 마스킹 통합 학습, Boehringer Ingelheim 공동 (arXiv:2608.22642) [preprint] — 참조: [[신약AI#2026-W35]]
- [[GITIII-scale TME]] — 팬-암 공간 전사체+scRNA-seq 계층적 그래프 트랜스포머, 세포 상태-니치 표현 파운데이션 모델 (방법 교차) (arXiv:2608.26208) [preprint] — 참조: [[유전체#2026-W35]]

### 2026-W32 (2026-08-03~08-09)
- [[2026-W32]] — 단일세포 생성 AR 트랜스포머 스케일링(Sharipov 외): 자기회귀 트랜스포머를 단일세포 생성에 스케일업, 세포 생성 스케일링 법칙 탐색 (arXiv:2608.02961) [preprint]
- [[2026-W32]] — 세포 표현형→분자 표현(Lin 외): 형태학적 세포 표현형에서 구조 보존형 분자 표현 학습, 표현형 데이터-신약 설계 공간 연결 (arXiv:2608.02688) [preprint]
- [[2026-W32]] — EpiBench(Wang 외): 에피토프 이해 LLM 비교 첫 벤치마크, 항체 신약 개발 LLM 역량 평가 (arXiv:2608.06022) [preprint]
- [[2026-W32]] — 유전체 LM 표현 접근성 진단(Datta 외): frozen 유전체 언어 모델 레이어별 표현 활용 가능성 실증 (와이드) (arXiv:2608.05329) [preprint]

### 2026-W31 (2026-07-27~08-02)
- [[2026-W31]] — CENO: 게놈 스케일 세계 모델, Mamba/Attention/MoE + MSA 사후 훈련, 코드 완전 공개 (DOI:10.64898/2026.07.28.741284) [preprint]
- [[2026-W31]] — PMRD: 다중모달 제로샷 약물 표현, 기전-노이즈 도메인 분리, KDD 2026 (arXiv:2607.25322) [preprint]
- [[2026-W31]] — EHR FM: 자기회귀 EHR FM에 ECG·CXR·노트 게이트 교차 어텐션 통합, ICML 2026 워크숍 (arXiv:2607.22264) [preprint]
- [[2026-W31]] — FEV 프레임워크: 에이전트 바이오인포매틱스 109개 시스템 Function·Evidence·Validation 평가 (와이드) (arXiv:2607.27556) [preprint]

### 2026-W30 (2026-07-26)
- [[2026-W30]] — 단일세포·공간 전사체 파운데이션 모델 조화 벤치마크 (arXiv:2607.17227) [preprint]
- [[2026-W30]] — LLM vs SBDD 공간 제약 벤치마크 (arXiv:2607.18144) [preprint]

### 2026-W29 (2026-07-14~19)
- [[scVision]] (arXiv:2607.14163) — 단일세포 생물학 비전 파운데이션 모델, ViT로 72M 세포 사전학습, 공간 유전자 지도 활용 [preprint]
- [[Evo2-Probes]] (arXiv:2607.14070) — Evo 2 게놈 언어 모델 프로브, 메타게노믹스 AMR·바이오시큐리티 기능 스크리닝 [preprint]

### 2026-W28
- **2026-W28** — MolBasic (arXiv:2607.03007): SMILES-그래프 번역으로 분자 LLM 구조 이해 개선 (와이드) [[2026-W28]]

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
