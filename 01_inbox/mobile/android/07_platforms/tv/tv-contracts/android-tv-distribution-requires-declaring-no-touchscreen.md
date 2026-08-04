---
title: android-tv-distribution-requires-declaring-no-touchscreen
tags: ["android", "android/platforms"]
aliases: []
date modified: 2026-08-04 15:35:00 +09:00
date created: 2026-08-03 17:27:18 +09:00
---

## Android TV 배포는 터치스크린 미보유를 명시적으로 선언해야 한다

상위 문서: [Android 폼 팩터와 플랫폼 확장 지도](../../android-platforms-and-form-factors.md)

관련 지도: [Android TV 계약](./tv-contracts.md)

### 핵심 정의

매니페스트에 `<uses-feature android:name="android.software.leanback" android:required="true">` 를 선언하고 `<uses-feature android:name="android.hardware.touchscreen" android:required="false">` 를 함께 선언해야, Play 스토어가 이 앱을 Android TV 기기에 배포 가능한 것으로 인식한다. 이 선언이 없으면 앱이 터치스크린을 요구하는 것으로 간주돼 TV 기기의 Play 스토어 검색/설치 대상에서 제외된다.

### 매니페스트 선언 구성 메커니즘

```xml
<!-- AndroidManifest.xml -->
<manifest xmlns:android="http://schemas.android.com/apk/res/android">

    <!-- TV Leanback 지원 및 터치스크린 비필수 선언 -->
    <uses-feature
        android:name="android.software.leanback"
        android:required="false" />
    <uses-feature
        android:name="android.hardware.touchscreen"
        android:required="false" />

    <application
        android:banner="@drawable/tv_app_banner"
        android:icon="@mipmap/ic_launcher">

        <activity
            android:name=".TvMainActivity"
            android:exported="true">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LEANBACK_LAUNCHER" />
            </intent-filter>
        </activity>
    </application>
</manifest>
```

### 판단 기준

- 휴대폰과 TV 를 모두 지원하는 단일 앱이라면 `leanback` 을 필수(`required="true"`)로 선언하지 않고, TV 전용 앱이라면 필수로 선언해 휴대폰 배포 대상에서 자연히 제외되게 한다.
- TV 런처에 노출되려면 배너 이미지와 함께 인텐트 필터에 `LEANBACK_LAUNCHER` 카테고리를 선언해야 한다. 일반 `LAUNCHER` 카테고리만으로는 TV 홈 화면에 나타나지 않는다.
- 터치 전용으로 작성된 UI 컴포넌트가 있다면, TV 에서는 그 흐름 자체가 아예 도달 불가능하지 않은지(대체 d-pad 경로가 있는지) 배포 전에 확인한다.

### 경계

- 이 노트는 Play 배포 조건을 다룬다. 실제 UI 가 d-pad 로 조작 가능한지는 [Android TV는 d-pad/리모컨을 1차 입력으로 가정한다](./android-tv-assumes-d-pad-remote-as-primary-input.md) 와 [10-foot UI는 포커스 기반 탐색을 요구한다](./10-foot-ui-requires-focus-based-navigation.md) 가 다룬다.
- 일반적인 Play 콘솔 배포/서명 절차 자체는 `03_packaging_deployment` 가 다룬다.

### 관측 가능한 증거 (Observable Evidence)

```bash
# 1. 설치된 패키지의 Leanback 및 Touchscreen 선언 수신 검증
adb shell pm dump <package_name> | grep -E "android.software.leanback|android.hardware.touchscreen"

# 2. TV Leanback 런처 액티비티 존재 여부 확인
adb shell cmd package resolve-activity --category android.intent.category.LEANBACK_LAUNCHER <package_name>
```

### 공식 문서

- https://developer.android.com/training/tv/start/hardware
- https://developer.android.com/training/tv/start/start#tv-features

