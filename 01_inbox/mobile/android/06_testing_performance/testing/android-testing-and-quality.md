---
title: android-testing-and-quality
tags: []
aliases: []
date modified: 2026-04-05 17:43:48 +09:00
date created: 2026-03-21 16:47:09 +09:00
---

## [[mobile-security]] > [[android-testing-and-quality]]

### Testing & Quality: Engineering Excellence

안드로이드 앱의 신뢰성을 보장하기 위한 **테스트 피라미드(Test Pyramid)**와 **유닛 테스트**, **UI 테스트(Espresso/Compose)** 기법을 분석합니다.

단순히 버그를 찾는 것을 넘어, 테스트 가능한 아키텍처를 설계하고 지속적 통합(CI) 환경에서 품질을 자동화하는 전략을 수립하는 것이 목표입니다.

#### 💡 Context: 테스트 가능한 아키텍처

견고한 앱은 코드 작성 단계부터 테스트를 고려해야 합니다. [[android-jetpack-architecture]] 의 핵심은 테스트 용이성(Testability)이며, 이는 곧 앱의 유지보수성과 직결됩니다. [[android-foundations]] 에서 강조한 엔지니어링 원칙의 실천 단계입니다.

#### 어떤 테스트가 있나

- 단위 테스트: 비즈니스 로직을 JVM 에서 빠르게 돌린다.
- 기기/에뮬레이터 테스트: UI 테스트(**UI Test with Compose**), 통합 (Instr), 성능 (Macrobenchmark).
>[!WARNING] **Devil's Advocate : 안녕, Espresso**
>`Espresso` 는 레이아웃 계층 `findViewById` 시절에 만들어진 무거운 프레임워크입니다. Compose 로 UI 를 구축하는 모던 안드로이드 환경에서는 `compose-ui-test` API 를 사용해야 하며, Espresso 와 UI Automator 를 혼용하는 것은 레거시 유지보수 목적일 뿐 신규 구축에서는 배제해야 합니다.
- 플랫폼 호환성: CTS/VTS/GTS 로 OS/HAL 이 규격을 지키는지 확인.
- 퍼지·샌리타이저: 네이티브 코드 안전성 강화.

#### 설계와 테스트 용이성

- MVVM/MVI 로 UI 와 로직을 분리하면 테스트가 쉽다.
- 의존성 주입 (Hilt/Koin/Dagger) 으로 가짜 (Stub/Fake) 를 넣어볼 수 있다.
- 시간/네트워크/저장을 추상화해 빠르게 반복 테스트한다.

#### 도구

- JUnit + Truth/AssertJ, Coroutine Test Rule 로 스레드를 제어.
- Compose Semantics 테스트 API. (Espresso IdlingResource 등 레거시 도구 지양)
- Snapshot/Screenshot 테스트로 UI 깨짐을 감시.

#### 기기 관리

- Gradle Managed Devices/에뮬레이터 스냅샷으로 빠르게 실행.
- FTL/클라우드 팜으로 여러 기기에서 병렬 테스트.
- 로캘/화면 크기/회전/다크 모드 매트릭스로 돌려본다.

#### 회귀를 막는 법

- 변경된 코드에 영향 있는 테스트만 추려 실행 (테스트 영향 분석).
- 플래키 테스트는 격리·수정 후 다시 합친다.
- 커버리지/린트/CI 에서 빨간불이면 고치고 넘어간다.

#### 성능·배터리 테스트

- Macrobenchmark 로 시작/스크롤/자원 사용을 잰다.
- Perfetto 로 CPU/GPU/네트워크 타임라인을 확인한다.
- batterystats/Battery Historian 으로 상위 소모원을 찾는다.

#### 출시 준비 체크

- 권한/프라이버시 흐름 검토, 접근성 (글자 크기/콘트라스트/포커스) 확인.
- R8 난독화 경고, 크래시/ANR 지표 (Play Vitals) 를 모니터링.
- 롤백·원격 플래그로 위험을 줄인다.

#### 문화

- 버그 재현 로그 (스크린레코드 +bugreport) 를 남기고 공유한다.
- 실험은 작은 비율부터, 실패 시 빠른 롤백.
- 회고/기술 문서를 남겨 다음에 같은 실수를 줄인다.

#### Screenshot Testing (UI 회귀 방지)

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

#### See Also

- [[android-foundations]]
- [[android-performance-and-debug]]
- [[android-os-development-guide]]
