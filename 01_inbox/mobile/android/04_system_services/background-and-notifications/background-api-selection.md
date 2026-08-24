---
title: background-api-selection
tags: ["android", "android/system-services"]
aliases: []
date modified: 2026-08-03 17:35:35 +09:00
date created: 2026-08-03 16:59:23 +09:00
---

## 백그라운드 실행 수단은 실패 비용으로 결정한다

상위 지도: [백그라운드 작업 계약](./background-work.md)

API 선택은 "백그라운드인가"가 아니라 **누가 시작했고, 언제 시작해야 하며, 중단·재실행돼도 되는가**를 구체화하는 일이다. 먼저 전용 API 를 찾고, 없을 때 작업 생명주기와 실패 비용을 비교한다.

### 실제 요구사항별 결정표

| 요구사항 | 선택 | 보장과 포기 | 관찰 신호 |
| --- | --- | --- | --- |
| 검색 화면을 닫으면 버려도 되는 자동완성 요청 | 화면/ViewModel 소유 coroutine | 프로세스 종료 뒤 복구 없음; 소유자 종료 시 취소가 올바른 결과 | coroutine 취소, UI state |
| 앱을 닫아도 서버에 분석 로그를 결국 전송, 수분 지연 허용 | WorkManager | 예약·constraint·재시도 영속화; 즉시/정확 시각/연속 실행은 보장하지 않음 | `WorkInfo.state`, `runAttemptCount`, WM 로그; 2.9.0+/API 31+ 의 `stopReason` |
| WorkManager 에 없는 `JobInfo` 기능(`setPrefetch`, UIDT, pending reason 등)이 필요 | 직접 JobScheduler | 플랫폼 기능과 stop reason 사용; API 버전 분기·job ID·재스케줄 설계 책임 증가 | `JobService` callback, `JobParameters.stopReason`, `dumpsys jobscheduler` |
| Android 14+ 에서 사용자가 탭한 대용량 앨범 다운로드를 즉시 진행하고 진행률 제공 | UIDT job | `RUN_USER_INITIATED_JOBS` 선언, 허용된 visible 상태에서 예약, 실행 중 `setNotification()` 필요; 일반 job quota 면제지만 constraint·전송 시간·시스템 건강·열·메모리로 중단 가능 | notification/Task Manager, `onStopJob`, stop reason, 저장된 offset |
| 짧고 중요한 메시지 전송을 앱 이탈 뒤 수분 내 완료 | expedited WorkManager | quota 가 있을 때 빠른 시작; out-of-quota 정책에 따라 일반 작업으로 강등 또는 취소, 시스템 부하로 지연 가능 | `WorkInfo`, quota/constraint, `WM-` 로그 |
| 통화·내비게이션·재생처럼 즉시 시작하고 사용자가 계속 인지하는 허용된 작업 | 직접 foreground service 또는 해당 전용 API | ongoing notification 과 type/permission 계약; background start 제한·type 별 timeout/정책 적용 | notification, service lifecycle, 시작 예외, Task Manager |
| 오전 8 시 복약 알림처럼 시각 자체가 기능 | AlarmManager | 시각 트리거; 긴 작업 컨테이너가 아니며 exact alarm 은 별도 요건과 배터리 비용 존재 | `PendingIntent` 수신 시각, alarm dumpsys |
| 공개 URL 의 장시간 파일 다운로드를 시스템 UI·재시도와 함께 위임 | DownloadManager | HTTP 다운로드를 연결 변화와 재부팅에 걸쳐 관리; 임의 프로토콜·복잡한 앱 도메인 workflow 에는 부적합 | `query()` 의 status/reason, 완료 broadcast, Downloads UI |

`JobScheduler` 직접 사용은 WorkManager 보다 일반적으로 우월한 선택이 아니다. UIDT 처럼 WorkManager 가 노출하지 않는 플랫폼 계약이 실제 요구일 때 선택한다. 기기 연결, 미디어, 위치처럼 task-specific API 가 있으면 generic scheduler 나 FGS 보다 먼저 검토한다.

