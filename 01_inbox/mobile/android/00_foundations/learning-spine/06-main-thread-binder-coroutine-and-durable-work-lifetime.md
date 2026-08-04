---
title: 06-main-thread-binder-coroutine-and-durable-work-lifetime
tags: ["android", "android/foundations", "learning-spine"]
aliases: ["Main thread, Binder, coroutine, and durable work lifetime"]
date modified: 2026-08-04 10:10:41 +09:00
date created: 2026-08-03 21:20:00 +09:00
---

## 메인 스레드, Binder, coroutine 과 durable scheduler 는 서로 다른 실행 책임을 진다

5 장은 화면, 컴포넌트, 프로세스, task 가 서로 다른 사건에 따라 독립적으로 소멸한다는 것을 다뤘다. 하지만 그 lifetime 들이 살아 있는 동안에도 코드가 항상 같은 조건으로 실행되는 것은 아니다. 코드는 어떤 스레드에서, 어떤 프로세스 경계를 넘어, 누가 소유한 lifetime 안에서 실행되는지에 따라 완전히 다른 계약을 따른다.

이 장의 핵심 질문은 다음과 같다.

>코드는 어느 스레드에서 실행되고, 어떤 프로세스 경계를 넘으며, 누가 소유한 lifetime 안에서 취소되거나 지속되는가?

이 장은 coroutine 문법이나 WorkManager API 사용법을 처음부터 가르치지 않는다. 개별 API 의 상세 사용법은 각 원자 노트가 다루는 수준으로 남겨두고, 여기서는 main thread, Binder, coroutine, durable scheduler 가 각각 실행 순서·프로세스 경계·취소 가능한 lifetime·지속성 중 무엇을 책임지는지 하나의 모델로 비교한다.

### 1. 같은 프로세스 안에서도 실행은 하나의 스레드로 직렬화된다

앱이 시작되면 시스템은 main thread(UI thread)를 만든다. 공식 문서는 이 스레드의 역할을 이렇게 설명한다.

>"This thread is very important, because it is in charge of dispatching events to the appropriate user interface widgets, including drawing events."
>
>"All components that run in the same process are instantiated in the UI thread, and system calls to each component are dispatched from that thread."

즉 같은 프로세스 안의 컴포넌트 호출은 기본적으로 이 하나의 스레드에서 순서대로 처리된다. 터치 입력을 위젯에 전달하는 일도, 화면을 다시 그리라는 요청을 처리하는 일도 이 스레드의 이벤트 큐를 거친다. Looper 가 스레드의 `MessageQueue` 를 돌리고 Handler 가 그 큐에 작업을 넣는다는 것은, 결국 이 순서를 만드는 하위 메커니즘을 가리키는 말이다.

문제는 이 큐가 하나뿐이라는 데 있다. 공식 문서는 그 결과를 이렇게 경고한다.

>"Performing long operations in the UI thread, such as network access or database queries, blocks the whole UI. When the thread is blocked, no events can be dispatched, including drawing events."
>
>"Even worse, if the UI thread is blocked for more than a few seconds, the user is presented with the 'application not responding' (ANR) dialog."

ANR 은 느린 메서드 하나의 문제가 아니라, 입력·화면 갱신·시스템 콜백이 지나가야 하는 유일한 통로가 막혔다는 응답성 계약 위반이다. 그래서 ANR 분석은 "어떤 코드가 오래 걸렸는가"만이 아니라 "그 코드가 왜 이 유일한 큐를 점유했는가"를 함께 봐야 한다.

### 2. 프로세스 경계를 넘는 호출은 다른 스레드 계층으로 넘어간다

같은 프로세스 안의 호출과 다른 프로세스로 넘어가는 호출은 실행되는 스레드 자체가 다르다. 공식 문서는 이 차이를 정확히 구분한다.

>"When a call on a method implemented in an IBinder originates in the same process in which the IBinder is running, the method is executed in the caller's thread. However, when the call originates in another process, the method executes in a thread chosen from a pool of threads that the system maintains in the same process as the IBinder."

