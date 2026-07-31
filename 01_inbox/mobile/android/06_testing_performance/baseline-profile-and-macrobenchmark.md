# Baseline Profile & Macrobenchmark 성능 최적화 가이드

이 문서는 앱의 시작 속도(Startup Time)를 개선하고 화면 전환 시의 프레임 저하(Jank)를 차단하기 위해 **Baseline Profile**과 **Jetpack Macrobenchmark**를 적용하는 방법과 관리 프로세스를 정리합니다. 

본 문서는 Google의 [Baseline Profile 가이드라인](https://developer.android.com/topic/performance/baselineprofiles) 및 최신 Gradle 플러그인 연동 규격을 반영하여 작성되었습니다.

---

## 1. 성능 최적화 동작 원리 (Baseline Profile, Macrobenchmark & Cloud Profile)

### 1-1. Baseline Profile 이란?
안드로이드 앱이 실행될 때 ART(Android Runtime)는 JIT(Just-In-Time) 컴파일과 인터프리터를 통해 기계어로 코드를 해석합니다. 이 과정에서 최초 앱 구동 시 CPU 부하가 집중되어 성능이 저하될 수 있습니다.
* **Baseline Profile**은 앱 내의 **자주 실행되는 주요 코드 경로(Hot Paths)**를 파일 형태(`baseline-prof.txt`)로 기록하여 배포 패키지(AAB/APK)에 동반시키는 기술입니다.
* 사용자가 Google Play 스토어에서 앱을 다운로드 및 설치할 때, 스토어 인스톨러가 프로필 데이터를 보고 최적화 대상을 파악하여 **미리 AOT(Ahead-Of-Time) 컴파일**을 완료합니다.
* 이를 통해 첫 실행(Cold Start) 속도가 최대 30~40% 이상 빨라지고 가시적인 프레임 버벅임이 대폭 줄어듭니다.

### 1-2. Cloud Profile과의 상호 보완 관계 (배포 시 운영 가이드)
Google Play 콘솔은 앱 배포 이후 실제 사용자들의 사용 데이터를 익명으로 수집(JIT 프로필 수집)하여 **Cloud Profile**을 자동으로 생성합니다.
* **Cloud Profile의 특징**: 개발자가 별도의 코드를 작성하거나 수동으로 추출하여 파일로 관리할 필요가 없으며, Google Play 서비스가 배포 완료 후 백그라운드에서 자동으로 관리하고 병합(Merge)합니다.
* **상호 보완 필요성 (Cold Start / Day 1 문제)**:
  * 신규 버전이 배포된 직후(Day 1)에는 아직 사용자가 사용한 데이터가 없어 **Cloud Profile이 존재하지 않는 공백기**가 생깁니다. 이 시기에는 최적화 가이드가 없어 사용자들이 앱이 버벅인다고 느낄 수 있습니다.
  * 개발자가 배포 시점에 **Baseline Profile**을 함께 패키징해 배포하면, Cloud Profile이 아직 생성되지 않은 버전 출시 극초기에도 **첫 다운로드 즉시 강력한 최적화 성능을 확보**할 수 있습니다.
  * 시간이 흐른 뒤 유저 데이터가 누적되면 Google Play가 [Baseline Profile] + [Cloud Profile]을 결합하여 더욱 정교한 최적화 맵으로 자동 갱신해 다운로드 처리를 돕습니다.
* **배포 관리 프로세스**:
  * 매 개발 빌드마다 재생성할 필요는 없으며, **운영 서버 배포(Production Release) 직전에만 1회 생성**하여 업데이트된 `baseline-prof.txt` 파일을 Git에 올려 배포 본체에 반영하는 사이클로 운영하면 번거로움을 최소화할 수 있습니다.

### 1-3. Macrobenchmark의 역할
* 벤치마크 테스트 코드를 통해 앱의 실제 성능 변화를 밀리초(ms) 단위의 리포트 및 성능 추적 파일(Trace)로 출력합니다.
* Baseline Profile이 있을 때와 없을 때(`CompilationMode.None` vs `CompilationMode.Partial`)의 속도 지표를 객관적으로 측정 및 검증하는 역할을 수행합니다.

---

## 2. Version Catalog (`libs.versions.toml`) 설정

의존성 격리와 라이브러리 정렬을 위해 Gradle Version Catalog에 관련 라이브러리 및 플러그인을 다음과 같이 설정하여 관리합니다.

### 2-1. versions, libraries, plugins, bundles 맵 구성
```toml
[versions]
# Baseline Profile & Macrobenchmark. 앱 시작 속도 및 프레임 성능 최적화 도구에 사용한다.
# ※ 최신 AGP (예: 9.4.0-alpha04) 호환을 위해 1.5.0-alpha07 이상 버전을 적용한다.
baselineprofile = "1.5.0-alpha07"
uiautomator = "2.4.0"

[libraries]
# Macrobenchmark.
# 앱 시작(Startup) 속도 및 프레임 버벅임(Jank) 성능을 측정하는 벤치마크 및 프로필 생성에 사용한다.
androidx-benchmark-macro-junit4 = { module = "androidx.benchmark:benchmark-macro-junit4", version.ref = "baselineprofile" }

# Profile Installer.
# 배포용 APK 패키징 시 AOT 컴파일을 위해 앱 내에 Baseline Profile을 설치하고 컴파일할 때 사용한다.
androidx-profileinstaller = { group = "androidx.profileinstaller", name = "profileinstaller", version.ref = "baselineprofile" }

# UI Automator.
# Macrobenchmark 측정 및 Baseline Profile 생성 과정에서 앱 외부 프로세스 경계를 넘어 디바이스/시스템을 제어할 때 필요하다.
androidx-test-uiautomator = { module = "androidx.test.uiautomator:uiautomator", version.ref = "uiautomator" }

[plugins]
# Android Standalone Test plugin.
# 라이브러리나 앱 모듈이 아닌, 독립적인 테스트 전용 모듈을 구성할 때 적용한다. (예: :baselineprofile)
android-test = { id = "com.android.test", version.ref = "agp" }

# Android Baseline Profile plugin.
# 앱이나 라이브러리 모듈에서 Baseline Profile 생성 및 컴파일 설정을 자동화할 때 사용한다.
androidx-baselineprofile = { id = "androidx.baselineprofile", version.ref = "baselineprofile" }

[bundles]
# Baseline Profile / Benchmark 기본 세트
baselineprofile-generator = [
    "androidx-benchmark-macro-junit4",
    "androidx-junit",
    "androidx-test-uiautomator",
]
```

> [!WARNING]
> **AGP(Android Gradle Plugin)와의 호환성 주의**:
> 최신 AGP 버전을 사용할 때 하위 버전의 Baseline Profile 플러그인을 적용하면 `Extension of type 'TestExtension' does not exist` 빌드 오류가 발생할 수 있습니다. 사용 중인 AGP 릴리즈 시점에 정렬하여 플러그인 버전을 최신 버전(예: `1.5.0-alphaXX`)으로 상향해야 합니다.

---

## 3. 모듈별 빌드 파일 (`build.gradle.kts`) 설정

기존 프로젝트의 멀티 모듈 의존성 구조를 존중하여 독립된 테스트 모듈 `:baselineprofile`을 등록하고 `:app` 모듈과 연결합니다.

### 3-1. 프로젝트 루트 `settings.gradle.kts`
새로운 빌드 타겟으로 `:baselineprofile`을 선언합니다.
```kotlin
include(":baselineprofile")
```

### 3-2. 독립형 `:baselineprofile/build.gradle.kts`
`com.android.test` 플러그인을 사용하여 최적화를 캡처할 독립형 테스트 타겟으로 설정합니다.

```kotlin
plugins {
    alias(libs.plugins.android.test)              // com.android.test
    alias(libs.plugins.androidx.baselineprofile)      // androidx.baselineprofile
    alias(libs.plugins.kotlin.android)
}

android {
    namespace = "com.benefit.virtualmate.baselineprofile"
    compileSdk = 35

    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_21
        targetCompatibility = JavaVersion.VERSION_21
    }
    kotlinOptions {
        jvmTarget = "21"
    }

    defaultConfig {
        minSdk = 28 // Macrobenchmark 측정은 API 28 이상 권장
        targetSdk = 37
        testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"
    }

    targetProjectPath = ":app" // 최적화 대상 애플리케이션 모듈 바인딩
}

dependencies {
    // libs.versions.toml에 등록한 테스트 전용 번들 주입
    implementation(libs.bundles.baselineprofile.generator)
    implementation(libs.androidx.espresso.core) // 간혹 필요한 에스프레소 기본 의존성
}
```

### 3-3. 애플리케이션 `:app/build.gradle.kts`
생성된 프로필 파일이 릴리즈에 자동 번들링되도록 플러그인을 연동하고, 앱 전용 인프라 구성 패키지(`app-infrastructure` 번들)를 주입합니다.

```kotlin
plugins {
    alias(libs.plugins.android.application)
    alias(libs.plugins.androidx.baselineprofile) // 1) 플러그인 추가
    // ...
}

dependencies {
    // 2) baselineProfile 구성을 사용해 생성기 모듈과 바인딩
    baselineProfile(project(":baselineprofile"))

    // 3) 앱 전용 기본 인프라/최적화 구성 번들 추가 (ProfileInstaller 및 SplashScreen 포함)
    implementation(libs.bundles.app.infrastructure)
}
```

---

## 4. 최적화 및 벤치마크 코드 구현

### 4-1. Jetpack Compose UI에서의 UI Automator 조작 고도화
기본적으로 Macrobenchmark와 Baseline Profile 테스트 코드는 타겟 앱과 **완전히 분리된 격리 프로세스**에서 디바이스를 통제합니다. 
Compose UI 요소를 찾고 조작하려면 컴포저블에 `testTag`를 명시적으로 부여하여 UI Automator가 `resource-id`로 이를 찾아갈 수 있게 세팅해야 합니다.

* **앱 컴포저블 대상 지정**:
```kotlin
LazyColumn(
    modifier = Modifier
        .fillMaxSize()
        .testTag("exercise_list_view") // testTag 부여
) {
    // ...
}
```

### 4-2. 프로필 생성기 (`BaselineProfileGenerator.kt`)
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

### 4-3. 성능 검증 벤치마크 (`StartupBenchmarks.kt`)
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

### 4-2. ADB 명령어를 통한 로컬 수동 검증 및 컴파일 시뮬레이션
로컬 개발 단계에서 Benchmark 코드 외에 **실제 단말에 프로필이 주입되어 작동하는지 수동으로 확인**하고 싶다면, 다음의 `adb` 명령어를 통해 ART(Android Runtime) 컴파일 상태를 강제로 시뮬레이션할 수 있습니다. (※ 에뮬레이터 또는 루팅된 실기기 환경 권장)

#### 1) 기존 컴파일 상태 초기화
앱을 순수 설치 상태(최적화 없는 상태, `CompilationMode.None`에 해당)로 복구합니다.
```bash
adb shell cmd package compile --reset <앱_패키지_명>
```

#### 2) Baseline Profile 강제 컴파일 적용
앱 패키지에 동반된 `baseline-prof.txt`를 기반으로 부분 AOT 컴파일을 수행합니다. (`CompilationMode.Partial`에 해당)
```bash
adb shell cmd package compile -m speed-profile -f <앱_패키지_명>
```

#### 3) Full AOT 컴파일 적용 (대조군 테스트용)
가장 극대화된 컴파일러 최적화 성능 지표를 테스트해볼 때 사용합니다. (`CompilationMode.Full`에 해당)
```bash
adb shell cmd package compile -m speed -f <앱_패키지_명>
```

#### 4) 현재 최적화/컴파일 상태 확인
해당 패키지가 어떠한 모드(speed, speed-profile 등)로 최적화되어 동작 중인지 로그로 검증합니다.
```bash
adb shell dumpsys package dexopt | grep -A 1 <앱_패키지_명>
```
출력 결과 로그 중 `[status=speed-profile]` 또는 `[reason=install-with-dexmetadata]` 등의 구문을 보고 컴파일 지도가 정상 적용되었는지 직접 판별할 수 있습니다.

---

## 5. 실무 운영 및 CI/CD 관리 가이드

### 5-1. 로컬 기반의 최적화 생성 및 관리 프로세스 (반자동 방식)
수동 기기 설정이나 CI 가상 리소스 제한으로 인해 수동 방식을 많이 활용합니다.

1. **기기 연결**: 루팅된 AOSP 에뮬레이터 또는 API 33+ 실제 디바이스를 연결합니다.
2. **태스크 실행**:
   ```bash
   ./gradlew :app:generateBaselineProfile
   ```
3. **결과 확인**: 플러그인이 빌드 완료 후 자동으로 최적화 지도인 `baseline-prof.txt`를 생성하여 `:app/src/main/baselineProfiles/` 디렉터리에 이식합니다.
4. **버전 관리**: 새로 추출되거나 업데이트된 `baseline-prof.txt` 파일을 **반드시 Git 저장소에 커밋**해야 빌드 파이프라인에서 정상 작동합니다.

### 5-2. CI/CD 가상 파이프라인 자동화 (AOT 가상 구동 방식 - GMD)
물리적인 디바이스가 없는 CI/CD 서버 환경(GitHub Actions, Bitrise 등)에서 Baseline Profile을 자동으로 빌드하려면 **GMD (Gradle Managed Device)** 설정을 이용해 가상 단말을 헤드리스(Headless) 모드로 띄워 캡처해야 합니다.

#### 1) GMD 설정 방식 (`baselineprofile/build.gradle.kts`)
가장 가볍고 백그라운드 노이즈가 없는 **AOSP 이미지**를 기반으로 가상 단말을 선언해 둡니다.

```kotlin
android {
    testOptions {
        managedDevices {
            localDevices {
                create("pixel6Api31") {
                    device = "Pixel 6"
                    apiLevel = 31
                    systemImageSource = "aosp" // 구글 API 서비스가 생략된 가벼운 이미지
                }
            }
        }
    }
}
```

#### 2) CI/CD 환경에서의 자동 생성 설정 (`app/build.gradle.kts`)
기본적으로 빌드 시 매번 테스트를 수행하면 빌드가 매우 느려집니다. 따라서 CI/CD 환경(예: 깃허브 액션, Codemagic, Bitrise 등의 플랫폼이 자동으로 제공하는 `CI` 환경 변수가 `true`인 경우)에서만 자동으로 생성 후 패키징하도록 제어합니다.

```kotlin
baselineProfile {
    // CI/CD 환경(환경 변수 CI=true)에서만 릴리즈 빌드(assembleRelease 등) 시 프로필을 자동 생성하여 포함시킵니다.
    automaticGenerationDuringBuild = System.getenv("CI") == "true"
}
```

#### 3) CI/CD 플랫폼별 실행 명령어 (Fastlane 연동)
Fastlane을 사용하여 Codemagic, Bitrise, Azure Pipelines 등에서 배포 파이프라인을 자동화할 때 사용할 수 있는 명령어 예시입니다.

* **수동/자동 갱신 실행**: GMD를 이용해 가상 단말을 띄우고 Baseline Profile을 생성할 때는 다음과 같이 디바이스 타겟 아규먼트를 주어 실행합니다.
  ```bash
  # pixel6Api31 GMD 단말을 띄워서 백그라운드 생성 실행
  ./gradlew :app:generateBaselineProfile -Pandroid.testInstrumentationRunnerArguments.device=pixel6Api31
  ```
  이때 Gradle은 UI(디스플레이 환경)가 없는 CI 머신임을 감지하고 자동으로 `-no-window`(Headless) 및 `-no-audio` 옵션을 에뮬레이터에 적용하여 무화면 상태로 테스트를 수행한 뒤 자동 종료합니다.

* **Fastlane Lane 연동 예시**:
  ```ruby
  lane :release_build do
    # 1. GMD를 이용해 최신 Baseline Profile 생성 (AOSP 헤드리스)
    gradle(
      task: ":app:generateBaselineProfile",
      properties: {
        "android.testInstrumentationRunnerArguments.device" => "pixel6Api31"
      }
    )
    # 2. 프로필이 빌드본에 심어진 상태로 릴리즈 빌드 및 배포 패키지 생성
    gradle(
      task: "bundle",
      flavor: "Production",
      buildType: "Release"
    )
    # 3. Google Play 배포 실행
    upload_to_play_store(track: 'internal')
  end
  ```

> [!NOTE]
> GMD 헤드리스 에뮬레이션은 내부 중첩 가상화(Nested Virtualization)를 활용하므로, CI 빌드 서버가 가상화 가속 기술(예: KVM, macOS 전용 하드웨어 지원)을 지원하는 성능 좋은 요금제 머신(예: Codemagic/Bitrise의 macOS/Linux premium instance)이어야 원활하게 작동합니다. 성능이 부족한 가상 머신 환경에서는 빌드 시간이 극도로 길어지거나 가상 에뮬레이터 에러로 멈출 수 있으므로 테스트 후 적용하시기 바랍니다.


---

## 6. 구글 권장 성능 모니터링 및 추가 최적화 도구 (Google I/O 요약)

Google I/O ("What's new in app performance") 세션에서 제시한 안드로이드 앱 성능 극대화를 위한 로드맵 및 핵심 도구 요약입니다.

### 6-1. JankStats를 이용한 실시간 UI 버벅임(Jank) 추적
로컬 개발 단계(Macrobenchmark)를 넘어, **실제 프로덕션 사용자 환경에서 일어나는 프레임 드랍(Jank)을 모니터링**하기 위해 Jetpack **JankStats** 라이브러리 도입을 권장합니다.
* **동작 원리**: 앱이 렌더링하는 매 프레임의 드로잉 성능을 모니터링하여, 프레임이 일정 기준(예: 16ms / 60Hz, 8.3ms / 120Hz)을 초과할 때 리스너를 호출합니다.
* **사용자 상태 바인딩(Context)**: 버벅임이 발생했을 때 단순히 "버벅였다"는 사실만 수집하는 것이 아니라, 사용자가 현재 어떤 화면을 스크롤 중이었는지, 어떤 Composable이 활성화되어 있었는지의 **UI 상태 정보(State)**를 결합하여 Firebase Performance Monitoring이나 분석 도구로 원격 전송할 수 있습니다.

### 6-2. App Startup 라이브러리를 통한 초기화 시간 단축
여러 오픈소스 및 타사 라이브러리(SDK)들이 앱 실행 단계에서 각각 `ContentProvider` 등을 사용해 개별적으로 초기화를 시도하면 Startup 타임에 큰 오버헤드가 발생합니다.
* **App Startup**을 활용하면 단일 Content Provider 내부에서 모든 종속 라이브러리의 초기화 순서를 결합하여 지연 실행(Lazy Initialization) 및 순차 실행 처리를 단순화하고 시작 속도를 더욱 개선할 수 있습니다.

### 6-3. 프로덕션 최적화 모니터링 루프
구글은 다음과 같은 순환 구조(Performance Loop)를 구축할 것을 권장합니다.
1. **모니터링**: Play Console (Android Vitals) 및 실서비스 **JankStats**를 통해 프레임 저하 및 ANR 유발 요소 상시 분석.
2. **현지화 및 재현**: **Macrobenchmark** 테스트 코드로 의심되는 시나리오(스크롤, 시작 등)를 작성하여 로컬에서 문제를 재현하고 성능 캡처.
3. **최적화 구현**: 비효율적인 Layout 및 Composable 재설계, 무거운 초기화 라이브러리 지연 처리(App Startup), 그리고 최종 배포 전 **Baseline Profile** 업데이트.



