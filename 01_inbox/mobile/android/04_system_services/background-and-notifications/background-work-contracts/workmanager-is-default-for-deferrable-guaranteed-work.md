---
title: "WorkManager는 지연 가능한 보장 작업의 기본 선택이다"
tags: ["android", "android/system-services"]
---

# WorkManager는 지연 가능한 보장 작업의 기본 선택이다

상위 지도: [백그라운드 작업 계약](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/background-work-contracts.md)
선택 비교: [백그라운드 실행 수단은 실패 비용으로 결정한다](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/background-work-api-selection-is-a-failure-cost-decision.md)

## 핵심 명제

WorkManager는 화면을 떠나거나 앱·기기가 재시작된 뒤에도 **예약을 보존하고 조건이 맞을 때 재실행해야 하는 작업**의 기본 선택이다. 내부 DB에 `WorkSpec`을 저장하고 플랫폼 스케줄러에 위임하므로 UI 관찰자가 없어도 상태가 이어진다.

여기서 보장은 "언젠가 한 번 끊김 없이 성공"이 아니다. constraint와 시스템 제한 아래 실행을 다시 시도하도록 관리한다는 뜻이다. 즉시 시작, 정확한 시각, 프로세스 생존, 강제 중지·앱 제거 뒤 실행은 보장하지 않는다.

## 상태와 재시도 메커니즘

`ENQUEUED` 작업은 constraint와 스케줄러 허가를 기다리고, 시작하면 `RUNNING`이 된다. one-time work에서 `Result.success()`와 `Result.failure()`는 terminal state로 가고, `Result.retry()`는 backoff 뒤 `ENQUEUED`로 돌린다. chain에서는 선행 실패·취소가 후행 작업으로 전파될 수 있다. periodic work는 성공하거나 실패해도 다음 주기를 위해 다시 `ENQUEUED`되며, 명시적으로 취소될 때만 terminal `CANCELLED`가 된다.

- 일시적 연결 오류만 `retry()`하고 인증 거부나 잘못된 입력은 terminal failure로 분류한다.
- Worker는 적어도 한 번 다시 실행될 수 있다는 가정으로 멱등적으로 만든다. unique work는 중복 **예약 정책**이지 서버 side effect의 exactly-once 보장이 아니다.
- `onStopped()`나 `isStopped`/coroutine cancellation으로 파일·DB handle을 닫되, 프로세스 kill에는 callback이 없을 수 있으므로 checkpoint를 먼저 저장한다.
- WorkManager 2.9.0+와 API 31+에서는 `WorkInfo.getStopReason()`으로 timeout, constraint 변화 등 이전 실행의 중단 원인을 기록한다. 그보다 낮은 버전에는 별도 앱 로그가 필요하다. Android 14+에서 timeout이 반복되면 restricted standby bucket으로 갈 수 있다.

## 일반·expedited·long-running을 구분한다

| 형태 | 적합한 요구 | 제한과 오해 방지 |
| --- | --- | --- |
| 일반 one-time/periodic work | 지연 가능한 sync, upload, cleanup | constraint·Doze·standby·job quota로 지연/중단 가능; periodic은 정확한 주기가 아니다 |
| expedited work | 사용자가 중요하게 여기는 수분 내 짧은 작업을 가능한 빨리 시작 | 즉시성 보장이 아니며 execution quota가 있다. `RUN_AS_NON_EXPEDITED_WORK_REQUEST`로 강등하거나 `DROP_WORK_REQUEST`로 취소하는 정책을 명시한다 |
| long-running Worker | WorkManager의 상태·재시도 모델이 필요한 사용자 가시 장시간 작업 | `setForeground()`로 WorkManager가 FGS와 notification을 관리한다. expedited의 동의어가 아니며 Android 16부터 long-running Worker도 job quota를 소모할 수 있다 |

Android 14+ target에서 long-running Worker는 해당 foreground service type과 선행 permission을 선언해야 한다. 사용자 탭으로 시작한 장시간 데이터 전송이면 long-running Worker를 자동 선택하지 말고 Android 14+ UIDT 또는 `DownloadManager`를 비교한다.

## 구체적 설계 예

사진 메타데이터 200건을 서버와 동기화하는 작업은 unmetered network가 필수가 아니라 비용 최적화 조건인지 먼저 결정한다. 입력에는 전체 payload 대신 sync session ID만 넣고, DB에 각 item 상태와 server idempotency key를 저장한다. 네트워크 단절이면 `retry()`, HTTP 401이면 token 갱신 흐름을 분리하거나 `failure()`, 성공이면 checkpoint를 commit한 뒤 `success()`를 반환한다.

동일 계정 sync에는 unique work 이름과 `ExistingWorkPolicy`를 명시한다. `KEEP`은 이미 예약된 sync를 보존하고, `REPLACE`는 기존 작업을 취소하므로 중간 상태를 폐기해도 되는지에 따라 결정한다.

## 관찰과 테스트

실기기에서는 `WorkInfo.state`, `runAttemptCount`, progress와 `WM-` log를 도메인 작업 ID와 함께 기록한다. WorkManager 2.9.0+이면서 API 31+이면 `stopReason`도 기록한다. API 23+에서는 `adb shell dumpsys jobscheduler`에서 `SystemJobService`, unsatisfied constraint, quota, 최근 START/STOP history를 확인한다.

통합 테스트는 `androidx.work:work-testing`의 `WorkManagerTestInitHelper`와 `TestDriver`로 시간·constraint를 제어한다. 아래 예시는 `@Before`에서 `SynchronousExecutor`를 넣은 `Configuration`으로 `initializeTestWorkManager(context, configuration)`를 호출한 계측 테스트를 전제로 한다. 이 초기화가 없으면 `setAllConstraintsMet()` 직후의 `SUCCEEDED` 단언은 비동기 실행과 경쟁할 수 있다.

```kotlin
val constraints = Constraints.Builder()
    .setRequiredNetworkType(NetworkType.CONNECTED)
    .build()
val request = OneTimeWorkRequestBuilder<SyncWorker>()
    .setConstraints(constraints)
    .build()
workManager.enqueue(request).result.get()

assertThat(workManager.getWorkInfoById(request.id).get().state)
    .isEqualTo(WorkInfo.State.ENQUEUED)
val testDriver = WorkManagerTestInitHelper.getTestDriver()
testDriver.setAllConstraintsMet(request.id)
assertThat(workManager.getWorkInfoById(request.id).get().state)
    .isEqualTo(WorkInfo.State.SUCCEEDED)
```

이 테스트는 scheduling integration을 검증한다. `CoroutineWorker`의 business logic과 cancellation은 `TestListenableWorkerBuilder`와 주입한 dispatcher로 별도 검사한다.

## 공식 근거

- [Task scheduling with WorkManager](https://developer.android.com/develop/background-work/background-tasks/persistent)
- [Define work requests and expedited quota](https://developer.android.com/develop/background-work/background-tasks/persistent/getting-started/define-work)
- [Support for long-running workers](https://developer.android.com/develop/background-work/background-tasks/persistent/how-to/long-running)
- [Manage and stop work](https://developer.android.com/develop/background-work/background-tasks/persistent/how-to/manage-work)
- [Integration tests with WorkManager](https://developer.android.com/develop/background-work/background-tasks/testing/persistent/integration-testing)
- [Optimize battery use for task scheduling APIs](https://developer.android.com/develop/background-work/background-tasks/optimize-battery)

검증일: 2026-08-03. Android 16의 long-running Worker quota와 Android 14+ FGS type 요건은 OS/target SDK 조건이므로 지원 버전별 테스트가 필요하다.
