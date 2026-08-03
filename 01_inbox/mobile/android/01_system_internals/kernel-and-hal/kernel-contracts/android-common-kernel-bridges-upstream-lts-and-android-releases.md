---
title: android-common-kernel-bridges-upstream-lts-and-android-releases
tags: [android, android/kernel, linux]
aliases: [ACK, Android Common Kernel]
date modified: 2026-08-03 17:25:55 +09:00
date created: 2026-07-31 23:45:00 +09:00
---

## ACK 는 upstream LTS 와 Android release 를 잇는다

Android Common Kernel(ACK)은 upstream Linux LTS kernel 에 Android 커뮤니티에 필요한 패치를 더한 kernel tree 다. Google 의 `kernel/common` repository 에서 관리되며, GKI kernel 도 ACK source tree 에서 빌드된다.

ACK 를 이해할 때는 branch 이름을 제품 지식처럼 외우기보다 branch 의 의미를 봐야 한다. 예를 들어 `android15-6.6` 은 Android 15 와 Linux 6.6 계열을 연결하는 ACK KMI branch 다.

`android-mainline` 은 Android kernel 기능 개발의 주된 branch 이고, platform release 용 ACK KMI branch 는 freeze 이후 KMI 안정성을 유지한다. 이 때문에 최신 branch 표는 노트에 고정 복사하기보다 공식 compatibility matrix 를 확인하는 편이 안전하다.

ACK 는 upstream Linux 와 완전히 같은 것도, OEM 별 product kernel 과 같은 것도 아니다. upstream 에서 바로 받아들여지지 않았거나 Android release 일정에 필요한 패치가 ACK 에 머물 수 있고, device-specific 코드는 vendor module 로 분리되는 방향을 갖는다.

관련 노트: [GKI는 공통 core kernel과 vendor module을 분리한다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/gki-splits-generic-core-from-vendor-modules.md), [Android kernel build는 branch, toolchain, build system 계약이다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/kernel-builds-depend-on-branch-toolchain-and-build-system.md)

근거: [AOSP Kernel overview](https://source.android.com/docs/core/architecture/kernel), [Android common kernels](https://source.android.com/docs/core/architecture/kernel/android-common)
