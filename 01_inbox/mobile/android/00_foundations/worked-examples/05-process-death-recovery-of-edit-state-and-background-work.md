---
title: process death 뒤 편집 상태와 background work 복구
tags: ["android", "android/foundations", "worked-example"]
aliases: ["Recovering edit state and background work after process death"]
date modified: 2026-08-04 02:50:00 +09:00
date created: 2026-08-04 02:50:00 +09:00
---

## process death 뒤 편집 상태와 background work 복구

이 예시는 Learning Spine 4·5·6·8장을 하나의 사건으로 잇는다. 화면 상태와 백그라운드 작업이라는 서로 다른 두 종류의 상태가, process death라는 같은 사건 앞에서 왜 서로 다르게(하나는 사라지고 하나는 남아) 반응하는지를 보여준다.

### 시작 상태

사용자는 게시물 작성 화면에서 긴 글을 쓰고 있다. 화면에는 "사진 첨부" 버튼이 있다.

### 입력

1. 사용자가 "사진 첨부"를 눌러 사진 선택 화면(다른 앱 또는 시스템 picker)으로 이동한다. 이 앱은 이제 background 상태다.
2. 사진을 고르는 동안 시스템이 메모리 확보를 위해 이 앱의 프로세스를 회수한다(5장의 process death).

### 단계별 흐름

1. **화면을 떠나기 전, 작성 중이던 텍스트는 어디에 있었는가(5장)**: 이 텍스트가 `ViewModel`의 필드에만 있었다면, process death와 함께 사라진다. `ViewModel`은 configuration change는 견디지만 process death는 견디지 못하기 때문이다. 그래서 이 앱은 사용자가 입력할 때마다 draft 텍스트를 `SavedStateHandle`에도 반영해뒀어야 한다 — 5장의 실무 규칙("화면이 끝날 때 한 번에 저장한다"는 설계는 process death 경로에서 실행되지 않을 수 있다)이 여기서 그대로 적용된다.
2. **사진 첨부와 함께 업로드가 이미 시작됐다면(6장)**: 만약 업로드 요청이 화면의 `viewModelScope`에 묶인 coroutine으로 시작됐다면, 이것도 process death와 함께 취소된다. 그래서 이런 지속 작업은 애초에 화면 lifetime이 아니라 WorkManager 같은 durable scheduler에 위임돼 있어야 한다. WorkManager는 요청을 메모리가 아니라 내부 DB에 저장하므로, 프로세스가 사라져도 이 요청 자체는 시스템에 남아 있다.
3. **재진입(4장)**: 사용자가 사진을 고르고 앱으로 돌아오면, 그 결과 Intent는 새로 만들어진 프로세스의 Activity로 전달된다. 이 경로는 4장에서 다룬 프로세스 상태 확인 → Zygote fork → `ActivityThread` attach 흐름을 다시 거친다. 즉 겉보기엔 "돌아온 것"처럼 보여도 실제로는 새 프로세스와 새 컴포넌트 인스턴스다.
4. **화면 상태 복원**: 재생성된 화면은 `SavedStateHandle`에 저장해둔 draft 텍스트를 읽어 입력창에 다시 채운다. `ViewModel`에만 있던 값(예: 아직 저장하지 않은 계산 결과, 임시 캐시)은 복원되지 않는다.
5. **업로드 상태 관찰(8장)**: 화면은 업로드 작업의 `WorkInfo`를 관찰하는 Flow를 다시 구독한다. 이 작업이 process death와 무관하게 시스템에 남아 있었으므로, 화면은 "작업이 여전히 진행 중이다" 또는 "이미 완료됐다"는 실제 최신 상태를 즉시 알 수 있다.

### 성공 결과

사용자는 앱으로 돌아왔을 때 작성 중이던 텍스트를 그대로 보고, 사진 업로드도 화면이 사라져 있던 동안 계속 진행됐거나 이미 완료된 것을 확인한다. 화면이 새로 만들어졌다는 사실은 사용자에게 드러나지 않는다.

### 관찰 가능한 신호

- Logcat에서 새 프로세스 ID가 이전과 다른지 확인하면, 정말 process death가 있었는지(단순 화면 재구성이 아닌지) 구분할 수 있다.
- `SavedStateHandle`에 저장된 키와 그 값을 로그로 남기면 복원된 값과 유실된 값을 구분할 수 있다.
- `WorkInfo.state`와 `runAttemptCount`로 업로드 작업이 실제로 계속됐는지, 중간에 재시도가 있었는지 확인한다.
- 개발 중에는 "활동 유지 안함" 개발자 옵션이나 `adb shell am kill <package>`로 이 시나리오를 의도적으로 재현할 수 있다.

### 실패 분기: draft 텍스트가 사라진다

