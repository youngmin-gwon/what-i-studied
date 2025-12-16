---
title: android-modular-system
tags: [android, android/apex, android/mainline, android/modules]
aliases: []
date modified: 2025-12-16 16:19:14 +09:00
date created: 2025-12-16 16:19:14 +09:00
---

## Android Modular System android android/apex android/mainline

[[android-glossary#apex|APEX]] 와 Mainline 모듈 시스템. 기본은 [[android-evolution-history]] 참고.

### Mainline 이란

Android 10 부터 도입된 모듈식 업데이트 시스템. OS 의 핵심 부분을 Google Play 를 통해 독립적으로 업데이트.

**장점:**
- OEM 업데이트 없이 보안 패치 가능
- 새 기능을 빠르게 배포
- 파편화 감소

### APEX (Android Pony EXpress)

APK 와 유사하지만 시스템 컴포넌트용 패키지 형식.

**특징:**
- 서명 검증
- 원자적 업데이트 (실패 시 롤백)
- 부팅 시 마운트
- 읽기 전용

### Mainline 모듈 목록

| 모듈 | 설명 |
|------|------|
| ART | Android Runtime |
| Conscrypt | TLS/SSL 라이브러리 |
| Media | 미디어 코덱 |
| MediaProvider | 미디어 저장소 |
| DocumentsUI | 파일 선택기 |
| ExtServices | 텍스트 분류 등 |
| NetworkStack | 네트워크 스택 |
| CaptivePortalLogin | 캡티브 포털 처리 |
| ModuleMetadata | 모듈 메타데이터 |
| DNS Resolver | DNS 리졸버 |
| PermissionController | 권한 UI |
| Tethering | 테더링 |
| Timezone Data | 시간대 데이터 |

### APEX 구조

```
apex_file.apex
├── apex_manifest.pb (메타데이터)
├── apex_payload.img (파일 시스템 이미지)
│   ├── bin/
│   ├── lib/
│   ├── lib64/
│   └── etc/
└── apex_pubkey (공개 키)
```

### APEX 빌드 (AOSP)

```python
# Android.bp
apex {
    name: "com.android.mymodule",
    manifest: "apex_manifest.json",
    file_contexts: ":mymodule-file_contexts",
    key: "com.android.mymodule.key",
    certificate: ":com.android.mymodule.certificate",
    
    native_shared_libs: [
        "libmymodule",
    ],
    
    binaries: [
        "mymodule_daemon",
    ],
    
    prebuilts: [
        "mymodule_config",
    ],
    
    updatable: true,
    min_sdk_version: "30",
}
```

```json
// apex_manifest.json
{
  "name": "com.android.mymodule",
  "version": 1,
  "versionName": "1.0.0"
}
```

### APEX 설치 흐름

1. **다운로드**: Play Store 에서 APEX 다운로드
2. **검증**: 서명 확인
3. **스테이징**: `/data/apex/active` 에 복사
4. **재부팅**: 다음 부팅 시 활성화
5. **마운트**: `/apex/<module_name>` 에 마운트
6. **롤백 준비**: 이전 버전 유지

### APEX 확인

```bash
# 설치된 APEX 목록
adb shell pm list packages --apex-only

# APEX 정보
adb shell pm dump com.android.runtime

# 마운트된 APEX
adb shell ls /apex/

# APEX 버전
adb shell dumpsys apex
```

### 앱에서 모듈 버전 확인

```kotlin
fun getModuleVersion(moduleName: String): Long? {
    val packageManager = packageManager
    return try {
        val packageInfo = packageManager.getPackageInfo(
            moduleName,
            PackageManager.MATCH_APEX
        )
        packageInfo.longVersionCode
    } catch (e: PackageManager.NameNotFoundException) {
        null
    }
}

// 사용
val artVersion = getModuleVersion("com.android.runtime")
Log.d("APEX", "ART version: $artVersion")
```

### 모듈 호환성

#### VINTF (Vendor Interface)

시스템과 벤더 파티션 간 호환성 계약.

```xml
<!-- device_manifest.xml -->
<manifest version="1.0" type="device">
    <hal format="aidl">
        <name>android.hardware.camera.provider</name>
        <version>1</version>
        <interface>
            <name>ICameraProvider</name>
            <instance>default</instance>
        </interface>
    </hal>
</manifest>
```

```xml
<!-- framework_compatibility_matrix.xml -->
<compatibility-matrix version="1.0" type="framework">
    <hal format="aidl" optional="false">
        <name>android.hardware.camera.provider</name>
        <version>1</version>
        <interface>
            <name>ICameraProvider</name>
            <instance>default</instance>
        </interface>
    </hal>
</compatibility-matrix>
```

### SDK Extensions

Android 11+ 에서 SDK 를 모듈식으로 업데이트.

```kotlin
// SDK Extension 레벨 확인
val extensionVersion = if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.R) {
    SdkExtensions.getExtensionVersion(Build.VERSION_CODES.R)
} else {
    0
}

// 특정 기능 사용 가능 여부
if (extensionVersion >= 5) {
    // Android 11 Extension 5 기능 사용
    useNewFeature()
}
```

```kotlin
// build.gradle.kts
android {
    compileSdkExtension = 5
}
```

### 모듈 업데이트 정책

#### 자동 업데이트

```kotlin
// Play Core 라이브러리로 모듈 업데이트 확인
val moduleUpdateManager = ModuleUpdateManager.create(this)

val request = ModuleUpdateRequest.newBuilder()
    .addModule("com.google.android.gms.vision")
    .build()

moduleUpdateManager.deferredInstall(request)
    .addOnSuccessListener {
        // 업데이트 예약됨
    }
    .addOnFailureListener { e ->
        // 실패
    }
```

### 롤백

APEX 업데이트 실패 시 자동 롤백.

```bash
# 롤백 트리거
adb shell pm rollback-app com.android.runtime

# 롤백 히스토리
adb shell dumpsys rollback
```

### 개발자 고려사항

#### 1. 모듈 의존성

```kotlin
// 특정 모듈 버전에 의존
if (getModuleVersion("com.android.media") ?: 0 < 300000000) {
    // 구버전 대응 코드
    useLegacyMediaCodec()
} else {
    // 신버전 기능 사용
    useNewMediaCodec()
}
```

#### 2. API 호환성

```kotlin
// SDK Extension 기반 분기
when {
    Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU -> {
        // Android 13 기능
    }
    Build.VERSION.SDK_INT >= Build.VERSION_CODES.R &&
        SdkExtensions.getExtensionVersion(Build.VERSION_CODES.R) >= 5 -> {
        // Android 11 Extension 5 기능
    }
    else -> {
        // 폴백
    }
}
```

#### 3. 테스트

```kotlin
// 다양한 모듈 버전에서 테스트
@Test
fun testWithDifferentModuleVersions() {
    // 모듈 버전별 동작 확인
    val moduleVersion = getModuleVersion("com.android.runtime")
    
    when {
        moduleVersion == null -> {
            // 모듈 없음
        }
        moduleVersion < 300000000 -> {
            // 구버전 테스트
        }
        else -> {
            // 신버전 테스트
        }
    }
}
```

### Treble

Vendor 와 System 분리 (Android 8.0+).

**구조:**
```
System Partition (Google)
    ↓ HIDL/AIDL
Vendor Partition (OEM)
    ↓
Hardware
```

**장점:**
- OEM 이 커널/드라이버만 업데이트하면 됨
- Google 이 시스템 업데이트 독립적으로 제공
- 업데이트 속도 향상

### GKI (Generic Kernel Image)

Android 11+ 에서 커널도 모듈화.

**구조:**
```
GKI (Generic Kernel)
    ↓
Vendor Modules (OEM 드라이버)
```

**장점:**
- 커널 보안 패치 빠르게 배포
- OEM 은 드라이버만 관리
- 파편화 감소

### 더 보기

[[android-evolution-history]], [[android-customization-and-oem]], [[android-boot-flow]], [[android-hal-and-kernel]]
