---
title: android-security-and-sandboxing
tags: [android, android/sandbox, android/security]
aliases: [Android Security, Sandboxing, 안드로이드 보안]
date modified: 2026-01-20 15:55:52 +09:00
date created: 2025-12-16 15:24:27 +09:00
---

## Android Security 와 Sandboxing

안드로이드 보안 모델은 **Defense in Depth(다층 방어)** 원칙을 따른다. 앱 샌드박싱, 권한 시스템, [SELinux](../../../../selinux.md), 암호화, Verified Boot 등 여러 계층의 보안 메커니즘이 협력하여 사용자 데이터와 시스템을 보호한다. 모바일 환경의 특성상 ― 신뢰할 수 없는 써드파티 앱 수백만 개, 분실/도난 위험, 다양한 공격 벡터 ― 때문에 매우 정교한 보안 아키텍처가 필요하다.

### 왜 안드로이드는 특별한 보안이 필요한가

#### 모바일 환경의 위협 (2000 년대 후반~현재)

**데스크톱과의 차이**:

1. **신뢰할 수 없는 앱 생태계**:
   - Play Store: 수백만 개 앱, 매일 수천 개 신규 등록
   - 악의적 앱, 스파이웨어, 애드웨어 혼재
   - 사용자는 앱 내부를 알 수 없음

2. **민감한 개인정보 집중**:
   - 연락처, 위치, 사진, 메시지, 통화 기록
   - 금융 앱 (은행, 결제)
   - 생체인증 데이터

3. **물리적 접근 위험**:
   - 분실, 도난
   - 공격자가 디바이스를 물리적으로 소유

4. **다양한 공격 벡터**:
   - 네트워크 (공용 Wi-Fi)
   - USB (Juice Jacking)
   - NFC
   - 블루투스

#### 초기 안드로이드의 취약점 (Android 1.0~2.3)

```mermaid
graph TB
    Problem1[권한이 설치 시<br/>일괄 승인]
    Problem2[외부 저장소<br/>모두 접근]
    Problem3[앱 간 데이터<br/>쉽게 접근]
    Problem4[루팅 쉬움]
    
    Problem1 --> Malware[악성 앱 많음]
    Problem2 --> Privacy[프라이버시 침해]
    Problem3 --> DataLeak[데이터 유출]
    Problem4 --> RootKit[루트킷 설치]
```

---

## 핵심 보안 메커니즘 진화

### Timeline: 보안 기능 도입

| Android 버전 | 주요 보안 기능 |
|-------------|----------------|
| **1.0** (2008) | UID 기반 샌드박싱, 권한 시스템 |
| **3.0** (2011) | 전체 디스크 암호화 |
| **4.3** (2013) | [SELinux](../../../../selinux.md) (permissive) |
| **5.0** (2014) | SELinux enforcing, Smart Lock |
| **6.0** (2015) | **런타임 권한**, 지문인증 API |
| **7.0** (2016) | 파일 기반 암호화 (FBE), Direct Boot |
| **8.0** (2017) | Treble, GMS Integrity |
| **9.0** (2018) | BiometricPrompt API |
| **10** (2019) | **Scoped Storage**, Background Location 제한 |
| **11** (2020) | 일회성 권한, 자동 권한 리셋 |
| **12** (2021) | Approximate Location |
| **13** (2022) | Photo Picker, 알림 권한 |
| **14** (2023) | Credential Manager |

---

## 앱 샌드박싱

### UID 기반 격리

**핵심 원칙**: 각 앱은 **독립된 Linux UID**를 받는다.

```bash
$ adb shell ps -A | grep -E "u0_a[0-9]+"

u0_a123  12345  1234  com.example.app1
u0_a124  12346  1234  com.example.app2
u0_a125  12347  1234  com.google.android.gms
```

- `u0`: 사용자 0 (primary user)
- `a123`: 앱 UID (10123 = 10000 + 123)

**UID 범위**:
```
10000-19999: 일반 앱 (User 0)
20000-29999: 격리 프로세스 (isolated process)
1000-9999:   시스템 서비스
```

### 파일 시스템 격리

각 앱의 데이터 디렉토리:

```bash
/data/data/com.example.app/
drwx------  10  u0_a123  u0_a123  files/
drwx------   2  u0_a123  u0_a123  cache/
drwx------   5  u0_a123  u0_a123  code_cache/
drwx------   2  u0_a123  u0_a123  databases/
```

**권한**: `rwx------` (700) → 오직 소유 UID 만 접근 가능

**다른 앱이 접근 시도**:
```bash
$ adb shell
$ run-as com.example.app2  # UID u0_a124
$ cat /data/data/com.example.app1/databases/data.db
# Permission denied
```

### 프로세스 간 격리

[UID 기반](../../../../cpu-privilege-levels.md) + [SELinux](../../../../selinux.md) + Seccomp:

```mermaid
graph TB
    App1[앱 1<br/>UID 10123<br/>SEL: untrusted_app]
    App2[앱 2<br/>UID 10124<br/>SEL: untrusted_app]
    System[System Server<br/>UID 1000<br/>SEL: system_server]
    
    App1 -.X.-> App2
    App1 -->|Binder| System
    App2 -->|Binder| System
    
    Note[앱끼리 직접 통신 불가<br/>System을<br>통해서만<br>직접 접근]
```

---

## 권한 시스템

### 설치 시 권한 (Android 5.x 이하)

```xml
<!-- AndroidManifest.xml -->
<uses-permission android:name="android.permission.CAMERA" />
<uses-permission android:name="android.permission.READ_CONTACTS" />
```

**문제**: 설치 시 모든 권한 일괄 승인 → 사용자가 잘 모르고 승인

### 런타임 권한 (Android 6.0+)

**위험 권한**은 실행 중 요청:

```java
// 권한 확인
if (checkSelfPermission(CAMERA) != PERMISSION_GRANTED) {
    // 권한 요청 다이얼로그
    requestPermissions(new String[]{CAMERA}, REQUEST_CODE);
}

@Override
public void onRequestPermissionsResult(int requestCode, String[] permissions, 
                                       int[] grantResults) {
    if (grantResults[0] == PERMISSION_GRANTED) {
        // 권한 획득
    }
}
```

**사용자 경험**:
```
[앱 이름] needs camera access
[ ] Don't ask again
[Deny] [Allow]
```

### 권한 그룹

| 그룹 | 포함 권한 |
|------|----------|
| **CAMERA** | CAMERA |
| **LOCATION** | ACCESS_FINE_LOCATION, ACCESS_COARSE_LOCATION |
| **MICROPHONE** | RECORD_AUDIO |
| **CONTACTS** | READ_CONTACTS, WRITE_CONTACTS, GET_ACCOUNTS |
| **PHONE** | READ_PHONE_STATE, CALL_PHONE, READ_CALL_LOG |
| **STORAGE** | READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE |

한 권한 허용 시 같은 그룹 다른 권한도 자동 허용 (Android 10 까지).

### 세분화된 권한 제어 (Android 11+)

**일회성 권한**:
```
[앱] needs location
[Deny] [Only this time] [While using the app] [Allow]
```

**자동 리셋**:
- 앱을 오래 사용 안 하면 (3 개월) 권한 자동 해제
- 다음 실행 시 재요청

**백그라운드 위치** (별도 승인):
```kotlin
// Foreground 위치 권한
requestPermissions(ACCESS_FINE_LOCATION)

// Background 위치는 별도
requestPermissions(ACCESS_BACKGROUND_LOCATION)
```

### AppOps

권한보다 세밀한 제어:

```bash
# 특정 앱의 AppOps 확인
adb shell appops get com.example.app

# 출력:
# COARSE_LOCATION: allow
# FINE_LOCATION: allow; time=+2d3h15m (running)
# CAMERA: allow; time=+5h30m
```

**제어 가능한 항목**:
- 언제 권한 사용했는지
- 포그라운드/백그라운드 구분
- 빈도 제한

---

## SEAndroid (Security Enhancements for Android)

안드로이드는 리눅스 커널의 **LSM(Linux Security Module)** 프레임워크 위에 커스텀된 **SELinux** 정책인 **SEAndroid**를 탑재하여 강제적 접근 통제(MAC)를 수행한다. 이는 루트 권한을 탈취당하더라도 공격자가 시스템 전체를 장악하는 것을 방지하는 핵심 계층이다.

