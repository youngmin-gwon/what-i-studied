---
title: notification-deep-link-needs-explicit-task-and-back-stack-policy
tags: [android, android/deep-links, android/navigation]
aliases: ["알림은 PendingIntent 로 딥 링크 여정을 시작한다"]
date modified: 2026-08-04 14:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## 알림은 PendingIntent 로 딥 링크 여정을 시작한다

상위 문서: [Deep Link 계약](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/deep-link-contracts/deep-link-contracts.md)

관련 노트: [PendingIntent는 미래 실행 권한을 위임하는 토큰이다](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/intent-manifest-contracts/pendingintent-is-delegated-future-intent-token.md), [Android task와 앱 back stack은 다른 스택이다](01_inbox/mobile/android/02_app_framework/navigation/navigation3/navigation3-contracts/android-task-and-app-back-stack-are-different-stacks.md)

### 알림 딥 링크의 구조

알림 자체는 화면이 아니라 사용자가 누를 수 있는 진입점이다.

알림 클릭 동작은 보통 URI 를 담은 Intent 와 PendingIntent 로 표현한다.

사용자가 클릭하면 시스템이 앱의 외부 진입과 같은 라우팅 경로를 실행해야 한다.

알림 전용 라우터를 따로 만들면 일반 링크와 인증·오류 정책이 달라질 수 있다.

따라서 알림 URI 도 [Android 딥 링크는 외부 URI 계약이다](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/deep-link-contracts/deep-link-is-external-uri-contract.md) 의 계약을 사용한다.

### PendingIntent 선택

`PendingIntent` 는 앱이 나중에 실행할 수 있도록 시스템에 위임하는 토큰이다.

변경되지 않아야 하는 딥 링크 데이터에는 `FLAG_IMMUTABLE` 을 우선 고려한다.

같은 알림을 갱신할 때는 request code 와 `FLAG_UPDATE_CURRENT` 정책을 일관되게 정한다.

서로 다른 상품이나 대상을 같은 request code 로 덮어쓰지 않도록 식별자를 설계한다.

Intent 에 불필요한 민감 정보나 장기 인증 토큰을 넣지 않는다.

### 합성 백 스택

알림에서 앱이 새로 열릴 때 상위 화면이 필요하면 `TaskStackBuilder` 를 사용할 수 있다.

부모 Activity 관계 또는 Navigation 의 시작 목적지가 기대한 뒤로 가기를 만들어야 한다.

합성 스택의 홈은 사용자가 실제로 접근할 수 있는 화면이어야 한다.

로그인이 필요한 대상은 클릭 후 인증 화면을 거쳐 pending destination 으로 복귀한다.

이미 실행 중인 task 를 재사용할 때도 중복 목적지와 stale state 를 점검한다.

```kotlin
val detailIntent = Intent(Intent.ACTION_VIEW, Uri.parse("https://example.com/orders/42"))
val pendingIntent = TaskStackBuilder.create(context)
    .addNextIntentWithParentStack(detailIntent)
    .getPendingIntent(orderId.hashCode(), PendingIntent.FLAG_IMMUTABLE)

NotificationCompat.Builder(context, CHANNEL_ID)
    .setContentIntent(pendingIntent)
    .build()
```

`addNextIntentWithParentStack()` 은 매니페스트의 `parentActivityName` 이나 Navigation 시작 목적지를 이용해 상위 화면을 합성 백 스택으로 넣는다. request code 로 `orderId.hashCode()` 처럼 대상별 값을 쓰지 않으면 서로 다른 주문 알림이 같은 `PendingIntent` 를 덮어써 최신 알림을 눌러도 예전 대상이 열릴 수 있다.

### 알림 내용과 링크의 일치

알림 제목과 클릭 결과가 가리키는 리소스가 일치해야 사용자가 혼란스럽지 않다.

리소스가 삭제되었거나 권한이 사라졌다면 오류 화면과 대체 행동을 제공한다.

알림은 오래 남을 수 있으므로 클릭 시점에 최신 상태를 조회한다.

딥 링크 검증이 실패해도 알림의 fallback 이 사용자에게 의미 있는 결과를 줘야 한다.

알림 클릭은 앱이 직접 만든 링크와 외부 브라우저 링크의 보안 검사를 우회하지 않아야 한다.

### 테스트 항목

앱이 종료된 상태, 백그라운드 상태, 기존 task 가 있는 상태를 나눠 확인한다.

동일 알림 갱신과 서로 다른 알림 동시 클릭에서 PendingIntent 충돌을 확인한다.

인증 만료, 잘못된 대상, 삭제된 대상, 뒤로 가기 동작을 확인한다.

실제 App Link 검증은 [App Links 테스트와 디버깅](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/deep-link-contracts/deep-link-testing-validates-resolution-verification-and-routing.md) 으로 수행한다.

### 결론

알림 딥 링크는 별도 목적지 체계가 아니라 딥 링크 계약을 호출하는 이벤트다.

PendingIntent 의 불변성, 식별자, 백 스택, 인증 복귀를 함께 설계해야 반복 클릭에도 예측 가능하다.
