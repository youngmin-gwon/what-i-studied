# Screenshot Testing (UI 회귀 방지)

>[!TIP] **스크린샷 테스트 = Compose UI 의 안전장치**
>코드 변경 후 UI 가 의도치 않게 깨졌는지 **픽셀 단위 비교**로 자동 검증한다. Compose 앱에서는 Espresso 보다 훨씬 효과적인 UI 품질 보장 수단이다.

**Roborazzi (JVM, 에뮬레이터 불필요, 권장)**:

```kotlin
// build.gradle.kts
plugins {
    id("io.github.takahirom.roborazzi") version "1.x"
}

@RunWith(RobolectricTestRunner::class)
class UserCardScreenshotTest {
    @get:Rule
    val composeTestRule = createComposeRule()
    
    @Test
    fun userCard_default() {
        composeTestRule.setContent {
            UserCard(User("1", "김영민", "개발자"))
        }
        composeTestRule.onRoot().captureRoboImage("UserCard_default.png")
    }
}
```

**Paparazzi (Square, Layout XML + Compose 지원)**:

```kotlin
class UserCardTest {
    @get:Rule
    val paparazzi = Paparazzi()
    
    @Test
    fun snapshot() {
        paparazzi.snapshot {
            UserCard(User("1", "김영민", "개발자"))
        }
    }
}
```

- **기록(Record)**: `./gradlew recordRoborazziDebug` → 골든 이미지 생성
- **검증(Verify)**: `./gradlew verifyRoborazziDebug` → CI 에서 비교

>[!NOTE] **iOS 비교: Swift UI Preview Tests**
>iOS 에서는 Xcode 의 **Preview** 기능과 **`swift-snapshot-testing`** (Point-Free) 라이브러리가 유사한 역할을 한다.
>Android 의 Roborazzi 가 JVM 에서 실행되는 것처럼, iOS 도 시뮬레이터 없이 스냅샷 테스트가 가능하다.
