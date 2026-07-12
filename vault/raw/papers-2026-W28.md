# 2026-W28 논문 수집 (2026-07-07 ~ 2026-07-12)
수집일: 2026-07-12 | 수집자: paper-scout

## 소스별 수집 건수
- Nature Genetics (peer-reviewed): 1편
- bioRxiv (preprint): 2편
- arXiv (preprint): 5편
- 합계: 핵심 5편 + 와이드 3편 = 8편

---

## 핵심 (Core 5)

### 1. 멀티오믹스의 임상 도입 경로 지도 그리기 (Mapping the path to clinical implementation of multi-omics)
- **저자**: Said I. Ismail, Chadi Saad, Wadha A. A. L. Muftah 외 | Qatar Genome Programme 외 다수 기관
- **출처**: Nature Genetics
- **날짜**: 2026-07-07
- **상태**: peer-reviewed (Perspective)
- **arXiv ID / DOI**: 10.1038/s41588-026-02663-2
- **원문 링크**: https://www.nature.com/articles/s41588-026-02663-2
- **코드/데이터**: 해당 없음 (Perspective 논문)
- **사회적 신호**: 없음
- **한 줄 요약**: 멀티오믹스(DNA·RNA·단백질·대사체)가 연구에서 임상 루틴으로 전환될 때 직면하는 전처리·계산·규제·윤리적 도전 과제를 체계적으로 정리하고 완화 전략을 제시한 Perspective.
- **선택 이유**: 이번 주(7월 7일) Nature Genetics 게재 확인. 멀티오믹스 임상 도입 논의를 종합하는 로드맵 성격의 논문으로, 임상ML과 바이오인포 커뮤니티가 공통으로 참조해야 할 레퍼런스.
- **분야 태그**: 바이오인포 / 멀티오믹스 / 임상ML

---

### 2. 단일세포 CRISPR 스크린에서 아이소폼 수준 해상도가 드러내는 유전자 교란의 숨겨진 기능적 결과 (Isoform-level resolution in single-cell CRISPR screens reveals hidden functional consequences of gene perturbation)
- **저자**: Nathanael Andrews, Josie Gleeson, Jasper Panten, Sofia Oling, Sofia Lundqvist, Tuuli Lappalainen | (소속 미확인 — 원문 확인 필요)
- **출처**: bioRxiv
- **날짜**: 2026-07-09
- **상태**: preprint (미동료심사)
- **arXiv ID / DOI**: 10.64898/2026.07.09.737410
- **원문 링크**: https://www.biorxiv.org/content/10.64898/2026.07.09.737410
- **코드/데이터**: 미확인 (원문 확인 필요)
- **사회적 신호**: 없음
- **한 줄 요약**: 단일세포 CRISPR 스크린에 아이소폼 수준 분석을 도입해 유전자 교란이 기존 방식으로는 감지되지 않던 기능적 결과를 유발함을 보인다.
- **선택 이유**: 단일세포 CRISPR 스크린의 분해능 한계를 아이소폼 수준으로 확장한 방법론 논문. Lappalainen 교수(RNA 생물학 권위자)가 교신저자로, RNA 이형접합(splicing) 규제 연구에 직접 활용 가능한 신규 도구 제공.
- **분야 태그**: 유전체 / 단일세포 / 기능유전체

---

