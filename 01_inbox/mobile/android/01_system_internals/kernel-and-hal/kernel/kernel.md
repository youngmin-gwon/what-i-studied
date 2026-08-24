---
title: kernel
tags: [android, android/kernel, android/system-internals]
aliases: [Android kernel contracts]
date modified: 2026-08-05 11:28:45 +09:00
date created: 2026-07-31 23:45:00 +09:00
---

## Kernel contracts

이 묶음은 Android kernel 을 "Linux 기능 목록"이 아니라 platform contract 기준으로 정리한다. 핵심은 upstream LTS, ACK, GKI/KMI, vendor module, power, memory, security, shared buffer, debugging 의 경계를 구분하는 것이다.

### 커널 계층과 업데이트

- [Android kernel은 Linux에 모바일 플랫폼 정책을 더한 커널이다](android-kernel-architecture.md)
- [ACK는 upstream LTS와 Android release를 잇는다](android-common-kernel.md)
- [GKI는 공통 core kernel과 vendor module을 분리한다](generic-kernel-image.md)
- [KMI 안정성은 같은 GKI LTS/Android branch 안에서만 성립한다](kernel-module-interface.md)
- [Vendor kernel module은 first-stage init 경계에서 로드된다](vendor-kernel-modules.md)
- [Android kernel build는 branch, toolchain, build system 계약이다](kernel-build-and-toolchain.md)

### 전원과 메모리

- [Wakelock은 background work 권한이 아니라 suspend blocker다](wakelocks-and-power-management.md)
- [SystemSuspend는 userspace wakelock과 kernel suspend를 중재한다](systemsuspend-and-wakelocks.md)
- [LMKD는 free memory가 아니라 memory pressure와 process importance로 종료를 결정한다](lmkd-memory-pressure.md)
- [PSI는 free memory가 아니라 stall time을 측정한다](psi-pressure-stall-information.md)
- [zRAM은 메모리 부족 해결책이 아니라 압축 swap 정책이다](zram-swap-policy.md)

### 공유 버퍼와 동적 확장

- [Android shared memory는 ashmem, ION, DMA-BUF heaps로 역할이 분화됐다](android-shared-memory-evolution.md)
- [DMA-BUF zero-copy는 무작업 보장이 아니라 shared buffer ownership이다](dmabuf-zero-copy.md)
- [eBPF는 검증된 프로그램으로 Android kernel 기능을 확장한다](ebpf-in-android-kernel.md)

### 보안과 진단

- [SELinux는 domain/type 정책으로 mandatory access control을 강제한다](selinux-mandatory-access-control.md)
- [SELinux policy는 Binder service와 file boundary를 함께 제어한다](selinux-policy-boundaries.md)
- [Kernel security는 AVB, dm-verity, SELinux, CFI가 나눠 맡는다](kernel-security-layers.md)
- [Kernel debugging은 logcat 이전의 신호에서 시작한다](kernel-debugging-and-trace.md)

### 중복 방지 규칙

- Binder 상세 구조는 IPC 정본으로 넘기고, kernel 노트에서는 `/dev/binder` 와 SELinux 경계만 언급한다.
- AVB 와 boot chain 상세는 boot/runtime 정본으로 넘기고, kernel 노트에서는 보안 계층의 역할만 설명한다.
- Surface/BufferQueue/zero-copy 상세는 graphics/media 정본과 연결하고, kernel 노트에서는 DMA-BUF 와 heap 경계만 설명한다.
- NDK/JNI 와 HAL 구현은 다음 `HAL/native boundary` 페이즈로 분리한다.
