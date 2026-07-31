---
title: Vendor kernel module은 first-stage init 경계에서 로드된다
tags: [android, android/kernel, android/gki, android/boot]
date modified: 2026-07-31 23:45:00 +09:00
date created: 2026-07-31 23:45:00 +09:00
---

GKI kernel은 모든 device driver를 core image에 포함하지 않는다. device boot에 필요한 vendor module은 vendor ramdisk와 vendor_boot partition 쪽에 놓이고, first-stage init이 module dependency와 load order를 참고해 로드한다.

이 구조는 boot partition과 vendor-specific driver delivery를 분리하기 위한 것이다. GKI kernel과 vendor module이 따로 빌드되더라도, device는 boot 초기에 필요한 storage, filesystem, SoC driver를 로드해야 system/vendor partition을 mount하고 계속 부팅할 수 있다.

module load order는 단순히 `insmod` 나열이 아니라 `modules.load`, `modules.dep`, soft dependency, recovery module 구성에 영향을 받는다. 따라서 boot failure를 분석할 때는 kernel image만 보지 말고 vendor_boot, ramdisk module 목록, first-stage init log를 같이 봐야 한다.

관련 노트: {link(ANDROID / "01_system_internals/boot-and-runtime/init-service-contracts/first-stage-init-builds-minimal-filesystem-for-second-stage.md", "First-stage init builds minimal filesystem")}, {link(CONTRACTS / "kernel-debugging-starts-before-logcat-with-bootloader-dmesg-and-trace.md", "Kernel debugging은 logcat 이전의 신호에서 시작한다")}

근거: [Kernel module support](https://source.android.com/docs/core/architecture/kernel/kernel-module-support)
