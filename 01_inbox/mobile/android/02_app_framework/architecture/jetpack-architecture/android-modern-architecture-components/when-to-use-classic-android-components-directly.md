# 언제 전통 컴포넌트를 직접 써야 하나?

상위 노트: [android-modern-architecture-components](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/android-modern-architecture-components.md)

전통 컴포넌트는 구식이라서 버리는 것이 아닙니다. **OS와 직접 계약해야 하는 경계**에서는 여전히 필요합니다.

| 요구사항                         | 필요한 컴포넌트                                        |
|:-----------------------------|:------------------------------------------------|
| 앱 아이콘, 딥 링크, 공유 인텐트로 진입      | Activity                                        |
| 음악/운동/위치 안내처럼 유저가 인지하는 장기 실행 | Foreground Service                              |
| 부팅 완료 후 작업 예약                | BroadcastReceiver + WorkManager 또는 JobScheduler |
| 알림 액션 버튼 처리                  | BroadcastReceiver 또는 Activity/PendingIntent     |
| 다른 앱에 파일 공유                  | FileProvider                                    |
| 다른 앱이 내 구조화 데이터를 조회해야 함      | ContentProvider                                 |
| 시스템/AI agent가 내 앱 기능을 실행해야 함 | App Functions                                   |
| 접근성/입력기/VPN 같은 OS 확장 기능      | 특수 Service                                      |

> [!TIP]
> 판단 기준은 간단합니다. **OS나 다른 앱이 내 코드를 직접 깨워야 하면 4대 컴포넌트 또는 App Functions**, 앱 내부의 상태와 작업 흐름이면 *
*ViewModel/Flow/Repository/WorkManager**를 먼저 생각하면 됩니다.

---
