---
title: "복원해야 하는 진행 상태는 일회성 이벤트가 아니라 UiState로 표현한다"
tags: [android, android/architecture, android/state-management, android/ui-state]
aliases: ["복원해야 하는 진행 상태는 일회성 이벤트가 아니라 UiState로 표현한다"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# 복원해야 하는 진행 상태는 일회성 이벤트가 아니라 UiState로 표현한다

상위 문서: [Android UI State](01_inbox/mobile/android/02_app_framework/architecture/state-management/ui-state/ui-state.md)


## 핵심 주장

화면 회전, collector 재시작, 프로세스 복원 뒤에도 이어져야 하는 진행 상태는 event stream에만 넣지 않는다.
현재 단계와 결과를 `UiState`에 기록해야 새 화면이 최신 상태를 읽고 같은 흐름을 재현할 수 있다.

```kotlin
enum class VerificationStep { INPUT, VERIFYING, VERIFIED, FAILED }

data class VerificationUiState(
    val step: VerificationStep = VerificationStep.INPUT,
    val code: String = "",
    val errorMessage: String? = null,
)
```

`VerifyStarted`, `VerifySucceeded` 같은 action은 상태 전이를 요청하는 입력으로 사용할 수 있다.
하지만 `Verified`라는 현재 사실을 event로만 발행하면 늦게 구독한 UI가 성공 여부를 알 수 없다.
특히 중간 단계 입력, 재시도 가능 여부, 복원해야 할 대상 id는 상태로 보존해야 한다.

## 적용 예

```text
SubmitStarted  -> step = VERIFYING
SubmitSuccess  -> step = VERIFIED
SubmitFailure  -> step = FAILED, errorMessage 설정
```

복원 대상이 작으면 `SavedStateHandle`이나 `rememberSaveable`로 저장하고, 서버 데이터나 영속 데이터는 Repository/DataStore/Room이 소유한다.
어떤 저장 수단을 쓰든 화면이 현재 진행 상태를 `UiState`로 표현하는 원칙은 유지된다.

## 판단 질문

- 새 collector가 이 값을 못 받으면 화면을 잘못 그리는가?
- 프로세스 복원 뒤 사용자가 이어서 봐야 하는가?
- 값이 현재 화면의 단계나 선택을 설명하는가?

하나라도 그렇다면 이벤트보다 상태를 우선한다.

## 이벤트와 함께 사용할 때

상태와 이벤트는 서로 대체재가 아니다.
`SubmitSucceeded` 이벤트로 즉시 snackbar를 보여 주면서, 동시에 `step = VERIFIED`를 `UiState`에 기록할 수 있다.
이벤트가 유실되어도 현재 단계는 상태에서 복원되고, 이벤트가 중복되어도 상태 자체가 여러 번 소비되지 않는다.

복원해야 하는 값은 primitive key나 작은 단계 정보로 제한한다.
대용량 응답이나 인증 토큰을 화면 상태에 넣는 대신 영속 계층과 다시 조회할 식별자를 분리한다.

## 테스트 관점

`SubmitStarted`와 `SubmitSuccess`를 순서대로 적용한 뒤 새 collector가 `VERIFIED`를 받는지 검증한다.
이벤트 collector가 실행되지 않아도 상태만으로 화면의 진행 단계를 설명할 수 있어야 한다.
