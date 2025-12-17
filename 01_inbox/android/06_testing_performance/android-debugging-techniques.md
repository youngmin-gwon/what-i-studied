---
title: android-debugging-techniques
tags: [android, android/debugging, android/tools, android/crash-analysis]
aliases: []
date modified: 2025-12-16 16:19:14 +09:00
date created: 2025-12-16 16:19:14 +09:00
---

## Android Debugging Techniques android android/debugging android/tools

크래시 분석, ANR 디버깅, 로깅 기법. 기본은 [[android-performance-and-debug]] 참고.

### Logcat

기본 로깅 도구.

```kotlin
import android.util.Log

class MyClass {
    companion object {
        private const val TAG = "MyClass"
    }
    
    fun doSomething() {
        Log.v(TAG, "Verbose message") // 상세 정보
        Log.d(TAG, "Debug message") // 디버그 정보
        Log.i(TAG, "Info message") // 일반 정보
        Log.w(TAG, "Warning message") // 경고
        Log.e(TAG, "Error message") // 에러
        
        // 예외와 함께
        try {
            riskyOperation()
        } catch (e: Exception) {
            Log.e(TAG, "Operation failed", e)
        }
    }
}
```

```bash
# Logcat 필터링
adb logcat TAG:D *:S # TAG 의 DEBUG 이상만 표시

# 패키지별 필터
adb logcat --pid=$(adb shell pidof -s com.example.app)

# 시간 포함
adb logcat -v time

# 파일로 저장
adb logcat -f /sdcard/logcat.txt

# 버퍼 클리어
adb logcat -c
```

### Timber (구조화된 로깅)

```kotlin
// build.gradle.kts
dependencies {
    implementation("com.jakewharton.timber:timber:5.0.1")
}

// Application
class MyApplication : Application() {
    override fun onCreate() {
        super.onCreate()
        
        if (BuildConfig.DEBUG) {
            Timber.plant(Timber.DebugTree())
        } else {
            Timber.plant(CrashReportingTree())
        }
    }
}

class CrashReportingTree : Timber.Tree() {
    override fun log(priority: Int, tag: String?, message: String, t: Throwable?) {
        if (priority == Log.ERROR || priority == Log.WARN) {
            // Firebase Crashlytics 등에 전송
            FirebaseCrashlytics.getInstance().log(message)
            t?.let { FirebaseCrashlytics.getInstance().recordException(it) }
        }
    }
}

// 사용
Timber.d("User logged in: %s", userId)
Timber.e(exception, "Failed to load data")
```

### 크래시 분석

#### Stack Trace 읽기

```
FATAL EXCEPTION: main
Process: com.example.app, PID: 12345
java.lang.NullPointerException: Attempt to invoke virtual method 'java.lang.String com.example.User.getName()' on a null object reference
    at com.example.app.MainActivity.displayUser(MainActivity.kt:42)
    at com.example.app.MainActivity.onCreate(MainActivity.kt:28)
    at android.app.Activity.performCreate(Activity.java:8000)
    ...
```

**분석:**
1. **예외 타입**: NullPointerException
2. **메시지**: User 객체가 null
3. **발생 위치**: MainActivity.kt:42
4. **호출 경로**: onCreate → displayUser

#### ProGuard 매핑

```bash
# mapping.txt 로 난독화 해제
retrace.bat -verbose mapping.txt stacktrace.txt

# Android Studio 에서
# Build → Analyze APK → Load Proguard Mappings
```

### ANR 분석

ANR (Application Not Responding) 은 메인 스레드가 5초 이상 블로킹될 때 발생.

#### ANR Trace 확인

```bash
# ANR 발생 시 자동 생성
adb pull /data/anr/traces.txt

# 또는
adb bugreport bugreport.zip
```

**Trace 예시:**
```
"main" prio=5 tid=1 Sleeping
  | group="main" sCount=1 dsCount=0 flags=1 obj=0x74b38080 self=0x7f8c001200
  | sysTid=12345 nice=-10 cgrp=default sched=0/0 handle=0x7f8c456000
  | state=S schedstat=( 1234567890 987654321 123 ) utm=100 stm=50 core=2 HZ=100
  | stack=0x7ffc000000-0x7ffc002000 stackSize=8MB
  | held mutexes=
  at java.lang.Thread.sleep(Native Method)
  at com.example.app.MainActivity.loadData(MainActivity.kt:50)
  at com.example.app.MainActivity.onCreate(MainActivity.kt:30)
```

**해결:**
```kotlin
// ❌ 나쁜 예: 메인 스레드에서 네트워크
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    val data = api.getData() // ANR!
}

// ✅ 좋은 예: 코루틴 사용
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    lifecycleScope.launch {
        val data = withContext(Dispatchers.IO) {
            api.getData()
        }
        updateUI(data)
    }
}
```

### Breakpoint Debugging

#### Android Studio Debugger

```kotlin
fun processData(items: List<Item>) {
    items.forEach { item ->
        // 여기에 브레이크포인트 설정
        val result = transform(item)
        save(result)
    }
}
```

**조건부 브레이크포인트:**
```kotlin
// 브레이크포인트 우클릭 → Condition
item.id == "특정ID"
```

**로그 브레이크포인트:**
```kotlin
// Evaluate and log: "Processing item: " + item.id
// Suspend: 체크 해제
```

