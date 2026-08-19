---
title: 07-compose-jank-from-ui-state-to-surfaceflinger
tags: ["android", "android/foundations", "worked-example"]
aliases: ["Narrowing Compose jank from UI state to SurfaceFlinger"]
date modified: 2026-08-04 16:10:00 +09:00
date created: 2026-08-04 03:10:00 +09:00
---

## Compose jank 를 UI state 에서 SurfaceFlinger 까지 좁히는 사례

이 예시는 Learning Spine 7·11 장을 하나의 성능 진단 분석으로 잇는다. 7 장에서 다룬 "입력 → UI 상태 → 그리기 명령(DisplayList) → BufferQueue → SurfaceFlinger/HWC" 라는 렌더링 파이프라인 전체를 시간축(Time-series Trace)에서 추적하여, 11 장의 "질문에 맞는 진단 도구를 고르고 프레임 예산을 정량적으로 증명한다"는 방법론으로 렌더링 병목(Jank)의 정확한 원인을 추적한다.

### 시작 상태

상품 목록 화면(`LazyColumn`)에서 사용자가 스크롤 제스처를 수행할 때 화면이 간헐적으로 끊긴다는 QA 리포트가 접수되었다.

### 입력

동일한 테스트 기기, 동일한 릴리스 빌드, 동일한 데이터 세트 환경에서 고정된 속도의 스크롤 제스처를 반복 수행하여 프레임 드롭 재현 조건을 고정한다(11 장의 "재현 조건 고정" 원칙).

---

### 다계층 실행 흐름 (UI → App Framework → System Server → Kernel)

1. **UI Thread Phase (Compose 3-Phase Pipeline: Composition → Layout → Draw)**
   - VSync-app 신호가 도착하면 `Choreographer.doFrame()` 이 실행되고 UI Thread 에서 Compose 프레임 렌더링이 시작된다.
   - **Composition Phase**: UI 상태(`State<T>`) 변화를 감지하여 영향을 받는 `RecompositionScope` 들을 재실행한다. 상태 읽기(State Read)가 상위 Composable Scope 에서 일어나면 스크롤 시 매 프레임 상위 전체가 Recompose 되면서 UI Thread 예산(60Hz 기준 16.6ms, 120Hz 기준 8.3ms)을 초과한다.
   - **Layout & Draw Phase**: Layout 노드들의 크기/위치를 측정(`Measure`/`Layout`)하고 DisplayList 그리기 명령을 생성하여 RenderThread 로 파이프라인을 넘긴다.

2. **App Framework & RenderThread Phase (Hardware Acceleration & Canvas Commands)**
   - UI Thread 가 완료되면 RenderThread 가 수신받은 DisplayList 그리기 명령을 GPU 렌더링 명령(Skia / Impeller / Vulkan)으로 변환한다.
   - 텍스트 셰이더 빌드, 대용량 비트맵 디코딩, Overdraw 비트맵 합성 등이 일어나는 경우 RenderThread 가 병목이 되어 VSync deadline 을 놓치게 된다.

3. **System Server & IPC Layer (BufferQueue & SurfaceFlinger Composition)**
   - RenderThread 가 렌더링을 마친 GraphicBuffer 를 [binder ipc](../../01_system_internals/binder-ipc.md) (`IGraphicBufferProducer`)를 통해 `BufferQueue` 에 `queueBuffer` 한다.
   - VSync-sf 신호가 도착하면 `SurfaceFlinger` 가 consumer 로서 `dequeueBuffer` / `acquireBuffer` 수행 후 앱의 Surface 와 다른 시스템 UI Surface(StatusBar, NavigationBar)를 레이어 합성한다.
   - UI Thread 나 RenderThread 의 대기가 길어져 VSync-sf 시점에 큐에 준비된 버퍼가 없으면, SurfaceFlinger 는 이전 프레임을 재사용하여 화면 스태터(Jank / Stutter)가 발생한다.

4. **Kernel & Hardware Layer (VSync Display Controller & HWC)**
   - Hardware Composer (HWC) 가 GPU 합성(GLES Composition) 대신 하드웨어 오버레이 레이어로 최종 패널에 프레임을 출력한다.
   - 시간축에서 `frameOverrunMs` 값이 양수(+)로 측정되는 프레임은 하드웨어 VSync 디스플레이 타임라인 예산을 이탈한 Jank 프레임으로 기록된다.

---

### 성공 결과 vs 실패 분기 비교

