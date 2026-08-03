---
title: hal-native-boundary
tags: [android, android/native, android/system-internals]
aliases: [Android HAL native boundary, HAL native boundary]
date modified: 2026-08-03 17:26:19 +09:00
date created: 2026-07-31 23:58:00 +09:00
---

## HAL and native boundary

Android 의 native 경계는 kernel 자체가 아니라 framework, vendor implementation, native process, 앱 native library 가 만나는 계약이다. 이 허브는 기존 HAL, native services, NDK/JNI 문서를 userspace contract 단위로 다시 묶는다.

이 목록은 톤이 균일하지 않다. 앞의 HAL/Treble/VINTF/HIDL/AIDL/binderized-passthrough/native service 항목은 platform/OEM 엔지니어가 다루는 영역이라 "관찰 가능 신호"와 "디버깅 진입점" 중심으로 읽는다 — 앱 코드로 이 계층을 직접 바꿀 수 없다. 뒤의 NDK/JNI/AndroidBitmap 항목은 앱 개발자가 실제로 호출하는 API 라 "언제/어떻게 쓰는가"와 "무엇을 지키지 않으면 깨지는가" 중심으로 읽는다. 아래 순서는 이 경계를 기준으로 나열한다.

정본 묶음: [HAL native contracts](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/hal-native-contracts.md) (읽는 순서와 문제 분류 기준은 여기에 더 자세히 정리되어 있다.)

### 읽는 순서

#### platform/OEM 관점 (앱이 직접 건드리지 않는 영역)

- [HAL은 framework와 vendor 구현 사이의 안정된 userspace contract다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/hal-is-stable-userspace-contract-between-framework-and-vendor.md)
- [Treble은 system과 vendor 업데이트 경계를 stable interface로 분리한다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/treble-separates-system-and-vendor-through-stable-interfaces.md)
- [VINTF는 framework/vendor 호환성을 manifest와 matrix로 선언한다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/vintf-declares-framework-vendor-compatibility.md)
- [HIDL은 legacy Treble interface이지 신규 기본값이 아니다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/hidl-is-legacy-treble-interface-not-new-default.md)
- [AIDL HAL은 신규 HAL의 현재 stable interface 선택지다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/aidl-hal-is-current-stable-interface-for-new-hals.md)
- [Binderized HAL과 passthrough HAL은 process boundary를 다르게 둔다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/binderized-and-passthrough-hal-define-process-boundary.md)
- [Native system service는 init이 띄우고 Binder로 발견되는 endpoint다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/native-system-services-are-init-managed-binder-endpoints.md)
- [Native service 디버깅은 init, Binder, VINTF, SELinux, tombstone을 분리한다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/native-service-debugging-separates-init-binder-vintf-selinux-and-tombstones.md)

#### 앱 개발자 관점 (NDK/JNI 로 직접 호출하는 영역)

- [NDK는 앱 아키텍처가 아니라 native library toolchain 경계다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/ndk-is-native-library-toolchain-not-app-architecture.md)
- [CMake, Gradle, ABI는 native build와 packaging 계약을 나눈다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/cmake-gradle-and-abi-define-native-build-and-packaging.md)
- [JNI는 managed runtime과 native code 사이의 명시적 호출 경계다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/jni-is-explicit-boundary-between-managed-runtime-and-native-code.md)
- [JNI reference는 local, global, weak lifetime이 다르다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/jni-references-have-local-global-and-weak-lifetimes.md)
- [JNIEnv는 thread-local이고 native thread는 attach가 필요하다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/jnienv-is-thread-local-and-native-threads-must-attach.md)
- [JNI string/array 접근은 copy, pin, release 계약이다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/jni-strings-and-arrays-have-copy-pin-and-release-contracts.md)
- [JNI method/field ID와 pending exception은 runtime state다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/jni-method-field-ids-and-pending-exceptions-are-runtime-state.md)
- [AndroidBitmap native 접근은 format, stride, lock lifetime을 확인해야 한다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/androidbitmap-native-access-requires-format-stride-and-lock-lifetime.md)
- [Native 성능과 crash debugging은 경계 비용에서 시작한다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/native-performance-and-crash-debugging-start-at-the-boundary.md)

### 범위

Kernel 내부 계약은 [Android kernel runtime](01_inbox/mobile/android/01_system_internals/kernel-and-hal/android-kernel-runtime.md) 에서 다룬다. 이 묶음은 kernel driver 를 직접 설명하지 않고, driver 위에 있는 HAL service, native service, 앱 native library 가 Android runtime 과 어떤 계약으로 연결되는지에 집중한다.