### 3. 데이터 기반 소프트 레이블로 DNA 리드 분류를 전신 세포유형 역분리로 확장 (Data-Driven Soft Labeling Scales DNA Read Classification to Whole-Body Cell-Type Deconvolution)
- **저자**: Dmytro Rizdvanetskyi, Nathan Ross, Pavlo Lutsik | KU Leuven
- **출처**: arXiv (q-bio)
- **날짜**: 2026-07-06
- **상태**: preprint (미동료심사)
- **arXiv ID / DOI**: arXiv:2607.04987
- **원문 링크**: https://arxiv.org/abs/2607.04987
- **코드/데이터**: 미확인 (원문 확인 필요)
- **사회적 신호**: 없음
- **한 줄 요약**: DNA 메틸화 리드 수준 분류에 데이터 기반 소프트 레이블을 적용한 Syto 프레임워크를 제안하고, 인체 39개 세포유형 전신 역분리에서 기존 SOTA 대비 MSE 2.56× 감소를 보고한다.
- **핵심 수치**: MSE 2.56× 감소 (39 세포유형 기준); OOD 16개 조직 전이 검증 — 초록 기준
- **선택 이유**: 세포 유리 DNA(cfDNA) 기반 액체생검의 세포유형 역분리 정확도를 획기적으로 끌어올리는 방법. KU Leuven의 메틸화 연구 그룹 산출물로, 암 조기진단·모니터링 파이프라인에 직접 접목 가능.
- **분야 태그**: 바이오인포 / 유전체 / 액체생검

---

### 4. 고차원 멀티오믹스 데이터에서의 확장 가능한 이중 계층 인과 발견 (Causal ASCEND: Scalable Two-tier Causal Discovery on High Dimensional Multi-omics Data)
- **저자**: Stephen Asiedu, David Watson | Department of Informatics, King's College London
- **출처**: arXiv (cs.LG / q-bio)
- **날짜**: 2026-07-05
- **상태**: preprint (미동료심사) — BIOKDD 2026 (ACM SIGKDD) 워크숍 채택
- **arXiv ID / DOI**: arXiv:2607.04527
- **원문 링크**: https://arxiv.org/abs/2607.04527
- **코드/데이터**: 미확인 (원문 확인 필요)
- **사회적 신호**: BIOKDD 2026 채택 (ACM SIGKDD 2026 병설)
- **한 줄 요약**: SNP·메틸화(상위층) → 유전자 발현(하위층)의 알려진 이중 계층 구조를 활용해 지수적 복잡도 없이 게놈 규모 인과 발견을 가능하게 하는 제약 기반 프레임워크 ASCEND를 제안한다.
- **핵심 수치**: 기존 방식이 지수 폭발을 겪는 고차원에서 다항식 시간 복잡도 달성 — 초록 기준
- **선택 이유**: 멀티오믹스 인과 추론은 eQTL 분석·유전자 조절망 재구성의 핵심 병목인데, 이 논문이 그 확장성 문제를 직접 공략. 코드 공개 시 유전체 분석 파이프라인에 즉시 활용 가치가 높다.
- **분야 태그**: 바이오인포 / 멀티오믹스 / 유전체

---

### 5. 환자 맞춤 지식 그래프와 유전자 교란 표현 정렬을 통한 치료 결과 예측 (Predicting Therapeutic Outcome via Aligning Patient-Specific Knowledge Graph and Gene-Level Perturbation Representations)
- **저자**: Dongmin Bang, Sugyun An, Inyoung Sung, Ilho Yun, Sun Kim (서울대학교 / AIGENDRUG Co., Ltd.), Sangseon Lee (인하대학교)
- **출처**: arXiv (cs.LG / q-bio)
- **날짜**: 2026-07-06
- **상태**: preprint (미동료심사) — BIOKDD 2026 (ACM SIGKDD) 워크숍 채택
- **arXiv ID / DOI**: arXiv:2607.04557
- **원문 링크**: https://arxiv.org/abs/2607.04557
- **코드/데이터**: 미확인 (원문 확인 필요)
- **사회적 신호**: BIOKDD 2026 채택
- **한 줄 요약**: 종양 전처리 전사체에서 환자별 유전자 조절망(DysRegNet)과 LINCS L1000 교란 시뮬레이션을 정렬하는 PREDIKTOR 프레임워크로 임상 약물 반응을 예측한다.
- **핵심 수치**: TCGA 환자·약물·조직 분할 평가에서 기존 SOTA 초과; I-SPY2 임상시험 제로샷 전이 AUROC +5.6% — 초록 기준
- **선택 이유**: 한국 연구팀(서울대·인하대·AIGENDRUG) 산출물. 실제 임상시험 데이터(I-SPY2)에 제로샷 전이가 검증된 점이 주목할 만하며, 정밀종양학 파이프라인에서 즉시 테스트 가능한 공개 워크플로우.
- **분야 태그**: 임상ML / 신약AI

