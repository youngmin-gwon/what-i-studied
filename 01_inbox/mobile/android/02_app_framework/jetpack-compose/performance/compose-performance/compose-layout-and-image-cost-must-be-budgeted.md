---
title: compose-layout-and-image-cost-must-be-budgeted
tags: [android, compose/performance, jetpack-compose]
aliases: []
date modified: 2026-08-06 14:48:00 +09:00
date created: 2026-08-03 16:59:23 +09:00
---

## Compose layout과 image 비용은 프레임 예산 안에서 관리한다

Compose의 한 프레임도 composition, measure, layout, draw를 거친다. Lazy container는 보이지 않는 항목 구성을 줄이지만, 잘못된 key·content type, 반복되는 복잡한 측정, 큰 bitmap decode 비용까지 없애지는 않는다.

```kotlin
@Composable
fun PhotoFeed(items: List<FeedItem>) {
    LazyColumn {
        items(
            items = items,
            key = { it.id },
            contentType = { it.kind },
        ) { item ->
            PhotoRow(
                item = item,
                modifier = Modifier
                    .fillParentMaxWidth()
                    .heightIn(min = 96.dp),
            )
        }
    }
}
```

재사용 메커니즘에서 stable key는 순서가 바뀌어도 item identity와 state를 연결한다. `contentType`은 호환되는 item끼리 composition 재사용 기회를 높인다. 둘 다 실제 측정 비용이 큰 `PhotoRow`를 자동으로 싸게 만들지는 않는다.

이미지 loader에는 화면에 필요한 pixel 크기에 가까운 decode 요청을 전달한다. 96dp thumbnail을 원본 해상도로 decode하면 heap과 decode 시간이 늘어난다. placeholder와 성공 이미지의 aspect ratio를 같게 두면 로드 완료 때 불필요한 재측정을 줄일 수 있다. 반복 clipping, shadow, offscreen alpha도 draw·GPU 비용으로 추적한다.

관찰 흐름은 다음과 같다.

```text
Macrobenchmark FrameTimingMetric에서 느린 스크롤 확인
  -> Perfetto frame timeline에서 UI/RenderThread 구간 확인
  -> Layout Inspector로 recomposition·layout 구조 확인
  -> 한 가지 변경 후 같은 release 빌드와 여정으로 재측정
```

Developer Options의 막대 하나를 Compose measure/layout/draw 시간으로 해석하지 않는다. 60Hz의 16.67ms도 모든 기기의 고정 기준이 아니다. refresh rate와 frame deadline을 포함한 trace·benchmark 결과를 증거로 사용한다.

관련 노트: [Compose 성능 최적화는 측정·진단·개선 순환으로 진행한다](./compose-performance-starts-with-measure-debug-improve-loop.md), [렌더링 성능은 프레임 지연의 원인을 분리한다](../../../../06_testing_performance/performance/performance/rendering-jank-is-frame-deadline-failure.md)

출처: [Compose lazy list 성능](https://developer.android.com/develop/ui/compose/lists#performance), [Compose 성능](https://developer.android.com/develop/ui/compose/performance)
