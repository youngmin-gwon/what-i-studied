# Context의 대표 종류

상위 노트: [android-context](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/android-context.md)

`Context`라고 다 같은 Context가 아닙니다. 수명과 역할이 다릅니다.

| 종류                             | 수명                  | 적합한 사용                                          | 피해야 할 사용                |
|:-------------------------------|:--------------------|:------------------------------------------------|:------------------------|
| `Application Context`          | 앱 프로세스가 살아있는 동안     | Repository, DataStore, Room, WorkManager, 파일 경로 | 화면 테마가 필요한 Dialog/UI    |
| `Activity Context`             | Activity 인스턴스 수명    | 화면 열기, Dialog, UI theme, Activity Result        | singleton에 저장           |
| `Service Context`              | Service 실행 수명       | foreground service 알림/작업                        | 화면 UI 소유                |
| `BroadcastReceiver`의 `context` | `onReceive()` 호출 동안 | 짧은 처리, WorkManager 예약                           | 긴 작업 직접 실행              |
| `ContentProvider`의 `context`   | provider 초기화 이후     | provider 내부 리소스/DB 접근                           | UI 작업                   |
| Compose `LocalContext.current` | 현재 Composition 위치   | Intent 실행, 리소스 접근, Android API 연결               | 장기 보관, ViewModel 필드로 저장 |

---
