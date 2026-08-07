---
title: compose-side-effect
tags: [android, benchmark, compose, perfetto, pure-composable, recomposition, side-effect, SideEffect, system-ui]
aliases: [Compose Side Effect, Compose 부수 효과, SideEffect API]
date modified: 2026-08-07 18:35:12 +09:00
date created: 2026-08-07 16:10:00 +09:00
---

## Compose Side Effect (Jetpack Compose 부수 효과 원리 & SideEffect API)

### 1. 개요 (Overview)

**Compose Side Effect (부수 효과)** 는 Jetpack Compose 의 Composable 함수 내부에서 **[CS Side Effect](../../../../../computer-science/side-effect.md) 개념이 적용된 것으로, Composable 스코프 외부의 상태(State)를 변경하거나 시스템 I/O 작업을 수행하는 모든 동작**을 의미한다.

Composable 함수는 성능 최적화를 위해 재구성(Recomposition) 과정에서 언제든지, 임의의 순서로, 병렬 스레드에서 수차례 재실행되거나 중단될 수 있다([Composable Body Purity](../runtime/compose-runtime-contracts/composable-body-purity.md)). 따라서 Composable 본문 내부에서 직접 외부 변수를 수정하거나 상태를 조작하면 무한 재구성이나 상태 오염 버그가 발생한다.

---

#### 🚨 아키텍처 경고: UI 레이어에서 비즈니스 Analytics 호출은 안티패턴

- 비즈니스 로직(결제 완료, 로깅 등)을 UI Composable 안에서 직접 `analytics.logEvent()` 로 처리하는 것은 **UI 레이어에 도메인 로직이 침범하는 아키텍처 안티패턴**이다. (비즈니스 이벤트는 ViewModel/Repository 에서 처리되어야 한다.)
- 그렇다면 `SideEffect { … }` 는 왜 존재하는가? `SideEffect` 의 정당한 존재 이유는 **"Compose `State` 를 Compose 가 다루지 않는 안드로이드 OS 시스템 영역(상태바 색상)이나 레거시 뷰(Custom View/Canvas), 또는 Perfetto / Benchmark 렌더링 성능 관측 도구에 매 Composition 완료 직후 안전하게 동기화(Synchronize)하기 위함"**이다.

---

#### 초보자를 위한 쉽게 이해하는 비유

- **SideEffect API (무대 연출 완료 후 조명 기사의 상태바 스위치 조작 & 스톱워치 틱)**:
  - 연극 무대(UI Composable)의 연기가 무사히 다 끝난 직후(Composition Success), 건물 상단의 외부 상태바 조명(Android System Bar Color) 스위치를 매번 켜고 끄거나, 무대 연기 완료 순간을 성능 기록 스톱워치(Perfetto / Benchmark)에 틱(Tick)으로 기록하는 시스템 동기화 기사.

```mermaid
graph TD
    Recomposition["Composable 함수 재실행 (Recomposition)"] --> BodyExec["Composable 본문 순수 UI 트리 계산"]
    BodyExec --> CompositionSuccess["Composition 무사 완료 & 렌더링 트리 반영"]
    CompositionSuccess --> SideEffectAPI["SideEffect { ... } 블록 실행"]
    SideEffectAPI --> SystemSync["1. OS 시스템 상태바 아이콘 색상 동기화"]
    SideEffectAPI --> PerfettoSync["2. Perfetto / Benchmark 렌더링 프레임 틱 기록 (Trace.begin/endSection)"]
```

---

### 2. `SideEffect { … }` 의 정당한 3 대 실전 사용 사례

1. **안드로이드 OS 시스템 UI 상태바 / 네비게이션 바 동기화**:
   - Compose 의 `isDarkTheme` 스태이트가 변경되었을 때, 매 Composition 성공 완료 직후 안드로이드 OS 의 `WindowInsetsController` 시스템 상단 상태바(StatusBar) 아이콘 색상(다크/라이트)을 매핑 동기화할 때.
2. **Perfetto & Macrobenchmark 렌더링 성능 트레이싱 Metrics 관측**:
   - Composable 화면 렌더링 트리가 무사히 완성되어 렌더링을 끝마친 직후 `Trace.beginSection()` 과 `Trace.endSection()` 을 호출하거나, Perfetto / Macrobenchmark 성능 측정 도구에 프레임 완료 틱(Tick) 이벤트를 기록할 때.
3. **레거시 커스텀 Android View (Canvas / Map SDK) 속성 주입**:
   - `AndroidView` 로 래핑된 레거시 지도 뷰나 커스텀 C++ 캔버스의 내부 뷰 속성에 Compose `State` 변경을 매번 반영해 주어야 할 때.

---

### 3. 실전 코드 예시

#### 예시 1: `SideEffect` 기반 안드로이드 OS 시스템 상태바 색상 동기화

```kotlin
@Composable
fun SystemBarThemeSyncScreen(isDarkTheme: Boolean) {
    val view = LocalView.current

    // Composition 이 무사히 완료된 직후에만 안드로이드 OS 시스템 상태바 아이콘 색상 동기화
    SideEffect {
        val window = (view.context as Activity).window
        val insetsController = WindowCompat.getInsetsController(window, view)
        insetsController.isAppearanceLightStatusBars = !isDarkTheme
    }

    Text(text = "현재 테마: ${if (isDarkTheme) "다크 모드" else "라이트 모드"}")
}
```

#### 예시 2: `SideEffect` 기반 Perfetto & Macrobenchmark 렌더링 성능 Metrics 관측

```kotlin
import androidx.tracing.trace

@Composable
fun MetricTracedFeedScreen(feedState: FeedUiState) {
    // 렌더링 트리가 무사히 완성된 직후 Perfetto / Benchmark 툴에 렌더링 완료 틱 기록
    SideEffect {
        trace("FeedScreen:CompositionCompleted") {
            // Perfetto 트레이스 뷰어 및 Macrobenchmark 렌더링 메트릭 리포트에 전송
            android.os.Trace.setCounter("FeedItemsCount", feedState.items.size.toLong())
        }
    }

    LazyColumn {
        items(feedState.items) { item ->
            FeedCard(item)
        }
    }
}
```

---

### 4. 연결 문서 (Related Links)

- [compose-effect-api-selection](compose-state-and-effect-contracts/compose-effect-api-selection.md) - 상황별 Effect API 선택 가이드 결정 트리
- [CS Side Effect](../../../../../computer-science/side-effect.md) - 소프트웨어 공학 부수 효과 원자 노드
- [compose-state-and-effect-contracts](compose-state-and-effect-contracts/compose-state-and-effect-contracts.md) - Compose 이펙트 규약 통합 인덱스
- [launched-effect](compose-state-and-effect-contracts/launched-effect.md) - 비동기 취소 가능 이펙트
- [disposable-effect](compose-state-and-effect-contracts/disposable-effect.md) - 자원 해제 정리 이펙트
- [Composable Body Purity](../runtime/compose-runtime-contracts/composable-body-purity.md) - Composable 함수 순수성 규칙
