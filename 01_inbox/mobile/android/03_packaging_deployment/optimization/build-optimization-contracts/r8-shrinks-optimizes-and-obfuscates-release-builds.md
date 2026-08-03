---
title: r8-shrinks-optimizes-and-obfuscates-release-builds
tags: ["android", "android/packaging-deployment"]
aliases: []
date modified: 2026-08-03 18:13:01 +09:00
date created: 2026-07-31 17:32:53 +09:00
---

## R8 은 릴리즈 코드의 수축, 최적화, 난독화를 수행한다

상위 문서: [Android 성능, 품질, 빌드 최적화 지도](01_inbox/mobile/android/06_testing_performance/performance/android-performance-quality-and-build-optimization.md)

관련 지도: [R8와 Gradle 빌드 최적화 계약](01_inbox/mobile/android/03_packaging_deployment/optimization/build-optimization-contracts/build-optimization-contracts.md)

관련 노트: [R8 keep 규칙은 최적화 경계다](01_inbox/mobile/android/03_packaging_deployment/optimization/build-optimization-contracts/keep-rules-are-optimization-boundaries.md), [리소스 수축은 코드 수축 후 미사용 리소스를 제거한다](01_inbox/mobile/android/03_packaging_deployment/optimization/build-optimization-contracts/resource-shrinking-removes-unused-resources-after-code-shrinking.md)

### 핵심 주장

R8 은 릴리즈 빌드에서 코드 크기와 실행 효율을 함께 다루는 컴파일러다.

코드 수축, 최적화, 난독화는 서로 다른 효과를 내므로 한 기능으로 뭉뚱그리면 안 된다.

`isMinifyEnabled = true` 는 일반적으로 세 기능이 동작할 수 있는 진입점이다.

리소스 수축은 코드 수축과 별개의 입력과 분석을 사용한다.

따라서 APK/AAB 크기 감소를 검증할 때 DEX 와 리소스를 따로 측정해야 한다.

### 기능별 역할

- 코드 수축은 정적 분석으로 도달 불가능한 클래스, 메서드, 필드를 제거한다.
- 최적화는 인라이닝, 클래스 계층 단순화, 상수 전파 등으로 바이트코드 형태를 바꾼다.
- 난독화는 클래스, 메서드, 필드 이름을 짧게 바꾸어 크기를 줄이고 분석 비용을 높인다.
- 리소스 수축은 코드와 리소스 참조를 분석하여 사용되지 않는 리소스를 제거한다.
- Kotlin metadata 처리는 리플렉션과 직렬화 계약을 깨지 않도록 별도 검증이 필요하다.

### 권장 릴리즈 설정

```kotlin
buildTypes {
    release {
        isMinifyEnabled = true
        isShrinkResources = true
        proguardFiles(
            getDefaultProguardFile("proguard-android-optimize.txt"),
            "proguard-rules.pro"
        )
    }
}
```

`proguard-android-optimize.txt` 는 최적화가 포함된 기본 설정이다.

디버그 빌드에 같은 수축을 적용하면 반복 개발 속도와 오류 분석성이 나빠질 수 있다.

대신 실제 배포와 가까운 별도 성능 검증 variant 를 둘 수 있다.

### 판단 순서

1. 릴리즈 variant 에서 수축을 켠다.
2. 리플렉션, JNI, 동적 클래스 로딩 경계를 식별한다.
3. 필요한 경계만 keep 규칙으로 보존한다.
4. mapping 과 결과 리포트를 보관한다.
5. 설치, 시작, 핵심 사용자 여정을 실제 기기에서 검증한다.

R8 설정 변경은 단순한 용량 최적화가 아니라 실행 계약 변경이다.

참고: [Shrink, obfuscate, and optimize your app](https://developer.android.com/studio/build/shrink-code)

참고: [R8 Configuration Analyzer](https://developer.android.com/topic/performance/app-optimization/r8-configuration-analyzer)
