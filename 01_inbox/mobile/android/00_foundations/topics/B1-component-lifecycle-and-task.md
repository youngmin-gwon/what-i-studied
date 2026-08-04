---
title: B1-component-lifecycle-and-task
tags: [android, architecture, lifecycle, task, topic-synthesis]
aliases: [Component Lifecycle Topic, 컴포넌트 생명주기와 Task 합성]
date modified: 2026-08-04 16:30:00 +09:00
date created: 2026-08-04 16:00:00 +09:00
---

## B1 · 컴포넌트 생명주기와 Task / Back Stack

> **이 문서의 목적**: Android 애플리케이션의 뼈대가 되는 컴포넌트 생명주기와 상태 보존 메커니즘, 화면 스택 관리 원칙을 하나의 흐름으로 정리한다. 화면이 어떻게 생성되고 살아남으며 파괴되는지를 이해하는 단일 진입점이다.

---

### 1. Activity/Fragment 생명주기 전체 조망

Android 의 UI 컴포넌트는 시스템에 의해 생성되고 파괴된다. 각 생명주기 콜백은 화면이 사용자에게 보이는지, 포커스를 가지는지, 백그라운드로 이동했는지를 나타낸다. UI 리소스 할당과 해제는 이 생명주기 상태에 맞춰 정확하게 대칭을 이루어야 메모리 누수를 막을 수 있다.

| 원자 노트 | 핵심 명제 |
|---|---|
| [Activity 생명주기 모델은 리소스 소유권과 화면 가시성을 조율한다](../../02_app_framework/architecture/lifecycle/activity-lifecycle-model.md) | onCreate-onDestroy, onStart-onStop, onResume-onPause 대칭 원칙 |
| [Fragment는 Activity 생명주기에 종속되며 뷰 생명주기를 분리한다](../../02_app_framework/architecture/lifecycle/fragment-lifecycle-is-tied-to-activity.md) | Fragment 수명과 뷰(View) 수명의 불일치 관리 |

---

### 2. ViewModel: 설정 변경을 넘어 살아남는 상태 홀더

ViewModel 은 화면 단위 상태와 외부 작업의 조율자다. 화면 회전이나 창 크기 변경처럼 화면이 재생성되는 설정 변경 시에도 `ViewModelStore` 에 남아 상태를 유지한다. 단, 프로세스 사망 시에는 함께 소멸되므로 영속적인 저장 장치로 사용해서는 안 된다.

| 원자 노트 | 핵심 명제 |
|---|---|
| [ViewModel은 설정 변경 동안 유지되지만 프로세스 사망 복원은 보장하지 않는다](../../02_app_framework/architecture/state-management/viewmodel/viewmodel-survives-configuration-change-not-process-death.md) | 설정 변경과 프로세스 사망의 차이 |
| [ViewModel은 화면 단위 상태와 외부 작업을 조율한다](../../02_app_framework/architecture/state-management/viewmodel/viewmodel-orchestrates-screen-state-and-external-work.md) | ViewModel 의 책임 경계와 상태 변환 역할 |
| [ViewModel은 UI 컨트롤러와 Android Context를 장기 보관하지 않는다](../../02_app_framework/architecture/state-management/viewmodel/viewmodel-does-not-retain-ui-controller-or-context.md) | 메모리 누수를 막기 위한 참조 제한 |

---

### 3. Task와 Back Stack 관리

Task 는 사용자가 특정 목표를 수행하기 위해 상호작용하는 Activity 의 집합이다. Back Stack 은 이 Activity 들이 열린 순서대로 쌓이는 구조를 말한다. Launch Mode (`standard`, `singleTop`, `singleTask`, `singleInstance`)와 Intent Flag 를 통해 이 스택에 새로운 화면이 어떻게 추가되거나 재활용될지 결정한다.

| 원자 노트 | 핵심 명제 |
|---|---|
| [Launch Mode는 Task 스택 내 Activity 인스턴스 재사용을 결정한다](../../02_app_framework/architecture/task-and-stack/launch-mode-determines-activity-instance-reuse.md) | 4가지 기본 Launch Mode 동작 방식 |
| [Intent Flag는 런타임에 Back Stack 조작을 동적으로 제어한다](../../02_app_framework/architecture/task-and-stack/intent-flags-dynamically-control-back-stack.md) | CLEAR_TOP 과 NEW_TASK 의 조합 |

---

### 4. 프로세스 죽음(Process Death)과 상태 복원

