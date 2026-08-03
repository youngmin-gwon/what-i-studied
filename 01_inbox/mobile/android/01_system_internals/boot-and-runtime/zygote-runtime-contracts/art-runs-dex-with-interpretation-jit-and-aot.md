---
title: art-runs-dex-with-interpretation-jit-and-aot
tags: [android, android/boot-runtime, android/runtime, android/system-internals]
aliases: ["ART는 DEX를 interpretation, JIT, AOT 조합으로 실행한다"]
date modified: 2026-08-03 17:24:03 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## ART 는 DEX 를 interpretation, JIT, AOT 조합으로 실행한다

상위 문서: [Zygote와 ART 런타임 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/zygote-runtime-contracts/zygote-runtime-contracts.md)

ART 는 Android 의 managed runtime 이며 DEX bytecode 를 실행한다. 현대 ART 는 interpretation, just-in-time compilation, ahead-of-time compilation 을 조합해 설치 시간, 저장소 사용량, 실행 성능 사이의 균형을 잡는다.

### 구분

- interpretation 은 compiled artifact 가 없어도 DEX 를 실행할 수 있게 한다.
- JIT 는 실행 중 hot method 를 컴파일해 반복 실행 성능을 높인다.
- AOT 는 install, idle, profile-guided compile 단계에서 미리 native code 를 만든다.
- Dalvik 과 ART 는 DEX 호환성을 공유하지만 runtime 구현과 최적화 방식이 다르다.

### 관련 문서

- [Profile guided compilation은 설치, 실행, idle compile 비용을 나눈다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/zygote-runtime-contracts/profile-guided-compilation-splits-install-runtime-and-idle-costs.md)
- [Baseline Profile은 자주 실행되는 경로를 배포 전에 ART가 미리 컴파일하도록 돕는다](01_inbox/mobile/android/06_testing_performance/performance/benchmark-baseline-contracts/baseline-profile-generation-records-critical-user-journeys.md)

공식 문서: [Android runtime and Dalvik](https://source.android.com/docs/core/runtime), [Implement ART JIT compiler](https://source.android.com/docs/core/runtime/jit-compiler)
