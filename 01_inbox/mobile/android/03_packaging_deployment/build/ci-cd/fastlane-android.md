---
title: fastlane-android
tags: ["android", "fastlane", "packaging-deployment", "ci-cd"]
aliases: ["Fastlane Android", "Fastlane Android 연동", "Fastlane Android Actions"]
date created: 2026-08-19 10:50:00 +09:00
date modified: 2026-08-19 10:50:00 +09:00
---

## Fastlane Android 플랫폼 연동

### 개요

본 문서는 범용 릴리스 오케스트레이션 엔진인 **Fastlane**을 Android 플랫폼 파이프라인에 적용할 때 필요한 **Android 전용 설정(`Appfile`), 표준 Action API 및 사용 패턴**을 다룬다.

---

### Android `Appfile` 구성 계약

Android 플랫폼에서 `Appfile`은 패키지명과 Google Play Console 인증용 서비스 계정 JSON 키 경로를 정의한다.

```ruby
# fastlane/Appfile
json_key_file(ENV["GCP_SERVICE_ACCOUNT_JSON_PATH"] || "config/google-service-account.json")
package_name("com.example.app")
```

---

### Android 전용 핵심 Action API

Fastlane 은 Android 빌드 디스패치 및 스토어 배포를 위해 검증된 내장 Action 들을 제공한다.

#### 1. `gradle(...)` Action
시스템 쉘을 통해 Android Gradle wrapper (`./gradlew`) 명령을 디스패치한다.

```ruby
gradle(
  task: "bundle",
  build_type: "Release",
  flavor: "Prod",
  properties: {
    "android.injected.version.code" => "105",
    "android.injected.version.name" => "1.5.0"
  },
  flags: "--no-daemon --stacktrace"
)
```

#### 2. `upload_to_play_store(...)` (`supply`) Action
Google Play Developer API v3를 통해 AAB/APK 아티팩트, 트랙 설정, 릴리스 노트(Changelog), 스크린샷 메타데이터를 자동 등록한다.

```ruby
upload_to_play_store(
  track: "internal", # internal, alpha, beta, production
  aab: "app/build/outputs/bundle/prodRelease/app-prod-release.aab",
  skip_upload_images: true,
  skip_upload_screenshots: true
)
```

#### 3. `firebase_app_distribution(...)` Action
테스터 및 내부 QA 그룹에 테스트용 APK/AAB 배포물을 전달한다.

```ruby
firebase_app_distribution(
  app: ENV["FIREBASE_APP_ID"],
  release_notes: "QA 테스트 빌드입니다.",
  groups: "internal-testers"
)
```

#### 4. Android `SharedValues` 참조
`gradle(...)` 실행 후 생성된 아티팩트 경로를 `lane_context`에서 직접 수집할 수 있다.

```ruby
aab_path = Actions.lane_context[SharedValues::GRADLE_AAB_OUTPUT_PATH]
```

---

### 상위 및 연관 문서

- [Fastlane 코어 엔진](fastlane.md)
- [Gradle 과 Fastlane CI/CD 파이프라인](gradle-fastlane-pipeline.md)
- [Android CI/CD](ci-cd.md)
