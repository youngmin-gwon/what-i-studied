---
title: foreground-service-is-user-visible-ongoing-work-contract
tags: [android, android/app-components, android/architecture]
aliases: ["Foreground Service는 사용자에게 보이는 진행 중 작업 계약이다"]
date modified: 2026-08-06 15:03:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Foreground Service는 시작 자격과 즉시 승격을 모두 만족해야 한다

Foreground service(FGS)는 사용자가 현재 진행 중임을 알아야 하는 허용된 작업을 위한 Service다. 알림을 붙였다는 이유만으로 background start 제한, foreground service type, runtime permission 또는 Play 정책을 우회하지 못한다.

### 두 단계 시작 메커니즘

1. 앱이 `startForegroundService()`를 호출할 자격이 있어야 한다. target 31+ 앱이 background 상태라면 Android 12부터 제한된 예외 외에는 시작 자체가 거부된다.
2. Service가 생성되면 약 5초 안에 `startForeground()`를 호출해 notification과 type을 게시해야 한다. 기존 문서의 “Android 12부터 10초”는 두 단계를 혼동한 설명이다.

### 안전한 최소 manifest와 코드

```xml
<uses-permission android:name="android.permission.FOREGROUND_SERVICE" />
<uses-permission android:name="android.permission.FOREGROUND_SERVICE_MEDIA_PLAYBACK" />

<service
    android:name=".MusicPlaybackService"
    android:exported="false"
    android:foregroundServiceType="mediaPlayback" />
```

```kotlin
class MusicPlaybackService : Service() {
    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
        ServiceCompat.startForeground(
            this,
            1001,
            playbackNotification(),
            ServiceInfo.FOREGROUND_SERVICE_TYPE_MEDIA_PLAYBACK,
        )
        player.play()
        return START_STICKY
    }
    override fun onBind(intent: Intent?): IBinder? = null
}

// 사용자에게 보이는 화면의 재생 버튼 등 허용된 시점
ContextCompat.startForegroundService(
    context,
    Intent(context, MusicPlaybackService::class.java),
)
```

Android 14+ target에서는 type별 foreground-service permission과 runtime prerequisite를 시작 전에 충족해야 한다. camera·microphone·location처럼 while-in-use permission이 필요한 type은 앱이 background일 때 별도 제한도 받는다.

### 실패·관찰 신호

- background에서 예외 조건 없이 시작하면 `ForegroundServiceStartNotAllowedException`이 난다.
- Service 생성 뒤 제때 승격하지 않으면 `ForegroundServiceDidNotStartInTimeException` 계열 crash가 난다.
- Android 14+에서 type을 선언하지 않으면 `MissingForegroundServiceTypeException`, 필요한 permission/prerequisite가 없으면 `SecurityException`이 난다.
- `adb shell dumpsys activity services <package>`와 notification drawer/Task Manager에서 service type, foreground 상태와 사용자 가시성을 확인한다.

상위 문서: [App Component Contracts](./app-component-contracts.md)

공식 문서: [Launch a foreground service](https://developer.android.com/develop/background-work/services/fgs/launch), [Background-start restrictions](https://developer.android.com/develop/background-work/services/fgs/restrictions-bg-start), [Declare foreground services](https://developer.android.com/develop/background-work/services/fgs/declare)
