---
title: apple-push-notifications-apns
tags: [apns, apple, ios, notifications, push]
aliases: [APNs, Push Notifications, Remote Notifications]
date modified: 2026-04-06 18:11:10 +09:00
date created: 2026-04-04 00:33:00 +09:00
---

## Apple Push Notifications (APNs)

애플의 원격 알림 표준은 **Apple Push Notification service (APNs)** 이다. 애플은 보안과 개인정보 보호를 위해 앱의 푸시 기능을 철저히 통제하며, HTTP/2 기반의 고성능 전송 엔진을 통해 전 세계 수십억 대의 기기에 알림을 전달한다.

>[!NOTE] **Android 비교: FCM vs APNs**
> - **Android**: `FCM` (Firebase Cloud Messaging)을 사용하며, 데이터 전용(Data-only) 메시지로 백그라운드 조작을 비교적 자유롭게 할 수 있다.
> - **iOS**: `APNs` 를 사용한다. 애플은 푸시 알림을 단순한 '알림'뿐만 아니라 **배경 작업 수행(Silent Push)** 및 **실시간 현황 업데이트(Live Activity)**의 핵심 트리거로 활용한다.
>자세한 내용은 [android-push-notifications-fcm](../../android/02_app_framework/android-push-notifications-fcm.md) 를 참고하세요.

### 1. APNs 아키텍처 및 인증

애플의 푸시를 보내려면 서버 인증 단계가 필요하다.

- **Certificate-based (.p12):** 이전 방식. 인증서가 만료되면 갱신해야 하는 번거로움이 있다.
- **Token-based (.p8):** 권장 방식. 하나의 키(`AuthKey`)로 여러 앱에 푸시를 보낼 수 있으며 만료되지 않는다.

### 2. Push Notification 타입

#### 1. Alert (Standard Push)

사용자에게 알림창을 띄우는 일반적인 푸시. 제목, 본문, 소리를 포함한다.

#### 2. Silent Push (Background Update)

사용자에게 알리지 않고 앱을 백그라운드에서 깨워 데이터를 업데이트한다.

- **Payload**: `"content-available": 1` 포함
- **제약**: 시스템에 의해 전달이 보장되지 않으며(Best-effort), 너무 자주 보내면 쓰로틀링(Throttling)에 걸려 무시된다.

#### 3. Live Activity Push (iOS 16+)

동적으로 변화하는 정보를 실시간으로 갱신한다. (예: 축구 점수, 배달 기사 위치)

- **Token**: 액티비티 시작 시 발급받은 `pushToken` 을 사용한다.
- **iOS 18+**: 대규모 실시간 업데이트를 위한 **Broadcast Push**를 지원한다.

---

### 🏛️ Notification Service Extension

알림을 사용자에게 보여주기 직전에 컨텐츠를 가공할 수 있는 별도의 프로세스(App Extension)이다.

- **기능**: 이미지/영상 첨부, 복호화(End-to-End Encryption 대응), 알림 텍스트 동적 수정.
- **제약**: 실행 시간이 매우 짧으며 (약 30 초), 메모리 사용량이 극도로 제한된다.

>[!TIP] **Devil's Advocate : Silent Push 에 의존하지 마라**
>Silent Push 는 사용자의 배터리와 데이터 보호를 위해 시스템이 언제든지 지연시키거나 버릴 수 있다. 중요한 데이터 동기화는 앱이 켜질 때 직접 요청하는 방식을 병행하라.

### 더 보기

- [apple-app-lifecycle-and-ui](../02_ui_frameworks/apple-app-lifecycle-and-ui.md) - 앱의 상태와 알림 처리
- [apple-background-tasks](apple-background-tasks.md) - 백그라운드 작업과 푸시의 결합
- [apple-widgets-live-activities](../02_ui_frameworks/apple-widgets-live-activities.md) - 위젯/실시간 현황 푸시 전략
