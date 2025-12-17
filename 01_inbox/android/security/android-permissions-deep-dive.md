---
title: android-permissions-deep-dive
tags: [android, android/permissions, android/security, android/privacy]
aliases: []
date modified: 2025-12-16 16:19:14 +09:00
date created: 2025-12-16 16:19:14 +09:00
---

## Android Permissions Deep Dive android android/permissions android/security android/privacy

안드로이드 권한 시스템을 깊이 있게 다룬다. 기본은 [[android-security-and-sandboxing]] 참고.

### 권한 시스템 개요

권한은 민감한 데이터나 기능에 대한 접근을 제어한다.

**보호 수준 (Protection Level):**
- **normal**: 낮은 위험, 설치 시 자동 부여 (인터넷, 진동)
- **dangerous**: 높은 위험, 사용자 승인 필요 (위치, 카메라, 연락처)
- **signature**: 같은 서명의 앱만 사용 가능
- **signatureOrSystem**: 시스템 앱 또는 같은 서명
- **internal**: 시스템 내부 전용

### 런타임 권한 (Dangerous Permissions)

Android 6.0 (M) 부터 위험 권한은 실행 중에 요청한다.

#### 권한 그룹

관련 권한들이 그룹으로 묶인다. 그룹 내 하나를 허용하면 같은 그룹의 다른 권한도 자동 허용 (단, 여전히 선언 필요).

| 그룹 | 권한 |
|------|------|
| CALENDAR | READ_CALENDAR, WRITE_CALENDAR |
| CAMERA | CAMERA |
| CONTACTS | READ_CONTACTS, WRITE_CONTACTS, GET_ACCOUNTS |
| LOCATION | ACCESS_FINE_LOCATION, ACCESS_COARSE_LOCATION, ACCESS_BACKGROUND_LOCATION |
| MICROPHONE | RECORD_AUDIO |
| PHONE | READ_PHONE_STATE, CALL_PHONE, READ_CALL_LOG, WRITE_CALL_LOG, ADD_VOICEMAIL, USE_SIP, PROCESS_OUTGOING_CALLS |
| SENSORS | BODY_SENSORS |
| SMS | SEND_SMS, RECEIVE_SMS, READ_SMS, RECEIVE_WAP_PUSH, RECEIVE_MMS |
| STORAGE | READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE |

#### 권한 요청 흐름

```kotlin
class MainActivity : AppCompatActivity() {
    private val requestPermissionLauncher = registerForActivityResult(
        ActivityResultContracts.RequestPermission()
    ) { isGranted: Boolean ->
        if (isGranted) {
            // 권한 허용됨
            accessCamera()
        } else {
            // 권한 거부됨
            showPermissionDeniedMessage()
        }
    }
    
    private fun checkAndRequestCamera() {
        when {
            ContextCompat.checkSelfPermission(
                this,
                Manifest.permission.CAMERA
            ) == PackageManager.PERMISSION_GRANTED -> {
                // 이미 권한 있음
                accessCamera()
            }
            
            shouldShowRequestPermissionRationale(Manifest.permission.CAMERA) -> {
                // 이전에 거부했지만 "다시 묻지 않기" 는 선택 안 함
                // 권한이 왜 필요한지 설명
                showRationaleDialog {
                    requestPermissionLauncher.launch(Manifest.permission.CAMERA)
                }
            }
            
            else -> {
                // 처음 요청하거나 "다시 묻지 않기" 선택됨
                requestPermissionLauncher.launch(Manifest.permission.CAMERA)
            }
        }
    }
    
    private fun showRationaleDialog(onPositive: () -> Unit) {
        AlertDialog.Builder(this)
            .setTitle("카메라 권한 필요")
            .setMessage("사진 촬영을 위해 카메라 권한이 필요합니다.")
            .setPositiveButton("확인") { _, _ -> onPositive() }
            .setNegativeButton("취소", null)
            .show()
    }
}
```

#### 여러 권한 동시 요청

