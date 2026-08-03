---
title: Dagger는 정적 graph 엔진이지 Android lifecycle 정책 자체가 아니다
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-03 16:30:14 +09:00
date created: 2026-08-03 16:28:45 +09:00
---

# Dagger는 정적 graph 엔진이지 Android lifecycle 정책 자체가 아니다

Dagger 는 compile time 에 dependency graph 를 생성하고 검증하는 정적 DI engine 이다. Android 에서 어떤 component 가 Activity, Fragment, ViewModel, Worker 와 어떻게 만나야 하는지는 별도의 integration policy 가 필요하다.

Hilt 는 이 Android integration 을 표준화한다. 순수 Dagger 를 쓰는 경우에는 component owner, subcomponent/factory, injection timing, test replacement 를 프로젝트가 직접 설계해야 한다.

공식 문서: [Dagger basics](https://developer.android.com/training/dependency-injection/dagger-basics)

### 판단 기준

- Dagger 는 컴파일 타임에 DI 그래프 정합성을 검증하는 도구일 뿐이므로, Dagger Component 의 생명주기는 안드로이드 생명주기에 맞게 개발자가 직접 설계하고 연결해야 한다.

### 경계

- Dagger 자체는 메모리 누수를 막아주지 않으므로, 정적 그래프 내부에 동적 UI 컨텍스트가 갇히지 않도록 Component 와 Scope 의 범위를 안드로이드 컴포넌트 생명주기와 정확히 일치시켜야 한다.
