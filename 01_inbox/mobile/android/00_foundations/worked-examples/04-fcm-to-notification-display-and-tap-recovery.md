---
title: FCM 전송에서 notification 표시와 탭 복구까지
tags: ["android", "android/foundations", "worked-example"]
aliases: ["FCM delivery to notification display and tap recovery"]
date modified: 2026-08-04 02:40:00 +09:00
date created: 2026-08-04 02:40:00 +09:00
---

## FCM 전송에서 notification 표시와 탭 복구까지

이 예시는 Learning Spine 4·5·6·8·9·10·11장을 하나의 이벤트로 잇는다. "FCM은 전달 수단이고 Android 알림은 표시 수단이며, 하나의 성공이 다른 하나를 보장하지 않는다"는 10장의 원칙을 실제 단계로 풀어내고, 탭 이후의 프로세스 재진입은 4장, 라우팅은 5장의 task/back stack 모델을, 누락 복구는 8장의 데이터 계약을, 관찰은 11장의 "전달·표시·탭·복구를 분리해서 본다"는 방법론을 그대로 따른다.

### 시작 상태

앱은 설치돼 있고 FCM 등록 토큰을 서버에 업로드해뒀다. 이 토큰은 사용자 계정이 아니라 이 앱 인스턴스를 가리키는 식별자다. `POST_NOTIFICATIONS` 런타임 권한(Android 13+)은 아직 승인 여부가 불확실하다.

### 입력

서버가 이 등록 토큰으로 notification과 data를 함께 담은(combined) 메시지를 FCM HTTP v1 API로 전송한다.

### 단계별 흐름

1. **전달(딜리버리)**: FCM 백엔드가 메시지를 기기로 전달한다. 이 단계의 성공은 서버 쪽에서 관측되는 지표이며, 사용자가 실제로 무언가를 봤다는 뜻이 아니다.
2. **앱 상태별 처리 분기(6장)**: 앱이 포그라운드에 있다면 `onMessageReceived` 콜백에서 notification·data 값을 모두 받는다. 앱이 백그라운드거나 종료 상태라면 notification 부분은 시스템이 곧바로 트레이로 보내고, 앱의 콜백은 실행되지 않을 수 있다. data 값은 이 경우 사용자가 알림을 탭한 시점에 Intent extras로 전달된다.
3. **표시 gate(9장 gate 모델의 구체 사례)**: 시스템이 알림을 실제로 트레이에 표시하려면 두 조건이 모두 필요하다. `POST_NOTIFICATIONS` 권한이 granted 상태여야 하고, 메시지가 지정한 채널이 존재하며 사용자가 차단하지 않았어야 한다. 이 두 조건은 FCM 전달 성공과는 독립적인 게이트다.
4. **사용자 탭과 프로세스 상태(4장)**: 사용자가 알림을 탭하면 알림에 연결된 `PendingIntent`가 실행된다. 앱 프로세스가 없었다면 이 탭은 WE1(앱 아이콘 탭에서 첫 프레임까지)과 같은 냉시작 경로를 거친다. 프로세스가 이미 있었다면 기존 task에 새 Intent가 전달된다.
5. **Task/back stack(5장)**: 알림에서 새로 시작된 task에는 자연스러운 부모 화면이 없을 수 있다. `TaskStackBuilder`로 합성 백 스택을 구성해, 탭한 화면에서 뒤로 가기를 눌렀을 때 곧바로 앱이 종료되지 않고 의미 있는 상위 화면으로 이동하게 한다. 이는 WE3(deep link)에서 다룬 것과 같은 계약이다 — 알림 클릭도 딥 링크 계약을 호출하는 하나의 이벤트다.
6. **데이터 사용과 재조회**: Intent extras에서 읽은 data 값(예: 메시지 ID)은 그 자체로 화면에 표시할 최종 값이 아니다. 화면은 이 ID로 서버의 최신 상태를 다시 조회한다. 알림이 오래 남아 있다가 클릭됐다면 그 사이 리소스가 삭제되거나 바뀌었을 수 있기 때문이다.
7. **누락 복구(8장)**: Doze, 강제 종료, 네트워크 불가 상태에서는 메시지 자체가 기기에 전달되지 못했을 수 있다. 그래서 앱은 알림 하나하나에 의존하지 않고, 앱을 다시 열었을 때 전체 동기화로 놓친 이벤트를 복구하는 경로를 별도로 둔다. 이것은 8장에서 다룬 "서버가 최종 source of truth"라는 원칙의 실제 적용이다.

### 성공 결과

사용자는 알림을 탭해 올바른 화면으로 이동하고, 그 화면은 서버에서 재조회한 최신 데이터를 보여준다. 뒤로 가기를 누르면 합성 백 스택을 따라 자연스러운 상위 화면으로 돌아간다.

### 관찰 가능한 신호

- 서버 쪽: FCM 전송 응답 코드와 오류 유형(예: `UNREGISTERED` 토큰).
- 기기 쪽 수신: `onMessageReceived` 호출 여부와 전달받은 payload(포그라운드에서만 신뢰할 수 있다).
- 표시: 알림이 실제로 트레이에 나타났는지는 `POST_NOTIFICATIONS` grant 상태와 채널 차단 여부를 각각 확인해야 한다.
- 탭: `dumpsys activity activities`로 알림 탭 이후 실제 task 구성을 확인한다.
- 복구: 앱 시작 시 전체 동기화가 실제로 실행되고 성공하는 비율을 별도로 측정한다.

