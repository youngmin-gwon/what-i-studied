---
title: agp-dsl-checklist-verifies-effective-release-variant-values
tags: ["android", "android/packaging-deployment"]
aliases: []
date modified: 2026-08-03 18:12:31 +09:00
date created: 2026-07-31 17:52:17 +09:00
---

## AGP DSL 체크리스트는 릴리스 변형의 실제 값을 확인한다

상위 문서: [Android 패키징과 배포 지도](01_inbox/mobile/android/03_packaging_deployment/android-packaging-deployment.md)

관련 지도: [Gradle 빌드 계약](01_inbox/mobile/android/03_packaging_deployment/build/gradle/gradle-build-contracts/gradle-build-contracts.md)

관련 노트: [Android 기본 설정은 식별자와 버전 계약을 만든다](01_inbox/mobile/android/03_packaging_deployment/build/gradle/gradle-build-contracts/android-default-config-defines-identity-and-version-contracts.md), [Signing config는 로컬 서명과 Play 배포 정체성을 연결한다](01_inbox/mobile/android/03_packaging_deployment/build/gradle/gradle-build-contracts/signing-config-connects-local-signing-and-play-release-identity.md)

### DSL 를 읽는 순서

1. `plugins` 에서 모듈 유형과 적용 플러그인을 확인한다.
2. `android` 의 `namespace`, SDK, `defaultConfig` 를 확인한다.
3. `buildTypes` 와 `productFlavors` 에서 변형 축을 확인한다.
4. `sourceSets` 와 디렉터리에서 코드·리소스 입력을 확인한다.
5. `signingConfigs` 와 배포 관련 속성을 확인한다.
6. `dependencies` 와 variant 별 의존성으로 최종 입력을 확인한다.

### 자주 쓰는 DSL 영역

| 블록 | 핵심 책임 |
| --- | --- |
| `plugins` | AGP 와 언어·도구 플러그인 적용 |
| `android` | Android 빌드 모델 전체 구성 |
| `defaultConfig` | 모든 변형의 기본값 |
| `buildTypes` | debug/release 및 단계별 패키징 |
| `productFlavors` | 제품·환경 차이와 dimension |
| `sourceSets` | 입력 디렉터리 경로 조정 |
| `signingConfigs` | APK/AAB 서명 자격 증명 |
| `dependencies` | 외부 라이브러리와 모듈 입력 |

### 설정과 실행의 구분

DSL 은 빌드 모델을 구성하고, Gradle 태스크 실행은 그 모델로 산출물을 만든다.

스크립트 안에서 임의 파일을 읽거나 외부 명령을 실행하는 방식은 재현성과 보안에 영향을 줄 수 있다.

가능하면 AGP 가 제공하는 typed property 와 Gradle Provider API 를 사용해 지연 평가한다.

### 최소 릴리스 점검

- 선택한 variant 가 release 목적에 맞는가?
- `applicationId`, `versionCode`, `versionName` 이 예상대로 병합되는가?
- source set 의 manifest·리소스·코드가 예상 파일을 포함하는가?
- release signing config 가 올바른 키를 가리키는가?
- AAB/APK 산출물이 CI 에서도 동일하게 생성되는가?
- 비밀 값과 로컬 경로가 저장소와 로그에 들어가지 않는가?

### 중복을 피할 주제

R8 의 규칙, 코드·리소스 축소, mapping 검증은 R8 정본에서 다룬다.

configuration cache, 증분 빌드, build scan, 태스크 병목 분석은 Gradle 성능 정본에서 다룬다.

이 문서에서는 해당 주제를 재설명하지 않고 릴리스 점검의 연결 후보로만 남긴다.

빌드 속도 공식 연결 후보: https://developer.android.com/build/optimize-your-build

### 참고

빌드 구성 공식 문서: https://developer.android.com/build

변형과 source set: https://developer.android.com/build/build-variants

AGP DSL API: https://developer.android.com/reference/tools/gradle-api
