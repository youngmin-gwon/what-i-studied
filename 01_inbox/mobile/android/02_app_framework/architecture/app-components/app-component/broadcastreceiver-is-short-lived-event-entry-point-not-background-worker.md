---
title: broadcastreceiver-is-short-lived-event-entry-point-not-background-worker
tags: [android, android/app-components, android/architecture]
aliases: ["BroadcastReceiver는 단명 이벤트 진입점이다"]
date modified: 2026-08-06 15:03:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## BroadcastReceiver는 제한된 실행 예산을 가진 이벤트 진입점이다

`onReceive()`는 별도 worker thread가 아니라 기본적으로 process의 main thread에서 호출된다. 일반적인 broadcast receiver 실행 제한은 최대 약 10초이며, 반환하면 manifest receiver instance는 더 이상 active하지 않다. 반환 뒤 임의 thread만 남겨 두면 process가 회수돼 작업이 중간에 사라질 수 있다.

### `goAsync()`의 정확한 경계

```kotlin
class CacheInvalidatedReceiver(
    private val appScope: CoroutineScope,
    private val cache: Cache,
) : BroadcastReceiver() {
    override fun onReceive(context: Context, intent: Intent) {
        if (intent.action != ACTION_CACHE_INVALIDATED) return

        val pending = goAsync()
        appScope.launch(Dispatchers.IO) {
            try {
                cache.markStale() // 짧고 제한된 작업만 수행
            } finally {
                pending.finish()
            }
        }
    }
}
```

`goAsync()`는 `onReceive()`가 먼저 반환하도록 해 main thread blocking을 피할 뿐 broadcast 실행 예산 자체를 없애지 않는다. `goAsync()`부터 `PendingResult.finish()`까지가 예산에 포함된다. foreground broadcast는 보통 약 10초이고, foreground flag가 없는 broadcast에는 30초 이상이 허용될 수 있지만 이를 장기 작업 budget으로 사용하지 않는다.

재시도·network constraint·process 재시작 뒤 지속성이 필요하면 receiver에서는 `WorkManager.enqueue()`만 하고 실제 작업을 Worker로 넘긴다.

```kotlin
override fun onReceive(context: Context, intent: Intent) {
    WorkManager.getInstance(context).enqueue(
        OneTimeWorkRequestBuilder<RefreshWorker>().build()
    )
}
```

### 실패·관찰 신호

- `goAsync()` 뒤 `finish()`가 누락되거나 예산을 넘기면 broadcast timeout과 ANR 흔적이 system log/ANR trace에 남는다.
- `onReceive()`에서 network·database를 동기로 호출하면 main-thread jank, StrictMode 위반 또는 ANR이 나타난다.
- `adb shell am broadcast -a <action> -n <package>/<receiver>`와 시작/종료 timestamp log로 callback 시간을 잰다.
- 알 수 없는 action은 즉시 무시한다. intent filter는 보안 검증을 대신하지 않으며 explicit broadcast가 filter resolution을 우회할 수 있다.

상위 문서: [App Component Contracts](./app-component.md)

공식 문서: [BroadcastReceiver API — `goAsync()`](https://developer.android.com/reference/android/content/BroadcastReceiver#goAsync()), [Broadcasts overview](https://developer.android.com/develop/background-work/background-tasks/broadcasts)
