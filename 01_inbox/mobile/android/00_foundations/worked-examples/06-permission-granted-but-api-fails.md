---
title: 06-permission-granted-but-api-fails
tags: ["android", "android/foundations", "worked-example"]
aliases: ["Permission is granted but the API still fails"]
date modified: 2026-08-04 16:10:00 +09:00
date created: 2026-08-04 03:00:00 +09:00
---

## permission 이 있는데 API 가 실패하는 사례

이 예시는 Learning Spine 9·10 장을 하나의 실제 개발 버그 리포트로 잇는다. "권한이 있다"는 단일한 승인 사실이 아니라, 여러 독립적인 Gate(Manifest, Runtime Permission Grant, AppOps, Feature Hardware/Settings, Foreground Service Type)가 모두 통과해야 최종 API 결과(위치 데이터)를 얻을 수 있다는 9 장의 다계층 보안 게이트 모델을 백그라운드 위치 기능 버그 추적을 통해 명확히 증명한다.

### 시작 상태

앱은 "매장 근처 도착 시 웰컴 알림 제공" 기능을 포함한다. 매니페스트에는 `ACCESS_FINE_LOCATION`, `ACCESS_COARSE_LOCATION`, `ACCESS_BACKGROUND_LOCATION` 이 모두 선언되어 있다. 사용자는 이 기능을 처음 사용할 때 "앱 사용 중에만 허용"(Foreground Location 권한)을 승인한 상태다.

### 입력

사용자가 이 기능을 활성화한 뒤 앱을 이탈하여 다른 앱을 실행하거나 화면을 끈다. 이 앱은 포그라운드 상태에서 백그라운드 상태로 전환된다.

---

### 다계층 실행 흐름 (UI → App Framework → System Server → Kernel)

1. **UI & Framework Layer (Foreground Permission & Request Flow)**
   - 앱은 최초에 `ACCESS_FINE_LOCATION` 과 `ACCESS_COARSE_LOCATION` 을 동시 요청하여 승인받았다.
   - Android 11(API 30) 이상에서는 Foreground 권한과 Background 권한(`ACCESS_BACKGROUND_LOCATION`)을 한 번의 런타임 팝업으로 동시 요청할 경우 시스템이 요청을 무시하고 즉시 거부한다. 따라서 두 요청은 반드시 시점상 분리되어야 한다.
   - 앱이 화면에 떠 있는 동안 `FusedLocationProviderClient.requestLocationUpdates()` 는 정상 동작한다.

2. **App Framework & IPC Layer (Background Transition & Permission Gate Split)**
   - 사용자가 앱을 떠나 백그라운드로 전환되는 순간, `FusedLocationProviderClient` 는 위치 업데이트 요청을 [binder ipc](../../01_system_internals/binder-ipc.md) 를 통해 System Server 의 `LocationManagerService` (LMS) 로 전달한다.
   - LMS 는 요청을 처리하기 전 9 장의 **다단계 Security Gate Check** 를 수행한다.
     - **Gate 1 (PackageManagerService)**: `checkSelfPermission(ACCESS_FINE_LOCATION)` → **Pass (`PERMISSION_GRANTED`)**
     - **Gate 2 (PermissionManagerService)**: `checkSelfPermission(ACCESS_BACKGROUND_LOCATION)` → **Fail (`PERMISSION_DENIED`)**
     - **Gate 3 (AppOpsService)**: `AppOpsManager.checkOpNoThrow(OP_BACKGROUND_LOCATION, uid, pkg)` → **Fail (`MODE_IGNORED` / `MODE_ERRORED`)**

3. **System Server & AppOps Layer (Operation Denial & Downsampling)**
   - Gate 2 와 Gate 3 가 통과하지 못했으므로, `LocationManagerService` 는 런타임 권한(Gate 1)이 `PERMISSION_GRANTED` 임에도 불구하고 앱으로 보내는 백그라운드 위치 콜백 전달을 차단하거나 빈도를 거의 0 에 가깝게 수동 드롭(Throttling / Suppression) 처리한다.
   - 만약 사용자가 "정확한 위치" 스위치를 꺼서 대략적 위치(Coarse Location)만 승인한 경우, `AppOpsManager` 의 `OP_FINE_LOCATION` 이 `MODE_IGNORED` 로 설정되고 `OP_COARSE_LOCATION` 만 `MODE_ALLOWED` 가 된다. 이 경우 LMS 는 예외를 던지지 않고 위치 데이터를 약 3km² 면적으로 spatial downsampling(위경도 뭉개기) 하여 전달한다.

