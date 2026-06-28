---
type: raw
period: 2026-W26
date_collected: 2026-06-28
sources:
  arxiv_qbio: 3편
  arxiv_csLG: 1편
  nature_medicine: 1편
  wide_nature: 1편
  wide_arxiv: 2편
total_core: 5
total_wide: 3
---

# 2026-W26 논문 수집 (2026-06-28)

수집 범위: 2026-06-22 ~ 2026-06-28  
소스: arXiv(q-bio·cs.LG), Nature Medicine, AICell Lab 뉴스레터(2026-06-23~26)  
중복 제외: W24 5편, W25 7편 (recent-papers.jsonl 기준)

---

# 핵심 논문 (Top 5)

## 1. 유전성 출생결함 변이 우선순위 지정을 위한 근거 기반 에이전트 워크플로 (DeepBD: A Grounded Agentic Workflow for Variant Prioritization and Diagnosis of Genetic Birth Defects)

- **저자**: Shiyu Li, Ziqi Yan, Zhihao Wu, Jielong Lu, Weiran Liao, Jiajun Yu, Genjie Li, Zeyu Chu, Jiajun Bu, Haishuai Wang | Zhejiang University
- **출처**: arXiv:2606.24779 · 2026-06-23 · **preprint(미동료심사)**
- **링크**: https://arxiv.org/abs/2606.24779
- **코드**: 미확인 (논문 내 GitHub 링크 미공개)
- **태그**: [임상ML, 유전체, 희귀질환, 에이전트]
- **사회적 신호**: 없음
- **선택 이유**: 18,622건 태아·영아 코호트로 학습한 LLM 보조 변이 진단 워크플로가 Exomiser·DeepRare 등 기존 베이스라인을 뚜렷이 상회하며, 임상 유전체 진단 파이프라인에 직접 적용 가능한 수준의 시스템 설계를 제시함.
- **초록 요약**: DeepBD는 유전성 출생결함 진단을 위한 에이전트 워크플로로, LLM 보조 케이스 구조화 → 사전학습 증거 엔진 → 전문가 모듈 → 근거 기반 진단 검토 레이어 순으로 구성된다. 자체 보유 태아·영아 코호트 18,622건으로 개발되었으며, 내부 held-out 해결 사례 벤치마크에서 Recall@1/3/5/10이 각각 0.658/0.882/0.912/0.929를 기록해 Exomiser, DeepRare, LLM 재순위화 베이스라인을 모두 상회했다. 제거 분석(ablation)에서 규칙 기반 증거, 기전 맥락, 전문가 세분화가 각각 보완적 신호를 제공한다고 보고한다.

---

## 2. 미관찰 유전자 교란에 대한 전사 반응 예측: 생물학적 구조 기반 Stable-Shift (Stable-Shift: Biologically Structured Prediction of Transcriptional Responses to Unseen Gene Perturbations)

- **저자**: Sajib Acharjee Dip, Liqing Zhang | Department of Computer Science, Virginia Tech
- **출처**: arXiv:2606.24940 · 2026-06-22 · **preprint(미동료심사)**
- **링크**: https://arxiv.org/abs/2606.24940
- **코드**: 미확인
- **태그**: [유전체, 단일세포, 교란예측]
- **사회적 신호**: ACM-BCB 2026 (June 30–July 3) 발표 예정
- **선택 이유**: Perturb-seq 벤치마크에서 GEARS를 코사인 유사도 기준 상회하며, 훈련 중 관찰하지 못한 유전자에 대한 zero-shot 교란 예측이라는 난제를 생물학적 맥락 통합 방식으로 접근한 점이 방법론적으로 새롭다.
- **초록 요약**: Stable-Shift는 단일세포 측정값을 교란 수준 발현 변화량(shift)으로 집계하고, 훈련 교란만으로 저랭크 반응 기저를 구성한 뒤, 새로운 유전자의 좌표를 생물학적 맥락에서 예측한다. 맥락 정보는 STRING 상호작용 네트워크, 대조세포 발현 통계, Gene Ontology 주석을 포함하며 그래프 합성곱으로 통합된다. K562 Perturb-seq 벤치마크에서 코사인 유사도 0.592를 기록해 GEARS(0.569)를 상회했으며, Spearman 상관과 상위 유전자 정밀도에서도 비교 방법 중 최고 성능을 보였다고 보고한다. (초록 기준 수치)

