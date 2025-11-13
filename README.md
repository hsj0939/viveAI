# Novel AI Editor (소설 AI 편집기)

---

## [cite_start]1. 제품 개요 [cite: 2]
[cite_start]이 제품은 소설 작가를 위한 데스크탑 AI 도우미 앱입니다. [cite: 3] [cite_start]작가가 집필한 원고 텍스트를 업로드하면, AI가 캐릭터 및 세계관 설정의 일관성을 분석하고, 챕터별 구조와 개연성 흐름을 점검합니다. [cite: 3]

[cite_start]또한, 작가는 대화형 인터페이스를 통해 원고에 관한 질문을 직접 입력하고, AI로부터 전문 편집자 수준의 피드백을 받을 수 있습니다. [cite: 4]

## [cite_start]2. 목표 [cite: 5]
* [cite_start]작가가 원고 단계에서 오류와 불일치를 빠르게 탐지하도록 돕습니다. [cite: 6]
* [cite_start]독자 관점의 이해도와 개연성을 보장할 수 있도록 지원합니다. [cite: 7]
* [cite_start]기존 편집자 피드백 이전 단계에서, 작가가 스스로 원고의 품질을 높이는 데 기여합니다. [cite: 8]

## [cite_start]3. 주요 사용자 [cite: 9]
* [cite_start]**핵심 타깃**: 소설 작가 (초보부터 프로 작가까지) [cite: 10]
* [cite_start]**2차 타깃**: 출판사 편집자, 베타리더, 문예 창작 학습자 [cite: 11]

## [cite_start]4. 주요 기능 (MVP) [cite: 12]

### [cite_start]1. 원고 텍스트 업로드/불러오기 [cite: 13]
* [cite_start]지원 포맷: `.txt`, `.docx`, `.pdf` [cite: 14]
* [cite_start]문서 내 챕터 구분 자동 인식 [cite: 15]

### [cite_start]2. 캐릭터 및 세계관 불일치 탐지 [cite: 16]
* [cite_start]인물 이름, 관계, 배경 지형, 세계관 설정의 모순 자동 식별 [cite: 17]
* [cite_start]주요 불일치 사례를 리포트 형식으로 제공 [cite: 18]

### [cite_start]3. 챕터별 구조 분석 [cite: 19]
* [cite_start]각 챕터의 주요 사건 요약 [cite: 20]
* [cite_start]플롯 진행의 개연성 평가 [cite: 21]
* [cite_start]서사 흐름의 약점 및 강점 표시 [cite: 22]

### [cite_start]4. 대화형 모드 (QA 인터페이스) [cite: 23]
* [cite_start]작가가 자유롭게 질문 가능 [cite: 24]
* [cite_start]예: "이 장면에서 독자가 혼란스러워할까?" [cite: 25]
* [cite_start]AI가 전문 편집자 톤으로 답변 [cite: 26]

## [cite_start]5. 사용자 경험(UX 플로우) [cite: 28]
1.  [cite_start]앱 실행 → 메인 화면에서 대화형 인터페이스 제공 [cite: 29]
2.  [cite_start]작가가 원고 파일 업로드 → 자동 분석 실행 [cite: 30]
3.  [cite_start]분석 결과는 사이드 패널/별도 창에서 확인 가능 [cite: 31]
    * [cite_start]캐릭터/세계관 불일치 리포트 [cite: 32]
    * [cite_start]챕터별 구조 분석 요약 [cite: 33]
4.  [cite_start]작가는 대화 인터페이스에서 AI와 질문/답변 진행 [cite: 34]
5.  [cite_start]필요 시 분석 패널과 대화창을 오가며 집필 보완 [cite: 35]

## [cite_start]6. AI 답변 톤 및 스타일 [cite: 36]
* [cite_start]전문가 편집자 톤 유지 [cite: 37]
* [cite_start]직접적이고 구체적인 피드백 제공 [cite: 38]
* [cite_start]단점과 개선점을 명확히 제안 [cite: 39]
* [cite_start]불필요한 격려나 장식적 언어 최소화 [cite: 40]

## [cite_start]7. 비기능적 요구사항 [cite: 41]
* [cite_start]**보안성**: 원고 데이터가 외부 서버로 유출되지 않도록 로컬 저장 우선 [cite: 42]
* [cite_start]**오프라인 지원**: 인터넷 연결이 없어도 기본 분석 가능 [cite: 43]
* [cite_start]**성능 최적화**: 수십만 자 규모 원고도 원활히 처리 [cite: 44]

