---
title: foreground-service-is-user-visible-ongoing-work-contract
tags: [android, android/app-components, android/architecture]
aliases: ["Foreground Service는 사용자에게 보이는 진행 중 작업 계약이다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Foreground Service는 사용자에게 보이는 진행 중 작업 계약이다

**Foreground Service 는 사용자가 알림창(Ongoing Notification)을 통해 직접 인식할 수 있는 장기 실행 작업(음악 재생, 네비게이션 내비게이션, 운동 추적, 위치 추적 등)을 구동하기 위한 서비스 계약**이다.

---

### 1. 개념 및 핵심 명제 (What)

- **사용자 가시성 필수 계약**:
  Foreground Service 는 실행 직후(Android 12+ 의 경우 10초 이내) `startForeground(id, notification)` 를 호출하여 지울 수 없는 진행 중 상태 알림(Ongoing Notification)을 게시해야 한다.
- **Android 14+ Foreground Service Type 필수화**:
  Android 14(API 34)부터 manifest 및 코드 상에 서비스 작업 타입(`mediaPlayback`, `location`, `connectedDevice`, `dataSync` 등)을 명시해야 하며, 유효한 권한이 선언되지 않은 경우 `SecurityException` 이 발생한다.

---

### 2. 코드 예시 (Foreground Service 및 Notification)

```kotlin
class MusicPlaybackService : Service() {

    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
        val notification = NotificationCompat.Builder(this, "MUSIC_CHANNEL")
            .setContentTitle("음악 재생 중")
            .setContentText("Artist - Song Title")
            .setSmallIcon(R.drawable.ic_music)
            .setOngoing(true)
            .build()

        // Android 14+ foregroundServiceType 지정 호출
        ServiceCompat.startForeground(
            this,
            1001,
            notification,
            ServiceInfo.FOREGROUND_SERVICE_TYPE_MEDIA_PLAYBACK
        )
        return START_STICKY
    }

    override fun onBind(intent: Intent?): IBinder? = null
}
```

---

### 3. 관련 문서 및 참조

- 상위 문서: [App Component Contracts](./app-component-contracts.md)
- 공식 가이드: [Foreground Services Guide](https://developer.android.com/guide/components/foreground-services)

검증일: 2026-08-05. Android 14 Foreground Service Type 정책 확인 완료.
