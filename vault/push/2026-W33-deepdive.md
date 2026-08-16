🔬 paper-radar Deep Dive — 2026-W33

▸ RetFold와 DRR: "신규 단백질 폴드"의 기준을 다시 세우다
단백질 구조 생성 AI는 지난 몇 년 사이 RFdiffusion, FrameDiff, Genie 등 확산(diffusion) · 흐름 매칭(flow matching) 기반 모델들이 잇달아 등장하면서 "AI가 자연에 없는 새로운 단백질 구조를 설계할 수 있다"는 서사가 분야를 지배해 왔다. 이 주장의 근거로 흔히 쓰인 지표가 전체 체인 TM-score다. TM-score가 낮으면 자연 단백질과
arXiv:2608.10598이 건드리는 것은 이 논리의 빈틈이다. 전체 체인 TM-score가 낮더라도, 그 구조를 도메인 단위로 쪼개보면 각 도메인 하나하나는 이미 CATH 데이터베이스에 존재하는 것일 수 있다. 도메인들이 이전에 없던 방식으로 연결됐을 때 전체 체인 TM-score는 낮아지지만, 이것을 "신규 폴드"라고 부를 수 있는지는 전혀 다른 문제다. TM-score는 전체 구조를
DRR(Domain Retrieval Rate) 은 이 허점을 메우는 지표다. 생성된 백본에서 각 부분을 CATH S40 데이터베이스의 기존 도메인과 국소 정렬(local alignment)로 비교해, 기존 도메인과 정렬 가능한 비율을 측정한다. DRR이 높으면 생성 모델의 출력물이 기존 도메인 조합으로 구성돼 있다는 의미다. 8개 확산·흐름 매칭 모델을 이 지표로 재평가하면, 대부분 모델의

🔗 전체 보기: https://kakyungkim.github.io/paper-radar/2026-W33.html
