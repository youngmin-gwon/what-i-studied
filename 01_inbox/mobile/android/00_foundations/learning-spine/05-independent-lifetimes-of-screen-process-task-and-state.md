---
title: 05-independent-lifetimes-of-screen-process-task-and-state
tags: ["android", "android/foundations", "learning-spine"]
aliases: ["Independent lifetimes of screen, process, task, and state"]
date modified: 2026-08-05 11:00:00 +09:00
date created: 2026-08-03 20:45:00 +09:00
---

## 화면, 프로세스, task 와 사용자 상태는 독립적인 lifetime 을 가진다

4 장은 등록된 컴포넌트가 Intent 해석과 프로세스 상태 확인을 거쳐 실제로 시작되는 경로를 다뤘다. 그러나 컴포넌트가 시작됐다는 사실은 그 컴포넌트, 그것이 속한 프로세스, 그것이 속한 task, 그리고 사용자가 화면에서 보던 상태가 앞으로도 함께 살고 함께 죽는다는 뜻이 아니다. 이 장은 그 네 가지가 왜 서로 다른 lifetime 을 갖는지를 다룬다.

이 장의 핵심 질문은 다음과 같다.

>화면, 컴포넌트, 프로세스, task 와 사용자 상태는 왜 함께 시작하고 함께 끝나지 않는가?

이 장은 각 상태 저장 API 의 사용법을 처음부터 가르치지 않는다. `ViewModel`, `rememberSaveable`, `SavedStateHandle` 의 구체적인 사용법은 각 원자 노트가 다루는 수준으로 남겨두고, 여기서는 서로 다른 사건이 서로 다른 lifetime 을 어떻게 끊는지 하나의 모델로 연결한다.

### 1. 겹쳐 있는 여러 lifetime 을 구분한다

한 화면을 이루는 것처럼 보이는 요소들은 실제로는 서로 다른 소유자와 종료 조건을 가진 여러 lifetime 이 겹쳐 있는 것이다.

| Lifetime | 누가 관리하는가 | 끝나는 조건의 예 |
| --- | --- | --- |
| 설치된 패키지 identity 와 사용자 데이터 | PackageManager, 영속 저장소(3 장) | 삭제(uninstall) |
| Linux process | Zygote/AMS(4 장) | 시스템의 메모리 회수, force-stop, crash |
| Task 와 back stack | ActivityTaskManagerService | 사용자의 task 제거, 마지막 Activity 의 finish |
| Activity/Service/Receiver/Provider 인스턴스 | 각 컴포넌트 계약 | configuration change, finish, task 제거, 프로세스 종료 |
| ViewModel | Jetpack 아키텍처 컴포넌트 | 소유자(Activity/Fragment/Navigation 진입점)가 완전히 종료될 때 |
| Transient UI state(스크롤 위치, 입력값 등) | `rememberSaveable`/저장된 인스턴스 상태 | 명시적으로 저장하지 않으면 화면 재생성 시 소실 |

이 표를 하나로 뭉뚱그리면 "화면이 죽으면 다 사라진다" 또는 "프로세스가 살아 있으면 다 괜찮다"는 잘못된 직관이 생긴다. 실제로는 사건마다 어느 lifetime 이 끊기고 어느 lifetime 은 유지되는지가 다르다.

### 2. Configuration change 는 화면만 깨끗하게 재생성한다

회전, 언어, 다크 모드, 창 크기 변경 같은 configuration change 가 일어나면 시스템은 원래 Activity 인스턴스에 `onPause → onStop → onDestroy` 를 호출하고, 새 인스턴스에 `onCreate → onStart → onResume` 을 호출한다.

이 경로에서 프로세스는 종료되지 않는다. Configuration change 는 사용자가 화면을 보고 있는 상태에서 일어나는 foreground 사건이며, 메모리 회수가 필요해서 시스템이 개입하는 사건이 아니다. 그래서 이 경로에는 애초에 프로세스를 회수할 이유가 없다. `ViewModel` 은 Activity 인스턴스가 아니라 그 소유자의 `ViewModelStore` 에 남아 있으므로 재생성된 새 Activity 가 같은 `ViewModel` 인스턴스를 다시 참조할 수 있다. 반면 `rememberSaveable` 로 감싸지 않은 일반 변수나 Composable 지역 상태는 이 재생성 과정에서 사라진다.

