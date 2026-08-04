---
title: state-owner-is-chosen-by-lifetime-owner-change-frequency-and-sharing
tags: [android, android/architecture, android/state-management, android/ui-state]
aliases: ["상태 소유자는 화면 위치가 아니라 수명, 소유자, 변경 주기, 공유 범위로 결정한다"]
date modified: 2026-08-04 13:35:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## 상태 소유자는 화면 위치가 아니라 수명, 소유자, 변경 주기, 공유 범위로 결정한다

상위 문서: [Android UI State](./ui-state.md)

### 핵심 주장

같은 화면에 보인다는 이유만으로 모든 상태를 하나의 ViewModel 에 넣지 않는다.

상태가 무엇과 함께 생성되고 사라지는지, 누가 변경하는지, 얼마나 자주 변하는지, 몇 곳에서 공유하는지를 기준으로 owner 를 정한다.

| 기준 | 질문 |
|---|---|
| 수명 | Composable, navigation entry, 화면, 세션 중 무엇과 함께 사라지는가? |
| 소유자 | 누가 변경 규칙과 source of truth 를 책임지는가? |
| 변경 주기 | 입력처럼 자주 변하는가, session 처럼 드물게 변하는가? |
| 공유 범위 | 한 컴포넌트, 화면, flow, 앱 전체 중 어디에서 공유하는가? |

예를 들어 session/settings 는 앱 또는 root scope 의 상태이고, 로그인 입력과 validation 은 screen interaction 상태다.

둘이 한 화면에 함께 표시되어도 각각의 owner 가 다를 수 있다.

```text
AppSessionViewModel -> sessionState
SignInViewModel     -> signInUiState
Route               -> 두 상태를 화면에 전달
```

반대로 fetch 결과, 검색어, 필터, 선택 상태가 하나의 화면 정책을 함께 결정하면 screen ViewModel 에서 조합할 수 있다.

분리는 화면을 쪼개기 위한 규칙이 아니라 수명과 변경 책임을 일치시키기 위한 판단이다.

### 흔한 오류

- 화면에 보인다는 이유로 session 을 form ViewModel 에 복사한다.
- 여러 화면에서 공유해야 할 값을 각 화면이 별도로 fetch 한다.
- 자주 변하는 입력과 드물게 변하는 서버 상태를 같은 변경 경로에 묶는다.
- owner 가 다른 상태를 하나의 거대한 `UiState` 에 넣고 갱신 원인을 숨긴다.

상태를 분리하더라도 route 에서 최종 화면 모델로 조합할 수 있다.

조합이 필요하다는 사실만으로 원래 상태의 owner 를 합칠 이유는 없다.

### 결정 기록

새 state holder 를 추가할 때는 수명, owner, 변경 주기, 공유 범위를 짧게 기록한다.

이 네 가지에 답하지 못하면 화면 위치만 보고 분리한 것일 수 있다.

이 기준은 ViewModel 을 많이 만들라는 뜻이 아니다.

상태를 가장 오래 필요로 하는 owner 가 누구인지 확인한 뒤, 필요한 범위만 올리고 나머지는 낮게 유지한다.

owner 가 바뀌면 상태를 복사하기보다 공유 scope 를 명시적으로 조정한다.

화면은 여러 상태를 읽을 수 있지만 각 상태의 변경 책임까지 소유할 필요는 없다.
