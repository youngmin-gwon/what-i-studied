# Android Gradle Plugin은 Android 빌드 규칙을 Gradle에 추가한다

상위 문서: [Android 패키징과 배포 지도](01_inbox/mobile/android/03_packaging_deployment/android-packaging-deployment.md)
관련 지도: [Gradle 빌드 계약](01_inbox/mobile/android/03_packaging_deployment/build/gradle/gradle-build-contracts/gradle-build-contracts.md)
관련 노트: [Gradle 프로젝트와 모듈 DSL은 서로 다른 책임을 가진다](01_inbox/mobile/android/03_packaging_deployment/build/gradle/gradle-build-contracts/gradle-project-and-module-dsl-have-different-responsibilities.md), [Build type, product flavor, build variant는 서로 다른 축이다](01_inbox/mobile/android/03_packaging_deployment/build/gradle/gradle-build-contracts/build-type-product-flavor-and-build-variant-are-different-axes.md)

## 한 문장 정리

Android Gradle Plugin(AGP)은 Gradle에 Android 앱과 라이브러리용 규칙, DSL, 태스크를 추가한다.
Gradle은 입력과 출력을 가진 태스크를 연결해 소스와 리소스를 APK 또는 AAB로 변환한다.

## 전체 흐름

1. `settings.gradle.kts`가 빌드에 포함할 모듈과 저장소를 정의한다.
2. 루트 `build.gradle.kts`가 플러그인 버전과 공통 플러그인 선언을 관리한다.
3. 모듈 스크립트가 Android 플러그인을 적용하고 `android {}` DSL을 구성한다.
4. AGP가 소스 세트, 변형, 리소스 병합, 컴파일, 패키징 태스크를 등록한다.
5. 선택한 변형의 태스크 그래프가 실행되어 APK 또는 AAB를 생성한다.

## Gradle과 AGP의 경계

Gradle 자체는 범용 빌드 오케스트레이터다. 언어 컴파일이나 Android 패키징의 의미를 스스로 알지는 않는다.
AGP가 `com.android.application` 또는 `com.android.library` 플러그인으로 Android 규칙을 제공한다.
따라서 `android {}`는 Gradle의 일반 문법이 아니라 AGP가 노출한 Kotlin DSL 영역이다.

## 프로젝트의 주요 파일

| 위치 | 책임 |
| --- | --- |
| `settings.gradle.kts` | 모듈 포함, 플러그인/의존성 저장소, 프로젝트 이름 |
| 루트 `build.gradle.kts` | 플러그인 버전 선언과 공통 적용 정책 |
| 모듈 `build.gradle.kts` | Android 컴파일, 변형, 소스 세트, 패키징 |
| `gradle/libs.versions.toml` | 라이브러리와 플러그인 버전의 이름 있는 카탈로그 |
| `gradle.properties` | Gradle 및 프로젝트 속성 |

## 결과물의 의미

앱 모듈은 설치·배포 가능한 APK 또는 Play 배포용 AAB를 만든다.
라이브러리 모듈은 다른 모듈이 소비하는 AAR과 메타데이터를 만든다.
같은 소스라도 build type과 product flavor 조합이 달라지면 별개의 build variant가 된다.

## 구성 원칙

- 공통 기본값은 `defaultConfig`와 공통 소스 세트에 둔다.
- 환경이나 제품 차이는 product flavor로 표현한다.
- 디버깅·릴리스·패키징 차이는 build type으로 표현한다.
- 결과물마다 바뀌는 값은 variant 조합의 우선순위를 확인한다.
- 비밀 값은 스크립트에 직접 기록하지 않고 CI 비밀 저장소나 로컬 보호 파일을 사용한다.

## 참고

공식 개요: https://developer.android.com/build/gradle-build-overview
빌드 구성 안내: https://developer.android.com/build
AGP 소개: https://developer.android.com/build/releases/about-agp
