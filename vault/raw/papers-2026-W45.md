# paper-radar 선별 — 2026-W45

- 선별 기준: 바이오인포·유전체·임상ML·신약AI 핵심 5편 + 와이드 3편
- 후보 풀: vault/raw/candidates-2026-W45.md (60건)
- 중복 회피: vault/_meta/recent-papers.jsonl (최근 W44 기준)
- 수집 창: 2026-11-02 ~ 2026-11-08

---

## 핵심 (Core) — 5편

### C1. 전사체와 크로마틴 간 교차 모달 분석을 가능하게 하는 단일세포 멀티모달 파운데이션 모델 (A single-cell multimodal foundation model enables cross modality analysis between transcriptome and chromatin — MUTUAL)

- 출처: biorxiv · 2026-11-02 · **preprint** · bioinformatics
- 저자: Bao, X.; Zhu, J.; Song, X.; et al.
- DOI/링크: https://doi.org/10.64898/2026.10.28.762297
- 코드/데이터: 초록에 링크 없음
- 선택 사유: scRNA-seq↔scATAC-seq 양방향 무학습(zero-shot) 전이를 400개 공개 멀티오믹 데이터셋으로 가능하게 한 최초의 멀티모달 단일세포 파운데이션 모델 브리징 프레임워크

> MUTUAL (MUltiome Transfer in a Unified Aligned Latent space) keeps scFoundation and EpiAgent frozen, combines embeddings with linear summaries of each modality, and learns a shared RNA–ATAC space from 3.0 million paired cells of 400 public multiome datasets. Applied without refitting to ten datasets not used for training, MUTUAL matched cells' RNA and ATAC profiles more accurately than methods fitted on other donors of the same dataset, annotated ATAC-only cells more accurately, and transferred transcription-factor motif activity to RNA-only cells beyond what cell-type assignment provides. In a maturation series of stem-cell-derived islets, motif activity predicted from RNA largely reproduced the measured stage-wise changes when other libraries of the series served as the reference.

---

### C2. DNA 파운데이션 모델 벤치마킹: Evo2 변이 효과 예측의 생물학적 맹점 (Benchmarking DNA Foundation Models: Biological Blind Spots in Evo2 Variant-Effect Prediction)

- 출처: biorxiv · 2026-11-03 · **preprint** · genomics
- 저자: Mathur, V.; Sachidanandam, R.
- DOI/링크: https://doi.org/10.64898/2026.03.10.710786
- 코드/데이터: 초록에 링크 없음
- 선택 사유: 대형 DNA 파운데이션 모델(Evo2)이 임상 변이 해석에서 갖는 맹점(코돈 편향·인접 서열 감도)을 체계적으로 드러낸 최초의 통제된 벤치마크로, 제로샷 게놈 FM의 임상 활용 가능성에 중요한 경고를 제시

> Evo2 achieves strong aggregate performance on mitochondrial variants (AUROC=0.927), but controlled benchmarks based on well-characterized nuclear and mitochondrial sequence features reveal systematic blind spots in short-range signals, including codon usage bias. Spurious sensitivity to biologically neutral flanking sequences can cause pathogenic tRNA variants to be misclassified as benign. These findings suggest that Evo2's predictive performance may rely more heavily on learned sequence regularities than on the biological constraints governing variant function, raising concerns about the clinical utility of zero-shot genomic foundation models.

---

### C3. 약물 발굴을 위한 스케일러블 AI 사이언티스트 (El Agente Fármaco: A Scalable AI Scientist for Drug Discovery)

- 출처: arxiv · 2026-11-02 · **preprint** · cs.AI
- 저자: Marcel Müller, Mohammad Ghazi Vakili, Yoshihiro Ogura, et al.
- DOI/링크: https://arxiv.org/abs/2611.03832
- 코드/데이터: 초록에 링크 없음
- 선택 사유: LLM이 약물 발굴 전체 워크플로(분자 생성·도킹·물성 예측·구매 가능 화합물 검색)를 오케스트레이션하고, 공유 과학 메모리(Fármaco Atlas)로 출처를 추적하는 스케일러블 AI 사이언티스트 프레임워크