4. **Kernel & Hardware Layer (Sensor & GNSS Hardware Power Management)**
   - LMS 가 앱의 백그라운드 요청을 거부하거나 드롭함에 따라, Kernel 레벨의 GNSS / GPS Hardware HAL 에 요청되는 수신 파워 모드가 `High Accuracy` 에서 `Standby` 또는 `Off` 로 강등된다.
   - 따라서 실제 위치 센서 칩셋은 디바이스의 무지오펜스 영역 진입 이벤트를 감지하더라도 작성 앱으로 H/W Interrupt 를 전달하지 않는다.

---

### 성공 결과 vs 실패 분기 비교

| 평가 항목 | 성공 경로 (Background Permission + AppOps Allowed) | 실패 분기 (Foreground Only / AppOps Denied) |
| :--- | :--- | :--- |
| **권한 승인 상태** | `FINE_LOCATION` + `BACKGROUND_LOCATION` 모두 Granted | `FINE_LOCATION` 은 Granted 이나 `BACKGROUND_LOCATION` 은 Denied |
| **AppOps 모드 (`dumpsys appops`)** | `FINE_LOCATION`: allow, `BACKGROUND_LOCATION`: allow | `FINE_LOCATION`: allow, `BACKGROUND_LOCATION`: ignore |
| **위치 콜백 동작** | 앱 백그라운드 진입 후에도 위치 수신 유지 (시스템 배터리 정책 주기) | 앱 백그라운드 진입 즉시 위치 수신 중단 (콜백 호출 안됨) |
| **알림 발생 여부** | 매장 도착 시 지오펜싱 판정 정상 트리거 → 알림 표시 | 매장에 도착해도 알림이 전혀 발생하지 않음 |
| **개발자 오진 가능성** | - | `checkSelfPermission(FINE_LOCATION)` 만 확인하면 `GRANTED` 로 보여 버그 원인을 찾지 못함 |

---

### 관찰 가능한 신호 및 CLI 진단 명령

1. **Runtime Permission Grant 상태 개별 검증**
   ```bash
   # FINE_LOCATION 과 BACKGROUND_LOCATION 의 grant 상태가 다름을 나란히 확인
   adb shell dumpsys package com.example.storeapp | grep -A 10 "User 0:" | grep -E "ACCESS_FINE_LOCATION|ACCESS_BACKGROUND_LOCATION"
   ```

2. **AppOps Gate 거부 상태 확인 (Permission 승인과 별개 확인)**
   ```bash
   # AppOps 모드가 allow 인지 ignore / default 인지 확인
   adb shell dumpsys appops com.example.storeapp | grep -E "COARSE_LOCATION|FINE_LOCATION|BACKGROUND_LOCATION"

   # cmd appops 명령으로 직접 특정 op 쿼리
   adb shell cmd appops get com.example.storeapp FINE_LOCATION
   adb shell cmd appops get com.example.storeapp BACKGROUND_LOCATION
   ```

3. **System LocationManagerService 의 실시간 등록 Listener 확인**
   ```bash
   # 현재 LMS에 등록된 active location request 및 백그라운드 패키지 갱신 상태 쿼리
   adb shell dumpsys location | grep -A 5 "com.example.storeapp"
   ```

4. **AppOps 모드 강제 재현 명령 (테스트 시 활용)**
   ```bash
   # 런타임 권한은 둔 채로 AppOps만 거부(ignore) 상태로 변경하여 실패 분기 재현
   adb shell cmd appops set com.example.storeapp BACKGROUND_LOCATION ignore
   ```

---

### Android 14 / 15 / 16 특화 동작

- **Foreground Service Type "location" 강제 (Android 14+)**: Android 14 이상에서 앱이 백그라운드 상태에서 continuous location updates 를 수신하려면 `Foreground Service` 를 사용해야 하며, `AndroidManifest.xml` 에 `<service android:foregroundServiceType="location">` 이 반드시 명시되어야 하고, 서비스 시작 시 runtime permission 게이트를 통과해야 한다. Type 미선언 시 `InvalidForegroundServiceTypeException` 이 발생한다.
- **Approximate Location Quantization (Android 12+)**: 사용자가 "대략적 위치(Coarse)"만 승인한 경우 반환되는 `Location.getAccuracy()` 값은 2,000m ~ 5,000m 수준으로 다운샘플링된다. 지오펜싱 반경 판정 로직이 `accuracy` 오차 범위를 반영하지 않으면 "권한도 있고 API 도 성공했지만 도착 판정에 실패하는" 논리적 오류가 발생한다.
- **Background Location Settings Routing (Android 11+)**: `ACCESS_BACKGROUND_LOCATION` 은 앱 내 다이얼로그 팝업이 불가능하며, `Intent(Settings.ACTION_APPLICATION_DETAILS_SETTINGS)` 또는 `ACTION_LOCATION_SOURCE_SETTINGS` 를 통해 사용자를 시스템 설정 앱으로 이동시켜 "항상 허용" 라디오 버튼을 선택하도록 요구해야 한다.

