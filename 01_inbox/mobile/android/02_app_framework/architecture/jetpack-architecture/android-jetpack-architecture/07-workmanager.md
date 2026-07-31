# WorkManager

상위 노트: [android-jetpack-architecture](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/android-jetpack-architecture.md)

지연 가능한 백그라운드 작업 스케줄링.

```kotlin
// Worker 정의
class UploadWorker(
    context: Context,
    params: WorkerParameters
) : CoroutineWorker(context, params) {
    
    override suspend fun doWork(): Result {
        val imageUri = inputData.getString("image_uri") ?: return Result.failure()
        
        return try {
            uploadImage(imageUri)
            Result.success()
        } catch (e: Exception) {
            if (runAttemptCount < 3) {
                Result.retry()
            } else {
                Result.failure()
            }
        }
    }
    
    private suspend fun uploadImage(uri: String) {
        // 업로드 로직
        setProgress(workDataOf("progress" to 50))
    }
}

// 작업 예약
val uploadRequest = OneTimeWorkRequestBuilder<UploadWorker>()
    .setInputData(workDataOf("image_uri" to uri.toString()))
    .setConstraints(
        Constraints.Builder()
            .setRequiredNetworkType(NetworkType.CONNECTED)
            .setRequiresBatteryNotLow(true)
            .build()
    )
    .setBackoffCriteria(
        BackoffPolicy.EXPONENTIAL,
        10, TimeUnit.SECONDS
    )
    .build()

WorkManager.getInstance(context).enqueue(uploadRequest)

// 진행 상황 관찰
WorkManager.getInstance(context)
    .getWorkInfoByIdLiveData(uploadRequest.id)
    .observe(this) { workInfo ->
        if (workInfo.state == WorkInfo.State.RUNNING) {
            val progress = workInfo.progress.getInt("progress", 0)
            progressBar.progress = progress
        }
    }
```

##### 주기적 작업

```kotlin
val periodicWork = PeriodicWorkRequestBuilder<SyncWorker>(
    15, TimeUnit.MINUTES // 최소 15분
).build()

WorkManager.getInstance(context).enqueueUniquePeriodicWork(
    "sync",
    ExistingPeriodicWorkPolicy.KEEP,
    periodicWork
)
```

##### 작업 체인

```kotlin
val cleanup = OneTimeWorkRequestBuilder<CleanupWorker>().build()
val download = OneTimeWorkRequestBuilder<DownloadWorker>().build()
val process = OneTimeWorkRequestBuilder<ProcessWorker>().build()

WorkManager.getInstance(context)
    .beginWith(cleanup)
    .then(download)
    .then(process)
    .enqueue()
```

// Safe Args 로 인자 받기

class DetailFragment : Fragment() {

    private val args: DetailFragmentArgs by navArgs()

    
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        val userId = args.userId
        // 사용
    }

}
