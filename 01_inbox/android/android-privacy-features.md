---
title: android-privacy-features
tags: [android, android/privacy, android/security, android/permissions]
aliases: []
date modified: 2025-12-16 16:19:14 +09:00
date created: 2025-12-16 16:19:14 +09:00
---

## Android Privacy Features android android/privacy android/security

최신 Android 프라이버시 기능. 기본은 [[android-permissions-deep-dive]] 와 [[android-security-and-sandboxing]] 참고.

### Privacy Dashboard (Android 12+)

사용자가 권한 사용 내역을 확인할 수 있는 대시보드.

**앱 개발자가 알아야 할 것:**
- 모든 권한 접근이 기록됨
- 타임라인으로 표시됨
- 사용자가 여기서 직접 권한 취소 가능

```kotlin
// 권한 사용 시 명확한 이유 제공
fun requestLocationPermission() {
    // 사용자에게 왜 필요한지 설명
    AlertDialog.Builder(this)
        .setTitle("위치 권한 필요")
        .setMessage("주변 맛집을 추천하기 위해 현재 위치가 필요합니다.")
        .setPositiveButton("허용") { _, _ ->
            requestPermissionLauncher.launch(Manifest.permission.ACCESS_FINE_LOCATION)
        }
        .show()
}
```

### 권한 자동 재설정 (Android 11+)

몇 달간 사용하지 않은 앱의 권한 자동 취소.

```kotlin
// 자동 재설정 비활성화 요청 (특수한 경우만)
fun checkAutoRevokePermissions() {
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.R) {
        val packageManager = packageManager
        val isExempt = packageManager.isAutoRevokeWhitelisted
        
        if (!isExempt) {
            // 사용자에게 설정 화면으로 안내
            val intent = Intent(Settings.ACTION_APPLICATION_DETAILS_SETTINGS)
            intent.data = Uri.parse("package:$packageName")
            startActivity(intent)
        }
    }
}
```

### 대략적 위치 (Android 12+)

사용자가 정확한 위치 대신 대략적 위치만 허용 가능.

```kotlin
fun checkLocationAccuracy() {
    val hasFineLocation = ContextCompat.checkSelfPermission(
        this,
        Manifest.permission.ACCESS_FINE_LOCATION
    ) == PackageManager.PERMISSION_GRANTED
    
    val hasCoarseLocation = ContextCompat.checkSelfPermission(
        this,
        Manifest.permission.ACCESS_COARSE_LOCATION
    ) == PackageManager.PERMISSION_GRANTED
    
    when {
        hasFineLocation -> {
            // 정확한 위치 (~5m)
            requestPreciseLocation()
        }
        hasCoarseLocation -> {
            // 대략적 위치 (~3km)
            requestApproximateLocation()
            
            // 정확한 위치로 업그레이드 요청
            showUpgradeDialog()
        }
        else -> {
            // 권한 없음
            requestLocationPermission()
        }
    }
}

fun showUpgradeDialog() {
    AlertDialog.Builder(this)
        .setTitle("정확한 위치 필요")
        .setMessage("더 정확한 추천을 위해 정확한 위치 권한이 필요합니다.")
        .setPositiveButton("허용") { _, _ ->
            // Android 12+ 에서 정확한 위치로 업그레이드 요청
            requestPermissionLauncher.launch(Manifest.permission.ACCESS_FINE_LOCATION)
        }
        .setNegativeButton("취소", null)
        .show()
}
```

### 클립보드 접근 알림 (Android 12+)

앱이 클립보드를 읽으면 토스트 알림 표시.

```kotlin
// 클립보드 읽기
val clipboard = getSystemService(Context.CLIPBOARD_SERVICE) as ClipboardManager
val clipData = clipboard.primaryClip

if (clipData != null && clipData.itemCount > 0) {
    val text = clipData.getItemAt(0).text
    // Android 12+ 에서 "앱이 클립보드에서 붙여넣었습니다" 알림 표시됨
}

// 민감한 데이터는 클립보드에 넣지 않기
// 또는 즉시 클리어
clipboard.setPrimaryClip(ClipData.newPlainText("", ""))
```

### 마이크/카메라 표시등 (Android 12+)

상태바에 마이크/카메라 사용 중 표시.

```kotlin
// 사용자에게 명확히 알리기
fun startRecording() {
    // 녹음 시작 전 알림
    Toast.makeText(this, "녹음을 시작합니다", Toast.LENGTH_SHORT).show()
    
    // 녹음 중임을 UI 에 표시
    recordingIndicator.visibility = View.VISIBLE
    
    // 실제 녹음
    mediaRecorder.start()
}
```

