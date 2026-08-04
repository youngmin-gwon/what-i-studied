---
title: 06-permission-granted-but-api-fails
tags: ["android", "android/foundations", "worked-example"]
aliases: ["Permission is granted but the API still fails"]
date modified: 2026-08-04 10:29:08 +09:00
date created: 2026-08-04 03:00:00 +09:00
---

## permission 이 있는데 API 가 실패하는 사례

이 예시는 Learning Spine 9·10 장을 하나의 버그 리포트로 잇는다. "권한이 있다"는 하나의 사실이 아니라 여러 독립적인 gate 가 모두 통과해야 한다는 9 장의 모델을, 백그라운드 위치라는 구체적인 기능으로 추적한다.

### 시작 상태

앱은 "매장 근처에 도착하면 알림"이라는 기능을 제공한다. 매니페스트에는 `ACCESS_FINE_LOCATION`, `ACCESS_COARSE_LOCATION`, `ACCESS_BACKGROUND_LOCATION` 이 모두 선언돼 있다(3·4 장의 registry 등록). 사용자는 이 기능을 처음 켤 때 "앱 사용 중에만 허용"(foreground 권한)을 승인했다.

### 입력

사용자가 이 기능을 켠 뒤 앱을 벗어나 다른 일을 한다. 이 앱은 이제 background 상태다.

### 공통 단계

1. **권한 요청 순서(9 장)**: 앱은 foreground 위치 권한을 먼저 요청했고 사용자가 승인했다. 이 시점에는 `ACCESS_BACKGROUND_LOCATION` 을 별도로 요청하지 않았다 — Android 11(API 30) 이상에서는 foreground 와 background 권한을 동시에 요청하면 시스템이 요청 자체를 무시하기 때문에, 두 요청은 서로 다른 시점에 나뉘어야 한다.
2. **foreground 에서의 동작**: 사용자가 앱을 보고 있는 동안 `FusedLocationProviderClient.requestLocationUpdates()` 는 정상적으로 위치를 스트리밍한다. 도착 감지 로직이 잘 동작하는 것처럼 보인다.
3. **백그라운드 전환**: 사용자가 다른 앱으로 전환하는 순간, 이후의 결과는 background 권한 승인 여부에 따라 완전히 달라진다.

### 성공 결과: background 권한까지 승인된 경우

1. 앱은 foreground 권한이 승인된 뒤, 이 기능이 실제로 백그라운드 동작을 필요로 한다는 것을 설명하는 화면을 보여주고, 사용자를 시스템 설정으로 유도해 "항상 허용"을 선택하게 한다. Android 11 이상에서는 이 승인을 시스템 다이얼로그로 즉시 받을 수 없고, 설정 화면에서 사용자가 직접 선택해야 한다.
2. `ACCESS_BACKGROUND_LOCATION` 이 승인되면, 앱이 백그라운드에 있어도 위치 업데이트가 이어진다(배터리 최적화 정책에 따라 빈도는 낮아질 수 있다).
3. 도착 감지 로직은 백그라운드에서도 계속 실행되고, 조건이 만족되면 알림이 표시된다.

### 실패 분기: background 권한이 없는 경우(신고된 버그)

1. 사용자가 foreground 권한만 승인하고 background 권한 요청 흐름을 아예 거치지 않았거나 거부했다.
2. 앱이 백그라운드로 전환되는 순간, 위치 콜백은 중단되거나 빈도가 크게 낮아진다.
3. 사용자 리포트: "포그라운드에서는 도착 알림이 잘 되는데, 화면을 끄면 알림이 안 옵니다."
4. 개발자가 "권한이 있는데 왜 안 될까"라고 생각하며 `ACCESS_FINE_LOCATION` 의 grant 상태만 확인하면, 그 권한은 실제로 granted 상태이므로 원인을 찾지 못한다.
5. 올바른 조사는 9 장의 gate 순서를 그대로 따른다. 매니페스트 선언(존재) → `ACCESS_FINE_LOCATION` 의 runtime grant(존재) → `ACCESS_BACKGROUND_LOCATION` 의 runtime grant 를 **별도로** 확인해야 한다. 이 권한이 없다는 것이 실제 원인이다.

이 실패는 permission 이라는 단어 하나로 뭉뚱그리면 보이지 않는다. foreground 권한과 background 권한은 같은 데이터(위치)에 대한 같은 permission grant 가 아니라, 서로 다른 시점에 서로 다른 방식으로 승인되는 두 개의 독립적인 gate 다.

### 추가로 걸릴 수 있는 층위: 정확도 강등