> El Agente Fármaco uses modern LLM technology to turn discovery goals expressed in everyday language into complex, scalable computational screening workflows. The agentic harness selects scientific tools, reviews results, and adjusts subsequent steps. Centers on Fármaco Atlas — a shared scientific memory storing molecules, structures, and results with their provenance. A single request can launch calculations for an entire collection of molecules without a separate LLM decision for every compound. Retrospective comparison with an expert-led campaign: proposed chemically distinct candidates with competitive docking scores and higher calculated drug-likeness. 22-task benchmark: highest mean model-judged score with lower median cumulative token use and peak context vs plain tool calls and Codex.

---

### C4. 대형 언어 모델로 강화된 전자 허약 평가와 입원 환자 예후 성능 (Large Language Model-Enhanced Electronic Frailty Assessment and Prognostic Performance in Hospitalized Adults: A Retrospective Cohort Study)

- 출처: medrxiv · 2026-11-05 · **preprint** · health systems and quality improvement
- 저자: Dalal, A. K.; Lundstedt, J.; Ernecoff, N.; et al.
- DOI/링크: https://doi.org/10.64898/2026.11.04.26367272
- 코드/데이터: 초록에 링크 없음
- 선택 사유: GPT-4o로 물리치료 기록에서 허약 지표를 추출해 전자 허약 지수를 보완했을 때 민감도는 올라가지만 예측 판별력(AUROC)은 개선되지 않은, 임상 ML에서 LLM 보강 효과의 현실적 한계를 보인 후향 코호트 연구

> 616 hospitalizations, adults ≥50 years, Feb 2022–Apr 2024. Standard eFI (35-deficit diagnosis-based) vs LLM-enhanced eFI (GPT-4o extracts frailty-related deficits from physical therapy documentation). Standard: 35.1% classified frail; LLM-enhanced: 58.8% classified frail. Both independently associated with composite adverse outcome (discharge to facility, readmission, or death within 90 days): adjusted OR 1.98 (95% CI 1.39–2.83) vs 2.46 (1.75–3.47). AUROC: 0.636 vs 0.660, difference 0.024 (95% CI −0.006 to 0.053; p=0.12). LLM enhancement increased sensitivity (42.5%→69.4%) but decreased specificity (73.0%→52.7%).

---

### C5. 세포 맥락이 체세포 변이의 전사체적 영향을 결정한다 (Cellular context shapes the transcriptomic impact of somatic variants)

- 출처: biorxiv · 2026-11-02 · **preprint** · genetics
- 저자: Sun, P.; Jia, P.; Lou, C.; et al.
- DOI/링크: https://doi.org/10.64898/2026.10.28.760887
- 코드/데이터: 초록에 링크 없음
- 선택 사유: 체세포 변이의 영향이 서열 주석이 아닌 세포 상태에 의해 결정된다는 패러다임 전환적 발견 — PrismSNV와 Ligo-Seq로 단일세포 전사체 수준에서 직접 측정한 최초의 체계적 연구

> PrismSNV and Ligo-Seq (a single-cell full-length transcriptome sequencing platform) quantify transcriptomic displacement associated with within-cell SNV-state toggling. Across 26 samples from three cancer types, >60% of candidate SNVs showed significant cell-type-specific displacement with >30% variation in magnitude. Sequence-based deleteriousness was poorly aligned with cellular displacement; <3% of top-displacement SNVs across six tumor types were catalogued in ClinVar. Displacement was strongest in transcriptionally plastic, less differentiated states. Analysis of 655,349 CD4+ T-cell transcriptomes showed that SNV-gene associations changed in magnitude and sometimes direction during T-cell activation. Variant impact is shaped by cellular context rather than sequence alone — the variant-cell pair is a critical unit for interpreting somatic variation.

---

## 와이드 (Wide) — 3편

### W1. 단일세포 파운데이션 모델이 도움이 되는 곳: 주석·교란·조절 추론의 단순 베이스라인 대비 벤치마크 (Where single-cell foundation models help: a benchmark of annotation, perturbation and regulatory inference against simple baselines)

