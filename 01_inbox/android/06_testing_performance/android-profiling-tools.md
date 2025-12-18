---
title: android-profiling-tools
tags: [android, android/profiling, android/performance, android/tools]
aliases: []
date modified: 2025-12-16 16:19:14 +09:00
date created: 2025-12-16 16:19:14 +09:00
---

## Android Profiling Tools android android/profiling android/performance

성능 분석 도구 사용법. 기본은 [android-performance-and-debug](android-performance-and-debug.md) 참고.

### Android Studio Profiler

실시간 CPU, 메모리, 네트워크, 에너지 모니터링.

#### CPU Profiler

**사용법:**
1. Android Studio → View → Tool Windows → Profiler
2. 앱 선택 후 CPU 타임라인 클릭
3. Record 버튼 → 작업 수행 → Stop

**Trace 종류:**
- **Sample Java Methods**: 낮은 오버헤드, 대략적 분석
- **Trace Java Methods**: 정확하지만 느림
- **Sample C/C++ Functions**: 네이티브 코드 분석
- **Trace System Calls**: 시스템 레벨 추적

**분석:**
```
Call Chart: 시간 순서대로 호출 표시
Flame Chart: 소요 시간 기준 정렬
Top Down: 호출자 → 피호출자
Bottom Up: 피호출자 → 호출자 (병목 찾기 좋음)
```

#### Memory Profiler

**Heap Dump:**
1. Memory 타임라인에서 Dump Java heap 클릭
2. Class List 에서 메모리 많이 차지하는 클래스 확인
3. Instance View 에서 개별 객체 검사
4. References 에서 누가 참조하는지 확인

**Allocation Tracking:**
```kotlin
// 특정 구간 추적
fun loadData() {
    // 여기서 Record allocation 시작
    val list = mutableListOf<String>()
    repeat(10000) {
        list.add("Item $it")
    }
    // Stop → 어디서 할당되었는지 확인
}
```

**메모리 누수 감지:**
1. 의심되는 화면 열기
2. Heap dump 생성
3. 화면 닫기
4. GC 강제 실행 (Profiler 에서 Initiate GC)
5. 다시 Heap dump
6. Activity/Fragment 인스턴스가 남아있는지 확인

#### Network Profiler

**분석 항목:**
- 요청/응답 크기
- 타임라인
- 요청 헤더/바디
- 응답 헤더/바디
- Call Stack (어디서 호출했는지)

```kotlin
// OkHttp Interceptor 로 상세 로깅
val loggingInterceptor = HttpLoggingInterceptor().apply {
    level = HttpLoggingInterceptor.Level.BODY
}

val client = OkHttpClient.Builder()
    .addInterceptor(loggingInterceptor)
    .build()
```

#### Energy Profiler

배터리 소모 분석.

**주요 지표:**
- CPU 사용량
- 네트워크 활동
- GPS 사용
- Wakelock 획득

### Perfetto

시스템 전체 성능 추적.

#### 사용법

```bash
# 1. 추적 시작
adb shell perfetto \
  -c - --txt \
  -o /data/misc/perfetto-traces/trace \
  <<EOF
buffers: {
    size_kb: 63488
    fill_policy: DISCARD
}
data_sources: {
    config {
        name: "linux.ftrace"
        ftrace_config {
            ftrace_events: "sched/sched_switch"
            ftrace_events: "power/suspend_resume"
            ftrace_events: "sched/sched_wakeup"
            ftrace_events: "sched/sched_waking"
            ftrace_events: "sched/sched_process_exit"
            ftrace_events: "sched/sched_process_free"
            ftrace_events: "task/task_newtask"
            ftrace_events: "task/task_rename"
            atrace_categories: "gfx"
            atrace_categories: "view"
            atrace_categories: "webview"
            atrace_categories: "camera"
            atrace_categories: "dalvik"
            atrace_categories: "power"
        }
    }
}
duration_ms: 10000
EOF

# 2. 앱 실행 및 작업 수행

# 3. 추적 파일 가져오기
adb pull /data/misc/perfetto-traces/trace trace.perfetto-trace

# 4. 분석
# https://ui.perfetto.dev 에서 trace.perfetto-trace 열기
```

#### 코드에서 추적

```kotlin
import android.os.Trace

fun expensiveOperation() {
    Trace.beginSection("ExpensiveOperation")
    try {
        // 작업 수행
        processData()
    } finally {
        Trace.endSection()
    }
}

// Async 추적
fun asyncOperation() {
    val cookie = 1
    Trace.beginAsyncSection("AsyncOperation", cookie)
    
    lifecycleScope.launch {
        delay(1000)
        Trace.endAsyncSection("AsyncOperation", cookie)
    }
}
```

### Simpleperf

CPU 프로파일링 (네이티브 코드 포함).

```bash
# 1. 앱 프로파일링
adb shell simpleperf record -p <pid> -o /data/local/tmp/perf.data

# 2. 파일 가져오기
adb pull /data/local/tmp/perf.data

# 3. 리포트 생성
simpleperf report -i perf.data

# 4. 플레임 그래프
simpleperf report -i perf.data --gui
```

### Macrobenchmark

앱 시작, 스크롤 등 성능 측정.

```kotlin
// build.gradle.kts (benchmark 모듈)
plugins {
    id("com.android.test")
    id("androidx.benchmark")
}

android {
    defaultConfig {
        testInstrumentationRunner = "androidx.benchmark.junit4.AndroidBenchmarkRunner"
    }
    
    testBuildType = "release"
    
    buildTypes {
        release {
            isDebuggable = true
            signingConfig = signingConfigs.getByName("debug")
        }
    }
}

dependencies {
    implementation("androidx.benchmark:benchmark-macro-junit4:1.2.2")
    implementation("androidx.test.ext:junit:1.1.5")
    implementation("androidx.test.uiautomator:uiautomator:2.2.0")
}
```

