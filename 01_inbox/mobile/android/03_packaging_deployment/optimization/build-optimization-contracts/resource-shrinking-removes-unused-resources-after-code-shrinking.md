---
title: "리소스 수축은 코드 수축 후 미사용 리소스를 제거한다"
tags: ["android", "android/packaging-deployment"]
---

# 리소스 수축은 코드 수축 후 미사용 리소스를 제거한다

상위 문서: [Android 성능, 품질, 빌드 최적화 지도](01_inbox/mobile/android/06_testing_performance/performance/android-performance-quality-and-build-optimization.md)
관련 지도: [R8와 Gradle 빌드 최적화 계약](01_inbox/mobile/android/03_packaging_deployment/optimization/build-optimization-contracts/build-optimization-contracts.md)
관련 노트: [R8은 릴리즈 코드의 수축, 최적화, 난독화를 수행한다](01_inbox/mobile/android/03_packaging_deployment/optimization/build-optimization-contracts/r8-shrinks-optimizes-and-obfuscates-release-builds.md), [R8 결과물은 크기와 런타임 회귀로 검증한다](01_inbox/mobile/android/03_packaging_deployment/optimization/build-optimization-contracts/r8-output-must-be-validated-with-size-and-runtime-regression.md)

## 핵심 주장

리소스 수축은 코드 수축과 별도로 리소스 사용 여부를 판단한다.

정적 참조만 분석하면 동적으로 구성한 이름을 사용하지 않는 리소스로 오판할 수 있다.

따라서 `isShrinkResources = true`를 켜는 일은 동적 리소스 접근 목록을 정리하는 일과 함께 진행해야 한다.

## 수축 대상

- drawable, mipmap, layout, string, color 등 APK에 포함되는 리소스
- flavor와 density별 중복 리소스
- 코드에서 참조되지 않는 리소스
- 다른 리소스에서 더 이상 연결되지 않는 리소스

AAB의 전달 분할은 기기 구성에 맞는 다운로드 크기를 다시 바꿀 수 있다.

APK 크기와 사용자가 실제 다운로드하는 크기를 같은 지표로 취급하지 않는다.

## 동적 접근의 위험

다음과 같은 코드는 정적 분석만으로 이름을 확정하기 어렵다.

```kotlin
val id = resources.getIdentifier("icon_$name", "drawable", packageName)
```

이 경우 실제 이름 패턴을 keep 파일로 보존하거나, 가능하면 정적 매핑으로 바꾼다.

```xml
<resources xmlns:tools="http://schemas.android.com/tools"
    tools:keep="@drawable/icon_*"
    tools:discard="@drawable/unused_banner"
    tools:shrinkMode="strict" />
```

Precise 또는 strict 방식은 보존 대상을 명시적으로 관리할 때 유용하다.

그러나 넓은 패턴은 다시 수축 효과를 약화하므로 실제 이름 집합을 좁혀야 한다.

## 검증 절차

1. 수축 전후의 APK Analyzer 리소스 목록을 비교한다.
2. 앱 시작, 이미지 로딩, 딥링크, 알림, 위젯을 확인한다.
3. flavor, locale, density별 대표 기기에서 확인한다.
4. 동적 리소스 이름을 사용하는 테스트를 릴리즈 variant로 실행한다.
5. 삭제된 리소스와 보존 이유를 변경 기록에 남긴다.

리소스 수축 오류는 대개 설치보다 특정 사용자 흐름에서 늦게 드러난다.

참고: [Shrink, obfuscate, and optimize your app](https://developer.android.com/studio/build/shrink-code)

참고: [Manage app size](https://developer.android.com/topic/performance/reduce-apk-size)
