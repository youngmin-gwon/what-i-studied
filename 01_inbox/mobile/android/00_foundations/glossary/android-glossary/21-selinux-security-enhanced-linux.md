---
title: "SELinux는 프로세스와 파일의 접근 권한을 강제하는 필수 접근 제어(MAC) 시스템이다"
tags: ["android", "android/glossary"]
aliases: ["Android SELinux", "Security Enhanced Linux"]
date modified: 2026-08-01 01:07:31 +09:00
date created: 2026-07-31 15:29:55 +09:00
---

# SELinux는 프로세스와 파일의 접근 권한을 강제하는 필수 접근 제어(MAC) 시스템이다

정의: SELinux 는 Android 에서 domain/type 기반 mandatory access control 을 적용해 process, file, binder service boundary 를 강제하는 security layer 다.

혼동 방지: SELinux 는 Linux user/group permission 을 대체하는 것이 아니라 그 위에 추가되는 mandatory policy 다. 앱 권한 문제와 platform domain policy 문제를 섞으면 원인 분석이 흐려진다.

정본 링크:

- [SELinux MAC policy](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/selinux-enforces-mac-with-domain-type-policy.md)
- [SELinux boundary policy](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/selinux-policy-controls-binder-service-and-file-boundaries.md)
