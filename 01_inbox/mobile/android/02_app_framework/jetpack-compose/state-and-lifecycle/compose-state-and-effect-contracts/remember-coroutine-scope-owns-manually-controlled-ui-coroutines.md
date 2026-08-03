---
title: rememberCoroutineScope는 수동 제어 UI Coroutine을 소유한다
tags: [android, compose/state, jetpack-compose]
aliases: [rememberCoroutineScope]
date modified: 2026-08-03 16:37:41 +09:00
date created: 2026-07-31 23:59:00 +09:00
---

# rememberCoroutineScope는 수동 제어 UI Coroutine을 소유한다

`rememberCoroutineScope` 는 Composable call site 의 Composition 수명에 묶인 `CoroutineScope` 를 돌려준다. Composable body 에서 바로 작업을 시작하는 API 가 아니라, click handler 나 callback 처럼 composition 밖의 사용자 이벤트에서 coroutine 을 시작할 때 쓴다.

Scope 는 call site 가 Composition 에서 제거되면 cancel 된다. 그래서 snackbar 표시, drawer 열기, scroll animation 처럼 UI controller 와 함께 사라져야 하는 수동 작업에 적합하다.

화면이 사라져도 완료되어야 하는 저장, 동기화, 결제, repository mutation 을 이 scope 에 숨기면 owner 가 잘못된다. 그런 작업은 ViewModel 이나 domain layer 가 소유하고 UI 는 event 만 전달한다.

관련 노트: [UI 컨트롤러와 Effect 실행기는 UI 수명에 둔다](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/compose-state-and-effect-contracts/ui-controllers-and-effect-runners-live-with-ui-lifetime.md), [Composable과 함께 취소되어야 하는 작업은 LaunchedEffect로 시작한다](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/compose-state-and-effect-contracts/launched-effect-owns-composable-cancellable-work.md)

출처: [Side-effects in Compose - rememberCoroutineScope](https://developer.android.com/develop/ui/compose/side-effects#remembercoroutinescope)
