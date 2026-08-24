---
title: service-execution-boundaries
tags: [android, android/app-components, android/architecture]
aliases: ["Service는 백그라운드/원격 작업 진입점이다"]
date modified: 2026-08-06 15:03:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Service는 thread나 durable scheduler가 아니라 시스템 lifecycle 진입점이다

Service는 UI 없이 started 또는 bound lifecycle을 제공하지만 자체 worker thread를 만들지 않는다. `onCreate()`, `onStartCommand()`, `onBind()`는 기본적으로 앱 main thread에서 호출된다. 별도 `android:process`나 remote Binder를 선언하지 않은 Service는 같은 process 안에 있으며, Service라는 이유만으로 IPC가 생기지도 않는다.

### Started service의 내부 동작

`startService(intent)` 호출마다 같은 Service instance의 `onStartCommand()`에 새 `startId`가 전달될 수 있다. 비동기 작업이 끝날 때 `stopSelfResult(startId)`를 쓰면 더 새로운 start 요청이 있는 Service를 오래된 작업이 잘못 중지하는 일을 피할 수 있다.

```kotlin
class ImportService : Service() {
    private val scope = CoroutineScope(SupervisorJob() + Dispatchers.IO)

    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
        scope.launch {
            try {
                importer.import(requireNotNull(intent?.data))
            } finally {
                stopSelfResult(startId)
            }
        }
        return START_NOT_STICKY
    }

    override fun onDestroy() {
        scope.cancel()
        super.onDestroy()
    }

    override fun onBind(intent: Intent?): IBinder? = null
}
```

이 코드는 thread 전환과 중지 ordering을 보여줄 뿐 process death 뒤 완료를 보장하지 않는다. 지연 가능한 영속 작업은 WorkManager, 사용자가 계속 인지해야 하는 허용된 지속 작업은 foreground service, client API는 bound service를 비교한다.

### 제한과 실패·관찰 신호

- main thread에서 blocking I/O를 실행하면 Service도 동일하게 jank와 ANR을 만든다.
- API 26+에서 background 앱이 일반 background service를 새로 만들거나 계속 실행하려 하면 background execution limit에 의해 시작 거부 또는 중지가 발생한다.
- `START_STICKY`는 작업 결과의 exactly-once 보장이 아니다. 재생성 시 null intent가 올 수 있으므로 durable payload/checkpoint는 별도 저장한다.
- `adb shell dumpsys activity services <package>`에서 started/bound/foreground 상태와 start ID를 확인한다.

상위 문서: [App Component Contracts](component-contracts.md)

공식 문서: [Services overview](https://developer.android.com/develop/background-work/services), [Background execution limits](https://developer.android.com/about/versions/oreo/background)
