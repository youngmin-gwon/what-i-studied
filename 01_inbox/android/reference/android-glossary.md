---
title: android-glossary
tags: [android, android/glossary, android/reference]
aliases: [Android Glossary, 안드로이드 용어집]
date modified: 2025-12-17 14:55:53 +09:00
date created: 2025-12-16 15:56:51 +09:00
---

## Android 용어집

안드로이드 관련 핵심 용어를 정의하고 실전 예시를 제공한다.

---

## A

### ADB (Android Debug Bridge)

**정의**: PC와 안드로이드 기기를 연결하는 명령줄 도구

**상세**:
개발/디버깅 시 필수 도구로, USB 또는 Wi-Fi를 통해 기기에 명령을 전송하고 로그를 확인한다. 앱 설치, 파일 전송, 쉘 접근, 디버깅 등 다양한 작업에 사용된다.

**예시**:
```bash
# 연결된 기기 확인
adb devices

# 앱 설치
adb install app-debug.apk

# 로그 확인
adb logcat

# 쉘 접근
adb shell
```

**관련**: [[android-debugging-techniques]]

---

### AMS/ATMS (ActivityManagerService / ActivityTaskManagerService)

**정의**: 앱 생명주기와 Activity 스택을 관리하는 시스템 서비스

**상세**:
Android 10부터 분리되었다. AMS는 프로세스/Service/Broadcast를 관리하고, ATMS는 Activity/Task/Window를 담당한다. 앱 시작, 종료, 프로세스 우선순위 결정 등 핵심 역할을 한다.

**예시**:
```bash
# Activity 스택 확인
adb shell dumpsys activity activities

# 프로세스 목록
adb shell dumpsys activity processes
```

**관련**: [[android-activity-manager-and-system-services]]

---

### ANR (Application Not Responding)

**정의**: 앱이 5초 이상 응답하지 않을 때 표시되는 경고

**상세**:
메인 스레드가 블로킹되면 발생한다. 원인은 네트워크 요청, 디스크 I/O, 무한 루프 등이다. ANR 발생 시 `/data/anr/traces.txt`에 스택 트레이스가 기록된다.

**해결**:
```kotlin
// ❌ 메인 스레드에서 네트워크 (ANR 발생!)
val data = api.getData()

// ✅ 코루틴 사용
lifecycleScope.launch {
    val data = withContext(Dispatchers.IO) {
        api.getData()
    }
    updateUI(data)
}
```

**디버깅**:
```bash
adb pull /data/anr/traces.txt
```

**관련**: [[android-debugging-techniques]]

---

### APEX (Android Pony EXpress)

**정의**: 모듈식 시스템 컴포넌트 업데이트 형식

**상세**:
Android 10부터 도입되어 시스템 모듈을 APK처럼 Google Play를 통해 업데이트할 수 있다. ART, Media, NetworkStack 등 핵심 모듈이 APEX로 제공된다.

**예시**:
```bash
# APEX 모듈 확인
adb shell pm list packages -apex

# 출력:
# com.android.media
# com.android.wifi
# com.android.runtime
```

**구조**:
```
/apex/com.android.media@330000000/
├─ lib64/
├─ bin/
└─ apex_manifest.json
```

**관련**: [[android-customization-and-oem]]

---

### APK/AAB (Android Package / Android App Bundle)

**정의**: 안드로이드 앱 배포 형식

**상세**:
- **APK**: 모든 리소스/코드를 포함한 단일 파일
- **AAB**: Play Store가 기기별로 최적화된 APK 생성

**차이**:
```
APK (50MB):
  └─ 모든 기기용 리소스/라이브러리

AAB → Play Store → Split APKs (30MB):
  ├─ base.apk (공통)
  ├─ arm64.apk (기기 CPU)
  └─ xxxhdpi.apk (화면 밀도)
```

**명령어**:
```bash
# APK 설치
adb install app.apk

# AAB 빌드
./gradlew bundleRelease
```

---

### AppOps (App Operations)

**정의**: 권한보다 세밀한 앱 동작 제어 시스템

**상세**:
언제, 얼마나 자주 특정 권한을 사용했는지 추적하고 제한할 수 있다. 시스템 내부적으로 사용되며 일부 기기는 설정에서 노출한다.

**예시**:
```bash
# 앱의 AppOps 확인
adb shell appops get com.example.app

# 출력:
# COARSE_LOCATION: allow; time=+2d3h (running)
# CAMERA: allow; time=+5h30m

# 특정 operation 차단
adb shell appops set com.example.app CAMERA deny
```