### 1. MAC(Mandatory Access Control) vs DAC(Discretionary Access Control)
- **DAC (전통적 리눅스)**: 파일의 소유자가 권한(`rwx`)을 결정한다. 루트(Root)는 모든 권한을 가진다.
- **MAC (SEAndroid)**: 시스템 관리자가 정의한 보안 정책에 따라 모든 접근이 결정된다. **루트 사용자라도 정책에 위배되는 행동은 차단된다.**

### 2. 도메인 및 타입 격리 (Domain & Type Enforcement)
모든 프로세스는 `domain`을, 모든 객체(파일, 소켓 등)는 `type`을 부여받는다.

```bash
# 앱 프로세스의 보안 컨텍스트 확인
u:r:untrusted_app:s0:c512,c768  # domain: untrusted_app

# 파일의 보안 컨텍스트 확인
u:object_r:app_data_file:s0    # type: app_data_file
```

**핵심 정책 파일**:
- `file_contexts`: 하드 코딩된 경로에 대한 레이블 설정.
- `seapp_contexts`: 앱의 `UID`, `isPrivileged` 여부에 따라 도메인 할당.
- `property_contexts`: 안드로이드 시스템 속성(`System Properties`)에 대한 접근 제어.

### 3. 실무적 의의: 권한 상승 공격 방어
공격자가 커널 취약점을 이용해 `UID 0`(Root)을 획득하더라도, SELinux 정책이 `untrusted_app` 도메인에 대해 `/system` 파티션 쓰기나 특정 커널 노드 접근을 금지(`neverallow`)하고 있다면 공격은 실패한다.

---

## 저장소 보안

### Scoped Storage (Android 10+)

**문제 (Android 9 이하)**:
```
앱이 READ_EXTERNAL_STORAGE 권한만 있으면
→ 모든 사진, 문서, 다운로드 파일 읽기 가능
→ 프라이버시 침해
```

**Scoped Storage**:

```mermaid
graph TB
    App[앱] --> OwnDir[자신의 디렉토리<br/>/sdcard/Android/data/com.example]
    App -.권한 필요.-> MediaStore[MediaStore API<br/>사진/비디오/오디오]
    App -.SAF.-> SAF[Storage Access Framework<br/>파일 선택기]
    
    App -.X.-> OtherDir[다른 앱 디렉토리]
    App -.X.-> RootFiles[/sdcard/Download직접접근]
```

**코드 변화**:

```java
// Android 9: 직접 파일 접근
File file = new File("/sdcard/DCIM/photo.jpg");
Bitmap bitmap = BitmapFactory.decodeFile(file.getAbsolutePath());

// Android 10+: MediaStore
Uri uri = MediaStore.Images.Media.EXTERNAL_CONTENT_URI;
Cursor cursor = getContentResolver().query(uri, projection, selection, null, null);
// ...
```

### 파일 기반 암호화 (FBE)

**전체 디스크 암호화 (FDE, ~Android 6.x)** 문제:
- 부팅 시 비밀번호 입력 전까지 모든 데이터 접근 불가
- 알람, 전화 수신 불가

**FBE (Android 7.0+)**:

```
/data/
├─ user/          # 사용자 잠금 시 암호화
│  └─ 0/com.example/files/
└─ user_de/       # Device Encrypted (항상 복호화)
   └─ 0/com.example/files/
```

**Direct Boot**:
- 디바이스 부팅 → FDE 복호화 (비밀번호 불필요)
- 알람, 전화 앱은 `user_de` 에 데이터 저장 → 작동
- 사용자 잠금 해제 → CE (Credential Encrypted) 복호화

```java
// CE Storage (기본)
File ceDir = context.getFilesDir();

// DE Storage
Context deContext = context.createDeviceProtectedStorageContext();
File deDir = deContext.getFilesDir();
```

### 암호화 알고리즘

**FBE**:
- Metadata: AES-256-XTS
- Contents: AES-256-XTS 또는 Adiantum (저사양 기기)

**키 파생**:
```
사용자 비밀번호 → scrypt(password, salt) → 마스터 키 → 파일 암호화 키
```

**Hardware-backed Keystore**:
- 키는 TEE (Trusted Execution Environment)에 저장
- 소프트웨어로 추출 불가

---

## Verified Boot

### 부팅 체인 검증

