---
title: android-auto-vs-automotive-os
tags: ["android", "android/platforms"]
aliases: []
date modified: 2026-08-06 14:48:27 +09:00
date created: 2026-08-03 18:05:35 +09:00
---

## Android Auto 는 투영이고 Android Automotive OS 는 차량에 내장된 독립 OS 다

상위 문서: [Android 폼 팩터와 플랫폼 확장 지도](../android-platforms-and-form-factors.md)

관련 지도: [Android Auto/Automotive 계약](./auto.md)

### 핵심 정의

Android Auto는 휴대폰의 앱과 차량 host가 통신하는 projection 환경이다. Car App Library 앱은 휴대폰 화면 픽셀을 그대로 미러링하는 것이 아니라 앱이 보낸 template model을 차량 host가 렌더링하고 입력을 되돌려 준다. 반면 Android Automotive OS(AAOS)는 차량 자체에 내장되어 독립적으로 부팅되는 Android 운영체제이며, 휴대폰 없이 차량에 설치된 앱이 직접 실행된다.

### 실행 환경 및 매니페스트 선언 차이

Android Auto용 phone/mobile 모듈과 AAOS용 automotive 모듈은 플랫폼별 manifest와 dependency가 다르다. `CarAppService` 구현은 shared module로 재사용할 수 있다.

#### Android Auto (phone/mobile module)

```xml
<!-- phone/mobile module: Android Auto -->
<application>
    <meta-data
        android:name="com.google.android.gms.car.application"
        android:resource="@xml/automotive_app_desc" />
    <service android:name=".MyCarAppService" android:exported="true">
        <intent-filter>
            <action android:name="androidx.car.app.CarAppService" />
            <category android:name="androidx.car.app.category.NAVIGATION" />
        </intent-filter>
    </service>
</application>
```

#### Android Automotive OS (automotive module)

```xml
<!-- automotive module: Android Automotive OS templated app -->
<uses-feature android:name="android.hardware.type.automotive" android:required="true" />
<application>
    <meta-data
        android:name="com.android.automotive"
        android:resource="@xml/automotive_app_desc" />
    <service android:name=".MyCarAppService" android:exported="true">
        <intent-filter>
            <action android:name="androidx.car.app.CarAppService" />
            <category android:name="androidx.car.app.category.NAVIGATION" />
        </intent-filter>
    </service>
    <activity
        android:name="androidx.car.app.activity.CarAppActivity"
        android:exported="true"
        android:launchMode="singleTask"
        android:theme="@android:style/Theme.DeviceDefault.NoActionBar">
        <intent-filter>
            <action android:name="android.intent.action.MAIN" />
            <category android:name="android.intent.category.LAUNCHER" />
        </intent-filter>
    </activity>
</application>
```

AAOS 모듈은 `androidx.car.app:app-automotive`를 사용한다. Android Auto용 `com.google.android.gms.car.application` metadata를 AAOS manifest에 그대로 복사하지 않는다. `automotive_app_desc.xml`의 `template` capability와 `CarAppService` 선언은 각 공식 가이드에 맞춰 함께 둔다.

### 판단 기준

- 앱이 휴대폰 없이 차량 단독으로 동작해야 한다면 AAOS 를 대상으로 개발해야 하며, Android Auto(투영)로는 이 요구를 충족할 수 없다.
- 반대로 기존 휴대폰 앱을 차량에서 쓰게 하는 것이 목적이면 Android Auto 의 Car App Library 로 화면을 노출하는 것이 AAOS 전용 앱을 새로 개발하는 것보다 적은 노력으로 목표를 달성한다.
- Google Play에서는 Android Auto와 AAOS를 서로 다른 form factor 및 release track 요구사항으로 관리하고 차량 앱 품질 심사를 적용한다. 같은 package name과 listing을 재사용하거나 AAOS 전용 track으로 별도 출시할 수 있으므로 항상 "각각 별도 앱으로 등록한다"고 단정하지 않는다.

### 경계

- 이 노트는 두 플랫폼의 근본적 차이를 다룬다. 실제 화면 구성 제약은 [Car App Library는 운전 중 배포 콘텐츠를 제한된 템플릿으로만 허용한다](car-app-library-templates.md) 가, 차량 신호 접근은 [Android Automotive는 Car HAL을 통해 차량 신호에 접근한다](automotive-car-hal-signals.md) 가 다룬다.

### 관측 가능한 증거 (Observable Evidence)

```bash
# 1. 런타임 하드웨어 Automotive 특징 여부 확인
adb shell pm list features | grep -i "automotive"

# 2. Android Auto Desktop Head Unit (DHU) 접속 연결 상태 관측
adb forward tcp:5277 tcp:5277
adb shell dumpsys activity service CarAppService
```

### 공식 문서

- https://developer.android.com/training/cars
- https://source.android.com/docs/automotive/start/what_automotive
- https://developer.android.com/training/cars/apps/auto
- https://developer.android.com/training/cars/apps/automotive-os
- https://developer.android.com/training/cars/distribute

검증일: 2026-08-06. Android Auto와 AAOS의 manifest metadata, AAOS `CarAppActivity`/artifact, Play form-factor track 차이를 최신 공식 가이드로 재확인했다.
