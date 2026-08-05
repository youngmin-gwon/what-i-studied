---
title: dynamic-feature-module-is-optional-feature-unit-dependent-on-base.md
tags: ["android", "agp", "dfm", "dynamic-feature"]
aliases: ["Dynamic feature module은 base에 의존하는 선택적 기능 단위다"]
date created: 2026-07-31 17:52:17 +09:00
date modified: 2026-08-05 16:15:00 +09:00
created: 2026-07-31 17:52:17 +09:00
updated: 2026-08-05 16:15:00 +09:00
---

## Dynamic feature module은 base에 의존하는 선택적 기능 단위다

상위 문서: [Play Delivery 계약](play-delivery-contracts.md)

### 개념 및 필요성 (What & Why)
**Dynamic Feature Module(동적 기능 모듈 - DFM)** 은 Android Gradle 빌드 시스템에서 `com.android.dynamic-feature` 플러그인을 사용하여 독립적으로 분리된 소스 코드 및 리소스 단위이다.
일반적인 멀티 모듈 구조에서는 앱 모듈(`:app`)이 라이브러리 모듈(`:feature:home`)을 의존성으로 참조하지만, **DFM 구조에서는 반대로 DFM이 기본 모듈(`:app` Base Module)을 의존성으로 참조하는 역의존성(Reverse Dependency)** 구조를 가진다.
이를 통해 Base 모듈의 크기를 최소화하고, 선택적인 대형 기능(예: AR 카메라, 카메라 스캐너, 특정 유료 결제 모듈)을 필요 시점에만 동적으로 다운로드받을 수 있게 만든다.

### 내부 메커니즘 (Internal Mechanism)
1. **Reverse Dependency (역의존성)**:
   - `:app` 모듈 `build.gradle.kts`: `dynamicFeatures = setOf(":features:ar_camera")`
   - `:features:ar_camera` 모듈 `build.gradle.kts`: `implementation(project(":app"))`
2. **Split Manifest Merging**: DFM의 `AndroidManifest.xml`은 Base 모듈 매니페스트와 합성되며 `<dist:module>` 태스크를 통해 동적 설치 조건(`dist:on-demand="true"`)을 선언한다.
3. **SplitCompat 연동**: 런타임에 DFM이 다운로드되어 설치되면, `SplitCompat.install(context)`를 호출하여 DFM 내의 클래스 및 리소스를 현재 애플리케이션의 ClassLoader 및 Resources 체인에 즉시 동적 로딩한다.

```mermaid
flowchart TD
    subgraph GradleDependency ["Reverse Dependency Structure"]
        AppBase[":app (Base Module)"] -->|dynamicFeatures += :feature_ar| DFMModule[":feature_ar (Dynamic Feature Module)"]
        DFMModule -->|implementation project(:app)| AppBase
    end

    subgraph RuntimeInstall ["Runtime Dynamic Loading"]
        DFMModule --> PlayStore["Google Play Download Engine"]
        PlayStore --> SplitCompat["SplitCompat.install(Context)"]
        SplitCompat --> DynamicClass["Dynamic Class Loading & Screen Launch"]
    end
```

### 코드 예시 (build.gradle.kts & Manifest)
```kotlin
// app/build.gradle.kts (Base 모듈 설정)
plugins {
    id("com.android.application")
}

android {
    dynamicFeatures += setOf(":features:ar_camera")
}
```

```xml
<!-- features/ar_camera/src/main/AndroidManifest.xml -->
<manifest xmlns:dist="http://schemas.android.com/play/delivery">
    <dist:module
        dist:instant="false"
        dist:title="@string/title_ar_camera">
        <dist:delivery>
            <dist:on-demand />
        </dist:delivery>
        <dist:fusing dist:include="true" />
    </dist:module>
</manifest>
```

### 관측 가능 증거 (Observable Evidence)
DFM 모듈이 올바르게 통합되었는지 `bundletool` 분석 명령으로 관측할 수 있다:
```bash
bundletool validate --bundle=app-release.aab
```

관련 노트: [Play feature delivery는 동적 기능 설치 시점을 제어한다](play-feature-delivery-controls-dynamic-feature-install-timing.md), [Play Delivery 계약](play-delivery-contracts.md)
