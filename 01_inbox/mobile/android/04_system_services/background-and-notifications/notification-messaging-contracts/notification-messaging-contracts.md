---
title: "알림과 FCM 메시징 계약"
tags: ["android", "android/system-services"]
---

# 알림과 FCM 메시징 계약

이 지도는 FCM 전송, 앱 인스턴스 식별, payload 처리, Android 알림 권한과 채널, 운영 관측을 분리한다.

## 읽는 순서

1. [FCM은 메시지 전송 서비스이지 비즈니스 실행 보장이 아니다](01_inbox/mobile/android/04_system_services/background-and-notifications/notification-messaging-contracts/fcm-is-message-delivery-not-business-execution-guarantee.md)로 전송과 실행을 분리한다.
2. [FCM 등록 식별자는 사용자 계정이 아니라 앱 인스턴스를 가리킨다](01_inbox/mobile/android/04_system_services/background-and-notifications/notification-messaging-contracts/fcm-registration-identifier-targets-app-instance-not-user-account.md)로 서버 대상 모델을 잡는다.
3. [FCM notification payload와 data payload는 처리 지점이 다르다](01_inbox/mobile/android/04_system_services/background-and-notifications/notification-messaging-contracts/fcm-notification-and-data-payloads-have-different-handling-points.md)와 [Android 알림은 권한과 채널이 표시 가능성을 결정한다](01_inbox/mobile/android/04_system_services/background-and-notifications/notification-messaging-contracts/android-notification-permission-and-channel-control-visibility.md)로 수신과 표시를 나눈다.
4. [FCM high priority는 사용자 가시 알림에만 정당화된다](01_inbox/mobile/android/04_system_services/background-and-notifications/notification-messaging-contracts/fcm-high-priority-is-justified-by-user-visible-notification.md)와 [FCM 운영은 전달, 표시, 탭, 복구를 분리해 관측한다](01_inbox/mobile/android/04_system_services/background-and-notifications/notification-messaging-contracts/fcm-operations-observe-delivery-display-tap-and-recovery-separately.md)로 운영 정책을 정한다.

## 문제 분류

| 관측 | 확인할 경계 |
| --- | --- |
| 서버 전송 요청 실패 | HTTP v1 인증, payload, 대상 등록 |
| 전송 성공이나 앱 콜백 없음 | 메시지 유형, 앱 상태, priority, 기기 연결 |
| 콜백은 왔으나 알림 없음 | `POST_NOTIFICATIONS`, 앱·채널 차단, 게시 코드 |
| 알림은 보이나 탭 목적지가 틀림 | PendingIntent와 Intent extra 검증 |
| 일부 기기만 계속 누락 | 오래된 등록, FID/legacy token 혼용, 계정 매핑 |
| high가 늦어짐 | 사용자 가시 알림으로 이어졌는지, priority 하향 여부 |

## 책임 경계

- FCM 백엔드는 메시지 라우팅을 맡고, 앱 서버는 사용자와 앱 인스턴스의 매핑 및 권한을 맡는다.
- notification/data payload는 앱 상태에 따라 처리 지점이 달라진다. 수신 콜백은 장시간 비즈니스 작업의 실행 보장이 아니다.
- Android 알림 권한과 채널은 표시 가능성을 정한다. FCM 전달 지표와 사용자 노출 지표를 합치지 않는다.
- 누락·중복·순서 변경은 서버의 최신 상태 조회와 멱등 처리로 복구한다.

## 노트 목록

- [FCM은 메시지 전송 서비스이지 비즈니스 실행 보장이 아니다](01_inbox/mobile/android/04_system_services/background-and-notifications/notification-messaging-contracts/fcm-is-message-delivery-not-business-execution-guarantee.md)
- [FCM 등록 식별자는 사용자 계정이 아니라 앱 인스턴스를 가리킨다](01_inbox/mobile/android/04_system_services/background-and-notifications/notification-messaging-contracts/fcm-registration-identifier-targets-app-instance-not-user-account.md)
- [FCM notification payload와 data payload는 처리 지점이 다르다](01_inbox/mobile/android/04_system_services/background-and-notifications/notification-messaging-contracts/fcm-notification-and-data-payloads-have-different-handling-points.md)
- [Android 알림은 권한과 채널이 표시 가능성을 결정한다](01_inbox/mobile/android/04_system_services/background-and-notifications/notification-messaging-contracts/android-notification-permission-and-channel-control-visibility.md)
- [FCM high priority는 사용자 가시 알림에만 정당화된다](01_inbox/mobile/android/04_system_services/background-and-notifications/notification-messaging-contracts/fcm-high-priority-is-justified-by-user-visible-notification.md)
- [FCM 운영은 전달, 표시, 탭, 복구를 분리해 관측한다](01_inbox/mobile/android/04_system_services/background-and-notifications/notification-messaging-contracts/fcm-operations-observe-delivery-display-tap-and-recovery-separately.md)

관련 지도: [백그라운드 작업 계약](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/background-work-contracts.md)

검증일: 2026-08-03. 메시지 유형, priority, 등록 수명주기는 [Firebase Cloud Messaging 공식 문서](https://firebase.google.com/docs/cloud-messaging)를 기준으로 릴리스 전에 다시 확인한다.
