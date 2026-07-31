---
title: HAL native contracts
tags: [android, android/native, android/system-internals]
aliases: [HAL native contracts]
date modified: 2026-07-31 23:58:00 +09:00
date created: 2026-07-31 23:58:00 +09:00
---

# HAL native contracts

- [HAL is a stable userspace contract between framework and vendor](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/hal-is-stable-userspace-contract-between-framework-and-vendor.md)
- [Treble separates system and vendor through stable interfaces](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/treble-separates-system-and-vendor-through-stable-interfaces.md)
- [VINTF declares framework vendor compatibility](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/vintf-declares-framework-vendor-compatibility.md)
- [HIDL is legacy Treble interface not new default](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/hidl-is-legacy-treble-interface-not-new-default.md)
- [AIDL HAL is current stable interface for new HALs](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/aidl-hal-is-current-stable-interface-for-new-hals.md)
- [Binderized and passthrough HAL define process boundary](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/binderized-and-passthrough-hal-define-process-boundary.md)
- [Native system services are init managed Binder endpoints](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/native-system-services-are-init-managed-binder-endpoints.md)
- [Native service debugging separates init Binder VINTF SELinux and tombstones](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/native-service-debugging-separates-init-binder-vintf-selinux-and-tombstones.md)
- [NDK is native library toolchain not app architecture](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/ndk-is-native-library-toolchain-not-app-architecture.md)
- [CMake Gradle and ABI define native build and packaging](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/cmake-gradle-and-abi-define-native-build-and-packaging.md)
- [JNI is explicit boundary between managed runtime and native code](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/jni-is-explicit-boundary-between-managed-runtime-and-native-code.md)
- [JNI references have local global and weak lifetimes](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/jni-references-have-local-global-and-weak-lifetimes.md)
- [JNIEnv is thread local and native threads must attach](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/jnienv-is-thread-local-and-native-threads-must-attach.md)
- [JNI strings and arrays have copy pin and release contracts](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/jni-strings-and-arrays-have-copy-pin-and-release-contracts.md)
- [JNI method field IDs and pending exceptions are runtime state](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/jni-method-field-ids-and-pending-exceptions-are-runtime-state.md)
- [AndroidBitmap native access requires format stride and lock lifetime](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/androidbitmap-native-access-requires-format-stride-and-lock-lifetime.md)
- [Native performance and crash debugging start at the boundary](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/native-performance-and-crash-debugging-start-at-the-boundary.md)
