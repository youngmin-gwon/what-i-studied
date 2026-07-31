---
title: Native performance and crash debugging start at the boundary
tags: [android, android/native, android/system-internals]
aliases: [native performance, native crash, LLDB]
date modified: 2026-07-31 23:58:00 +09:00
date created: 2026-07-31 23:58:00 +09:00
---

# Native performance and crash debugging start at the boundary

Native 성능 최적화는 C++ 코드 내부보다 managed/native 경계 비용에서 먼저 시작한다. JNI 호출 횟수, string/array 변환, object reference lifetime, allocation pattern을 줄이지 않으면 native 연산 자체가 빨라도 전체 경로는 느릴 수 있다.

Native crash debugging에는 symbol이 있는 build, ABI, build type, tombstone, logcat, debugger attachment 상태가 함께 필요하다. Android Studio의 LLDB는 C/C++ breakpoint와 native stack 확인에 쓰이고, tombstone은 device에서 발생한 crash의 사후 분석 출발점이다.

성능 도구 선택은 문제에 따라 달라진다. JNI 경계 비용은 call count와 allocation, native CPU hotspot은 profiler, system service/HAL 지연은 Perfetto나 trace, crash는 tombstone과 symbolization을 우선 본다.

관련 노트: [CMake, Gradle, ABI는 native build와 packaging 계약을 나눈다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/cmake-gradle-and-abi-define-native-build-and-packaging.md), [Native service 디버깅은 init, Binder, VINTF, SELinux, tombstone을 분리한다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/native-service-debugging-separates-init-binder-vintf-selinux-and-tombstones.md)

출처: [Android Studio native debugging](https://developer.android.com/studio/debug/native-debugging), [Android JNI tips](https://developer.android.com/ndk/guides/jni-tips)
