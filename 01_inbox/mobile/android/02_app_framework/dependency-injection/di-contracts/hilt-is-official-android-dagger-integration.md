---
title: hilt-is-official-android-dagger-integration
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-03 16:59:23 +09:00
---

## Hilt 는 Android 용 공식 Dagger 통합 경로다

**Hilt**(**Dagger**(컴파일 타임에 의존성 그래프를 정적으로 검증하고 코드 생성을 수행하는 Java/Kotlin용 DI 엔진)를 안드로이드 컴포넌트 생명주기에 맞춰 의존성 그래프 생성을 자동화하는 구글의 공식 DI 라이브러리) 는 Android framework class 가 OS 에 의해 생성되는 문제를 Dagger graph 와 연결하기 위한 공식 경로다. Hilt 는 Android class 별 component, scope, predefined binding, `@ApplicationContext` 와 `@ActivityContext` 같은 qualifier 를 제공한다.

그래서 Android 앱에서 Dagger 기반 DI 를 새로 도입한다면 Hilt 를 먼저 검토하는 것이 자연스럽다. 순수 Dagger 가 틀렸다는 뜻은 아니지만, Android lifecycle 과 framework entry point 연결을 직접 구성해야 하는 비용이 커진다.

공식 문서: [Dependency injection with Hilt](https://developer.android.com/training/dependency-injection/hilt-android), [Using Dagger in Android apps](https://developer.android.com/training/dependency-injection/dagger-android)

### 판단 기준

DI 노트는 객체를 어디서 만들고, 누가 소유하며, 어떤 lifetime 동안 재사용할지를 판단하는 기준으로 읽는다.

### 경계

framework 이름보다 graph boundary, scope, replacement seam, Android component lifetime 을 먼저 확인한다.