즉 시스템 서비스 호출이 실제로 Binder 를 거쳐야 한다면, 그 코드는 caller 의 스레드가 아니라 대상 프로세스의 Binder thread pool 에서 실행된다. 이 경로에는 요청을 보내고(call), 데이터를 커널을 거쳐 복사하고(copy), target Binder thread 가 처리하고(dispatch), 결과를 돌려받는(reply) 네 단계의 비용이 함께 따라온다. 그래서 Binder 호출은 로컬 함수 호출과 같은 비용 모델로 취급하면 안 된다.

이 thread pool 은 동시성을 제공하지만 무한하지 않다. 오래 걸리는 처리가 쌓이거나, 서비스 A 가 서비스 B 를 동기 호출하고 B 가 다시 A 를 호출하는 구조라면, thread pool 고갈이나 상호 대기로 이어질 수 있다. main thread 에서 느린 동기 Binder 호출을 직접 기다리면, 1 절의 "유일한 큐"가 이번에는 원격 프로세스의 처리 시간과 thread pool 상태에까지 종속된다.

### 3. Coroutine 은 실행 위치와 작업 수명을 분리해서 다룬다

Coroutine 자체는 스레드가 아니다. 어떤 스레드에서 실행될지는 `Dispatcher` 가 고르고, 그 작업이 언제까지 살아 있어야 하는지는 `CoroutineScope` 가 정한다. 이 둘을 같은 문제로 섞으면 안 된다.

이 구분은 5 장이 다룬 lifetime 모델과 바로 연결된다. 공식 문서는 `ViewModel` 에서 coroutine 을 시작해야 하는 이유를 이렇게 설명한다.

>"Views shouldn't directly trigger any coroutines to perform business logic. Instead, defer that responsibility to the ViewModel."
>
>"In addition to that, your coroutines will survive configuration changes automatically if the work is started in the viewModelScope. If you create coroutines using lifecycleScope instead, you'd have to handle that manually."

`viewModelScope` 에서 시작한 작업이 configuration change 를 자동으로 견디는 이유는 5 장에서 본 것과 같다. `ViewModel` 은 Activity 인스턴스가 아니라 그 소유자의 `ViewModelStore` 에 남아 있기 때문이다. 하지만 5 장이 이미 말했듯, 이 생존은 프로세스 종료까지 견디는 것은 아니다. `viewModelScope` 가 취소되지 않았다고 해서 그 작업이 durable 하다는 뜻은 아니다.

공식 문서는 `GlobalScope` 처럼 소유자가 불명확한 scope 를 피하라고도 명시한다.

>"By using GlobalScope, you're hardcoding the CoroutineScope that a class uses… Makes testing very hard as your code is executed in an uncontrolled scope, you won't be able to control its execution."

즉 coroutine 을 만들 때 먼저 물어야 할 질문은 "어느 스레드에서 실행할까"가 아니라 "이 작업은 누구의 lifetime 에 묶이고, 그 소유자가 사라지면 정말 취소돼도 되는가"다.

### 4. 화면 수명보다 오래 살아야 하는 작업은 다른 소유자가 필요하다

`viewModelScope` 나 `lifecycleScope` 에 묶인 작업은 화면(또는 그 소유자)이 사라지면 함께 취소된다. 이것은 결함이 아니라 의도된 계약이다. 문제는 화면이 사라져도, 심지어 프로세스가 재시작돼도 반드시 이어져야 하는 작업을 같은 방식으로 다루면 안 된다는 데 있다.

사용자가 지금 인지해야 하는 진행 중 작업(음악 재생, 활성 내비게이션, 진행 중인 전송)은 foreground service 의 영역이다. Foreground service 는 실행 스레드나 취소 정책이 아니라 "사용자에게 보이는 즉시성 있는 작업"이라는 가시성 계약을 시스템에 알리는 것이다.

