---
title: 07-jank-dropped-frames
tags: ["android", "android/foundations", "diagnostic-runbook"]
aliases: ["Runbook: jank and dropped frames"]
date modified: 2026-08-04 10:28:36 +09:00
date created: 2026-08-04 11:00:00 +09:00
---

## 화면이 끊긴다(jank, dropped frames)

### 증상

스크롤, 애니메이션, 화면 전환 중 프레임이 끊기거나 버벅거림이 느껴진다.

### 재현 조건

- 어떤 사용자 여정(스크롤, 특정 애니메이션, 화면 진입)이 느린지 먼저 정한다. "전반적으로 느리다"는 리포트는 그대로 조사할 수 없다.
- 같은 기기, 같은 빌드 타입(release 와 유사한 빌드), 같은 데이터 크기, 같은 입력(제스처 속도 등)으로 반복 재현한다. 디버그 빌드의 로그·검증 코드는 결과를 왜곡할 수 있다.

### 가능한 실패 경계와 우선순위

프레임 예산(60fps 기준 약 16ms, 90fps 약 11ms, 120fps 약 8ms)을 넘긴 프레임이 있다는 사실 하나가, 파이프라인의 여러 구간 중 어디서든 발생할 수 있다.

1. **UI thread(Compose composition/layout 또는 View measure/layout/draw)가 오래 걸린다.** 가장 흔한 원인 후보.
2. **RenderThread/GPU 작업이 오래 걸린다.** 무거운 이미지 디코딩, overdraw.
3. **`BufferQueue` 가 막혀 있다.** producer(앱)가 느린지 consumer(SurfaceFlinger)가 느린지 구분해야 한다.
4. **SurfaceFlinger/HWC 합성 자체가 느리다.** 레이어 수가 많거나 기기가 처리 못 하는 합성 조합.
5. **main thread 가 렌더링과 무관한 다른 작업(네트워크 콜백, 동기 I/O)으로 막혀 있다.** UI 작업 자체는 가벼운데 큐가 밀린 경우.

이 우선순위는 "recomposition 횟수가 많다" 같은 눈에 띄는 지표 하나만 보고 정하면 안 된다. trace 로 실제 시간이 어디서 소요됐는지 먼저 확인한다.

### 조사 절차

1. **어느 프레임이 예산을 넘겼는지 Perfetto trace 로 확인한다.**
   `Choreographer#doFrame` 구간 중 예산을 넘긴 프레임을 찾고, 그 프레임의 시간축에서 가장 긴 하위 구간을 본다.
   - 왜 이 필드를 보는가: 프레임 전체 길이만 봐서는 UI thread/RenderThread/GPU/합성 중 무엇이 원인인지 알 수 없다. 하위 구간별 길이가 다음 조사 방향을 결정한다.

2. **UI thread 구간이 길다면 recomposition(Compose) 또는 measure/layout(View) 범위를 본다.**
   Layout Inspector 나 컴파일러의 recomposition count 오버레이로 어떤 Composable 이 자주 재실행되는지 확인한다.
   - 주의: recomposition 횟수 자체는 정상적으로 자주 일어날 수 있다. 횟수가 많다는 사실이 아니라 **그 재실행이 무거운지**, **필요한 범위보다 넓은지**가 핵심이다. 상태를 상위 Composable 에서 읽고 있다면 하위로 옮겨 범위를 좁힌다.

3. **RenderThread/GPU 구간이 길다면 이미지·overdraw 를 의심한다.**
   Layout Inspector 의 overdraw 시각화나 Profiler 의 GPU 렌더링 프로파일로 확인한다.

4. **`dumpsys gfxinfo`로 프레임 통계 스냅샷을 확인한다.**
   ```bash
   adb shell dumpsys gfxinfo <pkg>
   ```
   최근 프레임들의 처리 시간 분포를 볼 수 있다. 대부분의 프레임이 예산 안에 있으면 정상 신호이고, janky(예산 초과) 프레임 비율이 두드러지게 높으면 실패 신호다. 스냅샷 하나만으로 원인을 설명할 수 없으므로 Perfetto trace 와 함께 해석한다.

5. **수정 후 반드시 동일 조건으로 재측정한다.**
   Macrobenchmark 의 프레임 타이밍 지표로 수정 전후를 비교한다. "코드를 바꿨다"는 사실이 아니라 실제 지표 변화로 개선을 판정한다. 프로파일러를 켠 상태의 수치는 오버헤드가 섞여 있으므로 방향을 찾는 용도로만 쓰고, 최종 판정은 별도로 측정한다.

### OS/API/target SDK 조건

- 프레임 예산은 기기의 refresh rate 에 따라 달라진다(60/90/120Hz). 재현 기기의 refresh rate 설정을 먼저 확인한다.
- Compose 의 상태 읽기 지연(defer reads) 관용구나 recomposition 최적화 API 는 사용 중인 Compose 컴파일러/런타임 버전에 따라 세부 동작이 달라질 수 있다.

### 다음 조사 경로

- 데이터 로딩이 UI thread 를 막고 있다면 → [Learning Spine 6장](../learning-spine/06-main-thread-binder-coroutine-and-durable-work-lifetime.md) 의 main thread/Binder 모델 확인
- 냉시작 직후의 jank 라면 → [app launch runbook](01-app-launch-slow-or-fails.md) 과 함께 조사
- 특정 기기·GPU 에서만 재현되면 → SurfaceFlinger/HWC 합성 조합 문제일 수 있으므로 기기별 실기기 검증으로 전환

### 관련 자료

- [Worked Example: Compose jank를 UI state에서 SurfaceFlinger까지 좁히는 사례](../worked-examples/07-compose-jank-from-ui-state-to-surfaceflinger.md)
- [Jank는 UI, RenderThread, SurfaceFlinger 전 구간의 frame deadline 실패다](../../01_system_internals/graphics-and-media/graphics-media-contracts/jank-is-frame-deadline-failure-across-ui-renderthread-and-surfaceflinger.md)
- [Compose 상태 읽기 위치는 recomposition 범위를 결정한다](../../02_app_framework/jetpack-compose/performance/compose-performance-contracts/compose-state-read-location-controls-recomposition-scope.md)
- [Profiler, Perfetto, dumpsys는 벤치마크가 아니라 진단 도구다](../../06_testing_performance/performance/performance-contracts/profiler-perfetto-dumpsys-are-diagnosis-tools-not-benchmarks.md)
- [Learning Spine 7장 입력, 리소스 선택과 화면 프레임](../learning-spine/07-input-resource-selection-and-display-frame.md)

### 공식 근거

- [Jetpack Compose performance](https://developer.android.com/develop/ui/compose/performance)
- [Inspect trace events with the System Trace app](https://developer.android.com/topic/performance/tracing)

검증일: 2026-08-04. 이 runbook 은 Learning Spine 7 장과 Worked Example 7 에서 이미 원문 대조를 마친 내용을 재사용했다.
