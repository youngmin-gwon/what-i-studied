# 현대 대체재: WorkManager

`WorkManager`는 "언젠가는 반드시 실행되어야 하는 백그라운드 작업"을 위한 Jetpack 라이브러리입니다.

대표 사례:

* 서버에 로그 업로드
* 장바구니/주문 데이터 동기화
* 이미지 압축 후 업로드
* 네트워크가 연결되면 재시도해야 하는 작업

```kotlin
class SyncOrdersWorker(
    appContext: Context,
    params: WorkerParameters,
) : CoroutineWorker(appContext, params) {
    override suspend fun doWork(): Result {
        return try {
            // repository.syncOrders()
            Result.success()
        } catch (e: IOException) {
            Result.retry()
        } catch (e: Exception) {
            Result.failure()
        }
    }
}
```

```kotlin
val request = OneTimeWorkRequestBuilder<SyncOrdersWorker>()
    .setConstraints(
        Constraints.Builder()
            .setRequiredNetworkType(NetworkType.CONNECTED)
            .build()
    )
    .build()

WorkManager.getInstance(context).enqueueUniqueWork(
    "sync-orders",
    ExistingWorkPolicy.KEEP,
    request,
)
```