```kotlin
private val requestMultiplePermissions = registerForActivityResult(
    ActivityResultContracts.RequestMultiplePermissions()
) { permissions ->
    permissions.entries.forEach { (permission, isGranted) ->
        when (permission) {
            Manifest.permission.CAMERA -> {
                if (isGranted) {
                    // 카메라 권한 허용
                }
            }
            Manifest.permission.RECORD_AUDIO -> {
                if (isGranted) {
                    // 오디오 권한 허용
                }
            }
        }
    }
}

fun requestCameraAndAudio() {
    requestMultiplePermissions.launch(arrayOf(
        Manifest.permission.CAMERA,
        Manifest.permission.RECORD_AUDIO
    ))
}
```

### 특수 권한

일반 권한 다이얼로그로 요청할 수 없는 특수 권한들.

#### 1. SYSTEM_ALERT_WINDOW (다른 앱 위에 표시)

```kotlin
fun checkOverlayPermission() {
    if (!Settings.canDrawOverlays(this)) {
        val intent = Intent(
            Settings.ACTION_MANAGE_OVERLAY_PERMISSION,
            Uri.parse("package:$packageName")
        )
        startActivity(intent)
    }
}
```

#### 2. WRITE_SETTINGS (시스템 설정 수정)

```kotlin
fun checkWriteSettingsPermission() {
    if (!Settings.System.canWrite(this)) {
        val intent = Intent(
            Settings.ACTION_MANAGE_WRITE_SETTINGS,
            Uri.parse("package:$packageName")
        )
        startActivity(intent)
    }
}
```

#### 3. REQUEST_INSTALL_PACKAGES (APK 설치)

```kotlin
fun checkInstallPermission() {
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
        if (!packageManager.canRequestPackageInstalls()) {
            val intent = Intent(
                Settings.ACTION_MANAGE_UNKNOWN_APP_SOURCES,
                Uri.parse("package:$packageName")
            )
            startActivity(intent)
        }
    }
}
```

#### 4. MANAGE_EXTERNAL_STORAGE (모든 파일 접근)

```kotlin
fun checkAllFilesAccess() {
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.R) {
        if (!Environment.isExternalStorageManager()) {
            val intent = Intent(
                Settings.ACTION_MANAGE_APP_ALL_FILES_ACCESS_PERMISSION,
                Uri.parse("package:$packageName")
            )
            startActivity(intent)
        }
    }
}
```

### 위치 권한 상세

Android 10+ 에서 위치 권한이 세분화되었다.

#### 포그라운드 vs 백그라운드

```xml
<!-- AndroidManifest.xml -->
<!-- 포그라운드 위치 (앱 사용 중) -->
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />

<!-- 백그라운드 위치 (항상) - Android 10+ -->
<uses-permission android:name="android.permission.ACCESS_BACKGROUND_LOCATION" />
```

```kotlin
// Android 10+ 에서는 포그라운드 먼저, 백그라운드 나중에 요청
fun requestLocationPermissions() {
    when {
        Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q -> {
            // 1단계: 포그라운드 위치 요청
            requestForegroundLocation()
        }
        else -> {
            // Android 9 이하는 한 번에 요청
            requestPermissionLauncher.launch(Manifest.permission.ACCESS_FINE_LOCATION)
        }
    }
}

private fun requestForegroundLocation() {
    requestPermissionLauncher.launch(Manifest.permission.ACCESS_FINE_LOCATION)
}

private fun requestBackgroundLocation() {
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
        // 2단계: 포그라운드 허용 후 백그라운드 요청
        requestPermissionLauncher.launch(Manifest.permission.ACCESS_BACKGROUND_LOCATION)
    }
}
```

#### 대략적 위치 (Android 12+)

사용자가 정확한 위치 대신 대략적 위치만 허용할 수 있다.

