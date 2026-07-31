# 프로필 생성기 (`BaselineProfileGenerator.kt`)
테스트 캡처 도구는 `BaselineProfileRule`의 도움을 받아 디바이스 액션을 모방해 핫 경로를 생성합니다.

```kotlin
package com.benefit.virtualmate.baselineprofile

import androidx.benchmark.macro.junit4.BaselineProfileRule
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
class BaselineProfileGenerator {

    @get:Rule
    val rule = BaselineProfileRule()

    @Test
    fun generate() {
        rule.collect(
            packageName = InstrumentationRegistry.getArguments().getString("targetAppId")
                ?: throw Exception("targetAppId argument is missing"),
            includeInStartupProfile = true
        ) {
            // 1. 앱 시작 시나리오 기록
            pressHome()
            startActivityAndWait()

            // 2. Compose 버튼 대기 및 클릭 시나리오 기록
            device.wait(Until.hasObject(By.res("start_button")), 5000)
            device.findObject(By.res("start_button"))?.click()

            // 3. 리스트 로드 대기 및 스크롤 제스처 코드 경로 확보
            device.wait(Until.hasObject(By.res("exercise_list_view")), 5000)
            val listView = device.findObject(By.res("exercise_list_view"))
            if (listView != null) {
                listView.setGestureMargin(device.displayWidth / 5)
                listView.fling(Direction.DOWN) // 하단 스크롤 기록
            }
        }
    }
}
```
