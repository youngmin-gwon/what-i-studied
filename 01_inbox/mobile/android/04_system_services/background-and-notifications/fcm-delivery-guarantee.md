---
title: fcm-delivery-guarantee
tags: ["android", "android/system-services"]
aliases: []
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-07-31 17:42:24 +09:00
---

## FCM 은 메시지 전송 서비스이지 비즈니스 실행 보장이 아니다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](../android-system-services-and-device-capabilities.md)
배경 지식: [HTTP 프로토콜](../../../../computer-science/networking/http-protocol.md)

관련 지도: [알림과 FCM 메시징 계약](notification-messaging.md)

관련 노트: [FCM high priority는 사용자 가시 알림에만 정당화된다](fcm-high-priority.md), [Android 백그라운드 실행은 보장, 지연, 사용자 가시성으로 선택한다](background-execution-selection.md)

### 핵심 정의

Firebase Cloud Messaging(FCM)은 서버가 Android 앱 인스턴스에 메시지를 전달하도록 돕는 전송 서비스다.

FCM 은 앱의 비즈니스 서버나 데이터베이스를 대신하지 않는다.

메시지 전달은 알림 표시, 앱 로직 실행, 데이터 동기화를 하나의 보장된 동작으로 묶지 않는다.

### 구성 요소

1. 앱 서버는 Firebase Admin SDK 또는 HTTP v1 API 로 신뢰된 환경에서 전송 요청을 만든다.
2. FCM 백엔드는 토큰, Firebase Installation ID, topic 등의 대상 정보를 사용해 라우팅한다.
3. Android 기기의 Google Play services 와 FCM SDK 가 메시지를 앱 프로세스 또는 시스템 알림 영역으로 전달한다.
4. 앱은 FirebaseMessagingService 에서 수신하고, 필요하면 NotificationManager 로 알림을 만든다.

```kotlin
override fun onMessageReceived(message: RemoteMessage) {
    val data: Map<String, String> = message.data
    // 여기서는 짧은 처리만 하고 긴 작업은 WorkManager 등으로 넘긴다.
}
```
5. 사용자가 알림을 누르면 앱의 Activity 가 Intent 를 받아 목적지와 데이터를 해석한다.

### 전송과 표시의 분리

FCM 이 메시지를 기기에 전달했다는 사실은 사용자가 알림을 보았다는 뜻이 아니다.

알림 메시지는 백그라운드에서 SDK 가 시스템 트레이에 표시할 수 있다.

data 메시지는 앱이 처리해야 하며, 처리 시간이 길면 별도 작업으로 넘겨야 한다.

알림 권한 거부, 채널 차단, 배터리 정책, 네트워크 상태가 최종 표시를 막을 수 있다.

### 대상 선택

- 특정 앱 인스턴스: 현재 등록 식별자를 사용한다.
- 로그인한 사용자: 사용자 계정과 여러 앱 인스턴스의 식별자를 서버에서 매핑한다.
- 관심사 집합: topic 을 사용하되 민감한 사용자 분류를 topic 이름에 노출하지 않는다.

서버는 앱에 전송 권한을 주지 않고, FCM 인증 정보는 앱에 포함하지 않는다.

클라이언트에서 받은 데이터는 신뢰할 수 없는 입력으로 취급하고 서버 권한 검사를 다시 수행한다.

### 설계 경계

FCM 은 실시간 연결이나 정확한 순서 전달을 제공하는 스트리밍 시스템이 아니다.

같은 이벤트가 중복되거나 순서가 바뀌어 도착할 수 있으므로 서버 상태를 기준으로 처리한다.

오프라인 기기와 만료된 등록을 고려해 앱 진입 시 보정 동기화를 제공한다.

알림이 비즈니스 작업의 유일한 실행 트리거가 되지 않도록 명시적인 재시도 경로를 둔다.

전달 지연과 누락을 정상적인 운영 조건으로 보고 복구 흐름을 함께 설계한다.

### 참고

- [Firebase Cloud Messaging 개요](https://firebase.google.com/docs/cloud-messaging)
- [Android에서 메시지 수신](https://firebase.google.com/docs/cloud-messaging/android/receive-messages)
- [FCM HTTP v1 전송](https://firebase.google.com/docs/cloud-messaging/send/v1-api)

검증일: 2026-08-03. FCM 은 메시지 전송 계층이며 표시, 사용자 탭, 비즈니스 작업 완료는 별도 관측 대상이다.