1. 개발자가 draft 텍스트를 `ViewModel`의 `MutableStateFlow`에만 저장하고 `SavedStateHandle`에는 반영하지 않았다고 하자.
2. 사용자가 사진을 고르는 동안 process death가 일어난다.
3. 앱으로 돌아오면 재생성된 `ViewModel`은 초깃값(빈 문자열)으로 시작한다.
4. 업로드는 WorkManager에 위임돼 있었으므로 정상적으로 이어지지만, 정작 사용자가 공들여 쓴 글은 사라져 있다.

이 실패는 "화면 상태"와 "백그라운드 작업"이 같은 사건(process death) 앞에서 반드시 같은 운명을 겪지 않는다는 것을 보여준다. 업로드가 안전했다는 사실이 텍스트도 안전했다는 것을 보장하지 않는다. 두 상태는 각각 다른 저장 계층(`SavedStateHandle` vs WorkManager의 영속 DB)에 독립적으로 책임져야 한다.

### 코드 예시

```kotlin
class ComposePostViewModel(
    private val savedStateHandle: SavedStateHandle,
    private val workManager: WorkManager,
) : ViewModel() {

    // 1. 입력할 때마다 SavedStateHandle에도 반영한다.
    val draftText: StateFlow<String> = savedStateHandle.getStateFlow("draft_text", "")

    fun onTextChanged(text: String) {
        savedStateHandle["draft_text"] = text
    }

    // 2. 업로드는 viewModelScope가 아니라 WorkManager로 위임한다.
    fun attachPhoto(photoUri: Uri) {
        val uploadRequest = OneTimeWorkRequestBuilder<UploadPhotoWorker>()
            .setInputData(workDataOf("photo_uri" to photoUri.toString()))
            .build()
        workManager.enqueueUniqueWork("upload_draft_photo", ExistingWorkPolicy.KEEP, uploadRequest)
        savedStateHandle["pending_upload_id"] = uploadRequest.id.toString()
    }

    // 5. 화면 재진입 시 업로드 상태를 다시 관찰한다.
    val uploadState: Flow<WorkInfo?> = savedStateHandle.getStateFlow<String?>("pending_upload_id", null)
        .flatMapLatest { id ->
            if (id == null) flowOf(null)
            else workManager.getWorkInfoByIdFlow(UUID.fromString(id))
        }
}
```

### 관련 원자 노트

- [설정 변경은 Activity를 재생성할 수 있으므로 상태를 화면 인스턴스에서 분리해야 한다](../../02_app_framework/architecture/app-components/app-component-contracts/configuration-change-recreates-activity-but-not-all-screen-state.md)
- [프로세스 종료 복구에는 saved state와 영속 source of truth가 필요하다](../../02_app_framework/architecture/app-components/app-component-contracts/process-death-recovery-needs-saved-state-and-persistent-source-of-truth.md)
- [ViewModel은 설정 변경 동안 유지되지만 프로세스 사망 복원은 보장하지 않는다](../../02_app_framework/architecture/state-management/viewmodel/viewmodel-survives-configuration-change-not-process-death.md)
- [SavedStateHandle은 프로세스 사망 후 복원해야 하는 작은 상태에 사용한다](../../02_app_framework/architecture/state-management/viewmodel/savedstatehandle-restores-small-process-death-state.md)
- [WorkManager는 지연 가능한 보장 작업의 기본 선택이다](../../04_system_services/background-and-notifications/background-work-contracts/workmanager-is-default-for-deferrable-guaranteed-work.md)
- [백그라운드 제한은 작업 상태를 영속적으로 설계하게 만든다](../../04_system_services/background-and-notifications/background-work-contracts/background-restrictions-require-persistent-work-state.md)

### 관련 Learning Spine 장

- [4장 매니페스트에서 컴포넌트 실행까지](../learning-spine/04-manifest-to-component-execution.md)
- [5장 화면, 프로세스, task와 사용자 상태는 독립적인 lifetime을 가진다](../learning-spine/05-independent-lifetimes-of-screen-process-task-and-state.md)
- [6장 메인 스레드, Binder, coroutine과 durable scheduler는 서로 다른 실행 책임을 진다](../learning-spine/06-main-thread-binder-coroutine-and-durable-work-lifetime.md)
- [8장 데이터, 저장소, 네트워크와 offline recovery](../learning-spine/08-data-storage-network-and-offline-recovery.md)

### 공식 근거

- [Activity state changes](https://developer.android.com/guide/components/activities/state-changes)
- [Persistent work with WorkManager](https://developer.android.com/develop/background-work/background-tasks/persistent)

검증일: 2026-08-04. 이 예시는 Learning Spine 5·6·8장에서 이미 원문 대조를 마친 인용을 재사용했다.
