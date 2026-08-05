---
title: android-default-config-defines-identity-and-version-contracts
tags: ["android", "gradle", "defaultconfig"]
aliases: ["Android 기본 설정은 식별자와 버전 계약을 만든다"]
date created: 2026-07-31 17:52:17 +09:00
date modified: 2026-08-05 16:15:00 +09:00
created: 2026-07-31 17:52:17 +09:00
updated: 2026-08-05 16:15:00 +09:00
---

## Android 기본 설정은 식별자와 버전 계약을 만든다

상위 문서: [Gradle 빌드 계약](gradle-build-contracts.md)

### 개념 및 필요성 (What & Why)
`defaultConfig` 블록은 AGP 빌드 시스템에서 모든 빌드 변형(Build Variant)에 공통으로 적용되는 애플리케이션 식별자(Application ID), API 타깃 버전 레벨(`minSdk`, `targetSdk`), 및 앱 버저닝 명세(`versionCode`, `versionName`)를 정의하는 계약이다.
Google Play 스토어는 앱을 고유하게 식별하고 업데이트 상향 호환성(Upgrade Compatibility)을 판단하기 위해 `applicationId`와 단조 증가하는 `versionCode` 정수값을 필수 계약조건으로 요구한다.

### 내부 메커니즘 (Internal Mechanism)
1. **Application ID vs Namespace**: `namespace`는 생성되는 `R.java` 클래스 및 소스 패키지 구조를 지정하며, `applicationId`는 Play 스토어 및 OS 단에서 앱을 구별하는 고유 패키지 식별자이다.
2. **SDK 레벨 매핑**:
   - `minSdk`: 이 앱이 실행 가능한 최소 Android OS 버전 (이보다 낮으면 앱 설치 거부).
   - `targetSdk`: 앱이 테스트되고 보장하는 OS 호환성 동작 기준점 (신규 런타임 권한 및 프레임워크 동작 변경 적용 기준).
3. **버전 계약 규칙**:
   - `versionCode`: 내부적 업그레이드 판별용 단조 증가 정수 (예: `100200`). 버전 업데이트 시 기존 버전보다 항상 커야 한다.
   - `versionName`: 사용자 표기용 버전 문자열 (예: `"1.2.0"`).
4. **Manifest Injection**: `defaultConfig`에 선언된 값들은 AGP 빌드 시 `AndroidManifest.xml`의 `<manifest package="...">`, `android:versionCode`, `android:versionName` 속성에 주입된다.

```mermaid
flowchart TD
    DefaultConfig["defaultConfig { applicationId, versionCode, minSdk }"] --> AGPMerger["AGP Manifest Merger"]
    AGPMerger --> FinalManifest["Final Merged AndroidManifest.xml"]
    FinalManifest --> OSValidator["Android OS / Google Play Verifier"]
    OSValidator -->|versionCode > currentVersionCode| UpgradeSuccess["App Upgrade Allowed"]
    OSValidator -->|versionCode <= currentVersionCode| UpgradeReject["App Upgrade Rejected"]
```

### 코드 예시 (build.gradle.kts)
```kotlin
// app/build.gradle.kts
android {
    namespace = "com.example.myapp"
    compileSdk = 34

    defaultConfig {
        applicationId = "com.example.myapp"
        minSdk = 26
        targetSdk = 34
        versionCode = 10001
        versionName = "1.0.1"

        testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"
    }
}
```

### 관측 가능 증거 (Observable Evidence)
빌드 산출물의 최종 매니페스트에 정의된 식별자와 버전 정보를 `apkanalyzer` 도구로 확인할 수 있다:
```bash
apkanalyzer manifest print build/outputs/apk/release/app-release.apk | grep -E "package|versionCode|versionName"

# Output Example:
# package="com.example.myapp"
# android:versionCode="10001"
# android:versionName="1.0.1"
```

관련 노트: [App 업데이트는 application id, version code, 그리고 서명 호환성을 요구한다](../../distribution/release-distribution-contracts/app-updates-require-application-id-version-code-and-signature-compatibility.md), [Gradle 빌드 계약](gradle-build-contracts.md)
