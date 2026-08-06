---
title: hal-native-boundary
tags: [android, android/native, android/system-internals]
aliases: [Android HAL native boundary, HAL native boundary]
date modified: 2026-08-06 15:25:00 +09:00
date created: 2026-07-31 23:58:00 +09:00
---

## HAL and native boundary

Android 의 native 경계는 kernel 자체가 아니라 framework, vendor implementation, native process, 앱 native library 가 만나는 계약이다. 이 허브는 기존 HAL, native services, NDK/JNI 문서를 userspace contract 단위로 다시 묶는다.

앞의 HAL/Treble/VINTF/HIDL/AIDL/binderized-passthrough/native service 영역은 platform/OEM 엔지니어가 다루므로 관찰 신호와 디버깅 진입점 중심으로 읽는다. NDK/JNI/AndroidBitmap 영역은 앱 개발자가 직접 호출하므로 사용 조건과 lifetime 위반을 중심으로 읽는다.

정본 묶음: [HAL native contracts](hal-native-contracts/hal-native-contracts.md). 전체 원자 목록과 읽는 순서는 이 정본 묶음이 소유한다.

### 읽는 기준

- system/vendor partition 호환성은 HAL·Treble·VINTF와 HIDL/AIDL 계약에서 시작한다.
- native service가 등록되지 않거나 죽는 문제는 init·Binder·SELinux·tombstone 경로로 분리한다.
- 앱 native code 문제는 NDK build·ABI에서 JNI thread/reference/copy/exception lifetime 순서로 좁힌다.
- 성능과 crash는 boundary crossing 비용과 native backtrace를 함께 본다.

### 범위

Kernel 내부 계약은 [Android kernel runtime](android-kernel-runtime.md) 에서 다룬다. 이 묶음은 kernel driver 를 직접 설명하지 않고, driver 위에 있는 HAL service, native service, 앱 native library 가 Android runtime 과 어떤 계약으로 연결되는지에 집중한다.