background 권한이 있어도 사용자가 "정확한 위치" 스위치를 꺼서 대략적 위치(coarse, 공식 문서 기준 약 3 제곱킬로미터 면적으로 뭉개짐)만 허용했을 수 있다. 이 경우 앱 코드가 예외 없이 정상적으로 `Location` 객체를 받지만, `accuracy` 값이 지오펜싱 반경 판정에 쓰기엔 너무 낮을 수 있다. 이 층위는 권한 grant 여부로는 드러나지 않으며, 반환된 `Location.getAccuracy()` 값을 직접 확인해야 알 수 있다.

### 관찰 가능한 신호

- `adb shell dumpsys package <pkg>` 의 `runtime permissions` 섹션에서 `ACCESS_FINE_LOCATION` 과 `ACCESS_BACKGROUND_LOCATION` 의 grant 상태를 각각 확인한다. 하나만 보고 판단하지 않는다.
- `adb shell dumpsys location` 으로 현재 등록된 위치 요청과 마지막 갱신 시각을 확인한다. 백그라운드 진입 후 갱신이 멈췄다면 이 출력에서 드러난다.
- 반환된 `Location.getAccuracy()` 값을 로그로 남겨 대략적 위치로 강등됐는지 별도로 확인한다.
- `dumpsys appops` 로 `COARSE_LOCATION`/`FINE_LOCATION` op 모드가 permission grant 상태와 별개로 거부돼 있지 않은지 확인한다(9 장의 AppOps gate).

### 코드 예시

```kotlin
// 1. foreground 권한을 먼저 요청한다.
fun requestForegroundLocation() {
    requestPermissionLauncher.launch(
        arrayOf(Manifest.permission.ACCESS_FINE_LOCATION, Manifest.permission.ACCESS_COARSE_LOCATION)
    )
}

// background 권한은 foreground 승인 이후, 별도 시점에 설명과 함께 요청한다.
fun requestBackgroundLocationIfNeeded() {
    val hasForeground = ContextCompat.checkSelfPermission(
        context, Manifest.permission.ACCESS_FINE_LOCATION
    ) == PackageManager.PERMISSION_GRANTED
    val hasBackground = ContextCompat.checkSelfPermission(
        context, Manifest.permission.ACCESS_BACKGROUND_LOCATION
    ) == PackageManager.PERMISSION_GRANTED

    if (hasForeground && !hasBackground) {
        showBackgroundLocationRationale() // "항상 허용"으로 유도하는 설명 화면
    }
}

// 5. 진단: 두 권한과 정확도를 각각 확인한다.
fun diagnoseLocationIssue(location: Location?) {
    val fine = hasPermission(Manifest.permission.ACCESS_FINE_LOCATION)
    val background = hasPermission(Manifest.permission.ACCESS_BACKGROUND_LOCATION)
    Log.d("LocationDiag", "fine=$fine background=$background accuracy=${location?.accuracy}")
}
```

### 관련 원자 노트

- [위치 권한은 foreground와 background 두 단계로 나뉜다](../../04_system_services/device-capabilities/location-contracts/location-permission-splits-into-foreground-and-background-tiers.md)
- [정밀 위치와 대략적 위치는 별도 permission으로 요청한다](../../04_system_services/device-capabilities/location-contracts/precise-and-approximate-location-are-separate-permissions.md)
- [FusedLocationProviderClient는 여러 위치 소스를 하나의 API로 합성한다](../../04_system_services/device-capabilities/location-contracts/fusedlocationproviderclient-merges-multiple-location-sources.md)
- [AppOps는 permission 승인 뒤에도 실행 시점 정책을 추가로 거부할 수 있다](../../04_system_services/service-lookup/service-lookup-contracts/appops-can-deny-after-permission-is-already-granted.md)
- [Permission protection level은 접근 승인 주체를 정의한다](../../05_security_privacy/permissions-and-sandbox/permission-contracts/permission-protection-level-defines-who-can-grant-access.md)

### 관련 Learning Spine 장

- [9장 Identity, 권한과 독립적인 security gate](../learning-spine/09-identity-permission-and-independent-security-gates.md)
- [10장 기기 기능 발견과 background execution](../learning-spine/10-device-capability-discovery-and-background-execution.md)

### 공식 근거

- [Access location permissions](https://developer.android.com/develop/sensors-and-location/location/permissions)
- [Android 11 location permissions changes](https://developer.android.com/about/versions/11/privacy/location)
- [Android 12 behavior changes: approximate location](https://developer.android.com/about/versions/12/behavior-changes-12#approximate-location)

검증일: 2026-08-04. 이 예시는 9·10 장에서 이미 원문 대조를 마친 위치 권한 관련 원자 노트를 재사용했다.
