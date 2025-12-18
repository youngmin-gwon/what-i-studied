---
title: android-process-and-memory
tags: [android, android/process, android/memory, android/zygote, systems]
aliases: []
date modified: 2025-12-16 16:19:14 +09:00
date created: 2025-12-16 16:19:14 +09:00
---

## Process and Memory Management android android/process android/memory systems

안드로이드의 프로세스 생성과 메모리 관리를 깊이 있게 다룬다. 기본은 [android-zygote-and-runtime](android-zygote-and-runtime.md) 과 [android-foundations](../00_foundations/android-foundations.md) 참고.

### 프로세스 생성 흐름

#### Zygote Fork 메커니즘

[[android-glossary#zygote|Zygote]] 는 모든 앱 프로세스의 부모다.

**부팅 시 Zygote 초기화:**
1. `app_process` 가 Zygote 프로세스를 시작
2. [[android-glossary#zygote#preload|Preload]]: 공통 클래스 (~4000개), 리소스, 공유 라이브러리를 메모리에 적재
3. Unix 소켓 `/dev/socket/zygote` 를 열고 대기

**앱 시작 시:**
1. [ActivityManagerService](android-activity-manager-and-system-services.md) 가 "이 앱 프로세스가 없다" 판단
2. Zygote 소켓으로 요청 전송 (UID, GID, 권한, 패키지명, nice 값 등)
3. Zygote 가 `fork()` 시스템 콜로 자신을 복사
4. 자식 프로세스에서:
   - [[android-glossary#selinux|SELinux]] 컨텍스트 설정
   - UID/GID 변경
   - 능력(capabilities) 조정
   - `ActivityThread.main()` 실행

#### Copy-on-Write (COW) 최적화

`fork()` 직후에는 부모와 자식이 **같은 물리 메모리 페이지를 공유**한다.

```
Zygote 프로세스 메모리:
┌─────────────────┐
│ Framework 클래스 │ ← 읽기 전용, 모든 앱이 공유
│ 리소스/라이브러리│
└─────────────────┘

앱 프로세스 1, 2, 3:
각각 위 메모리를 가리키는 포인터만 가짐 (실제 복사 없음)

쓰기 발생 시:
해당 페이지만 복사됨 (Copy-on-Write)
```

**효과:**
- 메모리 절약: 공통 코드를 한 번만 적재
- 빠른 시작: 복사 비용 최소화
- 단점: Zygote 가 너무 많이 preload 하면 모든 앱이 무거워짐

#### 프로세스 우선순위

시스템은 각 프로세스에 **oom_adj** 점수를 부여한다.

| 우선순위 | oom_adj | 설명 |
|---------|---------|------|
| Foreground | 0 | 사용자가 보고 있는 Activity |
| Visible | 100 | 보이지만 포커스 없음 (다이얼로그 뒤) |
| Service | 200-500 | Foreground Service 또는 중요 Service |
| Cached | 900-999 | 백그라운드, 언제든 종료 가능 |

```bash
# 프로세스 우선순위 확인
adb shell cat /proc/<pid>/oom_score_adj

# 모든 앱 프로세스 우선순위
adb shell dumpsys activity processes
```

### 메모리 관리

#### Low Memory Killer Daemon (LMKD)

[[android-glossary#lmkd|LMKD]] 는 메모리 부족 시 프로세스를 종료한다.

**동작 방식:**
1. 커널이 메모리 압력(pressure stall) 감지
2. LMKD 가 oom_adj 점수가 높은 (덜 중요한) 프로세스부터 종료
3. 메모리 확보 후 정상 동작 재개

**임계값 (minfree):**
```bash
# 메모리 임계값 확인
adb shell cat /sys/module/lowmemorykiller/parameters/minfree
# 예: 18432,23040,27648,32256,36864,46080 (페이지 단위, 1페이지=4KB)
```

#### Process State 와 생명주기

```kotlin
// Application 클래스에서 생명주기 감지
class MyApplication : Application() {
    override fun onCreate() {
        super.onCreate()
        
        registerActivityLifecycleCallbacks(object : ActivityLifecycleCallbacks {
            override fun onActivityCreated(activity: Activity, savedInstanceState: Bundle?) {}
            override fun onActivityStarted(activity: Activity) {}
            override fun onActivityResumed(activity: Activity) {}
            override fun onActivityPaused(activity: Activity) {}
            override fun onActivityStopped(activity: Activity) {}
            override fun onActivitySaveInstanceState(activity: Activity, outState: Bundle) {}
            override fun onActivityDestroyed(activity: Activity) {}
        })
        
        // 프로세스 상태 변화 감지
        ProcessLifecycleOwner.get().lifecycle.addObserver(object : DefaultLifecycleObserver {
            override fun onStart(owner: LifecycleOwner) {
                // 앱이 포그라운드로 진입
            }
            
            override fun onStop(owner: LifecycleOwner) {
                // 앱이 백그라운드로 진입
            }
        })
    }
    
    override fun onTrimMemory(level: Int) {
        super.onTrimMemory(level)
        when (level) {
            TRIM_MEMORY_RUNNING_CRITICAL -> {
                // 메모리 매우 부족, 캐시 정리
            }
            TRIM_MEMORY_UI_HIDDEN -> {
                // UI 가 숨겨짐, 큰 리소스 해제
            }
            TRIM_MEMORY_BACKGROUND -> {
                // 백그라운드 진입, 불필요한 메모리 해제
            }
        }
    }
}
```

#### Garbage Collection (GC)

[[android-glossary#art|ART]] 의 GC 는 메모리를 자동으로 회수한다.

**GC 종류:**
- **Concurrent Copying GC**: 대부분의 작업을 앱 실행과 동시에 수행 (Android 10+)
- **Mark-Compact**: 메모리 단편화 제거
- **Generational GC**: 젊은 객체와 오래된 객체를 다르게 처리

**GC 로그 확인:**
```bash
adb logcat | grep "GC"
# 예: Explicit concurrent mark sweep GC freed 104(6KB) AllocSpace objects, 0(0B) LOS objects, 33% free, 25MB/38MB, paused 1.230ms total 67.216ms
```

**메모리 누수 방지:**
```kotlin
// ❌ 나쁜 예: Activity 참조를 오래 유지
class BadSingleton {
    companion object {
        var context: Context? = null // Activity 를 넣으면 누수!
    }
}

// ✅ 좋은 예: Application Context 사용
class GoodSingleton {
    companion object {
        lateinit var appContext: Context
        
        fun init(context: Context) {
            appContext = context.applicationContext
        }
    }
}

// ✅ WeakReference 사용
class ImageCache {
    private val cache = WeakHashMap<String, Bitmap>()
    
    fun put(key: String, bitmap: Bitmap) {
        cache[key] = bitmap
    }
}
```

### 메모리 프로파일링

#### Memory Profiler 사용

Android Studio 의 Memory Profiler 로 실시간 메모리 사용량을 본다.

1. **Heap Dump**: 특정 시점의 메모리 스냅샷
2. **Allocation Tracking**: 객체 할당 추적
3. **Leak Detection**: 자동 누수 감지

#### dumpsys meminfo

```bash
# 특정 앱 메모리 상세 정보
adb shell dumpsys meminfo com.example.app

# 출력 예시:
# App Summary
#                       Pss(KB)
#                        ------
#           Java Heap:     8192
#         Native Heap:    12345
#                Code:     4567
#               Stack:      123
#            Graphics:    23456
#       Private Other:     1234
#              System:     5678
# 
#               TOTAL:    55595       TOTAL SWAP PSS:        0
```

**주요 항목:**
- **Java Heap**: Java/Kotlin 객체
- **Native Heap**: C/C++ 할당 (JNI, 네이티브 라이브러리)
- **Graphics**: 텍스처, 버퍼
- **Code**: DEX, SO 파일
- **Stack**: 스레드 스택

### 프로세스 격리와 샌드박스

#### UID 기반 격리

각 앱은 고유한 [[android-glossary#uid|UID]] 를 받는다.

```bash
# 앱의 UID 확인
adb shell dumpsys package com.example.app | grep userId
# 예: userId=10123

# 해당 UID 의 파일 권한
adb shell ls -l /data/data/com.example.app
# drwx------ 5 u0_a123 u0_a123 4096 2024-01-01 12:00 .
```

**SharedUserId** (Deprecated):
같은 서명의 앱들이 UID 를 공유할 수 있었으나, 보안상 권장하지 않음.

#### Isolated Process

권한이 거의 없는 특수 프로세스.

```xml
<service
    android:name=".IsolatedService"
    android:isolatedProcess="true" />
```

**특징:**
- 고유 UID 부여 (99000-99999)
- 네트워크 접근 불가
- 파일 시스템 접근 극히 제한
- 웹 렌더링 엔진 같은 신뢰할 수 없는 코드 실행에 적합

### 멀티 프로세스 앱

하나의 앱이 여러 프로세스를 가질 수 있다.

```xml
<service
    android:name=".HeavyService"
    android:process=":heavy" />
<!-- 프로세스명: com.example.app:heavy -->

<activity
    android:name=".RemoteActivity"
    android:process="com.example.remote" />
<!-- 독립 프로세스명: com.example.remote -->
```

**주의사항:**
- 각 프로세스는 별도의 Application 인스턴스를 가짐
- static 변수가 공유되지 않음
- 프로세스 간 통신은 [Binder/AIDL](android-binder-and-ipc.md) 필요

```kotlin
class MyApplication : Application() {
    override fun onCreate() {
        super.onCreate()
        val processName = getProcessName()
        Log.d("App", "Process: $processName")
        
        // 프로세스별로 다른 초기화
        when {
            processName == packageName -> {
                // 메인 프로세스
                initMainProcess()
            }
            processName.endsWith(":heavy") -> {
                // Heavy 프로세스
                initHeavyProcess()
            }
        }
    }
}
```

### 백그라운드 제한

#### Doze Mode

기기가 정지 상태일 때 배터리를 아낀다.

**제한사항:**
- 네트워크 접근 차단
- [[android-glossary#wakelock|Wakelock]] 무시
- AlarmManager 지연
- JobScheduler/WorkManager 지연

**예외:**
- Foreground Service
- High-priority FCM 메시지
- `setExactAndAllowWhileIdle()` 알람 (제한적)

#### App Standby Buckets

앱 사용 빈도에 따라 5단계로 분류.

| Bucket | 설명 | 제한 |
|--------|------|------|
| Active | 현재 사용 중 | 없음 |
| Working Set | 자주 사용 | 약간 제한 |
| Frequent | 가끔 사용 | 중간 제한 |
| Rare | 거의 안 씀 | 강한 제한 |
| Restricted | 문제 앱 | 매우 강한 제한 |

```bash
# 앱의 Standby Bucket 확인
adb shell am get-standby-bucket com.example.app

# 테스트용 강제 설정
adb shell am set-standby-bucket com.example.app rare
```

### 프로세스 사망과 복구

#### 프로세스가 죽는 경우

1. **시스템 종료**: LMKD 에 의한 메모리 회수
2. **크래시**: 처리되지 않은 예외
3. **ANR**: 5초 (Service), 10초 (BroadcastReceiver) 응답 없음
4. **사용자 종료**: 설정에서 강제 종료

#### 상태 복원

```kotlin
class MyActivity : AppCompatActivity() {
    private var counter = 0
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        
        // 프로세스가 죽었다가 재시작된 경우 복원
        counter = savedInstanceState?.getInt("counter") ?: 0
    }
    
    override fun onSaveInstanceState(outState: Bundle) {
        super.onSaveInstanceState(outState)
        outState.putInt("counter", counter)
    }
}

// ViewModel 은 설정 변경에서만 유지됨 (프로세스 사망 시 소실)
// SavedStateHandle 사용 시 프로세스 사망에서도 복원 가능
class MyViewModel(private val savedStateHandle: SavedStateHandle) : ViewModel() {
    var counter: Int
        get() = savedStateHandle.get<Int>("counter") ?: 0
        set(value) { savedStateHandle.set("counter", value) }
}
```

### 성능 최적화

#### 메모리 사용 줄이기

```kotlin
// 큰 비트맵 다운샘플링
fun decodeSampledBitmap(res: Resources, resId: Int, reqWidth: Int, reqHeight: Int): Bitmap {
    return BitmapFactory.Options().run {
        inJustDecodeBounds = true
        BitmapFactory.decodeResource(res, resId, this)
        
        inSampleSize = calculateInSampleSize(this, reqWidth, reqHeight)
        inJustDecodeBounds = false
        
        BitmapFactory.decodeResource(res, resId, this)
    }
}

// 객체 풀 사용
class ObjectPool<T>(private val factory: () -> T) {
    private val pool = mutableListOf<T>()
    
    fun acquire(): T = pool.removeLastOrNull() ?: factory()
    fun release(obj: T) { pool.add(obj) }
}
```

#### 프로세스 시작 최적화

```kotlin
// Application.onCreate() 최적화
class MyApplication : Application() {
    override fun onCreate() {
        super.onCreate()
        
        // ✅ 필수 초기화만 동기 실행
        initCrashReporting()
        
        // ✅ 나머지는 비동기
        GlobalScope.launch(Dispatchers.Default) {
            initAnalytics()
            initImageLoader()
        }
        
        // ✅ 지연 초기화 (필요할 때)
        // DI 프레임워크의 lazy injection 활용
    }
}
```

### 디버깅

```bash
# 프로세스 목록
adb shell ps | grep com.example

# 프로세스 상세 정보
adb shell dumpsys activity processes

# 메모리 압박 시뮬레이션
adb shell am send-trim-memory com.example.app RUNNING_CRITICAL

# 프로세스 강제 종료
adb shell am force-stop com.example.app

# GC 강제 실행
adb shell am dumpheap <pid> /data/local/tmp/heap.hprof
```

### 더 보기

[android-zygote-and-runtime](android-zygote-and-runtime.md), [android-activity-manager-and-system-services](android-activity-manager-and-system-services.md), [android-performance-and-debug](../06_testing_performance/android-performance-and-debug.md), [android-app-components-deep-dive](../02_app_framework/android-app-components-deep-dive.md), [android-security-and-sandboxing](../05_security_privacy/android-security-and-sandboxing.md)