```kotlin
fun checkLocationAccuracy() {
    val hasFineLocation = ContextCompat.checkSelfPermission(
        this, Manifest.permission.ACCESS_FINE_LOCATION
    ) == PackageManager.PERMISSION_GRANTED
    
    val hasCoarseLocation = ContextCompat.checkSelfPermission(
        this, Manifest.permission.ACCESS_COARSE_LOCATION
    ) == PackageManager.PERMISSION_GRANTED
    
    when {
        hasFineLocation -> {
            // 정확한 위치 사용 가능
            requestPreciseLocation()
        }
        hasCoarseLocation -> {
            // 대략적 위치만 사용 가능
            requestApproximateLocation()
            
            // 정확한 위치로 업그레이드 요청 가능
            showUpgradeToFineLocationDialog()
        }
    }
}
```

### 알림 권한 (Android 13+)

Android 13 부터 알림도 런타임 권한이 되었다.

```xml
<uses-permission android:name="android.permission.POST_NOTIFICATIONS" />
```

```kotlin
fun requestNotificationPermission() {
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU) {
        when {
            ContextCompat.checkSelfPermission(
                this,
                Manifest.permission.POST_NOTIFICATIONS
            ) == PackageManager.PERMISSION_GRANTED -> {
                // 알림 권한 있음
            }
            else -> {
                requestPermissionLauncher.launch(Manifest.permission.POST_NOTIFICATIONS)
            }
        }
    }
}
```

### AppOps (Application Operations)

