---
title: remember-is-composition-scoped-storage-not-general-cache
tags: [android, compose/runtime, jetpack-compose]
aliases: [remember]
date modified: 2026-08-03 18:11:00 +09:00
date created: 2026-07-31 23:59:00 +09:00
---

## remember 는 범용 캐시가 아니라 Composition 스코프 저장공간이다

`remember` 는 일반 memoization cache 가 아니라 Composition 의 특정 호출 위치에 귀속된 저장공간이다. Recomposition 사이에는 값을 유지하지만, 해당 call site 가 Composition 에서 제거되면 값도 잊힌다.

Key 를 넘기면 key 변화가 저장값의 identity 를 바꾼다. 이때 `remember` block 은 다시 실행되고 이전 값은 더 이상 같은 저장공간으로 취급되지 않는다.

`remember` 는 설정 변경, 시스템 주도 process recreation, 앱 재시작까지 보존하는 장치가 아니다. 작은 UI 복원 상태는 `rememberSaveable`, 화면 상태는 ViewModel/state holder, 영구 데이터는 persistence layer 가 후보가 된다.

관련 노트: [Composable 수명보다 오래 필요한 작은 복원 상태에만 rememberSaveable을 사용한다](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/compose-state-and-effect-contracts/remember-saveable-is-for-small-restorable-ui-state.md), [Composition은 호출 위치 identity로 remember 값을 보존한다](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/compose-runtime-contracts/composition-uses-callsite-identity-to-preserve-remembered-values.md)

출처: [State and Jetpack Compose](https://developer.android.com/develop/ui/compose/state)
