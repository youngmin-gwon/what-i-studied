---
title: Compose jank를 UI state에서 SurfaceFlinger까지 좁히는 사례
tags: ["android", "android/foundations", "worked-example"]
aliases: ["Narrowing Compose jank from UI state to SurfaceFlinger"]
date modified: 2026-08-04 03:10:00 +09:00
date created: 2026-08-04 03:10:00 +09:00
---

## Compose jank를 UI state에서 SurfaceFlinger까지 좁히는 사례

이 예시는 Learning Spine 7·11장을 하나의 진단 과정으로 잇는다. 7장에서 다룬 "입력 → UI 상태 → 그리기 명령 → Surface → SurfaceFlinger"라는 파이프라인 전체를 시간축에서 훑어, 11장에서 다룬 "질문에 맞는 도구를 고른다"는 방법론으로 병목을 하나씩 좁힌다.

### 시작 상태

목록 화면(`LazyColumn`)이 있고, QA가 "빠르게 스크롤하면 화면이 끊긴다"고 리포트했다.

### 입력

같은 기기, 같은 빌드, 같은 목록 데이터로 빠른 스크롤 제스처를 반복한다(11장의 "재현 조건 고정" 원칙).

### 단계별 흐름

1. **회귀 여부와 재현 조건 고정(11장)**: 먼저 이 문제가 최근 변경으로 새로 생겼는지, 특정 기기·데이터 크기에서만 나타나는지 확인한다. 빌드 타입, 기기 모델, 목록 아이템 수, 냉시작/온시작 조건을 고정해 여러 번 반복 재현한다.
2. **어느 프레임이 예산을 놓쳤는지 확인(7장 파이프라인)**: Perfetto trace를 열어 `Choreographer#doFrame` 구간 중 예산(예: 60fps 기준 약 16ms)을 넘긴 프레임을 찾는다. 그 프레임의 시간축에서 가장 긴 구간이 파이프라인의 어느 단계에 있는지 본다 — UI thread의 composition/layout/draw인지, RenderThread인지, GPU 작업인지, BufferQueue의 대기인지, SurfaceFlinger/HWC의 합성인지.
3. **원인이 UI thread라면 recomposition 범위를 의심한다**: trace가 `Composition`/`Layout` 구간에서 시간을 많이 쓴다면, 다음 질문은 "recomposition이 몇 번 일어났는가"가 아니라 "그 recomposition이 실제로 필요한 범위보다 넓은가"다. Recomposition 자체는 자주 일어날 수 있는 정상 동작이며, 횟수만으로 버그라고 단정하지 않는다.
4. **상태 읽기 위치를 확인한다**: 리스트 아이템의 선택 상태 같은 값을 `LazyColumn`을 감싼 상위 Composable에서 읽고 있다면, 아이템 하나의 선택이 바뀔 때마다 목록 전체가 다시 실행될 수 있다. 상태를 실제로 필요한 하위 Composable(아이템 자신) 가까이로 옮기면 변경 범위가 좁아진다.
5. **원인이 UI thread가 아니라면 다른 구간을 본다**: RenderThread/GPU 구간이 길면 이미지 디코딩 비용이나 overdraw를 의심한다. `BufferQueue`가 자주 막혀 있으면 producer(앱)와 consumer(SurfaceFlinger) 중 어느 쪽이 느린지 구분한다. SurfaceFlinger/HWC 구간이 길면 레이어 수나 기기가 처리할 수 없는 합성 조합을 의심한다.
6. **수정 후 같은 조건에서 재측정(11장)**: 코드를 바꾼 뒤에는 Macrobenchmark나 동일한 Perfetto 캡처 절차로 같은 스크롤 시나리오를 다시 측정한다. "코드를 바꿨다"는 사실이 아니라 프레임 드롭 비율의 실제 변화가 개선을 판정하는 기준이다.

### 성공 결과

상태 읽기 위치를 목록 아이템 레벨로 낮춘 뒤 다시 측정하면, 선택 상태가 바뀔 때 recomposition 범위가 해당 아이템으로 좁아지고, 같은 스크롤 시나리오에서 프레임 예산을 넘기는 비율이 줄어든다.

### 관찰 가능한 신호

- Perfetto trace의 `Choreographer#doFrame` 구간과 그 하위의 UI thread/RenderThread/GPU 구간 길이.
- Android Studio Layout Inspector 또는 Compose 컴파일러의 recomposition count 오버레이로 어떤 Composable이 얼마나 자주 재실행되는지 확인한다(횟수 자체가 아니라 그 실행이 무거운지가 핵심).
- `adb shell dumpsys gfxinfo <pkg>`로 프레임 통계 스냅샷을 확인한다.
- Macrobenchmark의 프레임 타이밍 지표로 수정 전후를 같은 조건에서 비교한다.

