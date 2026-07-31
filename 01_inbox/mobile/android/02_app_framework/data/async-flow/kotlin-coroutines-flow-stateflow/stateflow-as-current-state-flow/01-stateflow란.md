# StateFlow란?

`StateFlow`는 **항상 현재값을 하나 가지고 있는 Flow**입니다.

일반 Flow가 "흘러오는 데이터"라면, StateFlow는 "현재 상태가 적힌 전광판"에 가깝습니다.

| 구분       | Flow                      | StateFlow     |
|:---------|:--------------------------|:--------------|
| 현재값 보관   | 없음                        | 있음            |
| 초기값 필요   | 필요 없음                     | 반드시 필요        |
| 새 구독자 동작 | collect 시점부터 받음           | 즉시 최신값 1개를 받음 |
| 대표 용도    | DB 관찰, 이벤트 스트림, 비동기 파이프라인 | 화면 UI 상태      |
| 성격       | 보통 Cold                   | Hot           |

`StateFlow`는 UI 상태에 특히 잘 맞습니다. 화면은 언제든 "지금 무엇을 그려야 하는지"를 알아야 하기 때문입니다.

```kotlin
data class ProfileUiState(
    val isLoading: Boolean = false,
    val userName: String = "",
    val errorMessage: String? = null,
)
```

```kotlin
class ProfileViewModel(
    private val repository: ProfileRepository,
) : ViewModel() {
    private val _uiState = MutableStateFlow(ProfileUiState(isLoading = true))
    val uiState: StateFlow<ProfileUiState> = _uiState.asStateFlow()

    fun load() {
        viewModelScope.launch {
            runCatching {
                repository.fetchProfile()
            }.onSuccess { profile ->
                _uiState.value = ProfileUiState(userName = profile.name)
            }.onFailure {
                _uiState.value = ProfileUiState(errorMessage = "프로필을 불러오지 못했습니다.")
            }
        }
    }
}
```
