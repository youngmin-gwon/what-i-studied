---
title: vendor-kernel-modules-load-through-first-stage-init-boundaries
tags: [android, android/boot, android/gki, android/kernel]
aliases: []
date modified: 2026-08-03 17:26:14 +09:00
date created: 2026-07-31 23:45:00 +09:00
---

## Vendor kernel module 은 first-stage init 경계에서 로드된다

GKI kernel 은 모든 device driver 를 core image 에 포함하지 않는다. device boot 에 필요한 vendor module 은 vendor ramdisk 와 vendor_boot partition 쪽에 놓이고, first-stage init 이 module dependency 와 load order 를 참고해 로드한다.

이 구조는 boot partition 과 vendor-specific driver delivery 를 분리하기 위한 것이다. GKI kernel 과 vendor module 이 따로 빌드되더라도, device 는 boot 초기에 필요한 storage, filesystem, SoC driver 를 로드해야 system/vendor partition 을 mount 하고 계속 부팅할 수 있다.

module load order 는 단순히 `insmod` 나열이 아니라 `modules.load`, `modules.dep`, soft dependency, recovery module 구성에 영향을 받는다. 따라서 boot failure 를 분석할 때는 kernel image 만 보지 말고 vendor_boot, ramdisk module 목록, first-stage init log 를 같이 봐야 한다.

관련 노트: [First-stage init builds minimal filesystem](01_inbox/mobile/android/01_system_internals/boot-and-runtime/init-service-contracts/first-stage-init-builds-minimal-filesystem-for-second-stage.md), [Kernel debugging은 logcat 이전의 신호에서 시작한다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/kernel-debugging-starts-before-logcat-with-bootloader-dmesg-and-trace.md)

근거: [Kernel module support](https://source.android.com/docs/core/architecture/kernel/kernel-module-support)