#### JDWP (Java Debug Wire Protocol)

```bash
# 디버그 가능한 프로세스 확인
adb jdwp

# 포트 포워딩
adb forward tcp:8700 jdwp:12345

# Android Studio 에서 Attach to Process
```

### Native Debugging (lldb)

```bash
# lldb 서버 시작
adb shell
lldb-server platform --listen "*:1234"

# Android Studio 에서
# Run → Attach Debugger to Android Process
# Debugger: Native
```

```cpp
// C++ 코드에 브레이크포인트 설정 가능
extern "C" JNIEXPORT void JNICALL
Java_com_example_app_NativeLib_processImage(
    JNIEnv* env,
    jobject /* this */,
    jobject bitmap) {
    
    // 여기에 브레이크포인트
    AndroidBitmapInfo info;
    AndroidBitmap_getInfo(env, bitmap, &info);
}
```

### Memory Leak 디버깅

#### LeakCanary

```kotlin
// build.gradle.kts
dependencies {
    debugImplementation("com.squareup.leakcanary:leakcanary-android:2.12")
}

// 자동으로 누수 감지
// 알림으로 결과 표시
```

#### 수동 분석

```kotlin
// 의심되는 객체 추적
class MyActivity : AppCompatActivity() {
    companion object {
        private val instances = mutableListOf<WeakReference<MyActivity>>()
    }
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        instances.add(WeakReference(this))
        
        // 주기적으로 확인
        instances.removeAll { it.get() == null }
        Log.d("Leak", "Active instances: ${instances.size}")
    }
}
```

### Network Debugging

#### Charles Proxy / Fiddler

```xml
<!-- network_security_config.xml -->
<network-security-config>
    <debug-overrides>
        <trust-anchors>
            <certificates src="user" />
        </trust-anchors>
    </debug-overrides>
</network-security-config>
```

```kotlin
// AndroidManifest.xml
<application
    android:networkSecurityConfig="@xml/network_security_config">
```

```bash
# Charles 인증서 설치
# Settings → Security → Install from storage
```

#### OkHttp Interceptor

```kotlin
val loggingInterceptor = HttpLoggingInterceptor { message ->
    Log.d("OkHttp", message)
}.apply {
    level = HttpLoggingInterceptor.Level.BODY
}

val client = OkHttpClient.Builder()
    .addInterceptor(loggingInterceptor)
    .build()
```

### Layout Debugging

#### Layout Inspector

```
Tools → Layout Inspector
```

**기능:**
- 3D 뷰로 레이어 확인
- 각 View 의 속성 확인
- 렌더링 시간 측정

#### Show Layout Bounds

```bash
# 개발자 옵션에서 "레이아웃 경계 표시" 활성화
adb shell setprop debug.layout true
adb shell service call activity 1599295570
```

### Database Debugging

#### Database Inspector

```
View → Tool Windows → App Inspection → Database Inspector
```

**기능:**
- 실시간 데이터 확인
- 쿼리 실행
- 데이터 수정

#### 수동 확인

```bash
# SQLite DB 가져오기
adb pull /data/data/com.example.app/databases/app.db

# SQLite 열기
sqlite3 app.db

# 테이블 확인
.tables

# 쿼리
SELECT * FROM users;
```

### Stetho (Facebook)

웹 브라우저로 앱 디버깅.

```kotlin
// build.gradle.kts
dependencies {
    debugImplementation("com.facebook.stetho:stetho:1.6.0")
    debugImplementation("com.facebook.stetho:stetho-okhttp3:1.6.0")
}

// Application
class MyApplication : Application() {
    override fun onCreate() {
        super.onCreate()
        
        if (BuildConfig.DEBUG) {
            Stetho.initializeWithDefaults(this)
        }
    }
}

// OkHttp 에 연결
val client = OkHttpClient.Builder()
    .addNetworkInterceptor(StethoInterceptor())
    .build()
```

```
# Chrome 에서
chrome://inspect/#devices
```

### Flipper (Meta)

강력한 디버깅 플랫폼.

```kotlin
// build.gradle.kts
dependencies {
    debugImplementation("com.facebook.flipper:flipper:0.212.0")
    debugImplementation("com.facebook.soloader:soloader:0.10.5")
    debugImplementation("com.facebook.flipper:flipper-network-plugin:0.212.0")
    debugImplementation("com.facebook.flipper:flipper-leakcanary2-plugin:0.212.0")
}

// Application
class MyApplication : Application() {
    override fun onCreate() {
        super.onCreate()
        SoLoader.init(this, false)
        
        if (BuildConfig.DEBUG && FlipperUtils.shouldEnableFlipper(this)) {
            val client = AndroidFlipperClient.getInstance(this)
            client.addPlugin(InspectorFlipperPlugin(this, DescriptorMapping.withDefaults()))
            client.addPlugin(NetworkFlipperPlugin())
            client.addPlugin(DatabasesFlipperPlugin(this))
            client.addPlugin(LeakCanary2FlipperPlugin())
            client.start()
        }
    }
}
```

### 원격 디버깅

#### Wireless ADB

```bash
# USB 연결 후
adb tcpip 5555

# USB 분리 후
adb connect 192.168.1.100:5555

# 디버깅
adb logcat
```

### 더 보기

[[android-performance-and-debug]], [[android-profiling-tools]], [[android-testing-and-quality]], [[android-ndk-jni]]
