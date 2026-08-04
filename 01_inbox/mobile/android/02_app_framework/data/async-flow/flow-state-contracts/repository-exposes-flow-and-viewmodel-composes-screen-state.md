---
title: repository-exposes-flow-and-viewmodel-composes-screen-state
tags: [android, android/async, android/data, android/flow-state-contracts]
aliases: ["Repository는 데이터 흐름을 Flow로 제공하고 ViewModel은 화면 상태로 조합한다"]
date modified: 2026-08-04 16:33:21 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Repository 는 데이터 흐름을 Flow 로 제공하고 ViewModel 은 화면 상태로 조합한다

상위 문서: [Flow와 StateFlow 상태 계약](./flow-state-contracts.md)

관련 노트: [ViewModel은 화면 단위 상태와 외부 작업을 조율한다](../../../architecture/state-management/viewmodel/viewmodel-orchestrates-screen-state-and-external-work.md)

Repository 는 데이터의 출처와 갱신 방식을 감추고, 관찰 가능한 원천 데이터를 `Flow` 로 노출한다.

ViewModel 은 Repository 의 여러 흐름을 화면이 이해할 수 있는 `UiState` 로 변환한다.

화면은 데이터베이스, 네트워크, 캐시의 존재를 알 필요가 없다.

### 책임을 나눈다

- DAO 는 저장소 변화의 원천인 `Flow` 를 제공한다.
- Repository 는 DTO 변환, 캐시 정책, 원격 동기화를 담당한다.
- ViewModel 은 로딩, 성공, 오류와 같은 화면 상태를 조합한다.
- UI 는 `UiState` 를 수집하고 그 결과만 그린다.

```kotlin
class BenefitRepository(private val dao: BenefitDao) {
    fun observeBenefits(): Flow<List<Benefit>> =
        dao.observeBenefits().map { entities ->
            entities.map(BenefitEntity::toDomain)
        }
}

class BenefitViewModel(
    repository: BenefitRepository,
) : ViewModel() {
    val uiState: StateFlow<BenefitUiState> =
        repository.observeBenefits()
            .map { BenefitUiState.Ready(it) }
            .onStart { emit(BenefitUiState.Loading) }
            .catch { emit(BenefitUiState.Error) }
            .stateIn(
                viewModelScope,
                SharingStarted.WhileSubscribed(5_000),
                BenefitUiState.Loading,
            )
}
```

`Repository` 가 `StateFlow` 를 직접 소유해야 하는 것은 아니다.

원천 데이터가 cold `Flow` 라면 ViewModel 의 화면 생명주기에 맞춰 `stateIn` 으로 공유한다.

반대로 Repository 가 여러 소비자에게 공통으로 제공해야 하는 상태라면 그 공유 범위를 Repository 에 둘 수 있다.

이 구조는 데이터 접근 정책과 화면 표현 정책을 분리한다.

따라서 UI 테스트는 `UiState` 를 검사하고, Repository 테스트는 데이터 흐름을 검사할 수 있다.

구현을 시작할 때 다음 경계를 확인한다.

- Repository 반환 타입은 화면 전용 타입이 아닌 도메인 타입인가?
- ViewModel 이 원천 Flow 를 화면용 상태로 변환하는가?
- UI 가 Repository 나 DAO 를 직접 참조하지 않는가?
