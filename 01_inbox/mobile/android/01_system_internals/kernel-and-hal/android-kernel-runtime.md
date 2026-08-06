---
title: android-kernel-runtime
tags: [android, android/kernel, android/system-internals]
aliases: [Android Kernel, android-kernel, 안드로이드 커널]
date modified: 2026-08-06 15:25:00 +09:00
date created: 2026-07-31 23:45:00 +09:00
---

## Android kernel runtime

Android kernel 영역은 Linux kernel 지식과 Android platform 정책이 만나는 지점이다. 이 허브는 기존 `android-kernel` 가이드의 내용을 ACK/GKI/KMI, power, memory, shared buffer, SELinux, build/debugging 계약으로 다시 묶는다.

정본 묶음: [Kernel contracts](kernel-contracts/kernel-contracts.md). 원자 노트의 전체 목록과 세부 읽기 순서는 이 정본 묶음이 소유한다.

### 읽는 기준

kernel release와 vendor module 호환성 문제는 ACK·GKI·KMI·build 계약부터 읽는다. suspend 또는 memory pressure 문제는 power·LMKD·PSI·zRAM 계약으로 이동한다. shared buffer 문제는 DMA-BUF 소유권을, boot 이전 crash나 policy denial은 kernel debugging·SELinux 계약을 고른다. 구체적인 링크 순서는 [Kernel contracts](kernel-contracts/kernel-contracts.md)에 한 번만 유지한다.

### 다음 경계

HAL, native service, NDK/JNI 는 kernel 자체가 아니라 kernel 과 userspace/native code 의 경계다. 이 영역은 [HAL and native boundary](hal-native-boundary.md) 에서 별도 정본으로 분리했다.