**관련**: [[android-permissions-deep-dive]]

---

### ART (Android Runtime)

**정의**: 안드로이드 앱 실행 엔진 (Dalvik의 후속)

**상세**:
Android 5.0부터 기본값. DEX 바이트코드를 실행하며, 설치 시 AOT 컴파일과 실행 중 JIT 컴파일을 병행한다. Profile-Guided Optimization으로 자주 사용하는 코드를 최적화한다.

**진화**:
```
Dalvik (2008-2013):
  JIT만 → 매번 컴파일 → 느림

ART (2014-현재):
  AOT + JIT + Profile-Guided → 빠름
```

**확인**:
```bash
# 런타임 확인
adb shell getprop persist.sys.dalvik.vm.lib.2

# 출력: libart.so
```

**관련**: [[android-zygote-and-runtime]]

---

## B

### Binder

**정의**: 안드로이드의 프로세스 간 통신(IPC) 메커니즘

**상세**:
커널 드라이버 기반으로 앱과 시스템 서비스 간 메시지를 전달한다. 전통적인 Unix IPC와 달리 자동으로 호출자의 UID/PID를 확인하고 권한을 검사한다. 하나의 메모리 복사만으로 데이터 전달이 가능하여 성능이 우수하다.

**예시**:
```kotlin
// 시스템 서비스 호출 (내부적으로 Binder)
val am = getSystemService(ActivityManager::class.java)
val memoryInfo = ActivityManager.MemoryInfo()
am.getMemoryInfo(memoryInfo)
```

**디버깅**:
```bash
# Binder 서비스 목록
adb shell service list

# 특정 서비스 정보
adb shell dumpsys activity services
```

**관련**: [[android-binder-and-ipc]]

---

### Bugreport

**정의**: 기기 상태를 종합적으로 담은 로그 묶음

**상세**:
시스템 로그, 커널 로그, dumpsys 출력, 메모리 상태, 네트워크 상태 등 모든 디버깅 정보를 zip 파일로 압축한다. 버그 리포트 시 첨부하는 필수 자료다.

**생성**:
```bash
# 버그리포트 생성
adb bugreport bugreport.zip

# 또는 기기에서
# Settings → About Phone → 빌드 번호 7번 탭
# Developer Options → Take Bug Report
```

**포함 내용**:
- logcat 전체
- dmesg (커널 로그)
- dumpsys 모든 서비스
- /proc, /sys 정보
- ANR traces

**관련**: [[android-debugging-techniques]]

---

## D

### DEX (Dalvik Executable)

**정의**: 안드로이드 앱의 바이트코드 형식

**상세**:
Java/Kotlin 코드를 컴파일하면 JVM `.class` 파일이 생성되고, 이를 `dx` 도구로 `.dex`로 변환한다. DEX는 모바일에 최적화되어 있어 파일 크기가 작고 실행 효율이 높다.

**프로세스**:
```
.kt/.java → .class → .dex → .apk
         javac    dx/d8
```

**확인**:
```bash
# APK 내 DEX 파일 확인
unzip -l app.apk | grep dex

# 출력:
# classes.dex
# classes2.dex (MultiDex)
```

**최적화**:
```bash
# dexopt (설치 시)
# → .odex (Optimized DEX)
# → .vdex (Verified DEX, ART)
```

**관련**: [[android-zygote-and-runtime]]

---

### Doze / App Standby

**정의**: 배터리 절약을 위한 앱 활동 제한 모드

**상세**:
- **Doze**: 기기가 움직이지 않고 화면 꺼진 상태가 지속되면 네트워크/Wakelock/AlarmManager 제한
- **App Standby**: 미사용 앱의 백그라운드 작업 제한

**Doze 단계**:
```
화면 꺼짐 → 30분 대기 → Light Doze (제한 시작)
           → 1시간 대기 → Deep Doze (완전 제한)
```

**예외 목록**:
```kotlin
// 배터리 최적화 제외 요청
val intent = Intent(Settings.ACTION_REQUEST_IGNORE_BATTERY_OPTIMIZATIONS)
intent.data = Uri.parse("package:$packageName")
startActivity(intent)
```

**테스트**:
```bash
# Doze 강제 진입
adb shell dumpsys deviceidle force-idle

# 해제
adb shell dumpsys deviceidle unforce
```

**관련**: [[android-performance-and-debug]]

---

## F

### FBE (File-Based Encryption)

**정의**: 파일별로 다른 키로 암호화하는 방식