즉 configuration change 는 "화면 인스턴스"라는 lifetime 만 끊고, 프로세스와 ViewModel 이라는 lifetime 은 그대로 둔다.

### 3. 시스템에 의한 process death 는 정리 콜백을 보장하지 않는다

사용자가 다른 앱을 오래 쓰거나 메모리가 부족해지면, 시스템은 화면에 보이지 않는 앱의 프로세스를 회수할 수 있다. 공식 문서는 이 경로를 configuration change 와 분명히 구분한다.

>"If an app is in the background and the system needs to free up memory for a foreground app, the system can kill the background app. When the system kills an app, there is no guarantee that onDestroy is called in the app."

이것이 이 절의 핵심이다. Configuration change 는 정해진 콜백 순서를 보장하는 재생성이지만, process death 는 그 보장이 없는 소멸이다. 프로세스가 사라지면 그 프로세스 안에 있던 `ViewModel`, in-memory 캐시, 아직 저장하지 않은 화면 상태는 모두 함께 사라진다.

사용자가 나중에 같은 화면으로 "돌아오면", 시스템은 겉보기에 이전과 같은 화면을 다시 보여줄 수 있다. 하지만 이것은 이전 프로세스가 이어진 것이 아니라, 새 프로세스와 새 컴포넌트 인스턴스를 만든 뒤 명시적으로 저장해 둔 상태만 복원한 결과다. 이때 복원되는 것은 개발자가 `rememberSaveable` 이나 `SavedStateHandle` 에 미리 담아 둔 작은 값뿐이며, `ViewModel` 에만 있던 값이나 저장하지 않은 로컬 변수는 복원되지 않는다.

이 구분은 1 절 "설치된 패키지 identity" 층위와는 다른 층위에서 일어난다. 프로세스가 회수돼도 설치된 패키지, 사용자 데이터, 영속 저장소는 영향을 받지 않는다.

실무 규칙은 다음과 같다. `onDestroy` 나 그 시점의 콜백에서 상태를 저장하는 것에 의존하면 안 된다. 저장이 필요한 값은 그 값이 바뀌는 시점마다(예: `SavedStateHandle` 갱신, 영속 저장소 기록) 미리 반영해 둬야 하며, "화면이 끝날 때 한 번에 저장한다"는 설계는 process death 경로에서 그 저장 자체가 실행되지 않을 수 있다.

### 4. Task 제거와 화면 종료는 OS 내비게이션 기록의 종료다

Task 와 back stack 은 화면 상태가 아니라 사용자가 Activity 들을 어떤 순서로 오갔는지를 시스템이 관리하는 기록이다. 뒤로 가기로 화면이 `finish()` 되면 그 화면의 Activity 인스턴스와 `ViewModel` 만 정리 대상이 되고, task 의 나머지 항목과 프로세스는 영향을 받지 않는다.

반면 사용자가 최근 앱 목록(recents)에서 task 전체를 제거하면, 그 task 에 속한 모든 Activity 가 파괴 대상이 된다. 이 task 와 연관된 Service 가 있다면, 이 사건은 그 Service 의 생존 여부를 다시 판단해야 하는 별도의 신호가 된다. Task 제거는 화면 하나가 끝나는 사건이 아니라 그 task 전체의 내비게이션 기록이 끝나는 사건이라는 점에서, 개별 화면의 뒤로 가기와는 영향 범위가 다르다.

### 5. force-stop 과 uninstall 은 프로세스 종료보다 더 강한 경계다

force-stop 은 시스템이 메모리 확보를 위해 조용히 회수하는 process death 보다 더 명시적이고 강한 개입이다. 프로세스가 종료되고 task 가 제거되는 것은 물론, 그 앱의 모든 컴포넌트 상태가 초기화된다. force-stop 과 일반 process death 를 같은 사건으로 취급하면 안 된다.

