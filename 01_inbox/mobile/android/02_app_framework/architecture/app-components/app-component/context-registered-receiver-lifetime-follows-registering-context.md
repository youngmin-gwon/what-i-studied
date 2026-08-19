---
title: context-registered-receiver-lifetime-follows-registering-context
tags: [android, android/app-components, android/architecture]
aliases: ["context-registered receiver 수명은 등록한 Context 경계를 따른다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## context-registered receiver 수명은 등록한 Context 경계를 따른다

AndroidManifest 에 선언되는 정적 리시버(Static Receiver)와 달리, 코드 내에서 **`context.registerReceiver()` 로 동적 등록되는 리시버(Dynamic / Context-registered Receiver)의 수명은 해당 리시버를 등록한 Context 인스턴스의 생명주기 경계를 엄격히 따른다.**

---

### 1. 개념 및 핵심 구조 (What)

- **Context 동기화 생명주기**:
  Activity Context 에 등록된 리시버는 해당 Activity 의 `onStop()` 또는 `onDestroy()` 시점에 `unregisterReceiver()` 를 명시적으로 호출해 해제해야 한다. 해제하지 않을 경우 Activity Context Leak 이 일어난다.
- **Android 14+ Receiver Exported Flag 강제**:
  안드로이드 14(API 34)부터 동적 리시버 등록 시 `RECEIVER_EXPORTED` 또는 `RECEIVER_NOT_EXPORTED` 플래그 명시가 필수화되었다.

---

### 2. 코드 예시 (Activity Lifecycle 매핑 등록 및 해제)

```kotlin
class NetworkAwareActivity : ComponentActivity() {

    private val networkReceiver = object : BroadcastReceiver() {
        override fun onReceive(context: Context, intent: Intent) {
            // 네트워크 상태 변경 반영
        }
    }

    override fun onStart() {
        super.onStart()
        val filter = IntentFilter(ConnectivityManager.CONNECTIVITY_ACTION)
        ContextCompat.registerReceiver(
            this,
            networkReceiver,
            filter,
            ContextCompat.RECEIVER_NOT_EXPORTED
        )
    }

    override fun onStop() {
        unregisterReceiver(networkReceiver) // 수명에 맞춰 반드시 해제
        super.onStop()
    }
}
```

---

### 3. 관련 문서 및 참조

- 상위 문서: [App Component Contracts](./app-component.md)
- 공식 가이드: [Dynamic Broadcast Receivers](https://developer.android.com/guide/components/broadcasts#context-registered-receivers)

검증일: 2026-08-05. Dynamic Receiver unregister 필수 계약 대조 완료.
