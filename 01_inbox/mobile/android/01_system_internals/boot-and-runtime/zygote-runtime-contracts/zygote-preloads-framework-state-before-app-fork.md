---
title: zygote-preloads-framework-state-before-app-fork
tags: [android, android/boot-runtime, android/runtime, android/system-internals]
aliases: ["Zygote는 framework 공통 상태를 preload한 뒤 앱 프로세스를 fork한다"]
date modified: 2026-08-03 17:24:07 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Zygote 는 framework 공통 상태를 preload 한 뒤 앱 프로세스를 fork 한다

상위 문서: [Zygote와 ART 런타임 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/zygote-runtime-contracts/zygote-runtime-contracts.md)

Zygote 는 앱마다 새 runtime 을 처음부터 만드는 비용을 피하기 위해 framework class, resource, runtime state 의 공통 부분을 먼저 올린다. 이후 앱 실행 요청을 받으면 그 상태를 가진 프로세스를 fork 해 앱별 specialization 을 수행한다.

### 판단 기준

- preload 는 앱 시작을 빠르게 하지만 boot time 과 Zygote 메모리 footprint 를 늘릴 수 있다.
- 모든 앱이 공유할 가능성이 높은 framework 상태만 preload 이득이 크다.
- 앱별 상태를 Zygote preload 영역에 섞으면 copy-on-write 이점을 잃는다.

### 관련 문서

- [Zygote fork의 메모리 이점은 copy-on-write가 유지될 때 생긴다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/zygote-runtime-contracts/zygote-fork-saves-memory-while-copy-on-write-pages-stay-clean.md)
- [system_server는 framework service를 한 프로세스 안에서 시작한다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/system-server-starts-framework-services-in-one-process.md)

공식 문서: [About the Zygote processes](https://source.android.com/docs/core/runtime/zygote)
