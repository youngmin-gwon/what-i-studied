# Macrobenchmark

상위 노트: [[android-profiling-tools]]

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
