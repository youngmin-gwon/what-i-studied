# Android Task와 App Back Stack

상위 노트: [[jetpack-navigation-3-guide]]

Navigation 3의 `NavBackStack`은 앱 내부 Compose 화면 이동 상태입니다. Android OS의 `Task`는 Activity 단위 실행 이력입니다. 둘은 이름이 비슷하지만 책임이 다릅니다.

| 항목 | 책임 |
|:---|:---|
| Android `Activity` | OS가 실행하고 intent를 전달하는 앱 창 |
| Android `Task` | 최근 앱 화면에 보이는 Activity 실행 이력 |
| Navigation 3 `NavBackStack` | Compose 화면 key의 앱 내부 이동 이력 |

Single Activity 구조에서는 외부 intent를 `MainActivity`가 받고, 이후 화면 분기는 Navigation 3 back stack 조작으로 처리합니다.

본인인증, 결제 인증처럼 외부 앱 Activity가 끼어드는 흐름에서는 Android Task 동작도 UX에 영향을 줍니다. 하지만 앱 내부 화면 이동은 여전히 `NavBackStack`을 기준으로 복원하고 검증해야 합니다.

---
