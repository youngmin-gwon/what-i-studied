---
title: 05-process-death-recovery-of-edit-state-and-background-work
tags: ["android", "android/foundations", "worked-example"]
aliases: ["Recovering edit state and background work after process death"]
date modified: 2026-08-04 16:10:00 +09:00
date created: 2026-08-04 02:50:00 +09:00
---

## process death 뒤 편집 상태와 background work 복구

이 예시는 Learning Spine 4·5·6·8 장을 하나의 실무 시나리오로 잇는다. 화면 상태와 백그라운드 작업이라는 서로 다른 두 종류의 상태가, process death 라는 같은 시스템 사건 앞에서 왜 서로 다르게(하나는 사라질 수 있고 하나는 영속하여 남아) 반응하는지를 다계층 시스템 파이프라인 관점에서 분석한다.

### 시작 상태

사용자는 게시물 작성 화면에서 긴 글을 작성하고 있다. 화면에는 "사진 첨부" 버튼이 있으며, 앱은 작성 중인 글(Text Draft)과 대용량 첨부 미디어의 백그라운드 업로드(Background Work)를 동시에 처리하는 구조다.

### 입력

1. 사용자가 "사진 첨부"를 눌러 시스템 Photo Picker 또는 외부 카메라/갤러리 앱으로 이동한다. 이 순간 작성 앱은 background 상태가 된다.
2. 미디어를 선택하거나 외부 앱에 머무는 동안, 시스템이 메모리 확보를 위해 이 작성 앱의 프로세스를 회수한다(5 장의 process death).

---

### 다계층 실행 흐름 (UI → App Framework → System Server → Kernel)

1. **UI & Framework Layer (화면 이탈 시점 - SavedState vs Persistent Storage)**
   - 앱이 background 로 전환될 때, `ActivityThread.handleStopActivity()` 가 호출되며 `SavedStateRegistryController` 에 의해 UI 컴포넌트들의 `onSaveInstanceState(Bundle)` 가 트리거된다.
   - **경량 편집 상태 (Draft Text)**: `SavedStateHandle` 에 담긴 데이터는 `ActivityRecord.icicle` (Bundle)로 직렬화되어 Binder IPC 를 통해 `ActivityTaskManagerService` (ATMS) 로 전달된다.
   - **중량 작업 상태 (Media Upload)**: 만약 미디어 업로드가 화면의 `viewModelScope` 나 `lifecycleScope` 에 바인딩된 coroutine 으로 실행 중이었다면, process death 시 프로세스 메모리가 해제되면서 작업이 즉시 취소된다. 따라서 이 작업은 enqueue 시점에 `WorkManager` (App Framework)에 위임되어 SQLite DB (`/data/data/<pkg>/databases/FrameworkWorkManager.db`) 에 영속 저장(Persistent Storage)되어야 한다.

2. **System Server & IPC Layer (Process Death 발생 시점)**
   - 앱이 background 로 이동하면 `ActivityManagerService` (AMS) 는 프로세스의 OOM adjustment score (`adj`) 를 `cached` (900~999) 레벨로 낮춘다.
   - 시스템 메모리가 부족해지면 Kernel LMK (Low Memory Killer) / PSI (Pressure Stall Information) 가 signal 9 (`SIGKILL`) 를 보내 프로세스를 강제 종료한다.
   - 이때 ATMS 는 RAM 에서 프로세스가 제거되어도, 시스템 서버 메모리의 `ActivityRecord` 내부에 직렬화된 `SavedState` Bundle (`icicle`) 을 영속적으로 보관한다. 동시에 `JobSchedulerService` 는 WorkManager 에 의해 등록된 `JobInfo` 스케줄링을 계속 유지한다.

3. **Kernel & Framework Layer (앱 재진입 및 프로세스 재생성)**
   - 사용자가 외부 picker 에서 작업 후 작성 앱으로 복귀하면, ATMS 는 해당 `ActivityRecord` 의 상태를 확인하고 Zygote 에 `fork()` IPC 요청을 보내 새 프로세스를 생성한다.
   - 새로 생성된 프로세스의 `ActivityThread.main()` 이 실행되고, `attach()` → `handleLaunchActivity()` 흐름을 거쳐 `Activity` 및 `ViewModel` 이 새로 인스턴스화된다.

4. **UI & Work Recovery Layer (상태 및 작업 복원)**
   - **Draft Text 복원**: ATMS 에서 전달받은 `SavedState` Bundle 이 `SavedStateHandle` 로 재주입되어 `ViewModel` 이 생성된다. Compose UI 의 `TextField` 는 `SavedStateHandle` 의 `StateFlow` 를 관찰하여 작성 중이던 글을 다시 화면에 복원한다.
   - **Work Manager 복원**: `WorkManager` 가 초기화되면서 SQLite DB 에 남아 있던 기존 업로드 작업 ID (`pending_upload_id`) 의 최신 `WorkInfo` 상태를 `SystemJobService` / `JobScheduler` 와 동기화한다. 화면은 `getWorkInfoByIdFlow()` 를 통해 업로드 진행률 또는 완료 상태를 다시 관찰한다.

