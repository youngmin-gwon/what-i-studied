# [[mobile-security]] > [[android-app-bundles-and-optimization]]

## App Bundles: Distribution Optimization

사용자에게 가장 가벼운 앱을 전달하는 **Android App Bundle (.aab)**과 동적 기능 배포를 위한 **Dynamic Delivery** 시스템을 분석합니다. 

단순히 바이너리 용량을 줄이는 것을 넘어, 각 기기에 최적화된 APK를 생성하고 리소스 사용을 극대화하여 설치 전환율과 앱 유지율을 높이는 것이 목표입니다.

---

### 💡 Context: 효율적인 배포의 가치

현대의 모바일 사용자는 무거운 앱을 선호하지 않습니다. 안드로이드의 최신 배포 표준인 App Bundle은 구글 플레이가 직접 Split APK를 생성하게 함으로써 기기별 맞춤형 설치를 가능케 합니다. [[android-gradle-build-system]]과 연계된 최적화의 정점입니다.

> [!NOTE] **상호 참조**
> iOS의 App Thinning 및 배포 방식은 [[apple-distribution-and-policies]]를 참고하세요.

---

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

### See Also

- [[android-gradle-build-system]]
- [[android-deep-links]]
- [[android-performance-and-debug]]