지연 가능하지만 반드시 완료돼야 하는 작업(동기화, 업로드)은 WorkManager 의 영역이다. WorkManager 는 요청을 메모리가 아니라 내부 DB 에 `WorkSpec` 으로 저장하고 플랫폼 스케줄러에 위임하기 때문에, 화면이 사라지거나 프로세스가 재시작돼도 예약이 남아 있다. 이 지속성은 5 장의 "process death 가 ViewModel 과 in-memory 상태를 지운다"는 사실과 정확히 대비된다. WorkManager 가 살아남는 이유는 특별한 마법이 아니라 애초에 그 정보를 프로세스의 메모리가 아니라 영속 저장소에 두기 때문이다. 다만 이 지속성이 "정확한 시각에 실행"이나 "강제 종료 뒤에도 실행"까지 보장하지는 않는다.

### 5. 네 계층의 책임 비교

| 계층 | 무엇을 결정하는가 | 무엇을 결정하지 않는가 |
| --- | --- | --- |
| Main thread / Looper·Handler | 같은 프로세스 안 이벤트의 실행 **순서**(직렬화) | 그 작업이 얼마나 오래 걸려도 되는지, 프로세스 경계를 넘는 비용 |
| Binder / thread pool | 프로세스 **경계**를 넘는 호출의 실행 스레드와 동시성 한계 | 호출 자체의 취소 정책이나 화면 lifetime 과의 연결 |
| Coroutine(Dispatcher + Scope) | 작업의 실행 위치(Dispatcher)와 취소 가능한 **lifetime**(Scope) | 프로세스가 재시작돼도 이어져야 하는 **지속성** |
| Foreground service / WorkManager | 사용자 가시성 계약과 프로세스 재시작을 넘는 **지속성** | 정확한 실행 시각, 강제 종료 이후의 무조건적 실행 |

이 표는 "어느 API 가 더 좋은가"의 순위가 아니다. 같은 요청이라도 이 네 층 중 어디를 통과하느냐에 따라 순서, 비용, 취소 조건, 지속성이라는 서로 다른 축의 답이 나온다.

### 6. Worked example: 화면의 "동기화" 버튼 하나가 네 계층을 모두 지난다

사용자가 화면의 "지금 동기화" 버튼을 누른다고 하자.

1. 버튼 탭은 main thread 의 이벤트 큐를 거쳐 클릭 리스너에 전달된다.
2. 리스너는 `viewModelScope.launch(Dispatchers.IO) { … }` 로 작업을 시작한다. 실행 위치는 IO Dispatcher 가 고르고, 이 작업의 lifetime 은 화면의 `ViewModel` 이 소유한다.
3. 이 작업 중간에 시스템 서비스를 동기 호출해야 한다면, 그 호출은 caller 의 스레드가 아니라 대상 서비스의 Binder thread pool 에서 처리된다. 이 호출을 실수로 main thread 에서 직접 기다리게 만들면 1 절의 문제로 되돌아간다.
4. 사용자가 동기화가 끝나기 전에 화면을 벗어나면 `viewModelScope` 가 취소되고, 진행 중이던 작업도 함께 취소된다.
5. 만약 이 동기화가 화면을 벗어나도 반드시 끝까지 이어져야 하는 요구라면, 애초에 3~4 단계를 화면 lifetime 에 묶어서는 안 된다. 그 요청은 WorkManager 에 위임해 화면과 무관하게 지속되도록 설계해야 한다.

같은 버튼 클릭이라도 "화면이 보이는 동안만 유효한 동기화"와 "화면과 무관하게 끝까지 가야 하는 동기화"는 3~5 단계에서 완전히 다른 설계가 필요하다.

### 실패 사례: coroutine 안에서 느린 동기 Binder 호출을 기다린다

`viewModelScope.launch(Dispatchers.Main) { systemService.slowSyncCall() }` 처럼 Main dispatcher 위에서 느린 동기 Binder 호출을 직접 기다리면, coroutine 을 썼다는 사실과 무관하게 main thread 의 이벤트 큐는 그 호출이 끝날 때까지 막힌다. 이 호출이 대상 서비스의 thread pool 대기나 다른 서비스와의 상호 호출로 지연되면, 겉보기에는 "coroutine 하나가 느리다"지만 실제로는 1 절의 responsiveness 계약과 2 절의 Binder thread pool 경계가 함께 걸린 문제다. 해법은 dispatcher 를 IO/Default 로 옮기는 것만이 아니라, 애초에 그 호출이 동기여야 하는지, 어느 thread pool 에서 무엇을 기다리는지부터 분리해서 보는 것이다.