---

### 성공 결과 vs 실패 분기 비교

| 평가 항목 | 성공 경로 (SavedStateHandle + WorkManager) | 실패 분기 (ViewModel Only + coroutineScope) |
| :--- | :--- | :--- |
| **Draft Text 상태** | `SavedStateHandle` (ATMS `icicle` Bundle)에서 읽어와 100% 복원됨 | `ViewModel` 메모리 해제로 인해 빈 문자열(`""`)로 초기화 (유실) |
| **미디어 업로드 작업** | `WorkManager` 영속 DB 저장으로 process death 와 무관하게 백그라운드 재개/완료 | `viewModelScope` 취소 및 프로세스 강제 종료로 작업 영구 중단 |
| **사용자 경험 (UX)** | 프로세스 재시작 여부를 사용자가 인지하지 못함 | 공들여 작성한 텍스트가 사라지고 업로드 실패 |
| **시스템 신호** | PID 변경되나 `SavedState` restored 로그 및 `WorkInfo.State.RUNNING/SUCCEEDED` 관찰 | PID 변경과 함께 UI re-init (empty state) 및 network connection reset 로그 |

---

### 관찰 가능한 신호 및 CLI 진단 명령

1. **Process Death 의도적 강제 재현 및 PID 변화 관찰**
   ```bash
   # 1. 대상 앱의 현재 PID 확인
   adb shell pidof com.example.writerapp

   # 2. 앱을 background로 보낸 후 process death 강제 수행 (Activity는 유지하되 프로세스만 살해)
   adb shell am kill com.example.writerapp

   # 3. 앱으로 복귀 후 새 PID 확인 (이전 PID와 다르면 process death 재진입 성공)
   adb shell pidof com.example.writerapp
   ```

2. **ATMS Process & Activity State 진단**
   ```bash
   # SavedState Bundle 이 저장된 ActivityRecord 상태 확인
   adb shell dumpsys activity activities com.example.writerapp | grep -E "isStopping|icicle|state"
   ```

3. **WorkManager 영속 Job Scheduler 상태 확인**
   ```bash
   # System JobScheduler에 등록된 WorkManager 작업의 persistence 확인
   adb shell dumpsys jobscheduler com.example.writerapp
   ```

4. **Logcat 실시간 모니터링 필터**
   ```bash
   adb logcat -v threadtime | grep -E "ActivityThread|SavedStateRegistry|WM-Worker|WriterViewModel"
   ```

---

### Android 14 / 15 / 16 특화 동작

- **Predictive Back Gesture (Android 14+)**: Android 14 부터 도입된 Predictive Back 애니메이션 처리 시 `OnBackPressedDispatcher` 는 Activity 가 finish 되기 전에 `SavedStateRegistry` 의 최신 상태를 동기적으로 보존해야 한다. Process death 복원 시 Predictive back 상태 정보도 함께 복원된다.
- **TransactionTooLargeException 방지 (<50KB 룰)**: Binder Transaction 최대 허용 제한은 약 1MB 이지만, 동시 IPC 통신을 고려하여 `SavedStateHandle` 에 저장하는 데이터 크기는 **50KB 이하**로 제한해야 한다. 작성 중인 글이 매우 긴 대용량 텍스트인 경우 `SavedStateHandle` 에는 `draft_id` (UUID String) 만 보관하고, 텍스트 본문은 `Room` 이나 `DataStore` 에 저장하는 **Persistent Source of Truth Pattern** 을 사용해야 한다.
- **Android 14+ Foreground Service / Job Execution Restrictions**: Android 14 이상에서 백그라운드 업로드 작업이 네트워크 상태나 배터리 최적화 정책의 영향을 받지 않고 즉시 수행되어야 하는 경우, WorkManager 의 `OutOfQuotaPolicy.RUN_AS_NON_EXPEDITED_WORK_REQUEST` 처리 및 `foregroundServiceType="shortService"` 또는 `"dataSync"` 선언 규칙을 준수해야 한다.

---

### 코드 예시

