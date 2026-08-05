---
title: launched-effect-owns-composable-cancellable-work
tags: ["android", "android/app-framework"]
aliases: [Cancellable Coroutine Work, LaunchedEffect]
date modified: 2026-08-05 13:59:32 +09:00
date created: 2026-07-31 16:53:16 +09:00
---

## Composable 과 함께 취소되어야 하는 작업은 LaunchedEffect 로 시작한다

### 1. 개념 정의 (What)

`LaunchedEffect(key1, key2) { block }` 는 Composable 함수가 Composition 파이프라인에 진입(Enter)할 때 코루틴(Coroutine)을 생성하여 비동기 작업(Async Task)을 실행하고, Composable 이 트리를 이탈(Leave)하거나 키(Key)가 변경되면 **실행 중이던 코루틴을 자동으로 취소(Cancel)**하는 수명주기 종속 비동기 이펙트 API 다.

---

### 2. LaunchedEffect API 의 필요성 (Why)

Composable 바디 내부에서 `CoroutineScope().launch { … }` 를 직접 실행하는 것은 매우 치명적이다:

- **코루틴 누수(Leak)**: Recomposition 이 일어날 때마다 새로운 코루틴이 무한 생성되고, 화면을 벗어나도 비동기 작업이 취소되지 않아 백그라운드 자원을 점유한다.
- **Side-Effect 규칙 위반**: Composition 계산 파이프라인 중간에 비동기 작업을 직접 구동하므로 멱등성과 순수성이 깨진다.

`LaunchedEffect` 는 코루틴 수명주기를 Composition 수명주기와 정확히 일치시켜 자동 취소 및 안전한 비동기 작업 실행을 보장한다.

---

### 3. 내부 동작 메커니즘 (How)

```
[Composition 파이프라인 진입]
  |--> key1, key2 저장
  |--> CoroutineScope 생성 및 block launch
  
[Recomposition 시 (Key 변경 발생)]
  |--> 기존 실행 중이던 Job.cancel() 실행 (CancellationException 전파)
  |--> 새로운 키 기반 CoroutineScope 생성 및 block 재실행
  
[Composition 화면 이탈 시 (Leave/Uncompose)]
  |--> Job.cancel() 즉시 발동하여 비동기 코루틴 완전 정지!
```

1. **CompositionContinuationScope**: 런타임은 `LaunchedEffect` 가 호출되면 `ControlledComposition` 의 코루틴 컨텍스트를 상속하는 Scope 를 할당한다.
2. **Key 대조 기반 Restart**: 재구성 시 전달된 `key` 값들을 `equals()` 로 비교하여 하나라도 다르면 현재 진행 중인 Job 을 즉시 `cancel()` 하고 새 람다를 구동한다.
3. **단 1 회 실행 (`Unit` / `True` Key)**: `LaunchedEffect(Unit)` 형태로 전달하면 Composable 이 최초로 렌더링될 때 딱 1 회만 구동되며 이탈 전까지 취소되지 않는다.

---

### 4. 올바른 LaunchedEffect 코드 패턴

```kotlin
@Composable
fun UserDetailScreen(
    userId: String,
    viewModel: UserDetailViewModel = hiltViewModel()
) {
    val snackbarHostState = remember { SnackbarHostState() }

    // ✅ userId 가 변경될 때마다 이전 로딩 작업을 취소하고 새 사용자 정보를 가져옴
    LaunchedEffect(userId) {
        viewModel.loadUserProfile(userId)
    }

    // ✅ ViewModel의 일회성 UI Event (Channel/SharedFlow) 수집
    LaunchedEffect(Unit) {
        viewModel.uiEvent.collect { event ->
            when (event) {
                is UiEvent.ShowSnackbar -> snackbarHostState.showSnackbar(event.message)
            }
        }
    }

    Scaffold(snackbarHost = { SnackbarHost(snackbarHostState) }) { padding ->
        UserContent(padding)
    }
}
```

---

상위 문서: [Compose 상태와 Effect 계약](./compose-state-and-effect-contracts.md)

관련 노트: [Composable body는 빠르고 idempotent하며 side-effect free 해야 한다](../../runtime/compose-runtime-contracts/composable-body-must-be-fast-idempotent-and-side-effect-free.md), [rememberCoroutineScope는 수동 제어 UI Coroutine을 소유한다](./remember-coroutine-scope-owns-manually-controlled-ui-coroutines.md)

출처: [Side-effects in Compose](https://developer.android.com/develop/ui/compose/side-effects#launchedeffect)

검증일: 2026-08-05. Compose 공식 가이드의 LaunchedEffect 섹션을 대조하여 CoroutineScope 자동 취소, Key 기반 Restart 알고리즘 및 ViewModel UI Event 수집 패턴 서술을 정밀 보강했다.