### 조사 방법: 어느 계층에서 지연이 생겼는지 분류한다

1. **main thread 가 CPU 를 쓰고 있었는가, 무언가를 기다리고 있었는가?** trace 에서 이 둘을 구분한다. 기다리고 있었다면 lock 인지 Binder 응답인지 본다.
2. **Binder 호출이라면 caller 대기 시간과 callee 처리 시간을 분리한다.** callee 가 다른 서비스를 다시 호출하는 재진입 구조인지도 확인한다.
3. **coroutine 의 취소와 예외가 삼켜지지 않았는지 확인한다.** `CancellationException` 을 일반 오류로 처리하면 취소된 작업이 계속 실행된 것처럼 오해할 수 있다.
4. **작업이 durable 해야 하는데 화면 scope 에 묶여 있지 않은지 확인한다.** `WorkInfo.state` 나 `dumpsys jobscheduler` 로 예약이 실제로 시스템에 등록됐는지 본다.

### 반드시 교정해야 할 오해

| 오해 | 교정 |
| --- | --- |
| coroutine 을 쓰면 어떤 작업도 main thread 를 막지 않는다. | Dispatcher 를 Main 으로 두거나 그 안에서 동기 Binder 호출을 직접 기다리면 여전히 큐가 막힌다. |
| Binder 호출은 로컬 함수 호출과 비용이 같다. | 같은 프로세스 호출은 caller 스레드에서, 다른 프로세스 호출은 대상 프로세스의 thread pool 에서 실행되며 call/copy/dispatch/reply 비용이 따른다. |
| viewModelScope 에서 시작한 작업은 화면을 벗어나도 안전하게 이어진다. | viewModelScope 는 화면 소유자가 사라지면 취소되도록 설계된 것이며, 지속이 필요한 작업의 요구와는 반대다. |
| WorkManager 로 옮기면 정확한 시각에 실행되거나 강제 종료 후에도 실행된다는 뜻이다. | WorkManager 는 예약을 지속시키는 것이지 정확한 시각이나 무조건적 실행을 보장하지 않는다. |
| ANR 은 특정 timeout 초를 넘긴 메서드 하나의 문제다. | ANR 은 입력·화면 갱신이 지나가야 하는 유일한 큐가 막혔다는 응답성 계약 위반이며, 원인은 lock, Binder 대기, CPU 점유 등 다양하다. |
| GlobalScope 는 그냥 조금 더 넓은 범위의 viewModelScope 다. | GlobalScope 는 명시적 소유자가 없는 lifetime 밖의 실행이며 취소·테스트 책임을 흐리게 만든다. |

### 확인 질문

1. 같은 프로세스 안의 컴포넌트 호출이 하나의 스레드로 직렬화된다는 것은 어떤 실무 규칙으로 이어지는가?
2. 같은 프로세스 호출과 다른 프로세스 호출은 어느 스레드에서 실행되는지가 왜 다른가?
3. Dispatcher 와 CoroutineScope 는 각각 무엇을 결정하는가?
4. viewModelScope 가 configuration change 는 견디지만 지속성 요구에는 맞지 않는 이유는 무엇인가?
5. Foreground service 와 WorkManager 는 각각 어떤 요구(가시성, 지속성)에 대응하는가?
6. WorkManager 의 지속성은 어디에서 오며, 무엇까지는 보장하지 않는가?
7. coroutine 안에서 느린 동기 Binder 호출을 main dispatcher 로 기다리면 왜 문제가 되는가?
8. ANR 을 "특정 timeout 숫자"가 아니라 "응답성 계약 위반"으로 봐야 하는 이유는 무엇인가?

### 다음 장으로 이어지는 질문

이 장은 코드가 어느 스레드에서, 어떤 프로세스 경계를 넘어, 누가 소유한 lifetime 안에서 실행되는지를 다뤘다. 그러나 그 실행 결과가 실제로 사용자 입력에 응답하고 화면의 픽셀로 이어지는 경로는 아직 다루지 않았다.