force-stop 은 앱을 패키지 수준의 "stopped" 상태(`FLAG_STOPPED`)로 만든다. 공식 문서는 이 상태의 의도를 "사용자가 앱을 직접 실행하거나(직접 실행) 공유 시트·위젯·라이브 배경화면 선택 등으로 간접적으로 상호작용하기 전까지는 이 상태를 유지하는 것"이라고 명시한다. 즉 브로드캐스트, 예약된 job/alarm 을 포함해 시스템이 자동으로 앱을 다시 깨우는 어떤 경로도 이 상태를 해제하지 못하며, 오직 사용자의 직접/간접 실행만이 해제한다. Android 15 부터는 이 의도된 동작에 맞춰 stopped 상태 진입 시 대기 중인 pending intent 까지 전부 취소하도록 강화됐다. 사용자 행동으로 stopped 상태에서 벗어나면 시스템은 `ACTION_BOOT_COMPLETED` 를 다시 전달해 앱이 필요한 등록을 복구할 기회를 준다.

uninstall 은 여기서 한 단계 더 나아가 3 장이 다룬 설치된 패키지 identity 와 영속 저장소까지 제거한다. 3 장의 업데이트/서명 불일치/재설치/force-stop 비교표가 이미 UID·데이터 연속성 축에서 이 차이를 다뤘으므로, 이 장에서는 그 표를 반복하지 않고 lifetime 축에서만 연결한다.

### 사건별 lifetime 비교표

| 사건 | Linux process | Task/back stack | Component 인스턴스 | ViewModel/transient state | 영속 저장소 |
| --- | --- | --- | --- | --- | --- |
| Configuration change | 유지 | 유지 | 파괴 후 즉시 재생성 | ViewModel 유지, transient state 는 저장해 둔 것만 복원 | 무관 |
| 뒤로 가기로 화면 finish | 유지 | 해당 항목만 제거 | 그 화면만 파괴 | 그 화면의 ViewModel 만 정리 | 무관 |
| Task 제거(recents 에서 스와이프) | 연관 Service 유무에 따라 다름 | 제거 | task 내 모든 Activity 파괴 | 모두 정리 | 무관 |
| 시스템에 의한 process death | 종료(정리 콜백 보장 없음) | 시스템이 기록만 유지, 복귀 시 재구성 | 파괴, 복귀 시 새 인스턴스 | ViewModel 소실, 저장해 둔 값만 복원 | 유지 |
| force-stop | 종료 | 제거 | 모두 파괴 | 모두 소실 | 유지(3 장 참고) |
| uninstall | 종료 | 제거 | 모두 파괴, registry 에서도 제거 | 모두 소실 | 삭제(3 장 참고) |

### 실패 사례로 두 사건을 구분한다

**사례 A.** 화면을 회전했더니 입력 중이던 텍스트가 사라진다. 원인은 그 값이 Composable 의 일반 지역 상태나 Activity 필드에만 있었기 때문이다. `rememberSaveable` 이나 `ViewModel` 로 옮기면 configuration change 를 견딘다.

**사례 B.** 몇 시간 동안 다른 앱을 쓰다가 돌아오니 화면은 그대로인데 스크롤 위치나 선택했던 항목이 초기화돼 있다. 이 경우는 configuration change 가 아니라 process death 일 가능성이 크다. `ViewModel` 에만 값을 뒀다면 이 경로에서는 복원되지 않는다. `SavedStateHandle` 에 최소한의 식별자(선택된 ID, 스크롤 인덱스 등)를 저장해 두고, 복귀 시 그 식별자로 데이터를 다시 조회해야 한다.

두 사례는 증상이 비슷해 보이지만 원인이 되는 사건이 다르고, 따라서 필요한 저장 계층도 다르다.

### 조사 방법: 어떤 사건이었는지 구분한다

