---
title: "Android kernel runtime"
tags: [android, android/kernel, android/system-internals]
aliases: [android-kernel, Android Kernel, 안드로이드 커널]
date modified: 2026-07-31 23:45:00 +09:00
date created: 2026-07-31 23:45:00 +09:00
---

# Android kernel runtime

Android kernel 영역은 Linux kernel 지식과 Android platform 정책이 만나는 지점이다. 이 허브는 기존 `android-kernel` 가이드의 내용을 ACK/GKI/KMI, power, memory, shared buffer, SELinux, build/debugging 계약으로 다시 묶는다.

정본 묶음: [Kernel contracts](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/kernel-contracts.md)

## 읽는 순서

- [Android kernel이 일반 Linux와 달라지는 이유](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/android-kernel-is-linux-plus-mobile-platform-policy.md)
- [ACK와 upstream Linux 관계](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/android-common-kernel-bridges-upstream-lts-and-android-releases.md)
- [GKI와 vendor module 분리](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/gki-splits-generic-core-from-vendor-modules.md)
- [KMI 안정성 범위](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/kmi-is-stable-only-within-a-gki-lts-and-android-branch.md)
- [Wakelock과 suspend](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/wakelocks-are-suspend-blockers-not-background-work-permission.md)
- [LMKD와 memory pressure](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/lmkd-kills-processes-by-memory-pressure-and-process-importance.md)
- [zRAM과 compressed swap](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/zram-is-compressed-swap-policy-not-a-memory-fix.md)
- [ashmem, ION, DMA-BUF heaps](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/android-shared-memory-evolved-from-ashmem-ion-to-dmabuf-heaps.md)
- [SELinux domain/type policy](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/selinux-enforces-mac-with-domain-type-policy.md)
- [Kernel debugging](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/kernel-debugging-starts-before-logcat-with-bootloader-dmesg-and-trace.md)

## 다음 경계

HAL, native service, NDK/JNI는 kernel 자체가 아니라 kernel과 userspace/native code의 경계다. 이 영역은 [HAL and native boundary](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-boundary.md)에서 별도 정본으로 분리했다.
