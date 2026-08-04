---
title: "정밀 위치와 대략적 위치는 별도 permission으로 요청한다"
tags: ["android", "android/system-services"]
---

# 정밀 위치와 대략적 위치는 별도 permission으로 요청한다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](01_inbox/mobile/android/04_system_services/android-system-services-and-device-capabilities.md)
관련 지도: [위치 접근 계약](01_inbox/mobile/android/04_system_services/device-capabilities/location-contracts/location-contracts.md)

## 핵심 정의

Android 12(API 31)부터 사용자는 앱이 위치를 요청할 때 `ACCESS_FINE_LOCATION`(정밀)과 `ACCESS_COARSE_LOCATION`(대략, 공식 문서 기준 약 3제곱킬로미터 면적 정도로 뭉개짐)을 별도로 선택할 수 있다. 앱이 두 permission을 모두 선언해도 사용자는 대략적 위치만 승인할 수 있으며, 이 경우 fine 요청도 coarse 정확도로 강등된 값을 받는다.

## 메커니즘

권한 요청 대화상자에 "정확한 위치"와 "대략적 위치" 두 개의 별도 스위치가 나타난다. 사용자가 대략적 위치만 켜면, 시스템은 `ACCESS_FINE_LOCATION`이 매니페스트에 있어도 좌표를 의도적으로 낮은 해상도로 반올림해 반환한다. 앱 코드 입장에서는 API 호출 자체가 실패하지 않고 조용히 낮은 정확도의 값을 받는 형태로 나타난다.

## 판단 기준

- 코드에서 반환된 `Location` 객체의 `accuracy` 값을 확인해 대략적 위치로 강등됐는지 런타임에 판단해야 한다. permission grant 상태만으로는 이를 알 수 없다.
- 지도 상 정밀 마커 표시처럼 fine 정확도가 필수인 기능은 사용자가 coarse만 허용했을 때의 대체 UX(예: 대략적 지역 표시로 전환)를 설계해야 한다.
- 지오펜싱처럼 좁은 반경 판정이 필요한 기능은 대략적 위치로는 신뢰할 수 없다는 점을 요구사항에 명시한다.

## 경계

- 이 노트는 정확도 등급 선택 자체를 다룬다. foreground/background 접근 시점 구분은 [위치 권한은 foreground와 background 두 단계로 나뉜다](01_inbox/mobile/android/04_system_services/device-capabilities/location-contracts/location-permission-splits-into-foreground-and-background-tiers.md)가 다룬다.
- 정확도와 배터리 소모 트레이드오프 자체(주기, priority 선택)는 [FusedLocationProviderClient는 여러 위치 소스를 하나의 API로 합성한다](01_inbox/mobile/android/04_system_services/device-capabilities/location-contracts/fusedlocationproviderclient-merges-multiple-location-sources.md)가 다룬다.

## 관찰 가능한 신호

권한 대화상자를 실기기/에뮬레이터에서 직접 띄워 "정확한 위치" 스위치를 껐다 켰다 하며 반환되는 `Location.getAccuracy()` 값의 변화를 관찰한다. `adb shell dumpsys location`에도 마지막으로 부여된 정확도 등급이 나타난다.

## 공식 문서

- https://developer.android.com/about/versions/12/behavior-changes-12#approximate-location
