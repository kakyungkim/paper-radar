# Papers 2026-W39 (2026-09-21 ~ 2026-09-27)

수집일: 2026-09-27  
소스별 건수: arXiv 4편 · bioRxiv 2편 · medRxiv 0편  
핵심 5편 · 와이드 3편

---

## 핵심 (Core)

### C1. 전사인자는 크로마틴에서 두 번째 조절 코드를 읽는다 (Transcription factors read a second regulatory code in chromatin)

- arxiv_id / DOI: https://doi.org/10.64898/2026.09.23.753737
- 저자: Xin Zheng, Ying Tian, Jinyu Li, Haotian Sun, Xue Yue 외
- 소속: Tongji University; Shanghai Institute of Biochemistry and Cell Biology, Chinese Academy of Sciences
- 게시일: 2026-09-23
- 상태: preprint (미동료심사)
- 소스: bioRxiv
- 원문 링크: https://www.biorxiv.org/content/10.64898/2026.09.23.753737v1
- 코드/데이터: 미확인
- 초록 (원문, 영어): Transcription factors (TFs) decode gene regulatory information written in DNA, yet how this vocabulary is interpreted within chromatin remains largely unexplored. Using an upgraded NCAP-SELEX platform, we systematically mapped the nucleosomal DNA recognition landscapes of 269 human TFs and uncovered a widespread, chromatin-dependent mode of sequence recognition: many TFs recognize motifs on nucleosomal DNA that are distinct from their canonical naked-DNA binding sites, revealing that nucleosome architecture encodes a second gene regulatory code in chromatin. Cryo-electron microscopy structures of TF–nucleosome complexes demonstrate that this second code is read through a combination of nucleosome-induced DNA deformation and direct protein–histone contacts. Functional analyses show that these chromatin-encoded motifs actively promote chromatin accessibility and drive cell-type-specific cis-regulatory activity in vivo.
- 사회적 신호: 없음
- 핵심 태그: [유전체, 바이오인포]
- 선택 이유: 업그레이드된 NCAP-SELEX로 269개 인간 TF의 뉴클레오솜 결합 지형을 체계적으로 매핑해 크로마틴 내 '두 번째 조절 코드' 존재를 발견—규제 유전체 분야에서 방법적·개념적 기여가 뚜렷하다.

---

### C2. MIRCID: 추론된 허브 miRNA가 약물 기전 모델링의 다중 태스크 성능을 향상시킨다 (MIRCID: Inferred Hub-miRNAs Drive Cross-Task Improvements in Drug Mechanistic Modeling)

- arxiv_id / DOI: arXiv:2609.21280
- 저자: Xin Cao, Yigang Chen, Jiatong Xu, Ziyue Zhang, Xiang Cheng, Shenyu Wang, Yangyi Zhang, Xiaoxuan Cai, Shidong Cui, Zihao Zhu, Xiang Ji, Hsi-Yuan Huang, Yang-Chi-Dung Lin, Hsien-Da Huang
- 소속: 미확인 (중국계 기관 다수)
- 게시일: 2026-09-18 (v1), 2026-09-21 (v2, 이 주 기준)
- 상태: preprint (미동료심사)
- 소스: arXiv
- 원문 링크: https://arxiv.org/abs/2609.21280
- 코드/데이터: GitHub 공개 — https://github.com/XinCao02/MIRCID
- 초록 (원문, 영어): Drug mechanism-of-action (MoA) modeling commonly relies on perturbational transcriptomes, but matched microRNA (miRNA) measurements are often unavailable. Inferred regulatory features offer a scalable way to reuse these data. MIRCID is a framework comparing gene expression with inferred transcription factor (TF) activity and miRNA expression across pathway classification and similarity-based MoA retrieval. HubmiRNet infers 414 pan-cancer hub miRNAs (HubmiRs) from 977 L1000 landmark genes, achieving a Pearson correlation coefficient of 87.72%; its 1,298-output variant also outperformed SiCmiR on the full-miRNA task (71.21% versus 67.30%). In the evaluated comparisons, miRNA augmentation provided more consistent gains than TF activity.
- 사회적 신호: 없음
- 핵심 태그: [신약AI, 바이오인포]
- 선택 이유: L1000 랜드마크 유전자에서 414개 pan-cancer 허브 miRNA를 추론해 drug MoA 분류·검색 성능을 일관되게 개선; 코드 공개로 재현 가능.

---

