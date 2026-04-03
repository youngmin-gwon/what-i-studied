---
title: android-background-processing
tags: [android, android/workmanager, android/fgs, android/background]
aliases: [WorkManager, CoroutineWorker, Foreground Service, AlarmManager]
date modified: 2026-04-04 00:22:00 +09:00
date created: 2026-04-04 00:22:00 +09:00
---

## Android Background Processing Deep Dive

안드로이드의 백그라운드 처리는 사용자 경험(UX)과 배터리 효율 사이의 타이트한 균형을 유지해야 한다. 현대적인 안드로이드 개발에서는 **WorkManager**가 사실상의 표준이며, 즉각적인 반응이 필요한 경우에 한해 **Foreground Service**를 사용한다.

> [!NOTE] **iOS 비교: Background Tasks vs WorkManager**
> - **iOS**: `BGTaskScheduler`를 통해 시스템이 작업 실행 시점을 결정한다. (강한 제약)
> - **Android**: `WorkManager`가 유사한 역할을 수행하며, 네트워크 조건, 충전 상태 등 세밀한 제약 조건(Constraints)을 설정할 수 있다.
> 자세한 내용은 [apple-background-tasks](../../apple/04_system_services/apple-background-tasks.md)를 참고하세요.

### 1. WorkManager (권장)

지연 가능(Deferrable)하고 보장된 실행(Guaranteed execution)이 필요한 비동기 작업에 적합하다.

#### 기본 구현: CoroutineWorker

```kotlin
class SyncWorker(
    appContext: Context,
    workerParams: WorkerParameters
) : CoroutineWorker(appContext, workerParams) {

    override suspend fun doWork(): Result {
        return try {
            // 네트워크 동기화 작업
            repository.syncData()
            Result.success()
        } catch (e: Exception) {
            if (runAttemptCount < 3) {
                Result.retry() // 재시도
            } else {
                Result.failure()
            }
        }
    }
}
```

#### 제약 조건 및 실행

```kotlin
val constraints = Constraints.Builder()
    .setRequiredNetworkType(NetworkType.UNMETERED) // 와이파이 전용
    .setRequiresCharging(true)                    // 충전 중일 때만
    .setRequiresDeviceIdle(true)                  // 기기가 유휴 상태일 때
    .build()

val syncRequest = OneTimeWorkRequestBuilder<SyncWorker>()
    .setConstraints(constraints)
    .setBackoffCriteria(BackoffPolicy.EXPONENTIAL, 30, TimeUnit.SECONDS)
    .build()

WorkManager.getInstance(context).enqueueUniqueWork(
    "sync_data",
    ExistingWorkPolicy.REPLACE,
    syncRequest
)
```

### 2. Foreground Services (Android 14+ 제한)

사용자가 인지해야 하는 즉각적이고 지속적인 작업(음악 재생, 운동 추적)에 사용한다.

> [!CAUTION] **Devil's Advocate : Foreground Service 남용 금지**
> Android 14부터 `foregroundServiceType` 선언이 강제되었고, 구글 플레이 정책은 "사용자가 인지할 수 없는 백그라운드 작업은 무조건 WorkManager를 쓰라"고 강요한다. 타입을 속여서 승인받으려다가는 앱이 삭제될 수 있다.

#### Android 14+ 구현 규칙
1. `AndroidManifest.xml`에 특정 타입 권한과 서비스 타입 선언
2. `startForeground()` 호출 시 `ForegroundInfo` 전달

```xml
<!-- AndroidManifest.xml -->
<uses-permission android:name="android.permission.FOREGROUND_SERVICE" />
<uses-permission android:name="android.permission.FOREGROUND_SERVICE_DATA_SYNC" />

<service
    android:name=".DataSyncService"
    android:foregroundServiceType="dataSync" />
```

### 3. AlarmManager (정교한 타이밍)

정확한 시간에 특정 작업을 수행해야 할 때(알람 시계, 약 복용 알림) 사용한다.

```kotlin
val alarmManager = context.getSystemService(Context.ALARM_SERVICE) as AlarmManager
val intent = Intent(context, AlarmReceiver::class.java)
val pendingIntent = PendingIntent.getBroadcast(
    context, 0, intent, PendingIntent.FLAG_IMMUTABLE
)

// 정확한 시간 예약 (Android 12+ 에서는 SCHEDULE_EXACT_ALARM 권한 확인 필수)
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.S && alarmManager.canScheduleExactAlarms()) {
    alarmManager.setExactAndAllowWhileIdle(
        AlarmManager.RTC_WAKEUP,
        triggerTimeMillis,
        pendingIntent
    )
}
```

### 📊 언제 무엇을 사용하는가?

| 분류 | 작업 특성 | 권장 API |
| :--- | :--- | :--- |
| **즉시 실행** | 짧은 작업 (수 초 이내) | Kotlin Coroutines (`viewModelScope`) |
| **즉시 실행 (길게)** | 지속적 작업 (음악, 운동) | **Foreground Service** |
| **지연 가능** | 보장된 실행 필요 (업로드, 동기화) | **WorkManager** |
| **정확한 타이밍** | 정해진 시각에 실행 | **AlarmManager** |

### 더 보기
- [android-app-components-deep-dive](android-app-components-deep-dive.md)
- [android-coroutines-flow](android-coroutines-flow.md)
- [android-permissions-deep-dive](../05_security_privacy/android-permissions-deep-dive.md)
