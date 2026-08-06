---
title: [viewmodel](../../../viewmodel.md)-exposes-read-only-state
tags: [android, android/architecture, android/state-management, android/viewmodel]
aliases: ["Mutable 상태 홀더는 ViewModel 내부에 숨기고 외부에는 읽기 전용 상태만 노출한다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Mutable 상태 홀더는 ViewModel 내부에 숨기고 외부에는 읽기 전용 상태만 노출한다

상위 문서: [Android ViewModel](./viewmodel.md)

### 핵심 주장

상태를 변경할 수 있는 홀더는 ViewModel 의 private 필드로 제한한다.

UI 와 다른 호출자는 읽기 전용 `[stateflow](../../../stateflow-and-sharedflow.md)`, `LiveData` 또는 동등한 인터페이스만 받는다.

이 구조는 상태 변경의 단일 진입점을 만들고,

화면이 임의로 상태를 덮어쓰는 일을 막는다.

```kotlin
data class UiState(
    val users: List<User> = emptyList(),
    val isLoading: Boolean = false,
    val error: String? = null
)

class UserViewModel : ViewModel() {
    private val _uiState = MutableStateFlow(UiState())
    val uiState: StateFlow<UiState> = _uiState.asStateFlow()

    fun loadUsers() = viewModelScope.launch {
        _uiState.update { it.copy(isLoading = true, error = null) }
        val result = runCatching { repository.getUsers() }
        _uiState.update {
            result.fold(
                onSuccess = { users -> it.copy(users = users, isLoading = false) },
                onFailure = { error -> it.copy(error = error.message, isLoading = false) }
            )
        }
    }
}
```

### 상태 모델

여러 값이 함께 움직이면 불변 `UiState` 로 묶는다.

상태 전이는 `copy` 로 새 객체를 만들어 표현한다.

그러면 한 번의 방출이 화면에 일관된 스냅샷을 전달한다.

`MutableLiveData` 를 써야 하는 경우에도 외부에는 `LiveData` 만 반환한다.

Compose 에서는 `StateFlow` 와 `asStateFlow()` 조합을 기본으로 삼을 수 있다.

UI 는 상태를 읽고 이벤트를 ViewModel 메서드로 전달한다.

상태 홀더를 public 으로 열거나 mutable 컬렉션을 그대로 노출하지 않는다.

### API 점검

- `MutableStateFlow` 와 `MutableLiveData` 가 private 인가?
- 외부 타입이 `StateFlow` 또는 `LiveData` 인가?
- 상태 변경 메서드가 ViewModel 내부에만 있는가?
- 목록과 중첩 객체도 외부에서 변경할 수 없는가?

컬렉션을 담은 상태라면 새 목록을 만들어 방출한다.

기존 mutable 목록을 그대로 수정하면 관찰자가 변경을 안정적으로 감지하지 못할 수 있다.

읽기 전용 노출은 단순히 접근 제한자를 줄이는 문제가 아니다.

상태 전이를 ViewModel 의 명령과 검증 안에 모아,

UI 와 비동기 작업이 서로 다른 값을 덮어쓰지 않게 하는 설계다.

테스트는 public 상태만 읽어 결과를 검증한다.

테스트 코드가 내부 mutable 홀더를 직접 건드린다면 캡슐화 경계가 약해진 신호다.
