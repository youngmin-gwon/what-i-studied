---
title: android
tags: [android, mobile]
aliases: []
date modified: 2025-07-06 20:56:13 +09:00
date created: 2025-07-06 20:27:45 +09:00
---

## Entrypoint?

`AndroidManifest.xml` 파일의 activity 에서 지정함. 즉, 꼭 MainActivity 가 아닐 수 있음.

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools">
    <application
        android:allowBackup="true"
        android:dataExtractionRules="@xml/data_extraction_rules"
        android:fullBackupContent="@xml/backup_rules"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/Theme.Android101"
        tools:targetApi="31">
        <!-- 여기에서 지정함 -->
        <activity
            android:name=".MainActivity"
            android:exported="true"
            android:label="@string/app_name"
            android:theme="@style/Theme.Android101">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />

                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>

</manifest>
```

## mipmap?

컴퓨터 그래픽스 용어. 3D 게임이나 이미지 렌더링에서 텍스처(이미지)를 다양한 해상도로 미리 만들어 두는 기법.
    - mipmap = "Multum In Parvo" map = "a lot in a small space"
    - 즉 "이미지 레벨이 여러 개 있는 구조", 여러 해상도 이미지를 계층 구조로 나열한 지도
    - 여러 해상도 버전의 이미지를 하나로 다루는 구조

이걸 통해:

- 렌더링 성능 최적화
- 메모리 사용량 감소
- 시각적으로 더 부드러운 결과

앱 아이콘처럼 고해상도 디스플레이에 맞게 다양한 크기로 자동 조정되어야 하는 이미지 리소스를 저장하는 디렉토리.

### mipmap vs drawable

| 항목         | `mipmap`                                      | `drawable`                         |
| ------------ | --------------------------------------------- | ---------------------------------- |
| 목적         | **앱 아이콘 등**, 다양한 화면 밀도에서 최적화 | 일반 이미지 (버튼, 배경 등)        |
| 용도         | 런처 아이콘, 라운드 아이콘 등                 | 버튼 아이콘, 배경, UI 요소         |
| 성능         | 시스템이 런처에서 아이콘을 더 효율적으로 로딩 | 일반적인 이미지 처리 방식          |
| Android 권장 | ✅ **아이콘은 mipmap에** 저장 권장             | ❌ 아이콘을 drawable에 넣는 건 비추 |

### 폴더 구조

```plaintext
res/
├── mipmap-mdpi/       ← 중간 밀도 (160dpi)
├── mipmap-hdpi/       ← 높은 밀도 (240dpi)
├── mipmap-xhdpi/      ← 초고밀도 (320dpi)
├── mipmap-xxhdpi/     ← 더 높은 (480dpi)
├── mipmap-xxxhdpi/    ← 극초고밀도 (640dpi)
├── mipmap-anydpi-v26/ ← Adaptive icon 지원 (API 26+)
```

## Intent?

**Intent는 "의도"**.
"무언가를 하고 싶다"는 요청을 Android 시스템에 전달하는 메시지.

e.g.

어떤 액티비티를 열고 싶을 때:
→ "이 화면을 열어줘!"

연락처에서 사람을 선택하고 싶을 때:
→ "연락처 앱에게 사람 하나 골라달라고 부탁!"

사진을 찍고 싶을 때:
→ "카메라 앱, 사진 좀 찍어줘!"

### Explicit Intent

인텐트가 **정확히 어떤 컴포넌트(Activity, Service 등)**를 호출할지 명확히 지정하는 방식

```kotlin
val intent = Intent(this, DetailActivity::class.java)
startActivity(intent)
```

- 보통 앱 내부에서 액티비티간 이동에 사용됨.
- `Intent-Filter` 없이도 실행됨.

### Implicit Intent

인텐트가 무엇을 하고 싶은지만 설명하고, 어떤 앱(또는 컴포넌트)이 그걸 처리할지는 Android 시스템이 결정

```kotlin
val intent = Intent(Intent.ACTION_VIEW)
intent.data = Uri.parse("https://www.naver.com")
startActivity(intent)
```

- 의도만 표현함
- Android가 적절한 앱(예: Chrome, 네이버 앱)을 찾아 실행해줌
- 이럴 땐 그 앱의 intent-filter가 이 요청을 받을 수 있어야 함

## Intent-Filter?

"나는 이런 요청(intent)을 받아들일 수 있어요!" 라고 선언하는 부분
**앱의 구성요소(Activity, Service, BroadcastReceiver 등)**가
어떤 종류의 요청을 받아서 처리할 수 있는지를 정의하는 XML 설정

## Project Structure

```plaintext
├── app
│   ├── build.gradle.kts
│   ├── proguard-rules.pro
│   └── src
│       ├── androidTest
│       ├── test
│       └── main
│           ├── AndroidManifest.xml
│           ├── java
│           └── res
├── build.gradle.kts
├── settings.gradle.kts
├── gradle.properties
├── local.properties
├── gradlew/gradlew.bat
└── gradle
    ├── wrapper
    └── libs.versions.toml
