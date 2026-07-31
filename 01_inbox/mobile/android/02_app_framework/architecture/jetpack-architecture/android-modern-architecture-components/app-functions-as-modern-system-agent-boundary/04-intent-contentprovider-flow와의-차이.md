# Intent, ContentProvider, Flow와의 차이

| 비교 대상                | App Functions와의 차이                                                            |
|:---------------------|:------------------------------------------------------------------------------|
| `Intent`             | Intent는 "이 화면/액션을 처리해줘"에 가깝고, App Functions는 agent가 검색 가능한 구조화된 기능 계약에 가깝습니다. |
| `ContentProvider`    | ContentProvider는 데이터를 조회/수정하는 창구이고, App Functions는 앱의 동작을 실행하는 창구입니다.         |
| `Flow` / `StateFlow` | Flow는 앱 내부 프로세스의 상태 흐름이고, App Functions는 앱 밖의 시스템/agent가 호출하는 경계입니다.          |
| `WorkManager`        | WorkManager는 내 앱의 백그라운드 작업 예약이고, App Functions는 외부 agent가 내 앱 기능을 실행하는 통로입니다. |