```kotlin
class ComposePostViewModel(
    private val savedStateHandle: SavedStateHandle,
    private val workManager: WorkManager,
    private val draftRepository: DraftRepository // Room/DataStore 기반 영속 저장소
) : ViewModel() {

    // 1. SavedStateHandle에는 대용량 텍스트 대신 draft_id (작은 크기의 키)를 보관 (TransactionTooLargeException 방지)
    val draftId: String = savedStateHandle["draft_id"] ?: UUID.randomUUID().toString().also {
        savedStateHandle["draft_id"] = it
    }

    // 2. 실제 텍스트 본문은 Room DB / DataStore persistent source of truth에서 읽어옴
    val draftText: StateFlow<String> = draftRepository.getDraftFlow(draftId)
        .stateIn(viewModelScope, SharingStarted.WhileSubscribed(5000), "")

    fun onTextChanged(text: String) {
        viewModelScope.launch {
            draftRepository.saveDraft(draftId, text)
        }
    }

    // 3. 업로드 작업은 process death에도 견디는 WorkManager durable scheduler로 위임
    fun attachPhotoAndUpload(photoUri: Uri) {
        val uploadRequest = OneTimeWorkRequestBuilder<UploadPhotoWorker>()
            .setInputData(workDataOf("photo_uri" to photoUri.toString(), "draft_id" to draftId))
            .setConstraints(
                Constraints.Builder()
                    .setRequiredNetworkType(NetworkType.CONNECTED)
                    .build()
            )
            .build()

        workManager.enqueueUniqueWork(
            "upload_draft_photo_$draftId",
            ExistingWorkPolicy.KEEP,
            uploadRequest
        )
        savedStateHandle["pending_upload_id"] = uploadRequest.id.toString()
    }

    // 4. 앱 재진입 및 Process Death 복원 시 WorkManager DB 작업의 최신 진행 상태 재구독
    @OptIn(ExperimentalCoroutinesApi::class)
    val uploadState: Flow<WorkInfo?> = savedStateHandle.getStateFlow<String?>("pending_upload_id", null)
        .flatMapLatest { id ->
            if (id == null) flowOf(null)
            else workManager.getWorkInfoByIdFlow(UUID.fromString(id))
        }
}
```

---

### 관련 Diagnostic Runbook

- [03-process-death-state-loss.md](../diagnostic-runbooks/03-process-death-state-loss.md)
- [05-background-work-delayed-or-not-running.md](../diagnostic-runbooks/05-background-work-delayed-or-not-running.md)

### 관련 Learning Spine 장

- [4장 매니페스트에서 컴포넌트 실행까지](../learning-spine/04-manifest-to-component-execution.md)
- [5장 화면, 프로세스, task와 사용자 상태는 독립적인 lifetime을 가진다](../learning-spine/05-independent-lifetimes-of-screen-process-task-and-state.md)
- [6장 메인 스레드, Binder, coroutine과 durable scheduler는 서로 다른 실행 책임을 진다](../learning-spine/06-main-thread-binder-coroutine-and-durable-work-lifetime.md)
- [8장 데이터, 저장소, 네트워크와 offline recovery](../learning-spine/08-data-storage-network-and-offline-recovery.md)

### 관련 원자 노트

- [설정 변경은 Activity를 재생성할 수 있으므로 상태를 화면 인스턴스에서 분리해야 한다](../../02_app_framework/architecture/app-components/app-component-contracts/configuration-change-recreates-activity-but-not-all-screen-state.md)
- [프로세스 종료 복구에는 saved state와 영속 source of truth가 필요하다](../../02_app_framework/architecture/app-components/app-component-contracts/process-death-recovery-needs-saved-state-and-persistent-source-of-truth.md)
- [ViewModel은 설정 변경 동안 유지되지만 프로세스 사망 복원은 보장하지 않는다](../../02_app_framework/architecture/state-management/viewmodel/viewmodel-survives-configuration-change-not-process-death.md)
- [SavedStateHandle은 프로세스 사망 후 복원해야 하는 작은 상태에 사용한다](../../02_app_framework/architecture/state-management/viewmodel/savedstatehandle-restores-small-process-death-state.md)
- [WorkManager는 지연 가능한 보장 작업의 기본 선택이다](../../04_system_services/background-and-notifications/background-work-contracts/workmanager-is-default-for-deferrable-guaranteed-work.md)
- [백그라운드 제한은 작업 상태를 영속적으로 설계하게 만든다](../../04_system_services/background-and-notifications/background-work-contracts/background-restrictions-require-persistent-work-state.md)

### 공식 근거

- [Activity state changes](https://developer.android.com/guide/components/activities/state-changes)
- [Save UI states](https://developer.android.com/topic/libraries/architecture/saving-states)
- [Persistent work with WorkManager](https://developer.android.com/develop/background-work/background-tasks/persistent)

검증일: 2026-08-04. 이 예시는 Learning Spine 4·5·6·8 장과 Android 14/15 process death / SavedStateHandle specs 원문 대조를 마쳤다.
