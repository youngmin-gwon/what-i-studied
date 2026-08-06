---
title: component-communication-uses-intent-binder-uri-and-pendingintent-by-boundary
tags: [android, android/app-components, android/architecture]
aliases: ["컴포넌트 통신은 경계에 따라 Intent, Binder, URI, PendingIntent를 사용한다"]
date modified: 2026-08-06 15:03:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Intent, Binder, URI, PendingIntent는 서로 다른 경계와 권한을 표현한다

이 네 API를 모두 “IPC 수단”이라고 묶으면 중요한 차이를 잃는다. Intent는 시스템에 component 실행·message delivery를 요청하고 같은 process에서 처리될 수도 있다. Binder는 local object 또는 remote proxy가 될 수 있다. URI는 provider가 해석하는 resource address이고, PendingIntent는 creator의 identity로 정해진 Intent를 나중에 실행할 수 있는 capability token이다.

### 선택 기준

| 수단 | 고유 계약 | 피해야 할 오해 |
| --- | --- | --- |
| explicit/implicit Intent | Activity·Service·receiver routing과 작은 command payload | object reference나 큰 데이터 운반 |
| Binder / AIDL / Messenger | 연결된 client-server API, remote일 때 transaction·caller identity | 호출이 항상 background thread이거나 항상 remote라는 가정 |
| content URI | `ContentResolver`를 통한 데이터/stream 접근과 read/write grant | 실제 filesystem path 공유 |
| PendingIntent | 시스템/다른 앱에 creator 권한의 제한된 future action 위임 | 임의 Intent를 담는 일반 wrapper |

### 안전한 PendingIntent 예시

```kotlin
val openOrder = Intent(context, OrderActivity::class.java).apply {
    action = ACTION_OPEN_ORDER
    data = "example://orders/$orderId".toUri()
}

val pendingIntent = PendingIntent.getActivity(
    context,
    orderId.hashCode(),
    openOrder,
    PendingIntent.FLAG_UPDATE_CURRENT or PendingIntent.FLAG_IMMUTABLE,
)
```

대상을 explicit하게 고정하고 수정될 이유가 없으면 immutable로 만든다. receiver나 exported Activity에서는 creator가 구성한 값이라도 URI·ID 권한을 다시 검증한다. 큰 bitmap/list는 Intent extra에 넣지 말고 DB key나 content URI를 전달한다.

### 호출과 실패 메커니즘

- Binder remote 호출은 caller thread를 block할 수 있고 remote process가 죽으면 `DeadObjectException` 등으로 실패한다. main thread의 느린 Binder 호출은 ANR 원인이 된다.
- Intent/Bundle/Binder transaction buffer에 큰 payload를 넣으면 `TransactionTooLargeException`이 날 수 있다.
- URI permission flag나 provider permission이 빠지면 수신 앱에서 `SecurityException`/permission denial이 난다.
- mutable·implicit PendingIntent는 다른 주체가 빈 field를 채우거나 의도하지 않은 component로 보내는 위험을 키운다.

### 관찰 신호

- `adb shell dumpsys package <package>`로 intent filter·permission·provider authority를 확인한다.
- Binder failure는 exception과 `binder`/`ActivityManager` log를 caller/remote PID와 함께 본다.
- 전달 payload byte 크기와 component entry timestamp를 log해 routing failure와 처리 failure를 분리한다.

상위 문서: [App Component Contracts](./app-component-contracts.md)

공식 문서: [Intents and intent filters](https://developer.android.com/guide/components/intents-filters), [Binder IPC](https://developer.android.com/develop/background-work/services/aidl), [PendingIntent reference](https://developer.android.com/reference/android/app/PendingIntent)