이 다섯 신호는 11장에서 강조한 것처럼 서로 다른 이벤트이며, 하나만 보고 전체가 성공했다고 판단하면 안 된다.

### 실패 분기: 전달은 성공했지만 알림이 보이지 않는다

1. 서버 로그에는 FCM 전송이 성공(200)했다고 기록된다.
2. 기기의 `onMessageReceived`도 백그라운드 경로로 정상 호출됐을 수 있다(data 처리만).
3. 하지만 사용자가 이전에 `POST_NOTIFICATIONS` 권한을 거부했거나, 이 메시지가 지정한 채널을 설정에서 꺼뒀다면 시스템은 알림을 트레이에 표시하지 않는다.
4. 사용자에게는 "알림이 안 온다"는 증상으로 보이지만, 원인은 전달 실패가 아니라 9장에서 다룬 표시 gate에 있다.

이 실패를 "FCM이 안 됐다"로 뭉뚱그리면 잘못된 방향(서버·네트워크)을 조사하게 된다. 올바른 순서는 서버 전송 로그 → 기기 수신 로그 → 권한 grant 상태 → 채널 차단 상태를 차례로 좁히는 것이다.

### 코드 예시

```kotlin
class MyMessagingService : FirebaseMessagingService() {
    override fun onMessageReceived(message: RemoteMessage) {
        // 3. 표시 gate: 채널이 없으면 시스템이 heads-up을 만들지 못한다.
        ensureChannelExists(CHANNEL_ID)

        val eventId = message.data["event_id"] ?: return
        // notification payload는 시스템이 트레이 표시를 처리하므로
        // 여기서는 data 처리(백그라운드 동기화 트리거 등)만 한다.
        scheduleShortSync(eventId)
    }
}

// 5. 탭 시 합성 백 스택 구성
fun buildNotificationPendingIntent(context: Context, eventId: String): PendingIntent {
    val detailIntent = Intent(context, EventDetailActivity::class.java).apply {
        putExtra("event_id", eventId)
    }
    return TaskStackBuilder.create(context)
        .addNextIntentWithParentStack(detailIntent)
        .getPendingIntent(eventId.hashCode(), PendingIntent.FLAG_UPDATE_CURRENT or PendingIntent.FLAG_IMMUTABLE)!!
}
```

### 관련 원자 노트

- [FCM은 메시지 전송 서비스이지 비즈니스 실행 보장이 아니다](../../04_system_services/background-and-notifications/notification-messaging-contracts/fcm-is-message-delivery-not-business-execution-guarantee.md)
- [FCM notification payload와 data payload는 처리 지점이 다르다](../../04_system_services/background-and-notifications/notification-messaging-contracts/fcm-notification-and-data-payloads-have-different-handling-points.md)
- [Android 알림은 권한과 채널이 표시 가능성을 결정한다](../../04_system_services/background-and-notifications/notification-messaging-contracts/android-notification-permission-and-channel-control-visibility.md)
- [FCM 운영은 전달, 표시, 탭, 복구를 분리해 관측한다](../../04_system_services/background-and-notifications/notification-messaging-contracts/fcm-operations-observe-delivery-display-tap-and-recovery-separately.md)
- [알림은 PendingIntent로 딥 링크 여정을 시작한다](../../02_app_framework/navigation/intents-and-deep-links/deep-link-contracts/notification-deep-link-needs-explicit-task-and-back-stack-policy.md)
- [FCM 등록 식별자는 사용자 계정이 아니라 앱 인스턴스를 가리킨다](../../04_system_services/background-and-notifications/notification-messaging-contracts/fcm-registration-identifier-targets-app-instance-not-user-account.md)

### 관련 Learning Spine 장

- [4장 매니페스트에서 컴포넌트 실행까지](../learning-spine/04-manifest-to-component-execution.md)
- [5장 화면, 프로세스, task와 사용자 상태는 독립적인 lifetime을 가진다](../learning-spine/05-independent-lifetimes-of-screen-process-task-and-state.md)
- [6장 메인 스레드, Binder, coroutine과 durable scheduler는 서로 다른 실행 책임을 진다](../learning-spine/06-main-thread-binder-coroutine-and-durable-work-lifetime.md)
- [8장 데이터, 저장소, 네트워크와 offline recovery](../learning-spine/08-data-storage-network-and-offline-recovery.md)
- [9장 Identity, 권한과 독립적인 security gate](../learning-spine/09-identity-permission-and-independent-security-gates.md)
- [10장 기기 기능 발견과 background execution](../learning-spine/10-device-capability-discovery-and-background-execution.md)
- [11장 관찰, 테스트와 품질 feedback](../learning-spine/11-observation-testing-and-quality-feedback.md)

### 공식 근거

- [FCM Android 시작 안내](https://firebase.google.com/docs/cloud-messaging/android/get-started)
- [FCM 메시지 전달 이해](https://firebase.google.com/docs/cloud-messaging/understand-delivery)
- [알림 런타임 권한](https://developer.android.com/develop/ui/compose/notifications/notification-permission)

검증일: 2026-08-04. FCM SDK 세대(토큰/FID)와 알림 권한 요구 조건은 버전에 따라 다르므로 실제 구현 시점에 다시 확인한다.
