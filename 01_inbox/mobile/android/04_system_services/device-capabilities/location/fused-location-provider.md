---
title: fusedlocationproviderclient-merges-multiple-location-sources
tags: ["android", "android/system-services"]
aliases: ["FusedLocationProviderClient는 여러 위치 소스를 하나의 API로 합성한다"]
date modified: 2026-08-06 14:59:18 +09:00
date created: 2026-08-03 17:19:24 +09:00
---

## FusedLocationProviderClient는 여러 위치 소스를 하나의 API로 합성한다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](../../android-system-services-and-device-capabilities.md)
관련 지도: [위치 접근 계약](./location.md)

### 핵심 정의

`FusedLocationProviderClient`(Google Play services 위치 API)는 GPS, Wi-Fi/셀 기반 네트워크 위치, 기기 센서를 앱이 개별적으로 다루지 않도록 하나의 합성된 위치 스트림으로 제공한다. 플랫폼 기본 `LocationManager`도 존재하지만 대부분의 앱은 배터리 효율과 정확도 균형 때문에 fused 클라이언트를 우선 사용한다.

### 메커니즘

앱은 `Priority`(예: `PRIORITY_HIGH_ACCURACY`, `PRIORITY_BALANCED_POWER_ACCURACY`)와 업데이트 interval을 지정해 **LocationRequest**(위치 요청 빈도, 요구 정확도 수준, 배터리 소모 정책을 설정하는 데이터 객체)를 만든다. 내부적으로 시스템은 이 요청을 다른 앱의 동시 요청과 병합해 실제 하드웨어(GPS 칩, 네트워크 위치 조회)에 필요한 최소한의 작업만 수행한다. 즉 여러 앱이 비슷한 정확도를 요청하면 시스템이 하드웨어 사용을 공유해 배터리를 아낀다.

`getLastLocation()`은 캐시된 최근 위치를 즉시 반환하고, `requestLocationUpdates()`는 콜백으로 새 위치를 스트리밍한다. 두 API는 지연과 정확도 트레이드오프가 다르다.

### 신선도와 수명주기를 포함한 호출 흐름

```kotlin
@RequiresPermission(anyOf = [ACCESS_COARSE_LOCATION, ACCESS_FINE_LOCATION])
suspend fun currentLocation(client: FusedLocationProviderClient): Location? {
    val request = CurrentLocationRequest.Builder()
        .setPriority(Priority.PRIORITY_BALANCED_POWER_ACCURACY)
        .setMaxUpdateAgeMillis(30_000)
        .setDurationMillis(10_000)
        .build()
    return client.getCurrentLocation(request, null).await()
}
```

`lastLocation`은 null이거나 매우 오래된 캐시일 수 있으므로 `Location.time`/`elapsedRealtimeNanos`로 신선도를 검사한다. 일회성 최신 값은 bounded `getCurrentLocation()`을 사용한다. 연속 업데이트는 lifecycle 진입 때 등록하고 이탈 때 같은 callback으로 `removeLocationUpdates()`해 누수와 불필요한 배터리 사용을 막는다.

### 판단 기준

- 즉시 응답이 필요하고 약간의 오차를 허용하면 `getLastLocation()`을 우선 시도한다.
- 연속 추적(내비게이션, 실시간 트래킹)에는 `requestLocationUpdates()`와 적절한 interval을 사용한다. interval을 필요 이상으로 짧게 잡으면 배터리 소모가 커진다.
- 실내처럼 GPS 신호가 약한 환경에서는 fused 결과가 네트워크 기반 위치로 대체되어 정확도가 떨어질 수 있다는 점을 제품 요구사항에 반영한다.

### 경계

- 이 노트는 위치 소스 합성 메커니즘까지만 다룬다. 권한 단계는 [위치 권한은 foreground와 background 두 단계로 나뉜다](./location-permission-tiers.md)가, 정확도 등급 선택은 [정밀 위치와 대략적 위치는 별도 permission으로 요청한다](./precise-and-approximate-location-are-separate-permissions.md)가 다룬다.
- GNSS 원시 측정치나 센서 퓨전 알고리즘 자체의 구현 세부는 다루지 않는다.

### 관찰 가능한 신호

`adb shell dumpsys location`으로 현재 등록된 위치 요청 목록과 마지막 위치 갱신 시각을 확인할 수 있다. 여러 앱이 등록한 요청과 그 priority/interval이 이 출력에 함께 나타난다.

### 공식 문서

- https://developer.android.com/develop/sensors-and-location/location/retrieve-current
- https://developers.google.com/android/reference/com/google/android/gms/location/FusedLocationProviderClient

검증일: 2026-08-06. 캐시 신선도, bounded current-location 요청, callback 해제 흐름을 공식 API로 보강했다.