```

### build.gradle.kts

전체 프로젝트에 적용되는 공통 설정(모듈 레벨 아님)
e.g. 리포지토리 설정, 전역 플러그인, 버전 카탈로그 참조 등

- 플러그인 관리, dependency version 설정 등(보통 많이 비워져 있음)

### settings.gradle.kts

프로젝트에 포함된 모듈 목록 정의(`include(":app")`)

- gradle 빌드 구성 초기화

### gradle.properties

Gradle 빌드 시 사용되는 속성값 정의

예: org.gradle.jvmargs=-Xmx2048m (JVM 메모리 설정), VERSION_NAME=1.0

### local.properties

로컬 환경 전용 설정 파일 (예: SDK 경로)

버전 관리에 포함시키지 않음 (.gitignore에 포함됨)

### gradlew, gradlew.bat

프로젝트에 포함된 Gradle Wrapper 실행 파일

Gradle 설치없이도 동일한 버전으로 빌드 가능하게 해줌

`/gradle/wrapper/gradle-wrapper.properties` 에는 사용할 gradle 버전 명시

### gradle/libs.versions.toml

kotlin DSL에서 사용하는 버전 카탈로그 정의 파일

gradle 7.0 이상 부터 실험적으로 도입된 이후, 7.4 부터 안정화.

기존 방식의 문제:

- 버전이 build.gradle.kts 여기저기에 흩어져 관리됨
- 프로젝트가 커지면 중복/불일치 발생 (특히 다모듈 프로젝트)
- 공통 버전 업데이트가 번거로움

Version Catalog (libs.versions.toml) 도입 목적:

- ✅ 버전 정의의 중앙 집중화
- ✅ 의존성 사용 시 alias로 짧고 명확하게 표현
- ✅ 코드 자동 완성 지원 & IDE 연동 강화
- ✅ 중복 방지, 오류 줄이기

특별한 설정을 하지 않아도 경로에 파일 존재하면 Gradle이 자동으로 인식함.

- 버전, 라이브러리 그룹, 모듈 이름을 분리해서 관리
- build.gradle.kts에서 alias로 접근 가능

사용 방법: `build.gradle.kts`

```toml
[versions]
kotlin = "1.9.10"
compose = "1.6.4"
coroutines = "1.7.3"

[libraries]
kotlin-stdlib = { module = "org.jetbrains.kotlin:kotlin-stdlib", version.ref = "kotlin" }
compose-ui = { module = "androidx.compose.ui:ui", version.ref = "compose" }
coroutines-core = { module = "org.jetbrains.kotlinx:kotlinx-coroutines-core", version.ref = "coroutines" }

[plugins]
kotlin-android = { id = "org.jetbrains.kotlin.android", version.ref = "kotlin" }
```

```gradle
dependencies {
    implementation(libs.kotlin.stdlib)
    implementation(libs.compose.ui)
    implementation(libs.coroutines.core)
}

