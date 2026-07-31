# 선택 기준 요약

상위 노트: [kotlin-coroutines-flow-stateflow](01_inbox/mobile/android/02_app_framework/data/async-flow/kotlin-coroutines-flow-stateflow.md)

| 하고 싶은 일                              | 도구                                  |
|:-------------------------------------|:------------------------------------|
| 네트워크 요청을 한 번 실행                      | `suspend` 함수 + Coroutine            |
| 버튼 클릭 후 저장 작업 실행                     | `viewModelScope.launch`             |
| 화면에 보여줄 최신 UI 상태 관리                  | `StateFlow`                         |
| DB 변경을 화면에 자동 반영                     | Room `Flow` + ViewModel `StateFlow` |
| 검색어 변경마다 최신 검색만 실행                   | `debounce` + `flatMapLatest`        |
| 여러 데이터 출처를 하나의 화면 상태로 합침             | `combine`                           |
| Snackbar/Toast/Navigation 같은 일회성 이벤트 | `SharedFlow` 또는 `Channel`           |
| 콜백 기반 시스템 API를 스트림으로 변환              | `callbackFlow`                      |
| 앱이 꺼져도 해야 하는 작업                      | `WorkManager` + `CoroutineWorker`   |

---
