---
title: init-is-pid1-and-userspace-bootstrap-policy-engine
tags: [android, android/boot-runtime, android/init, android/system-internals]
aliases: ["init는 PID 1이자 Android userspace의 부트스트랩 정책 엔진이다"]
date modified: 2026-08-03 17:23:38 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## init 는 PID 1 이자 Android userspace 의 부트스트랩 정책 엔진이다

상위 문서: [init와 네이티브 서비스 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/init-service-contracts/init-service-contracts.md)

Android 의 `init` 은 Linux PID 1 인 동시에 Android 전용 부팅 정책 엔진이다. kernel 이 userspace 로 넘어오면 `init` 은 mount, property, SELinux, device node, native service, Zygote 시작을 단계적으로 조율한다.

### 판단 기준

- `init` 은 앱 프레임워크 service 가 아니라 userspace 기반을 세우는 최상위 supervisor 다.
- `.rc` 파일은 imperative shell script 가 아니라 init language 선언이다.
- service 재시작, property trigger, class start/stop 은 `init` main loop 가 처리한다.
- Zygote 가 죽으면 앱 프로세스 전반이 영향을 받으므로 `init` 서비스 정책이 framework 안정성과 직접 연결된다.

### 관련 문서

- [First stage init은 second stage가 읽을 최소 파일시스템을 만든다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/init-service-contracts/first-stage-init-builds-minimal-filesystem-for-second-stage.md)
- [Zygote는 framework 공통 상태를 preload한 뒤 앱 프로세스를 fork한다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/zygote-runtime-contracts/zygote-preloads-framework-state-before-app-fork.md)

공식 문서: [Android Init Language](https://android.googlesource.com/platform/system/core/+/master/init/README.md)
