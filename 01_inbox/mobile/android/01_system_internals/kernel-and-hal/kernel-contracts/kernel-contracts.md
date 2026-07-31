---
title: Kernel contracts
tags: [android, android/kernel, android/system-internals]
aliases: [Android kernel contracts]
date modified: 2026-07-31 23:45:00 +09:00
date created: 2026-07-31 23:45:00 +09:00
---

이 묶음은 Android kernel을 “Linux 기능 목록”이 아니라 platform contract 기준으로 정리한다. 핵심은 upstream LTS, ACK, GKI/KMI, vendor module, power, memory, security, shared buffer, debugging의 경계를 구분하는 것이다.

## 커널 계층과 업데이트

- [Android kernel은 Linux에 모바일 플랫폼 정책을 더한 커널이다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/android-kernel-is-linux-plus-mobile-platform-policy.md)
- [ACK는 upstream LTS와 Android release를 잇는다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/android-common-kernel-bridges-upstream-lts-and-android-releases.md)
- [GKI는 공통 core kernel과 vendor module을 분리한다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/gki-splits-generic-core-from-vendor-modules.md)
- [KMI 안정성은 같은 GKI LTS/Android branch 안에서만 성립한다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/kmi-is-stable-only-within-a-gki-lts-and-android-branch.md)
- [Vendor kernel module은 first-stage init 경계에서 로드된다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/vendor-kernel-modules-load-through-first-stage-init-boundaries.md)
- [Android kernel build는 branch, toolchain, build system 계약이다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/kernel-builds-depend-on-branch-toolchain-and-build-system.md)

## 전원과 메모리

- [Wakelock은 background work 권한이 아니라 suspend blocker다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/wakelocks-are-suspend-blockers-not-background-work-permission.md)
- [SystemSuspend는 userspace wakelock과 kernel suspend를 중재한다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/systemsuspend-arbitrates-userspace-wakelocks-and-kernel-suspend.md)
- [LMKD는 free memory가 아니라 memory pressure와 process importance로 종료를 결정한다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/lmkd-kills-processes-by-memory-pressure-and-process-importance.md)
- [PSI는 free memory가 아니라 stall time을 측정한다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/psi-measures-stall-time-for-memory-pressure.md)
- [zRAM은 메모리 부족 해결책이 아니라 압축 swap 정책이다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/zram-is-compressed-swap-policy-not-a-memory-fix.md)

## 공유 버퍼와 동적 확장

- [Android shared memory는 ashmem, ION, DMA-BUF heaps로 역할이 분화됐다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/android-shared-memory-evolved-from-ashmem-ion-to-dmabuf-heaps.md)
- [DMA-BUF zero-copy는 무작업 보장이 아니라 shared buffer ownership이다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/dmabuf-zero-copy-means-shared-buffer-ownership-not-no-work.md)
- [eBPF는 검증된 프로그램으로 Android kernel 기능을 확장한다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/ebpf-extends-android-kernel-through-verified-programs.md)

## 보안과 진단

- [SELinux는 domain/type 정책으로 mandatory access control을 강제한다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/selinux-enforces-mac-with-domain-type-policy.md)
- [SELinux policy는 Binder service와 file boundary를 함께 제어한다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/selinux-policy-controls-binder-service-and-file-boundaries.md)
- [Kernel security는 AVB, dm-verity, SELinux, CFI가 나눠 맡는다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/kernel-security-is-layered-with-avb-dmverity-selinux-and-cfi.md)
- [Kernel debugging은 logcat 이전의 신호에서 시작한다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/kernel-debugging-starts-before-logcat-with-bootloader-dmesg-and-trace.md)

## 중복 방지 규칙

- Binder 상세 구조는 IPC 정본으로 넘기고, kernel 노트에서는 `/dev/binder`와 SELinux 경계만 언급한다.
- AVB와 boot chain 상세는 boot/runtime 정본으로 넘기고, kernel 노트에서는 보안 계층의 역할만 설명한다.
- Surface/BufferQueue/zero-copy 상세는 graphics/media 정본과 연결하고, kernel 노트에서는 DMA-BUF와 heap 경계만 설명한다.
- NDK/JNI와 HAL 구현은 다음 `HAL/native boundary` 페이즈로 분리한다.
