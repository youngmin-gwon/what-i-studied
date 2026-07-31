---
title: NDK is native library toolchain not app architecture
tags: [android, android/native, android/system-internals]
aliases: [NDK]
date modified: 2026-07-31 23:58:00 +09:00
date created: 2026-07-31 23:58:00 +09:00
---

# NDK is native library toolchain not app architecture

NDK는 Android 앱 계층을 대체하는 아키텍처가 아니라 C/C++ native code를 Android용 shared library로 빌드하고 앱에 넣기 위한 도구 모음이다. 일반 UI, lifecycle, permission, framework API 사용은 여전히 Android app model 위에서 이뤄진다.

NDK를 쓰는 대표 이유는 기존 C/C++ library 재사용, CPU 집약 작업, cross-platform engine 공유다. “C++가 빠르다”는 이유만으로 JNI 경계와 메모리 안전성, ABI별 배포 비용을 무시하면 오히려 복잡도가 커진다.

ABI는 CPU instruction set, calling convention, binary format, C++ name mangling 같은 native binary compatibility 계약이다. 같은 source라도 `arm64-v8a`, `armeabi-v7a`, `x86_64`처럼 ABI별 산출물이 달라질 수 있다.

관련 노트: [CMake, Gradle, ABI는 native build와 packaging 계약을 나눈다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/cmake-gradle-and-abi-define-native-build-and-packaging.md), [JNI는 managed runtime과 native code 사이의 명시적 호출 경계다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/jni-is-explicit-boundary-between-managed-runtime-and-native-code.md)

출처: [Android NDK concepts](https://developer.android.com/ndk/guides/concepts), [Android ABIs](https://developer.android.com/ndk/guides/abis)
