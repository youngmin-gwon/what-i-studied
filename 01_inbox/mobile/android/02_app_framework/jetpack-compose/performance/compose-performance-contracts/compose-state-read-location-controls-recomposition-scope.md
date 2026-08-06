---
title: compose-state-read-location-controls-[recomposition](../../runtime/recomposition.md)-scope
tags: [android, compose/performance, jetpack-compose]
aliases: []
date modified: 2026-08-06 14:48:00 +09:00
date created: 2026-08-03 16:59:23 +09:00
---

## Compose 상태 읽기 위치는 다시 실행할 phase와 범위를 결정한다

무효화 메커니즘에서 Compose Runtime은 snapshot state를 어느 restart scope 또는 modifier phase에서 읽었는지 추적한다. 자주 바뀌는 값을 상위 composition에서 읽으면 그 범위가 무효화된다. layout lambda나 draw lambda까지 읽기를 늦추면 composition을 건너뛸 수 있지만 해당 phase의 작업은 여전히 발생한다.

composition에서 scroll 값을 읽는 예다.

```kotlin
@Composable
fun MovingTitle(listState: LazyListState) {
    val y = listState.firstVisibleItemScrollOffset // composition read
    Text("목록", Modifier.offset(y = y.dp))
}
```

pixel offset처럼 layout에만 필요한 값은 lambda overload에서 읽을 수 있다.

```kotlin
@Composable
fun MovingTitle(listState: LazyListState) {
    Text(
        "목록",
        Modifier.offset {
            IntOffset(x = 0, y = listState.firstVisibleItemScrollOffset)
        },
    )
}
```

두 번째 코드는 state read를 placement까지 지연한다. 스크롤 때 composition을 다시 실행하지 않아도 되지만 placement는 다시 일어날 수 있다. `graphicsLayer { translationY = ... }`처럼 draw 단계에서 읽는 선택도 결과와 hit testing 요구에 맞아야 한다.

```text
composition read -> recomposition + 필요한 후속 phase
layout read      -> layout/placement + draw
draw read        -> draw
```

Layout Inspector에서 대상 Composable의 recomposition count를 스크롤 전후 비교하고, Perfetto frame에서 layout/draw 비용이 새 병목이 되지 않았는지 확인한다. 읽기를 늦추기 위한 lambda가 동작 의미를 숨기거나 좌표·접근성 bounds를 틀리게 만들면 적용하지 않는다.

관련 노트: [Compose 성능 최적화는 측정·진단·개선 순환으로 진행한다](./compose-performance-starts-with-measure-debug-improve-loop.md), [`derivedStateOf`는 고빈도 입력에서 저빈도 결과를 만들 때 쓴다](./derivedstateof-is-for-high-frequency-derived-values.md)

출처: [Compose phase별 상태 읽기](https://developer.android.com/develop/ui/compose/phases), [상태 읽기를 늦추는 성능 지침](https://developer.android.com/develop/ui/compose/performance/bestpractices#defer-reads)
