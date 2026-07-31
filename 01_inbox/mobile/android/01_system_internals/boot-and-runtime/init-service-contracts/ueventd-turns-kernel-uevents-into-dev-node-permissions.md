---
title: "ueventd는 kernel uevent를 dev node 권한으로 변환한다"
tags: [android, android/system-internals, android/boot-runtime, android/init]
aliases: ["ueventd는 kernel uevent를 dev node 권한으로 변환한다"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# ueventd는 kernel uevent를 dev node 권한으로 변환한다

상위 문서: [init와 네이티브 서비스 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/init-service-contracts/init-service-contracts.md)

`ueventd`는 kernel이 보낸 device event를 받아 `/dev` node 생성, owner/group, mode, SELinux label을 적용한다. 앱이나 framework가 하드웨어에 접근하는 권한은 이 dev node 경계에서 이미 한 번 결정된다.

## 왜 중요한가

camera, audio, binder, hwbinder, input device 같은 node 권한이 잘못되면 framework service가 정상이어도 기기가 동작하지 않는다. 반대로 너무 넓은 권한은 HAL 또는 native daemon의 보안 경계를 약하게 만든다.

## 관련 문서

- [init 보안은 SELinux domain과 capability 경계로 정의된다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/init-service-contracts/init-security-is-selinux-domain-and-capability-boundary.md)
- [Android HAL과 커널](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/hal-is-stable-userspace-contract-between-framework-and-vendor.md)

공식 문서: [Android Init Language](https://android.googlesource.com/platform/system/core/+/master/init/README.md)