### 근처 기기 권한 (Android 12+)

Bluetooth, Wi-Fi Direct 등 근처 기기 검색 권한.

```xml
<uses-permission android:name="android.permission.BLUETOOTH_SCAN"
    android:usesPermissionFlags="neverForLocation" />
<uses-permission android:name="android.permission.BLUETOOTH_CONNECT" />
```

```kotlin
fun scanBluetoothDevices() {
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.S) {
        when {
            ContextCompat.checkSelfPermission(
                this,
                Manifest.permission.BLUETOOTH_SCAN
            ) == PackageManager.PERMISSION_GRANTED -> {
                // 스캔 시작
                startBluetoothScan()
            }
            else -> {
                requestPermissionLauncher.launch(Manifest.permission.BLUETOOTH_SCAN)
            }
        }
    } else {
        // Android 11 이하
        startBluetoothScan()
    }
}
```

### 알림 권한 (Android 13+)

알림도 런타임 권한.

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
                // 알림 보내기
                showNotification()
            }
            shouldShowRequestPermissionRationale(Manifest.permission.POST_NOTIFICATIONS) -> {
                // 설명 표시
                showRationaleDialog()
            }
            else -> {
                requestPermissionLauncher.launch(Manifest.permission.POST_NOTIFICATIONS)
            }
        }
    } else {
        // Android 12 이하는 자동 허용
        showNotification()
    }
}
```

### 사진/비디오 선택기 (Android 13+)

전체 저장소 권한 없이 특정 미디어만 선택.

```kotlin
// ❌ 구식: 전체 저장소 권한
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />

// ✅ 신식: Photo Picker 사용
val pickMedia = registerForActivityResult(ActivityResultContracts.PickVisualMedia()) { uri ->
    if (uri != null) {
        // 선택된 이미지 사용
        imageView.setImageURI(uri)
    }
}

fun selectPhoto() {
    pickMedia.launch(PickVisualMediaRequest(ActivityResultContracts.PickVisualMedia.ImageOnly))
}

// 여러 개 선택
val pickMultipleMedia = registerForActivityResult(
    ActivityResultContracts.PickMultipleVisualMedia(5)
) { uris ->
    if (uris.isNotEmpty()) {
        // 선택된 이미지들 사용
    }
}
```

### 정확한 알람 권한 (Android 12+)

정확한 시간에 알람을 울리려면 특수 권한 필요.

```xml
<uses-permission android:name="android.permission.SCHEDULE_EXACT_ALARM" />
```

```kotlin
fun scheduleExactAlarm() {
    val alarmManager = getSystemService(Context.ALARM_SERVICE) as AlarmManager
    
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.S) {
        if (!alarmManager.canScheduleExactAlarms()) {
            // 설정 화면으로 안내
            val intent = Intent(Settings.ACTION_REQUEST_SCHEDULE_EXACT_ALARM)
            startActivity(intent)
            return
        }
    }
    
    // 정확한 알람 설정
    val intent = Intent(this, AlarmReceiver::class.java)
    val pendingIntent = PendingIntent.getBroadcast(
        this, 0, intent,
        PendingIntent.FLAG_IMMUTABLE
    )
    
    alarmManager.setExact(
        AlarmManager.RTC_WAKEUP,
        System.currentTimeMillis() + 60000,
        pendingIntent
    )
}
```

### 백그라운드 위치 (Android 10+)

백그라운드에서 위치 접근은 별도 권한.

```xml
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_BACKGROUND_LOCATION" />
```

```kotlin
fun requestBackgroundLocation() {
    // 1단계: 포그라운드 위치 먼저 요청
    if (ContextCompat.checkSelfPermission(
            this,
            Manifest.permission.ACCESS_FINE_LOCATION
        ) != PackageManager.PERMISSION_GRANTED
    ) {
        requestPermissionLauncher.launch(Manifest.permission.ACCESS_FINE_LOCATION)
        return
    }
    
    // 2단계: 백그라운드 위치 요청 (별도 다이얼로그)
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
        if (ContextCompat.checkSelfPermission(
                this,
                Manifest.permission.ACCESS_BACKGROUND_LOCATION
            ) != PackageManager.PERMISSION_GRANTED
        ) {
            // 명확한 이유 설명
            AlertDialog.Builder(this)
                .setTitle("백그라운드 위치 필요")
                .setMessage("운동 기록을 위해 앱이 백그라운드에서도 위치를 추적해야 합니다.")
                .setPositiveButton("허용") { _, _ ->
                    requestPermissionLauncher.launch(Manifest.permission.ACCESS_BACKGROUND_LOCATION)
                }
                .show()
        }
    }
}
```

### Scoped Storage (Android 10+)

앱별로 저장소 격리. 자세한 내용은 [[android-storage-systems]] 참고.

```kotlin
// ✅ 앱 전용 저장소 (권한 불필요)
val file = File(filesDir, "data.txt")
file.writeText("Hello")

