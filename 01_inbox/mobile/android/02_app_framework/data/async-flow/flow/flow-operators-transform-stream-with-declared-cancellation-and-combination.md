---
title: flow-operators-transform-stream-with-declared-cancellation-and-combination
tags: [android, android/async, android/data, android/flow]
aliases: ["Flow operator는 stream 변환과 취소 규칙을 드러낸다"]
date modified: 2026-08-04 14:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Flow operator 는 stream 변환과 취소 규칙을 드러낸다

Flow operator 는 값 목록을 편의상 가공하는 문법이 아니라 stream 의 변환, 결합, 취소 규칙을 선언하는 위치다. `map` 과 `filter` 는 각 값을 변환하거나 걸러내고, `combine` 은 여러 source 의 최신값을 묶고, `flatMapLatest` 는 새 입력이 오면 이전 작업을 취소한다.

검색어 입력처럼 최신 요청만 의미 있는 흐름에는 `flatMapLatest` 가 맞다. 사용자 정보와 설정처럼 서로 다른 source 의 최신 조합이 화면 상태를 만들면 `combine` 이 맞다.

operator 를 선택할 때는 "어떤 값이 필요한가"보다 "이전 작업을 유지할 것인가, 취소할 것인가, 여러 source 중 어느 시점의 값을 합칠 것인가"를 먼저 본다. 이 규칙이 화면 버그와 중복 요청을 줄인다.

```kotlin
query
    .debounce(300)
    .distinctUntilChanged()
    .flatMapLatest { keyword -> repository.search(keyword) } // 이전 검색을 취소
    .catch { emit(emptyList()) }
    .collect { results -> render(results) }
```

여기서 검색어가 빠르게 두 번 바뀌면, `flatMapLatest` 는 첫 번째 `repository.search(keyword)` 코루틴을 취소하고 두 번째 keyword 로 다시 매핑한다. 취소된 검색 내부의 suspend 지점은 `CancellationException` 을 받고 종료되므로, 먼저 시작된 느린 네트워크 응답이 나중에 도착해 최신 검색 결과를 덮어쓰는 일이 없다. 반대로 `flatMapConcat` 을 썼다면 두 번째 검색은 첫 번째가 끝날 때까지 시작조차 되지 않는다.

관련 노트: [flatMapLatest는 새 입력이 오면 이전 작업을 취소한다](../flow-state-contracts/flatmaplatest-cancels-obsolete-work-for-new-input.md), [combine은 여러 source의 최신값으로 화면 상태를 만든다](../flow-state-contracts/combine-builds-screen-state-from-latest-source-values.md)