plugins {
    alias(libs.plugins.kotlin.android)
}
```

### /app/build.gradle.kts

앱 모듈(`:app`)의 개별 빌드 설정
e.g. 컴파일 SDK, 의존성, 빌드 타입, Proguard 설정 등

- 플러그인, 의존성, 빌드 설정 포함(e.g. `compileSdk`, `defaultConfig`)

### /app/proguard-rules.pro

릴리즈 빌드 시 사용하는 난독화(Proguard/R8) 규칙

### /app/src/main/AndroidManifest.xml

앱의 기본 정보와 컴포넌트 등록(e.g. 액티비티, 퍼미션)

Android 앱의 메타데이터를 정의하는 핵심파일.

앱의 구조, 권한, 설정 등을 Android 시스템에 알리는 역할

```xml
<!--
<xml>
- 파일 선언 및 네임스페이스
- xml 파일의 버전과 문자 인코딩 방식 정의.
- 표준 xml 선언.
-->
<?xml version="1.0" encoding="utf-8"?>

<!--
<manifest>
- 앱의 루트, 패키지 및 권한 정의 위치
- xmlns:android : Android 속성 네임스페이스 정의
- xmlns:tools : Android Studio 도구용 추가 네임스페이스

네임스페이스?
- XML 에서 사용하는 속성들의 "출처"를 구분하기 위한 방식.
- XML 에서는 서로 다른 시스템이 제공하는 속성 이름이 충돌하지 않도록 하기 위해 "속성은 어디에서 온것인가" 를 명확히 선언해야함. 이를 구분해주는 것이 "네임스페이스".
- 정의에 따르면 아래는 "android" 라는 접두사가 붙었을 때, "tools" 라는 접두사가 붙었을 때 각각 어디 출처를 따르는지 선언한 것.
-->
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools">

    <!--
    <application>
    - 앱의 전역 설정, 테마, 아이콘 등

    android:allowBackup
    - 사용자가 기기 백업/복원 기능을 사용할 수 있도록 허용.

    android:dataExtractionRules="@xml/data_extraction_rules"
    - 백업/복원 시 어떤 데이터가 추출될지 정의한 XML 파일을 지정. (Android 12 이상)

    android:fullBackupContent="@xml/backup_rules"
    - 전체 백업 콘텐츠 규칙을 정의하는 파일입니다 (백업 제외/포함 항목 지정).

    android:icon="@mipmap/ic_launcher"
    - 앱 아이콘으로 사용될 리소스를 지정합니다.

    android:label="@string/app_name"
    - 앱 이름을 정의합니다. 런처 및 최근 앱 목록에 표시됩니다.

    android:roundIcon="@mipmap/ic_launcher_round"
    - 라운드 버전의 아이콘 (특정 런처에서 사용됨).

    android:supportsRtl="true"
    - RTL(오른쪽에서 왼쪽으로 쓰는 언어) 레이아웃 지원 여부.

    android:theme="@style/Theme.Android101"
    - 앱 전체에서 사용할 기본 테마를 지정합니다.

    tools:targetApi="31"
    - Android Studio 빌드 도구를 위한 힌트입니다. API 31(Android 12) 기준으로 동작을 점검하라는 의미이며, 런타임에는 영향이 없습니다.

    -->
    <application
        android:allowBackup="true"
        android:dataExtractionRules="@xml/data_extraction_rules"
        android:fullBackupContent="@xml/backup_rules"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/Theme.Android101"
        tools:targetApi="31">
        <!--
        <activity>
        - UI 화면 중 하나 정의

        android:name=".MainActivity"
        - 액티비티 클래스 경로입니다. `.`으로 시작하면 기본 패키지 기준으로 com.example.your-app.MainActivity가 됩니다.

        android:exported="true"
        - 이 액티비티가 외부 앱에서 인텐트로 호출 가능한지를 나타냅니다.
        - **Android 12(API 31)**부터는 intent-filter가 있으면 반드시 exported="true" 또는 "false"를 명시해야 함.

        android:label="@string/app_name"
        - 이 액티비티의 표시 이름 (앱 바 등).

        android:theme="@style/Theme.Android101"
        - 이 액티비티만의 테마 (앱 기본 테마와 다르게 지정할 수 있음).
        -->
        <activity
            android:name=".MainActivity"
            android:exported="true"
            android:label="@string/app_name"
            android:theme="@style/Theme.Android101">

            <!--
            <intent-filter>
            - 해당 액티비티가 어떤 인텐트를 수신할 수 있는지 정의
            - 여기서는 런처에 표시될 수 있는 앱의 진입점임을 정의

            `MAIN`: 앱의 시작점이라는 뜻
            `LAUNCHER`: 런처 앱이 이 액티비티를 앱 아이콘으로 보여줄 수 있다는 뜻
            두 개가 같이 선언되어 있어야 런처 아이콘으로 노출 됨.
            -->
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />

                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>

