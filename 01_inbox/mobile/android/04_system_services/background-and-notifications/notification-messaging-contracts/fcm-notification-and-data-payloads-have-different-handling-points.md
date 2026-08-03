---
title: fcm-notification-and-data-payloads-have-different-handling-points
tags: ["android", "android/system-services"]
aliases: []
date modified: 2026-08-03 17:36:47 +09:00
date created: 2026-07-31 17:42:24 +09:00
---

## FCM notification payload 와 data payload 는 처리 지점이 다르다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](01_inbox/mobile/android/04_system_services/android-system-services-and-device-capabilities.md)

관련 지도: [알림과 FCM 메시징 계약](01_inbox/mobile/android/04_system_services/background-and-notifications/notification-messaging-contracts/notification-messaging-contracts.md)

관련 노트: [Android 알림은 권한과 채널이 표시 가능성을 결정한다](01_inbox/mobile/android/04_system_services/background-and-notifications/notification-messaging-contracts/android-notification-permission-and-channel-control-visibility.md), [FCM high priority는 사용자 가시 알림에만 정당화된다](01_inbox/mobile/android/04_system_services/background-and-notifications/notification-messaging-contracts/fcm-high-priority-is-justified-by-user-visible-notification.md)

### 두 payload 의 책임

`notification` payload 는 사용자에게 보일 제목, 본문 등 SDK 가 이해하는 표시 정보다.

`data` payload 는 앱이 해석하는 사용자 정의 key-value 데이터다.

두 payload 를 함께 보낼 수도 있지만, 앱 상태에 따라 전달 지점이 달라진다.

HTTP v1 메시지의 payload 전체 크기는 일반적으로 4096 바이트 한도를 고려한다.

### 앱 상태별 동작

| 앱 상태 | notification | data | 둘 다 포함 |
| --- | --- | --- | --- |
| 포그라운드 | `onMessageReceived` | `onMessageReceived` | 콜백에서 둘 다 처리 |
| 백그라운드 | 시스템 트레이 표시 | `onMessageReceived` | 알림은 트레이, data 는 탭 Intent extras |

백그라운드의 notification 메시지는 앱 콜백이 실행되지 않을 수 있다.

notification 과 data 를 함께 보낸 경우 data 를 수신 시점에 처리한다고 가정하지 않는다.

사용자가 알림을 탭했을 때 launcher Activity 의 Intent extras 에서 data 를 읽는 흐름을 설계한다.

### data-only 의 용도와 한계

data-only 는 앱이 알림 내용과 동작을 직접 결정해야 할 때 적합하다.

다만 백그라운드 콜백 실행, 네트워크 접근, 처리 완료, 사용자 표시를 보장하지 않는다.

메시지 수신 콜백은 짧은 실행 창만 가지므로 무거운 동기화는 WorkManager 등으로 넘긴다.

최종 알림은 앱 상태, 알림 권한, 채널 설정, 메시지 우선순위를 함께 고려한다.

### payload 설계 규칙

- payload 에는 화면 이동에 필요한 최소한의 ID 와 버전만 넣는다.
- 비밀번호, 접근 토큰, 주민번호 등 민감정보를 넣지 않는다.
- 서버에서 읽을 최신 상태와 이벤트 ID 를 구분한다.
- 같은 메시지가 여러 번 처리되어도 결과가 망가지지 않게 멱등성을 둔다.
- 탭 처리와 백그라운드 수신 처리를 각각 테스트한다.

### 클릭 이후 처리

알림 탭은 앱이 이미 실행 중인지 새로 시작되는지에 따라 Intent 전달 경로가 달라질 수 있다.

실행 중 Activity 의 새 Intent 와 cold start 의 초기 Intent 를 모두 처리한다.

같은 알림을 반복해서 눌러도 동일 화면이나 동일 이벤트가 중복 실행되지 않게 한다.

data 값이 없거나 만료된 경우에는 안전한 기본 화면으로 이동한다.

### 참고

- [FCM 메시지 유형](https://firebase.google.com/docs/cloud-messaging/customize-messages/set-message-type)
- [Android에서 메시지 수신](https://firebase.google.com/docs/cloud-messaging/android/receive-messages)

검증일: 2026-08-03. notification/data 혼합 메시지의 foreground·background 처리 지점을 Firebase 공식 문서에서 확인했다.
