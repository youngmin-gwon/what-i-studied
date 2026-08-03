---
title: profile-guided-compilation-splits-install-runtime-and-idle-costs
tags: [android, android/boot-runtime, android/runtime, android/system-internals]
aliases: ["Profile guided compilation은 설치, 실행, idle compile 비용을 나눈다"]
date modified: 2026-08-03 17:24:03 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Profile guided compilation 은 설치, 실행, idle compile 비용을 나눈다

상위 문서: [Zygote와 ART 런타임 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/zygote-runtime-contracts/zygote-runtime-contracts.md)

Profile guided compilation 은 앱 설치 시 모든 코드를 컴파일하는 방식과 실행 시 전부 JIT 하는 방식 사이의 절충이다. 앱은 처음에는 해석 또는 JIT 로 실행되고, runtime profile 과 cloud/baseline profile 을 바탕으로 idle compile 단계에서 자주 쓰는 경로를 AOT 컴파일할 수 있다.

### 실무 의미

- 설치 속도, 저장소 사용량, 첫 실행 성능은 서로 trade-off 다.
- Play 가 전달하는 dex metadata 나 앱의 Baseline Profile 은 초기 AOT 범위에 영향을 줄 수 있다.
- 사용 중 생성된 local profile 은 이후 idle compile 또는 다음 실행 성능에 반영될 수 있다.
- cold start 성능을 보려면 profile 설치 상태와 compile filter 를 고정해야 한다.

### 관련 문서

- [Baseline Profile은 자주 실행되는 경로를 배포 전에 ART가 미리 컴파일하도록 돕는다](01_inbox/mobile/android/06_testing_performance/performance/benchmark-baseline-contracts/baseline-profile-generation-records-critical-user-journeys.md)
- [런타임 디버깅은 profile, compile filter, JIT 상태를 분리해서 본다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/zygote-runtime-contracts/runtime-debugging-separates-profile-compile-filter-and-jit-state.md)

공식 문서: [Configure ART](https://source.android.com/docs/core/runtime/configure)
