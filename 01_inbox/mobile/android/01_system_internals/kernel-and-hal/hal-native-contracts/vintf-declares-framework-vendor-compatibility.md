---
title: VINTF declares framework vendor compatibility
tags: [android, android/native, android/system-internals]
aliases: [VINTF, Vendor Interface Object]
date modified: 2026-07-31 23:58:00 +09:00
date created: 2026-07-31 23:58:00 +09:00
---

VINTF는 IPC mechanism이 아니라 framework와 device/vendor 쪽 interface 요구사항을 manifest와 compatibility matrix로 표현하는 호환성 체계다. manifest는 제공하는 것을, compatibility matrix는 요구하는 것을 드러낸다.

Device manifest는 보통 vendor/ODM 쪽 HAL service와 instance를 설명하고, framework compatibility matrix는 framework가 기대하는 HAL interface와 version을 표현한다. OTA에서는 이 둘이 서로 맞는지가 중요하다.

VINTF 선언, service registration, SELinux service context는 서로 다른 층이다. VINTF에 선언되어도 process가 실제로 뜨고 service manager에 등록되어야 호출할 수 있으며, SELinux 정책도 client/server 접근을 허용해야 한다.

관련 노트: [AIDL HAL은 신규 HAL의 현재 stable interface 선택지다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/aidl-hal-is-current-stable-interface-for-new-hals.md), [Native service 디버깅은 init, Binder, VINTF, SELinux, tombstone을 분리한다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/native-service-debugging-separates-init-binder-vintf-selinux-and-tombstones.md)

출처: [AOSP VINTF](https://source.android.com/docs/core/architecture/vintf), [AOSP AIDL for HALs](https://source.android.com/docs/core/architecture/aidl/aidl-hals)