1. **재현 가능한 개발자 옵션을 구분해 쓴다.** "활동 유지 안함(Don't keep activities)"은 화면을 떠나는 즉시 Activity 를 파괴해 configuration-change 에 가까운 재생성을 재현하지만 프로세스 자체를 반드시 종료하지는 않는다. 실제 process death 를 재현하려면 Android Studio 의 프로세스 종료 기능이나 `adb shell am kill <package>` 계열 도구로 프로세스 자체를 없애야 한다.
2. **Logcat 에서 프로세스 생성/종료 로그를 확인한다.** 새 프로세스가 만들어졌다면 이전 인스턴스가 이어진 것이 아니라 처음부터 다시 만들어졌다는 뜻이다.
3. **어떤 값이 비었는지 본다.** `ViewModel` 에 있던 값까지 비었다면 process death, `rememberSaveable` 로 감싸지 않은 화면 지역 값만 비었다면 configuration change 쪽을 먼저 의심한다.
4. **task 가 유지됐는지 본다.** `dumpsys activity activities` 로 task 와 back stack 구성을 확인해, 문제가 개별 화면 재생성인지 task 자체가 없어진 것인지 구분한다.

### 반드시 교정해야 할 오해

| 오해 | 교정 |
| --- | --- |
| 화면이 다시 보이면 이전 프로세스가 계속 실행되고 있던 것이다. | process death 이후의 복귀는 새 프로세스와 새 인스턴스에 저장된 값만 복원한 결과일 수 있다. |
| ViewModel 에 담아 두면 어떤 경우에도 상태가 보존된다. | ViewModel 은 configuration change 는 견디지만 process death 는 견디지 못한다. |
| onDestroy 에서 정리나 저장을 하면 항상 안전하다. | 시스템이 프로세스를 회수할 때는 onDestroy 호출 자체가 보장되지 않는다. |
| 최근 앱 목록에서 task 를 지우는 것은 뒤로 가기를 여러 번 하는 것과 같다. | task 제거는 그 task 전체와 연관 컴포넌트의 생존을 한 번에 재판단하게 만드는 별도의 사건이다. |
| force-stop 은 process death 의 한 종류일 뿐 특별할 것이 없다. | force-stop 은 시스템이 조용히 회수하는 process death 보다 더 명시적이고 강한 개입이며, 3 장이 다룬 UID/데이터 연속성과는 별도로 이 장에서는 lifetime 초기화 범위가 더 넓다는 점이 다르다. |
| 상태 저장 문제는 항상 한 가지 저장소만 있으면 해결된다. | 화면 재생성, 프로세스 종료, 영속 데이터는 서로 다른 저장 계층(ViewModel, saved state, repository/storage)이 필요하다. |

### 확인 질문

1. 설치된 패키지 identity, 프로세스, task, 컴포넌트 인스턴스, ViewModel, transient state 는 각각 누가 관리하는가?
2. configuration change 에서 프로세스와 ViewModel 이 유지되는 이유는 무엇인가?
3. "onDestroy 호출이 보장되지 않는다"는 서술은 어떤 실무 규칙으로 이어지는가?
4. 뒤로 가기로 인한 화면 finish 와 task 전체 제거는 영향 범위가 어떻게 다른가?
5. process death 이후 복귀했을 때 무엇이 복원되고 무엇이 복원되지 않는가?
6. force-stop 과 uninstall 은 process death 와 비교해 어떤 lifetime 까지 추가로 정리하는가?
7. 화면 회전 직후 입력값이 사라지는 문제와 오랜 백그라운드 이후 선택 상태가 사라지는 문제는 왜 서로 다른 원인으로 조사해야 하는가?
8. "활동 유지 안함" 옵션과 실제 프로세스 종료 도구는 어떤 차이를 재현하는가?

### 다음 장으로 이어지는 질문

이 장은 화면, 프로세스, task 와 사용자 상태가 서로 다른 사건에 따라 독립적으로 소멸한다는 것을 다뤘다. 그러나 이 lifetime 들이 살아 있는 동안 코드가 실제로 어느 스레드에서, 어떤 실행 보장을 받으며 실행되는지는 아직 다루지 않았다.

