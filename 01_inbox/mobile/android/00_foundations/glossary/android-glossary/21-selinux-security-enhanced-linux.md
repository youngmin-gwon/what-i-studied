---
title: "SELinux"
tags: ["android", "android/glossary"]
aliases: ["Security Enhanced Linux", "Android SELinux"]
---

# SELinux

정의: SELinux는 Android에서 domain/type 기반 mandatory access control을 적용해 process, file, binder service boundary를 강제하는 security layer다.

혼동 방지: SELinux는 Linux user/group permission을 대체하는 것이 아니라 그 위에 추가되는 mandatory policy다. 앱 권한 문제와 platform domain policy 문제를 섞으면 원인 분석이 흐려진다.

정본 링크:
- [SELinux MAC policy](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/selinux-enforces-mac-with-domain-type-policy.md)
- [SELinux boundary policy](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/selinux-policy-controls-binder-service-and-file-boundaries.md)