---

### 코드 예시

```kotlin
class LocationPermissionManager(private val context: Context) {

    // 1. 1단계: Foreground 위치 권한 승인 확인
    fun hasForegroundLocationPermission(): Boolean {
        val fine = ContextCompat.checkSelfPermission(context, Manifest.permission.ACCESS_FINE_LOCATION) == PackageManager.PERMISSION_GRANTED
        val coarse = ContextCompat.checkSelfPermission(context, Manifest.permission.ACCESS_COARSE_LOCATION) == PackageManager.PERMISSION_GRANTED
        return fine || coarse
    }

    // 2. 2단계: Background 위치 권한 별도 확인 (Foreground와 동시 요청 금지)
    fun hasBackgroundLocationPermission(): Boolean {
        return if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
            ContextCompat.checkSelfPermission(context, Manifest.permission.ACCESS_BACKGROUND_LOCATION) == PackageManager.PERMISSION_GRANTED
        } else {
            true
        }
    }

    // 3. 3단계: AppOps Gate 검증 (checkSelfPermission이 GRANTED라도 AppOps가 IGNORED일 수 있음)
    fun isLocationAppOpsAllowed(): Boolean {
        val appOpsManager = context.getSystemService(Context.APP_OPS_SERVICE) as AppOpsManager
        val mode = if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
            appOpsManager.unsafeCheckOpNoThrow(
                AppOpsManager.OPSTR_FINE_LOCATION,
                android.os.Process.myUid(),
                context.packageName
            )
        } else {
            @Suppress("DEPRECATION")
            appOpsManager.checkOpNoThrow(
                AppOpsManager.OPSTR_FINE_LOCATION,
                android.os.Process.myUid(),
                context.packageName
            )
        }
        return mode == AppOpsManager.MODE_ALLOWED
    }

    // 4. 4단계: 위치 데이터 수신 시 정밀도(Accuracy) 검증
    fun processLocationUpdate(location: Location) {
        // Coarse location 강등 시 accuracy 범위가 수천 미터에 달할 수 있음
        if (location.accuracy > 500f) {
            Log.w("LocationGate", "Location accuracy is too low (${location.accuracy}m). Geofence check skipped.")
            return
        }
        // 지오펜싱 도착 판정 수행
        checkStoreArrival(location)
    }

    private fun checkStoreArrival(location: Location) { /* ... */ }
}
```

---

### 관련 Diagnostic Runbook

- [04-permission-denial.md](../diagnostic-runbooks/04-permission-denial.md)

### 관련 Learning Spine 장

- [9장 Identity, 권한과 독립적인 security gate](../learning-spine/09-identity-permission-and-independent-security-gates.md)
- [10장 기기 기능 발견과 background execution](../learning-spine/10-device-capability-discovery-and-background-execution.md)

### 관련 원자 노트

- [위치 권한은 foreground와 background 두 단계로 나뉜다](../../04_system_services/device-capabilities/location-contracts/location-permission-splits-into-foreground-and-background-tiers.md)
- [정밀 위치와 대략적 위치는 별도 permission으로 요청한다](../../04_system_services/device-capabilities/location-contracts/precise-and-approximate-location-are-separate-permissions.md)
- [FusedLocationProviderClient는 여러 위치 소스를 하나의 API로 합성한다](../../04_system_services/device-capabilities/location-contracts/fusedlocationproviderclient-merges-multiple-location-sources.md)
- [AppOps는 permission 승인 뒤에도 실행 시점 정책을 추가로 거부할 수 있다](../../04_system_services/service-lookup/service-lookup-contracts/appops-can-deny-after-permission-is-already-granted.md)
- [Permission protection level은 접근 승인 주체를 정의한다](../../05_security_privacy/permissions-and-sandbox/permission-contracts/permission-protection-level-defines-who-can-grant-access.md)

### 공식 근거

- [Access location permissions](https://developer.android.com/develop/sensors-and-location/location/permissions)
- [Android 11 location permissions changes](https://developer.android.com/about/versions/11/privacy/location)
- [Android 12 behavior changes: approximate location](https://developer.android.com/about/versions/12/behavior-changes-12#approximate-location)
- [Android 14 Foreground Service types: location](https://developer.android.com/about/versions/14/changes/fgs-types-required#location)

검증일: 2026-08-04. 이 예시는 Learning Spine 9·10 장 및 Android 12~15 Location Security Gates 원문 대조를 마쳤다.