```mermaid
graph LR
    BootROM[Boot ROM<br/>OEM Key 내장] --> Bootloader[Bootloader<br/>서명 검증]
    Bootloader --> Kernel[Kernel/Ramdisk<br/>서명 검증]
    Kernel --> System[System Partition<br/>dm-verity]
    System --> App[앱 실행]
```

### dm-verity

**목적**: 시스템 파티션 무결성 보장

**동작**:
1. 빌드 시 `/system` 파티션의 해시 트리 생성
2. 루트 해시를 bootloader 에 저장
3. 런타임에 블록 읽을 때마다 해시 검증

```
Block → Hash → 부모 Hash → ... → Root Hash (Bootloader에 저장)
```

**변조 시도**:
```
공격자가 /system/app/Settings.apk 수정
→ dm-verity 해시 불일치 감지
→ 부팅 실패 or 경고 화면
```

### Verified Boot States

- **Green**: 완전히 검증됨
- **Yellow**: 부팅 가능하지만 사용자 키로 서명 (커스텀 ROM)
- **Orange**: Bootloader 언락됨 (개발자 모드)
- **Red**: 검증 실패 (부팅 차단)

---

## 네트워크 보안

### Network Security Configuration

```xml
<!-- res/xml/network_security_config.xml -->
<network-security-config>
    <!-- 기본: HTTPS만 -->
    <base-config cleartextTrafficPermitted="false">
        <trust-anchors>
            <certificates src="system" />
        </trust-anchors>
    </base-config>
    
    <!-- 예외: 특정 도메인만 HTTP 허용 -->
    <domain-config cleartextTrafficPermitted="true">
        <domain includeSubdomains="true">example.com</domain>
    </domain-config>
</network-security-config>
```

**AndroidManifest.xml**:
```xml
<application
    android:networkSecurityConfig="@xml/network_security_config">
```

### Certificate Pinning

```xml
<network-security-config>
    <domain-config>
        <domain>example.com</domain>
        <pin-set>
            <pin digest="SHA-256">7HIpactkIAq2Y49orFOOQKurWxmmSFZhBCoQYcRhJ3Y=</pin>
            <!-- Backup pin -->
            <pin digest="SHA-256">fwza0LRMXouZHRC8Ei+4PyuldPDcf3UKgO/04cDM1oE=</pin>
        </pin-set>
    </domain-config>
</network-security-config>
```

**효과**: 중간자 공격(MITM) 차단

### Private DNS (DNS-over-TLS)

```
Settings → Network → Advanced → Private DNS
```

**기본값**: Automatic (dns.google 등)

---

## 생체 인증

### BiometricPrompt API

```kotlin
val promptInfo = BiometricPrompt.PromptInfo.Builder()
    .setTitle("Unlock with fingerprint")
    .setNegativeButtonText("Use password")
    .setAllowedAuthenticators(BIOMETRIC_STRONG or DEVICE_CREDENTIAL)
    .build()

biometricPrompt.authenticate(promptInfo)
```

**보안 등급**:
- **BIOMETRIC_STRONG** (Class 3): 지문, 얼굴 (1/50,000 오인식률)
- **BIOMETRIC_WEAK** (Class 2): 1/1,000 오인식률
- **DEVICE_CREDENTIAL**: PIN/패턴/비밀번호

### StrongBox Keymaster

**Titan M** (Pixel) 같은 별도 보안 칩:
- 생체 인증 템플릿 저장
- 암호화 키 저장
- 소프트웨어로 절대 추출 불가

```kotlin
val keyGenParameterSpec = KeyGenParameterSpec.Builder(...)
    .setIsStrongBoxBacked(true)  // Titan M 사용
    .build()
```

---

## Play Integrity API (Integrity Enforcement)

과거의 SafetyNet을 대체하는 **Play Integrity API**는 앱이 변조되지 않았으며(App Integrity), 신뢰할 수 있는 구글 인증 기기(Device Integrity)에서 실행 중인지 검증한다.

### 1. Standard Integrity 실무 구현 패턴 (2026 기준)

기존의 Classic 방식보다 레이턴시가 낮고 리플레이 공격 방어에 최적화된 **Standard Integrity** 사용이 권장된다.

#### [Kotlin] Production-ready Integrity Manager

