# Repository는 Flow를 노출하고, ViewModel은 StateFlow로 바꾼다

현대 Android에서 가장 흔한 패턴입니다.

```kotlin
class BenefitRepository(
    private val dao: BenefitDao,
    private val api: BenefitApi,
) {
    fun observeBenefits(): Flow<List<Benefit>> {
        return dao.observeBenefits()
    }

    suspend fun refreshBenefits() {
        val remoteBenefits = api.fetchBenefits()
        dao.replaceAll(remoteBenefits)
    }
}
```

Repository는 데이터 출처를 숨깁니다. UI 입장에서는 이 데이터가 DB에서 오는지, 네트워크에서 오는지, 캐시에서 오는지 몰라도 됩니다.

ViewModel은 이 Flow를 화면 상태로 바꿉니다.

```kotlin
class BenefitViewModel(
    repository: BenefitRepository,
) : ViewModel() {
    val uiState: StateFlow<BenefitUiState> =
        repository.observeBenefits()
            .map { benefits ->
                BenefitUiState.Ready(benefits)
            }
            .stateIn(
                scope = viewModelScope,
                started = SharingStarted.WhileSubscribed(5_000),
                initialValue = BenefitUiState.Loading,
            )
}
```

---
