---
title: CMake Gradle and ABI define native build and packaging
tags: [android, android/native, android/system-internals]
aliases: [CMake, ABI, externalNativeBuild]
date modified: 2026-07-31 23:58:00 +09:00
date created: 2026-07-31 23:58:00 +09:00
---

CMake는 native source, target, include path, link dependency를 선언한다. Gradle/Android Gradle Plugin은 이 native build를 Android build variant와 연결하고, 결과 `.so`를 ABI별로 앱 패키지에 넣는다.

`abiFilters`는 Gradle이 build 또는 packaging할 ABI 집합을 제한하는 앱 설정이다. 반면 CMake의 `ANDROID_ABI`는 CMake invocation이 어떤 ABI로 configure/build되는지를 나타내는 변수다.

APK 안의 native library는 일반적으로 `lib/<abi>/lib<name>.so` 형태로 들어가야 한다. fat APK는 여러 ABI library를 함께 담아 호환성을 넓히지만 크기가 커지고, App Bundle이나 split은 배포 단위에서 이를 줄일 수 있다.

관련 노트: [NDK는 앱 아키텍처가 아니라 native library toolchain 경계다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/ndk-is-native-library-toolchain-not-app-architecture.md), [Native 성능과 crash debugging은 경계 비용에서 시작한다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/native-performance-and-crash-debugging-start-at-the-boundary.md)

출처: [Add C and C++ code](https://developer.android.com/studio/projects/add-native-code), [Android NDK CMake](https://developer.android.com/ndk/guides/cmake), [Android ABIs](https://developer.android.com/ndk/guides/abis)