**상세**:
전체 디스크 암호화(FDE)와 달리 사용자 잠금 상태에 따라 일부 파일은 접근 가능하다. Direct Boot 기능으로 부팅 후 잠금 해제 전에도 알람/전화 수신이 가능하다.

**저장 영역**:
```
/data/user_de/0/com.example/  # Device Encrypted (항상 복호화)
/data/user/0/com.example/     # Credential Encrypted (잠금 시 암호화)
```

**사용**:
```kotlin
// DE Storage
val deContext = context.createDeviceProtectedStorageContext()
val deFile = File(deContext.filesDir, "alarm.txt")

// CE Storage (기본)
val ceFile = File(context.filesDir, "user_data.txt")
```

**관련**: [[android-security-and-sandboxing]]

---

## H

### HAL (Hardware Abstraction Layer)

**정의**: 하드웨어와 안드로이드 프레임워크를 연결하는 인터페이스

**상세**:
기기마다 다른 하드웨어(카메라, 센서, GPS 등)를 표준 API로 추상화한다. HIDL(Legacy) 또는 AIDL(Modern)로 정의되며, Vendor 파티션에 구현체가 위치한다.

**진화**:
```
Legacy HAL (.so 직접 로드)
  ↓
HIDL HAL (C++, Treble)
  ↓
AIDL HAL (다중 언어, 간결)
```

**예시**:
```bash
# HAL 서비스 확인
adb shell lshal

# 출력:
# android.hardware.camera.provider@2.4::ICameraProvider/legacy/0
# android.hardware.audio@7.0::IDevicesFactory/default
```

**관련**: [[android-hal-and-kernel]]

---

## L

### LMKD (Low Memory Killer Daemon)

**정의**: 메모리 부족 시 프로세스를 종료하는 데몬

**상세**:
프로세스마다 OOM Adjuster가 부여한 우선순위를 기반으로 메모리가 부족하면 낮은 우선순위 프로세스부터 종료한다. 커널의 OOM Killer를 대체한다.

**우선순위**:
```
0    - Foreground (사용자 보는 앱)
100  - Visible
200  - Perceptible (음악 재생)
500  - Service
900+ - Cached (백그라운드)
```

**확인**:
```bash
# 프로세스별 OOM 점수
adb shell cat /proc/$(pidof com.example)/oom_score_adj

# LMKD 로그
adb logcat | grep lmkd
```

**관련**: [[android-kernel]], [[android-activity-manager-and-system-services]]

---

## O

### OTA (Over-The-Air)

**정의**: 무선으로 시스템 업데이트를 전송하는 방식

**상세**:
사용자가 Wi-Fi를 통해 업데이트를 다운로드하고 설치한다. A/B 업데이트는 백그라운드에서 설치하고 재부팅 시 교체하여 중단 없는 업데이트를 제공한다.

**방식**:
```
Full OTA: 전체 시스템 이미지
Incremental OTA: 변경된 부분만

A/B Seamless:
  Slot A (현재) + Slot B (업데이트) → 재부팅 시 교체
```

**확인**:
```bash
# 현재 슬롯
adb shell getprop ro.boot.slot_suffix

# 출력: _a 또는 _b
```

**관련**: [[android-boot-flow]], [[android-customization-and-oem]]

---

## P

### Parcelable

**정의**: Binder로 전송하기 위한 객체 직렬화 인터페이스

**상세**:
Java Serializable보다 빠르다. 객체를 Parcel로 변환하여 프로세스 간 전달한다. Android Studio가 자동 생성을 지원한다.

**예시**:
```kotlin
@Parcelize
data class User(
    val id: Int,
    val name: String
) : Parcelable

// Intent로 전달
val intent = Intent(this, DetailActivity::class.java)
intent.putExtra("user", user)
startActivity(intent)

// 수신
val user = intent.getParcelableExtra<User>("user")
```

**관련**: [[android-binder-and-ipc]]

---

### Perfetto

**정의**: 시스템 전체 성능을 추적하는 도구

**상세**:
CPU, 메모리, 디스크, 네트워크, 프레임 렌더링 등을 시간 순서대로 기록한다. Systrace의 후속으로 더 많은 정보와 분석 기능을 제공한다.

**수집**:
```bash
# 10초 trace
adb shell perfetto \
  -c - --txt \
  -o /data/local/tmp/trace <<EOF
buffers: {
    size_kb: 65536
}
data_sources: {
    config {
        name: "linux.ftrace"
    }
}
duration_ms: 10000
EOF

# trace 가져오기
adb pull /data/local/tmp/trace trace.perfetto-trace

# 분석: https://ui.perfetto.dev/
```