---

## 3. 약물 설계를 위한 통합 다중모달 분자 파운데이션 모델 Molexar (Molexar: A Unified Multimodal Molecular Foundation Model for Drug Design)

- **저자**: Haoyu Lin, Yiyan Liao, Jinmei Pan, Xinliao Ling, Luhua Lai, Jianfeng Pei | Peking-Tsinghua Center for Life Sciences, Peking University
- **출처**: arXiv:2606.25865 · 2026-06-24 · **preprint(미동료심사)**
- **링크**: https://arxiv.org/abs/2606.25865
- **코드**: 미확인 (공개 여부 미확인)
- **태그**: [신약AI, 분자생성, LLM-bio]
- **사회적 신호**: 없음
- **선택 이유**: Fragment-SELFIES라는 분절 인식 분자 언어 위에 단일 자기회귀 경로로 스칼라 분자 특성, 파마코포어, 단백질 서열, 결합 포켓 등 다양한 조건부 생성을 통합한 구조가 방법론적으로 새롭고, CrossDocked2020 및 MolGenBench 결과를 보고한다.
- **초록 요약**: Molexar는 Fragment-SELFIES 기반의 통합 다중모달 분자 파운데이션 모델이다. 사전학습된 자기회귀 디코더가 Fragment-SELFIES 문법과 분자 분포를 학습하고, 지도 파인튜닝(SFT)으로 스칼라 분자 특성·파마코포어 지문·단백질 서열·결합 포켓을 조건으로 하는 분자 생성에 동일 디코더를 재사용한다. 각 조건은 값-토큰 임베딩 인플레이스 교체로 주입돼 모든 생성 모드가 단일 자기회귀 경로를 공유한다. 사전학습 모델은 비조건부 및 분절 제약 생성에서 유효성 100%와 높은 약물 유사성을 달성하고, SFT 모델은 CrossDocked2020 테스트 세트에서 목표 조건부 생성 경쟁력을 유지하며, MolGenBench에서는 안전성 및 효능 지표에서 유리한 결과를 보고한다. (초록 기준 수치)

---

## 4. 유전적 증거와 신약 승인의 연관성: 26,278 타깃-질환 쌍의 관찰 연구 (Human genetic evidence is associated with drug approval across therapeutic areas)

- **저자**: Victoria Paterson | University of Edinburgh
- **출처**: arXiv:2606.14823 · 2026-06-12 · **preprint(미동료심사)**
- **링크**: https://arxiv.org/abs/2606.14823
- **코드**: 미확인
- **태그**: [신약AI, 유전체, 타깃발굴, 바이오인포]
- **사회적 신호**: 없음
- **선택 이유**: Open Targets·ChEMBL 기반 26,278 타깃-질환 쌍이라는 대규모 데이터셋으로 유전적 증거와 신약 승인의 연관성을 정량화하고, 시간적 검증과 특성 제거 분석을 통해 기존 연구의 방법론적 결함(리키지 등)을 보완한 점이 신약개발 타깃 우선순위화에 직접적 함의를 가진다.
- **초록 요약**: Open Targets와 ChEMBL에서 구축된 26,278 타깃-질환 쌍을 분석한 결과, 유전적 연관성이 있는 타깃은 없는 타깃 대비 승인률이 3.25배 높았다(OR=3.25, 95% CI 2.79~3.79). 동일 유전자를 공유하는 쌍 간 비독립성을 보정한 타깃 수준 분석에서는 OR=2.79(부트스트랩 95% CI 2.22~3.53)였다. 이 연관성은 2015년 이후 승인 신약에서도 재현되었고(OR=3.51, p=1.72×10⁻⁸), 6가지 증거 유형에 대한 특성 제거 분석에서는 문헌 마이닝 단독이 분류기 성능의 대부분을 설명해 출판 후 데이터에서 비롯된 시간적 누출(leakage) 가능성을 시사했다. (초록 기준 수치)

---

## 5. 범용 대형언어모델이 전문 임상 AI 도구를 능가한다: 의료 벤치마크 비교 연구 (General-purpose large language models outperform specialized clinical AI tools on medical benchmarks)