다음 장에서는 main thread, Binder, coroutine 과 background 작업이 각각 실행 순서, 가시성, 지속성 중 무엇을 책임지는지를 다룬다.

- 같은 프로세스 안에서 코드는 왜 항상 같은 스레드에서 실행되지 않는가?
- coroutine 의 취소 가능한 작업 lifetime 은 이 장의 component/process lifetime 과 어떻게 다른가?
- foreground service 와 durable scheduler(WorkManager 등)는 이 장의 어떤 lifetime 문제를 해결하기 위한 것인가?

### 관련 정본

- [설정 변경은 Activity를 재생성할 수 있으므로 상태를 화면 인스턴스에서 분리해야 한다](../../02_app_framework/architecture/app-components/app-component-contracts/configuration-change-recreates-activity-but-not-all-screen-state.md)
- [프로세스 종료 복구에는 saved state와 영속 source of truth가 필요하다](../../02_app_framework/architecture/app-components/app-component-contracts/process-death-recovery-needs-saved-state-and-persistent-source-of-truth.md)
- [Activity 콜백은 화면 인스턴스의 visibility와 interaction 경계를 알린다](../../02_app_framework/architecture/app-components/app-component-contracts/activity-lifecycle-callbacks-describe-visibility-and-interaction-boundaries.md)
- [Task와 back stack은 OS가 관리하는 Activity 작업 기록이지 앱 내부 navigation state가 아니다](../../02_app_framework/architecture/app-components/app-component-contracts/task-and-back-stack-are-os-activity-navigation-not-app-navigation-state.md)
- [ViewModel은 설정 변경 동안 유지되지만 프로세스 사망 복원은 보장하지 않는다](../../02_app_framework/architecture/state-management/viewmodel/viewmodel-survives-configuration-change-not-process-death.md)
- [SavedStateHandle은 프로세스 사망 후 복원해야 하는 작은 상태에 사용한다](../../02_app_framework/architecture/state-management/viewmodel/savedstatehandle-restores-small-process-death-state.md)
- [Context-registered Receiver의 수명은 등록한 Context를 따른다](../../02_app_framework/architecture/app-components/app-component-contracts/context-registered-receiver-lifetime-follows-registering-context.md)
- [AMS는 앱 프로세스와 컴포넌트 lifecycle을 조율한다](../../01_system_internals/boot-and-runtime/system-server-contracts/ams-coordinates-app-process-and-component-lifecycle.md)
- [프로세스 우선순위는 메모리 회수 정책 입력이지 앱 상태의 진실이 아니다](../../01_system_internals/boot-and-runtime/system-server-contracts/process-priority-is-memory-reclaim-policy-input-not-app-state-truth.md)

### 공식 근거

- [Activity state changes](https://developer.android.com/guide/components/activities/state-changes)
- [Activity lifecycle](https://developer.android.com/guide/components/activities/activity-lifecycle)
- [Processes and app lifecycle](https://developer.android.com/guide/components/activities/process-lifecycle)
- [Tasks and back stack](https://developer.android.com/guide/components/activities/tasks-and-back-stack)
- [Services overview](https://developer.android.com/guide/components/services)
- [Behavior changes: all apps (Android 15) — package stopped state](https://developer.android.com/about/versions/15/behavior-changes-all)

검증일: 2026-08-03. force-stop 이후 백그라운드 자동 재시작이 억제되는 정확한 조건은 이 장 저작 시점에 공식 문서 원문 인용으로 재확인하지 못했다(수동 확인 필요). 나머지 인용은 WebFetch 로 원문을 대조했다.

추가 검증일: 2026-08-05. 위에서 수동 확인이 필요하다고 남겨뒀던 force-stop 이후 자동 재시작 억제 조건을 WebSearch/WebFetch 로 재시도해 공식 문서(Android 15 all-apps behavior changes)에서 확인했다 — stopped 상태는 오직 사용자의 직접/간접 실행으로만 해제되고, 브로드캐스트/pending intent 로는 해제되지 않는다는 원문을 인용해 본문을 갱신했다. 더 이상 수동 확인 필요 항목이 아니다.
