# 성능 검증 벤치마크 (`StartupBenchmarks.kt`)
`MacrobenchmarkRule`은 프로필 활성화 여부에 따라 시작 성능 속도를 다회 반복 측정하여 데이터 리포트를 수집합니다.

```kotlin
package com.benefit.virtualmate.baselineprofile

import androidx.benchmark.macro.BaselineProfileMode
import androidx.benchmark.macro.CompilationMode
import androidx.benchmark.macro.StartupMode
import androidx.benchmark.macro.StartupTimingMetric
import androidx.benchmark.macro.junit4.MacrobenchmarkRule
import androidx.test.ext.junit.runners.AndroidJUnit4
import androidx.test.filters.LargeTest
import androidx.test.platform.app.InstrumentationRegistry
import androidx.test.uiautomator.By
import androidx.test.uiautomator.Direction
import androidx.test.uiautomator.Until
import org.junit.Rule
import org.junit.Test
import org.junit.runner.RunWith

@RunWith(AndroidJUnit4::class)
@LargeTest
class StartupBenchmarks {

    @get:Rule
    val rule = MacrobenchmarkRule()

    @Test
    fun startupCompilationNone() = benchmark(CompilationMode.None())

    @Test
    fun startupCompilationBaselineProfiles() = benchmark(
        CompilationMode.Partial(BaselineProfileMode.Require)
    )

    private fun benchmark(compilationMode: CompilationMode) {
        rule.measureRepeated(
            packageName = InstrumentationRegistry.getArguments().getString("targetAppId")
                ?: throw Exception("targetAppId argument is missing"),
            metrics = listOf(StartupTimingMetric()),
            compilationMode = compilationMode,
            startupMode = StartupMode.COLD,
            iterations = 5,
            setupBlock = { pressHome() }
        ) {
            // 앱 실행
            startActivityAndWait()

            // Generator와 동일하게 복잡한 조작 흐름 측정
            device.wait(Until.hasObject(By.res("start_button")), 5000)
            device.findObject(By.res("start_button"))?.click()
        }
    }
}
```
