# WorkManager / JobScheduler

상위 노트: [[android-glossary]]

**정의**: 백그라운드 작업을 예약하는 API

**상세**:

- **JobScheduler**: 시스템 API, 조건 기반 실행
- **WorkManager**: Jetpack 라이브러리, JobScheduler/AlarmManager 추상화

**WorkManager 사용**:

```kotlin
val constraints = Constraints.Builder()
    .setRequiredNetworkType(NetworkType.CONNECTED)
    .setRequiresBatteryNotLow(true)
    .build()

val work = OneTimeWorkRequestBuilder<MyWorker>()
    .setConstraints(constraints)
    .build()

WorkManager.getInstance(context).enqueue(work)
```

**JobScheduler**:

```kotlin
val job = JobInfo.Builder(JOB_ID, componentName)
    .setRequiredNetworkType(JobInfo.NETWORK_TYPE_UNMETERED)
    .setRequiresCharging(true)
    .build()

jobScheduler.schedule(job)
```

**관련**: [android-activity-manager-and-system-services](../01_system_internals/android-activity-manager-and-system-services.md)

---

### Z
