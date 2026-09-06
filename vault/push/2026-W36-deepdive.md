🔬 paper-radar Deep Dive — 2026-W36

▸ STV-C8: AI가 RNA를 옮기는 법을 새로 설계했다
RNA 치료제의 역사에서 전달 시스템은 반복적으로 가장 단단한 벽이었다. 1990년대 antisense oligonucleotide 연구자들이 처음 이 벽에 부딪혔고, siRNA·mRNA 시대를 거쳐 Moderna와 BioNTech이 지질나노입자(LNP)로 이 벽을 처음 임상 수준에서 허물었다. 그러나 LNP도 완전한 해답이 아니었다. 간(liver) 외 조직 도달 효율이 낮고, 반복 투여 
이 팀이 선택한 출발점은 생성형 AI, 구체적으로 RFdiffusion이다. David Baker 그룹이 개발·공개한 확산 기반 단백질 구조 설계 도구로, 자연에 존재하지 않는 단백질 구조를 처음부터 설계할 수 있다. 이들은 RFdiffusion으로 C8 사이클릭 대칭 스캐폴드를 설계했다 — 8회 대칭을 가지는 고리 모양 비자연 구조물이다. 여기에 RNA 패키징 기능을 담당하는 천연 단백질 
성능 수치가 크게 언급된다. 세포 배양에서 LNP 대비 검토필요: 1,000배 이상의 형질감염율, 동일 단백질 발현 유도를 위한 mRNA 용량이 검토필요: 100,000배 이상 낮다는 보고다. 이 수치는 언론 보도와 초록 기준이며, 구체적 실험 조건(세포주·RNA 화물 종류·LNP 비교 대상)은 원문 결과 섹션에서 확인이 필요하다. 단일 세포주·단일 실험 조건에서의 결과일 가능성이 높고, 다

▸ ProbeMatchDTI: 모델이 놓치던 신호를 찾는 탐침
DTI 예측 분야는 오래 벤치마크 레이스의 성격을 띠어 왔다. DeepDTA, GraphDTA, MolTrans, DrugBAN이 차례로 BindingDB·DrugBank에서 AUC를 높여왔고, 이미 0.97~0.99 수준에서 포화가 시작됐다. 이 맥락에서 ProbeMatchDTI가 AUC-ROC +2.0%를 달성했다고 주장하면, "그게 임상적으로 무슨 의미인가"라는 질문이 즉시 따라온다.
이 논문에서 수치보다 먼저 주목할 부분은 문제 정의다. 저자들은 기존 딥러닝 DTI 모델이 분자 내 지배적 패턴을 선호하다 보니, 결합 포켓의 기능기(functional group)나 잔기 맥락(residue-context) 같은 약한 신호를 집계 과정에서 억제한다는 구체적 문제를 제기한다. 이 "약한 신호 억제" 문제는 알로스테릭(allosteric) 결합부위나 단편 기반 스크리닝(FBDD
해법이 "탐침(probe)"이다. 학습 가능한 탐침으로 기능기-국소 모티프-분자 스캐폴드 세 척도의 생화학적 대응을 능동적으로 탐색한다. IterProbe 모듈이 문맥 상태를 보존하며 약한 신호를 추출하고, BindingProbe가 원자-잔기 수준의 미시적 대응과 분자 쌍 호환성의 거시적 수준을 연결한다. 4개 공개 벤치마크(BindingDB, DrugBank, C. elegans, Huma

🔗 전체 보기: https://kakyungkim.github.io/paper-radar/2026-W36.html
