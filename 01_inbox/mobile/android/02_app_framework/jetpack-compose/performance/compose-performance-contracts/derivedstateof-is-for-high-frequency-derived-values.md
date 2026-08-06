---
title: derivedstateof-is-for-high-frequency-derived-values
tags: [android, compose/performance, jetpack-compose]
aliases: []
date modified: 2026-08-06 14:48:00 +09:00
date created: 2026-08-03 16:59:23 +09:00
---

## derivedStateOf는 고빈도 입력에서 저빈도 결과를 만들 때 쓴다

`derivedStateOf`의 내부 동작은 snapshot state가 바뀔 때 파생 값을 다시 계산하고, 결과가 이전과 다를 때 그 파생 state의 소비자를 무효화하는 것이다. 일반 계산 캐시가 아니라 입력 변경 빈도와 UI가 필요한 결과 변경 빈도 사이에 경계를 만든다.

```kotlin
@Composable
fun Messages(messages: List<Message>) {
    val listState = rememberLazyListState()
    val showScrollToTop by remember(listState) {
        derivedStateOf { listState.firstVisibleItemIndex > 0 }
    }

    Box {
        LazyColumn(state = listState) {
            items(messages, key = { it.id }) { MessageRow(it) }
        }
        AnimatedVisibility(showScrollToTop) {
            ScrollToTopButton()
        }
    }
}
```

`firstVisibleItemIndex`와 offset은 스크롤 중 자주 변하지만 `showScrollToTop`은 0번 항목 경계를 넘을 때만 바뀐다. 이때 파생 state를 읽는 `AnimatedVisibility`의 무효화 빈도를 줄일 수 있다.

반대로 다음은 결과가 입력마다 바뀌므로 이점이 없다.

```kotlin
val fullName by remember(firstName, lastName) {
    derivedStateOf { "$firstName $lastName" }
}
```

단순 문자열은 composition에서 계산하면 된다. `derivedStateOf`에도 state 객체·dependency 추적 비용이 있다.

관찰 증거는 도입 전후 Layout Inspector의 recomposition count와 Macrobenchmark frame timing이다. 같은 스크롤 동작으로 비교하고, count가 줄어도 사용자 metric이 같고 코드만 복잡해졌다면 유지할 근거가 약하다.

관련 노트: [Compose 상태 읽기 위치는 다시 실행할 phase와 범위를 결정한다](./compose-state-read-location-controls-recomposition-scope.md), [Compose 성능 최적화는 측정·진단·개선 순환으로 진행한다](./compose-performance-starts-with-measure-debug-improve-loop.md)

출처: [Compose side effects와 derivedStateOf](https://developer.android.com/develop/ui/compose/side-effects#derivedstateof)