- 출처: biorxiv · 2026-11-04 · **preprint** · bioinformatics
- 저자: Cupaioli, F. A.; Merelli, I.
- DOI/링크: https://doi.org/10.64898/2026.11.03.763968
- 코드/데이터: 초록에 링크 없음 (fmaudit 패키지 공개 예정)
- 선택 사유: 단일세포 파운데이션 모델이 실제로 가치를 더하는 태스크와 그렇지 않은 태스크를 구분한 최초의 종합 벤치마크 — 종간 전이와 in silico 교란에서 강점 확인

> Benchmarked 5 FMs (scGPT, Geneformer V1 and V2, Nicheformer, scFoundation), CellOracle, supervised perturbation models (STATE), and task-matched simple baselines. FMs most useful for cross-species annotation transfer: Nicheformer reached 0.98 accuracy (human→mouse lung), Geneformer V2 and scFoundation ~0.90 vs 0.68 for the best baseline. Zero-shot in silico perturbations: up to 75% shifted in the expected direction (scFoundation, p<1e-8). Within a species, FM embeddings annotated cells as accurately as principal components. Releases fmaudit benchmark package.

---

### W2. 과학적 샌드박스에서의 추론 역설: 확장 추론이 자율 바이오인포매틱스에서 실패하는 이유와 해결책 (The Reasoning Paradox in Scientific Sandboxes: Why Extended Reasoning Fails in Autonomous Bioinformatics and How to Fix It)

- 출처: biorxiv · 2026-11-03 · **preprint** · bioinformatics
- 저자: Salami, R. O.; Amuna, D.; Akorful, R. A.; et al.
- DOI/링크: https://doi.org/10.64898/2026.10.30.763189
- 코드/데이터: 초록에 링크 없음 (파이프라인·프롬프트·궤적 공개 예정)
- 선택 사유: 확장 추론 LLM(DeepSeek-R1 등)이 자율 바이오인포매틱스 환경에서 오히려 성능이 저하되는 역설을 처음으로 체계적으로 분석하고 DTDR 아키텍처로 해결책을 제시

> Forensic audit of extended reasoning models (DeepSeek-R1-Distill-Qwen-14B) vs instruction-tuned controls (Qwen2.5-Coder-14B) in containerized computational biology sandboxes (scRNA-seq, DESeq2, variant prioritization; n=22 per arm). Two failure modes identified: (1) PubMed Prior Trap — epistemic rationalization replacing empirical computation with speculative literature recall; (2) Tag Language Nesting Collisions — XML action tags conflated with Python syntax. DTDR (Dual Track Decoupled Reasoning) architecture: accuracy rescued from 0.0% to 9.09% (2/22), code errors reduced 81% (13.6% vs 72.7%), average steps to solution reduced 66% (1.77 vs 5.18).

---

### W3. 변이스케이프: 출판된 종양학 초록에서 변이-치료-암 연관성의 대형 언어 모델 기반 추출 후향 연구 (Variantscape: Retrospective Study of Large Language Model-Based Extraction of Variant-Treatment-Cancer Associations from Published Oncology Abstracts)

- 출처: medrxiv · 2026-11-02 · **preprint** · health informatics
- 저자: Wosny, M.; Blindu, A. S.; Boesch, M.; et al.
- DOI/링크: https://doi.org/10.64898/2026.08.02.26359492
- 코드/데이터: 초록에 링크 없음
- 선택 사유: 370만 편 초록에서 LLM으로 변이-치료-암 삼각 연관성을 대규모 자동 추출한 오픈 액세스 정밀 종양학 도구로, 분자 종양위원회(MTB) 준비 지원에 직접 활용 가능

> From >3.7 million abstracts (January 2014–October 2026), 37,895 papers mentioning a variant, cancer type, and therapeutic agent together. 11,985 unique variants across 197 cancer types and 547 therapeutic agents. LLM verification confirmed ≥1 association in 35,224 papers: literature-derived graph of 10,571 nodes and 44,644 verified edges. Canonical alterations (e.g., BRAF V600E in melanoma) strongly linked to established treatments; several rare variants also emerged with high-confidence literature support.
