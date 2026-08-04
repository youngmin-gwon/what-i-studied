---
title: "Android 성능, 품질, 빌드 최적화 지도"
tags: ["android", "android/testing-performance"]
aliases: ["android-performance-quality-and-build-optimization"]
date created: 2026-07-31 17:32:53 +09:00
date modified: 2026-08-04 14:58:55 +09:00
---

## Android 성능, 품질, 빌드 최적화 지도

이 지도는 Android 앱 품질을 한 덩어리로 보지 않고 사용자 성능, 반복 가능한 측정, 테스트 피드백, 진단 도구, 배포 산출물 최적화로 분리한다.

### 품질 및 성능 체계도

```mermaid
flowchart TD
    AppQuality["Android 앱 품질 & 성능 체계"]
    
    AppQuality --> RuntimePerf["런타임 성능 계약<br/>(Startup, Jank, Memory, Main Thread)"]
    AppQuality --> BenchmarkBP["Benchmark & Baseline Profile 계약<br/>(Macrobenchmark, Baseline Profile)"]
    AppQuality --> TestQuality["테스트 품질 계약<br/>(Unit, Integration, Compose UI, Screenshot)"]
    AppQuality --> DebugTools["디버깅 도구 계약<br/>(Logcat, ANR Trace, ADB, Debugger)"]
    AppQuality --> BuildOpt["R8 & Gradle 빌드 최적화 계약<br/>(Keep Rules, Tree Shaking, Dex)"]

    RuntimePerf --> BenchmarkBP
    BenchmarkBP --> TestQuality
    DebugTools --> RuntimePerf
    BuildOpt --> RuntimePerf
```

## 정본 노트

- [런타임 성능 계약](./performance-contracts/performance-contracts.md)
- [Benchmark와 Baseline Profile 계약](./benchmark-baseline-contracts/benchmark-baseline-contracts.md)
- [Compose 성능 계약](../../02_app_framework/jetpack-compose/performance/compose-performance-contracts/compose-performance-contracts.md)
- [테스트 품질 계약](../testing/testing-quality-contracts/testing-quality-contracts.md)
- [디버깅 도구 계약](../debugging/debugging-contracts/debugging-contracts.md)
- [R8와 Gradle 빌드 최적화 계약](../../03_packaging_deployment/optimization/build-optimization-contracts/build-optimization-contracts.md)

