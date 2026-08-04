---
title: 05-background-work-delayed-or-not-running
tags: ["android", "android/foundations", "diagnostic-runbook"]
aliases: ["Runbook: background work delayed or not running"]
date modified: 2026-08-04 10:28:33 +09:00
date created: 2026-08-04 10:50:00 +09:00
---

## 백그라운드 작업이 지연되거나 실행되지 않는다

### 증상

화면을 닫으면 동기화·업로드 같은 작업이 멈추거나, WorkManager/JobScheduler 에 예약한 작업이 기대한 시점에 실행되지 않는다.

### 재현 조건

- 이 작업이 정확한 시각이 중요한 작업인지, 지연 가능한 작업인지 먼저 구분한다 — 요구사항 자체가 잘못된 API 선택으로 이어졌을 수 있다.
- Doze/앱 대기(App Standby) 상태를 재현하려면 화면을 끄고 충전기를 뽑은 채 일정 시간 방치하거나, `adb shell dumpsys deviceidle force-idle` 류의 명령으로 강제 진입시킨다(기기·OS 버전에 따라 명령이 다를 수 있다).

### 가능한 실패 경계와 우선순위

1. **작업이 애초에 화면의 `viewModelScope` 에 묶여 있었다.** 화면이 사라지면 작업 자체가 취소된 것이지 "지연"이 아니다.
2. **작업은 예약됐지만 constraint 가 만족되지 않았다.** 네트워크 조건, 충전 상태 등 지정한 조건이 충족되지 않아 대기 중인 경우.
3. **작업은 실행됐지만 프로세스가 도중에 죽어 완료 콜백이 오지 않았다.** WorkManager/JobScheduler 는 이를 최소 한 번(at-least-once) 재실행하지만, 재시도 사이 지연이 있을 수 있다.
4. **Doze/앱 대기 상태로 인해 시스템이 실행을 지연시켰다.** 정상적인 배터리 보호 동작이며 "버그"가 아닐 수 있다.
5. **Standby bucket 이 낮아 quota 가 부족하다.** 최근 사용 빈도가 낮은 앱은 시스템이 백그라운드 실행 quota 를 줄인다.

### 조사 절차

1. **작업이 실제로 시스템에 예약됐는지 확인한다.**
   ```bash
   adb shell dumpsys jobscheduler
   ```

   대상 패키지와 `androidx.work.impl.background.systemjob.SystemJobService`(WorkManager 를 쓰는 경우)를 찾아 다음 필드를 확인한다.

   - `Required constraints` / `Satisfied constraints` / `Unsatisfied constraints`: 어떤 조건이 아직 충족되지 않았는지 보여준다. `Unsatisfied constraints: CONNECTIVITY` 라면 코드 실패가 아니라 실행 조건 대기다.
   - `WITHIN_QUOTA`: quota 안에 있는지 여부.
   - `Standby bucket`: 이 앱이 시스템에 의해 어느 사용 빈도 등급으로 분류됐는지.
   - `Job history`: 최근 실행/중단 이력.

2. **WorkManager 를 쓴다면 `WorkInfo.state` 와 진단 브로드캐스트를 함께 본다.**
   ```bash
   adb shell am broadcast -a "androidx.work.diagnostics.REQUEST_DIAGNOSTICS" -p <pkg>
   adb logcat -s WM-DiagnosticsWrkr WM-WorkerWrapper WM-JobScheduler
   ```

   `ENQUEUED` 에 머물러 있다면 constraint 미충족, `RUNNING` 뒤 반복 중단이라면 API 31+ 및 WorkManager 2.9.0+ 환경에서 `WorkInfo.getStopReason()` 을 확인한다.

3. **강제 실행/중단으로 재현 경로를 검증한다(직접 JobScheduler/UIDT job 의 경우).**
   ```bash
   adb shell cmd jobscheduler run -f <pkg> <job_id>
   adb shell cmd jobscheduler timeout <pkg> <job_id>
   ```

   두 번째 명령 뒤 `onStopJob()` 기록과 checkpoint 저장 여부, 재시도 여부를 확인한다. 이 명령은 프로세스 kill 이나 실제 Doze 전체를 대신하지 않는다는 점에 유의한다.

4. **코드에서 재개 지점이 실제로 저장되고 있는지 확인한다.**
   enqueue 전에 논리 작업 ID 와 재개 지점(byte offset, 마지막 처리 항목 등)을 저장소에 남기고 있는지, 재실행 시 그 상태를 읽어 이어가는지 확인한다. 콜백만 믿고 checkpoint 를 저장하지 않으면, 프로세스가 강제 종료될 때(`onStopJob()` 조차 호출되지 않을 수 있다) 진행 상황을 통째로 잃는다.

### OS/API/target SDK 조건

- `stopReason` 조회는 WorkManager 2.9.0+ 이면서 API 31+ 인 조합에서만 가능하다. 그보다 낮은 조합에서는 앱이 남긴 자체 실행/중단 로그로 대체해야 한다.
- Android 14+ 에서 timeout 이 반복되면 restricted standby bucket 으로 강등될 수 있다 — 최근 실패가 잦았던 작업이라면 이 강등 자체가 추가 지연의 원인일 수 있다.
- User-initiated data transfer(UIDT) job 은 API 34+ 에서만 사용 가능하다.

### 다음 조사 경로

- constraint 미충족이 원인이면 → 요구 조건이 제품 요구사항과 맞는지 재검토(예: unmetered network 가 꼭 필요한지)
- 화면 lifetime 에 잘못 묶여 있었다면 → [Learning Spine 6장](../learning-spine/06-main-thread-binder-coroutine-and-durable-work-lifetime.md) 의 durable scheduler 선택 기준으로
- 알림으로 결과를 보여줘야 하는 작업이라면 → [notification missing runbook](06-notification-missing.md) 과 함께 조사

### 관련 자료

- [백그라운드 실행 수단은 실패 비용으로 결정한다](../../04_system_services/background-and-notifications/background-work-contracts/background-work-api-selection-is-a-failure-cost-decision.md)
- [WorkManager는 지연 가능한 보장 작업의 기본 선택이다](../../04_system_services/background-and-notifications/background-work-contracts/workmanager-is-default-for-deferrable-guaranteed-work.md)
- [백그라운드 제한은 작업 상태를 영속적으로 설계하게 만든다](../../04_system_services/background-and-notifications/background-work-contracts/background-restrictions-require-persistent-work-state.md)
- [Worked Example: process death 뒤 편집 상태와 background work 복구](../worked-examples/05-process-death-recovery-of-edit-state-and-background-work.md)
- [Learning Spine 6장 메인 스레드, Binder, coroutine과 durable scheduler](../learning-spine/06-main-thread-binder-coroutine-and-durable-work-lifetime.md)

### 공식 근거

- [Background tasks overview](https://developer.android.com/develop/background-work/background-tasks)
- [Debug WorkManager](https://developer.android.com/develop/background-work/background-tasks/testing/persistent/debug)
- [Optimize battery use for task scheduling APIs](https://developer.android.com/develop/background-work/background-tasks/optimize-battery)

검증일: 2026-08-04. 이 runbook 은 기존 원자 노트(`background-work-api-selection-is-a-failure-cost-decision.md`)에서 이미 공식 문서로 검증된 명령과 필드를 재사용했다.
