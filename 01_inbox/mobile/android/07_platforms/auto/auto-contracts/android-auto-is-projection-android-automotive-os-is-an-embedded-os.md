---
title: "Android Auto는 투영이고 Android Automotive OS는 차량에 내장된 독립 OS다"
tags: ["android", "android/platforms"]
---

# Android Auto는 투영이고 Android Automotive OS는 차량에 내장된 독립 OS다

상위 문서: [Android 폼 팩터와 플랫폼 확장 지도](01_inbox/mobile/android/07_platforms/android-platforms-and-form-factors.md)
관련 지도: [Android Auto/Automotive 계약](01_inbox/mobile/android/07_platforms/auto/auto-contracts/auto-contracts.md)

## 핵심 정의

Android Auto는 휴대폰에서 앱을 실행한 상태로, 그 화면을 차량 헤드유닛 디스플레이에 투영(projection)하고 차량의 입력(터치스크린, 다이얼 노브)을 휴대폰 앱으로 전달하는 방식이다. 반면 Android Automotive OS(AAOS)는 차량 자체에 내장되어 독립적으로 부팅되는 Android 운영체제이며, 휴대폰 없이도 헤드유닛에서 직접 앱이 실행된다.

## 메커니즘

Android Auto에서는 휴대폰이 USB 또는 무선으로 차량과 연결되어 있어야 하며, 앱 로직과 데이터는 모두 휴대폰에서 실행된다. 헤드유닛은 사실상 디스플레이+입력 장치 역할이다. AAOS에서는 헤드유닛 자체가 Android 기기이므로, 앱은 차량에 직접 설치되고 차량의 시스템 자원(차량 신호, 전용 하드웨어)에 접근할 수 있다. 같은 앱이라도 Android Auto용으로 빌드된 것과 AAOS용으로 빌드된 것은 대상 API 표면과 배포 경로가 다르다.

## 판단 기준

- 앱이 휴대폰 없이 차량 단독으로 동작해야 한다면 AAOS를 대상으로 개발해야 하며, Android Auto(투영)로는 이 요구를 충족할 수 없다.
- 반대로 기존 휴대폰 앱을 차량에서 쓰게 하는 것이 목적이면 Android Auto의 Car App Library로 화면을 노출하는 것이 AAOS 전용 앱을 새로 개발하는 것보다 적은 노력으로 목표를 달성한다.
- 두 플랫폼은 각각 다른 방식으로 Play 콘솔에 등록되고 심사받는다. "Auto 지원"이라는 표현만으로 어느 플랫폼을 뜻하는지 문서/의사소통에서 반드시 구분한다.

## 경계

- 이 노트는 두 플랫폼의 근본적 차이를 다룬다. 실제 화면 구성 제약은 [Car App Library는 운전 중 배포 콘텐츠를 제한된 템플릿으로만 허용한다](01_inbox/mobile/android/07_platforms/auto/auto-contracts/car-app-library-restricts-content-to-approved-templates.md)가, 차량 신호 접근은 [Android Automotive는 Car HAL을 통해 차량 신호에 접근한다](01_inbox/mobile/android/07_platforms/auto/auto-contracts/android-automotive-accesses-vehicle-signals-through-car-hal.md)가 다룬다.

## 관찰 가능한 신호

Android Auto는 휴대폰의 Android Auto 데스크톱 헤드유닛 에뮬레이터로, AAOS는 별도의 Automotive OS 시스템 이미지 에뮬레이터로 각각 다른 도구를 사용해 테스트한다는 사실 자체가 두 플랫폼이 다른 실행 환경임을 보여준다.

## 공식 문서

- https://developer.android.com/training/cars
- https://source.android.com/docs/automotive/start/what_is_android_automotive
