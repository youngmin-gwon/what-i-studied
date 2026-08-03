---
title: "Android Automotive는 Car HAL을 통해 차량 신호에 접근한다"
tags: ["android", "android/platforms"]
---

# Android Automotive는 Car HAL을 통해 차량 신호에 접근한다

상위 문서: [Android 폼 팩터와 플랫폼 확장 지도](01_inbox/mobile/android/07_platforms/android-platforms-and-form-factors.md)
관련 지도: [Android Auto/Automotive 계약](01_inbox/mobile/android/07_platforms/auto/auto-contracts/auto-contracts.md)

## 핵심 정의

AAOS에서 앱이 차량 속도, 기어 위치, 연료/배터리 잔량 같은 차량 신호(Vehicle Property)에 접근하려면 `Car` API(`android.car`)를 통해 Vehicle HAL(VHAL)이 노출하는 프로퍼티를 조회한다. 이 신호는 일반 시스템 서비스가 아니라 차량 제조사가 구현한 별도 HAL 계층에서 온다.

## 메커니즘

앱은 `Car.createCar()`로 `Car` 객체를 얻고, `CarPropertyManager`로 특정 `VehiclePropertyIds`(예: 속도, 기어, 주차 브레이크 상태)를 구독하거나 조회한다. 실제 값은 차량 CAN 버스 등에서 온 신호를 차량 제조사의 VHAL 구현이 Android가 이해하는 프로퍼티 형태로 변환한 것이다. 민감한 프로퍼티(예: 주행 중 제어 관련 신호)는 시스템 권한이나 OEM 서명 앱으로 접근이 제한될 수 있다.

## 판단 기준

- 일반 서드파티 앱이 접근할 수 있는 차량 신호는 제조사와 Android 버전에 따라 다르다는 것을 전제로, 특정 프로퍼티가 실제로 노출되는지 대상 차량에서 확인 없이 가정하지 않는다.
- 주행 중 표시 정보(속도 등)를 이용해 운전자 주의를 분산시키는 기능을 만들 때는 Car App Library의 운전 중 배포 제약과 별개로, 실제 안전 가이드라인을 함께 검토한다.
- 차량 신호를 이용한 기능은 AAOS 전용이며 Android Auto(투영)에서는 이 API 표면 자체를 사용할 수 없다는 점을 [Android Auto는 투영이고 Android Automotive OS는 차량에 내장된 독립 OS다](01_inbox/mobile/android/07_platforms/auto/auto-contracts/android-auto-is-projection-android-automotive-os-is-an-embedded-os.md)와 함께 확인한다.

## 경계

- 이 노트는 차량 신호 접근 경로를 다룬다. 화면 구성 제약은 [Car App Library는 운전 중 배포 콘텐츠를 제한된 템플릿으로만 허용한다](01_inbox/mobile/android/07_platforms/auto/auto-contracts/car-app-library-restricts-content-to-approved-templates.md)가 다룬다.
- HAL 자체의 일반 구조(HIDL/AIDL, HAL 등록)는 `01_system_internals/kernel-and-hal`이 다룬다.

## 관찰 가능한 신호

AAOS 에뮬레이터의 확장 컨트롤 패널에서 속도, 기어 등 가상 차량 신호를 직접 조작해 앱이 `CarPropertyManager` 콜백으로 값을 받는지 확인할 수 있다. `adb shell dumpsys car_service`로 등록된 프로퍼티와 현재 값을 조회할 수 있다.

## 공식 문서

- https://developer.android.com/reference/android/car/hardware/property/CarPropertyManager
- https://source.android.com/docs/automotive/vhal
