---
title: 14-hal-hardware-abstraction-layer
tags: ["android", "android/glossary"]
aliases: ["Hardware Abstraction Layer"]
date modified: 2026-08-01 01:07:23 +09:00
date created: 2026-07-31 15:29:55 +09:00
---

## HAL

정의: HAL 은 Android framework 가 camera, audio, sensors 같은 vendor hardware capability 를 안정된 userspace contract 로 호출하게 해주는 boundary 다.

혼동 방지: HAL 은 앱 API 가 아니다. 앱은 CameraX, AudioTrack 같은 framework API 를 호출하고, framework 와 vendor implementation 사이의 compatibility 는 HAL, VINTF, binderized service 경계가 담당한다.

정본 링크:

- [HAL userspace contract](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/hal-is-stable-userspace-contract-between-framework-and-vendor.md)
- [VINTF compatibility contract](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/vintf-declares-framework-vendor-compatibility.md)
