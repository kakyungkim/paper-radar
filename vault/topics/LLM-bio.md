---
type: moc
tags: [LLM-bio]
---
# 🗂 LLM-bio — 주제 지도(MOC)

## 핵심 흐름
(2026-W29 기준) scVision(yesiloglu, arXiv:2607.14163)은 ViT 아키텍처를 단일세포 생물학에 이식해 공간 유전자 지도(spatial gene cartography)로 72M 세포를 사전학습한 비전 파운데이션 모델이다. 언어 모델이 아닌 비전 트랜스포머를 세포 생물학에 적용한 흐름이 W24 m6A-FORM·W25 scGTN 이후 뚜렷해지고 있다. Evo 2 Probes(guntoro, arXiv:2607.14070)는 게놈 언어 모델 Evo 2를 프로브로 활용해 메타게노믹스에서 바이오시큐리티 기능(AMR 유전자 등)을 스크리닝한다. W27 Affinage의 문헌 마이닝 LLM에 이어, W29에서는 비전 파운데이션 모델과 게놈 언어 모델 프로브로 적용 방향이 분화한다. 생물학 에이전트 LLM 흐름(W25~W27)은 W28~W29에서 소강 상태다.

## 타임라인
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
