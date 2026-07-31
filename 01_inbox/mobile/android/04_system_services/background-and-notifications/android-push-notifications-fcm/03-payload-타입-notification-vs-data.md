# Payload 타입: Notification vs Data

FCM 메시지는 두 가지 타입의 페이로드를 가질 수 있으며, 앱의 상태에 따라 동작 방식이 결정적으로 달라진다.

| 타입 | 구조 | 앱이 백그라운드/킬(Killed)일 때 |
| :--- | :--- | :--- |
| **Notification** | `notification` 키 포함 | 시스템이 **자동으로** 알림창에 띄움. 앱 코드는 타지 않음. |
| **Data** | `data` 키 포함 (Key-Value) | `onMessageReceived` 가 호출됨. 개발자가 직접 알림을 띄우거나 작업 수행 가능. |
| **Combined** | 둘 다 포함 | 시스템이 알림을 띄우고, 사용자가 클릭하면 `Intent` 의 `extras` 로 데이터 전달. |

>[!IMPORTANT] **Devil's Advocate : Data 페이로드를 기본으로 하라**
>알림의 커스터마이징(아이콘, 채널, 행동 등)을 완전히 제어하고 싶다면 서버에서 `notification` 키를 빼고 `data` 키만 보내는 **Data-only message**를 권장한다. 이렇게 하면 앱이 백그라운드에서도 `onMessageReceived` 를 통해 로직을 수행할 수 있다.
