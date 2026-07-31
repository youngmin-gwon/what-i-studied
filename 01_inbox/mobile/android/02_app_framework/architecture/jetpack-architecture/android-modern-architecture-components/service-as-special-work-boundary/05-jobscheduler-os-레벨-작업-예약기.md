# JobScheduler: OS 레벨 작업 예약기

`JobScheduler`는 Android 프레임워크가 제공하는 **OS 레벨 작업 예약 API**입니다. 네트워크 연결, 충전 중, 대기 시간, 주기 실행 같은 조건을 걸어
작업을 예약할 수 있습니다.

```kotlin
val jobInfo = JobInfo.Builder(
    1001,
    ComponentName(context, SyncJobService::class.java),
)
    .setRequiredNetworkType(JobInfo.NETWORK_TYPE_UNMETERED)
    .setRequiresCharging(true)
    .build()

context.getSystemService(JobScheduler::class.java).schedule(jobInfo)
```

```kotlin
class SyncJobService : JobService() {
    override fun onStartJob(params: JobParameters?): Boolean {
        // 별도 스레드/Coroutine에서 작업 시작
        return true
    }

    override fun onStopJob(params: JobParameters?): Boolean {
        // true를 반환하면 나중에 재시도 가능
        return true
    }
}
```

다만 일반 앱에서는 `JobScheduler`를 직접 쓰기보다 `WorkManager`를 먼저 고려하는 편이 보통 더 좋습니다.

| 구분            | JobScheduler           | WorkManager                        |
|:--------------|:-----------------------|:-----------------------------------|
| 소속            | Android Framework API  | Jetpack 라이브러리                      |
| 추상화 수준        | 낮음. `JobService` 직접 구현 | 높음. `Worker`, `CoroutineWorker` 제공 |
| OS 버전 대응      | 개발자가 세부 차이를 더 신경 써야 함  | 내부적으로 적절한 스케줄러 사용                  |
| 체이닝/재시도/상태 관찰 | 직접 설계 필요               | API로 제공                            |
| 일반 앱 권장도      | 특수한 플랫폼 제어가 필요할 때      | 대부분의 보장 백그라운드 작업                   |

> [!NOTE]
> WorkManager는 내부적으로 OS 버전과 상황에 맞는 스케줄링 메커니즘을 사용합니다. 그래서 "작업 예약"이 목적이라면 보통 WorkManager가 더 높은 수준의 표준
> API입니다.
