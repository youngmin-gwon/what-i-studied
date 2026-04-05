# [[mobile-security]] > [[android-background-processing]]

## Background Processing: Execution Strategy

안드로이드 앱이 포그라운드에 있지 않을 때 작업을 수행하는 **WorkManager**, **Foreground Service**, **AlarmManager**의 메커니즘을 심층 분석합니다. 

단순히 비동기 처리를 하는 것을 넘어, 사용자 경험(UX)을 해치지 않으면서 배터리 효율을 극대화하고 OS의 강력한 백그라운드 제약을 어떻게 우회하거나 준수할지 이해하는 것이 목표입니다.

---

### 💡 Context: 백그라운드 처리의 진화

안드로이드 OS는 버전이 올라갈수록 백그라운드 작업에 대해 엄격한 제한을 가하고 있습니다. 현대적인 개발에서는 **WorkManager**가 사실상의 표준이며, 즉각적인 반응이 필요한 특수한 경우에만 **Foreground Service**를 사용해야 합니다.

> [!NOTE] **상호 참조**
> iOS의 백그라운드 처리 방식은 [[apple-background-tasks]]를 참고하세요.

---

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

### See Also

- [[android-app-components-deep-dive]]
- [[android-coroutines-flow]]
- [[android-permissions-deep-dive]]
