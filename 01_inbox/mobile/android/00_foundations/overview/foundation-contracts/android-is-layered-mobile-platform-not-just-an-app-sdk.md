---
title: android-is-layered-mobile-platform-not-just-an-app-sdk
tags: ["android", "android/foundations"]
aliases: []
date modified: 2026-08-03 17:22:39 +09:00
date created: 2026-07-31 23:04:26 +09:00
---

## Android 는 앱 SDK 만이 아니라 계층형 모바일 플랫폼이다

Android 를 앱 API 목록으로만 보면 system behavior 를 설명하기 어렵다. Android 는 Linux kernel, native userspace, HAL, Android Runtime, framework services, app framework, distribution/security policy 가 겹친 플랫폼이다.

앱 개발자가 이 구조를 알아야 하는 이유는 버그와 제약이 API boundary 하나에서 끝나지 않기 때문이다. 예를 들어 camera feature 는 permission, app component, CameraX/Camera2, media pipeline, HAL, vendor implementation 을 지나간다.

입문 문서는 세부 구현을 다시 설명하지 않고 어느 정본으로 가야 하는지를 알려주는 map 이어야 한다.

관련 노트: [kernel/runtime](../../../01_system_internals/kernel-and-hal/android-kernel-runtime.md), [HAL/native boundary](../../../01_system_internals/kernel-and-hal/hal-native-boundary.md), [app architecture](../../../02_app_framework/architecture/android-app-architecture.md), [security/privacy](../../../05_security_privacy/security-practices/security-practice-contracts/android-security-practice-is-defense-in-depth-not-client-trust.md).

공식 문서: [Android Developers](https://developer.android.com/), [Android Open Source Project](https://source.android.com/)
