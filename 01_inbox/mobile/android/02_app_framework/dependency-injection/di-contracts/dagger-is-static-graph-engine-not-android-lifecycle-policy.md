---
title: dagger-is-static-graph-engine-not-android-lifecycle-policy
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-06 15:05:00 +09:00
date created: 2026-08-03 16:28:45 +09:00
---

## Dagger 는 정적 graph 엔진이지 Android lifecycle 정책 자체가 아니다
배경 지식: [의존성 역전 원칙](../../../../../../02_references/oop/solid/DIP%28Dependency%20Inversion%20Principle%29.md), [독립 수명 모델](../../../00_foundations/learning-spine/05-independent-lifetimes-of-screen-process-task-and-state.md)

**Dagger**(컴파일 타임에 의존성 그래프를 정적으로 검증하고 코드 생성을 수행하는 Java/Kotlin용 DI 엔진) 는 compile time 에 dependency graph 를 생성하고 검증하는 정적 DI engine 이다. Android 에서 어떤 component 가 Activity, Fragment, ViewModel, Worker 와 어떻게 만나야 하는지는 별도의 integration policy 가 필요하다.

**Hilt**(Dagger를 안드로이드 컴포넌트 생명주기에 맞춰 의존성 그래프 생성을 자동화하는 구글의 공식 DI 라이브러리) 는 이 Android integration 을 표준화한다. 순수 Dagger 를 쓰는 경우에는 component owner, subcomponent/factory, injection timing, test replacement 를 프로젝트가 직접 설계해야 한다.

공식 문서: [Dagger basics](https://developer.android.com/training/dependency-injection/dagger-basics)

### 판단 기준

- Dagger 는 컴파일 타임에 DI 그래프 정합성을 검증하는 도구일 뿐이므로, Dagger Component 의 생명주기는 안드로이드 생명주기에 맞게 개발자가 직접 설계하고 연결해야 한다.

### 경계

- Dagger 자체는 메모리 누수를 막아주지 않으므로, 정적 그래프 내부에 동적 UI 컨텍스트가 갇히지 않도록 Component 와 **Scope**(스코프 — 의존성 객체의 생명주기를 특정 DI 컨테이너 수명과 일치시켜 재사용을 제어하는 어노테이션) 의 범위를 안드로이드 컴포넌트 생명주기와 정확히 일치시켜야 한다.
