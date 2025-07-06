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
        - 액티비티 클래스 경로입니다. `.`으로 시작하면 기본 패키지 기준으로 com.example.yourapp.MainActivity가 됩니다.

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

- `/drawble` : 벡터나 비트맵 이미지
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
