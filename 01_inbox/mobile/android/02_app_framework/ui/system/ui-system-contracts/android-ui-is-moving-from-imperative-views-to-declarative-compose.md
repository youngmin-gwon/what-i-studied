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

UI system 노트는 View System과 Compose가 state, tree mutation, layout, side effect를 어디서 처리하는지 비교하는 기준으로 읽는다.

## 경계

API 이름 매핑보다 rendering model, state ownership, insets/back/adaptive boundary를 먼저 본다.