## [cite_start]8. 기술 요구사항 [cite: 45]

### [cite_start]개발 언어 및 프레임워크 [cite: 46]
* [cite_start]`Python` 기반 AI 분석 엔진 (NLP/LLM 활용) [cite: 47]
* [cite_start]`Electron` 또는 `Tauri`를 활용한 크로스플랫폼 데스크탑 앱 개발 [cite: 48]
* [cite_start]로컬 DB (`SQLite`)로 사용자 데이터 및 분석 결과 저장 [cite: 49]

### [cite_start]AI 모델 활용 [cite: 50]
* [cite_start]캐릭터 및 세계관 불일치 탐지를 위한 **Named Entity Recognition (NER)** [cite: 51]
* [cite_start]챕터별 구조 분석용 **텍스트 요약 모델** [cite: 52]
* [cite_start]대화형 QA용 **대형 언어 모델 (LLM)** [cite: 53]

### [cite_start]보안/프라이버시 [cite: 54]
* [cite_start]모든 데이터 로컬 처리 (기본) [cite: 55]
* [cite_start]클라우드 기능은 선택적 (추가 로그인/동기화 시) [cite: 56]

## [cite_start]9. 와이어프레임 흐름 (초안) [cite: 58]

### [cite_start]메인 화면 [cite: 59]
* [cite_start]**중앙**: 대화형 인터페이스 (질문/답변) [cite: 60]
* [cite_start]**상단**: 원고 업로드 버튼 (`txt`/`docx`/`pdf`) [cite: 61]
* [cite_start]**우측 패널**: 분석 결과 보기 버튼 [cite: 62]

### [cite_start]분석 결과 패널 [cite: 63]
* [cite_start]**탭 구조**: [cite: 64]
    * [cite_start]캐릭터/세계관 불일치 [cite: 65]
    * [cite_start]챕터 구조 분석 [cite: 66]
* [cite_start]각 항목에 요약 리포트 및 세부 내용 제공 [cite: 68]

### [cite_start]대화창 [cite: 67]
* [cite_start]**하단 입력창**: 질문 입력 [cite: 69]
* [cite_start]**중앙 대화 기록**: AI 답변 표시 (전문가 편집자 톤) [cite: 70]
* [cite_start]특정 답변에 "자세히 보기" 클릭 시 분석 패널 자동 연동 [cite: 71]

## [cite_start]10. 향후 확장 기능 (로드맵) [cite: 72]
* [cite_start]**문체 분석**: 어휘 반복, 문체 톤 불일치 감지 [cite: 73]
* [cite_start]**독자 페르소나 시뮬레이션**: 타깃 독자의 반응 예측 [cite: 74]
* [cite_start]**장르별 클리셰 탐지**: 판타지/스릴러/로맨스 등 장르별 패턴 분석 [cite: 75]
* [cite_start]**작업 히스토리 관리**: 이전 분석 결과와 비교 기능 [cite: 76]
* [cite_start]**협업 모드**: 공동 작가/편집자와 함께 리뷰 가능 [cite: 77]

## [cite_start]11. 성공 지표(KPI) [cite: 78]
* [cite_start]작가 사용자의 원고 오류 탐지 만족도 (설문 기반) [cite: 79]
* [cite_start]앱 내 평균 세션 길이 (집필+분석 사용 시간) [cite: 80]
* [cite_start]재사용률/잔존율: 반복적으로 쓰는 작가 비율 [cite: 81]
* [cite_start]작가가 편집자에게 제출 전 원고 퀄리티 향상 경험 보고 [cite: 82]

## [cite_start]12. 결론 [cite: 83]
[cite_start]이 제품은 소설 작가들이 원고 품질을 사전에 개선할 수 있도록 돕는 데스크탑 AI 도우미입니다. [cite: 84] [cite_start]핵심은 **일관성 분석 + 구조 피드백 + 대화형 전문가 상담**이며, 초기 MVP는 4개의 필수 기능을 중심으로 설계됩니다. [cite: 85] [cite_start]이후 확장 기능을 통해 편집자와 협업하거나 독자 반응을 시뮬레이션하는 방향으로 발전할 수 있습니다. [cite: 86]
