---
title: boot-chain-confirms-trust-before-kernel-and-userspace
tags: [android, android/boot, android/boot-runtime, android/system-internals]
aliases: ["부팅 체인은 신뢰 상태를 확정한 뒤 kernel과 userspace로 넘어간다"]
date modified: 2026-08-03 17:23:04 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## 부팅 체인은 신뢰 상태를 확정한 뒤 kernel 과 userspace 로 넘어간다

상위 문서: [부팅 흐름 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/boot-flow-contracts/boot-flow-contracts.md)

Android 부팅은 Boot ROM, bootloader, kernel, `init`, Zygote, `system_server`, System UI/Launcher 순서로 이어진다. 중요한 점은 단순 실행 순서가 아니라, 어느 단계가 다음 단계의 신뢰성과 실행 조건을 확정하는지다.

### 판단 기준

- Boot ROM 과 bootloader 는 기기별 구현이며, OS 이미지 검증과 slot 선택을 끝낸 뒤 kernel 을 올린다.
- kernel 은 Android userspace 의 첫 프로세스로 `init` 을 실행한다.
- `init` 이후부터는 AOSP init language, property, SELinux, service class 가 부팅 순서를 지배한다.
- Zygote 와 `system_server` 가 올라가기 전에는 앱 프레임워크 관점의 디버깅 도구가 제한된다.

### 관련 문서

- [init는 PID 1이자 Android userspace의 부트스트랩 정책 엔진이다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/init-service-contracts/init-is-pid1-and-userspace-bootstrap-policy-engine.md)
- [Zygote는 framework 공통 상태를 preload한 뒤 앱 프로세스를 fork한다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/zygote-runtime-contracts/zygote-preloads-framework-state-before-app-fork.md)
- [system_server는 framework service를 한 프로세스 안에서 시작한다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/system-server-starts-framework-services-in-one-process.md)

공식 문서: [Bootloader overview](https://source.android.com/docs/core/architecture/bootloader), [Boot flow](https://source.android.com/docs/security/features/verifiedboot/boot-flow)