**관련**: [[android-profiling-tools]], [[android-performance-and-debug]]

---

## S

### Scoped Storage

**정의**: 앱별로 외부 저장소 접근을 제한하는 정책

**상세**:
Android 10부터 도입되어 앱은 자신의 디렉토리와 MediaStore로만 접근 가능하다. 다른 앱 파일이나 임의 경로 접근이 차단된다.

**접근 방식**:
```kotlin
// 1. 앱 전용 디렉토리 (권한 불필요)
val appFiles = context.getExternalFilesDir(null)
// /sdcard/Android/data/com.example/files/

// 2. MediaStore (사진/비디오/오디오)
val uri = MediaStore.Images.Media.EXTERNAL_CONTENT_URI
contentResolver.query(uri, ...)

// 3. Storage Access Framework (파일 선택)
val intent = Intent(Intent.ACTION_OPEN_DOCUMENT)
intent.type = "*/*"
startActivityForResult(intent, REQUEST_CODE)
```

**관련**: [[android-security-and-sandboxing]], [[android-storage-systems]]

---

### SELinux (Security-Enhanced Linux)

**정의**: Mandatory Access Control 보안 메커니즘

**상세**:
모든 프로세스/파일에 보안 레이블을 부여하고 정책으로 접근을 제어한다. 루트 권한을 획득해도 SELinux 정책이 막으면 시스템 파일을 수정할 수 없다.

**모드**:
```bash
# 모드 확인
adb shell getenforce

# Enforcing: 정책 강제 (기본)
# Permissive: 정책 기록만 (개발용)
```

**도메인 예시**:
```
u:r:untrusted_app:s0:c512     # 일반 앱
u:r:system_server:s0           # system_server
u:r:init:s0                    # init
```

**거부 로그**:
```bash
adb logcat | grep avc

# avc: denied { read } for scontext=u:r:untrusted_app:s0 ...
```

**관련**: [[selinux]], [[android-security-and-sandboxing]]

---

### system_server

**정의**: 시스템 서비스들이 실행되는 Java 프로세스

**상세**:
Zygote가 fork하여 생성하며, ActivityManager, WindowManager, PackageManager 등 100여 개 서비스를 호스팅한다. system_server가 크래시하면 기기 재부팅된다.

**확인**:
```bash
# system_server 프로세스
adb shell ps -A | grep system_server

# 포함된 서비스
adb shell service list
```

**크래시 시**:
```
system_server 죽음 → Zygote가 재시작 감지 → 기기 재부팅
```

**관련**: [[android-activity-manager-and-system-services]]

---

## U

### UID (User ID)

**정의**: 앱마다 부여되는 고유 번호

**상세**:
Linux UID 시스템을 활용하여 앱을 격리한다. 각 앱은 독립된 UID를 받아 다른 앱의 파일에 접근할 수 없다. SharedUserID로 여러 앱이 같은 UID를 공유할 수도 있다.

**범위**:
```
10000-19999: 일반 앱 (User 0)
20000-29999: 격리 프로세스
1000-9999:   시스템 서비스
```

**확인**:
```bash
# 앱의 UID
adb shell dumpsys package com.example | grep userId

# 출력: userId=10123
```

**파일 권한**:
```bash
adb shell ls -la /data/data/com.example

# drwx------  10  u0_a123  u0_a123  files/
#             (UID만 접근 가능)
```

**관련**: [[android-security-and-sandboxing]]

---

## V

### Verified Boot (AVB)

**정의**: 부팅 이미지의 무결성을 검증하는 메커니즘

**상세**:
부트로더가 vbmeta를 검증하고, vbmeta가 system/vendor 파티션을 검증한다. 변조된 이미지는 부팅이 차단되거나 경고가 표시된다.

**검증 체인**:
```
OEM Key (eFuse) 
  → vbmeta.img
    → boot.img
    → system.img (dm-verity)
    → vendor.img (dm-verity)
```

**상태**:
```
Green:  OEM key 검증됨 (정상)
Yellow: User key 검증됨 (커스텀 ROM)
Orange: Bootloader unlocked (경고)
Red:    검증 실패 (부팅 차단)
```

**확인**:
```bash
adb shell getprop ro.boot.verifiedbootstate

# green / yellow / orange / red
```

**관련**: [[android-security-and-sandboxing]], [[android-boot-flow]]

---

## W

### Wakelock

**정의**: 기기가 절전 모드로 진입하는 것을 막는 잠금

