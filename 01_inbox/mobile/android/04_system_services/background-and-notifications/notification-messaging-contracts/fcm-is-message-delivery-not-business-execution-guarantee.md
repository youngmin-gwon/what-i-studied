# FCM은 메시지 전송 서비스이지 비즈니스 실행 보장이 아니다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](01_inbox/mobile/android/04_system_services/android-system-services-and-device-capabilities.md)
관련 지도: [알림과 FCM 메시징 계약](01_inbox/mobile/android/04_system_services/background-and-notifications/notification-messaging-contracts/notification-messaging-contracts.md)
관련 노트: [FCM high priority는 사용자 가시 알림에만 정당화된다](01_inbox/mobile/android/04_system_services/background-and-notifications/notification-messaging-contracts/fcm-high-priority-is-justified-by-user-visible-notification.md), [Android 백그라운드 실행은 보장, 지연, 사용자 가시성으로 선택한다](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/background-execution-is-selected-by-guarantee-delay-and-visibility.md)

## 핵심 정의

Firebase Cloud Messaging(FCM)은 서버가 Android 앱 인스턴스에 메시지를 전달하도록 돕는 전송 서비스다.
FCM은 앱의 비즈니스 서버나 데이터베이스를 대신하지 않는다.
메시지 전달은 알림 표시, 앱 로직 실행, 데이터 동기화를 하나의 보장된 동작으로 묶지 않는다.

## 구성 요소

1. 앱 서버는 Firebase Admin SDK 또는 HTTP v1 API로 신뢰된 환경에서 전송 요청을 만든다.
2. FCM 백엔드는 토큰, Firebase Installation ID, topic 등의 대상 정보를 사용해 라우팅한다.
3. Android 기기의 Google Play services와 FCM SDK가 메시지를 앱 프로세스 또는 시스템 알림 영역으로 전달한다.
4. 앱은 FirebaseMessagingService에서 수신하고, 필요하면 NotificationManager로 알림을 만든다.
5. 사용자가 알림을 누르면 앱의 Activity가 Intent를 받아 목적지와 데이터를 해석한다.

## 전송과 표시의 분리

FCM이 메시지를 기기에 전달했다는 사실은 사용자가 알림을 보았다는 뜻이 아니다.
알림 메시지는 백그라운드에서 SDK가 시스템 트레이에 표시할 수 있다.
data 메시지는 앱이 처리해야 하며, 처리 시간이 길면 별도 작업으로 넘겨야 한다.
알림 권한 거부, 채널 차단, 배터리 정책, 네트워크 상태가 최종 표시를 막을 수 있다.

## 대상 선택

- 특정 앱 인스턴스: 현재 등록 식별자를 사용한다.
- 로그인한 사용자: 사용자 계정과 여러 앱 인스턴스의 식별자를 서버에서 매핑한다.
- 관심사 집합: topic을 사용하되 민감한 사용자 분류를 topic 이름에 노출하지 않는다.

서버는 앱에 전송 권한을 주지 않고, FCM 인증 정보는 앱에 포함하지 않는다.
클라이언트에서 받은 데이터는 신뢰할 수 없는 입력으로 취급하고 서버 권한 검사를 다시 수행한다.

## 설계 경계

FCM은 실시간 연결이나 정확한 순서 전달을 제공하는 스트리밍 시스템이 아니다.
같은 이벤트가 중복되거나 순서가 바뀌어 도착할 수 있으므로 서버 상태를 기준으로 처리한다.
오프라인 기기와 만료된 등록을 고려해 앱 진입 시 보정 동기화를 제공한다.
알림이 비즈니스 작업의 유일한 실행 트리거가 되지 않도록 명시적인 재시도 경로를 둔다.
전달 지연과 누락을 정상적인 운영 조건으로 보고 복구 흐름을 함께 설계한다.

## 참고

- [Firebase Cloud Messaging 개요](https://firebase.google.com/docs/cloud-messaging)
- [Android에서 메시지 수신](https://firebase.google.com/docs/cloud-messaging/android/receive-messages)
- [FCM HTTP v1 전송](https://firebase.google.com/docs/cloud-messaging/send/v1-api)