- **저자**: Vishwanath K., Alyakin A., Ghosh M., Hage A., Neifert S.N., Orillac C., Mandelberg N.J., Khan H.A., Lee J.V., Yao J.J., Small W.R., Varma A., Hewitt D.B., Aphinyanaphongs Y., Alber D.A., Oermann E.K. | NYU Langone Health / NYU Grossman School of Medicine
- **출처**: DOI: 10.1038/s41591-026-04431-5 · Nature Medicine · 2026-06-12 · **peer-reviewed**
- **링크**: https://www.nature.com/articles/s41591-026-04431-5
- **코드**: https://github.com/nyuolab/clinical-llm-benchmarks
- **태그**: [임상ML, LLM-bio]
- **사회적 신호**: Nature Medicine 게재, 다수 언론 보도(ClinicalTrialVanguard, CryptoBriefing, Digg 등)
- **선택 이유**: FDA 승인 임상 AI 도구(OpenEvidence, UpToDate Expert AI)와 범용 프론티어 LLM(GPT-5.2, Gemini 3.1 Pro, Claude Opus 4.6)을 MedQA·HealthBench·실제 의사 쿼리 세 단계로 비교한 동료심사 연구로, 임상 AI 규제 및 배포 전략에 직접적 파급력이 있다.
- **초록 요약**: 세 단계 평가를 수행했다: (1) MedQA 500문항(의학 지식), (2) HealthBench 500항목(의사 정렬도), (3) 실제 임상 쿼리(RCQ) 벤치마크 — 100건의 익명화된 의사-LLM 질문으로 구성되며 12명의 미국 임상의가 맹검 평가해 1,800건의 모델-질문 주석을 생성했다. 세 가지 프론티어 LLM(GPT-5.2, Gemini 3.1 Pro, Claude Opus 4.6)은 세 평가 단계 모두에서 OpenEvidence와 UpToDate Expert AI를 상회했다. 임상 AI 도구들은 RCQ에서 Google Search AI Overview와 동등한 수준에 머물렀다고 보고한다. (초록 및 보도 기준 수치)

---

# 와이드 (Wide Angle)

## W1. Robin: 과학적 발견을 자동화하는 다중에이전트 시스템 (Robin: A multi-agent system for automating scientific discovery)

- **출처**: arXiv:2505.13400 / DOI:10.1038/s41586-026-10652-y · Nature · 2026 게재 · **peer-reviewed**
- **링크**: https://www.nature.com/articles/s41586-026-10652-y
- **태그**: [AI에이전트, 신약AI, 자율과학]
- **사회적 신호**: Nature 게재, 이번 주 AICell Lab 뉴스레터(2026-06-26) 주요 소개
- **한줄 요약**: 가설 생성·데이터 분석·문헌 검색을 자동화하는 세 개의 특화 서브에이전트(Crow, Falcon, Finch)로 구성된 Robin이 건성 황반변성(dAMD) 대상 신약 후보로 리파수딜(ripasudil) 재창출을 제안하고 in vitro 확인에 성공했다고 보고한다.

## W2. 실험실 로봇을 위한 비전-언어-액션 모델 LabVLA (LabVLA: Grounding Vision-Language-Action Models in Scientific Laboratories)

- **출처**: arXiv:2606.13578 · 2026-06-11 · **preprint(미동료심사)**
- **링크**: https://arxiv.org/abs/2606.13578
- **코드**: https://github.com/zjunlp/LabVLA
- **태그**: [AI에이전트, 로봇, 실험자동화]
- **사회적 신호**: HuggingFace Papers 등재 (https://huggingface.co/papers/2606.13578)
- **한줄 요약**: 실험실 워크플로 시뮬레이션 엔진 RoboGenesis로 구성한 데모로 학습된 LabVLA가 LabUtopia 벤치마크에서 분포 내·외 모두 기존 베이스라인 대비 최고 평균 성공률을 기록했다고 보고한다.

## W3. 게놈·AI로 예측적 가상 배아 만들기 (Towards predictive virtual embryos with genomics and AI)

- **출처**: DOI:10.1038/s41592-026-03055-4 · Nature Methods · 2026-03-26 · **peer-reviewed**
- **링크**: https://www.nature.com/articles/s41592-026-03055-4
- **태그**: [발생학, 유전체, 가상세포]
- **사회적 신호**: 없음
- **한줄 요약**: 단일세포·공간 데이터를 AI와 통합해 포유류 배아 발생을 다중 스케일로 모델링하는 예측적 가상 배아 시스템의 가능성과 과제를 제시하는 리뷰·전망 논문.
