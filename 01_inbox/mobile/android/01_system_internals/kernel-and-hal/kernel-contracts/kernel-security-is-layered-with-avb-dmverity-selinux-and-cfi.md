---
title: Kernel security는 AVB, dm-verity, SELinux, CFI가 나눠 맡는다
tags: [android, android/kernel, android/security]
date modified: 2026-07-31 23:45:00 +09:00
date created: 2026-07-31 23:45:00 +09:00
---

Android kernel 보안을 하나의 기능으로 설명하면 안 된다. boot 전에 실행 code와 partition integrity를 검증하는 AVB/dm-verity, runtime access를 제한하는 SELinux, kernel indirect control flow 공격을 줄이는 CFI/KCFI는 서로 다른 실패 모드를 다룬다.

AVB는 boot partition, dtbo, system, vendor 같은 boot 대상 code/data가 기대한 상태인지 검증한다. 큰 partition은 hash tree 기반의 dm-verity로 runtime read path에서 검증될 수 있다.

SELinux는 부팅 후 process와 object의 access decision을 강제한다. 공격자가 root나 capability를 얻더라도 policy가 허용하지 않은 system resource 접근을 줄이는 역할을 한다.

CFI/KCFI는 kernel binary 내부의 indirect function call control flow를 제한해 code-reuse 공격 난이도를 높인다. GKI에서는 CFI가 기본 활성화되어 있지만, driver type mismatch 같은 문제는 device bring-up에서 별도 검증이 필요하다.

관련 노트: [AVB verifies boot images and rollback protection](01_inbox/mobile/android/01_system_internals/boot-and-runtime/boot-flow-contracts/avb-verifies-boot-images-and-rollback-protection.md), [SELinux는 domain/type 정책으로 mandatory access control을 강제한다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/selinux-enforces-mac-with-domain-type-policy.md)

근거: [Use Verified Boot](https://source.android.com/docs/security/features/verifiedboot/verified-boot), [Implement dm-verity](https://source.android.com/docs/security/features/verifiedboot/dm-verity), [Control flow integrity in the kernel](https://source.android.com/docs/security/test/kcfi)
