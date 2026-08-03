---
title: "AIDL HAL is current stable interface for new HALs"
tags: [android, android/native, android/system-internals]
aliases: [AIDL HAL, Stable AIDL]
date modified: 2026-07-31 23:58:00 +09:00
date created: 2026-07-31 23:58:00 +09:00
---

# AIDL HAL is current stable interface for new HALs

AIDL HAL은 Android 11부터 HAL 구현에 사용할 수 있게 된 방식이며, 가능한 신규 HAL에는 Stable AIDL을 사용하는 방향이 권장된다. AIDL은 Java-like interface language지만 backend에 따라 C++, Java, Rust, NDK 경계에서 사용할 수 있다.

Framework component가 `system.img`에 있고 hardware component가 `vendor.img`에 있는 식으로 partition 경계를 넘는 HAL 통신은 stable AIDL을 사용해야 한다. 같은 partition 내부 통신은 같은 제약을 받는 경계가 아니다.

AIDL HAL은 interface 안정성만으로 끝나지 않는다. VINTF manifest declaration, service registration, SELinux service type, VTS가 함께 맞아야 device/framework contract가 실제로 성립한다.

관련 노트: [VINTF는 framework/vendor 호환성을 manifest와 matrix로 선언한다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/vintf-declares-framework-vendor-compatibility.md), [Native system service는 init이 띄우고 Binder로 발견되는 endpoint다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/native-system-services-are-init-managed-binder-endpoints.md)

출처: [AOSP AIDL for HALs](https://source.android.com/docs/core/architecture/aidl/aidl-hals), [AOSP AIDL overview](https://source.android.com/docs/core/architecture/aidl)
