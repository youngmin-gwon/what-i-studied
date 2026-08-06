---
title: android-app-framework-map
tags: ["android", "android/app-framework"]
aliases: ["Android App Framework Map 은 앱 코드가 소유하는 7개 하위 클러스터를 계층별로 연결하는 통합 지도다"]
date modified: 2026-08-06 15:00:00 +09:00
date created: 2026-08-04 18:00:00 +09:00
---

## Android App Framework Map 은 앱 코드가 소유하는 7개 하위 클러스터를 계층별로 연결하는 통합 지도다

`02_app_framework` 는 `01_system_internals` 가 제공하는 실행 계층 위에서 앱 개발자가 실제로 작성하는 코드를 다룬다. entry point 를 어떻게 선언하는지(architecture), 여러 플랫폼과 공유할 경계를 어디에 둘지(multiplatform), 상태와 UI 를 어떻게 그리는지(jetpack-compose, ui), 화면 사이를 어떻게 이동하는지(navigation), 데이터를 어떻게 저장·전송하는지(data), 객체를 어떻게 조립하는지(dependency-injection), 홈 화면 표면을 어떻게 그리는지(app-widgets)를 구분한다.

### 하위 클러스터와 hub 경로

| 클러스터 | hub 노트 | 다루는 범위 |
|---|---|---|
| [architecture](architecture/android-app-architecture.md) | `architecture/android-app-architecture.md` | Activity/Service/BroadcastReceiver/ContentProvider 같은 OS entry point, Context 경계, ViewModel/state 관리 |
| [multiplatform](architecture/multiplatform-contracts/multiplatform-contracts.md) | `architecture/multiplatform-contracts/multiplatform-contracts.md` | Kotlin Multiplatform의 공유 source set과 플랫폼별 구현 경계, `expect`/`actual` 선택 |
| [dependency-injection](dependency-injection/android-dependency-injection-map.md) | `dependency-injection/android-dependency-injection-map.md` | 객체 graph, binding, scope lifetime, Hilt/Metro, test override |
| [data](data/android-data-layer-map.md) | `data/android-data-layer-map.md` | Flow/StateFlow 상태 조합, Room/DataStore 영속 저장소, 파일 접근, Paging |
| [data/networking](./data/networking/networking-contracts/networking-contracts.md) | `data/networking/networking-contracts/networking-contracts.md` | Retrofit/OkHttp 네트워크 클라이언트 계층, interceptor, suspend 통합, timeout/retry 정책 |
| Jetpack Compose | [runtime](jetpack-compose/runtime/compose-runtime-and-state-model.md), [design system](jetpack-compose/design-system-and-architecture/compose-design-system.md), [layout/UI](jetpack-compose/layout-and-ui/compose-layout-animation-accessibility.md), [performance](jetpack-compose/performance/compose-performance-contracts/compose-performance-contracts.md), [state/effect](jetpack-compose/state-and-lifecycle/compose-state-and-effect-contracts/compose-state-and-effect-contracts.md) | Composable 함수 모델, recomposition, layout/modifier/animation/accessibility, 상태-effect API 선택, 성능 예산 |
| [ui](ui/system/android-ui-system.md) | `ui/system/android-ui-system.md` | View System 과 Compose 의 공존, edge-to-edge/adaptive layout, RecyclerView-LazyColumn 경계 |
| [navigation](navigation/navigation-contracts/navigation-contracts.md) | `navigation/navigation-contracts/navigation-contracts.md` | Manifest/Intent 로 OS 가 컴포넌트를 찾는 계약, deep link 검증, Navigation 3 back stack, adaptive navigation |
| [app-widgets](./app-widgets/app-widget-contracts/app-widget-contracts.md) | `app-widgets/app-widget-contracts/app-widget-contracts.md` | `AppWidgetProvider` lifecycle, `RemoteViews` 제약, 위젯 설정 Activity, `updatePeriodMillis` best-effort 스케줄 |

### 읽는 순서