Android 시스템은 메모리가 부족할 때 백그라운드에 있는 앱 프로세스를 강제로 종료할 수 있다. 사용자가 다시 앱으로 돌아왔을 때 이전 상태를 매끄럽게 복원하려면 `onSaveInstanceState` 나 `SavedStateHandle` 을 사용해야 한다. 이때 저장하는 데이터는 복원에 필요한 최소한의 식별자나 작은 데이터여야 한다.

| 원자 노트 | 핵심 명제 |
|---|---|
| [SavedStateHandle은 프로세스 사망 후 복원해야 하는 작은 상태에 사용한다](../../02_app_framework/architecture/state-management/viewmodel/savedstatehandle-restores-small-process-death-state.md) | 뷰모델 내에서의 상태 복원 전략 |
| [대용량 데이터는 로컬 저장소에 두고 식별자만 Bundle에 저장한다](../../02_app_framework/architecture/state-management/large-data-goes-to-local-storage-and-ids-to-bundle.md) | Bundle 크기 제한과 TransactionTooLargeException 방지 |

---

### 5. 단방향 데이터 흐름 (UDF) 패턴

단방향 데이터 흐름 (Unidirectional Data Flow)은 상태 변경의 진입점과 관찰점을 엄격히 분리하는 패턴이다. UI 는 이벤트를 상위로 전달하고, ViewModel 은 상태를 변경하여 하위로 흘려보낸다. Mutable 상태 홀더는 내부에 숨기고 외부에는 읽기 전용 상태만 노출하여 예측 가능성을 높인다.

| 원자 노트 | 핵심 명제 |
|---|---|
| [Mutable 상태 홀더는 ViewModel 내부에 숨기고 외부에는 읽기 전용 상태만 노출한다](../../02_app_framework/architecture/state-management/viewmodel/viewmodel-exposes-read-only-state.md) | 상태 변경 단일 진입점 확보 |
| [UI 이벤트는 상향 전달되고 상태는 하향 흐른다](../../02_app_framework/architecture/state-management/udf-events-up-state-down.md) | UDF 패턴의 핵심 흐름 모델 |

---

### 6. 관찰 가능한 신호와 디버깅

생명주기와 상태 관리는 비동기적으로 일어나므로 디버깅이 어렵다. LifecycleObserver 와 엄격한 로깅을 통해 상태 전이를 시각화할 수 있다. 특히 코루틴 스코프 취소와 생명주기 이벤트가 맞물리는 지점은 버그가 빈번하게 발생하는 곳이므로 명확한 관찰이 필요하다.

| 원자 노트 | 핵심 명제 |
|---|---|
| [ViewModel은 외부 작업을 viewModelScope의 수명에 묶는다](../../02_app_framework/architecture/state-management/viewmodel/viewmodelscope-binds-external-work-to-viewmodel-lifetime.md) | 비동기 작업 취소와 ViewModel 수명의 일치 |
| [LifecycleObserver는 컴포넌트 생명주기 변화를 외부 컴포넌트에 알린다](../../02_app_framework/architecture/lifecycle/lifecycleobserver-notifies-component-lifecycle-changes.md) | 생명주기 이벤트 기반 리소스 관리 |

---

### 이 주제와 연결된 Worked Example

| Worked Example | 연결 포인트 |
|---|---|
| [WE 01 · App Icon Tap to First Frame](../worked-examples/01-app-icon-tap-to-first-frame.md) | 앱 프로세스 시작과 Activity 인스턴스 생성 과정 |
| [WE 03 · Deep Link Navigation Resolving](../worked-examples/03-deep-link-navigation-resolving.md) | Task 생성과 Back Stack 재구성 원리 |
| [WE 05 · Process Death Recovery Simulation](../worked-examples/05-process-death-recovery-simulation.md) | 앱이 강제 종료된 후 복원되는 과정의 State 관찰 |

---

### 이 주제와 연결된 Diagnostic Runbook

| Runbook | 연결 포인트 |
|---|---|
| [RB 01 · App Launch Performance](../diagnostic-runbooks/01-app-launch-performance.md) | 콜백 지연과 메인 스레드 블로킹 진단 |
| [RB 03 · State Loss & Process Death](../diagnostic-runbooks/03-state-loss-and-process-death.md) | 복원 실패와 TransactionTooLargeException 트러블슈팅 |

---

### 더 깊이 들어갈 때 (Learning Spine)

- **Chapter 05 · Architecture** — 단방향 데이터 흐름과 앱 아키텍처 가이드라인 전체
- **Chapter 03 · Data Layer** — ViewModel 에서 데이터를 제공받기 위한 Repository 설계
- **Chapter 02 · Jetpack Compose** — ViewModel 상태와 Compose UI 수명주기의 연결