```kotlin
// build.gradle (Kotlin DSL)
// implementation("com.google.android.play:integrity:1.4.0")

class SecurityIntegrityClient(private val context: Context) {
    private val integrityManager = IntegrityManagerFactory.createStandard(context)
    private var tokenProvider: StandardIntegrityTokenProvider? = null

    /**
     * 1. Warm-up (앱 시작 시 또는 민감한 작업 직전에 호출)
     * Google Cloud Project 번호를 사용하여 프로바이더를 미리 로드한다.
     */
    suspend fun prepareIntegrityProvider(cloudProjectNumber: Long): Boolean {
        return try {
            val request = StandardIntegrityManager.PrepareIntegrityTokenRequest.builder()
                .setCloudProjectNumber(cloudProjectNumber)
                .build()
            tokenProvider = integrityManager.prepareIntegrityToken(request).await()
            true
        } catch (e: Exception) {
            Log.e("Integrity", "Provider preparation failed", e)
            false
        }
    }

    /**
     * 2. 토큰 요청 및 요청 바인딩 (Binding)
     * nonce 대신 requestHash를 사용하여 특정 요청과 무결성 결과를 묶는다.
     */
    suspend fun requestIntegrityToken(requestPayload: String): String? {
        val provider = tokenProvider ?: return null
        
        // Replay Attack 방지를 위해 실제 요청 데이터의 SHA-256 해시를 생성
        val requestHash = MessageDigest.getInstance("SHA-256")
            .digest(requestPayload.toByteArray())
            .joinToString("") { "%02x".format(it) }

        val tokenRequest = StandardIntegrityManager.StandardIntegrityTokenRequest.builder()
            .setRequestHash(requestHash) // 요청 데이터와 결과 토큰을 바인딩
            .build()

        return try {
            val response = provider.request(tokenRequest).await()
            response.token()
        } catch (e: Exception) {
            Log.e("Integrity", "Token request failed", e)
            null
        }
    }
}
```

### 2. 서버 측 검증 및 정책 결정 (Enforcement)

클라이언트에서 받은 토큰은 반드시 서버에서 **Google Play Developer API**를 통해 검증해야 한다.

- **Check requestHash**: 서버로 전송된 원본 요청의 해시와 토큰 내부의 `requestHash`가 일치하는지 확인.
- **Device Integrity Verdict**:
    - `MEETS_STRONG_INTEGRITY`: 하드웨어 계층의 서명 검증을 통과한 가장 안전한 상태. 금융/결제 앱 필수.
    - `MEETS_DEVICE_INTEGRITY`: 일반적인 순정 안드로이드 기기. 대부분의 상용 서비스 기준.
    - `MEETS_BASIC_INTEGRITY`: 부트로더가 언락되었거나 커스텀 롬일 가능성 있음.

---

## 보안 진단 도구 및 실무 기법 (Engineering Focus)

정보보안 전문가의 관점에서 앱을 진단하고, 이에 대응하는 방어 전략을 구축하는 실무 내용이다.

### 1. Frida를 이용한 동적 분석 (Dynamic Analysis)
**Frida**는 런타임에 JavaScript를 삽입하여 앱의 동작을 가로채거나 수정하는 강력한 도구이다.

- **진단 시나리오**: SSL Pinning 우회(Bypass), 생체 인증 강제 통과, 로컬 변수 조작.
- **방어 관점의 대응 (Anti-Frida)**:
    - **포트 스캔**: Frida 기본 포트(27042) 모니터링 시도.
    - **메모리 검사**: `/proc/self/maps`에서 `frida-agent.so` 등 의존성 문자열 탐색.
    - **ptrace 방어**: 이미 디버깅 중인 프로세스인 것처럼 속여 Frida 가 접속하지 못하게 차단.

### 2. Drozer를 이용한 취약점 분석
안드로이드 컴포넌트(`Activity`, `Provider`)간의 유출 경로를 탐색하는 도구이다.

- **진단**: `run app.activity.info -a com.package` 명령어로 외부 노출된 액티비티 확인 및 인텐트 인젝션 시도.
- **방어**: `AndroidManifest.xml`에서 의도하지 않은 컴포넌트의 `android:exported="false"` 설정 및 서명 기반 권한(`signature` level permission) 적용.

---

## 모바일 보안 법규 및 컴플라이언스 (Compliance)

