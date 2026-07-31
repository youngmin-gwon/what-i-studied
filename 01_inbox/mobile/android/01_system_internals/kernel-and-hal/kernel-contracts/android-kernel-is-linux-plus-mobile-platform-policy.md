---
title: Android kernel은 Linux에 모바일 플랫폼 정책을 더한 커널이다
tags: [android, android/kernel, linux]
aliases: [Android Kernel, 안드로이드 커널]
date modified: 2026-07-31 23:45:00 +09:00
date created: 2026-07-31 23:45:00 +09:00
---

Android kernel은 upstream Linux LTS를 기반으로 하지만, 앱 샌드박스, 전원 관리, 메모리 압박 대응, 하드웨어 추상화, verified boot 같은 Android 플랫폼 요구를 만족하도록 구성된다.

핵심 차이는 “Linux와 다른 별도 OS 커널”이 아니라 “모바일 제품을 대량으로 출하하기 위해 Linux kernel 위에 Android 공통 패치와 정책 경계를 얹었다”는 점이다. 앱 개발자는 대부분 이 경계를 framework API로 만나지만, 성능·보안·부팅 문제를 분석할 때는 kernel 정책까지 내려가야 한다.

초기 Android는 Binder, ashmem, wakelock, LMK 같은 out-of-tree 요소가 많았다. 시간이 지나면서 일부는 upstream Linux에 들어가거나, GKI/KMI, DMA-BUF heaps, userspace lmkd처럼 더 표준화된 구조로 이동했다.

이 노트의 범위는 kernel 자체의 실행 계약이다. HAL 구현, NDK/JNI 사용법, 앱 아키텍처는 별도 노트로 분리한다.

관련 노트: [ACK는 upstream LTS와 Android release를 잇는다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/android-common-kernel-bridges-upstream-lts-and-android-releases.md), [Android HAL and kernel](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/hal-is-stable-userspace-contract-between-framework-and-vendor.md)

근거: [AOSP Kernel overview](https://source.android.com/docs/core/architecture/kernel)
