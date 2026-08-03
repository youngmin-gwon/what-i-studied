---
title: "Android 16 과 17 은 빠른 API release 와 form factor 변화를 계속 밀고 있다"
tags: ["android", "android/foundations"]
aliases: []
date modified: 2026-08-03 16:33:36 +09:00
date created: 2026-07-31 23:04:26 +09:00
---

# Android 16 과 17 은 빠른 API release 와 form factor 변화를 계속 밀고 있다

2026 년 8 월 3 일 검증 기준 Android Developers 문서는 Android 16(API 36)과 Android 17(API 37)을 노출한다. Android 16 은 2025 년부터 major/minor API release cadence 를 도입했고, `SDK_INT_FULL` 은 같은 major API level 안의 minor release 까지 구분한다.

Android 17 의 target SDK 변화에는 large screen 에서 orientation, resizability, aspect ratio 제한을 무시하는 정책의 opt-out 제거가 포함된다. 다만 Android 17 문서는 SDK setup 화면에 preview 표기가 남는 등 페이지별 배포 상태 표현이 다를 수 있으므로, 기능 존재와 안정성·배포 상태를 한 문장으로 단정하지 않는다.

판단할 때는 `compileSdk`/API availability, device runtime version, 모든 앱 대상 behavior change, `targetSdkVersion` gated change, form factor 조건을 각각 확인한다. 이 노트는 최신 feature 를 복사하지 않고 확인 축과 정본만 남긴다.

관련 노트: [large screen contracts](01_inbox/mobile/android/07_platforms/large-screens/large-screen-contracts/large-screen-contracts.md), [Compose UI](01_inbox/mobile/android/02_app_framework/jetpack-compose/layout-and-ui/compose-layout-animation-accessibility.md), [security practices](01_inbox/mobile/android/05_security_privacy/security-practices/security-practice-contracts/android-security-practice-is-defense-in-depth-not-client-trust.md).

공식 문서(2026-08-03 검증): [Android 16 summary](https://developer.android.com/about/versions/16/summary), [Build.VERSION](https://developer.android.com/reference/android/os/Build.VERSION), [Android 17 SDK setup](https://developer.android.com/about/versions/17/setup-sdk), [Android 17 target behavior changes](https://developer.android.com/about/versions/17/behavior-changes-17)
