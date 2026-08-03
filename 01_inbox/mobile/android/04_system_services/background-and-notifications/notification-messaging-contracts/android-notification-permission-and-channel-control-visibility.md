---
title: "Android 알림은 권한과 채널이 표시 가능성을 결정한다"
tags: ["android", "android/system-services"]
---

# Android 알림은 권한과 채널이 표시 가능성을 결정한다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](01_inbox/mobile/android/04_system_services/android-system-services-and-device-capabilities.md)
관련 지도: [알림과 FCM 메시징 계약](01_inbox/mobile/android/04_system_services/background-and-notifications/notification-messaging-contracts/notification-messaging-contracts.md)
관련 노트: [FCM notification payload와 data payload는 처리 지점이 다르다](01_inbox/mobile/android/04_system_services/background-and-notifications/notification-messaging-contracts/fcm-notification-and-data-payloads-have-different-handling-points.md), [Android 백그라운드 실행은 보장, 지연, 사용자 가시성으로 선택한다](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/background-execution-is-selected-by-guarantee-delay-and-visibility.md)

## Android 13 이상 권한

Android 13(API 33)부터 대부분의 알림에는 `POST_NOTIFICATIONS` 런타임 권한이 필요하다.
매니페스트에 권한을 선언하고, 앱 기능의 맥락을 설명한 뒤 적절한 시점에 사용자에게 요청한다.
사용자가 거부하면 일반 알림은 표시되지 않으며 FCM 전달 성공과 알림 표시를 혼동하면 안 된다.
포그라운드 서비스 시작 자체에는 권한이 필요하지 않지만 서비스 알림은 별도 규칙을 따른다.
권한이 거부된 Android 13+ 기기에서도 FGS notice는 Task Manager에 보일 수 있지만 notification drawer에는 보이지 않는다.

```xml
<uses-permission android:name="android.permission.POST_NOTIFICATIONS" />
```

## 권한 상태 처리

- 허용: 알림 채널의 설정 범위 안에서 알림을 게시한다.
- 거부: 인앱 화면에서 상태를 설명하고 시스템 설정으로 이동할 선택지를 제공한다.
- 아직 결정되지 않음: 최초 실행 즉시보다 사용자가 알림 가치를 이해하는 시점을 고려한다.

권한 요청 결과를 서버의 전달 성공으로 기록하지 않는다.
사용자가 앱 전체 알림이나 개별 채널을 설정에서 끌 수 있다는 전제도 둔다.

## Android 8 이상 채널

Android 8.0(API 26)부터 모든 게시 알림은 채널에 속해야 한다.
채널 ID는 코드에 안정적으로 고정하고, 앱 시작이나 첫 사용 전에 채널을 생성한다.
채널 중요도는 생성 후 사용자가 관리하므로 앱이 매번 덮어쓸 수 없다.
긴급도와 소리 정책이 다른 알림은 별도 채널로 나누되 채널을 과도하게 만들지 않는다.

FCM notification payload를 사용할 때 기본 채널 ID를 지정하고, 앱에서도 같은 채널을 준비한다.
채널이 없거나 사용자가 차단하면 메시지는 도착해도 기대한 heads-up이 나오지 않을 수 있다.

## 표시 설계

알림 탭 Intent는 명시적 목적지와 안전한 입력 검증을 포함한다.
알림 ID와 group key를 정해 중복 게시와 그룹화 정책을 일관되게 유지한다.
전체 화면 Intent는 통화나 알람처럼 정당한 사용 사례에 한정한다.

## 호환성 기준

Android 7 이하에서는 채널 API를 호출하지 않도록 API 버전을 분기한다.
Android 13 미만은 `POST_NOTIFICATIONS` 런타임 요청 대상이 아니지만 채널 동작은 버전에 따라 확인한다.
권한과 채널의 현재 상태는 게시 직전에 확인하고, 실패 시 앱 내 메시지로 대체한다.

## 참고

- [알림 런타임 권한](https://developer.android.com/develop/ui/compose/notifications/notification-permission)
- [알림 채널 생성과 관리](https://developer.android.com/develop/ui/compose/notifications/channels)

검증일: 2026-08-03. Android 13+ 권한, Android 8+ 채널, FGS notice 예외를 Android Developers 공식 문서에서 확인했다.
