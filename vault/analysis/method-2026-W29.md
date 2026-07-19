---
type: analysis
lens: method
week: 2026-W29
date: 2026-07-19
analyst: method-analyst
input: vault/raw/papers-2026-W29.md
---

# 방법 분석 — 2026-W29
분석일: 2026-07-19 | 렌즈: Method | source-grounding 원칙 준수

---

## 핵심 5편

---

### 1. A vision foundation model for single-cell biology via spatial gene cartography (scVision)
**원문**: https://arxiv.org/abs/2607.14163 | preprint (미동료심사) | arXiv:2607.14163
**저자**: Ridvan Yesiloglu, Sakib Mostafa, James Zou 외 — Stanford University (Adeli, Islam, Alizadeh, Wu, Xing 그룹)

**문제의식**: 기존 단일세포 파운데이션 모델은 언어 모델 구조를 그대로 이식해 유전자를 토큰 시퀀스로 처리한다. 이 방식은 유전자 간 공발현 관계와 발현량 규모 정보를 버리는 구조적 손실이 있다. "왜 유전자를 이미지 픽셀로 표현하지 않았나?"라는 질문에서 출발한다.

**기존 한계 → 이번 해결**: 언어 모델 기반 scRNA-seq 파운데이션 모델(Geneformer, scGPT 등)은 유전자 순서 정보만 인코딩하고, 공발현 구조가 시퀀스 순서에 의존적이어서 생물학적 위상(topology)이 왜곡된다. scVision은 최적전달(optimal transport)로 전체 조직에서 공유되는 단일 2D 유전자 레이아웃을 학습해, 공발현 유전자를 이미지 상의 공간적 이웃으로 배치한다. 세포 하나가 픽셀 이미지가 되면 유전자 프로그램(gene program)은 국소 텍스처로 나타나며, 비전 트랜스포머(ViT) + 마스크 이미지 모델링(MIM)이 이 구조를 학습한다.

**아키텍처/방법**:
- 최적전달(OT)로 pan-tissue 2D 유전자 레이아웃 최적화 → 공발현 유전자가 공간적으로 인접
- ViT(Vision Transformer) 인코더 + MIM(Masked Image Modeling) 자기지도 사전학습
- 추론 시 인코더 동결(frozen), fine-tuning 없이 zero-shot 사용
- 구체적 ViT 크기(파라미터 수, 레이어 수)는 초록에서 미확인 — 미제공: 방법 섹션 원문 확인 필요

**데이터**: 7,200만 인간 세포 (pan-tissue) 사전학습. 6개 독립 보류(held-out) 연구로 zero-shot 평가. 데이터 출처(어떤 공개 데이터베이스인지) 미제공: 원문 확인 필요.

**핵심 수치**: 6개 독립 보류 연구에서 zero-shot 세포유형 주석(cell-type annotation) 및 유전자 프로그램 발굴 모두 기존 파운데이션 모델 + 고전 기준선 대비 최고 성능(초록 기준). 멀티스터디 통합 벤치마크에서 가장 강한 토큰 기반 파운데이션 모델과 동등한 성능이며, 생물학적 구조 보존에서 모든 방법 중 최고(검색 결과 기반). 정량 AUC·F1 수치는 미제공: 방법·결과 섹션 원문 직접 확인 필요.

**코드/재현성**: 미제공: 공개 GitHub 레포지토리 미확인. 사전학습 데이터 72M 세포의 재구성도 사전에 확인 필요. preprint 단계이므로 코드 릴리스 전일 가능성 있음.

**검증 수준**: (in silico) — zero-shot 평가를 6개 독립 보류 연구에서 수행, 외부 검증에 해당하나 모두 공개 단일세포 데이터셋 수준. 임상 검증 없음.

