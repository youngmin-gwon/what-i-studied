---
title: "HAL native contracts"
tags: [android, android/native, android/system-internals]
aliases: [HAL native contracts]
date modified: 2026-07-31 23:58:00 +09:00
date created: 2026-07-31 23:58:00 +09:00
---

# HAL native contracts

이 묶음은 native 경계를 하나의 주제가 아니라 세 개의 서로 다른 책임 층으로 나눠 다룬다. (1) framework와 vendor 구현 사이의 HAL/Treble/VINTF 계약, (2) init이 관리하는 native system service, (3) 앱이 실제로 다루는 NDK/JNI 경계다. 앞의 둘은 platform/OEM 엔지니어가 주로 다루는 관찰 대상이고, 마지막은 앱 개발자가 직접 코드를 작성하는 영역이다 — 같은 "native"라는 말을 써도 톤이 달라야 한다.

## 읽는 순서와 문제 분류

- **"이 기능이 어느 partition 책임인가"를 물을 때**: HAL과 Treble/VINTF 순서로 읽는다. [HAL is a stable userspace contract between framework and vendor](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/hal-is-stable-userspace-contract-between-framework-and-vendor.md) → [Treble separates system and vendor through stable interfaces](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/treble-separates-system-and-vendor-through-stable-interfaces.md) → [VINTF declares framework vendor compatibility](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/vintf-declares-framework-vendor-compatibility.md).
- **"이 HAL은 어떤 interface 방식인가"를 구분할 때**: HIDL과 AIDL은 세대가 다른 선택지이고, binderized/passthrough는 그 위의 process 배치 방식이다. [HIDL is legacy Treble interface not new default](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/hidl-is-legacy-treble-interface-not-new-default.md) → [AIDL HAL is current stable interface for new HALs](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/aidl-hal-is-current-stable-interface-for-new-hals.md) → [Binderized and passthrough HAL define process boundary](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/binderized-and-passthrough-hal-define-process-boundary.md).
- **"native process/service가 왜 죽거나 안 뜨는가"를 진단할 때**: [Native system services are init managed Binder endpoints](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/native-system-services-are-init-managed-binder-endpoints.md) → [Native service debugging separates init Binder VINTF SELinux and tombstones](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/native-service-debugging-separates-init-binder-vintf-selinux-and-tombstones.md).
- **"앱에 native 코드를 어떻게 넣고 부르는가"를 물을 때 (여기서부터는 앱 개발자 영역)**: [NDK is native library toolchain not app architecture](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/ndk-is-native-library-toolchain-not-app-architecture.md) → [CMake Gradle and ABI define native build and packaging](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/cmake-gradle-and-abi-define-native-build-and-packaging.md) → [JNI is explicit boundary between managed runtime and native code](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/jni-is-explicit-boundary-between-managed-runtime-and-native-code.md).
- **JNI 호출 규약을 세부적으로 확인할 때**: [JNI references have local global and weak lifetimes](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/jni-references-have-local-global-and-weak-lifetimes.md), [JNIEnv is thread local and native threads must attach](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/jnienv-is-thread-local-and-native-threads-must-attach.md), [JNI strings and arrays have copy pin and release contracts](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/jni-strings-and-arrays-have-copy-pin-and-release-contracts.md), [JNI method field IDs and pending exceptions are runtime state](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/jni-method-field-ids-and-pending-exceptions-are-runtime-state.md), [AndroidBitmap native access requires format stride and lock lifetime](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/androidbitmap-native-access-requires-format-stride-and-lock-lifetime.md)는 각각 독립된 실수 지점(lifetime, thread attach, copy/release, exception state, stride)을 다루므로 증상에 맞는 노트만 골라 읽는다.
- **"native 경로가 느리거나 죽는다"를 마지막으로 진단할 때**: [Native performance and crash debugging start at the boundary](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/native-performance-and-crash-debugging-start-at-the-boundary.md)로 마무리한다.

## 비슷해 보이지만 다른 노트

- HIDL vs AIDL: 둘 다 HAL interface definition language지만 AIDL이 현재 신규 HAL의 기본 선택지이고 HIDL은 legacy다.
- Binderized vs passthrough: interface 언어(HIDL/AIDL) 선택과 별개로, 실행 시 process를 분리하는지(binderized) 같은 process에서 부르는지(passthrough)의 문제다.
- Native system service vs HAL: 둘 다 init이 띄우는 Binder endpoint일 수 있지만, HAL은 hardware abstraction 계약이고 native system service는 반드시 hardware를 추상화하지 않는 framework-facing 서비스도 포함한다.
- JNI 노트들: "JNI가 무엇인가"(is-explicit-boundary)와 "JNI 호출 중 무엇이 깨지는가"(reference lifetime, thread attach, string/array, exception)는 다른 질문이다.
