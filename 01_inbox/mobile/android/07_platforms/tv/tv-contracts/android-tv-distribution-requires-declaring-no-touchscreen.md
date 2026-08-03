---
title: "Android TV 배포는 터치스크린 미보유를 명시적으로 선언해야 한다"
tags: ["android", "android/platforms"]
---

# Android TV 배포는 터치스크린 미보유를 명시적으로 선언해야 한다

상위 문서: [Android 폼 팩터와 플랫폼 확장 지도](01_inbox/mobile/android/07_platforms/android-platforms-and-form-factors.md)
관련 지도: [Android TV 계약](01_inbox/mobile/android/07_platforms/tv/tv-contracts/tv-contracts.md)

## 핵심 정의

매니페스트에 `<uses-feature android:name="android.software.leanback" android:required="true">`를 선언하고 `<uses-feature android:name="android.hardware.touchscreen" android:required="false">`를 함께 선언해야, Play 스토어가 이 앱을 Android TV 기기에 배포 가능한 것으로 인식한다. 이 선언이 없으면 앱이 터치스크린을 요구하는 것으로 간주돼 TV 기기의 Play 스토어 검색/설치 대상에서 제외된다.

## 메커니즘

Google Play는 기기 호환성을 매니페스트의 `<uses-feature>` 선언으로 판단한다. 대부분의 안드로이드 앱은 터치스크린을 암묵적으로 필요로 하는 것으로 취급되므로, TV처럼 터치스크린이 없는 기기에는 기본적으로 노출되지 않는다. `leanback` 기능을 필수로 선언하면 Play는 이 앱을 TV용 앱 카테고리로 분류하고, TV 기기의 홈 화면 런처(Leanback launcher)에 표시할 배너 이미지(`android:banner`)도 별도로 요구한다.

## 판단 기준

- 휴대폰과 TV를 모두 지원하는 단일 앱이라면 `leanback`을 필수(`required="true"`)로 선언하지 않고, TV 전용 앱이라면 필수로 선언해 휴대폰 배포 대상에서 자연히 제외되게 한다.
- TV 런처에 노출되려면 배너 이미지와 함께 인텐트 필터에 `LEANBACK_LAUNCHER` 카테고리를 선언해야 한다. 일반 `LAUNCHER` 카테고리만으로는 TV 홈 화면에 나타나지 않는다.
- 터치 전용으로 작성된 UI 컴포넌트가 있다면, TV에서는 그 흐름 자체가 아예 도달 불가능하지 않은지(대체 d-pad 경로가 있는지) 배포 전에 확인한다.

## 경계

- 이 노트는 Play 배포 조건을 다룬다. 실제 UI가 d-pad로 조작 가능한지는 [Android TV는 d-pad/리모컨을 1차 입력으로 가정한다](01_inbox/mobile/android/07_platforms/tv/tv-contracts/android-tv-assumes-d-pad-remote-as-primary-input.md)와 [10-foot UI는 포커스 기반 탐색을 요구한다](01_inbox/mobile/android/07_platforms/tv/tv-contracts/10-foot-ui-requires-focus-based-navigation.md)가 다룬다.
- 일반적인 Play 콘솔 배포/서명 절차 자체는 `03_packaging_deployment`가 다룬다.

## 관찰 가능한 신호

Play 콘솔의 "기기 카탈로그" 또는 "지원 기기" 화면에서 실제로 Android TV 기기가 배포 대상에 포함되는지 확인할 수 있다. 매니페스트 선언 누락 시 TV 기기에서 Play 스토어 검색 결과 자체에 앱이 나타나지 않는 것으로 문제를 재현할 수 있다.

## 공식 문서

- https://developer.android.com/training/tv/start/hardware
- https://developer.android.com/training/tv/start/start#tv-features
