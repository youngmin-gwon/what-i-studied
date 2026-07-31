# WorkManager (권장)

지연 가능(Deferrable)하고 보장된 실행(Guaranteed execution)이 필요한 비동기 작업에 적합하다.

##### 기본 구현: CoroutineWorker

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

##### 제약 조건 및 실행

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