**메커니즘 핵심 가정**:
1. OT로 학습한 2D 유전자 레이아웃이 전 조직·세포유형에 걸쳐 일관된 표현 공간을 제공한다 — 레이아웃 자체가 불안정하면 전이 성능이 무너진다.
2. 유전자 프로그램의 공간적 공동 발현이 이미지 내 국소 패턴으로 나타난다 — 생물학적 모듈성(modularity) 가정.
3. ViT + MIM으로 학습한 표현이 시퀀스 기반 모델보다 일반화한다 — 검증은 인간 데이터만, 마우스·기타 생물 적용 가능성 미확인.

**강점**:
- 유전자 공발현 구조를 명시적으로 모델에 인코딩하는 설계 아이디어는 언어 모델 패러다임과 근본적으로 다름
- 72M 세포 규모 사전학습으로 기존 모델과 경쟁 가능한 스케일
- Zero-shot 평가가 6개 독립 연구에 걸쳐 일관됨 — 단일 평가셋 과적합 위험 낮음

**한계**:
- 추정: OT 레이아웃 학습 자체에 대규모 계산 비용 소요 예상 — 재현 장벽
- 코드/데이터 미공개 상태에서 재현 불가
- 인간 세포에만 사전학습 — 마우스·기타 모델 생물 적용 시 추가 학습 필요
- 초록 기준 평가이므로 벤치마크 세부(어떤 6개 연구인지, 어떤 지표인지)는 원문 확인 전까지 클레임 수용 보류

**내 연구 활용**:
해석: scRNA-seq 세포유형 주석 작업이 있다면 코드 공개 시 즉시 테스트해볼 가치가 있다. 특히 학습 데이터가 없는 새로운 조직·질환에서 zero-shot 성능이 관건. 다만 코드 미공개·OT 레이아웃 재현 비용이 실제 사용 장벽이 될 수 있어, 공개 전까지는 wait-and-see. 향후 scVI-tools 생태계 편입 여부가 채택을 결정할 것.

---

### 2. Context-aware sequence-to-function model of human gene regulation (Corgi)
**원문**: https://www.nature.com/articles/s41467-026-75527-2 | peer-reviewed (Nature Communications, Vol. 17, Art. 6200)
**DOI**: 10.1038/s41467-026-75527-2
**저자**: Ekin Deniz Aksu, Martin Vingron | Max Planck Institute for Molecular Genetics
**코드**: https://github.com/ekinda/corgi (공개, Python 3.9+, NVIDIA GPU 필요)

**문제의식**: DNA 서열-기능 모델(Enformer, Basenji2 등)은 특정 세포유형으로 학습된 후 그 조합에 고정된다. 보류된 새 세포유형에서 후성유전체 신호를 예측하려면 해당 세포의 ChIP-seq·ATAC-seq 데이터가 필요해, 실험 데이터가 없는 세포유형에서는 적용 불가다.

**기존 한계 → 이번 해결**: 기존 모델은 "DNA 서열 → 특정 세포유형 신호"의 함수로 세포유형을 내재화한다. Corgi는 트랜스-조절 인자(trans-regulator — TF, 전사 공활성인자, 크로마틴 수식 효소, RNA 결합 단백질의 발현 벡터) 2,891개를 두 번째 입력으로 받아 FiLM(Feature-wise Linear Modulation)으로 서열 표현에 조건 부여한다. RNA-seq 데이터만 있으면 실험한 적 없는 세포유형의 크로마틴 접근성·히스톤 변형·유전자 발현까지 예측한다.

**아키텍처/방법**:
- 기반: DNA 서열 입력 → 시퀀스 인코더 (Basenji2/Enformer 계열로 추정: 검토필요: 방법 섹션 원문 확인 필요)
- 컨텍스트 벡터: 2,891개 trans-regulator 발현값 (TF·공활성인자·크로마틴 수식 효소·RBP)
- FiLM 기법으로 서열 표현에 세포유형 컨텍스트를 feature-wise 선형 변조
- 예측 대상: DNase-seq, ATAC-seq, DNA 메틸화, 히스톤 마크 다수, 유전자 발현 커버리지
- Corgi+: RNA-seq만 입력 → 후성유전체 트랙 대체(imputation) — 후성유전체 실험 없이도 신호 예측

