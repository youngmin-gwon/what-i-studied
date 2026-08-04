---
title: 03-process-death-state-loss
tags: ["android", "android/foundations", "diagnostic-runbook"]
aliases: ["Runbook: state loss after process death"]
date modified: 2026-08-04 10:28:28 +09:00
date created: 2026-08-04 10:40:00 +09:00
---

## process death 뒤 화면 상태가 사라진다

### 증상

사용자가 다른 앱을 쓰다가(또는 화면을 끈 채 오래 두다가) 돌아왔더니 입력하던 내용, 스크롤 위치, 선택 상태 같은 화면 상태가 초기화돼 있다.

### 재현 조건

- 이 증상이 **configuration change**(회전, 다크모드 전환)에서도 나는지, 백그라운드에 오래 둔 뒤에만 나는지 먼저 구분한다. 둘은 원인이 다르다.
- 의도적 재현 도구를 구분해서 쓴다.
  - **"활동 유지 안함" 개발자 옵션**: 화면을 떠나는 즉시 Activity 를 파괴한다. 프로세스 자체는 유지될 수 있어 configuration-change 에 가까운 재생성을 재현한다.
  - **실제 프로세스 종료**: `adb shell am kill <package>` 또는 Android Studio 의 프로세스 종료 기능. 진짜 process death 를 재현하려면 이쪽을 쓴다.
- 재현 전후로 프로세스 ID 가 바뀌었는지 반드시 확인한다(아래 조사 절차 1 번). 이것이 configuration change 와 process death 를 구분하는 가장 확실한 신호다.

### 가능한 실패 경계와 우선순위

1. **해당 상태가 `ViewModel` 에만 있었다.** `ViewModel` 은 configuration change 는 견디지만 process death 는 견디지 못한다. 가장 흔한 원인.
2. **해당 상태가 `rememberSaveable`/`SavedStateHandle` 로 감싸지 않은 일반 변수였다.** configuration change 에서도 사라진다 — 1 번보다 더 기본적인 문제.
3. **`SavedStateHandle` 에는 값을 저장했지만, 복원 시점에 그 값으로 데이터를 다시 조회하는 로직이 없다.** 식별자는 복원됐지만 그 식별자로 화면에 보여줄 실제 데이터를 다시 불러오지 않은 경우.
4. **백그라운드 작업(업로드 등)이 화면의 `viewModelScope` 에 묶여 있었다.** 상태 소실이 아니라 작업 자체가 취소된 경우 — [background delay runbook](05-background-work-delayed-or-not-running.md) 과 겹친다.

### 조사 절차

1. **새 프로세스인지 확인한다.**
   ```bash
   adb shell pidof <package>
   ```

   재현 전후 PID 가 다르면 process death 가 실제로 일어난 것이다. 같다면 configuration change 나 다른 원인을 의심해야 한다.

2. **사라진 값이 어디에 있었는지 코드에서 역추적한다.**
   `ViewModel` 의 일반 프로퍼티(`var`, plain `MutableStateFlow`)에만 있었는지, `SavedStateHandle` 을 거쳤는지 확인한다. 사라진 값과 남아 있는 값을 나란히 놓고 어느 저장 계층에 있었는지 비교한다.

3. **`SavedStateHandle` 에 실제로 값이 기록되고 있는지 로그로 확인한다.**
   값이 바뀔 때마다 `savedStateHandle["key"] = value` 가 호출되는지, 아니면 화면을 떠날 때 한 번에 저장하는 구조인지 확인한다. "떠날 때 한 번에 저장" 구조는 process death 경로에서 그 저장 자체가 실행되지 않을 수 있다 — `onDestroy` 나 유사 콜백은 process death 시 호출이 보장되지 않는다.

4. **복원된 식별자가 실제로 데이터 재조회에 쓰이는지 확인한다.**
   `SavedStateHandle` 에서 ID 는 복원됐는데 화면이 여전히 빈 상태라면, 그 ID 로 Repository 를 다시 조회하는 코드가 없거나 조회 결과를 화면 상태에 반영하지 못하고 있는 것이다.

5. **백그라운드 작업이 얽혀 있다면 `WorkInfo.state` 를 별도로 확인한다.**
   화면 상태 소실과 백그라운드 작업 소실은 서로 다른 저장 계층(`SavedStateHandle` vs WorkManager 의 영속 DB) 문제이므로 섞어서 진단하지 않는다.

### OS/API/target SDK 조건

- process death 는 특정 API 레벨에 국한된 동작이 아니라 메모리 관리 정책이므로 모든 버전에서 발생할 수 있다. 다만 기기 제조사의 메모리 관리 공격성에 따라 재현 빈도가 크게 달라질 수 있으므로, 특정 기기·제조사에서만 리포트가 몰린다면 [compatibility runbook 없이도] Learning Spine 12 장의 OEM 구현 차이를 의심한다.

### 다음 조사 경로

- configuration change 에서도 재현되면 → 저장 계층 자체가 없는 더 기본적인 문제이므로 `rememberSaveable`/`ViewModel` 배치부터 다시 본다
- 백그라운드 작업까지 함께 사라졌다면 → [background delay runbook](05-background-work-delayed-or-not-running.md)
- 특정 기기·제조사에서만 유독 자주 재현되면 → Android vitals 로 현장 분포 확인([관찰 방법론](../learning-spine/11-observation-testing-and-quality-feedback.md))

### 관련 자료

- [Worked Example: process death 뒤 편집 상태와 background work 복구](../worked-examples/05-process-death-recovery-of-edit-state-and-background-work.md)
- [ViewModel은 설정 변경 동안 유지되지만 프로세스 사망 복원은 보장하지 않는다](../../02_app_framework/architecture/state-management/viewmodel/viewmodel-survives-configuration-change-not-process-death.md)
- [SavedStateHandle은 프로세스 사망 후 복원해야 하는 작은 상태에 사용한다](../../02_app_framework/architecture/state-management/viewmodel/savedstatehandle-restores-small-process-death-state.md)
- [프로세스 종료 복구에는 saved state와 영속 source of truth가 필요하다](../../02_app_framework/architecture/app-components/app-component-contracts/process-death-recovery-needs-saved-state-and-persistent-source-of-truth.md)
- [Learning Spine 5장 화면, 프로세스, task와 사용자 상태는 독립적인 lifetime을 가진다](../learning-spine/05-independent-lifetimes-of-screen-process-task-and-state.md)

### 공식 근거

- [Activity state changes](https://developer.android.com/guide/components/activities/state-changes)
- [Save UI states](https://developer.android.com/topic/libraries/architecture/saving-states)

검증일: 2026-08-04. 이 runbook 은 Learning Spine 5 장과 Worked Example 5 에서 이미 원문 대조를 마친 내용을 재사용했다.
