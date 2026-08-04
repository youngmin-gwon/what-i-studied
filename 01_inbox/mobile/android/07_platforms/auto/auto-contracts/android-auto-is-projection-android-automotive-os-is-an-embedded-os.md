---
title: android-auto-is-projection-android-automotive-os-is-an-embedded-os
tags: ["android", "android/platforms"]
aliases: []
date modified: 2026-08-04 15:35:00 +09:00
date created: 2026-08-03 18:05:35 +09:00
---

## Android Auto 는 투영이고 Android Automotive OS 는 차량에 내장된 독립 OS 다

상위 문서: [Android 폼 팩터와 플랫폼 확장 지도](../../android-platforms-and-form-factors.md)

관련 지도: [Android Auto/Automotive 계약](./auto-contracts.md)

### 핵심 정의

Android Auto 는 휴대폰에서 앱을 실행한 상태로, 그 화면을 차량 헤드유닛 디스플레이에 투영(projection)하고 차량의 입력(터치스크린, 다이얼 노브)을 휴대폰 앱으로 전달하는 방식이다. 반면 Android Automotive OS(AAOS)는 차량 자체에 내장되어 독립적으로 부팅되는 Android 운영체제이며, 휴대폰 없이도 헤드유닛에서 직접 앱이 실행된다.

### 실행 환경 및 매니페스트 선언 차이

```xml
<!-- Android Auto (Projection) / Automotive Common Manifest Declaration -->
<manifest xmlns:android="http://schemas.android.com/apk/res/android">

    <!-- Android Auto / Automotive 호환 기능 선언 -->
    <uses-feature
        android:name="android.hardware.type.automotive"
        android:required="false" />

    <application>
        <meta-data
            android:name="com.google.android.gms.car.application"
            android:resource="@xml/automotive_app_desc" />
            
        <service
            android:name=".MyCarAppService"
            android:exported="true">
            <intent-filter>
                <action android:name="androidx.car.app.CarAppService" />
                <category android:name="androidx.car.app.category.NAVIGATION" />
            </intent-filter>
        </service>
    </application>
</manifest>
```

### 판단 기준

- 앱이 휴대폰 없이 차량 단독으로 동작해야 한다면 AAOS 를 대상으로 개발해야 하며, Android Auto(투영)로는 이 요구를 충족할 수 없다.
- 반대로 기존 휴대폰 앱을 차량에서 쓰게 하는 것이 목적이면 Android Auto 의 Car App Library 로 화면을 노출하는 것이 AAOS 전용 앱을 새로 개발하는 것보다 적은 노력으로 목표를 달성한다.
- 두 플랫폼은 각각 다른 방식으로 Play 콘솔에 등록되고 심사받는다. "Auto 지원"이라는 표현만으로 어느 플랫폼을 뜻하는지 문서/의사소통에서 반드시 구분한다.

### 경계

- 이 노트는 두 플랫폼의 근본적 차이를 다룬다. 실제 화면 구성 제약은 [Car App Library는 운전 중 배포 콘텐츠를 제한된 템플릿으로만 허용한다](./car-app-library-restricts-content-to-approved-templates.md) 가, 차량 신호 접근은 [Android Automotive는 Car HAL을 통해 차량 신호에 접근한다](./android-automotive-accesses-vehicle-signals-through-car-hal.md) 가 다룬다.

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

