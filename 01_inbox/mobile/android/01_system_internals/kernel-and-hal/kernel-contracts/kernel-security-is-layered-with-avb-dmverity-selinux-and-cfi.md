---
title: kernel-security-is-layered-with-avb-dmverity-selinux-and-cfi
tags: [android, android/kernel, android/security]
aliases: []
date modified: 2026-08-03 17:26:10 +09:00
date created: 2026-07-31 23:45:00 +09:00
---

## Kernel security 는 AVB, dm-verity, SELinux, CFI 가 나눠 맡는다

Android kernel 보안을 하나의 기능으로 설명하면 안 된다. boot 전에 실행 code 와 partition integrity 를 검증하는 AVB/dm-verity, runtime access 를 제한하는 SELinux, kernel indirect control flow 공격을 줄이는 CFI/KCFI 는 서로 다른 실패 모드를 다룬다.

AVB 는 boot partition, dtbo, system, vendor 같은 boot 대상 code/data 가 기대한 상태인지 검증한다. 큰 partition 은 hash tree 기반의 dm-verity 로 runtime read path 에서 검증될 수 있다.

SELinux 는 부팅 후 process 와 object 의 access decision 을 강제한다. 공격자가 root 나 capability 를 얻더라도 policy 가 허용하지 않은 system resource 접근을 줄이는 역할을 한다.

CFI/KCFI 는 kernel binary 내부의 indirect function call control flow 를 제한해 code-reuse 공격 난이도를 높인다. GKI 에서는 CFI 가 기본 활성화되어 있지만, driver type mismatch 같은 문제는 device bring-up 에서 별도 검증이 필요하다.

관련 노트: [AVB verifies boot images and rollback protection](01_inbox/mobile/android/01_system_internals/boot-and-runtime/boot-flow-contracts/avb-verifies-boot-images-and-rollback-protection.md), [SELinux는 domain/type 정책으로 mandatory access control을 강제한다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/selinux-enforces-mac-with-domain-type-policy.md)

근거: [Use Verified Boot](https://source.android.com/docs/security/features/verifiedboot/verified-boot), [Implement dm-verity](https://source.android.com/docs/security/features/verifiedboot/dm-verity), [Control flow integrity in the kernel](https://source.android.com/docs/security/test/kcfi)
