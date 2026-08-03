---
title: first-stage-init-builds-minimal-filesystem-for-second-stage
tags: [android, android/boot-runtime, android/init, android/system-internals]
aliases: ["First stage init은 second stage가 읽을 최소 파일시스템을 만든다"]
date modified: 2026-08-03 17:23:31 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## First stage init 은 second stage 가 읽을 최소 파일시스템을 만든다

상위 문서: [init와 네이티브 서비스 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/init-service-contracts/init-service-contracts.md)

First stage init 은 전체 Android 서비스를 시작하지 않는다. `/dev`, `/proc`, `/sys` 같은 기본 파일시스템과 first-stage mount 가 필요한 파티션을 준비해 second stage init 이 `.rc` 와 SELinux 정책을 읽을 수 있게 만드는 단계다.

### 왜 중요한가

`/vendor` 의 init rc 를 읽으려면 `/vendor` 가 먼저 mount 되어야 한다. 이 순환 문제 때문에 first-stage mount 와 fstab flag 가 부팅 구조의 핵심 계약이 된다.

### 관련 문서

- [fstab은 mount와 검증 플래그를 묶은 부팅 계약이다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/init-service-contracts/fstab-is-boot-time-mount-and-verification-contract.md)
- [파티션 구조는 system과 vendor의 업데이트 경계를 만든다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/boot-flow-contracts/partitions-define-system-vendor-and-update-boundaries.md)

공식 문서: [Android Init Language](https://android.googlesource.com/platform/system/core/+/master/init/README.md)