### 중단을 정상 상태로 설계한다

1. enqueue 전에 논리 작업 ID, 입력, 재개 지점을 DB 에 저장한다.
2. 실행기는 DB 에서 현재 상태를 읽고 서버 idempotency key 또는 원자적 상태 전이로 중복 결과를 막는다.
3. WorkManager 의 `onStopped()`/`isStopped`, JobScheduler 의 `onStopJob()`/`stopReason`, coroutine 취소를 받아 리소스를 닫는다. 프로세스 kill 에는 callback 이 없을 수 있으므로 callback 만 믿지 않는다.
4. 재실행은 마지막 checkpoint 에서 이어가며, 영구 오류와 일시 오류를 분리한다.

예: 2 GB 파일을 620 MB 까지 받은 뒤 열 상태 때문에 UIDT 가 중단됐다면 성공으로 표시하지 않는다. byte offset 과 서버 validator 를 저장하고 `onStartJob()` 재호출 때 검증 후 재개한다. Task Manager 의 Stop 은 프로세스를 즉시 종료할 수 있어 `onStopJob()` 도 호출되지 않을 수 있다.

### 실행 가능한 관찰 절차

API 23+ 기기에서 package 가 실제로 어떤 job 을 기다리는지 확인한다.

```sh
adb shell dumpsys jobscheduler
```

출력에서 package 와 `androidx.work.impl.background.systemjob.SystemJobService` 를 찾고 `Required constraints`, `Satisfied constraints`, `Unsatisfied constraints`, `WITHIN_QUOTA`, `Standby bucket`, `Job history` 를 읽는다. `Unsatisfied constraints: CONNECTIVITY` 이면 Worker 코드 실패가 아니라 실행 조건 대기다.

WorkManager 2.4+ debug build 에서는 예약 상태를 logcat 으로 요청한다.

```sh
adb shell am broadcast -a "androidx.work.diagnostics.REQUEST_DIAGNOSTICS" -p "com.example.app"
adb logcat -s WM-DiagnosticsWrkr WM-WorkerWrapper WM-JobScheduler
```

`Scheduled work` 의 ID·class·state·unique name 을 도메인 작업 ID 와 대조한다. `RUNNING` 뒤 반복 중단이면 WorkManager 2.9.0+ 및 API 31+ 에서 `WorkInfo.getStopReason()` 을 확인하고, 그보다 낮은 조합에서는 앱이 남긴 실행·중단 로그를 확인한다.

직접 JobScheduler/UIDT job 은 테스트 job ID 로 강제 실행·중단 경로를 재현한다.

```sh
adb shell cmd jobscheduler run -f com.example.app 42
adb shell cmd jobscheduler timeout com.example.app 42
```

두 번째 명령 뒤 `onStopJob()` 기록, checkpoint 저장, 재시도 여부를 확인한다. API 31+ 에서는 `JobParameters.getStopReason()` 도 기록한다. 이 명령은 프로세스 kill 이나 실제 Doze 전체를 대신하지 않는다.

### 공식 근거

- [Background tasks overview](https://developer.android.com/develop/background-work/background-tasks)
- [Data transfer background task options](https://developer.android.com/develop/background-work/background-tasks/data-transfer-options)
- [User-initiated data transfer](https://developer.android.com/develop/background-work/background-tasks/uidt)
- [Optimize battery use for task scheduling APIs](https://developer.android.com/develop/background-work/background-tasks/optimize-battery)
- [Debug WorkManager](https://developer.android.com/develop/background-work/background-tasks/testing/persistent/debug)
- [DownloadManager API](https://developer.android.com/reference/android/app/DownloadManager)

검증일: 2026-08-03. UIDT 는 API 34+, WorkManager/JobScheduler 의 stop reason 과 quota 동작은 OS 및 라이브러리 버전별 조건을 함께 확인해야 한다.
