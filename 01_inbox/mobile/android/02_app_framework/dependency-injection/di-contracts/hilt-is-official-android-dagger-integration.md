---
title: "Hilt는 Android용 공식 Dagger 통합 경로다"
tags: ["android", "android/app-framework"]
---

# Hilt는 Android용 공식 Dagger 통합 경로다

Hilt는 Android framework class가 OS에 의해 생성되는 문제를 Dagger graph와 연결하기 위한 공식 경로다. Hilt는 Android class별 component, scope, predefined binding, `@ApplicationContext`와 `@ActivityContext` 같은 qualifier를 제공한다.

그래서 Android 앱에서 Dagger 기반 DI를 새로 도입한다면 Hilt를 먼저 검토하는 것이 자연스럽다. 순수 Dagger가 틀렸다는 뜻은 아니지만, Android lifecycle과 framework entry point 연결을 직접 구성해야 하는 비용이 커진다.

공식 문서: [Dependency injection with Hilt](https://developer.android.com/training/dependency-injection/hilt-android), [Using Dagger in Android apps](https://developer.android.com/training/dependency-injection/dagger-android)

## 판단 기준

DI 노트는 객체를 어디서 만들고, 누가 소유하며, 어떤 lifetime 동안 재사용할지를 판단하는 기준으로 읽는다.

## 경계

framework 이름보다 graph boundary, scope, replacement seam, Android component lifetime을 먼저 확인한다.
