# 전통 컴포넌트와 현대 도구 매핑

상위 노트: [[android-modern-architecture-components]]

| 예전 접근                       | 현대 접근                                | 핵심 변화                        |
|:----------------------------|:-------------------------------------|:-----------------------------|
| 화면마다 Activity 생성            | Single Activity + Compose Navigation | OS 화면 단위에서 앱 내부 라우트 단위로 이동   |
| Activity가 API 호출과 상태 관리     | ViewModel + Repository + Flow        | UI와 비즈니스 로직 분리               |
| Service로 동기화                | WorkManager / JobScheduler           | OS 친화적 예약/재시도                |
| Service로 음악/운동/길안내 유지       | Foreground Service                   | 유저가 인지하는 실시간 장기 실행           |
| Receiver로 앱 내부 이벤트 전달       | StateFlow/SharedFlow/Channel         | 앱 내부 상태/이벤트를 Kotlin 스트림으로 처리 |
| SQLiteOpenHelper 직접 사용      | Room                                 | 타입 안정성, Flow 연동, 마이그레이션 관리   |
| SharedPreferences 직접 사용     | DataStore                            | 코루틴/Flow 기반 비동기 저장           |
| 파일 경로 직접 공유                 | FileProvider                         | `content://` URI와 임시 권한      |
| Provider로 앱 내부 DB 접근        | Repository                           | 외부 공개 API와 내부 저장소 분리         |
| Intent/Provider만으로 agent 연동 | App Functions                        | 앱 기능을 구조화된 함수 계약으로 공개        |

---
