---
title: ViewModel은 화면 단위 상태와 외부 작업을 조율한다
tags: [android, android/architecture, android/state-management, android/viewmodel]
aliases: ["ViewModel은 화면 단위 상태와 외부 작업을 조율한다"]
date modified: 2026-08-03 16:35:35 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# ViewModel은 화면 단위 상태와 외부 작업을 조율한다

상위 문서: [Android ViewModel](01_inbox/mobile/android/02_app_framework/architecture/state-management/viewmodel/viewmodel.md)

### 핵심 주장

ViewModel 은 화면이 표시할 상태를 소유하고,

사용자 입력을 외부 작업으로 연결하며,

작업 결과를 다시 UI 상태로 변환한다.

화면 컨트롤러는 ViewModel 의 상태를 관찰하고 그 결과를 그린다.

화면 컨트롤러가 네트워크 요청이나 데이터 변환을 직접 결정하지 않는다.

### 책임 경계

- 화면 입력을 의미 있는 의도로 바꾼다.
- Repository 나 UseCase 를 호출한다.
- 진행 중, 성공, 실패 같은 상태를 관리한다.
- UI 가 소비할 상태를 노출한다.
- 화면에 남아야 할 상태의 생명주기를 결정한다.

ViewModel 은 화면을 그리지 않는다.

ViewModel 은 클릭 이벤트에 따라 버튼의 색을 직접 바꾸지 않는다.

ViewModel 은 Activity 나 Fragment 의 메서드를 호출하지 않는다.

### 흐름

```text
사용자 입력
  -> UI 컨트롤러가 ViewModel 메서드 호출
  -> ViewModel이 외부 작업 조율
  -> 결과를 UiState로 반영
  -> UI가 UiState를 관찰하고 렌더링
```

```kotlin
class UserViewModel(
    private val repository: UserRepository
) : ViewModel() {
    private val _uiState = MutableStateFlow<UiState>(UiState.Idle)
    val uiState = _uiState.asStateFlow()

    fun loadUsers() {
        viewModelScope.launch {
            _uiState.value = UiState.Loading
            _uiState.value = runCatching { repository.getUsers() }
                .fold(
                    onSuccess = { UiState.Success(it) },
                    onFailure = { UiState.Error(it) }
                )
        }
    }
}
```

UI 는 `uiState` 를 수집하고 상태별 화면만 선택한다.

Repository 는 데이터 접근을 담당하고,

ViewModel 은 그 작업과 화면 상태 사이의 조정 지점이 된다.

이 경계는 화면 재생성과 테스트를 단순하게 만든다.
