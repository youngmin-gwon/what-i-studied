# Version Catalog (`libs.versions.toml`) 설정

상위 노트: [[baseline-profile-and-macrobenchmark]]

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