### C3. GLR-MM: 결측 모달리티 조건에서 흉부 X선·EHR 다중 모달 표현을 위한 그래프 기반 전역-국소 재구성 (GLR-MM: Graph-Based Global-Local Reconstruction for Robust Multimodal Chest X-ray and EHR Representation Learning under Missing Modalities)

- arxiv_id / DOI: arXiv:2609.23876
- 저자: Surbhi Sharma, Nikhil Manali, Devesh Maheshwari
- 소속: Houston Methodist (Sharma); University of Wisconsin–Madison (Maheshwari); Walmart (Manali)
- 게시일: 2026-09-20 (제출; arXiv 공고 2026-09-23)
- 상태: preprint — MICCAI 2026 accepted
- 소스: arXiv
- 원문 링크: https://arxiv.org/abs/2609.23876
- 코드/데이터: 미확인
- 초록 (원문, 영어): Clinical multimodal models must often predict before all chest X-ray (CXR) and electronic health record (EHR) inputs are available. Existing approaches align observed representations, model missingness, or reconstruct across modalities, but do not jointly exploit within-patient and clinically similar inter-patient evidence. GLR-MM maps five CXR-EHR modalities to a shared space, reconstructs missing embeddings through complementary local cross-modal and global graph-attention branches, adaptively fuses their estimates, and optimizes class-balanced prediction, reconstruction, and contrastive objectives. On 9,620 MIMIC-derived ICU stays evaluated with 10%, 30%, and 50% random modality missingness, GLR-MM achieves higher AUROC and AUPRC at 50% missingness by 0.0088 and 0.0249, respectively, compared to strong baselines.
- 사회적 신호: MICCAI 2026 accepted
- 핵심 태그: [임상ML]
- 선택 이유: ICU 사망 예측 태스크에서 흉부 X선 + EHR 5개 모달리티의 결측 문제를 전역·국소 그래프 재구성으로 해결; MICCAI 2026 채택, MIMIC 기반 외부 검증.

---

### C4. QLoRA로 Ministral LLM을 시퀀스→기능 단백질 주석 생성에 파인튜닝 (QLoRA Fine-Tuning of Ministral LLM for Sequence-to-Function Protein Annotation)

- arxiv_id / DOI: arXiv:2609.24538
- 저자: Demian Pavlyshenko, Bohdan Pavlyshenko
- 소속: 미확인
- 게시일: 2026-09-21
- 상태: preprint (미동료심사)
- 소스: arXiv
- 원문 링크: https://arxiv.org/abs/2609.24538
- 코드/데이터: 미확인
- 초록 (원문, 영어): Functional annotation of newly sequenced proteins remains a bottleneck in molecular biology: the number of sequences in public repositories grows far faster than the capacity for manual curation. Most computational approaches consider annotation as multi-label classification over a fixed ontology, which constrains predictions to a predefined label set. In this work we study protein annotation as a sequence-to-text generation problem. We fine-tune the 3B-parameter Ministral 3 base model with QLoRA (4-bit NF4 quantization with low-rank adapters) on sequence–annotation pairs. Predictions are assessed with an LLM-as-expert protocol: a GPT model prompted as a senior molecular-biology curator scores organism identification as binary and function annotation quality. We conclude that QLoRA-fine-tuned compact LLMs can generate curator-style annotations with genuine biological value for a substantial subset of proteins.
- 사회적 신호: 없음
- 핵심 태그: [단백질, LLM-bio]
- 선택 이유: 3B 파라미터 LLM을 4-bit QLoRA로 파인튜닝해 단백질 기능 주석을 자유 텍스트로 생성; 고정 온톨로지 분류를 벗어난 생성 접근법의 가능성을 실험적으로 보임.

---

### C5. HR-FRGS: 이중 레이어 하이퍼그래프 학습을 이용한 NGS RNA 시퀀스 데이터의 새 바이오마커 발굴 프로토콜 (HR-FRGS: A Novel Biomarker Discovery Protocol using Dual Layer Hypergraph Learning for NGS RNA Sequence Data)