| 평가 항목 | 성공 경로 (State Read Deferral to Draw Phase) | 실패 분기 (Unscoped Composition Phase Read) |
| :--- | :--- | :--- |
| **Compose Phase** | Draw Phase 로 상태 읽기 지연 (`graphicsLayer { alpha = ... }`) | Composition Phase 에서 상태 읽기 (`alpha = state.value`) |
| **[recomposition](../../02_app_framework/jetpack-compose/runtime/recomposition.md) Scope** | 스크롤 시 Recomposition 0 회 (Composition/Layout 단계 건너뜀) | 스크롤 시 `LazyColumn` 및 모든 child 노드 매 프레임 Recomposition |
| **UI Thread 시간** | `Choreographer#doFrame` duration < 2.0ms | `Choreographer#doFrame` duration > 16.6ms (VSync 예산 초과) |
| **`frameOverrunMs`** | 음수 (-) 값 유지 (충분한 프레임 헤드룸 확보) | 양수 (+) 값 발생 (Jank / Frame Missed) |
| **SurfaceFlinger 상태** | `BufferQueue` 에 매 VSync 마다 새 버퍼 래치 완료 | `BufferQueue` 버퍼 부족으로 이전 프레임 latch (Frame Drop) |

---

### 관찰 가능한 신호 및 CLI 진단 명령

1. **Macrobenchmark `FrameTimingMetric` & `frameOverrunMs` 측정**
   - Macrobenchmark 결과 JSON 및 Perfetto Trace 에서 `frameOverrunMs` 지표를 관찰한다.
   - `frameOverrunMs > 0`: VSync 마감 시간을 넘겨 Jank 가 발생함.
   - `frameOverrunMs <= 0`: 마감 시간 내에 정상 렌더링 완료.

2. **`dumpsys gfxinfo` 정량 분석**
   ```bash
   # 프레임 타임라인 스냅샷 및 95th/99th percentile Janky Frames 비율 확인
   adb shell dumpsys gfxinfo com.example.shopapp framestats

   # HWUI Profile 활성화 후 프레임 렌더링 파이프라인 단계별 시간 관찰
   adb shell setprop debug.hwui.profile true
   ```

3. **Perfetto CLI System Tracing 캡처**
   ```bash
   # Compose 3-phase 및 Choreographer trace point 캡처
   adb shell perfetto \
     -c - --txt \
     -o /data/misc/perfetto-traces/compose_jank_trace.perfetto-trace <<EOF
   buffers: { size_kb: 32768 }
   data_sources: {
       config {
           name: "android.trace_view"
       }
   }
   data_sources: {
       config {
           name: "linux.ftrace"
           ftrace_config {
               atrace_categories: "gfx"
               atrace_categories: "view"
               atrace_categories: "dalvik"
           }
       }
   }
   duration_ms: 10000
   EOF
   ```

4. **Compose Layout Inspector & Compiler Tracing**
   - Android Studio Layout Inspector 에서 Recomposition Count 오버레이를 통해 스크롤 시 숫자가 급증하는 Composable 노드 검출.

---

### Android 14 / 15 / 16 특화 동작

- **Macrobenchmark `frameOverrunMs` Metric (Android 14+)**: Android 14 이상 Macrobenchmark 에서는 기존 `frameDurationCpuMs` 외에도 `frameOverrunMs` 가 핵심 지표로 제공된다. `frameOverrunMs` 는 프로세스가 하드웨어 디스플레이 렌더링 마감 시한(VSync Deadline)을 몇 ms 만큼 초과했는지 직관적인 음수/양수 값으로 정량화해준다.
- **Compose Strong Skipping Mode (Kotlin 2.0+ / Compose 1.7+)**: Kotlin 2.0+ 기본 설정인 Strong Skipping Mode 환경에서는 unstable 파라미터가 포함된 Composable 도 인스턴스 동일성이 유지되면 skipping 되지만, **Composable 함수 바디 내부에서 State.value 를 직접 읽는 구조**는 skipping 대상이 되지 못하고 Recompose 가 강제 트리거된다.
- **Draw Phase Deferral via `Modifier.graphicsLayer`**: alpha, translation, scale 등 시각적 변환 상태는 `Modifier.graphicsLayer { alpha = scrollState.value }` 형태의 lambda 블록을 통해 Draw Phase 로 상태 읽기를 지연시켜 Composition 및 Layout 단계를 완전히 우회(Bypass)할 수 있다.

---

### 코드 예시

