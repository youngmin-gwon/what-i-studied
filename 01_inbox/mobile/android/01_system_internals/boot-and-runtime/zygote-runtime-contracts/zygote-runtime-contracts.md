---
title: zygote-runtime-contracts
tags: [android, android/boot-runtime, android/runtime, android/system-internals]
aliases: ["Zygote와 ART 런타임 계약"]
date modified: 2026-08-03 17:24:09 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Zygote 와 ART 런타임 계약

Zygote 와 ART 는 Android 앱 프로세스의 시작 비용, 메모리 공유, DEX 실행, profile 기반 최적화, `ActivityThread` 진입을 결정한다.

### 정본 노트

- [Zygote는 framework 공통 상태를 preload한 뒤 앱 프로세스를 fork한다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/zygote-runtime-contracts/zygote-preloads-framework-state-before-app-fork.md)
- [Zygote fork의 메모리 이점은 copy-on-write가 유지될 때 생긴다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/zygote-runtime-contracts/zygote-fork-saves-memory-while-copy-on-write-pages-stay-clean.md)
- [Zygote socket은 system_server가 앱 프로세스를 요청하는 factory interface다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/zygote-runtime-contracts/zygote-socket-is-system-server-process-factory-interface.md)
- [앱 프로세스는 specialization 뒤 ActivityThread로 framework에 attach한다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/zygote-runtime-contracts/app-process-specializes-before-activitythread-attaches-to-framework.md)
- [ART는 DEX를 interpretation, JIT, AOT 조합으로 실행한다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/zygote-runtime-contracts/art-runs-dex-with-interpretation-jit-and-aot.md)
- [Profile guided compilation은 설치, 실행, idle compile 비용을 나눈다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/zygote-runtime-contracts/profile-guided-compilation-splits-install-runtime-and-idle-costs.md)
- [런타임 디버깅은 profile, compile filter, JIT 상태를 분리해서 본다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/zygote-runtime-contracts/runtime-debugging-separates-profile-compile-filter-and-jit-state.md)

### 경계 규칙

- process 생성은 Zygote/ActivityThread 경계로 설명하고 Activity lifecycle 자체는 app component 정본으로 넘긴다.
- ART 실행과 profile compilation 은 runtime 비용 경계로 다루고 Gradle/R8 최적화와 섞지 않는다.
- copy-on-write 메모리 이점은 Zygote preload 와 process private page 관점으로 설명한다.

관련 지도: [system_server와 ActivityManager 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/system-server-contracts.md), [Kernel contracts](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/kernel-contracts.md)