- arxiv_id / DOI: https://doi.org/10.64898/2026.09.21.753079
- 저자: Manan Kumar Gupta, Mainak Paul, Soumen Kumar Pati
- 소속: Presidency University, Bangalore; Maulana Abul Kalam Azad University of Technology, West Bengal
- 게시일: 2026-09-21
- 상태: preprint (미동료심사)
- 소스: bioRxiv
- 원문 링크: https://www.biorxiv.org/content/10.64898/2026.09.21.753079v1
- 코드/데이터: 미확인
- 초록 (원문, 영어 — 검색 기반 요약, 원문 전문 미확인): Biomarker discovery from high-dimensional RNA sequencing data remains challenging due to noise, sparsity, and complex gene–gene interactions. HR-FRGS (Hypergraph Regularised Fuzzy Rough Gene Selection) is a dual-layer hypergraph learning framework that combines Random Walk with Restart (RWR) diffusion and Hypergraph Betweenness Centrality to score genes by their centrality in the biological interaction network, enabling knowledge-driven identification of robust NGS RNA biomarkers.
- 사회적 신호: 없음
- 핵심 태그: [바이오인포, 유전체]
- 선택 이유: 퍼지 러프 집합과 하이퍼그래프 중심성을 결합한 이중 레이어 유전자 선택 프로토콜; NGS RNA 고차원 데이터에서 생물학적 네트워크 구조를 활용하는 방법론적 기여.

---

## 와이드 (Wide)

### W1. JEPA-Anything: 다양한 세계에서 예측 모델 학습 (JEPA-Anything: Learning Predictive Models across Different Worlds)

- arxiv_id / DOI: arXiv:2609.20800
- 저자: Taoyong Cui 외 (NVIDIA, NTU, MIT 공동)
- 게시일: 2026-09-17 (HuggingFace Daily Papers 2026-09-22 등재)
- 상태: preprint (미동료심사)
- 원문 링크: https://arxiv.org/abs/2609.20800
- 초록 (1~2문장 요약): 도메인 불가지론적 예측 아키텍처 JEPA-Anything이 직교 예측 인수분해(OPF)로 시각·생물학·임상 궤적·분자 동역학 등 7개 도메인에 걸쳐 기존 JEPA 베이스라인 대비 10개 동역학 태스크 전체에서 성능 개선을 달성; 코드·모델 공개(GitHub: Gen-Verse/JEPA-Anything).
- 핵심 태그: [LLM-bio, 기타]
- 선택 이유: 생물학·임상 궤적 도메인을 포함한 범용 예측 아키텍처로 이 주 HuggingFace에서 화제.

---

### W2. Brain-Token Learning: 마이크로상태 기반 토크나이제이션과 멀티스케일 상호작용을 이용한 장기 EEG 시퀀스 모델링 (Brain-Token Learning: Microstate-Based Tokenization and Multi-Scale Interaction for Long-Horizon EEG Sequence Modeling)

- arxiv_id / DOI: arXiv:2609.24324
- 저자: Weishan Ye, Yue Pan, Li Zhang, Gan Huang, Zhen Liang
- 게시일: 2026-09-21
- 상태: preprint (미동료심사)
- 원문 링크: https://arxiv.org/abs/2609.24324
- 초록 (1~2문장 요약): EEG 신호를 고정 윈도우가 아닌 준안정 뇌 마이크로상태 단위의 가변 길이 토큰으로 표현해 장기 시퀀스 모델링에서 생물학적으로 의미 있는 시간 구조를 포착한다.
- 핵심 태그: [기타 (뇌공학)]
- 선택 이유: 뇌 상태 기반 토크나이제이션 아이디어가 단일세포 시계열·임상 EHR 시퀀스 모델링으로 이식 가능한 방법론적 아이디어로 주목.

---

### W3. SoL-Pi: 효율적인 에이전트 하네스를 위한 자율 연구 루프 재귀 확장 (SoL-Pi: Recursively Scaling Auto-Research Loops for Efficient Agent Harness)

- arxiv_id / DOI: arXiv:2609.20519
- 저자: Haozhe Liu 외 (NVIDIA, NTU, MIT)
- 게시일: 2026-09-17 (HuggingFace Daily Papers 2026-09-22 등재)
- 상태: preprint (미동료심사)
- 원문 링크: https://arxiv.org/abs/2609.20519
- 초록 (1~2문장 요약): 자율 연구 에이전트 하네스에서 4가지 메커니즘(액션 실행·컨텍스트 압축·관측 처리·위임 읽기)으로 루프를 재귀 확장해 GPT-5.6/Opus 5 수준 성능을 유지하면서 토큰 트래픽을 44.7–49.0%, API 비용을 약 1/3 절감.
- 핵심 태그: [기타 (AI 에이전트)]
- 선택 이유: 바이오인포 자율 연구 에이전트(BixBench3 등)와 직결되는 토큰 효율 연구; 이 주 HuggingFace 화제작.