[[android-glossary#appops|AppOps]] 는 권한보다 더 세밀한 제어를 제공한다.

**특징:**
- 권한 사용 시간 추적
- 포그라운드/백그라운드 구분
- 사용자가 "앱 사용 중에만" 허용 가능

```kotlin
// AppOps 사용 여부 확인 (예: 위치)
fun checkLocationAppOps(): Boolean {
    val appOps = getSystemService(Context.APP_OPS_SERVICE) as AppOpsManager
    val mode = if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
        appOps.unsafeCheckOpNoThrow(
            AppOpsManager.OPSTR_FINE_LOCATION,
            android.os.Process.myUid(),
            packageName
        )
    } else {
        appOps.checkOpNoThrow(
            AppOpsManager.OPSTR_FINE_LOCATION,
            android.os.Process.myUid(),
            packageName
        )
    }
    return mode == AppOpsManager.MODE_ALLOWED
}

// 권한 사용 기록 확인
fun getLocationUsageHistory() {
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
        val appOps = getSystemService(Context.APP_OPS_SERVICE) as AppOpsManager
        val ops = appOps.getOpsForPackage(
            android.os.Process.myUid(),
            packageName,
            AppOpsManager.OPSTR_FINE_LOCATION
        )
        // ops 에서 마지막 사용 시간 등 확인 가능
    }
}
```

### 권한 자동 재설정 (Android 11+)

몇 달간 사용하지 않은 앱의 권한이 자동으로 취소된다.

```kotlin
// 자동 재설정 비활성화 요청 (특수한 경우만)
fun requestDisableAutoRevoke() {
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.R) {
        val intent = Intent(Settings.ACTION_APPLICATION_DETAILS_SETTINGS)
        intent.data = Uri.parse("package:$packageName")
        startActivity(intent)
        // 사용자가 수동으로 "권한 자동 삭제 안 함" 선택 필요
    }
}
```

### 커스텀 권한 정의

자신의 앱이 제공하는 기능을 다른 앱이 사용하도록 권한을 정의할 수 있다.

```xml
<!-- 권한 정의 -->
<permission
    android:name="com.example.app.permission.READ_DATA"
    android:label="@string/perm_read_data_label"
    android:description="@string/perm_read_data_desc"
    android:protectionLevel="normal" />

<!-- 컴포넌트에 권한 적용 -->
<provider
    android:name=".MyContentProvider"
    android:authorities="com.example.provider"
    android:readPermission="com.example.app.permission.READ_DATA"
    android:exported="true" />
```

```kotlin
// 코드에서 권한 검사
override fun query(...): Cursor? {
    val result = context?.checkCallingPermission("com.example.app.permission.READ_DATA")
    if (result != PackageManager.PERMISSION_GRANTED) {
        throw SecurityException("Permission denied")
    }
    // 쿼리 처리
}
```

### 권한 위임 (Permission Delegation)

한 앱이 다른 앱에게 임시로 권한을 위임할 수 있다.

#### URI 권한

```kotlin
// 파일 공유 시 읽기 권한 부여
val uri = FileProvider.getUriForFile(
    this,
    "${packageName}.fileprovider",
    file
)

val intent = Intent(Intent.ACTION_VIEW).apply {
    setDataAndType(uri, "image/*")
    flags = Intent.FLAG_GRANT_READ_URI_PERMISSION
}
startActivity(intent)
```

#### PendingIntent 권한

```kotlin
// PendingIntent 를 통해 일시적으로 권한 부여
val intent = Intent(this, TargetActivity::class.java)
val pendingIntent = PendingIntent.getActivity(
    this,
    0,
    intent,
    PendingIntent.FLAG_IMMUTABLE or PendingIntent.FLAG_GRANT_READ_URI_PERMISSION
)
```

### 시스템 권한 검사 흐름

앱이 권한이 필요한 API 를 호출하면:

1. **Framework 레이어**: `Context.checkPermission()` 호출
2. **[[android-activity-manager-and-system-services|ActivityManagerService]]**: UID/PID 와 권한 매핑 확인
3. **PackageManagerService**: 앱이 해당 권한을 선언했는지 확인
4. **AppOpsService**: 런타임 권한 상태 확인
5. **[[android-glossary#selinux|SELinux]]**: 도메인 간 접근 규칙 확인

```bash
# 권한 검사 로그 확인
adb logcat | grep "Permission"

# 특정 앱의 권한 목록
adb shell dumpsys package com.example.app | grep permission

# AppOps 상태
adb shell appops get com.example.app
```

### 베스트 프랙티스

#### 1. 최소 권한 원칙

```kotlin
// ❌ 나쁜 예: 불필요하게 많은 권한
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
<uses-permission android:name="android.permission.READ_CONTACTS" />
<uses-permission android:name="android.permission.CAMERA" />

// ✅ 좋은 예: 필요한 권한만
<uses-permission android:name="android.permission.INTERNET" />
```

#### 2. 컨텍스트 내 요청

```kotlin
// ✅ 사용자가 기능을 사용하려 할 때 요청
button.setOnClickListener {
    checkAndRequestCamera() // 카메라 버튼 클릭 시
}

// ❌ 앱 시작 시 모든 권한 요청
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    requestAllPermissions() // 나쁜 UX
}
```

#### 3. 대안 제시

```kotlin
// 위치 권한 없이도 동작하도록
fun getLocation() {
    if (hasLocationPermission()) {
        // GPS 위치 사용
        useGpsLocation()
    } else {
        // IP 기반 대략적 위치 사용
        useIpBasedLocation()
    }
}
```

#### 4. 투명성

```kotlin
// 권한 사용 목적을 명확히
fun showPermissionRationale() {
    AlertDialog.Builder(this)
        .setTitle("위치 권한 필요")
        .setMessage("주변 맛집을 추천하기 위해 현재 위치가 필요합니다.")
        .setPositiveButton("허용") { _, _ -> requestLocation() }
        .setNegativeButton("취소", null)
        .show()
}
```

### 디버깅

```bash
# 권한 부여/취소
adb shell pm grant com.example.app android.permission.CAMERA
adb shell pm revoke com.example.app android.permission.CAMERA

# 모든 권한 초기화
adb shell pm reset-permissions

# 권한 그룹 확인
adb shell pm list permissions -g

# 특정 앱의 권한 상태
adb shell dumpsys package com.example.app | grep "granted=true"
```

### 더 보기

[[android-security-and-sandboxing]], [[android-app-components-deep-dive]], [[android-storage-systems]], [[android-privacy-features]], [[android-activity-manager-and-system-services]]
