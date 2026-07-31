---
title: Native service debugging separates init Binder VINTF SELinux and tombstones
tags: [android, android/native, android/system-internals]
aliases: [native debugging, tombstone, SELinux]
date modified: 2026-07-31 23:58:00 +09:00
date created: 2026-07-31 23:58:00 +09:00
---

# Native service debugging separates init Binder VINTF SELinux and tombstones

Native service나 HAL 문제를 볼 때는 process launch, Binder registration, VINTF declaration, SELinux access, native crash를 같은 문제로 뭉개지 않는다. 증상은 비슷해도 실패 지점이 다르면 보는 로그와 명령이 달라진다.

`adb shell service list`는 Binder service discovery를 확인하는 도구이고, init service 전체 목록이나 모든 HAL instance 목록과 동일하지 않다. `dumpsys`는 등록된 service가 제공하는 dump endpoint를 통해 상태를 확인한다.

Native crash는 logcat만으로 끝나지 않는다. tombstone, symbol, ABI, build variant, SELinux denial, init restart 여부를 함께 봐야 한다. HAL이면 추가로 VINTF manifest와 service context, hwservice/service manager registration을 확인한다.

관련 노트: [Native system service는 init이 띄우고 Binder로 발견되는 endpoint다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/native-system-services-are-init-managed-binder-endpoints.md), [Native 성능과 crash debugging은 경계 비용에서 시작한다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/native-performance-and-crash-debugging-start-at-the-boundary.md)

출처: [AOSP AIDL for HALs](https://source.android.com/docs/core/architecture/aidl/aidl-hals), [Android Studio native debugging](https://developer.android.com/studio/debug/native-debugging)
