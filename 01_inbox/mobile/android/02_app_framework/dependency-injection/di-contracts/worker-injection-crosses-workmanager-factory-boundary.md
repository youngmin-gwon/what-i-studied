---
title: worker-injection-crosses-workmanager-factory-boundary
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-06 14:55:00 +09:00
date created: 2026-08-03 16:59:23 +09:00
---

## Worker 주입은 WorkManager factory boundary 를 지난다

Worker 는 앱 코드가 직접 생성하는 일반 객체가 아니라 WorkManager 가 필요 시점에 생성하는 framework-managed 객체다. 그래서 Repository 같은 dependency 를 넣으려면 WorkerFactory 또는 **Hilt**(**Dagger**(컴파일 타임에 의존성 그래프를 정적으로 검증하고 코드 생성을 수행하는 Java/Kotlin용 DI 엔진)를 안드로이드 컴포넌트 생명주기에 맞춰 의존성 그래프 생성을 자동화하는 구글의 공식 DI 라이브러리) WorkManager integration 같은 생성 boundary 를 통과해야 한다.

Worker 에 Activity, Fragment, screen-scoped object 를 넣으면 background execution lifetime 과 맞지 않는다. Worker dependency 는 작업이 실행되는 동안 안전한 app-level 또는 task-level dependency 로 제한한다.

관련 노트: [WorkManager](../../../04_system_services/background-and-notifications/background-work-contracts/workmanager-is-default-for-deferrable-guaranteed-work.md).

### 최소 예시

```kotlin
@HiltWorker
class UploadWorker @AssistedInject constructor(
    @Assisted appContext: Context,
    @Assisted params: WorkerParameters,
    private val uploader: Uploader,
) : CoroutineWorker(appContext, params) {
    override suspend fun doWork(): Result = uploader.upload().toWorkerResult()
}

@HiltAndroidApp
class App : Application(), Configuration.Provider {
    @Inject lateinit var workerFactory: HiltWorkerFactory
    override val workManagerConfiguration =
        Configuration.Builder().setWorkerFactory(workerFactory).build()
}
```

`Context`와 `WorkerParameters`만 assisted parameter이고, Hilt Worker에는 `SingletonComponent`의 unscoped 또는 `@Singleton` binding만 주입할 수 있다. custom configuration을 쓰면 manifest의 기본 WorkManager initializer도 공식 절차대로 제거해야 factory가 사용된다.

### 실패와 관찰 신호

- factory가 등록되지 않으면 WorkManager가 Worker constructor를 찾지 못해 생성 실패 log를 남기고 작업이 실행되지 않는다.
- Activity/ViewModel scoped dependency를 요청하면 component에서 binding을 볼 수 없어 build가 실패한다.
- `WorkInfo` state와 WorkManager log에서 `FAILED` 이전의 worker instantiation 예외를 먼저 확인한다.

상위 문서: [DI 계약](./di-contracts.md)

공식 문서: [Hilt and WorkManager](https://developer.android.com/training/dependency-injection/hilt-jetpack#workmanager)
