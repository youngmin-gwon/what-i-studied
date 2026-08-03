---
title: 새 입력이 이전 작업을 무효화하면 flatMapLatest로 이전 흐름을 취소한다
tags: [android, android/data, android/async, android/flow-state-contracts]
aliases: ["새 입력이 이전 작업을 무효화하면 flatMapLatest로 이전 흐름을 취소한다"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# 새 입력이 이전 작업을 무효화하면 flatMapLatest로 이전 흐름을 취소한다

상위 문서: [Flow와 StateFlow 상태 계약](01_inbox/mobile/android/02_app_framework/data/async-flow/flow-state-contracts/flow-state-contracts.md)


검색어, 선택된 계정, 필터처럼 새 입력이 이전 요청의 의미를 없애면 `flatMapLatest`를 사용한다.
새 입력이 들어오면 이전에 매핑된 Flow의 수집이 취소되고 최신 Flow만 유지된다.

```kotlin
private val query = MutableStateFlow("")

val results: StateFlow<List<Product>> =
    query
        .debounce(300)
        .distinctUntilChanged()
        .flatMapLatest { keyword ->
            if (keyword.isBlank()) {
                flowOf(emptyList())
            } else {
                repository.searchProducts(keyword)
            }
        }
        .stateIn(
            viewModelScope,
            SharingStarted.WhileSubscribed(5_000),
            emptyList(),
        )
```

`debounce`는 짧은 입력 연속으로 요청이 과도하게 발생하는 것을 줄인다.
`distinctUntilChanged`는 같은 입력에 대한 중복 작업을 막는다.
그 다음 `flatMapLatest`를 적용해야 이전 검색 결과가 늦게 도착해 최신 결과를 덮어쓰지 않는다.

모든 입력의 작업을 끝까지 처리해야 한다면 `flatMapConcat`이나 `flatMapMerge`가 더 적합할 수 있다.
즉, 연산자 선택은 동시성 자체보다 이전 작업의 결과가 여전히 유효한지에 달려 있다.

Repository의 검색 Flow는 취소에 협조하는 suspend/Flow 기반 API로 구현한다.
빈 입력의 결과도 명시해 화면이 이전 결과를 계속 보여주지 않게 한다.

취소된 요청의 오류를 최신 요청의 오류로 잘못 표시하지 않도록 취소 예외를 일반 오류와 구분한다.
입력 흐름과 결과 흐름의 수명은 화면 상태의 `stateIn` 정책으로 함께 관리한다.

이 연산자는 최신 입력만 유효한 경우에만 사용한다.
이전 결과도 모두 저장해야 하는 작업에는 취소가 손실을 만들 수 있다.
취소가 요구사항에 맞는지 작업의 도메인 의미를 먼저 확인한다.
검색과 자동완성처럼 최신 입력만 의미 있는 작업이 대표적인 적용 대상이다.
취소 가능한 호출과 오류 처리를 함께 설계해야 최신 결과 계약이 유지된다.
