---
title: introduce-reducer-only-when-state-transitions-are-complex
tags: [android, android/architecture, android/reducer, android/state-management]
aliases: ["Reducer는 상태 계산이 반복되고 전이 규칙이 복잡해질 때만 도입한다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Reducer 는 상태 계산이 반복되고 전이 규칙이 복잡해질 때만 도입한다

상위 문서: [Android Reducer](./reducer.md)

### 핵심 주장

Reducer 는 모든 화면에 기본으로 추가하는 계층이 아니다.

작은 화면은 [viewmodel](../../../viewmodel.md) 의 `_uiState.update { it.copy(…) }` 가 가장 읽기 쉽고, 상태 계산이 반복되거나 전이 규칙을 한 곳에서 읽어야 할 때만 Reducer 를 도입한다.

### 아직 필요하지 않은 경우

- 단순 조회나 목록 화면
- 상태 필드가 적은 상세 화면
- 몇 개의 명시적 callback 만 있는 설정 화면
- ViewModel 테스트만으로 전이가 충분히 읽히는 화면

### 도입을 검토할 경우

- 입력 필드와 action 종류가 크게 늘어난다.
- 여러 함수에 `copy` 와 검증 계산이 반복된다.
- 특정 action 이 어떤 상태를 만드는지 ViewModel 전체를 읽어야 한다.
- 회원가입, 결제, 주문, 예약, wizard 처럼 단계 전이가 많다.
- Reducer 단위 순수 JVM 테스트가 ViewModel 테스트보다 명확하다.

### 구체적 사례: 회원가입 화면이 복잡해지는 과정

필드가 email, password 두 개뿐이면 ViewModel 의 `update` 만으로 충분하다.

```kotlin
class SignUpViewModel : ViewModel() {
    private val _uiState = MutableStateFlow(SignUpUiState())
    val uiState = _uiState.asStateFlow()

    fun onEmailChanged(value: String) {
        _uiState.update { it.copy(email = value, canSubmit = value.isNotBlank() && it.password.isNotBlank()) }
    }

    fun onPasswordChanged(value: String) {
        _uiState.update { it.copy(password = value, canSubmit = it.email.isNotBlank() && value.isNotBlank()) }
    }
}
```

`canSubmit` 계산이 두 함수에 한 줄씩만 있고, 어떤 action 이 어떤 상태를 만드는지 함수 단위로 바로 읽힌다. 여기까지는 Reducer 가 필요 없다.

닉네임, 비밀번호 확인, 약관 동의, 인증 단계가 추가되면 같은 `canSubmit` 조건이 여러 함수에 중복된다.

```kotlin
fun onNicknameChanged(value: String) {
    _uiState.update {
        it.copy(
            nickname = value,
            canSubmit = it.email.isNotBlank() && it.password.isNotBlank() &&
                value.isNotBlank() && it.agreedToTerms && it.step == SignUpStep.INPUT,
        )
    }
}
// onEmailChanged, onPasswordChanged, onTermsAgreed 도 같은 canSubmit 식을 각자 반복해서 계산한다.
```

이 시점에서 `canSubmit` 조건 하나를 바꾸려면 4개 함수를 모두 찾아 고쳐야 한다. "여러 함수에 `copy` 와 검증 계산이 반복된다" 는 신호가 실제로 드러나는 지점이다.

Reducer 로 옮기면 조건이 한 곳에만 있다.

```kotlin
class SignUpReducer {
    fun reduce(state: SignUpUiState, action: SignUpAction): SignUpUiState {
        val next = when (action) {
            is SignUpAction.EmailChanged -> state.copy(email = action.value)
            is SignUpAction.PasswordChanged -> state.copy(password = action.value)
            is SignUpAction.NicknameChanged -> state.copy(nickname = action.value)
            is SignUpAction.TermsAgreed -> state.copy(agreedToTerms = action.value)
        }
        return next.copy(canSubmit = next.isSubmittable())
    }
}

private fun SignUpUiState.isSubmittable() =
    email.isNotBlank() && password.isNotBlank() && nickname.isNotBlank() &&
        agreedToTerms && step == SignUpStep.INPUT
```

`canSubmit` 계산이 `isSubmittable()` 한 곳으로 모이면서, 조건을 바꿀 때 고쳐야 할 지점이 4곳에서 1곳으로 준다.

### 관찰 신호: 도입 전후 비교

코드 줄 수 대신 실제로 세어볼 수 있는 지표로 판단한다.

| 지표 | Reducer 도입 전 | Reducer 도입 후 |
|---|---|---|
| `canSubmit` 계산이 나타나는 함수 수 | 4 | 1 |
| 새 action 추가 시 수정해야 하는 함수 수 | 상태를 바꾸는 함수 전부 | `reduce` 한 곳 |
| 순수 JVM 테스트로 검증 가능한 범위 | ViewModel 전체(coroutine 포함) | `reduce(oldState, action)` 단위 |

Reducer 단위 테스트는 old state 와 action 을 조합해 전이 누락을 표로 확인할 수 있다.

```kotlin
@Test
fun `약관 미동의 상태에서 닉네임을 입력해도 제출 불가`() {
    val oldState = SignUpUiState(email = "a@test.com", password = "pw1234", agreedToTerms = false)
    val next = reducer.reduce(oldState, SignUpAction.NicknameChanged("mina"))
    assertFalse(next.canSubmit)
}
```

이 표와 테스트는 "함수 4곳에 흩어졌던 계산이 1곳으로 줄었다" 는 것을 추상적 판단이 아니라 실제 수정 지점 수와 테스트 결과로 보여준다.

### 도입 원칙

1. 먼저 단순한 ViewModel 로 시작한다.
2. 반복되는 상태 계산만 Reducer 로 옮긴다.
3. Repository, coroutine, Flow, event stream 은 ViewModel 에 남긴다.
4. `oldState + action -> newState` 계약을 테스트한다.
5. 새 아키텍처를 도입하기보다 ViewModel 내부 계산을 분리한 리팩터링으로 다룬다.

Reducer 가 생겼다는 이유만으로 Store, Processor, Result 계층을 추가하지 않는다.

복잡도를 줄이는 만큼만 추상화하고, 상태 전이 규칙이 단순해지면 직접 `update` 로 되돌릴 수도 있다.

### 복잡도의 신호

코드 줄 수 자체보다 상태 전이의 추적 비용을 본다.

`copy` 가 몇 번 있는지는 참고 지표일 뿐이며, 작은 화면에서 Reducer 를 추가하면 Action 과 dispatch 가 오히려 잡음을 만든다.

반대로 필드가 많지 않아도 한 action 이 여러 필드의 검증, 단계, 오류를 함께 바꾸면 분리가 유용할 수 있다.

### 도입 후 점검

- Reducer 이름만 있고 실제 계산은 ViewModel 에 남아 있지 않은가?
- 외부 의존성이 Reducer 안으로 새어 들어오지 않았는가?
- action 목록이 화면의 실제 사용자 행동과 결과를 설명하는가?
- 순수 JVM 테스트가 전이 표를 읽기 쉽게 표현하는가?

이 질문에 부정적이면 Reducer 가 복잡도를 줄이는지 다시 확인한다.