1. **architecture** 로 시작한다. Activity/Service 같은 OS entry point 와 Context/ViewModel lifetime 을 먼저 나누지 않으면 이후 UI/데이터 클러스터의 "누가 이 객체를 소유하는가"를 판단할 수 없다.
2. **dependency-injection** 으로 이동한다. architecture 가 나눈 lifetime 을 실제 객체 조립에 어떻게 반영하는지를 본다.
3. **data** 와 **data/networking** 을 읽는다. 화면에 그리기 전에 데이터가 어디서 오고(네트워크) 어디에 남는지(저장소)를 먼저 이해해야 UI state 흐름을 추적할 수 있다.
4. **jetpack-compose** 로 넘어간다. runtime → design-system → layout-and-ui → state-and-lifecycle → performance 순으로 5개 하위 영역을 읽는다. state 를 읽고 UI 를 그리는 함수 호출 모델이 이 클러스터의 핵심이며, 앞서 읽은 data 클러스터의 Flow 가 여기서 UI state 로 이어진다.
5. **ui** 를 읽는다. Compose 와 View System 이 같은 프로젝트에 공존할 때의 경계를 확인한다.
6. **navigation** 을 읽는다. Manifest/Intent 로 OS 가 컴포넌트를 찾는 계약, deep link 가 외부 URI 를 내부 목적지로 바꾸는 계약, Navigation 3 의 back stack 을 순서대로 본다.
7. **app-widgets** 는 마지막에 읽는다. Activity/Compose 화면과 달리 별도 프로세스 없이 broadcast 로만 갱신되는 예외적인 표면이므로, architecture 의 일반 lifecycle 모델을 먼저 이해한 뒤 그 예외를 본다.

### 포함하지 않는 범위

- Binder, Zygote, SurfaceFlinger 같은 시스템 native 구현은 다루지 않는다. `01_system_internals` 로 간다.
- WorkManager/JobScheduler 같은 background 실행 스케줄링 자체는 다루지 않는다. `04_system_services` 로 간다. 단 app-widgets 클러스터는 `updatePeriodMillis` 가 WorkManager 로 보완되는 접점만 언급한다.
- 테스트 전략과 CI 는 다루지 않는다. `06_testing_performance` 로 간다.
- 서명, 배포, Play Billing 은 다루지 않는다. `03_packaging_deployment` 로 간다.

### 문제 분류

- **화면이 그려지지 않거나 예상과 다른 Activity/Service 가 실행된다**: architecture 로 OS entry point 를, navigation 으로 Intent/Manifest 매칭을 확인한다.
- **객체가 예상과 다른 시점에 생성/해제된다**: dependency-injection 의 scope-lifetime 매칭을 본다.
- **UI 가 예상보다 자주/드물게 다시 그려진다(recomposition)**: jetpack-compose 의 runtime·performance 하위 영역을 본다.
- **네트워크 응답이 화면에 반영되지 않거나 취소되지 않는다**: data/networking 의 suspend-코루틴 취소 연결과 data 클러스터의 Flow 계약을 함께 본다.
- **deep link 가 잘못된 화면이나 빈 back stack 으로 열린다**: navigation 의 deep-link-contracts 를 본다.
- **홈 화면 위젯이 갱신되지 않거나 설정이 저장되지 않는다**: app-widgets 클러스터를 본다.

### 관련 지도

- [Android Foundation Map](../00_foundations/android-foundation-map.md) — 전체 canonical area 로 돌아가는 최상위 지도.
- [Learning Spine 4장](../00_foundations/learning-spine/04-manifest-to-component-execution.md) — manifest 선언에서 component callback까지.
- [Learning Spine 5장](../00_foundations/learning-spine/05-independent-lifetimes-of-screen-process-task-and-state.md) — screen, process, task, state의 독립 수명.
- [Learning Spine 6장](../00_foundations/learning-spine/06-main-thread-binder-coroutine-and-durable-work-lifetime.md) — coroutine과 framework callback의 취소·실패 경계.
- [Learning Spine 7장](../00_foundations/learning-spine/07-input-resource-selection-and-display-frame.md) — UI 입력·resource·frame 경로.
- [Learning Spine 8장](../00_foundations/learning-spine/08-data-storage-network-and-offline-recovery.md) — storage, network, offline recovery 경계.
- [System Internals Map](../01_system_internals/android-system-internals-map.md) — 이 지도가 호출하는 실행 계층과 IPC 경로.
