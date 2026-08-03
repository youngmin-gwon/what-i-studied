---
title: "Android UI는 imperative View에서 declarative Compose로 중심이 이동했다"
tags: ["android", "android/app-framework"]
---

# Android UI는 imperative View에서 declarative Compose로 중심이 이동했다

Android의 기존 View System은 화면 객체를 만들고 나중에 속성을 변경하는 imperative 모델이다. Jetpack Compose는 현재 state를 입력받아 UI를 계산하는 declarative 모델이다.

이 변화는 단순히 XML을 Kotlin 함수로 바꾸는 문제가 아니다. View System에서는 view reference, adapter, listener, mutation 순서가 중요하다. Compose에서는 state 읽기, recomposition, effect boundary가 중요하다.

그래서 Compose UI는 가능한 한 `UI = f(state)` 형태로 유지한다. 네트워크 호출, 저장소 변경, analytics 같은 부수 효과는 composable 본문이 아니라 ViewModel, repository, 또는 effect API의 명시적인 경계로 옮긴다.

Compose의 runtime 관점은 [Automatic State Observation은 Compose와 Flutter rebuild 모델의 핵심 차이다](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/compose-runtime-contracts/automatic-state-observation-is-the-compose-flutter-rebuild-difference.md)와 연결된다.

## 판단 기준

- 신규 안드로이드 UI 개발 시 명령형 View System(`findViewById`, XML Layout, `setText`) 대신 선언형 Compose 기반의 데이터 바인딩 및 Recomposition 패러다임을 표준으로 채택한다.
- UI 상태 변화가 화면 렌더링으로 연결되는 데이터 흐름을 단방향(Unidirectional Data Flow)으로 유지한다.

## 경계

- 기존의 대규모 View System 기반 프로젝트나 `AndroidView` 호환성(Interop) 래퍼를 다룰 때는 View 수명주기와 Compose Composition 수명주기가 충돌하지 않도록 `DisposeOnViewTreeLifecycleDestroyed` 전략 등을 명시적으로 수반해야 한다.
