---
title: GKI는 공통 core kernel과 vendor module을 분리한다
tags: [android, android/kernel, android/gki]
aliases: [GKI, Generic Kernel Image]
date modified: 2026-07-31 23:45:00 +09:00
date created: 2026-07-31 23:45:00 +09:00
---

Generic Kernel Image(GKI)는 Android kernel fragmentation을 줄이기 위한 구조다. 공통 core kernel은 GKI로 제공하고, SoC나 board에 특화된 기능은 vendor module로 분리한다.

GKI의 목표는 모든 기기가 완전히 같은 driver set을 갖게 하는 것이 아니다. 공통 kernel binary와 안정적인 module interface를 유지해 security fix와 bug fix를 더 일관되게 전달하고, vendor-specific code가 core kernel을 과도하게 fork하지 않게 만드는 것이다.

Android 12부터 kernel 5.10 이상으로 출시되는 기기는 GKI kernel을 사용해야 한다. “Android 11부터 모든 기기에 강제”처럼 단정하면 release 조건과 kernel version 조건을 놓치게 된다.

GKI는 성능이나 전력 비용이 사라진다는 보장도 아니다. vendor module, firmware, HAL, device tree, boot partition 구성까지 함께 맞아야 실제 device가 부팅하고 안정적으로 동작한다.

관련 노트: [KMI 안정성은 같은 GKI LTS/Android branch 안에서만 성립한다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/kmi-is-stable-only-within-a-gki-lts-and-android-branch.md), [Vendor kernel module은 first-stage init 경계에서 로드된다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/vendor-kernel-modules-load-through-first-stage-init-boundaries.md)

근거: [Generic Kernel Image project](https://source.android.com/docs/core/architecture/kernel/generic-kernel-image)
