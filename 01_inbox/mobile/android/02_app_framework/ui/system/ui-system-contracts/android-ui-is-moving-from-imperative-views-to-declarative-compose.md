---
title: android-ui-is-moving-from-imperative-views-to-declarative-compose
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-04 14:00:00 +09:00
date created: 2026-07-31 23:38:40 +09:00
---

## Android UI 는 imperative View 에서 declarative Compose 로 중심이 이동했다

Android 의 기존 View System 은 화면 객체를 만들고 나중에 속성을 변경하는 imperative 모델이다. Jetpack Compose 는 현재 state 를 입력받아 UI 를 계산하는 declarative 모델이다.

이 변화는 단순히 XML 을 Kotlin 함수로 바꾸는 문제가 아니다. View System 에서는 view reference, adapter, listener, mutation 순서가 중요하다. Compose 에서는 state 읽기, [recomposition](../../../jetpack-compose/runtime/recomposition.md), effect boundary 가 중요하다.

그래서 Compose UI 는 가능한 한 `UI = f(state)` 형태로 유지한다. 네트워크 호출, 저장소 변경, analytics 같은 [부수 효과](../../../../../../computer-science/side-effect.md)는 composable 본문이 아니라 [viewmodel](../../../viewmodel.md), repository, 또는 effect API 의 명시적인 경계로 옮긴다.

Compose 의 runtime 관점은 [Automatic State Observation은 Compose와 Flutter rebuild 모델의 핵심 차이다](../../../jetpack-compose/runtime/compose-runtime-contracts/automatic-state-observation-is-the-compose-flutter-rebuild-difference.md) 와 연결된다.

### 판단 기준

- 신규 안드로이드 UI 개발 시 명령형 View System(`findViewById`, XML Layout, `setText`) 대신 선언형 Compose 기반의 데이터 바인딩 및 Recomposition 패러다임을 표준으로 채택한다.
- UI 상태 변화가 화면 렌더링으로 연결되는 데이터 흐름을 단방향(Unidirectional Data Flow)으로 유지한다.

### 경계

- 기존의 대규모 View System 기반 프로젝트나 `AndroidView` 호환성(Interop) 래퍼를 다룰 때는 View 수명주기와 Compose Composition 수명주기가 충돌하지 않도록 `DisposeOnViewTreeLifecycleDestroyed` 전략 등을 명시적으로 수반해야 한다.

```kotlin
// View System: findViewById로 참조를 얻고 setter로 직접 mutate한다
val textView = findViewById<TextView>(R.id.title)
textView.text = "Hello"

// Compose: 같은 결과를 state 입력에 대한 선언으로 표현한다
@Composable
fun Title(text: String) {
    Text(text)
}
```

`AndroidView { }` 로 기존 View 를 Compose 트리에 끼워 넣으면, 그 View 는 Compose 의 declarative 모델이 아니라 원래의 imperative mutation 규칙을 그대로 따른다. 이 경계에서 lifecycle 을 명시적으로 맞추지 않으면(`ViewCompositionStrategy.DisposeOnViewTreeLifecycleDestroyed` 등) View 가 Composition 보다 오래 남거나 일찍 정리되는 문제가 생긴다.
