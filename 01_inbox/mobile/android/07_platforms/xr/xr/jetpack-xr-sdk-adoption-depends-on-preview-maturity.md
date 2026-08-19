---
title: jetpack-xr-sdk-adoption-depends-on-preview-maturity
tags: ["android", "android/platforms"]
aliases: []
date modified: 2026-08-04 15:35:00 +09:00
date created: 2026-07-31 18:06:11 +09:00
---

## Jetpack XR SDK 는 preview 성숙도를 전제로 채택해야 한다

상위 문서: [Android XR 계약](./xr.md)

Jetpack XR SDK 는 Android XR 개발을 위한 공식 Jetpack 계층이지만 하나의 안정성 단계로 출시되지 않는다. 제품 적용 여부는 라이브러리별 alpha/beta 상태, 기능별 experimental 표기, 지원 기기, 알려진 이슈, 배포 채널을 확인한 뒤 결정해야 한다.

### Gradle 모듈성 및 라이브러리 격리 선언

```kotlin
// build.gradle.kts (feature:xr-spatial module)
dependencies {
    // Jetpack XR Core Runtime
    implementation("androidx.xr.runtime:runtime:1.0.0-beta01")
    // Jetpack XR Compose
    implementation("androidx.xr.compose:compose:1.0.0-alpha16")
    // Jetpack XR SceneCore (3D Entities)
    implementation("androidx.xr.scenecore:scenecore:1.0.0-beta01")
}
```

### 라이브러리 성숙도 상태 매트릭스 (2026 기준)

| Library Module | Maturity Level | Core Focus | Feature Flag Isolation Strategy |
| :--- | :--- | :--- | :--- |
| `androidx.xr.runtime` | Beta (`1.0.0-beta01`) | Session Management, Spatial Capabilities | Required for basic XR detection |
| `androidx.xr.scenecore` | Beta (`1.0.0-beta01`) | 3D Gltf Entities, Spatial Audio, Anchors | Wrap behind SceneGraphManager interface |
| `androidx.xr.compose` | Alpha (`1.0.0-alpha16`) | Subspace, SpatialPanel, Orbiter UI | Isolated in feature module, fallback to 2D |

### 실무 규칙

- Compose for XR, SceneCore, ARCore for Jetpack XR, XR Runtime 의 release notes 를 각각 확인한다.
- alpha 와 experimental API 이름과 동작은 바뀔 수 있으므로 앱 핵심 구조에 직접 퍼뜨리지 않는다. beta 도 stable 호환성을 뜻하지 않는다.
- XR 전용 코드는 일반 Android UI 와 경계를 두고 feature flag 또는 별도 module 로 격리한다.
- 공식 sample 과 codelab 기준으로 현재 가능한 surface 를 먼저 검증한다.
- 기기명이나 출시 상태는 문서화 시점 기준 정보로 적고 주기적으로 갱신한다.

### 관측 가능한 증거 (Observable Evidence)

```bash
# 앱 프로세스 인스턴스화 시 XR 런타임 클래스 로딩 모니터링
adb logcat -v threadtime | grep -E "androidx.xr.runtime|androidx.xr.scenecore"

# XR 런타임 패키지 메타데이터 검증
adb shell pm dump <package_name> | grep -i "xr"
```

### 관련 문서

- [Android 패키징과 배포 지도](../../../03_packaging_deployment/android-packaging-deployment.md)
- [Compose for XR은 기존 Compose를 subspace와 spatial component로 확장한다](./compose-for-xr-extends-compose-with-subspace-and-spatial-components.md)

공식 문서: [Develop with the Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk), [XR Compose releases](https://developer.android.com/jetpack/androidx/releases/xr-compose), [XR Runtime releases](https://developer.android.com/jetpack/androidx/releases/xr-runtime), [XR SceneCore releases](https://developer.android.com/jetpack/androidx/releases/xr-scenecore)

검증일: 2026-08-03. XR Compose 는 `1.0.0-alpha16`, XR Runtime 과 XR SceneCore 는 `1.0.0-beta01` 이며 모두 2026-07-15 release note 기준이다. 버전 자체보다 stable/RC/beta/alpha 열과 개별 API 의 experimental 표기를 출시 직전에 다시 확인한다.