### 실패 분기: recomposition 횟수만 보고 잘못 진단한다

1. 개발자가 recomposition count 오버레이에서 목록 아이템들이 자주 다시 실행되는 것을 본다.
2. "recomposition이 너무 많다"고 결론짓고, 무작정 여러 곳에 `remember`를 추가하거나 상태를 상위로 끌어올려 업데이트 빈도를 줄이려 시도한다.
3. 그러나 실제로는 각 recomposition이 가벼운 작업(텍스트 색상 변경 하나)이었고, 진짜 프레임 드롭의 원인은 별도 구간(예: 매 프레임 다시 디코딩되는 이미지)에 있었다.
4. recomposition 횟수를 줄이는 처방은 증상과 무관했으므로 스크롤 jank는 그대로 남는다.

이 실패가 보여주는 것은, trace로 실제 병목 구간을 먼저 확인하지 않고 눈에 보이는 지표(recomposition count) 하나만 보고 처방을 정하면 원인과 무관한 곳을 고치게 된다는 것이다. 7장의 파이프라인 모델은 "UI thread가 느린가, 그 아래가 느린가"를 먼저 나누라고 요구하고, 11장의 방법론은 그 판단을 trace라는 시간축 증거로 하라고 요구한다.

### 코드 예시

```kotlin
// 나쁜 예: 선택 상태를 상위에서 읽어 목록 전체 recomposition 범위를 넓힌다.
@Composable
fun ItemList(items: List<Item>, selectedId: String?) {
    LazyColumn {
        items(items) { item ->
            // selectedId가 상위에서 값으로 전달되어, 값이 바뀔 때마다 ItemList 전체가 재구성된다.
            ItemRow(item, isSelected = item.id == selectedId)
        }
    }
}

// 나은 예: 선택 여부 판정을 아이템 자신의 범위로 내린다.
@Composable
fun ItemList(items: List<Item>, selectedId: State<String?>) {
    LazyColumn {
        items(items, key = { it.id }) { item ->
            ItemRow(item, isSelectedProvider = { item.id == selectedId.value })
        }
    }
}

@Composable
fun ItemRow(item: Item, isSelectedProvider: () -> Boolean) {
    val isSelected = isSelectedProvider() // 이 Composable 범위에서만 상태를 읽는다.
    Text(item.title, color = if (isSelected) SelectedColor else DefaultColor)
}
```

### 관련 원자 노트

- [Jank는 UI, RenderThread, SurfaceFlinger 전 구간의 frame deadline 실패다](../../01_system_internals/graphics-and-media/graphics-media-contracts/jank-is-frame-deadline-failure-across-ui-renderthread-and-surfaceflinger.md)
- [VSync와 Choreographer는 frame deadline을 정의한다](../../01_system_internals/graphics-and-media/graphics-media-contracts/vsync-and-choreographer-define-frame-deadline.md)
- [Compose 상태 읽기 위치는 recomposition 범위를 결정한다](../../02_app_framework/jetpack-compose/performance/compose-performance-contracts/compose-state-read-location-controls-recomposition-scope.md)
- [Recomposition은 전체 UI 재그리가 아니라 필요한 Composable scope 재실행이다](../../02_app_framework/jetpack-compose/runtime/compose-runtime-contracts/recomposition-reruns-needed-composable-scopes-not-the-whole-ui.md)
- [Compose 성능 최적화는 measure, debug, improve 순환으로 진행한다](../../02_app_framework/jetpack-compose/performance/compose-performance-contracts/compose-performance-starts-with-measure-debug-improve-loop.md)
- [Profiler, Perfetto, dumpsys는 벤치마크가 아니라 진단 도구다](../../06_testing_performance/performance/performance-contracts/profiler-perfetto-dumpsys-are-diagnosis-tools-not-benchmarks.md)

### 관련 Learning Spine 장

- [7장 입력, 리소스 선택과 화면 프레임](../learning-spine/07-input-resource-selection-and-display-frame.md)
- [11장 관찰, 테스트와 품질 feedback](../learning-spine/11-observation-testing-and-quality-feedback.md)

### 공식 근거

- [Jetpack Compose performance](https://developer.android.com/develop/ui/compose/performance)
- [Compose performance best practices: defer reads](https://developer.android.com/develop/ui/compose/performance/bestpractices#defer-reads)
- [Inspect trace events with the System Trace app](https://developer.android.com/topic/performance/tracing)

검증일: 2026-08-04. 이 예시는 7·11장에서 이미 원문 대조를 마친 렌더링 파이프라인·진단 도구 원자 노트를 재사용했다.
