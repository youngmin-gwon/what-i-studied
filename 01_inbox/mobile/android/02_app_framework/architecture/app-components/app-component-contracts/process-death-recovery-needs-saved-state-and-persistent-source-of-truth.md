---
title: process-death-recovery-needs-saved-state-and-persistent-source-of-truth
tags: [android, android/app-components, android/architecture]
aliases: ["Process death 복구는 saved state와 persistent source of truth를 필요로 한다"]
date modified: 2026-08-06 15:03:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Process death 복구는 최소 saved state와 영속 source of truth를 결합한다

시스템이 background process를 회수하면 `Application`, singleton, [viewmodel](../../../viewmodel.md), coroutine과 in-memory cache가 함께 사라진다. 정리 callback이나 마지막 저장 기회는 보장되지 않는다. task 기록이 남아 사용자가 돌아왔을 때 화면처럼 보일 수 있어도 실제로는 새 PID와 새 component instance다.

### 복구 메커니즘

```kotlin
class EditorViewModel(
    private val savedStateHandle: SavedStateHandle,
    private val drafts: DraftRepository,
) : ViewModel() {
    var draftId: String?
        get() = savedStateHandle["draft_id"]
        set(value) { savedStateHandle["draft_id"] = value }

    suspend fun restore(): Draft? = draftId?.let(drafts::load)
}
```

`SavedStateHandle`에는 선택 ID, 검색어, tab처럼 화면을 다시 찾는 작은 값만 둔다. 본문, bitmap, 목록과 완료돼야 하는 business mutation은 Room/DataStore/file/server 같은 persistent source에 값이 바뀌는 시점부터 기록한다. saved state는 `Activity`가 stopped일 때 저장되며, stopped 상태에서 쓴 값은 다시 start→stop을 거치기 전에는 새 snapshot에 반영되지 않을 수 있다.

### 실제 process death 재현

```bash
# 1. 복구할 상태를 만든 뒤 Home으로 보내 Activity를 stopped 상태로 만든다.
adb shell input keyevent KEYCODE_HOME
adb shell pidof com.example.app

# 2. task는 남기고 background process만 회수한다.
adb shell am kill com.example.app
adb shell pidof com.example.app

# 3. Recents에서 task로 돌아온 뒤 새 PID와 복원 값을 확인한다.
adb shell pidof com.example.app
```

`am force-stop`은 package를 stopped state로 만들고 task·예약 실행에도 더 강한 영향을 주므로 일반적인 low-memory process death와 같은 테스트가 아니다. 개발자 옵션의 “활동 유지 안 함”도 Activity destruction을 재현할 뿐 process 자체가 죽었다는 보장이 없다.

### 실패·관찰 신호

- 복귀 전후 PID가 달라지고 `Application.onCreate()`가 다시 찍혀야 process recreation을 확인한 것이다.
- ViewModel instance ID가 바뀌었는데 입력·선택이 복원되면 saved state 경로가 작동한 것이다.
- Room의 draft는 남고 ViewModel에만 둔 임시 object가 사라지는 차이를 의도적으로 테스트한다.
- `TransactionTooLargeException`이나 저장 시 frame drop이 보이면 saved-state Bundle에 큰 object를 넣은 신호다.

관련 노트: [SavedStateHandle은 프로세스 데스의 소량 상태를 복구한다](../../state-management/viewmodel/savedstatehandle-restores-small-process-death-state.md)

상위 문서: [App Component Contracts](./app-component-contracts.md)

공식 문서: [Save UI states](https://developer.android.com/topic/libraries/architecture/saving-states), [Processes and app lifecycle](https://developer.android.com/guide/components/activities/process-lifecycle)
