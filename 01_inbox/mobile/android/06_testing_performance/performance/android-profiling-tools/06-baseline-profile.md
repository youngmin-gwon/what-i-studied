# Baseline Profile

상위 노트: [android-profiling-tools](01_inbox/mobile/android/06_testing_performance/performance/android-profiling-tools.md)

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