다음 장에서는 입력과 configuration 이 어떻게 UI 상태로, 그리고 그 상태가 어떻게 실제 화면 프레임으로 이어지는지를 다룬다.

- 사용자의 입력은 main thread 의 이벤트 큐에 도달하기 전 어떤 경로를 거치는가?
- configuration change 는 왜 단순한 값 변경이 아니라 5 장이 다룬 Activity 재생성으로 이어지는가?
- 계산된 UI 상태는 어떤 과정을 거쳐 실제 화면에 그려지는 프레임이 되는가?

### 관련 정본

- [Looper와 Handler는 스레드의 메시지 큐를 관리하고 이벤트를 순차적으로 처리한다](../glossary/android-glossary/15-looper-handler.md)
- [ANR은 단일 timeout이 아니라 responsiveness 계약 위반이다](../../01_system_internals/boot-and-runtime/system-server-contracts/anr-is-responsiveness-contract-violation-not-single-timeout.md)
- [메인 스레드 작업은 앱 응답성을 결정한다](../../06_testing_performance/performance/performance-contracts/main-thread-work-controls-responsiveness.md)
- [IPC and process contracts](../../01_system_internals/ipc-and-process/ipc-process-contracts/ipc-process-contracts.md)
- [Binder transaction lifetime은 call, copy, dispatch, reply로 나뉜다](../../01_system_internals/ipc-and-process/ipc-process-contracts/binder-transaction-lifetime-is-call-copy-dispatch-and-reply.md)
- [Binder thread pool은 service concurrency와 deadlock 경계다](../../01_system_internals/ipc-and-process/ipc-process-contracts/binder-thread-pool-is-service-concurrency-and-deadlock-boundary.md)
- [Coroutine은 thread가 아니라 취소 가능한 경량 작업이다](../../02_app_framework/data/async-flow/coroutines/coroutine-is-lightweight-cancellable-work-not-thread.md)
- [Dispatcher는 실행 위치를 고르고 Scope는 작업 수명을 소유한다](../../02_app_framework/data/async-flow/coroutines/dispatcher-selects-execution-context-not-work-lifetime.md)
- [Structured concurrency는 부모 scope가 자식 작업의 수명을 소유하게 한다](../../02_app_framework/data/async-flow/coroutines/structured-concurrency-parent-owns-child-lifetime.md)
- [ViewModel은 외부 작업을 viewModelScope의 수명에 묶는다](../../02_app_framework/architecture/state-management/viewmodel/viewmodelscope-binds-external-work-to-viewmodel-lifetime.md)
- [Foreground Service는 사용자에게 보이는 진행 중 작업 계약이다](../../02_app_framework/architecture/app-components/app-component-contracts/foreground-service-is-user-visible-ongoing-work-contract.md)
- [Service는 UI 없는 컴포넌트이지 일반 background task runner가 아니다](../../02_app_framework/architecture/app-components/app-component-contracts/service-is-background-or-remote-work-entry-point-not-general-task-runner.md)
- [WorkManager는 지연 가능한 보장 작업의 기본 선택이다](../../04_system_services/background-and-notifications/background-work-contracts/workmanager-is-default-for-deferrable-guaranteed-work.md)
- [백그라운드 제한은 작업 상태를 영속적으로 설계하게 만든다](../../04_system_services/background-and-notifications/background-work-contracts/background-restrictions-require-persistent-work-state.md)

### 공식 근거

- [Processes and threads](https://developer.android.com/guide/components/processes-and-threads)
- [ANRs](https://developer.android.com/topic/performance/vitals/anr)
- [Coroutines best practices on Android](https://developer.android.com/kotlin/coroutines/coroutines-best-practices)
- [Task scheduling with WorkManager](https://developer.android.com/develop/background-work/background-tasks/persistent)
- [Foreground services](https://developer.android.com/develop/background-work/services/fgs)

검증일: 2026-08-03. Binder thread pool 크기, ANR timeout 세부 값, WorkManager 의 expedited/long-running quota 는 Android 버전과 target SDK 에 따라 달라지므로 실제 적용 시점에 다시 확인한다.
