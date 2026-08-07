---
title: android-atomic-rewrite-plan
tags: []
aliases: []
date modified: 2026-08-01 01:06:54 +09:00
date created: 2026-07-31 16:43:35 +09:00
---

## Android 문서 의미 기반 원자화 계획

이 문서는 `01_inbox/mobile/android` 아래 Android 노트를 단순 분할 상태에서 의미 기반 원자 노트 체계로 재작성하기 위한 실행 계획이다.

### 현재 판단

현재 구조는 링크 무결성과 파일 단위 분해는 되어 있지만, 최종 원자 노트 체계는 아니다.

문제는 다음과 같다.

- 원본 문서명을 폴더로 보존한 구조가 많다.
- 같은 개념이 [viewmodel](../02_app_framework/viewmodel.md), Flow, Compose State 문서에 반복된다.
- Storage, Security, Performance, Navigation 영역에서 개념 노트와 실무 가이드가 섞여 있다.
- 숫자 prefix 파일은 원자 노트라기보다 원본 heading 조각에 가깝다.
- 허브 문서와 원자 노트가 같은 계층에서 혼재한다.

현재 확정된 정리 기준은 다음과 같다.

- 내부 링크는 Markdown link 형식을 사용한다.
- 원자 노트 제목은 명사형이 아니라 하나의 주장 또는 판단 기준으로 쓴다.
- 허브 문서는 설명 본문을 최소화하고 canonical note 목록과 판단 순서만 가진다.
- 비교 문서는 canonical 지식의 원본이 아니라 진입 경로로 둔다.
- 프로젝트 적용 판단은 일반 개념 노트와 분리해 decision note 로 둔다.

### 최종 폴더 전략

Top-level 구조는 유지한다.

```text
00_foundations
01_system_internals
02_app_framework
03_packaging_deployment
04_system_services
05_security_privacy
06_testing_performance
07_platforms
```

주요 재설계 대상은 `02_app_framework`, `03_packaging_deployment`, `05_security_privacy`, `06_testing_performance` 내부다.

권장 내부 구조는 다음과 같다.

```text
02_app_framework/
  architecture/
    app-components/
    state-management/
    ui-architecture/
    modularity/
  data/
    coroutine/
    flow/
    persistence/
    storage-access/
    paging/
  ui/
    compose/
      runtime/
      state/
      side-effects/
      layout/
      design-system/
      animation/
      performance/
      accessibility/
  navigation/
    intent/
    deep-link/
    navigation3/
    adaptive-navigation/
  dependency-injection/
    hilt/
    metro/
    dynamic-feature/
```

기존 `jetpack-compose` 는 `ui/compose` 로 옮기는 방안을 우선 검토한다. 다만 이동 비용이 크면 `jetpack-compose` 이름을 유지하되 내부만 위와 같이 정리한다.

### 원자 노트 작성 기준

각 원자 노트는 다음 질문 중 하나에만 답해야 한다.

- 이것은 무엇인가?
- 언제 쓰는가?
- 언제 쓰지 않는가?
- 무엇과 구분해야 하는가?
- 어떤 판단 기준으로 선택하는가?
- 어떤 실무 규칙을 지켜야 하는가?

권장 본문 구조:

```md
# 주장형 제목

상위 문서 예시: `허브 제목 -> 상대경로.md`

핵심 주장 2~4문장.

## 왜 중요한가

## 언제 쓰는가

## 쓰지 말아야 할 때

## 관련 문서
```

모든 섹션이 항상 필요하지는 않다. 짧은 개념 노트는 핵심 주장과 관련 문서만 있어도 된다.

### Phase 1. State / ViewModel / Flow / Reducer

가장 먼저 처리한다. 현재 중복 밀도가 가장 높고 Compose State 와도 강하게 얽혀 있다.

Canonical note 후보:

