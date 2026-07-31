---
title: Treble separates system and vendor through stable interfaces
tags: [android, android/native, android/system-internals]
aliases: [Project Treble]
date modified: 2026-07-31 23:58:00 +09:00
date created: 2026-07-31 23:58:00 +09:00
---

# Treble separates system and vendor through stable interfaces

Project Treble의 실무적 의미는 Android framework 쪽 system image와 vendor implementation 쪽 vendor image 사이에 업데이트 가능한 경계를 세우는 것이다. 이 경계가 없으면 framework 변경이 vendor HAL, driver, device-specific 코드 재작업으로 쉽게 번진다.

Treble 이후 HAL은 단순한 C 함수 묶음보다 stable interface, process boundary, manifest/matrix 검증과 함께 이해해야 한다. framework가 요구하는 interface와 device가 제공하는 interface가 맞아야 system/vendor 조합이 OTA 이후에도 동작할 수 있다.

이 노트의 초점은 “OS 업데이트가 쉬워졌다”는 결과가 아니라, 그 결과를 가능하게 만든 contract boundary다. 구체적인 호환성 선언은 VINTF가 맡는다.

관련 노트: [HAL은 framework와 vendor 구현 사이의 안정된 userspace contract다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/hal-is-stable-userspace-contract-between-framework-and-vendor.md), [VINTF는 framework/vendor 호환성을 manifest와 matrix로 선언한다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/vintf-declares-framework-vendor-compatibility.md)

출처: [AOSP HAL overview](https://source.android.com/docs/core/architecture/hal), [AOSP VINTF](https://source.android.com/docs/core/architecture/vintf)
