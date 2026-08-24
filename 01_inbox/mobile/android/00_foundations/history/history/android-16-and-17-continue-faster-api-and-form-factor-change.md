---
title: android-16-and-17-continue-faster-api-and-form-factor-change
tags: ["android", "android/foundations"]
aliases: []
date modified: 2026-08-24 17:14:06 +09:00
date created: 2026-07-31 23:04:26 +09:00
---

## Android 16 과 17 은 연 1 회 major API 와 분기별 platform release 를 분리했다

2026 년 8 월 6 일 기준 Android 16 은 API 36, Android 17 은 API 37 이다. Android 17 정식 버전은 2026 년 6 월 16 일 공개됐고, Android 17 QPR1 은 2026 년 7 월 Beta 7 단계다. QPR1 의 API surface 는 Beta 6 에서 Platform Stability 에 도달했지만 QPR beta 와 정식 major release 를 같은 배포 상태로 취급하면 안 된다.

Android 16 부터 platform release 는 분기별로 이어진다. 연간 major release 가 앱에 영향을 주는 behavior change 와 새 major API level 을 담당하고, minor release 는 같은 major 계열 안에서 기능·API 를 추가할 수 있다. 따라서 `SDK_INT`만으로 major 와 minor API 를 모두 구분한다고 가정하지 말고, 필요한 경우 `SDK_INT_FULL`, `VERSION_CODES_FULL`, `Build.getMinorSdkVersion()` 같은 full-version API 를 사용한다.

Android 17 을 target 하는 앱은 API 37 의 target-gated 변화도 별도로 검토한다. 대표적으로 smallest width 가 600dp 보다 큰 display 에서는 orientation, resizability, aspect-ratio 제한과 관련 runtime API 가 원칙적으로 무시된다. Android 16 에 있던 임시 developer opt-out 은 Android 17 에서 제거됐다. 다만 game, 사용자가 aspect-ratio 설정에서 앱 요청 동작을 선택한 경우, `sw600dp` 보다 작은 화면에는 예외가 있다.

### 최신 release 를 판정하는 순서

1. `compileSdk` 와 API availability 를 확인한다.
2. 기기의 runtime major/minor version 을 확인한다.
3. 모든 앱에 적용되는 behavior change 인지 `targetSdkVersion` 으로 gated 된 변화인지 구분한다.
4. phone, large screen, foldable, desktop windowing 같은 form-factor 조건을 확인한다.
5. major 정식 release, QPR 정식 release, QPR beta 의 배포 상태를 구분한다.

이 노트는 기능 목록을 복제하지 않고 빠르게 변하는 checkpoint 와 확인 축만 소유한다.

관련 노트: [API level, codename, extension level, targetSdkVersion은 서로 다른 version 축이다](./api-level-codename-extension-level-and-target-sdk-are-different-version-axes.md), [large screen contracts](../../../07_platforms/large-screens/large-screen.md).

공식 문서(2026-08-06 검증): [Android 16 features](https://developer.android.com/about/versions/16/features), [Android 17](https://developer.android.com/about/versions/17), [Android 17 SDK setup](https://developer.android.com/about/versions/17/setup-sdk), [Android 17 large-screen behavior change](https://developer.android.com/about/versions/17/changes/ff-restrictions-ignored), [Android 17 QPR1 release notes](https://developer.android.com/about/versions/17/qpr1/release-notes).
