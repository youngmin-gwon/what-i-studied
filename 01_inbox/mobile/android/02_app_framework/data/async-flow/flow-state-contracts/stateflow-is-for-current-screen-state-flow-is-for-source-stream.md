---
title: "StateFlow는 현재값이 필요한 화면 상태에 사용하고 Flow는 원천 데이터 흐름에 사용한다"
tags: [android, android/data, android/async, android/flow-state-contracts]
aliases: ["StateFlow는 현재값이 필요한 화면 상태에 사용하고 Flow는 원천 데이터 흐름에 사용한다"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# StateFlow는 현재값이 필요한 화면 상태에 사용하고 Flow는 원천 데이터 흐름에 사용한다

상위 문서: [Flow와 StateFlow 상태 계약](01_inbox/mobile/android/02_app_framework/data/async-flow/flow-state-contracts/flow-state-contracts.md)


화면이 지금 즉시 읽을 수 있는 값과 새 구독자에게 현재 상태를 재생해야 한다면 `StateFlow`를 사용한다.
데이터가 시간에 따라 발생하는 원천 스트림이고 현재값 보관이 흐름의 책임이 아니라면 `Flow`를 사용한다.

## 선택 기준

| 질문 | 선택 |
| --- | --- |
| 새 화면이 들어올 때 현재 UI를 즉시 그려야 하는가? | `StateFlow` |
| 초기값이 의미 있는가? | `StateFlow` |
| DB 변경이나 검색 결과처럼 생산 시점에 값이 나오는가? | `Flow` |
| 수집할 때마다 작업을 시작해도 되는 cold stream인가? | `Flow` |
| 로딩, 성공, 오류를 화면이 항상 알아야 하는가? | `StateFlow<UiState>` |

```kotlin
// 원천 데이터: DAO가 DB 관찰 흐름을 제공한다.
@Query("SELECT * FROM benefits")
fun observeBenefits(): Flow<List<BenefitEntity>>

// 화면 상태: ViewModel이 현재값을 보관한다.
val uiState: StateFlow<BenefitUiState> =
    repository.observeBenefits()
        .map { BenefitUiState.Ready(it) }
        .stateIn(
            viewModelScope,
            SharingStarted.WhileSubscribed(5_000),
            BenefitUiState.Loading,
        )
```

`StateFlow`는 초기값이 필수이고 `.value`로 현재값을 읽을 수 있다.
동일 값은 다시 방출하지 않으므로 화면 상태의 불필요한 갱신을 줄인다.
`Flow`는 기본적으로 cold stream이며 수집이 시작될 때 생산 로직이 실행된다.

원천 흐름을 무조건 `StateFlow`로 바꾸면 생명주기와 캐시 정책이 불필요하게 강해질 수 있다.
먼저 그 값이 상태인지, 발생 순서가 중요한 스트림인지 구분한다.
화면에 전달하는 최종 계약은 대체로 `StateFlow<UiState>`로 명확하게 만든다.

따라서 타입만 보고도 소비자가 계약을 이해할 수 있게 한다.
변경 가능한 `MutableStateFlow`는 ViewModel 내부에 숨기고 읽기 전용 흐름만 외부에 공개한다.

값을 보관해야 하는 이유와 원천 스트림인 이유를 주석보다 타입과 변환 위치로 드러낸다.
이 구분이 화면 요구사항과 맞는지 확인한 뒤 공개 타입을 결정한다.
