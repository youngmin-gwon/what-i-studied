---
title: UiState는 새 collector가 받아도 안전한 현재 화면의 표현이다
tags: [android, android/architecture, android/state-management, android/ui-state]
aliases: ["UiState는 새 collector가 받아도 안전한 현재 화면의 표현이다"]
date modified: 2026-08-03 16:35:29 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# UiState는 새 collector가 받아도 안전한 현재 화면의 표현이다

상위 문서: [Android UI State](01_inbox/mobile/android/02_app_framework/architecture/state-management/ui-state/ui-state.md)

### 핵심 주장

`UiState` 는 지금 화면이 무엇을 그려야 하는지를 나타내는 현재 상태다.

새 collector 가 구독해도 같은 값을 받아 화면을 재현할 수 있어야 한다.

따라서 로딩, 입력값, 선택값, 오류, 현재 단계처럼 다시 읽어도 의미가 유지되는 정보를 담는다.

```kotlin
data class ProfileUiState(
    val isLoading: Boolean = false,
    val name: String = "",
    val errorMessage: String? = null,
)
```

`StateFlow` 는 최신 상태를 보관하고 새 collector 에게 현재 값을 전달하므로 이 목적에 맞다.

UI 는 collector 가 잠시 없어졌다가 다시 생겨도 최신 `UiState` 를 받아 동일한 화면을 그린다.

### 담을 것

- 화면에 표시할 데이터
- 입력 draft 와 선택된 탭
- 로딩, 빈 결과, 오류, 성공 같은 화면 단계
- 복원되어야 하는 진행 단계
- 다른 필드로부터 계산되는 파생 표시 상태

### 담지 않을 것

- 한 번만 실행해야 하는 snackbar 호출 자체
- `NavController`, `SnackbarHostState`, `FocusRequester`
- Repository 나 Android `Context` 같은 외부 의존성
- collector 가 놓치면 안 되는 진행 상태를 대체하는 ephemeral signal

### 실무 규칙

상태 필드는 화면이 현재 어떤 모드인지 설명하는 이름을 사용한다.

`isLoading`, `selectedTab`, `errorMessage` 처럼 렌더링 조건과 직접 연결되는 이름이 좋다.

반대로 `shouldShowOnce` 처럼 소비 여부를 나타내는 플래그는 event 와 상태를 혼합하기 쉽다.

상태가 여러 필드의 조합으로만 유효하다면 sealed class 로 불가능한 조합을 제거할 수 있다.

예를 들어 `Loading` 과 `Content` 가 동시에 참이 될 수 없다면 별도 boolean 여러 개보다 하나의 화면 단계가 안전하다.

### 테스트 관점

새 collector 가 초기값 또는 최신값을 받았을 때 화면이 재현되는지 확인한다.

상태를 만들기 위해 Android UI 객체나 collector 의 실행 순서가 필요하다면 UiState 의 책임이 흐려진 것이다.

`errorMessage` 처럼 상태로 남겨도 되는 값과 `ShowSnackbar` 처럼 소비 시점이 중요한 신호는 분리 기준을 명시해야 한다.

같은 오류라도 화면에 계속 표시해야 하면 `UiState`, 한 번만 알림을 실행해야 하면 event 가 적합하다.
