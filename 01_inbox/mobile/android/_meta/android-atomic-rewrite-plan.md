# Android 문서 의미 기반 원자화 계획

이 문서는 `01_inbox/mobile/android` 아래 Android 노트를 단순 분할 상태에서 의미 기반 원자 노트 체계로 재작성하기 위한 실행 계획이다.

## 현재 판단

현재 구조는 링크 무결성과 파일 단위 분해는 되어 있지만, 최종 원자 노트 체계는 아니다.

문제는 다음과 같다.

- 원본 문서명을 폴더로 보존한 구조가 많다.
- 같은 개념이 ViewModel, Flow, Compose State 문서에 반복된다.
- Storage, Security, Performance, Navigation 영역에서 개념 노트와 실무 가이드가 섞여 있다.
- 숫자 prefix 파일은 원자 노트라기보다 원본 heading 조각에 가깝다.
- 허브 문서와 원자 노트가 같은 계층에서 혼재한다.

현재 확정된 정리 기준은 다음과 같다.

- 내부 링크는 Markdown link 형식을 사용한다.
- 원자 노트 제목은 명사형이 아니라 하나의 주장 또는 판단 기준으로 쓴다.
- 허브 문서는 설명 본문을 최소화하고 canonical note 목록과 판단 순서만 가진다.
- 비교 문서는 canonical 지식의 원본이 아니라 진입 경로로 둔다.
- 프로젝트 적용 판단은 일반 개념 노트와 분리해 decision note로 둔다.

## 최종 폴더 전략

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

기존 `jetpack-compose`는 `ui/compose`로 옮기는 방안을 우선 검토한다. 다만 이동 비용이 크면 `jetpack-compose` 이름을 유지하되 내부만 위와 같이 정리한다.

## 원자 노트 작성 기준

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

## Phase 1. State / ViewModel / Flow / Reducer

가장 먼저 처리한다. 현재 중복 밀도가 가장 높고 Compose State와도 강하게 얽혀 있다.

Canonical note 후보:

- ViewModel은 화면 단위 상태와 외부 작업을 조율한다
- ViewModel은 UI 컨트롤러와 Android Context를 장기 보관하지 않는다
- ViewModel은 설정 변경 동안 유지되지만 프로세스 사망 복원까지 보장하지 않는다
- SavedStateHandle은 프로세스 사망 후 복원해야 하는 작은 상태에 사용한다
- ViewModel은 외부 작업을 viewModelScope의 수명에 묶는다
- Mutable 상태 홀더는 ViewModel 내부에 숨기고 외부에는 읽기 전용 상태만 노출한다
- UI는 상태를 아래로 받고 사용자 행동을 위로 전달한다
- UiState는 새 collector가 받아도 안전한 현재 화면의 표현이다
- 복원해야 하는 진행 상태는 일회성 이벤트가 아니라 UiState로 표현한다
- Snackbar와 Navigation처럼 소비 시점이 중요한 신호만 이벤트 스트림으로 분리한다
- Repository는 데이터 흐름을 Flow로 제공하고 ViewModel은 화면 상태로 조합한다
- StateFlow는 현재값이 필요한 화면 상태에 사용하고 Flow는 원천 데이터 흐름에 사용한다
- SharedFlow와 Channel은 상태 저장소가 아니라 일회성 신호 전달 수단이다
- Flow를 StateFlow로 바꿀 때는 stateIn의 수명과 공유 정책을 명시한다
- Reducer는 이전 상태와 Action만 받아 새 상태를 계산한다
- Reducer는 Repository, Coroutine, Flow, Android API에 의존하지 않는다
- Reducer는 상태 계산이 반복되고 전이 규칙이 복잡해질 때만 도입한다

허브화 대상:

- `02_app_framework/architecture/jetpack-architecture/android-viewmodel.md`
- `02_app_framework/architecture/jetpack-architecture/viewmodel-ui-state-reducer.md`
- `02_app_framework/data/async-flow/kotlin-coroutines-flow-stateflow.md`
- `02_app_framework/data/async-flow/kotlin-coroutines-flow-stateflow/flow-as-async-stream.md`
- `02_app_framework/data/async-flow/kotlin-coroutines-flow-stateflow/stateflow-as-current-state-flow.md`
- `02_app_framework/data/async-flow/kotlin-coroutines-flow-stateflow/android-coroutine-flow-practical-patterns.md`

경계 규칙:

- `UiState`의 의미는 ViewModel/Reducer 영역이 정본이다.
- `StateFlow`의 의미는 Flow 영역이 정본이다.
- `collectAsStateWithLifecycle()` 사용 이유는 Compose State 영역이 정본이다.
- SharedFlow/Channel 선택은 Flow 영역이 정본이다.
- 화면 상태와 일회성 이벤트 구분은 ViewModel/Reducer 영역이 정본이다.

## Phase 2. Compose Runtime / State / Side Effects

Compose 문서는 Flutter 비교, state lifetime, runtime internals가 섞여 있다.

Canonical note 후보:

- Compose Runtime은 읽힌 State를 기록해 필요한 Composable scope만 무효화한다
- @Composable 코드는 Compiler가 Composer 호출로 변환하고 Runtime이 Composition을 유지한다
- Slot Table은 호출 위치를 기준으로 remember 값과 Composition 구조를 보존한다
- State는 가장 낮은 공통 소유자에 두고 값은 아래로 이벤트는 위로 보낸다
- remember와 rememberSaveable은 서로 다른 복원 수명을 제공한다
- 화면 상태는 ViewModel 또는 적절한 state holder가 소유하고 Composable은 소비한다
- 상태 API는 Composable, 화면, Navigation entry, 앱 수명에 따라 선택해야 한다
- Composable body에서는 외부 부작용을 실행하지 않고 effect 수명에 맞는 API를 선택한다
- LaunchedEffect와 DisposableEffect의 key가 작업 재시작과 정리를 결정한다
- produceState와 snapshotFlow는 Compose State와 외부 비동기 흐름 사이의 변환 경계다

경계 규칙:

- Flutter 비교 문서는 canonical 지식의 원본이 아니라 bridge 문서다.
- `remember`의 runtime 보존 원리는 Runtime 쪽에 둔다.
- `remember`와 `rememberSaveable`의 선택 기준은 Compose State 쪽에 둔다.
- `StateFlow` 자체의 의미는 Flow 영역에 둔다.
- `collectAsStateWithLifecycle()`는 Compose State에서 설명하고 Flow 문서에서는 링크한다.

## Phase 3. Storage / Persistence / Secure Storage

Storage는 일반 저장소와 보안 저장소를 분리한다.

Canonical note 후보:

- 저장 대상의 소유권과 수명으로 저장소를 먼저 결정한다
- 작은 설정값과 상태값은 DataStore에 저장한다
- 누적, 검색, 관계형 데이터는 Room을 통해 저장한다
- SQLite는 저장 엔진이고 Room은 애플리케이션 접근 계층이다
- 앱 전용 파일은 app-specific directory에 저장한다
- 다른 앱과 공유할 미디어는 MediaStore에 등록한다
- 사용자가 고르는 일반 문서는 SAF가 소유권을 위임받는다
- 사진 선택은 Photo Picker를 우선 사용해 권한을 줄인다
- Scoped Storage는 공유 저장소 직접 경로 접근을 제한한다
- 민감한 값은 Keystore 키와 암호화된 영속 저장소를 함께 사용한다
- Keystore 키 원본은 하드웨어 격리 영역 밖으로 내보내지 않는다
- AES-GCM 암호화는 매번 새로운 IV와 인증 태그를 사용해야 한다
- 생체 인증은 Keystore 키 사용 조건으로 적용해야 한다
- FBE의 CE/DE 구분으로 잠금 전후 데이터 가용성을 결정한다
- 백업 대상에서 비밀값과 재생성 가능한 캐시는 제외한다

