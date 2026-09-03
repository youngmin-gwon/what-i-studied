---
title: xr-comfort-safety-performance
tags: ["android", "android/platforms"]
aliases: []
date modified: 2026-08-04 15:35:00 +09:00
date created: 2026-07-31 18:06:11 +09:00
---

## XR 품질은 성능, 편안함, 안전을 기능 요구사항으로 포함한다

상위 문서: [Android XR 계약](xr.md)

XR 에서 성능 문제는 단순히 프레임이 낮은 UI 문제가 아니다. 지연, 흔들림, 과도한 움직임, 잘못된 거리와 크기는 멀미, 피로, 조작 실패, 안전 문제로 이어질 수 있다.

### XR 프레임 레이트 및 Latency 허용 임계치

| Target Display Refresh Rate | Max Budget per Frame | Latency Tolerance | Motion Sickness Risk Signal |
| :--- | :--- | :--- | :--- |
| **90 Hz** | **11.1 ms** | `< 20 ms` end-to-end | Drop frames > 2 consecutive frames |
| **72 Hz** | **13.8 ms** | `< 25 ms` end-to-end | Unanchored camera motion / Jitter |

성능 프로파일링 시에는 Macrobenchmark를 활용하여 XR 환경의 프레임 타이밍(FrameTimingMetric)을 측정하고, 11.1ms 기준을 일관성 있게 지키는지 확인해야 한다.

```kotlin
@RunWith(AndroidJUnit4::class)
class XrPerformanceBenchmark {
    @get:Rule
    val benchmarkRule = MacrobenchmarkRule()

    @Test
    fun benchmarkXrFrameTiming() = benchmarkRule.measureRepeated(
        packageName = "com.example.xr.app",
        metrics = listOf(FrameTimingMetric()),
        compilationMode = CompilationMode.DEFAULT,
        iterations = 5,
        startupMode = StartupMode.WARM
    ) {
        pressHome()
        startActivityAndWait()
        // XR 환경 내 상호작용 및 공간 렌더링 부하 유발
        device.findObject(By.res("spatial_button")).click()
    }
}
```

### 실무 규칙

- rendering 은 공식 품질 기준의 90Hz 에서 프레임당 11.1ms 미만, 72Hz 에서 13.8ms 미만을 측정하고 latency, 3D asset, animation 비용을 함께 본다.
- panel 과 3D object 의 거리, 크기, 대비는 오래 보아도 피로하지 않게 정한다.
- 갑작스러운 camera movement, 강제 이동, 사용자를 둘러싼 UI 과밀 배치를 피한다.
- passthrough, scene understanding, anchor 같은 기능은 권한과 사생활 기대를 함께 검토한다.
- release 전에 실제 XR 기기 또는 공식 emulator 에서 입력, comfort, fallback 을 검증한다.

### 테스트 경계

emulator 는 space 전환, capability fallback, UI 와 입력 흐름의 반복 검증에 적합하지만 착용감, 멀미, tracking 품질, 광학 가독성, 발열과 배터리는 검증하지 못한다. comfort 와 장시간 성능은 지원하는 실제 기기에서 별도 통과시킨다.

### 관측 가능한 증거 (Observable Evidence)

```bash
# XR 렌더링 프레임 타임라인 덤프 (90Hz -> 11.1ms 기준 검증)
adb shell dumpsys gfxinfo <package_name> framestats

# 헤드 트래킹 Latency 및 Passthrough 프레임 드랍 센서 모니터링
adb logcat -v threadtime | grep -E "FrameTime|Jitter|PassthroughLatency"
```

### 관련 문서

- [Jetpack XR SDK는 preview 성숙도를 전제로 채택해야 한다](jetpack-xr-sdk-adoption.md)

공식 문서: [Android XR app quality](https://developer.android.com/docs/quality-guidelines/android-xr), [Create virtual XR devices](https://developer.android.com/develop/xr/jetpack-xr-sdk/run/create-avds/xr-headsets-glasses)

검증일: 2026-08-03. 수치 기준과 지원 emulator 종류는 출시 직전에 재확인한다.