- ViewModel 은 화면 단위 상태와 외부 작업을 조율한다
- ViewModel 은 UI 컨트롤러와 Android Context 를 장기 보관하지 않는다
- ViewModel 은 설정 변경 동안 유지되지만 프로세스 사망 복원까지 보장하지 않는다
- SavedStateHandle 은 프로세스 사망 후 복원해야 하는 작은 상태에 사용한다
- ViewModel 은 외부 작업을 viewModelScope 의 수명에 묶는다
- Mutable 상태 홀더는 ViewModel 내부에 숨기고 외부에는 읽기 전용 상태만 노출한다
- UI 는 상태를 아래로 받고 사용자 행동을 위로 전달한다
- UiState 는 새 collector 가 받아도 안전한 현재 화면의 표현이다
- 복원해야 하는 진행 상태는 일회성 이벤트가 아니라 UiState 로 표현한다
- Snackbar 와 Navigation 처럼 소비 시점이 중요한 신호만 이벤트 스트림으로 분리한다
- Repository 는 데이터 흐름을 Flow 로 제공하고 ViewModel 은 화면 상태로 조합한다
- [stateflow](../02_app_framework/stateflow-and-sharedflow.md) 는 현재값이 필요한 화면 상태에 사용하고 Flow 는 원천 데이터 흐름에 사용한다
- SharedFlow 와 Channel 은 상태 저장소가 아니라 일회성 신호 전달 수단이다
- Flow 를 StateFlow 로 바꿀 때는 stateIn 의 수명과 공유 정책을 명시한다
- Reducer 는 이전 상태와 Action 만 받아 새 상태를 계산한다
- Reducer 는 Repository, Coroutine, Flow, Android API 에 의존하지 않는다
- Reducer 는 상태 계산이 반복되고 전이 규칙이 복잡해질 때만 도입한다

허브화 대상:

- `02_app_framework/architecture/jetpack-architecture/android-viewmodel.md`
- `02_app_framework/architecture/jetpack-architecture/viewmodel-ui-state-reducer.md`
- `02_app_framework/data/async-flow/kotlin-coroutines-flow-stateflow.md`
- `02_app_framework/data/async-flow/kotlin-coroutines-flow-stateflow/flow-as-async-stream.md`
- `02_app_framework/data/async-flow/kotlin-coroutines-flow-stateflow/stateflow-as-current-state-flow.md`
- `02_app_framework/data/async-flow/kotlin-coroutines-flow-stateflow/android-coroutine-flow-practical-patterns.md`

경계 규칙:

- `UiState` 의 의미는 ViewModel/Reducer 영역이 정본이다.
- `StateFlow` 의 의미는 Flow 영역이 정본이다.
- `collectAsStateWithLifecycle()` 사용 이유는 Compose State 영역이 정본이다.
- SharedFlow/Channel 선택은 Flow 영역이 정본이다.
- 화면 상태와 일회성 이벤트 구분은 ViewModel/Reducer 영역이 정본이다.

### Phase 2. Compose Runtime / State / Side Effects

Compose 문서는 Flutter 비교, state lifetime, runtime internals 가 섞여 있다.

Canonical note 후보:

- Compose Runtime 은 읽힌 State 를 기록해 필요한 Composable scope 만 무효화한다
- @Composable 코드는 Compiler 가 Composer 호출로 변환하고 Runtime 이 Composition 을 유지한다
- Slot Table 은 호출 위치를 기준으로 remember 값과 Composition 구조를 보존한다
- State 는 가장 낮은 공통 소유자에 두고 값은 아래로 이벤트는 위로 보낸다
- remember 와 rememberSaveable 은 서로 다른 복원 수명을 제공한다
- 화면 상태는 ViewModel 또는 적절한 state holder 가 소유하고 Composable 은 소비한다
- 상태 API 는 Composable, 화면, Navigation entry, 앱 수명에 따라 선택해야 한다
- Composable body 에서는 외부 부작용을 실행하지 않고 effect 수명에 맞는 API 를 선택한다
- LaunchedEffect 와 DisposableEffect 의 key 가 작업 재시작과 정리를 결정한다
- produceState 와 snapshotFlow 는 Compose State 와 외부 비동기 흐름 사이의 변환 경계다

경계 규칙:

- Flutter 비교 문서는 canonical 지식의 원본이 아니라 bridge 문서다.
- `remember` 의 runtime 보존 원리는 Runtime 쪽에 둔다.
- `remember` 와 `rememberSaveable` 의 선택 기준은 Compose State 쪽에 둔다.
- `StateFlow` 자체의 의미는 Flow 영역에 둔다.
- `collectAsStateWithLifecycle()` 는 Compose State 에서 설명하고 Flow 문서에서는 링크한다.

### Phase 3. Storage / Persistence / Secure Storage

Storage 는 일반 저장소와 보안 저장소를 분리한다.

Canonical note 후보:

- 저장 대상의 소유권과 수명으로 저장소를 먼저 결정한다
- 작은 설정값과 상태값은 DataStore 에 저장한다
- 누적, 검색, 관계형 데이터는 Room 을 통해 저장한다
- SQLite 는 저장 엔진이고 Room 은 애플리케이션 접근 계층이다
- 앱 전용 파일은 app-specific directory 에 저장한다
- 다른 앱과 공유할 미디어는 MediaStore 에 등록한다
- 사용자가 고르는 일반 문서는 SAF 가 소유권을 위임받는다
- 사진 선택은 Photo Picker 를 우선 사용해 권한을 줄인다
- Scoped Storage 는 공유 저장소 직접 경로 접근을 제한한다
- 민감한 값은 Keystore 키와 암호화된 영속 저장소를 함께 사용한다
- Keystore 키 원본은 하드웨어 격리 영역 밖으로 내보내지 않는다
- AES-GCM 암호화는 매번 새로운 IV 와 인증 태그를 사용해야 한다
- 생체 인증은 Keystore 키 사용 조건으로 적용해야 한다
- FBE 의 CE/DE 구분으로 잠금 전후 데이터 가용성을 결정한다
- 백업 대상에서 비밀값과 재생성 가능한 캐시는 제외한다

허브화 대상:

- `02_app_framework/data/storage/android-storage-systems.md`
- `02_app_framework/data/storage/android-storage-and-databases.md`
- `05_security_privacy/secure-storage/android-security-storage.md`

통합 후보:

- `mobile-android-secure-storage.md` 는 `android-security-storage.md` 로 흡수하거나 bridge 문서로 축소한다.
- glossary 의 scoped storage 노트는 3~5 줄 정의만 남긴다.

### Phase 4. Navigation / Intent / Deep Link / Manifest

Navigation 영역은 OS 진입과 앱 내부 back stack 을 분리한다.

Canonical note 후보:

- Intent 는 Android 컴포넌트 실행을 요청하는 데이터 객체다
- 명시적 Intent 는 대상을 지정하고 암시적 Intent 는 조건으로 대상을 찾는다
- Intent filter 는 컴포넌트가 수신할 수 있는 암시적 Intent 의 공개 계약이다
- Intent filter 매칭은 action, category, data 조건의 조합으로 결정된다
- Deep link 는 외부 URI 를 앱 내부 목적지로 연결하는 진입 계약이다
- App Link 는 도메인 소유권을 검증한 HTTPS Deep Link 다
- Deep link URI 는 Activity 에서 수신하고 app layer 에서 내부 destination 으로 변환해야 한다
- 인증이 필요한 Deep link 는 pending destination 과 synthetic back stack 을 명시적으로 처리해야 한다
- Navigation 3 는 Android OS 진입이 아니라 앱 내부 NavKey back stack 을 관리한다
- Deep link 는 URI 에서 NavKey 로 변환된 뒤 Navigation 3 back stack 에 반영된다
- Adaptive navigation 은 top-level destination 을 창 크기에 맞는 navigation chrome 으로 표시한다
- AndroidManifest.xml 은 OS 가 앱 컴포넌트와 외부 진입점을 발견하기 위한 선언 파일이다
- Manifest 는 Deep link 통로를 선언하지만 URI 를 앱 화면으로 해석하지 않는다
- Single Activity 구조에서도 외부 Intent 수신과 내부 화면 이동은 서로 다른 책임이다

경계 규칙:

- Manifest 는 외부 요청을 어떤 컴포넌트가 받을 수 있는지만 선언한다.
- URI 를 어떤 내부 목적지로 바꿀지는 앱 코드의 책임이다.
- Navigation 3 는 OS intent resolution 을 담당하지 않는다.
- Adaptive navigation 은 top-level shell 이고 Navigation 3 Scene 은 back stack entry 배치다.

### Phase 5. Performance / Debugging / Build Optimization

성능 영역은 testing, profiling, debugging, optimization, release validation 을 분리한다.

Canonical note 후보:

- 성능 개선은 기준선 측정과 원인 분석을 통과한 변경만 유효하다
- Macrobenchmark 는 실제 디바이스에서 사용자 시나리오의 성능 회귀를 수치로 검증한다
- Profiler 와 Perfetto 는 성능 저하의 원인을 찾는 도구이지 성능 기준선을 대신하지 않는다
- Compose 성능은 불필요한 재구성을 줄이고 상태 읽기를 늦출 때 개선된다
- 앱 시작 성능의 측정 종료점은 실제 콘텐츠가 그려지는 시점으로 정의해야 한다
- 메모리 성능 문제는 Heap Dump, Allocation Tracking, 운영 Vitals 를 함께 봐야 판단할 수 있다
- 테스트 레이어는 검증 대상과 피드백 비용에 따라 분리해야 한다
- UI 테스트 선택자는 상호작용에는 안정적인 식별자를, 결과 검증에는 의미 정보를 사용해야 한다
- Baseline Profile 은 자주 실행되는 경로를 배포 전에 ART 가 미리 컴파일하도록 돕는다
- Macrobenchmark 는 Baseline Profile 을 생성하고 효과를 검증하지만 Baseline Profile 자체는 테스트가 아니다
- R8 은 릴리즈 빌드에서 코드, 리소스, 이름을 줄이고 keep 규칙으로 동적 사용을 보존한다
- R8 결과는 산출물 크기와 런타임 회귀를 함께 검증해야 안전하다
- Gradle 빌드 최적화는 앱 런타임 성능 최적화와 별도의 문제다
- CI 에서 Baseline Profile 을 자동 생성할 때는 릴리즈 변형과 디바이스 조건을 고정해야 한다