허브화 대상:

- `02_app_framework/data/storage/android-storage-systems.md`
- `02_app_framework/data/storage/android-storage-and-databases.md`
- `05_security_privacy/secure-storage/android-security-storage.md`

통합 후보:

- `mobile-android-secure-storage.md`는 `android-security-storage.md`로 흡수하거나 bridge 문서로 축소한다.
- glossary의 scoped storage 노트는 3~5줄 정의만 남긴다.

## Phase 4. Navigation / Intent / Deep Link / Manifest

Navigation 영역은 OS 진입과 앱 내부 back stack을 분리한다.

Canonical note 후보:

- Intent는 Android 컴포넌트 실행을 요청하는 데이터 객체다
- 명시적 Intent는 대상을 지정하고 암시적 Intent는 조건으로 대상을 찾는다
- Intent filter는 컴포넌트가 수신할 수 있는 암시적 Intent의 공개 계약이다
- Intent filter 매칭은 action, category, data 조건의 조합으로 결정된다
- Deep link는 외부 URI를 앱 내부 목적지로 연결하는 진입 계약이다
- App Link는 도메인 소유권을 검증한 HTTPS Deep Link다
- Deep link URI는 Activity에서 수신하고 app layer에서 내부 destination으로 변환해야 한다
- 인증이 필요한 Deep link는 pending destination과 synthetic back stack을 명시적으로 처리해야 한다
- Navigation 3는 Android OS 진입이 아니라 앱 내부 NavKey back stack을 관리한다
- Deep link는 URI에서 NavKey로 변환된 뒤 Navigation 3 back stack에 반영된다
- Adaptive navigation은 top-level destination을 창 크기에 맞는 navigation chrome으로 표시한다
- AndroidManifest.xml은 OS가 앱 컴포넌트와 외부 진입점을 발견하기 위한 선언 파일이다
- Manifest는 Deep link 통로를 선언하지만 URI를 앱 화면으로 해석하지 않는다
- Single Activity 구조에서도 외부 Intent 수신과 내부 화면 이동은 서로 다른 책임이다

경계 규칙:

- Manifest는 외부 요청을 어떤 컴포넌트가 받을 수 있는지만 선언한다.
- URI를 어떤 내부 목적지로 바꿀지는 앱 코드의 책임이다.
- Navigation 3는 OS intent resolution을 담당하지 않는다.
- Adaptive navigation은 top-level shell이고 Navigation 3 Scene은 back stack entry 배치다.

## Phase 5. Performance / Debugging / Build Optimization

성능 영역은 testing, profiling, debugging, optimization, release validation을 분리한다.

Canonical note 후보:

- 성능 개선은 기준선 측정과 원인 분석을 통과한 변경만 유효하다
- Macrobenchmark는 실제 디바이스에서 사용자 시나리오의 성능 회귀를 수치로 검증한다
- Profiler와 Perfetto는 성능 저하의 원인을 찾는 도구이지 성능 기준선을 대신하지 않는다
- Compose 성능은 불필요한 재구성을 줄이고 상태 읽기를 늦출 때 개선된다
- 앱 시작 성능의 측정 종료점은 실제 콘텐츠가 그려지는 시점으로 정의해야 한다
- 메모리 성능 문제는 Heap Dump, Allocation Tracking, 운영 Vitals를 함께 봐야 판단할 수 있다
- 테스트 레이어는 검증 대상과 피드백 비용에 따라 분리해야 한다
- UI 테스트 선택자는 상호작용에는 안정적인 식별자를, 결과 검증에는 의미 정보를 사용해야 한다
- Baseline Profile은 자주 실행되는 경로를 배포 전에 ART가 미리 컴파일하도록 돕는다
- Macrobenchmark는 Baseline Profile을 생성하고 효과를 검증하지만 Baseline Profile 자체는 테스트가 아니다
- R8은 릴리즈 빌드에서 코드, 리소스, 이름을 줄이고 keep 규칙으로 동적 사용을 보존한다
- R8 결과는 산출물 크기와 런타임 회귀를 함께 검증해야 안전하다
- Gradle 빌드 최적화는 앱 런타임 성능 최적화와 별도의 문제다
- CI에서 Baseline Profile을 자동 생성할 때는 릴리즈 변형과 디바이스 조건을 고정해야 한다

