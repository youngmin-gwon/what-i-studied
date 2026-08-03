---
title: android-release-history
tags: ["android", "android/foundations"]
aliases: []
date modified: 2026-08-03 17:22:17 +09:00
date created: 2026-07-31 23:04:26 +09:00
---

## Android Release History 는 안드로이드 플랫폼의 버전별 주요 변화를 요약한 기록이다

Android version history 는 platform contract 변화와 현재 API/version 축을 이해하기 위한 timeline map 이다. 기능을 연대순으로 외우기보다 현재 문제에 어떤 호환성 조건이 적용되는지 찾는 데 쓴다.

### 읽는 순서

1. [Version 축 구분](01_inbox/mobile/android/00_foundations/history/history-contracts/api-level-codename-extension-level-and-target-sdk-are-different-version-axes.md) 에서 device OS, compile SDK, target SDK, extension/minor SDK 를 섞지 않는다.
2. [Contract 변화 지도](01_inbox/mobile/android/00_foundations/history/history-contracts/android-history-is-a-map-of-platform-contract-changes-not-a-feature-list.md) 로 permission, storage, background, update 경계가 언제 달라졌는지 찾는다.
3. [현대화 방향](01_inbox/mobile/android/00_foundations/history/history-contracts/android-modernization-shifted-toward-privacy-updatability-and-adaptive-form-factors.md) 으로 여러 release 에 걸친 흐름을 읽는다.
4. 최신 개발·테스트가 필요할 때만 [Android 16과 17 checkpoint](01_inbox/mobile/android/00_foundations/history/history-contracts/android-16-and-17-continue-faster-api-and-form-factor-change.md) 를 공식 release/behavior 문서와 함께 확인한다.

[History Contracts](01_inbox/mobile/android/00_foundations/history/history-contracts/history-contracts.md) 는 위 원자 노트의 역할 차이와 새 history 노트의 경계를 관리하는 하위 지도다.

### History Notes

- [Android history는 기능 목록이 아니라 platform contract 변화 지도다](01_inbox/mobile/android/00_foundations/history/history-contracts/android-history-is-a-map-of-platform-contract-changes-not-a-feature-list.md)
- [API level, codename, extension level, targetSdkVersion은 서로 다른 version 축이다](01_inbox/mobile/android/00_foundations/history/history-contracts/api-level-codename-extension-level-and-target-sdk-are-different-version-axes.md)
- [Android 현대화는 privacy, updatability, adaptive form factor 쪽으로 이동했다](01_inbox/mobile/android/00_foundations/history/history-contracts/android-modernization-shifted-toward-privacy-updatability-and-adaptive-form-factors.md)
- [Android 16과 17은 빠른 API release와 form factor 변화를 계속 밀고 있다](01_inbox/mobile/android/00_foundations/history/history-contracts/android-16-and-17-continue-faster-api-and-form-factor-change.md)

### Current Checkpoint

2026-08-03 검증 기준 공식 Android Developers 문서는 Android 16/API 36/Baklava 와 Android 17/API 37/Cinnamon Bun 을 노출한다. Android 17 문서는 배포 대상과 페이지에 따라 preview 표기가 남아 있을 수 있으므로, version-specific 판단은 release status, SDK setup, 모든 앱 대상 변화, target SDK 대상 변화를 각각 확인한다.

공식 문서: [Android 16 summary](https://developer.android.com/about/versions/16/summary), [Android 17 behavior changes](https://developer.android.com/about/versions/17/behavior-changes-all), [Build.VERSION](https://developer.android.com/reference/android/os/Build.VERSION)

### 문제 분류

- API 를 compile 할 수 있는가: `compileSdk` 와 API/extension availability 를 확인한다.
- 이 device 에서 API 가 존재하는가: `SDK_INT`, `SDK_INT_FULL`, extension version 을 확인한다.
- 기존 앱 동작이 왜 바뀌었는가: 모든 앱 대상 변화와 `targetSdkVersion` gated 변화를 나눠 본다.
- 특정 화면 크기에서만 달라지는가: version 변화와 form factor 정책을 함께 보되 별도 조건으로 기록한다.

### 경계

이 map 에는 장기적인 contract 변화와 공식 checkpoint 만 둔다. release 별 기능 목록과 migration 절차는 공식 release note 를 정본으로 삼는다.
