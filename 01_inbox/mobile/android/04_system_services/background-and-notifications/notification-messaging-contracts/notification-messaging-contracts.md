---
title: "알림과 FCM 메시징 계약"
tags: ["android", "android/system-services"]
---

# 알림과 FCM 메시징 계약

이 지도는 FCM 전송, 앱 인스턴스 식별, payload 처리, Android 알림 권한과 채널, 운영 관측을 분리한다.

## 정본 노트

- [FCM은 메시지 전송 서비스이지 비즈니스 실행 보장이 아니다](01_inbox/mobile/android/04_system_services/background-and-notifications/notification-messaging-contracts/fcm-is-message-delivery-not-business-execution-guarantee.md)
- [FCM 등록 식별자는 사용자 계정이 아니라 앱 인스턴스를 가리킨다](01_inbox/mobile/android/04_system_services/background-and-notifications/notification-messaging-contracts/fcm-registration-identifier-targets-app-instance-not-user-account.md)
- [FCM notification payload와 data payload는 처리 지점이 다르다](01_inbox/mobile/android/04_system_services/background-and-notifications/notification-messaging-contracts/fcm-notification-and-data-payloads-have-different-handling-points.md)
- [Android 알림은 권한과 채널이 표시 가능성을 결정한다](01_inbox/mobile/android/04_system_services/background-and-notifications/notification-messaging-contracts/android-notification-permission-and-channel-control-visibility.md)
- [FCM high priority는 사용자 가시 알림에만 정당화된다](01_inbox/mobile/android/04_system_services/background-and-notifications/notification-messaging-contracts/fcm-high-priority-is-justified-by-user-visible-notification.md)
- [FCM 운영은 전달, 표시, 탭, 복구를 분리해 관측한다](01_inbox/mobile/android/04_system_services/background-and-notifications/notification-messaging-contracts/fcm-operations-observe-delivery-display-tap-and-recovery-separately.md)

관련 지도: [백그라운드 작업 계약](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/background-work-contracts.md)
