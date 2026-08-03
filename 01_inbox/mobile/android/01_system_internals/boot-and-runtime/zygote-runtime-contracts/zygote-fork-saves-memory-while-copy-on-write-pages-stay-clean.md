---
title: zygote-fork-saves-memory-while-copy-on-write-pages-stay-clean
tags: [android, android/boot-runtime, android/runtime, android/system-internals]
aliases: ["Zygote fork의 메모리 이점은 copy-on-write가 유지될 때 생긴다"]
date modified: 2026-08-03 17:24:04 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Zygote fork 의 메모리 이점은 copy-on-write 가 유지될 때 생긴다

상위 문서: [Zygote와 ART 런타임 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/zygote-runtime-contracts/zygote-runtime-contracts.md)

Zygote fork 가 빠른 이유는 부모 메모리를 즉시 복사하지 않고 child process 와 page 를 공유하기 때문이다. 하지만 공유 page 에 쓰기가 발생하면 copy-on-write 로 private copy 가 생기므로, preload 된 상태가 clean 하게 유지될수록 메모리 이점이 커진다.

### 실무 의미

- framework class 와 immutable resource 는 여러 앱 사이에서 공유 이득이 크다.
- 앱 시작 중 많은 전역 상태를 수정하면 COW page 가 늘어날 수 있다.
- native heap, JIT code cache, 앱별 class loading 은 각 process 의 private 비용으로 본다.
- 메모리 분석에서는 RSS 하나만 보지 말고 shared/private page 관점을 함께 본다.

### 관련 문서

- [IPC and process contracts](01_inbox/mobile/android/01_system_internals/ipc-and-process/ipc-process-contracts/ipc-process-contracts.md)
- [Zygote는 framework 공통 상태를 preload한 뒤 앱 프로세스를 fork한다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/zygote-runtime-contracts/zygote-preloads-framework-state-before-app-fork.md)
