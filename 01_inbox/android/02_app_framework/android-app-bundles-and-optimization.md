---
title: android-app-bundles-and-optimization
tags: [android, android/app-bundle, android/dynamic-delivery, android/instant-apps]
aliases: [AAB, App Bundle, Dynamic Delivery, Play Feature Delivery, Asset Delivery]
date modified: 2026-04-04 00:28:00 +09:00
date created: 2026-04-04 00:28:00 +09:00
---

## Android App Bundles & Distribution Optimization

사용자에게 가장 가벼운 앱을 전달하는 것은 설치 전환율과 유지율에 직결된다. 안드로이드의 최신 배포 표준은 **Android App Bundle (.aab)**이며, 이를 통해 각 기기에 최적화된 APK를 생성한다.

> [!NOTE] **iOS 비교: App Thinning vs Android App Bundle**
> - **iOS**: `App Thinning` (Slicing, ODR) 작업을 통해 각 디바이스 모델에 맞는 바이너리만 전달하도록 자동화되어 있다. Xcode 빌드와 App Store가 이를 전담한다.
> - **Android**: 개발자가 `Android App Bundle` 형식을 사용해야 하며, 구글 플레이가 이를 기반으로 **Split APK**를 생성한다. 추가로 `Dynamic Feature Modules`를 사용하여 특정 기능을 나중에 다운로드하도록 직접 설계할 수 있다.
> 자세한 내용은 [apple-distribution-and-policies](../../apple/05_security_privacy/apple-distribution-and-policies.md)를 참고하세요.

### 1. Android App Bundle (.aab)

구글 플레이에 제출하는 단일 아티팩트이지만, 내부적으로는 모든 리소스가 포함된 메타 구조체이다. 구글 플레이는 이를 분석하여 언어별, 이미지 해상도별, CPU 아키텍처별로 **Split APK**를 생성해 각 사용자에게 배포한다.

**장점:**
- 바이너리 용량 감소 (평균 20~30%)
- Unused Code 제거 (Proguard/R8 연계)
- 보안 강화 (Play App Signing 필수)

### 2. Play Feature Delivery (Dynamic Features)

앱의 특정 기능을 설치 시점이 아닌, 필요할 때(On-demand) 다운로드하도록 구성할 수 있다.

#### 구조 및 호출

```kotlin
// build.gradle.kts (feature module)
plugins {
    id("com.android.dynamic-feature")
}

// 코드에서 동적 모듈 다운로드
val splitInstallManager = SplitInstallManagerFactory.create(context)
val request = SplitInstallRequest.newBuilder()
    .addModule("premium_camera_filter")
    .build()

splitInstallManager.startInstall(request)
    .addOnSuccessListener { /* 모듈 로드 완료 */ }
```

### 3. Play Asset Delivery (대용량 리소스)

게임이나 리소스가 많은 앱에서 리버리(Delivery)를 관리한다.
- **Install-time**: 설치 시 함께 다운로드 (200MB 제한)
- **Fast-follow**: 설치 직후 자동 다운로드 (512MB 제한)
- **On-demand**: 앱의 요청 시점에 다운로드

---

### ⚠️ Instant Apps: The Sunset and Beyond (2025-2026)

> [!CAUTION] **Devil's Advocate : Instant Apps 대신 딥링크를 고도화하라**
> 구글은 2025년 12월부터 **Instant Apps** 서비스를 종료할 예정이다. 이제 더 이상 별도의 인스턴트 모듈을 개발하는 데 리소스를 낭비하지 마라.
> 대신, **앱 번들 최적화**와 **매끄러운 딥링크(App Links)**를 통해 사용자가 클릭 한 번으로 앱을 설치하고 즉시 원하는 화면으로 진입할 수 있도록 사용자 여정을 설계하는 것이 정석이다.

### 더 보기
- [android-gradle-build-system](android-gradle-build-system.md)
- [android-deep-links](android-deep-links.md)
- [android-performance-and-debug](../06_testing_performance/android-performance-and-debug.md)