</manifest>
```

### /app/src/res

- `/drawable` : 벡터나 비트맵 이미지
- `mipmap-*/`: 런처 아이콘용 이미지 (해상도별로 나뉨)
- `values/`: 공통 리소스 정의
  - `colors.xml`: 색상
  - `strings.xml`: 문자열
  - `themes.xml`: 테마 스타일
- `xml/`: 설정 XML (예: backup_rules.xml, data_extraction_rules.xml)

### /app/src/androidTest

계측 테스트(디바이스/에뮬레이터 필요)
안드로이드 환경에서의 테스트

### /app/src/test

단위 테스트(JVM 실행)
로컬 JVM 기반 테스트

## Gradle

JVM 기반 언어의 빌드 툴.

다음과 같은 작업을 할 수 있음.

- 소스 코드를 컴파일해서 클래스 파일(.class)을 생성
  - java or kotlin 플러그인이 자동으로 컴파일
- 코딩 규약에 맞게 작성했는지 확인
  - checkstyle, ktlint, spotless 같은 플러그인 사용
- 정적 코드 분석
  - SonarQube, Detekt, PMD, ErrorProne 등과 연동
- 테스트 하고 테스트 결과나 커버리지 측정 결과를 리포트로 출력
  - JUnit, TestNG, Jacoco, Kover 등으로 리포트 생성
- javadoc 문서 작성
  - javadoc 태스크 자동 생성 (java 플러그인 포함 시)
- 클래스 파일과 리소스 파일을 패키징해서 압축 파일 만들기(.jar, .war)
  - jar, war 태스크로 빌드 아티팩트 생성
- 압축파일을 테스트 환경이나 스테이징 환경에 배포
  - scp, ssh, docker, kubernetes, Ansible 등과 연동 가능
- 압축 파일을 저장소에 등록
  - maven-publish, nexus-publish, artifactory 등 사용

특징

| 항목                               | 설명                                                                            |
| ---------------------------------- | ------------------------------------------------------------------------------- |
| **확장 가능한 DSL 제공**           | Groovy/Kotlin 기반 DSL로 사용자 정의 태스크, 플러그인 구성 가능                 |
| **빌드 분할·공통 컴포넌트 체계화** | `buildSrc/`, 플러그인 분리, 공통 빌드 설정 공유 가능                            |
| **IDE와 연계된 API 제공**          | IntelliJ/Android Studio에서 Gradle 모델 연동 API 존재 (Tooling API)             |
| **변경 내역 기반 빌드, 병렬 빌드** | Incremental Build, Configuration Cache, Parallel Execution 등 지원              |
| **멀티 프로젝트 지원**             | `settings.gradle.kts`, `include()` 등으로 하위 모듈 관리                        |
| **유연한 의존성 관리**             | `mavenCentral`, `google`, `file()`, `flatDir()` 등 지원                         |
| **Ant 통합 가능**                  | `ant.importBuild`, `ant.taskdef` 등으로 기존 Ant 프로젝트와 연동 가능           |
| **Gradle Wrapper 제공**            | `./gradlew`로 로컬에 Gradle 없어도 지정된 버전 자동 설치                        |
| **호환성 배려**                    | 다양한 Gradle/Java 버전 조합 및 하위 호환성 고려 (플러그인 제한은 있을 수 있음) |

### 장점

- (ant 나 maven 에 비해) 생산성이 높다
  - 규칙 기반 빌드 접근법(=규칙을 따라 프로젝트 구조를 만드는 방법)을 사용하기 때문에 빌드 스크립트 내용 줄일 수 있음
  - 빌드 스크립트에서 java, kotlin 유틸리티를 쉽게 사용할 수 있음

- 빌드 순서를 제어하기 쉽다
  - 변경 가능한 기본 빌드 순서를 제공하여 언제든 재정의 해서 바꿀 수 있음(Maven의 표준 빌드 순서 와 Ant 의ㅂ자유로운 빌드 순서의 중간 접근법)
  - "Task(빌드 순서의 각 단계)" 를 도입. 이 Task 의존관계에 따라 빌드 순서가 정해 진다.
    - Ant 의 문제였던 '빌드 스크립트의 복잡성' 은 플러그인을 사용해서 Task 의존 관계의 기본 구성을 할 수 있게 함
    - 이 의존관계는 어디까지나 기본 구성이므로 얼마든지 빌드 순서를 재정의해서 바꿀 수 있음

- 멀티 프로젝트 대응
  - 규모가 커지는 경우 한 프로젝트를 여러개의 서브 프로젝트로 나누는 경우가 생김. 이런 경우 서브 프로젝트 간 의존관계나 서브 프로젝트들의 공통 빌드 설정을 어떻게 효율적으로 관리하느냐 문제가 생김.
  - 다음 같은 기능으로 서브 프로젝트로 구성된 전체 프로젝트의 빌드를 지원
    - 멀티 프로젝트에 있는 서브 프로젝트를 정의하는 기능
    - 서브 프로젝트에 공통 빌드 스크립트를 집약하는 기능
    - 서브 프로젝트 간 의존관계를 정의하는 기능
    - 의존관계를 고려해서 변경 내역만 빌드하는 기능

- 컴포넌트로 만들기 쉽다
  - 빌드 스크립트에서 메서드나 클래스 추출
  - 빌드 스크립트의 분할과 재사용(apply from 이용)
  - 프로젝트에서만 사용할 수 있는 확장 모듈(buildSrc 프로젝트)
  - 여러 프로젝트에서 범용적으로 재사용할 수 있는 라이브러리

- 별도 설치할 필요 없음
  - gradle wrapper 제공하여, gradle project 안에 bootstrap 심어서 지정한 버전의 gradle 을 자동으로 설치해주는 기능 제공
    - gradlew 명령어 실행하면 gradle binary 다운되면서 빌드 실행됨

- 호환성 최대한 배려
  - 기존 기능을 갑자기 사용할 수 없게 되는 변경은 하지 않음
  - 기능을 제거해야 한다면 장래에 폐지될 가능성이 있음을 명시하고 단계적으로 제거
  - 신기능은 피드백을 충분히 받아서 안정화한 후에 추가

### ios 와 flutter build system 과 비교

공통점

| 기능                          | Gradle                        | Flutter (Dart)                 | iOS (Xcode)                            |
| ----------------------------- | ----------------------------- | ------------------------------ | -------------------------------------- |
| **의존성 관리**               | ✅ (Maven, Ivy, etc.)          | ✅ (`pubspec.yaml`)             | ✅ (CocoaPods, SwiftPM)                 |
| **스크립트 기반 빌드 구성**   | ✅ DSL 기반 (Groovy/Kotlin)    | ✅ Dart 기반 일부 CLI           | ✅ Xcode Build Settings + 스크립트      |
| **멀티 모듈 지원**            | ✅ `multi-project` 구조        | ✅ 패키지/모듈 나눌 수 있음     | ✅ Workspace, Project, Target 구조      |
| **캐시 및 Incremental Build** | ✅ 매우 강력함                 | ⚠️ 일부 캐시 있음 (비교적 단순) | ⚠️ 있음 (하지만 복잡하고 느릴 수 있음)  |
| **외부/로컬 저장소 지원**     | ✅ 다양하게 지원               | ✅ pub.dev + git + path 등      | ✅ CocoaPods/SwiftPM도 다양한 소스 지원 |
| **IDE 통합**                  | ✅ Android Studio, IntelliJ 등 | ✅ VSCode, Android Studio       | ✅ Xcode                                |

차이점

| 항목                            | Gradle                                           | Flutter                   | iOS (Xcode)                  |
| ------------------------------- | ------------------------------------------------ | ------------------------- | ---------------------------- |
| **DSL 확장성**                  | 매우 높음 (Groovy/Kotlin)                        | 낮음 (CLI에 가까움)       | 낮음 (Xcode 설정 UI 기반)    |
| **사용자 정의 태스크/플러그인** | 완전 가능                                        | 불편하거나 거의 없음      | 매우 제한적 (스킴/스텝 기반) |
| **멀티 플랫폼 대응성**          | ✅ JVM, Android, Kotlin Multiplatform 등          | ✅ Android + iOS 모두 대응 | ❌ iOS 전용                   |
| **병렬 빌드/캐시 효율화**       | 고성능 설정 가능 (`--parallel`, `--build-cache`) | 덜 최적화됨               | 자동 캐시 있지만 설정이 복잡 |
| **오픈 구조 유연성**            | 매우 높음                                        | 중간                      | 낮음 (Xcode 의존)            |

### 조각지식: Maven

ant 다음 세대, gradle 이전 세대 빌드 툴.
의존 라이브러리를 관리하기 위해 Maven Central Repository(mavenCenter) 제공.
Sonatype 에서 관리함.

### 조각지식: google()

Google 에서 관리하는 의존 라이브러리 관리 공간.
Google은 Android 생태계를 강화하면서, Android 관련 라이브러리(예: Jetpack, AndroidX, Play Services 등)를 빠르게 배포하기 위해 자체 Maven 저장소를 운영하게 됨.
Android 관련 라이브러리를 Maven Central에 올리기엔 승인 절차가 오래 걸림.
Android Studio + Gradle 환경에 최적화된 릴리스 속도와 배포 제어 필요.

### 조각지식: Groovy

JVM 기반의 동적 타입 언어이며, Java와 매우 밀접한 관계를 가진 스크립트 언어.

| 항목        | 설명                                                       |
| ----------- | ---------------------------------------------------------- |
| 플랫폼      | JVM 기반 (Java Virtual Machine)                            |
| 타입 시스템 | **동적 타입** (필요시 정적 타입도 가능)                    |
| 문법 특징   | Java와 거의 동일하지만 훨씬 간결                           |
| 주요 용도   | 스크립트 작성, 빌드 도구(Gradle), DSL, 테스트 코드, 자동화 |
| 처음 등장   | 2003년경 (James Strachan에 의해 시작)                      |
| 버전 관리   | Apache Software Foundation에서 관리 중                     |

어떤 맥락에서 나왔나?

> 📌 Java의 한계를 보완하기 위해

- 너무 장황한 문법 (Boilerplate)
- 동적 프로그래밍이 거의 불가능
- 스크립팅/자동화가 어려움
- Java로 간단한 작업하기엔 무거움

| 개선 포인트                       | 설명                                      |
| --------------------------------- | ----------------------------------------- |
| 타입 생략 가능                    | `def name = "groovy"` 처럼 동적 타입 가능 |
| 컬렉션 리터럴                     | `[]`, `[:]` 등 Python처럼 간단하게        |
| 클로저 지원                       | `list.each { println it }`                |
| 문자열 템플릿                     | `"Hello, ${name}"`                        |
| 빌드 스크립트에 최적화된 DSL 구조 | Gradle의 `task {}` 문법에 딱 맞음         |

Groovy는 동적 타입 기반이라 런타임 에러가 더 많을 수 있고, 정적 분석이 어려움.
성능도 Java에 비해 다소 느릴 수 있음.
이런 이유로 최근에는 Gradle에서도 Groovy DSL → Kotlin DSL로 전환하는 흐름이 강해짐.

### Kotlin DSL

Kotlin DSL은 Kotlin 언어를 기반으로 작성된 DSL(Domain-Specific Language).
즉, 빌드 스크립트를 Kotlin 문법으로 작성하는 방법. 스크립트 역할을 하는 kotlin 코드.

일반적인 Kotlin 애플리케이션은 main() 함수가 있고, JVM에서 실행됨.
Gradle의 Kotlin DSL은 Gradle이 실행할 때 스크립트처럼 해석되며, 특정 DSL 문법을 통해 Gradle의 API를 호출.
