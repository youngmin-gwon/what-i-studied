---
title: android-push-notifications-fcm
tags: [android, android/push, fcm, firebase, notifications]
aliases: [Push Notifications, FCM, Firebase Cloud Messaging]
date modified: 2026-04-04 00:33:00 +09:00
date created: 2026-04-04 00:33:00 +09:00
---

## Android Push Notifications (FCM)

안드로이드의 원격 알림 표준은 **Firebase Cloud Messaging (FCM)**이다. 시스템은 구글 플레이 서비스(GMS)를 통해 서버와의 지속적인 연결을 유지하며, 앱이 종료된 상태에서도 메시지를 수신할 수 있게 돕는다.

> [!NOTE] **iOS 비교: APNs vs FCM**
> - **iOS**: `APNs` (Apple Push Notification service)를 사용하며, 애플이 직접 모든 메시지를 중개한다. 인증 방식(p8)과 페이로드 구조가 다르지만, 핵심적인 전달 메커니즘은 유사하다.
> - **Android**: `FCM`을 사용한다. 과거에는 GCM이었으나 FCM으로 통합되었다. 안드로이드의 특징은 **데이터 전용 메시지(Data-only message)**를 통해 앱을 백그라운드에서 깨워 조용히 데이터를 동기화하는 능력이 매우 강력하다는 점이다.
> 자세한 내용은 [apple-push-notifications-apns](../../apple/04_system_services/apple-push-notifications-apns.md)를 참고하세요.

### 1. FCM 아키텍처 및 토큰 관리

앱이 처음 실행되면 FCM 서버로부터 고유한 **Registration Token**을 발급받는다. 서버는 이 토큰을 기반으로 특정 기기를 식별한다.

```kotlin
// FirebaseMessagingService 구현
class MyFcmService : FirebaseMessagingService() {

    override fun onNewToken(token: String) {
        // 새 토큰이 발급됨. 서버(App Server)에 전송하여 저장해야 함
        sendTokenToServer(token)
    }

    override fun onMessageReceived(remoteMessage: RemoteMessage) {
        // 메시지 수신 시 호출 (Data 페이로드가 포함된 경우 필수 호출)
        handleMessage(remoteMessage)
    }
}
```

### 2. Payload 타입: Notification vs Data

FCM 메시지는 두 가지 타입의 페이로드를 가질 수 있으며, 앱의 상태에 따라 동작 방식이 결정적으로 달라진다.

| 타입 | 구조 | 앱이 백그라운드/킬(Killed)일 때 |
| :--- | :--- | :--- |
| **Notification** | `notification` 키 포함 | 시스템이 **자동으로** 알림창에 띄움. 앱 코드는 타지 않음. |
| **Data** | `data` 키 포함 (Key-Value) | `onMessageReceived`가 호출됨. 개발자가 직접 알림을 띄우거나 작업 수행 가능. |
| **Combined** | 둘 다 포함 | 시스템이 알림을 띄우고, 사용자가 클릭하면 `Intent`의 `extras`로 데이터 전달. |

> [!IMPORTANT] **Devil's Advocate : Data 페이로드를 기본으로 하라**
> 알림의 커스터마이징(아이콘, 채널, 행동 등)을 완전히 제어하고 싶다면 서버에서 `notification` 키를 빼고 `data` 키만 보내는 **Data-only message**를 권장한다. 이렇게 하면 앱이 백그라운드에서도 `onMessageReceived`를 통해 로직을 수행할 수 있다.

### 3. 현대적 필수 요구사항 (Android 13~15)

- **런타임 권한**: Android 13(API 33)부터 `POST_NOTIFICATIONS` 권한이 필수다.
- **알림 채널 (Channels)**: Android 8.0 이상에서는 모든 알림이 특정 채널에 속해야 한다.
- **Full Screen Intent**: Android 14+ 에서는 통화나 알람 앱이 아닌 경우 전체 화면 알림 권한이 기본적으로 제한된다.

### 📊 플랫폼별 주요 개념 매핑

| 특징 | Android (FCM) | iOS (APNs) |
| :--- | :--- | :--- |
| **기기 식별** | FCM Token | Device Token |
| **백그라운드 갱신** | Data-only (High Priority) | Silent Push (`content-available`) |
| **커스텀 UI** | RemoteViews | Content Extension |
| **알림 그룹화** | Group Key | Thread ID |

### 더 보기
- [android-app-components-deep-dive](android-app-components-deep-dive.md) - Service 구조
- [android-deep-links](android-deep-links.md) - 알림 클릭 시 특정 화면 진입
- [android-background-processing](android-background-processing.md) - 백그라운드 작업 제한