경계 규칙:

- Testing은 정상 동작 여부를 검증한다.
- Macrobenchmark는 성능 수치를 검증한다.
- Profiler와 Perfetto는 원인을 찾는다.
- R8은 빌드 시점 축소/최적화다.
- Baseline Profile은 ART 컴파일 경로를 돕는다.
- Gradle 최적화는 앱 런타임 성능과 별도 문제다.

## 실행 방식

각 phase는 다음 순서로 진행한다.

1. 기존 파일 목록과 링크 그래프를 수집한다.
2. canonical note 파일명을 확정한다.
3. 기존 본문에서 반복되는 설명을 제거하고 canonical note로 재작성한다.
4. 기존 원본 파일은 삭제하지 않고 허브 또는 redirect로 줄인다.
5. Markdown internal link를 새 canonical note로 갱신한다.
6. 다음 검증을 실행한다.

검증 항목:

- 남은 wikilink가 없어야 한다.
- 깨진 Markdown internal link가 없어야 한다.
- Android subtree 안에서 파일 stem 중복이 없어야 한다.
- 120줄 이상 비허브 문서가 없어야 한다.
- 완전 동일 본문 중복이 없어야 한다.
- 같은 정본 개념이 2개 이상의 문서에 반복되면 안 된다.

## Subagent 결과 반영 메모

- Storage subagent는 실제 Obsidian 경로를 기준으로 분석했으므로 바로 적용 가능하다.
- State/ViewModel/Flow subagent는 실제 Obsidian 경로를 기준으로 분석했으므로 Phase 1의 기준으로 삼는다.
- Compose, Navigation, Performance subagent 일부는 repo `docs/`를 기준으로 분석했다. 개념 경계는 유효하지만 실제 적용 전 Obsidian 현재 경로로 다시 매핑해야 한다.

## 우선순위

1. State / ViewModel / Flow / Reducer
2. Compose State / Runtime / Side Effects
3. Storage / Persistence / Secure Storage
4. Navigation / Intent / Deep Link / Manifest
5. Performance / Debugging / Build Optimization

첫 구현 패스는 Phase 1부터 시작한다.

## Phase 1 적용 기록

- 적용일: 2026-07-31
- 범위: ViewModel, UiState, Reducer, Flow/StateFlow, Compose 상태 수명/Effect
- 정본 지도: [Android 상태 관리 정본 지도](01_inbox/mobile/android/02_app_framework/architecture/state-management/android-state-management.md)
- 원칙: 중복 장문 노트는 삭제하지 않고 기존 링크를 보존하는 경유 노트로 축소한다.

## Phase 3 적용 기록

- 적용일: 2026-07-31
- 범위: DataStore, Room, SQLite, app-specific files, MediaStore, SAF, Photo Picker, Scoped Storage, Keystore, AES-GCM, BiometricPrompt, FBE, Direct Boot, backup/cache boundary
- 정본 지도: [Android 저장소와 영속성](01_inbox/mobile/android/02_app_framework/data/storage/android-storage-and-persistence.md)
- 보안 정본 지도: [보안 저장소 계약](01_inbox/mobile/android/05_security_privacy/secure-storage/secure-storage-contracts/secure-storage-contracts.md)
- 원칙: 파일 접근 계약과 보안 저장소 계약을 분리하고, 기존 장문 노트는 정본 링크를 가진 경유 노트로 축소한다.