경계 규칙:

- Testing 은 정상 동작 여부를 검증한다.
- Macrobenchmark 는 성능 수치를 검증한다.
- Profiler 와 Perfetto 는 원인을 찾는다.
- R8 은 빌드 시점 축소/최적화다.
- Baseline Profile 은 ART 컴파일 경로를 돕는다.
- Gradle 최적화는 앱 런타임 성능과 별도 문제다.

### 실행 방식

각 phase 는 다음 순서로 진행한다.

1. 기존 파일 목록과 링크 그래프를 수집한다.
2. canonical note 파일명을 확정한다.
3. 기존 본문에서 반복되는 설명을 제거하고 canonical note 로 재작성한다.
4. 기존 원본 파일은 삭제하지 않고 허브 또는 redirect 로 줄인다.
5. Markdown internal link 를 새 canonical note 로 갱신한다.
6. 다음 검증을 실행한다.

검증 항목:

- 남은 wikilink 가 없어야 한다.
- 깨진 Markdown internal link 가 없어야 한다.
- Android subtree 안에서 파일 stem 중복이 없어야 한다.
- 120 줄 이상 비허브 문서가 없어야 한다.
- 완전 동일 본문 중복이 없어야 한다.
- 같은 정본 개념이 2 개 이상의 문서에 반복되면 안 된다.

### Subagent 결과 반영 메모

- Storage subagent 는 실제 Obsidian 경로를 기준으로 분석했으므로 바로 적용 가능하다.
- State/ViewModel/Flow subagent 는 실제 Obsidian 경로를 기준으로 분석했으므로 Phase 1 의 기준으로 삼는다.
- Compose, Navigation, Performance subagent 일부는 repo `docs/` 를 기준으로 분석했다. 개념 경계는 유효하지만 실제 적용 전 Obsidian 현재 경로로 다시 매핑해야 한다.

### 우선순위

1. State / ViewModel / Flow / Reducer
2. Compose State / Runtime / Side Effects
3. Storage / Persistence / Secure Storage
4. Navigation / Intent / Deep Link / Manifest
5. Performance / Debugging / Build Optimization

첫 구현 패스는 Phase 1 부터 시작한다.

### Phase 1 적용 기록

- 적용일: 2026-07-31
- 범위: ViewModel, UiState, Reducer, Flow/StateFlow, Compose 상태 수명/Effect
- 정본 지도: [Android 상태 관리 정본 지도](../02_app_framework/architecture/state-management/android-state-management.md)
- 원칙: 중복 장문 노트는 삭제하지 않고 기존 링크를 보존하는 경유 노트로 축소한다.

### Phase 3 적용 기록

- 적용일: 2026-07-31
- 범위: DataStore, Room, SQLite, app-specific files, MediaStore, SAF, Photo Picker, Scoped Storage, Keystore, AES-GCM, BiometricPrompt, FBE, Direct Boot, backup/cache boundary
- 정본 지도: [Android 저장소와 영속성](../02_app_framework/data/storage/android-storage-and-persistence.md)
- 보안 정본 지도: [보안 저장소 계약](../05_security_privacy/secure-storage/secure-storage-contracts/secure-storage-contracts.md)
- 원칙: 파일 접근 계약과 보안 저장소 계약을 분리하고, 기존 장문 노트는 정본 링크를 가진 경유 노트로 축소한다.

### Phase 4 적용 기록