**데이터**: ENCODE·Roadmap Epigenomics 계열 다세포유형 에피게놈 데이터 (추정: 원문 확인 필요). 세포유형 hold-out 방식으로 평가. 코드 레포에 `data/tf_reference.npy` 형태로 trans-regulator 발현 참고 분포 포함.

**핵심 수치**: Corgi+, RNA-seq 입력만으로 후성유전체 트랙 imputation SOTA (기존 최고 방법 대비). "실험 수준에 근접한 유전자 발현 예측 정확도" — 구체적 Pearson r·AUROC 수치는 미제공: 방법·결과 섹션 원문 직접 확인 필요.

**코드/재현성**: GitHub 공개 확인 (https://github.com/ekinda/corgi, 27개 커밋). `pip install .` 설치, 단일 서열 추론·영역 기반 예측·BigWig 출력 예시 스크립트 포함. NVIDIA Ampere 이상 GPU 필요. Nature Communications 게재로 동료심사 완료.

**검증 수준**: (외부검증 수준의 in silico) — 학습에 포함되지 않은 보류 세포유형에서 독립 평가. 임상 검증 없음.

**메커니즘 핵심 가정**:
1. 세포유형의 기능적 정체성이 trans-regulator 발현 프로파일 2,891차원으로 충분히 표현된다 — 상피·면역 등 극단적으로 다른 세포유형에서도 성립하는지 추가 확인 필요.
2. FiLM의 feature-wise linear 조건화가 비선형 조절 메커니즘을 충분히 포착한다 — 비선형 상호작용이 강한 케이스에서 bottleneck 가능.
3. DNA 서열 + trans-regulator 발현 두 입력이 epigenome 신호를 결정한다 — 3D 크로마틴 구조 등 추가 인자 미포함.

**강점**:
- peer-reviewed (Nature Communications) — 방법 신뢰도 높음
- 코드·추론 스크립트 공개 → 즉시 재현 가능
- RNA-seq → 후성유전체 변환(Corgi+)은 실험 비용 절감 경로로 실용적
- 새 세포유형 예측이 가능해 희귀 세포유형·환자별 차이 분석에 활용 가능

**한계**:
- trans-regulator 발현 벡터 2,891개 전부 필요 — 불완전한 RNA-seq(낮은 감도 scRNA-seq)에서 입력 품질 저하 위험
- 3D 크로마틴 구조, enhancer-promoter looping 등 공간 게놈 정보는 미포함
- 인간 중심 학습 데이터 — 비인간 생물 적용 시 trans-regulator 목록 재정의 필요
- 추정: Basenji2/Enformer 구조 계승 시 긴 DNA 서열(수십 kb) 처리 계산 비용이 high-throughput 스크리닝에 병목이 될 수 있음

**내 연구 활용**:
해석: RNA-seq 데이터가 있는 연구에서 ChIP-seq·ATAC-seq 없이 후성유전체 프로파일을 1차 스크리닝하는 용도로 코드를 바로 테스트할 수 있다. 특히 임상 샘플처럼 에피게놈 실험이 제한된 환경에서 활용 가능성이 높다. `pip install corgi` 수준의 접근성이 확보됐으므로 재현 장벽이 낮다. 단, NVIDIA Ampere GPU 없이는 추론 속도가 문제가 될 수 있어 계산 환경 확인 선행 필요.

---

### 3. LATTICE: Graph Self-Supervised Learning for Multimodal Spatial Omics Integration
**원문**: https://arxiv.org/abs/2607.14410 | preprint (미동료심사) | arXiv:2607.14410
**저자**: Jagan Mohan Reddy Dwarampudi, Veena Kochat, Suresh Satpati, Kunal Rai, Tania Banerjee | University of Houston + MD Anderson Cancer Center

**문제의식**: 공간 전사체 + 공간 후성유전체 실험이 동시에 수행되기 시작했으나, 하류(downstream) 분석은 여전히 단일 모달리티 파이프라인에 머물러 있다. 5가지 모달리티를 단일 스팟 수준에서 통합하는 계산 틀이 없다.

**기존 한계 → 이번 해결**: 기존 공간 오믹스 통합 방법은 RNA 중심(예: Seurat, STAGATE) 또는 2~3 모달리티 처리에 그친다. LATTICE는 Visium RNA·scMultiome RNA·scMultiome ATAC·공간 ATAC·공간 CUT&Tag 5가지 모달리티를 단일 프레임워크 안에서 스팟-수준 표현으로 통합한다.

**아키텍처/방법**:
- 공간 인접 그래프(spatial neighborhood graph) 구성
- TransformerConv 인코더: 그래프 어텐션으로 이웃 스팟 정보 집계
- 모달리티별 입력 어댑터(modality-specific adapters)로 5가지 이질적 입력을 공통 임베딩 공간으로 변환
- 3가지 학습 목적함수:
  1. 마스크 재구성(masked reconstruction): 마스킹된 모달리티를 나머지로 예측
  2. 교차 모달 정렬(cross-modal alignment): 같은 스팟의 서로 다른 모달리티 표현을 정렬
  3. 공간 평활도(spatial smoothness): 인접 스팟 간 표현 유사성 유도

**데이터**: 암 조직 샘플 (MD Anderson 협업). 정확한 샘플 수·조직 종류·스팟 수 미제공: 초록 기준.

**핵심 수치**: 미제공: 초록에서 구체적 벤치마크 수치 없음. 정량 비교 결과는 원문 확인 필요.

**코드/재현성**: 미제공: 공개 GitHub 레포지토리 미확인. preprint 단계. 재현 어려움.

**검증 수준**: (in silico) — 계산 통합 평가만. 임상 검증 없음. 구체적 벤치마크 방법·대조군 미확인.

**메커니즘 핵심 가정**:
1. 공간적 인접성이 기능적 유사성을 의미한다 — 공간 평활도 목적함수의 전제. 종양 내 이질성(intratumoral heterogeneity)이 강한 경우 이 가정이 깨질 수 있음.
2. 5가지 모달리티가 동일 스팟에 등록(co-registered)되어 있다 — 실험 프로토콜 정확도에 의존.
3. TransformerConv로 포착한 그래프 표현이 각 모달리티의 고유한 생물학적 신호를 손실 없이 집약한다 — 모달리티 수가 많아질수록 정렬 목적함수의 최적화 난이도 상승.

**강점**:
- 5가지 이질적 공간 오믹스 모달리티를 단일 틀로 처리하는 최초 시도 중 하나
- 3가지 상보적 목적함수 조합이 자기지도 학습의 signal 다양성을 확보
- MD Anderson 협업 — 암 공간 오믹스 응용에 실용적 관련성

**한계**:
- 코드 미공개 — 재현 불가, 방법 세부 확인 불가
- 벤치마크 수치 미공개 — 실제 개선 효과 판단 불가
- 5가지 모달리티를 동시에 갖춘 데이터가 현재 드물어 실제 적용 범위 제한적
- preprint이므로 동료심사 전 — 방법 타당성 미검증

**내 연구 활용**:
해석: 공간 전사체 + 공간 후성유전체 데이터를 동시에 처리해야 하는 파이프라인이 있다면 코드 공개 후 추적 가치가 있다. 현재는 코드·수치 미공개 상태이므로 직접 적용보다 방법론적 설계 참고(그래프 SSL + 다목적함수 조합 전략)로 활용하는 수준. 단일 조직 종양 공간 오믹스 프로젝트가 있다면 데이터 구성을 이 프레임워크에 맞출 수 있는지 실험 설계 단계에서 고려.

---

### 4. Screening of Biosecurity Features in Metagenomic Data with Evo 2 Probes
**원문**: https://arxiv.org/abs/2607.14070 | preprint (미동료심사) | arXiv:2607.14070
**저자**: Guntoro 외 | AIxBio Hackathon 2026 참가팀

**문제의식**: 메타게노믹 데이터에서 항생제 내성(AMR) 유전자·독성 인자를 탐지하는 현행 도구(ResFinder, AMRFinderPlus 등)는 데이터베이스 의존적 정렬 기반이다. 게놈 파운데이션 모델이 이 신호를 별도 fine-tuning 없이 이미 내재화하고 있는지 검증된 바 없다.

**기존 한계 → 이번 해결**: 기존 AMR 탐지는 알려진 내성 유전자 데이터베이스 비교에 의존 — 신규 내성 메커니즘·미등록 변이체에 취약. Evo 2의 26번째 레이어 활성화에 경량 프로브(선형·어텐션)만 훈련해, fine-tuning 없이도 AMR과 독성 인자를 탐지할 수 있음을 보인다.

**아키텍처/방법**:
- 기반 모델: Evo 2 (게놈 파운데이션 모델) — 26번째 레이어 활성화 추출, 가중치 동결(frozen)
- 선형 프로브(linear probe): 평균 풀링(mean-pool)으로 시퀀스 표현 집약 후 선형 분류기
- 어텐션 프로브(attention probe): 단일 헤드 어텐션으로 중요 위치 가중 풀링 후 분류기
- 대상: AMR (약제 클래스 수준 세분화 포함) + 독성 인자(virulence factor)
- 검증: 보류된 메타게노믹 테스트 세트에서 평가

**데이터**: 메타게노믹 데이터셋 (구체적 데이터베이스·샘플 수 미제공: 초록 기준). AMR 약제 클래스 세분화 분석 포함.

**핵심 수치** (초록/검색 결과 기반):
- AMR 탐지, 선형 프로브 ROC-AUC: **0.888** (region-level, mean-pool)
- AMR 탐지, 어텐션 프로브 ROC-AUC: **0.977** (region-level, single-head attention)
- 독성 인자 탐지 ROC-AUC: **0.833** (region-level)
- AMR 약제 클래스 subcategory 분리 성능 확인 — 수치 미제공

**코드/재현성**: 미제공: 해커톤 참가작이며 코드 레포지토리 확인 불가. Evo 2 기반 모델 자체는 공개 접근 가능하나, 프로브 훈련 데이터·코드 미공개로 독립 재현 어려움.

**검증 수준**: (in silico) — 보류 메타게노믹 테스트 세트 평가만. 실제 임상·환경 샘플 검증 없음. 전문 AMR 탐지 도구와의 직접 비교 데이터 미제공.

**메커니즘 핵심 가정**:
1. Evo 2 26번째 레이어가 기능적 유전자 분류(AMR·독성)에 충분한 표현을 내재화하고 있다.
2. AMR 신호가 generic 기능 유전자 신호와 구분 가능한 임베딩 공간 구조를 가진다 — 저자가 약제 클래스 분리로 검증 시도.
3. 프로브 학습에 사용된 데이터의 분포가 테스트 메타게노믹 데이터와 충분히 일치한다.

**강점**:
- Fine-tuning 없는 프로빙만으로 AMR AUC 0.977은 실용적으로 높은 수준 — 계산 비용 대비 효율적
- 어텐션 프로브가 선형보다 유의하게 높아 중요 위치 가중 풀링의 효과를 입증
- 파운데이션 모델 임베딩의 AMR·독성 정보 내재화를 검증하는 probe 분석 자체가 방법론적으로 참고할 만함

**한계**:
- 해커톤 참가작 — 소규모 팀, 짧은 개발 기간, 방법 세부 검증 제한적
- 테스트 데이터 규모·다양성 미공개 — AUC 신뢰 구간 불명확
- ResFinder, AMRFinderPlus, DeepARG 등 전문 도구와의 비교 없음 — 실제 성능 이점 불확실
- 독성 인자 AUC 0.833 — AMR 대비 낮아, virulence 특징이 Evo 2 표현에 덜 내재화됨을 시사
- 추정: 훈련 데이터의 AMR 유전자 클래스 분포에 따라 드문 내성 메커니즘에서 성능 저하 가능

**내 연구 활용**:
해석: 메타게노믹 파이프라인에 Evo 2 임베딩을 추가 레이어로 통합하는 아이디어는 실용적이다. 특히 데이터베이스 미등록 내성 변이체 탐지가 필요한 연구에서 테스트 가치가 있다. 코드 미공개가 장벽이지만 프로브 구조 자체는 단순(선형·단일 어텐션 헤드)해서 Evo 2 API를 통해 직접 재현 시도 가능. 전문 AMR 도구 대체보다는 보완적 스크리닝 레이어로 포지셔닝하는 것이 현실적.

---

### 5. Causal Discovery of Radiation Response Mechanisms in Human Cells
**원문**: https://arxiv.org/abs/2607.13994 | preprint (미동료심사) | arXiv:2607.13994
**저자**: Ashka Shah, Rick Stevens | University of Chicago, Department of Computer Science

**문제의식**: 방사선 반응 연구의 기존 바이오인포 도구는 단변량·선형 분석에 그치거나 미리 정의된 경로 지식(KEGG, Reactome)에 의존한다. 어느 유전자가 어느 유전자를 조절하는지의 방향성 인과 구조는 상관 분석으로 복원 불가다.

**기존 한계 → 이번 해결**: 상관 분석·유전자 발현 네트워크(GCN) 방법들은 방향성 없는 공동 발현 구조만 제공한다. 인과 발견(causal discovery) 알고리즘은 교란 조건(방사선 조사)을 활용해 방향성 비순환 그래프(DAG)를 복원하려 시도한다. 저자들은 방사선 선량률(dose rate) 변화를 교란 변수로 삼아 방향성 유전자 조절 네트워크를 학습한다.

**아키텍처/방법**:
- 인과 발견 알고리즘 적용 (추정: NOTEARS, DAGMA 계열의 연속 최적화 기반 — 검색 결과에 언급됨; 구체적 알고리즘명 원문 확인 필요)
- 입력: 방사선 선량률별 인간 세포 유전자 발현 데이터 (RNA-seq 추정: 미확인)
- 출력: 방향성 유전자 조절 DAG
- 알려진 방사선 반응 경로(radiation response pathway) 농축 분석으로 네트워크 검증
- 네트워크 구조 분석: 고 in-degree(허브 수신) 유전자 = 하우스키핑 유전자, 고 out-degree(허브 발신) 유전자 = 전사인자 — 방사선 스트레스 반응의 계층적 구조 시사

**데이터**: 방사선 조사 인간 세포 + 유전자 발현 데이터. 샘플 수·세포주·선량률 범위 미제공: 초록 기준.

**핵심 수치**: 알려진 방사선 반응 경로가 복원된 네트워크에서 기준선(baseline) 대비 유의하게 농축됨 확인(초록 기준). 구체적 농축 배수·p-value 미제공.

**코드/재현성**: 미제공: 공개 코드 레포지토리 미확인. 2인 저자 preprint — 대규모 협업 없이 방법 세부 검증 제한적.

**검증 수준**: (in silico) — 계산 네트워크 분석 + 경로 농축 검증만. 외부 검증 데이터셋·세포주 독립 재현 없음.

**메커니즘 핵심 가정**:
1. 인과 마르코프 조건(Causal Markov Condition)과 충실성(faithfulness) 가정 — 관찰 데이터로 인과 방향을 식별하려면 이 가정이 성립해야 함. 생물학적 네트워크에서는 잠재 교란 인자(latent confounder) 많아 이 가정이 자주 위반됨.
2. 방사선 선량률 변화가 충분한 조건부 독립성 패턴 다양성을 제공한다 — 교란 수가 적으면 방향성 식별 능력 저하.
3. 분석 대상 유전자 공간이 적당히 제한되어 있다 — 인과 발견 알고리즘은 변수 수 p에 대해 O(p³) 이상 계산 복잡도를 가질 수 있어, 전체 전사체 수준 적용은 수치 불안정성 위험.

**강점**:
- 상관 분석을 넘어 방향성 조절 관계 추론을 시도 — 방사선 반응 기전 연구의 방법론적 진전
- 알려진 경로 농축으로 생물학적 타당성 1차 검증
- 네트워크 구조(in/out-degree 분포)가 예상되는 조절 위계(TF → 다운스트림)와 일치 — 질적 확인

**한계**:
- 2인 저자 preprint — 동료심사 전, 방법 신뢰도 낮음
- 인과 발견 알고리즘은 잠재 교란 인자에 취약 — 세포 내 수천 개 미관측 변수 존재
- 선량률 조건 수가 적으면 DAG 식별 가능성(identifiability) 낮아짐 — 실험 설계 세부 미공개
- 경로 농축은 방향성이 맞는지 검증하지 못함 — 무방향 네트워크도 동일한 농축 보일 수 있음
- 코드·데이터 미공개 → 독립 재현 불가

**내 연구 활용**:
해석: 방사선 반응 연구에 직접적 관련성보다는 "교란 데이터(perturbation data)를 인과 발견에 활용하는 방법론"이 유전자 조절 네트워크 연구 전반에 참고 가능하다. 다만 인과 발견 알고리즘의 생물학적 고차원 데이터 적용은 여전히 가정 위반 리스크가 크므로, 이 논문 결과를 재현성 없이 그대로 수용하기보다 방법론 아이디어를 가져와 다른 교란 설계(CRISPR KO, 약물 처리 등)에 적용하는 방향이 현실적.

---

## 와이드 2편 — 방법 요약

---

### W1. Inkling — 오픈웨이트 975B 멀티모달 MoE 모델 (Thinking Machines Lab)
**원문**: https://thinkingmachines.ai/news/introducing-inkling/ | 모델 카드: https://thinkingmachines.ai/model-card/inkling/
**가중치**: https://huggingface.co/thinkingmachines (Apache 2.0)
**출처**: 모델 릴리스 (동료심사 없음) | 2026-07-15

**방법 요약**:
- 66층 디코더-온리 트랜스포머, 총 975B 파라미터, 활성 파라미터 41B/토큰
- MoE(Mixture of Experts): 토큰당 256 전문가 중 6개 라우팅 + 공유 2개 상시 활성
- 컨텍스트 윈도우 1M 토큰
- 멀티모달: 텍스트·이미지·오디오 (45조 토큰으로 사전학습, 텍스트·이미지·오디오·비디오 포함)
- 보고된 벤치마크: FORTRESS Adversarial 78.0%, MMMU Pro 73.5%, VoiceBench 91.4%, CharXiv RQ 82.0% — 생물학 특화 벤치마크 없음 (미제공)

**방법 렌즈 요점**:
- Apache 2.0 라이선스 — 생물의학 도메인 파인튜닝 가능
- 41B 활성 파라미터는 오픈웨이트 생물학 파운데이션 모델(Evo 2, ESM-3 등)에 비해 범용 언어 모델 스케일이며, 멀티모달 처리 능력이 강점
- 미제공: 생물학 태스크 평가 없음. 바이오인포 적용 시 도메인 파인튜닝 결과를 별도 확인 필요
- 해석: 범용 오픈웨이트 멀티모달 모델의 생물의학 벤치마크 기준선 역할을 할 수 있어 추적 가치 있음

---

### W2. SEED: Self-Evolving On-Policy Distillation for Agentic Reinforcement Learning
**원문**: https://arxiv.org/abs/2607.14777 | preprint (미동료심사) | arXiv:2607.14777
**저자**: Jinyang Wu 외 | Tsinghua · Zhejiang · CUHK · NTU · Tongji University
**코드**: https://github.com/jinyangwu/SEED (공개)

**방법 요약**:
- 문제: 장기 에이전트 태스크에서 결과 전용(outcome-only) RL은 희박한 보상(sparse reward)만 제공 — 중간 의사결정 개선 어려움
- 핵심 아이디어: 완료된 온-폴리시 궤적(trajectory)에서 재사용 가능한 '힌드사이트 스킬(hindsight skill)' 자동 추출 → 정책 모델에 내재화 → 이후 RL에서 토큰 수준 밀집 감독(dense supervision) 제공
- 자기 진화 루프: 정책 모델이 궤적 수집 + 스킬 분석 + 파인튜닝 동시 수행 → 스킬이 정책과 함께 진화
- 벤치마크: ALFWorld 매크로 성공률 14.9% → 45.9%pp (결과 전용 RL 대비), 코드 공개
- 메커니즘 핵심 가정: 완료 궤적에서 추출한 자연어 스킬이 미래 유사 태스크에 전이 가능한 재사용 구조를 가진다.

**방법 렌즈 요점**:
- 해석: CellVoyager 류의 생물학 AI 에이전트(문헌 검색, 실험 계획, 멀티스텝 데이터 분석)에 이 프레임워크를 적용할 때 궤적 수집 데이터로 실험 노트·프로토콜을 활용하는 방향이 가능하다.
- 코드 공개 확인 — 즉시 실험 가능
- 한계: ALFWorld(텍스트 기반 가상 환경)에서만 검증됨 — 실험 자동화·생물학 에이전트로의 전이는 별도 검증 필요

---

## 주간 방법 요약 (digest-editor 참고)

| # | 논문 | 방법 키워드 | 신규성 수준 | 코드 공개 | 검증 수준 |
|---|------|------------|-----------|----------|---------|
| 1 | scVision | ViT + MIM + OT gene layout | 높음 (패러다임 전환) | 미공개 | in silico, 6개 held-out |
| 2 | Corgi | FiLM + trans-regulator conditioning | 중상 (기존 모델 확장) | 공개 ✓ | in silico, held-out cell types |
| 3 | LATTICE | GraphSSL + TransformerConv, 5 modalities | 중상 (모달리티 확장) | 미공개 | in silico, 수치 미공개 |
| 4 | Evo 2 Probes | Frozen Evo 2 + lightweight probes | 중 (응용 검증) | 미공개 | in silico, ROC-AUC 수치 제공 |
| 5 | Causal Discovery | Causal discovery on perturbation data | 중 (방법 적용) | 미공개 | in silico, 경로 농축만 |
| W1 | Inkling | MoE 975B, Apache 2.0 | — (릴리스) | 가중치 공개 ✓ | 범용 벤치마크만 |
| W2 | SEED | Hindsight skill distillation + RL | 중 (훈련 방법) | 공개 ✓ | ALFWorld |

---

## 이번 주 방법 패턴 메모

이번 주 5편에서 공통적으로 보이는 경향: **파운데이션 모델의 표현을 새로운 생물학 입력 공간으로 끌어오는 시도**가 다양한 형태로 등장한다. scVision은 이미지 표현, Corgi는 trans-regulator 컨텍스트, Evo 2 Probes는 프로브 분석 — 셋 모두 기존 모델 아키텍처 위에 새로운 입력 표현 방식을 얹는 전략이다. LATTICE는 이질적 모달리티 결합이라는 좀 다른 방향이고, 인과 발견 논문은 방법론 조합(교란 데이터 + DAG 알고리즘) 영역이다.

코드 공개 논문이 7편 중 Corgi와 SEED 두 편뿐이라는 점은 재현성 측면에서 이번 주 수집 결과의 한계다.
