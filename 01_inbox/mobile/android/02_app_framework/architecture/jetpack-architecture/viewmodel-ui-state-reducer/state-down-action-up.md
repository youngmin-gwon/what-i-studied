# 기본 구조: State Down, Action Up

상위 노트: [viewmodel-ui-state-reducer](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/viewmodel-ui-state-reducer.md)

Compose 화면의 기본 흐름은 `state down, action up`입니다.

```kotlin
data class SignInUiState(
    val isIdError: Boolean = false,
    val isPasswordError: Boolean = false,
    val isSubmitting: Boolean = false,
    val errorMessage: String? = null,
)

class SignInViewModel(
    private val authRepository: AuthRepository,
) : ViewModel() {
    private val _uiState = MutableStateFlow(SignInUiState())
    val uiState: StateFlow<SignInUiState> = _uiState.asStateFlow()

    fun onIdChanged() {
        _uiState.update { state ->
            state.copy(isIdError = false)
        }
    }

    fun signIn(id: String, password: String) {
        viewModelScope.launch {
            _uiState.update {
                it.copy(
                    isSubmitting = true,
                    errorMessage = null,
                )
            }

            val result = authRepository.signIn(id, password)

            _uiState.update {
                result.fold(
                    onSuccess = { it.copy(isSubmitting = false) },
                    onFailure = { error ->
                        it.copy(
                            isSubmitting = false,
                            errorMessage = error.message ?: "로그인에 실패했습니다.",
                        )
                    }
                )
            }
        }
    }
}

### 5-1. Data 계층 예외 처리: Result<T>와 runCatching

Repository나 DataSource에서 파일 IO, 네트워크, JSON 파싱 시 발생하는 예외(Exception)를 안전하게 처리하기 위해 Kotlin의 `runCatching`과 `Result<T>`를 활용합니다.

```kotlin
// Data 계층 (RepositoryImpl)
class LicenseRepositoryImpl(
    private val assetManager: AssetManager,
) : LicenseRepository {

    override suspend fun getOpenSourceLicenses(): Result<List<OpenSourceArtifact>> = withContext(Dispatchers.IO) {
        runCatching {
            val jsonString = assetManager.open("licenses/artifacts.json")
                .bufferedReader()
                .use { it.readText() }

            LicenseJsonParser.parseJson(jsonString).map { it.toDomain() }
        }
    }
}
```

* **`runCatching { ... }`**: 실행 블록 내에서 예외가 발생할 경우 이를 낚아채 `Result.failure(exception)`로 감싸 반환합니다.
* **ViewModel과의 연동**: ViewModel은 `Result.fold()` 또는 `onSuccess`/`onFailure`를 통해 비동기 작업 결과를 안전하게 UI State(`UiState.Content`, `UiState.Error` 등)로 매핑할 수 있습니다.
```

Composable은 상태를 구독하고 callback만 넘깁니다.

```kotlin
@Composable
fun SignInRoute(
    viewModel: SignInViewModel,
) {
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()

    SignInScreen(
        uiState = uiState,
        onIdChanged = viewModel::onIdChanged,
        onSignInClick = viewModel::signIn,
    )
}
```

이 구조에서는 화면 상태의 단일 출처가 ViewModel입니다. UI는 상태를 직접 고치지 않고, 행동만 올립니다.

---
