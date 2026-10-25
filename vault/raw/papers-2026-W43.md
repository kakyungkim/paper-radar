---
week: 2026-W43
period: 2026-10-19 ~ 2026-10-25
collected: 2026-10-25
sources:
  arxiv: 7
  biorxiv: 0
  medrxiv: 0
  pubmed_journal: 0
  total: 7
---

# 2026-W43 수집 논문

수집일: 2026-10-25 / 대상 기간: 2026-10-19 ~ 2026-10-25

소스별 건수: arXiv 7편 (핵심 5 + 와이드 2)

> 수집 방법: GitHub 일별 arXiv 다이제스트(spacenship/newDailyArxiv issues #113–#117), NeurIPS 2026 포스터 목록(neurips.cc), papers.cool 미러, HuggingFace 모델 카드 및 블로그, Pebblous·book.st-hakky 등 2차 요약 사이트 참조. arxiv.org·biorxiv.org·huggingface.co 직접 접근은 에이전트 프록시 차단으로 불가 — 제목·ID는 검색 스니펫 및 다이제스트 기반 추출. 저자명 미확인 논문은 "저자명 미확인" 표기. 초록을 직접 확인하지 못한 논문은 "초록 미확인 (제목·ID 확인)" 표기.
>
> 이번 주 특이사항: NeurIPS 2026 아카이브 공개가 맞물리면서 10월 16~19일 제출 논문 다수가 NeurIPS 2026 포스터로 확인됨. 유전체·전사체·임상ML 분야 강력 후보를 충분히 확인하지 못한 채 단백질·신약AI 쪽으로 편중됨을 메모로 남긴다.

---

## 핵심 (Core)

### [핵심] C1. 재귀적 단백질 언어 모델 대규모 사전훈련 (recAMPLIFY: Large-Scale Pretraining of Recursive Protein Language Models)

- **저자/소속**: Saurav Jha, Qianli Liao, Robert Vernon, Sarath Chandar, Quentin Fournier · Mila / McGill University
- **출처**: arXiv · 2026-10-19 · **preprint(미동료심사)**
- **DOI/링크**: https://arxiv.org/abs/2610.26747
- **코드/데이터**: https://huggingface.co/chandar-lab/recamplify (11개 모델 체크포인트, 훈련·평가 코드 포함)
- **초록 요약** (papers.cool 미러 및 HuggingFace 모델 카드 기반): 마스크드 단백질 언어 모델에 재귀적 사전훈련을 적용한 recAMPLIFY를 제안. 가중치 공유 Transformer 코어가 잔기 수준 은닉 상태를 조절 가능한 사이클 수만큼 반복 정제하므로 추론 시 추가 파라미터 없이 연산을 늘릴 수 있다. 또한 Gated Mixture Recurrence(GMR)를 도입해 각 재귀 단계의 은닉 상태를 확률 가중 혼합으로 디코딩하여 기대 레이어 깊이를 줄인다.
- **핵심 수치**: 155M 고유 파라미터(AMPLIFY-350M 대비 56% 적음) / 동일한 2T 토큰으로 학습 / CASP 접촉 회수율 개선 / 4개 지도학습 태스크 중 3개 향상 / fold 정확도 +22.5% / GMR 적용 시 기대 레이어 깊이 최대 37% 감소 (출처: papers.cool 스니펫)
- **분야 태그**: 단백질 / LLM-bio
- **사회적 신호**: HuggingFace 모델 페이지 공개(chandar-lab/recamplify); Mila 블로그 소개 ("Is Bigger Always Better? Democratizing AI Protein Discovery")
- **선별 사유**: 파라미터 절감(56%)과 성능 개선(fold 정확도 +22.5%)을 동시에 달성하고, 코드·체크포인트를 즉시 사용 가능한 형태로 공개함 — 단백질 설계·기능 예측 파이프라인에 직접 통합 가능한 실용적 기여.

---

### [핵심] C2. 단백질-당질 도킹을 위한 맞춤형 데이터셋·벤치마크·모델 (ProtGlycanDock: Towards Accurate Protein-Glycan Docking with Tailored Dataset, Benchmark and Model)

- **저자/소속**: 저자명 미확인 (NeurIPS 2026 포스터 목록에서 확인; 원문 접근 불가)
- **출처**: arXiv · 2026-10-19 · **preprint(미동료심사)** (NeurIPS 2026 accepted poster)
- **DOI/링크**: https://arxiv.org/abs/2610.26009
- **코드/데이터**: 미확인
- **초록 요약** (NeurIPS 2026 포스터 초록 기반): 단백질-당질(protein-glycan) 도킹 분야는 맞춤형 데이터셋·벤치마크·모델이 없어 발전이 더뎠다. 저자들은 단백질 일반화(protein generalization) 및 당질 일반화(glycan generalization) 두 가지 설정으로 구성된 벤치마크를 구축하고, 물리 기반 방법과 ML 기반 분자 구조 예측 모델 8개를 평가했다. AlphaFold 3가 기존 방법 중 최고 성능을 보였으며, 당질 위상적 특징(glycan topological features) 입력 추가와 당질 에너지 손실(glycan energy loss)을 결합한 미세조정 기법이 AF3를 상회하는 최첨단 도킹 모델을 달성했다.
- **핵심 수치**: 8개 모델 평가 / 단백질·당질 일반화 두 설정 / AF3 기존 방법 중 최고; 미세조정 후 AF3 상회 (출처: NeurIPS 2026 포스터 초록)
- **분야 태그**: 단백질 / 신약AI
- **사회적 신호**: NeurIPS 2026 포스터 채택 (poster #139712)
- **선별 사유**: 당질화(glycosylation)는 항체·수용체 약물 상호작용에서 핵심이지만 도킹 방법론이 크게 뒤처진 분야 — 최초 체계적 벤치마크 + 실용 모델 제시로 즉시 활용 가능성이 높음.

---

### [핵심] C3. 구조 기반 신약 설계 생성 모델의 선택성 평가 (On the Selectivity of Generative Models in Structure-Based Drug Design)

- **저자/소속**: University of Toronto · Université de Montréal 연구팀 (2차 출처 Pebblous 블로그 인용 — 원문 미확인)
- **출처**: arXiv · 2026-10-16 · **preprint(미동료심사)** (NeurIPS 2026 accepted poster)
- **DOI/링크**: https://arxiv.org/abs/2610.24124
- **코드/데이터**: 미확인
- **초록 요약** (NeurIPS 2026 포스터 초록 + Pebblous 블로그 기반): 구조 기반 신약 설계(SBDD) 생성 모델이 목표 단백질에 선택적으로 결합하는 분자를 생성할 수 있는지 평가하는 벤치마크 SelectBench를 소개. 태스크는 ① 문헌 케이스 스터디, ② 제약업계 안전 스크리닝 패널(85개 오프타깃 구조), ③ CrossDocked2020 기반 대규모 구조 쌍(9,900쌍) 세 가지로 구성. 선택성 전용 학습 모델을 포함해 9개 대표 SBDD 모델을 평가한 결과, 선택성 학습 모델도 오프타깃 판별 성능이 미미하고 추론 시 유도(inference-time guidance)도 제한적 개선만 보였다.
- **핵심 수치**: 9개 SBDD 모델 평가 / 85개 오프타깃 구조(안전 패널) / 9,900쌍(대규모 평가 세트) / 엄격한 선택성 기준 미충족 비율 50% 초과 (출처: Pebblous 블로그 스니펫 — 원문 확인 권장)
- **분야 태그**: 신약AI
- **사회적 신호**: NeurIPS 2026 포스터 채택 (poster #138964); Pebblous 블로그 소개
- **선별 사유**: SBDD 분야가 결합 친화도(affinity)에만 집중한 나머지 선택성(selectivity)을 체계적으로 평가하지 않아 왔다는 맹점을 짚음 — 결합 우수 → 부작용 발생 경로의 핵심 약점을 정량화한 첫 체계적 벤치마크.

---

### [핵심] C4. 생명과학 LLM 평가를 위한 그래프 구조 벤치마크 (LG-Bench: A Graph-Structured Evaluation Benchmark for Life Science)

- **저자/소속**: Lu Sun, Xiangyi Zhang, Guangtao Zhai 외 (2차 출처 book.st-hakky.com 인용 — AI 생성 요약이므로 저자명 원문 확인 권장)
- **출처**: arXiv · 2026-10-19 · **preprint(미동료심사)** (NeurIPS 2026 accepted poster)
- **DOI/링크**: https://arxiv.org/abs/2610.26787
- **코드/데이터**: 미확인
- **초록 요약** (NeurIPS 2026 포스터 초록 + book.st-hakky 스니펫 기반): 기존 생명과학 LLM 평가 벤치마크는 개념들 간의 상호연결성을 무시하고 독립적 질문으로만 구성된다는 한계를 지적. 의학·생물학·화학에 걸쳐 10,000개 이상의 고품질 4지선다 문항을 구성하고, 양방향 매칭과 의미적 유사도로 질문을 그래프 노드로 연결함. 모델이 연관된 질문들을 일관되게 답하는지 측정하는 Global Coherence Score와 오답이 특정 개념 영역에 집중되는지 시각화하는 Knowledge Balance Score(KBS)를 새롭게 제안. 현행 LLM의 생명과학 개념적 맹점을 드러냄.
- **핵심 수치**: 10,000개 이상 MCQ / 의학·생물학·화학 3개 도메인 / KBS·Global Coherence Score 2개 신규 지표 (출처: NeurIPS 2026 포스터 초록 + 2차 요약)
- **분야 태그**: LLM-bio / 바이오인포
- **사회적 신호**: NeurIPS 2026 포스터 채택 (poster #139764); book.st-hakky.com 소개
- **선별 사유**: 생명과학 LLM 성능을 단순 정확도가 아닌 개념 간 일관성과 맹점 분포로 평가한다는 새로운 프레임 — 생물의학 LLM 선택·도입 시 기준선으로 직접 사용 가능.

---

### [핵심] C5. 모듈식 확산 스티어링을 통한 다목적 단백질 최적화 (Multi-Objective Protein Optimization via Modular Diffusion Steering)

- **저자/소속**: 저자명 미확인 (GitHub 일별 다이제스트 제목 확인; 원문 접근 불가)
- **출처**: arXiv · 2026-10-20 · **preprint(미동료심사)**
- **DOI/링크**: https://arxiv.org/abs/2610.28943
- **코드/데이터**: 미확인
- **초록 요약** (초록 미확인 — GitHub 다이제스트 제목 및 관련 문헌 맥락 기반 추정): 확산 모델(diffusion model) 기반 스티어링(steering)을 모듈화하여 단백질 서열 최적화에서 항균 활성·독성·결합력 등 복수의 상충 목표를 동시에 최적화하는 프레임워크를 제안하는 것으로 추정. 동계 연구 MoMST(ICML 2026), MP2D(IJCAI 2026)와 유사한 다목적 단백질 최적화 방향성을 지님.
- **핵심 수치**: 미확인 (원문 직접 확인 필요)
- **분야 태그**: 신약AI / 단백질
- **사회적 신호**: 없음
- **선별 사유**: 실제 신약 후보 단백질(항체·펩타이드)은 결합력 단독이 아닌 복수 목표를 동시에 만족해야 하므로, 다목적 최적화 방법론은 응용 가치가 높음 — 제목 확인 수준이므로 분석가가 원문 초록 확인 후 세부 평가 권장.

---

## 🔭 와이드 (Wide)

### [와이드] W1. 과학 탐색으로 확장된 장기 실행 에이전트: Sage-A1.5 (Sage-A1.5: From Long-Horizon Execution to Scientific Exploration with Capability Composition)

- **arXiv/DOI**: https://arxiv.org/abs/2610.28578
- **저자**: 저자명 미확인 (Shanghai Artificial Intelligence Laboratory 소속으로 추정 — HyperAI 미러 기반)
- **날짜**: 2026-10-20
- **상태**: preprint(미동료심사)
- **한 줄 요약**: 35B MoE 에이전트 모델 Sage-A1.5는 병렬 하위 에이전트 오케스트레이션, 증거 기반 자기 교정(verification), 과학적 발견 모드를 조합하여 장기 과학 탐색 태스크를 수행한다고 주장. FrontierScience-Olympiad 등 벤치마크에서 대형 경쟁 모델을 상회했다고 보고하나 원문 수치 미확인.
- **와이드 선택 사유**: 과학 탐색 자동화 에이전트는 장기적으로 바이오인포 워크플로우 자동화(OmicsBench류 태스크 수행)와 연결되는 트렌드로, 방향성 파악 차원에서 모니터링 가치가 있음.

---

### [와이드] W2. 다중모달 기억과 도구 사용을 갖춘 시각 에이전트 하네스 (OpenVLHarness: Real World Visual Agentic Tool-Use with Multimodal Memory)

- **arXiv/DOI**: https://arxiv.org/abs/2610.26860
- **저자**: 저자명 미확인 (papers.cool 및 deeplearn.org 미러 기반; 소속 Apple 일부 보고 — 미확인)
- **날짜**: 2026-10-19
- **상태**: preprint(미동료심사)
- **한 줄 요약**: 이미지·구조화 데이터·웹 참조를 아티팩트로 유지하는 다중모달 영속 기억(persistent multimodal memory)과 도구 실행 인터페이스를 결합한 에이전트 하네스. 22개 벤치마크·8개 백본에서 도구 미사용 대비 +9.7~+12.6점(Qwen3-VL-8B 기준 +11.2)을 보고.
- **와이드 선택 사유**: 다중모달 기억 + 코드 실행 프레임워크는 문헌·실험 데이터 통합 분석이 빈번한 생물의학 연구 보조 도구 설계 패턴으로 참고할 만함.

---

## 수집 메모

- **검색 쿼리**: "arxiv bioinformatics machine learning October 2026", "arxiv 2610 protein drug discovery October 2026", "NeurIPS 2026 poster genomics clinical drug discovery", "HuggingFace daily papers biology October 2026", GitHub spacenship/newDailyArxiv issues #113–117 직접 열람 등
- **유효 중복 제외**: W42 제외 목록(2610.16093·2610.17108·2610.18879·2610.19029·2610.21074·2610.15182·2610.20288) 및 W41(2610.07340·2610.07607·2610.08736·2610.11222) 전량 제외. C3 SelectBench(2610.24124, 10-16 제출)는 W42 제외 목록에 없고 이번 주 다이제스트에서 처음 부각됨 — 포함 처리.
- **분야 편중**: 이번 주는 NeurIPS 2026 아카이브 공개와 맞물려 단백질·신약AI 논문이 다수 노출됨. 유전체·전사체·멀티오믹스, 임상ML 분야 강력 후보를 충분히 확인하지 못함 — arxiv.org·biorxiv.org 직접 접근 차단이 주된 원인.
- **정보 신뢰도 주의**: 저자명·소속·핵심 수치는 NeurIPS 2026 포스터 초록, papers.cool, HuggingFace 카드, 2차 블로그 스니펫 기반이며 arXiv 원문 직접 확인이 안 된 경우 "미확인" 표기. 분석가 단계에서 원문 재확인 권장.
- **다음 주 참고**: C5(2610.28943) 다목적 단백질 최적화는 원문 미확인 상태이므로, 분석가가 초록·방법·결과 섹션을 먼저 열람 후 분석 진행 권장.
