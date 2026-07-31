---
title: "Fetch 상태와 Interaction 상태는 소유자와 변경 주기가 다르면 분리한다"
tags: [android, android/architecture, android/state-management, android/ui-state]
aliases: ["Fetch 상태와 Interaction 상태는 소유자와 변경 주기가 다르면 분리한다"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# Fetch 상태와 Interaction 상태는 소유자와 변경 주기가 다르면 분리한다

상위 문서: [Android UI State](01_inbox/mobile/android/02_app_framework/architecture/state-management/ui-state/ui-state.md)


## 핵심 주장

Repository에서 오는 fetch 상태와 사용자의 입력·선택·검증·submit 상태는 같은 화면에 있어도 성격이 다를 수 있다.
전자는 데이터 계층이나 공유 관찰자가 소유하고, 후자는 screen ViewModel이 소유하는 편이 자연스럽다.

```text
Repository Flow -> App/session 또는 screen data state
사용자 입력    -> screen interaction state
```

예를 들어 session은 앱 전체에서 공유되며 변경이 드물다.
반면 로그인 form은 한 navigation entry의 수명에 묶이고 입력마다 자주 변한다.
두 상태를 억지로 하나의 거대한 `UiState`로 만들면 owner와 변경 원인이 흐려진다.

```kotlin
@Composable
fun SignInRoute(
    sessionViewModel: AppSessionViewModel,
    signInViewModel: SignInViewModel,
) {
    val session by sessionViewModel.sessionState.collectAsStateWithLifecycle()
    val form by signInViewModel.uiState.collectAsStateWithLifecycle()

    SignInScreen(sessionState = session, uiState = form)
}
```

## 합칠 수 있는 경우

쿠폰 목록, 검색어, 정렬, 필터, 선택, 새로고침처럼 하나의 화면 정책을 함께 결정하는 값은 한 ViewModel에서 `combine`해 최종 `UiState`로 만들 수 있다.
결정 기준은 화면에 같이 보이는지가 아니라 상태 간 정책적 결합도다.

## 변경 주기 차이

Repository fetch는 데이터 갱신이나 화면 재진입 때 바뀌지만, 검색어와 선택 상태는 키 입력마다 바뀔 수 있다.
두 흐름을 분리하면 빠른 interaction 변경이 공유 데이터 관찰을 불필요하게 재생성하지 않는다.
반대로 interaction이 fetch 결과의 필터링·정렬을 결정한다면 화면 ViewModel에서 명시적으로 조합한다.

## 구현 순서

1. data layer의 원본 Flow와 screen interaction state를 식별한다.
2. 각 상태의 owner와 lifecycle을 결정한다.
3. 화면 정책이 필요한 지점에서만 `combine` 또는 명시적인 mapping을 적용한다.
4. 최종적으로 UI에는 필요한 `UiState`만 전달한다.

이 순서는 모든 상태를 처음부터 하나의 모델로 복사하는 일을 줄이고, source of truth 중복을 방지한다.

단순 fetch-only 변환이면 별도 ViewModel을 추가하기 전에 Repository Flow, observer, 기존 `stateIn` 중 가장 단순한 owner를 선택한다.