```kotlin
// StartupBenchmark.kt
@RunWith(AndroidJUnit4::class)
class StartupBenchmark {
    
    @get:Rule
    val benchmarkRule = MacrobenchmarkRule()
    
    @Test
    fun startup() = benchmarkRule.measureRepeated(
        packageName = "com.example.app",
        metrics = listOf(StartupTimingMetric()),
        iterations = 5,
        startupMode = StartupMode.COLD
    ) {
        pressHome()
        startActivityAndWait()
    }
    
    @Test
    fun scrollBenchmark() = benchmarkRule.measureRepeated(
        packageName = "com.example.app",
        metrics = listOf(FrameTimingMetric()),
        iterations = 5,
        setupBlock = {
            startActivityAndWait()
        }
    ) {
        val recyclerView = device.findObject(By.res("recycler_view"))
        recyclerView.setGestureMargin(device.displayWidth / 5)
        recyclerView.fling(Direction.DOWN)
        device.waitForIdle()
    }
}
```

```bash
# 실행
./gradlew :benchmark:connectedCheck

# 결과 확인
# benchmark/build/outputs/connected_android_test_additional_output/
```

### Baseline Profile

자주 사용되는 코드를 미리 컴파일.

```kotlin
// build.gradle.kts (benchmark 모듈)
dependencies {
    implementation("androidx.benchmark:benchmark-macro-junit4:1.2.2")
    implementation("androidx.profileinstaller:profileinstaller:1.3.1")
}
```

```kotlin
@ExperimentalBaselineProfilesApi
@RunWith(AndroidJUnit4::class)
class BaselineProfileGenerator {
    
    @get:Rule
    val baselineProfileRule = BaselineProfileRule()
    
    @Test
    fun startup() = baselineProfileRule.collect(
        packageName = "com.example.app",
        profileBlock = {
            pressHome()
            startActivityAndWait()
            
            // 주요 사용자 플로우 수행
            device.findObject(By.text("Login")).click()
            device.waitForIdle()
            
            device.findObject(By.res("username")).text = "user"
            device.findObject(By.res("password")).text = "pass"
            device.findObject(By.text("Submit")).click()
            device.waitForIdle()
        }
    )
}
```

```bash
# Baseline Profile 생성
./gradlew :benchmark:pixel6Api31BenchmarkAndroidTest \
  -P android.testInstrumentationRunnerArguments.class=BaselineProfileGenerator

# 생성된 파일을 앱 모듈로 복사
# benchmark/build/outputs/managed_device_android_test_additional_output/
# → app/src/main/baseline-prof.txt
```

### Layout Inspector

UI 계층 구조 분석.

**사용법:**
1. Tools → Layout Inspector
2. 실행 중인 앱 선택
3. 3D 뷰로 레이어 확인
4. 속성 패널에서 각 View 의 속성 확인

**성능 팁:**
- 중첩 깊이 줄이기 (ConstraintLayout 사용)
- 불필요한 배경 제거
- ViewStub 으로 지연 로딩

### dumpsys

시스템 서비스 정보 확인.

```bash
# 메모리
adb shell dumpsys meminfo com.example.app

# CPU
adb shell dumpsys cpuinfo

# 배터리
adb shell dumpsys batterystats com.example.app

# 그래픽
adb shell dumpsys gfxinfo com.example.app

# Activity
adb shell dumpsys activity com.example.app

# 네트워크
adb shell dumpsys netstats

# 알람
adb shell dumpsys alarm
```

### Battery Historian

배터리 사용 분석.

```bash
# 1. 배터리 통계 초기화
adb shell dumpsys batterystats --reset

# 2. 앱 사용

# 3. 통계 수집
adb bugreport bugreport.zip

# 4. Battery Historian 실행
docker run -p 9999:9999 gcr.io/android-battery-historian/stable:3.1 --port 9999

# 5. http://localhost:9999 에서 bugreport.zip 업로드
```

### LeakCanary

메모리 누수 자동 감지.

```kotlin
// build.gradle.kts
dependencies {
    debugImplementation("com.squareup.leakcanary:leakcanary-android:2.12")
}

// 자동으로 누수 감지 및 알림
// 커스터마이징
class MyApplication : Application() {
    override fun onCreate() {
        super.onCreate()
        
        LeakCanary.config = LeakCanary.config.copy(
            dumpHeap = true,
            retainedVisibleThreshold = 3
        )
    }
}
```

### StrictMode

메인 스레드 위반 감지.

```kotlin
class MyApplication : Application() {
    override fun onCreate() {
        super.onCreate()
        
        if (BuildConfig.DEBUG) {
            StrictMode.setThreadPolicy(
                StrictMode.ThreadPolicy.Builder()
                    .detectDiskReads()
                    .detectDiskWrites()
                    .detectNetwork()
                    .penaltyLog()
                    .penaltyDeath() // 크래시
                    .build()
            )
            
            StrictMode.setVmPolicy(
                StrictMode.VmPolicy.Builder()
                    .detectLeakedSqlLiteObjects()
                    .detectLeakedClosableObjects()
                    .detectActivityLeaks()
                    .penaltyLog()
                    .build()
            )
        }
    }
}
```

### 더 보기

[android-performance-and-debug](android-performance-and-debug.md), [android-testing-and-quality](android-testing-and-quality.md), [android-compose-internals](../02_app_framework/android-compose-internals.md), [android-process-and-memory](../01_system_internals/android-process-and-memory.md)
