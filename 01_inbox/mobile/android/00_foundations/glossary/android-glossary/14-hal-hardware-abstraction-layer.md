---
title: "HAL"
tags: ["android", "android/glossary"]
aliases: ["Hardware Abstraction Layer"]
---

# HAL

정의: HAL은 Android framework가 camera, audio, sensors 같은 vendor hardware capability를 안정된 userspace contract로 호출하게 해주는 boundary다.

혼동 방지: HAL은 앱 API가 아니다. 앱은 CameraX, AudioTrack 같은 framework API를 호출하고, framework와 vendor implementation 사이의 compatibility는 HAL, VINTF, binderized service 경계가 담당한다.

정본 링크:
- [HAL userspace contract](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/hal-is-stable-userspace-contract-between-framework-and-vendor.md)
- [VINTF compatibility contract](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/vintf-declares-framework-vendor-compatibility.md)