**대한민국 개인정보 보호법** 및 관계 법령에 따른 개발 시 필수 준수 사항이다.

- **최소 권한의 법칙**: 앱의 핵심 기능 수행에 불필요한 권한(예: 캘린더 앱이 연락처 요구)은 원천 차단해야 한다. (시험 단골 소재)
- **모바일 앱 접근권한 고지 (정통망법 제22조의2)**: 
    - **필수적 접근권한**: 없으면 앱 실행이 불가능한 권한. (고지 및 동의 필수)
    - **선택적 접근권한**: 없어도 앱 기능 이용은 가능하나 특정 기능이 제한됨. (거부해도 앱 실행 가능해야 함)
- **민감정보 암호화**: 주민등록번호, 계좌번호, 생체정보 등은 단말기에 저장 시 반드시 **Android Keystore** 기반의 암호화가 적용되어야 한다.

## 개발자 모범 사례

### 보안 코딩

**1. 입력 검증**:
```kotlin
// 나쁜 예
val userId = intent.getStringExtra("user_id")
db.execSQL("SELECT * FROM users WHERE id = " + userId)  // SQL Injection!

// 좋은 예
val userId = intent.getStringExtra("user_id") ?: return
db.query("users", null, "id = ?", arrayOf(userId), null, null, null)
```

**2. 안전한 Intent**:
```kotlin
// Exported Component는 명시적으로
<activity
    android:name=".ExportedActivity"
    android:exported="true">
    <intent-filter>
        <action android:name="com.example.ACTION" />
    </intent-filter>
</activity>

// 내부 전용은 false
<activity
    android:name=".InternalActivity"
    android:exported="false" />
```

**3. PendingIntent**:
```kotlin
// Android 12+: 기본값 immutable
val pendingIntent = PendingIntent.getActivity(
    context, 0, intent, 
    PendingIntent.FLAG_IMMUTABLE  // 명시적으로
)
```

**4. 로그에 민감 정보 금지**:
```kotlin
// 나쁜 예
Log.d(TAG, "Password: $password")

// 좋은 예
Log.d(TAG, "Login attempt for user: ${username.take(3)}***")
```

---

## 디버깅 보안 이슈

### ADB 권한

```bash
# 앱 권한 강제 부여 (테스트용)
adb shell pm grant com.example.app android.permission.CAMERA

# AppOps 덮어쓰기
adb shell appops set com.example.app CAMERA allow
```

### SELinux 로그

```bash
# 거부된 접근
adb logcat | grep avc

# 출력:
# avc: denied { read } for scontext=u:r:untrusted_app:s0 \
#      tcontext=u:object_r:system_data_file:s0
```

### 네트워크 인터셉트

**개발 빌드에서만**:
```xml
<network-security-config>
    <debug-overrides>
        <trust-anchors>
            <certificates src="user" />  <!-- Charles, Fiddler -->
        </trust-anchors>
    </debug-overrides>
</network-security-config>
```

---

## 학습 리소스

**공식 문서**:
- [Security Overview](../../../../https:/source.android.com/docs/security.md)
- [App Sandboxing](../../../../https:/source.android.com/docs/security/app-sandbox.md)
- [Permissions](../../../../https:/developer.android.com/guide/topics/permissions/overview.md)

**보안 테스트**:
- [Android Security Checklist](../../../../https:/developer.android.com/privacy-and-security/security-checklist.md)
- OWASP Mobile Top 10

**도구**:
- `adb shell pm list permissions`: 모든 권한
- `adb shell dumpsys package <pkg>`: 앱 권한 상태
- Frida, Objection: 동적 분석

---

## 연결 문서

[selinux](../../../../selinux.md) - SELinux 정책 상세

[android-kernel](../01_system_internals/android-kernel.md) - 커널 보안 (SELinux, Seccomp)

[cpu-privilege-levels](../../../../cpu-privilege-levels.md) - UID 기반 격리

[android-binder-and-ipc](../01_system_internals/android-binder-and-ipc.md) - Binder 보안

[android-init-and-services](../01_system_internals/android-init-and-services.md) - Verified Boot 부팅 체인

[android-zygote-and-runtime](../01_system_internals/android-zygote-and-runtime.md) - 앱 프로세스 격리
