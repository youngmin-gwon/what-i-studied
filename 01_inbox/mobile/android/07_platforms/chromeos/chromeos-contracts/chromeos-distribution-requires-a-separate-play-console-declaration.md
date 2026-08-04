---
title: chromeos-distribution-requires-a-separate-play-console-declaration
tags: ["android", "android/platforms"]
aliases: []
date modified: 2026-08-04 15:35:00 +09:00
date created: 2026-08-03 17:30:11 +09:00
---

## ChromeOS 전용 배포는 Play 콘솔에서 Chromebook 지원 여부를 별도로 선언한다

상위 문서: [Android 폼 팩터와 플랫폼 확장 지도](../../android-platforms-and-form-factors.md)

관련 지도: [ChromeOS 고유 계약](./chromeos-contracts.md)

### 핵심 정의

Google Play 콘솔은 앱이 Chromebook 에서 사용 가능한지 여부를 별도 설정(기기 카탈로그의 Chromebook 포함/제외)으로 관리한다. 앱이 특정 하드웨어 기능(예: 카메라, 특정 센서)을 필수로 선언했는데 대상 Chromebook 에 그 하드웨어가 없으면, 해당 기기는 자동으로 배포 대상에서 제외된다.

### 매니페스트 선택적 하드웨어 선언 메커니즘

```xml
<!-- AndroidManifest.xml -->
<manifest xmlns:android="http://schemas.android.com/apk/res/android">

    <!-- Chromebook 호환성을 위해 하드웨어 요구사항을 required=false로 지정 -->
    <uses-feature
        android:name="android.hardware.camera"
        android:required="false" />
    <uses-feature
        android:name="android.hardware.camera.autofocus"
        android:required="false" />
    <uses-feature
        android:name="android.hardware.telephony"
        android:required="false" />

</manifest>
```

### 판단 기준

- 앱이 실제로는 선택적으로만 사용하는 하드웨어 기능(카메라, 특정 센서)을 `required="true"` 로 과도하게 선언하지 않는다. 이는 Chromebook 뿐 아니라 해당 하드웨어가 없는 휴대폰/태블릿 배포에도 영향을 준다.
- Chromebook 전용 UX 검증이 필요한 기능(파일 시스템 접근, 외부 디스플레이 대응)이 있다면 출시 전 Play 콘솔의 기기 카탈로그에서 실제 배포 대상 목록을 확인한다.
- "큰 화면 지원" Play 정책 요구사항(품질 등급)이 Chromebook 에도 적용되므로, large-screen 적응형 레이아웃 완성도가 배포 노출과 검색 순위에도 영향을 줄 수 있다는 점을 인지한다.

### 경계

- 이 노트는 배포 심사와 기기 카탈로그 조건을 다룬다. 실행 환경 자체의 창 매핑 방식은 [ChromeOS는 Android 앱을 컨테이너에서 실행하고 창을 데스크톱 윈도우로 매핑한다](./chromeos-runs-android-apps-in-a-container-mapped-to-desktop-windows.md) 가 다룬다.
- 일반적인 Play 콘솔 배포 절차(서명, 트랙 구성)는 `03_packaging_deployment` 가 다룬다.

### 관측 가능한 증거 (Observable Evidence)

```bash
# 1. 설치 패키지의 하드웨어 피처 요구사항 (required=true/false) 확인
adb shell pm dump <package_name> | grep -A 10 "uses-feature"

# 2. 시스템 호환 하드웨어 기능 목록 검색
adb shell pm list features | grep -E "camera|telephony|sensor"
```

### 공식 문서

- https://developer.android.com/topic/arc
- https://support.google.com/googleplay/android-developer/answer/9844486