// ✅ MediaStore 사용 (권한 불필요, Android 10+)
val contentValues = ContentValues().apply {
    put(MediaStore.Images.Media.DISPLAY_NAME, "photo.jpg")
    put(MediaStore.Images.Media.MIME_TYPE, "image/jpeg")
    put(MediaStore.Images.Media.RELATIVE_PATH, Environment.DIRECTORY_PICTURES)
}

val uri = contentResolver.insert(MediaStore.Images.Media.EXTERNAL_CONTENT_URI, contentValues)

// ❌ 직접 파일 접근 (Android 10+ 에서 제한)
val legacyFile = File(Environment.getExternalStorageDirectory(), "photo.jpg")
```

### Package Visibility (Android 11+)

다른 앱 목록 조회 제한.

```xml
<!-- 특정 앱 쿼리 -->
<queries>
    <package android:name="com.example.otherapp" />
    
    <!-- Intent 로 쿼리 -->
    <intent>
        <action android:name="android.intent.action.VIEW" />
        <data android:scheme="https" />
    </intent>
    
    <!-- Provider 쿼리 -->
    <provider android:authorities="com.example.provider" />
</queries>
```

```kotlin
// 설치된 앱 확인
val intent = Intent(Intent.ACTION_VIEW, Uri.parse("https://example.com"))
val resolveInfo = packageManager.resolveActivity(intent, PackageManager.MATCH_DEFAULT_ONLY)

if (resolveInfo != null) {
    // 브라우저 앱 있음
    startActivity(intent)
}
```

### 데이터 접근 감사 (Android 11+)

민감한 데이터 접근 추적.

```kotlin
val appOpsManager = getSystemService(Context.APP_OPS_SERVICE) as AppOpsManager

if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.R) {
    appOpsManager.setOnOpNotedCallback(
        mainExecutor,
        object : AppOpsManager.OnOpNotedCallback() {
            override fun onNoted(syncNotedAppOp: SyncNotedAppOp) {
                Log.d("Privacy", "Sync access: ${syncNotedAppOp.op}")
            }
            
            override fun onSelfNoted(syncNotedAppOp: SyncNotedAppOp) {
                Log.d("Privacy", "Self access: ${syncNotedAppOp.op}")
            }
            
            override fun onAsyncNoted(asyncNotedAppOp: AsyncNotedAppOp) {
                Log.d("Privacy", "Async access: ${asyncNotedAppOp.op}")
            }
        }
    )
}
```

### 베스트 프랙티스

#### 1. 최소 권한 원칙

```kotlin
// ❌ 과도한 권한
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
<uses-permission android:name="android.permission.READ_CONTACTS" />
<uses-permission android:name="android.permission.CAMERA" />

// ✅ 필요한 권한만
<uses-permission android:name="android.permission.INTERNET" />
```

#### 2. 투명성

```kotlin
// 권한 사용 목적을 명확히
fun showPermissionRationale() {
    AlertDialog.Builder(this)
        .setTitle("카메라 권한 필요")
        .setMessage("프로필 사진 촬영을 위해 카메라 권한이 필요합니다.")
        .setPositiveButton("허용") { _, _ ->
            requestCameraPermission()
        }
        .setNegativeButton("취소", null)
        .show()
}
```

#### 3. 대안 제공

```kotlin
// 권한 없이도 기능 제공
fun getLocation() {
    if (hasLocationPermission()) {
        // GPS 위치
        useGpsLocation()
    } else {
        // IP 기반 대략적 위치
        useIpBasedLocation()
    }
}
```

#### 4. 적시 요청

```kotlin
// ✅ 기능 사용 시점에 요청
button.setOnClickListener {
    checkAndRequestCamera()
}

// ❌ 앱 시작 시 모든 권한 요청
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    requestAllPermissions() // 나쁜 UX
}
```

### 더 보기

[[android-permissions-deep-dive]], [[android-security-and-sandboxing]], [[android-storage-systems]], [[android-app-components-deep-dive]]
