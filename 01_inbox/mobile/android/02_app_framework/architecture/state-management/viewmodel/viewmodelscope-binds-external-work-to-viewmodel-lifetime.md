# ViewModel은 외부 작업을 viewModelScope의 수명에 묶는다

상위 문서: [Android ViewModel](01_inbox/mobile/android/02_app_framework/architecture/state-management/viewmodel/viewmodel.md)


## 핵심 주장

ViewModel이 시작한 비동기 작업은 `viewModelScope`에서 실행한다.
ViewModel이 제거되면 스코프가 취소되어 작업도 함께 종료된다.

이렇게 하면 화면 소유자가 사라진 뒤에도 네트워크 요청이나 데이터 처리가
계속 실행되는 일을 줄이고, 작업의 취소 경계를 ViewModel 수명과 일치시킬 수 있다.

```kotlin
class UserViewModel(
    private val repository: UserRepository
) : ViewModel() {
    fun refresh() = viewModelScope.launch {
        repository.refresh()
    }
}
```

## 작업 조율

여러 작업이 같은 화면 상태를 갱신하면 하나의 부모 코루틴 아래에서 조율한다.
실패를 화면 상태로 바꾸고, 취소는 정상적인 생명주기 동작으로 취급한다.

```kotlin
fun load() = viewModelScope.launch {
    _uiState.value = UiState.Loading
    try {
        val users = repository.getUsers()
        _uiState.value = UiState.Success(users)
    } catch (cancelled: CancellationException) {
        throw cancelled
    } catch (error: Exception) {
        _uiState.value = UiState.Error(error)
    }
}
```

`GlobalScope`나 ViewModel과 무관한 독립 스코프를 사용하지 않는다.
그런 작업은 소유자가 불명확해지고 취소·테스트가 어려워진다.

작업이 ViewModel보다 오래 살아야 한다면 Repository나 애플리케이션 수준의
작업 관리자처럼 더 적절한 소유자를 정하고 결과 전달 규칙을 명시한다.

`viewModelScope`는 작업 취소를 보장하지만, 결과를 저장하거나 재시도하는 정책까지
자동으로 결정하지는 않는다.

## 테스트 기준

테스트에서는 외부 작업을 가짜 Repository로 대체하고,
작업 완료 전 상태와 완료 후 상태를 확인한다.
ViewModel이 정리될 때 작업이 취소되는지도 검증 대상이다.

작업이 실패했을 때 예외가 무시되지 않고 UI 상태로 전달되는지 확인한다.
취소 예외를 일반 오류로 표시하지 않도록 구분한다.

화면이 다시 만들어져도 이미 실행 중인 작업을 중복 시작하지 않도록
호출 조건과 상태 전이를 함께 설계한다.