- 적용일: 2026-07-31
- 범위: Intent, intent-filter, AndroidManifest, exported, package visibility, PendingIntent, Deep Link, App Link, Dynamic App Links, Navigation 3, adaptive navigation
- 정본 지도: [Android Navigation 진입 계약](../02_app_framework/navigation/navigation-contracts/navigation-contracts.md)
- 원칙: OS 진입 계약(Intent/Manifest), 외부 URI 계약(Deep Link), 앱 내부 back stack 계약(Navigation 3), adaptive chrome 계약을 분리한다.
- 참고한 공식 문서: [Intents and intent filters](https://developer.android.com/guide/components/intents-filters), [About App Links](https://developer.android.com/training/app-links/about), [Configure website associations and dynamic rules](https://developer.android.com/training/app-links/configure-assetlinks), [Navigation 3 Deep Link Basic Recipe](https://developer.android.com/guide/navigation/navigation-3/recipes/deeplinks-basic)

### Phase 8 적용 기록

- 적용일: 2026-07-31
- 범위: 큰 화면, 폴더블, PiP, drag and drop, keyboard/pointer/stylus, desktop windowing, multi-window, multi-instance, caption bar, Android XR, Compose for XR, SceneCore, XR capability
- 정본 지도: [Android 폼 팩터와 플랫폼 확장 지도](../07_platforms/android-platforms-and-form-factors.md)
- 원칙: 기기명 분기가 아니라 앱 창, posture, 입력 장치, 공간 capability 를 기준으로 폼 팩터 대응을 설명한다.
- 참고한 공식 문서: [Use window size classes](https://developer.android.com/develop/ui/views/layout/use-window-size-classes), [Adaptive do's and don'ts](https://developer.android.com/develop/adaptive-apps/guides/adaptive-dos-and-donts), [Support desktop windowing](https://developer.android.com/develop/adaptive-apps/guides/support-desktop-windowing), [Make your app fold aware](https://developer.android.com/develop/adaptive-apps/guides/foldables/make-your-app-fold-aware), [Develop with the Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk)

### Phase 9 적용 기록

- 적용일: 2026-07-31
- 범위: bootloader, bootconfig, partitions, AVB, A/B and Virtual A/B OTA, first-stage/second-stage init, init rc language, triggers, services, property service, ueventd, fstab, SELinux/capabilities, Zygote, ART, app process specialization, system_server, AMS/ATMS, process priority, ANR, Rescue Party, dumpsys
- 정본 지도: [Android 부팅과 런타임 지도](../01_system_internals/boot-and-runtime/android-boot-and-runtime.md)
- 원칙: 부팅 순서 조각을 나열하지 않고, 신뢰 검증, mount/update 경계, init 선언, 프로세스 생성, framework service 운영 계약으로 나눈다.
- 참고한 공식 문서: [Bootloader overview](https://source.android.com/docs/core/architecture/bootloader), [Android Verified Boot](https://source.android.com/docs/security/features/verifiedboot/avb), [A/B system updates](https://source.android.com/docs/core/ota/ab), [Android Init Language](https://android.googlesource.com/platform/system/core/+/master/init/README.md), [About the Zygote processes](https://source.android.com/docs/core/runtime/zygote), [Android runtime and Dalvik](https://source.android.com/docs/core/runtime)

## Phase 10 적용 기록

- 적용일: 2026-07-31
- 범위: ConnectivityService, ConnectivityManager, Network, NetworkCapabilities, LinkProperties, default/requested network, NetworkCallback, metered/Data Saver, captive portal, Wi-Fi APIs, cellular policy, VpnService, always-on/lockdown VPN, Private DNS, Network Security Config, netd, TrafficStats, tethering, network debugging
- 정본 지도: [Android 연결성과 네트워크 지도](../01_system_internals/connectivity/android-connectivity.md)
- 원칙: transport 이름이 아니라 capability, validation, policy, 수명, 보안 경계를 기준으로 네트워크 동작을 설명한다.
- 참고한 공식 문서: [ConnectivityManager](https://developer.android.com/reference/android/net/ConnectivityManager), [ConnectivityManager.NetworkCallback](https://developer.android.com/reference/android/net/ConnectivityManager.NetworkCallback), [Wi-Fi infrastructure](https://developer.android.com/develop/connectivity/wifi), [VPN](https://developer.android.com/develop/connectivity/vpn), [Network security configuration](https://developer.android.com/privacy-and-security/security-config), [Connectivity module](https://source.android.com/docs/core/architecture/modular-system/connectivity)

### Phase 13A 적용 기록

- 적용일: 2026-07-31
- 범위: Compose mental model, [recomposition](../02_app_framework/jetpack-compose/runtime/recomposition.md), snapshot state observation, remember, Slot Table/positional identity, Compose compiler/restart/skip, frame phases, state owner, Flutter rebuild comparison, effect API overlap, strong skipping wording
- 정본 지도: [Compose runtime and state model](../02_app_framework/jetpack-compose/runtime/compose-runtime-and-state-model.md)
- 상태/Effect 정본 지도: [Compose 상태와 Effect 계약](../02_app_framework/jetpack-compose/state-and-lifecycle/compose-state-and-effect-contracts/compose-state-and-effect-contracts.md)
- 성능 정본 지도: [Compose 성능 계약](../02_app_framework/jetpack-compose/performance/compose-performance-contracts/compose-performance-contracts.md)
- 원칙: Runtime mental model 은 새 정본으로 묶고, 이미 좋은 state/effect/performance 정본은 재사용하며, 예전 튜토리얼 조각은 redirect stub 으로 축소한다.
- 참고한 공식 문서: [Thinking in Compose](https://developer.android.com/develop/ui/compose/mental-model), [State and Jetpack Compose](https://developer.android.com/develop/ui/compose/state), [State hoisting](https://developer.android.com/develop/ui/compose/state-hoisting), [Side-effects in Compose](https://developer.android.com/develop/ui/compose/side-effects), [Compose phases](https://developer.android.com/develop/ui/compose/phases), [Strong skipping mode](https://developer.android.com/develop/ui/compose/performance/stability/strongskipping)

### Phase 13B 적용 기록

- 적용일: 2026-07-31
- 범위: Compose layout constraints, modifier order, custom layout, intrinsic measurement, SubcomposeLayout, animation API/spec, accessibility semantics, Material 3 color roles, CompositionLocal/design-system provider, Glance app widget boundary
- UI 정본 지도: [Compose layout, animation, accessibility](../02_app_framework/jetpack-compose/layout-and-ui/compose-layout-animation-accessibility.md)
- Design System 정본 지도: [Compose design system](../02_app_framework/jetpack-compose/design-system-and-architecture/compose-design-system.md)
- 원칙: Layout/animation/accessibility 는 UI surface 계약으로, CompositionLocal/Material color/design-system provider 는 architecture/design-system 계약으로 분리한다. Glance 는 일반 Compose UI 가 아니라 RemoteViews widget surface 로 분리한다.
- 참고한 공식 문서: [Compose layouts](https://developer.android.com/develop/ui/compose/layouts/basics), [Constraints and modifier order](https://developer.android.com/develop/ui/compose/layouts/constraints-modifiers), [Custom layouts](https://developer.android.com/develop/ui/compose/layouts/custom), [Choose an animation API](https://developer.android.com/develop/ui/compose/animation/choose-api), [Semantics in Compose](https://developer.android.com/develop/ui/compose/accessibility/semantics), [CompositionLocal](https://developer.android.com/develop/ui/compose/compositionlocal), [Material 3 in Compose](https://developer.android.com/develop/ui/compose/designsystems/material3), [Jetpack Glance](https://developer.android.com/develop/ui/compose/glance)

### Phase 28 적용 기록

- 적용일: 2026-08-01
- 범위: [binder ipc](../01_system_internals/binder-ipc.md), Binder transaction, AIDL, oneway call, Binder thread pool, IPC debugging, process/system service 경계 연결
- 정본 지도: [IPC and process contracts](../01_system_internals/ipc-and-process/ipc-process-contracts/ipc-process-contracts.md)
- 원칙: IPC 고유 계약은 Binder/AIDL/process boundary 로 새로 정리하고, Zygote, system_server, LMKD, sandbox, graphics/media, storage/security 같은 이미 정본이 있는 주제는 중복 작성하지 않고 해당 정본으로 연결한다.
- 추가 정리: Android 전체 문서에서 `관련 정본:` 을 `관련 노트:` 로 통일하고, `- 정본:` 형식의 legacy redirect stub 을 표준 redirect 문서로 변환했다.

### Phase 29 적용 기록

- 적용일: 2026-08-01
- 범위: AOSP/OEM customization, partition ownership, product configuration, RRO, GMS, AOSP build, device bring-up, platform compatibility tests, platform signing, OEM API, custom ROM, platform debugging
- 정본 지도: [Platform customization contracts](../01_system_internals/platform-customization/platform-customization-contracts/platform-customization-contracts.md)
- 원칙: OEM customization 과 OS development guide 조각을 플랫폼 통합 계약으로 재작성하고, Treble/VINTF/HAL, Mainline/APEX, AVB, 앱 배포 서명처럼 이미 정본이 있는 주제는 중복 작성하지 않고 해당 정본으로 연결한다.

### Phase 30 적용 기록

- 적용일: 2026-08-01
- 범위: Jetpack Compose 정본 문서 품질 보강
- 정본 지도: [Compose runtime and state model](../02_app_framework/jetpack-compose/runtime/compose-runtime-and-state-model.md), [Compose layout, animation, accessibility](../02_app_framework/jetpack-compose/layout-and-ui/compose-layout-animation-accessibility.md), [Compose design system](../02_app_framework/jetpack-compose/design-system-and-architecture/compose-design-system.md)
- 원칙: 이미 정본화된 Compose 노트를 추가로 쪼개지 않고, 활성 정본에 H1 을 보강해 단독 노트로 읽히게 만들고 stem 기반 링크 라벨을 제목 기반으로 정리한다.
- 검증: Compose 활성 정본 중 H1 누락 0 개, Android 전체 링크/중복/legacy syntax 검증 통과.

### Phase 31 적용 기록

- 적용일: 2026-08-01
- 범위: Architecture 정본 문서 품질 보강
- 정본 지도: [Android App Architecture](../02_app_framework/architecture/android-app-architecture.md), [Android App Components](../02_app_framework/architecture/app-components/android-app-components.md), [Android Context Boundaries](../02_app_framework/architecture/context-and-modularity/android-context-boundaries.md), [Jetpack Architecture Map](../02_app_framework/architecture/jetpack-architecture/android-jetpack-architecture-map.md), [Android 상태 관리 정본 지도](../02_app_framework/architecture/state-management/android-state-management.md)
- 원칙: 이미 의미 단위로 정본화된 Architecture 노트를 추가로 쪼개지 않고, 활성 정본 54 개에 frontmatter 를 추가해 Obsidian metadata 를 통일했다.
- 추가 정리: Architecture 활성 문서의 redirect 경유 링크 14 개를 권한, IPC, DI 정본 링크로 직접 보정했다.
- 검증: Architecture 활성 frontmatter 누락 0 개, Architecture 활성 redirect 경유 링크 0 개, Android 전체 링크/중복/legacy syntax 검증 통과.

### Phase 32 적용 기록

- 적용일: 2026-08-01
- 범위: Data 정본 문서 품질 보강, Paging 정본 보강, Coroutine/Flow 지도 보강
- 정본 지도: [Android Data Layer Map](../02_app_framework/data/android-data-layer-map.md), [Android Paging Map](../02_app_framework/data/paging/android-paging-map.md), [Flow와 StateFlow 상태 계약](../02_app_framework/data/async-flow/flow-state-contracts/flow-state-contracts.md), [영속 저장소 계약](../02_app_framework/data/storage/persistence-contracts/persistence-contracts.md), [파일 접근 계약](../02_app_framework/data/storage/file-access-contracts/file-access-contracts.md)
- 원칙: 이미 정본화된 storage/Flow/Paging 묶음을 새로 쪼개지 않고, 활성 정본 45 개에 frontmatter 를 추가하고 너무 얇은 Paging 정본에 판단 기준과 layer boundary 를 보강했다.
- 추가 정리: Coroutine/Flow 지도 노트에 중복 방지 규칙을 추가해 coroutine lifetime, stream model, UI state collection, persistence 책임을 분리했다.
- 검증: Data 활성 frontmatter 누락 0 개, Data 활성 13 줄 이하 얇은 정본 0 개, Android 전체 링크/중복/legacy syntax 검증 통과.

### Phase 33 적용 기록

- 적용일: 2026-08-01
- 범위: Navigation 정본 문서 품질 보강, Adaptive Navigation 얇은 정본 보강, Navigation 3 얇은 정본 보강, Intent/Deep Link entrypoint 보강
- 정본 지도: [Android Navigation 진입 계약](../02_app_framework/navigation/navigation-contracts/navigation-contracts.md), [Intent 와 Manifest 계약](../02_app_framework/navigation/intents-and-deep-links/intent-manifest-contracts/intent-manifest-contracts.md), [Deep Link 계약](../02_app_framework/navigation/intents-and-deep-links/deep-link-contracts/deep-link-contracts.md), [Navigation 3 계약](../02_app_framework/navigation/navigation3/navigation3-contracts/navigation3-contracts.md), [Adaptive Navigation 계약](../02_app_framework/navigation/adaptive-navigation/adaptive-navigation-contracts/adaptive-navigation-contracts.md)
- 원칙: 이미 정본화된 navigation 묶음을 새로 쪼개지 않고, 활성 정본 43 개에 frontmatter/H1 을 통일하고 13 줄 이하 얇은 정본에 판단 기준과 책임 경계를 보강했다.
- 검증: Navigation 활성 frontmatter 누락 0 개, H1 누락 0 개, 13 줄 이하 얇은 정본 0 개, Android 전체 링크/중복/legacy syntax 검증 통과.

### Phase 34 적용 기록

- 적용일: 2026-08-01
- 범위: Boot/runtime 정본 문서 품질 보강, 부팅 흐름/system_server/Zygote 지도 보강, redirect 경유 링크 보정
- 정본 지도: [Android 부팅과 런타임 지도](../01_system_internals/boot-and-runtime/android-boot-and-runtime.md), [부팅 흐름 계약](../01_system_internals/boot-and-runtime/boot-flow-contracts/boot-flow-contracts.md), [init와 네이티브 서비스 계약](../01_system_internals/boot-and-runtime/init-service-contracts/init-service-contracts.md), [system_server와 ActivityManager 계약](../01_system_internals/boot-and-runtime/system-server-contracts/system-server-contracts.md), [Zygote와 ART 런타임 계약](../01_system_internals/boot-and-runtime/zygote-runtime-contracts/zygote-runtime-contracts.md)
- 원칙: 이미 정본화된 boot/runtime 묶음을 새로 쪼개지 않고, 활성 정본 40 개에 frontmatter 를 추가하고 얇은 지도 노트 3 개에 경계 규칙을 보강했다.
- 추가 정리: Boot/runtime 활성 문서의 redirect 경유 링크 7 개를 보안, IPC, process 정본 링크로 직접 보정했다.
- 검증: Boot/runtime 활성 frontmatter 누락 0 개, 14 줄 이하 얇은 정본 0 개, redirect 경유 링크 0 개, Android 전체 링크/중복/legacy syntax 검증 통과.

### Phase 35 적용 기록

- 적용일: 2026-08-01
- 범위: Kernel/HAL 정본 문서 품질 보강, H1 보강, HAL native contracts 링크 라벨 보정, redirect 경유 링크 보정
- 정본 지도: [Android kernel runtime](../01_system_internals/kernel-and-hal/android-kernel-runtime.md), [HAL and native boundary](../01_system_internals/kernel-and-hal/hal-native-boundary.md), [Kernel contracts](../01_system_internals/kernel-and-hal/kernel-contracts/kernel-contracts.md), [HAL native contracts](../01_system_internals/kernel-and-hal/hal-native-contracts/hal-native-contracts.md)
- 원칙: 이미 정본화된 kernel/HAL 묶음을 새로 쪼개지 않고, 활성 정본 39 개에 H1 을 추가해 단독 노트로 읽히게 만들었다.
- 추가 정리: Kernel/HAL 활성 문서의 redirect 경유 링크 3 개를 보안과 IPC 정본 링크로 직접 보정하고, stem 기반 링크 라벨 17 개를 제목 기반 라벨로 바꿨다.
- 검증: Kernel/HAL 활성 H1 누락 0 개, 14 줄 이하 얇은 정본 0 개, redirect 경유 링크 0 개, Android 전체 링크/중복/legacy syntax 검증 통과.

### Phase 36 적용 기록

- 적용일: 2026-08-01
- 범위: Android glossary 품질 보강, 용어 노트 frontmatter/H1 정규화, redirect 경유 링크 보정
- 정본 지도: [Android Glossary](../04_system_services/activity-manager-service.md)
- 원칙: Glossary 는 정본을 대체하지 않고 용어별 진입점 역할만 한다. 각 용어 노트는 짧은 정의, 혼동 방지, 정본 링크로 제한해 중복 설명을 만들지 않는다.
- 추가 정리: Glossary 활성 문서 32 개에 frontmatter 를 추가하고, Binder/AppOps/SELinux/UID/Verified Boot 등 redirect 로 향하던 링크를 실제 정본 노트로 직접 보정했다.
- 검증: Glossary 활성 frontmatter 누락 0 개, 14 줄 이하 얇은 정본 0 개, redirect 경유 링크 0 개, Android 전체 링크/중복/legacy syntax 검증 통과.

### Phase 37 권장 종료 적용 기록

- 적용일: 2026-08-01
- 범위: 남은 활성 Android 문서 품질 종료, 전체 redirect 링크 재배선, 이전 문서 redirect stub 삭제
- 원칙: 활성 문서는 frontmatter 와 H1 을 갖추고, 14 줄 이하의 얇은 정본에는 폴더별 판단 기준과 경계를 추가한다. 이전 문서 역할만 남은 redirect stub 은 정본 링크로 inbound link 를 돌린 뒤 제거한다.
- 적용: 활성 문서/메타 문서 293 개를 보정했고, redirect stub 1191 개와 빈 legacy directory 141 개를 제거했다.
- 검증 기준: Android 전체 markdown link, wikilink, file URI, repo docs link, duplicate stem/body, 120 줄 초과 비허브 문서, legacy redirect syntax 를 최종 검증한다.