---

## 와이드 (Wide 3)

### W1. AI가 설계한 DNA 라이브러리의 합성 장벽 돌파 (Breaking the Synthesis Barrier for AI-Designed DNA Libraries)
- **저자**: Plesa Lab 소속 (구체적 저자 미확인 — 원문 확인 필요)
- **출처**: bioRxiv (Synthetic Biology)
- **날짜**: 2026-07-07
- **상태**: preprint (미동료심사)
- **arXiv ID / DOI**: 10.64898/2026.07.07.736931
- **원문 링크**: https://www.biorxiv.org/content/10.64898/2026.07.07.736931v1
- **코드/데이터**: 미확인
- **사회적 신호**: 없음
- **한 줄 요약**: 확률적 DNA 라이브러리의 합성 인식 매개변수화에 정책 경사(PGLD)를 적용해 DNA 합성 비용이라는 장벽을 우회하고, 광역 중화 항체 변이 공간 탐색을 위한 ~10^6 서열 라이브러리를 약 700 USD에 설계·합성한다.
- **선택 이유**: 합성생물학 + 강화학습의 결합으로 항체공학·단백질 엔지니어링 실험 주기를 단축하는 방법론. 신약AI 핵심 축과 인접하지만 주 무대는 합성생물학이어서 와이드로 분류.

---

### W2. LLM 강화학습 훈련 정책 최적화의 신기루 (The Mirage of Optimizing Training Policies: Monotonic Inference Policies as the Real Objective for LLM Reinforcement Learning)
- **저자**: 미확인 (원문 확인 필요)
- **출처**: arXiv (cs.LG)
- **날짜**: 2026-06-말 (2606.29526)
- **상태**: preprint (미동료심사)
- **arXiv ID / DOI**: arXiv:2606.29526
- **원문 링크**: https://arxiv.org/abs/2606.29526
- **코드/데이터**: 미확인
- **사회적 신호**: HuggingFace Daily Papers 7월 7일 상위 트렌드
- **한 줄 요약**: LLM 강화학습에서 훈련 엔진과 추론 엔진의 확률 불일치 문제를 지적하고, 추론 정책 단조 개선을 실제 목표로 삼는 MIPU 프레임워크를 제안한다.
- **선택 이유**: 이번 주 HF 상위 트렌드. GRPO·PPO 기반 생물학 도메인 LLM 포스트-트레이닝에도 직접 적용 가능한 일반 방법론이어서 추적 가치가 있다.

---

### W3. LLM의 분자 이해 개선을 위한 SMILES-그래프 번역 (Back to Basics: Improving Molecular Understanding in LLMs via SMILES-Graph Translation)
- **저자**: Wenda Wang, Jinjia Feng, Zhewei Wei | (소속 미확인 — 원문 확인 필요)
- **출처**: arXiv (cs.LG / q-bio.QM)
- **날짜**: 2026-07-03
- **상태**: preprint (미동료심사)
- **arXiv ID / DOI**: arXiv:2607.03007
- **원문 링크**: https://arxiv.org/abs/2607.03007
- **코드/데이터**: 미확인
- **사회적 신호**: 없음
- **한 줄 요약**: 분자 LLM이 SMILES의 그래프 위상 구조를 실제로 학습하지 못한다는 한계를 진단하고, SMILES-그래프 양방향 변환을 핵심 과제로 삼는 MolBasic 프레임워크와 Chain-of-Thought 점진 학습 체계를 제안한다.
- **선택 이유**: 신약AI와 인접하지만 주 관심사는 LLM 분자 표현의 구조적 결함 진단이라는 방법론 논문. 분자 생성·특성 예측 LLM을 쓰는 연구자에게 체크리스트로 활용 가능.