**상세**:
화면이 꺼져도 CPU/네트워크를 유지해야 할 때 사용한다. 잘못 사용하면 배터리를 심하게 소모하므로 꼭 필요할 때만 짧게 사용해야 한다.

**사용**:
```kotlin
val powerManager = getSystemService(PowerManager::class.java)
val wakeLock = powerManager.newWakeLock(
    PowerManager.PARTIAL_WAKE_LOCK,
    "MyApp::MyWakelockTag"
)

// 획득
wakeLock.acquire(10 * 60 * 1000L)  // 10분 타임아웃

// 해제 (필수!)
wakeLock.release()
```

**디버깅**:
```bash
# Wakelock 확인
adb shell dumpsys power | grep Wake

# 배터리 사용량
adb shell dumpsys batterystats
```

**관련**: [[android-performance-and-debug]]

---

### WorkManager / JobScheduler

**정의**: 백그라운드 작업을 예약하는 API

**상세**:
- **JobScheduler**: 시스템 API, 조건 기반 실행
- **WorkManager**: Jetpack 라이브러리, JobScheduler/AlarmManager 추상화

**WorkManager 사용**:
```kotlin
val constraints = Constraints.Builder()
    .setRequiredNetworkType(NetworkType.CONNECTED)
    .setRequiresBatteryNotLow(true)
    .build()

val work = OneTimeWorkRequestBuilder<MyWorker>()
    .setConstraints(constraints)
    .build()

WorkManager.getInstance(context).enqueue(work)
```

**JobScheduler**:
```kotlin
val job = JobInfo.Builder(JOB_ID, componentName)
    .setRequiredNetworkType(JobInfo.NETWORK_TYPE_UNMETERED)
    .setRequiresCharging(true)
    .build()

jobScheduler.schedule(job)
```

**관련**: [[android-activity-manager-and-system-services]]

---

## Z

### Zygote

**정의**: 모든 앱 프로세스를 생성하는 부모 프로세스

**상세**:
부팅 시 Framework 클래스와 리소스를 미리 로드(Preload)한 후 대기한다. 앱 시작 요청이 오면 자신을 fork하여 새 프로세스를 빠르게 만든다. Copy-on-Write로 메모리를 절약한다.

**프로세스**:
```
Zygote (PID 1234, 4000개 클래스 Preload)
  ↓ fork
앱 A (PID 5678, Preload 공유)
앱 B (PID 5679, Preload 공유)
```

**확인**:
```bash
# Zygote 프로세스
adb shell ps -A | grep zygote

# Preload 클래스 수
adb shell getprop dalvik.vm.preloadedclasses

# 출력: ~4000
```

**소켓**:
```bash
# Zygote 소켓
adb shell ls -la /dev/socket/zygote*

# /dev/socket/zygote
# /dev/socket/zygote_secondary (32-bit)
```

**관련**: [[android-zygote-and-runtime]]

---

## 기타

### Baseline Profile

**정의**: 앱에서 자주 사용되는 코드 경로를 기록한 파일

**상세**:
설치 시 이 프로파일을 기반으로 AOT 컴파일하여 첫 실행부터 빠른 성능을 제공한다. Jetpack Compose 앱에서 특히 효과적이다.

**생성**:
```kotlin
// build.gradle.kts
dependencies {
    implementation("androidx.profileinstaller:profileinstaller:1.3.0")
}

// 벤치마크로 프로파일 생성
./gradlew :app:generateBaselineProfile
```

**관련**: [[android-zygote-and-runtime]]

---

### Mipmap

**정의**: 앱 아이콘을 저장하는 리소스 디렉토리

**상세**:
Drawable과 달리 런처가 아이콘을 로딩할 때 최적화되어 있다. 다양한 화면 밀도(mdpi, hdpi, xhdpi 등)별로 제공해야 한다.

**구조**:
```
res/
├─ mipmap-mdpi/ic_launcher.png     (48x48)
├─ mipmap-hdpi/ic_launcher.png     (72x72)
├─ mipmap-xhdpi/ic_launcher.png    (96x96)
├─ mipmap-xxhdpi/ic_launcher.png   (144x144)
└─ mipmap-xxxhdpi/ic_launcher.png  (192x192)
```

**사용**:
```xml
<application
    android:icon="@mipmap/ic_launcher"
    ...>
```

---

## 관련 문서

[[android-overview]] - 시스템 전체 개요  
[[android-evolution-history]] - 기술 진화  
[[android-debugging-techniques]] - 디버깅 도구