```kotlin
// 1. [나쁜 예시]: Composition Phase에서 스크롤 상태 읽기
// scrollState가 변경될 때마다 ItemRow 및 하위 모든 Composable이 Recomposition & Layout을 재수행함
@Composable
fun BadItemRow(scrollState: ScrollState) {
    val alpha = remember { derivedStateOf { 1f - (scrollState.value / 1000f) } }
    
    Row(
        modifier = Modifier
            .fillMaxWidth()
            .alpha(alpha.value) // Composition Phase에서 alpha.value 상태를 읽음 -> Recomposition 발생!
            .padding(16.dp)
    ) {
        Text("Product Title", style = MaterialTheme.typography.bodyLarge)
    }
}

// 2. [최적화 예시]: Draw Phase로 State Read 지연 (State Read Deferral)
// lambda 블록 내부로 state read를 지연시켜 Composition & Layout 단계를 우회하고 Draw 단계만 재실행함
@Composable
fun OptimizedItemRow(scrollStateProvider: () -> Int) {
    Row(
        modifier = Modifier
            .fillMaxWidth()
            .graphicsLayer {
                // Draw Phase 스코프 안에서만 상태를 읽음
                // Recomposition 및 Layout 없이 RenderThread DisplayList 속성만 업데이트됨
                alpha = 1f - (scrollStateProvider() / 1000f)
            }
            .padding(16.dp)
    ) {
        Text("Product Title", style = MaterialTheme.typography.bodyLarge)
    }
}
```

```kotlin
// 3. Macrobenchmark를 통한 frameOverrunMs 정량 측정 테스트 코드
@RunWith(AndroidJUnit4::class)
class ScrollWatermarkBenchmark {
    @get:Rule
    val benchmarkRule = MacrobenchmarkRule()

    @Test
    fun scrollListCompilationNone() = benchmarkRule.measureRepeated(
        packageName = "com.example.shopapp",
        metrics = listOf(FrameTimingMetric()), // frameOverrunMs 포함 지표
        compilationMode = CompilationMode.None(),
        iterations = 5,
        setupBlock = { pressHome() }
    ) {
        startActivityAndWait()
        val lazyColumn = device.findObject(By.res("product_list"))
        lazyColumn.setGestureMargin(device.displayWidth / 5)
        lazyColumn.fling(Direction.DOWN)
    }
}
```

---

### 관련 Diagnostic Runbook

- [07-jank-dropped-frames.md](../diagnostic-runbooks/07-jank-dropped-frames.md)

### 관련 Learning Spine 장

- [7장 입력, 리소스 선택과 화면 프레임](../learning-spine/07-input-resource-selection-and-display-frame.md)
- [11장 관찰, 테스트와 품질 feedback](../learning-spine/11-observation-testing-and-quality-feedback.md)

### 관련 원자 노트

- [Jank는 UI, RenderThread, SurfaceFlinger 전 구간의 frame deadline 실패다](../../01_system_internals/graphics-and-media/graphics-media/jank-is-frame-deadline-failure-across-ui-renderthread-and-surfaceflinger.md)
- [VSync와 Choreographer는 frame deadline을 정의한다](../../01_system_internals/graphics-and-media/graphics-media/vsync-and-choreographer-define-frame-deadline.md)
- [Compose 상태 읽기 위치는 recomposition 범위를 결정한다](../../02_app_framework/jetpack-compose/performance/compose-performance/compose-state-read-location-controls-recomposition-scope.md)
- [Recomposition은 전체 UI 재그리가 아니라 필요한 Composable scope 재실행이다](../../02_app_framework/jetpack-compose/runtime/compose-runtime/recomposition-scope-control.md)
- [Compose 성능 최적화는 measure, debug, improve 순환으로 진행한다](../../02_app_framework/jetpack-compose/performance/compose-performance/compose-performance-starts-with-measure-debug-improve-loop.md)
- [Profiler, Perfetto, dumpsys는 벤치마크가 아니라 진단 도구다](../../06_testing_performance/performance/performance/profiler-perfetto-dumpsys-are-diagnosis-tools-not-benchmarks.md)

### 공식 근거

- [Jetpack Compose performance](https://developer.android.com/develop/ui/compose/performance)
- [Compose performance best practices: defer reads](https://developer.android.com/develop/ui/compose/performance/bestpractices#defer-reads)
- [Inspect trace events with the System Trace app](https://developer.android.com/topic/performance/tracing)
- [Macrobenchmark FrameTimingMetric](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-metrics#frametimingmetric)

검증일: 2026-08-04. 이 예시는 Learning Spine 7·11 장 및 Compose 1.7+/Android 14 frameOverrunMs specs 원문 대조를 마쳤다.
