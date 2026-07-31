---
title: Composable body must be fast idempotent and side effect free
tags: [android, jetpack-compose, compose/runtime]
aliases: [side-effect free composable]
date modified: 2026-07-31 23:59:00 +09:00
date created: 2026-07-31 23:59:00 +09:00
---

Composable body는 같은 입력으로 여러 번 실행되어도 같은 UI 설명을 만들어야 한다. DB write, analytics 전송, preference update, repository mutation처럼 외부에 관찰 가능한 변경을 본문에 넣으면 skip, retry, cancel, 재실행 타이밍에 따라 결과가 흔들린다.

무거운 작업도 본문에 두지 않는다. Compose는 Composable을 자주 다시 호출할 수 있으므로 storage read, 큰 list sort, blocking I/O는 jank를 만들 수 있다.

외부 작업은 callback에서 app logic으로 전달하거나, composition 수명과 맞는 effect API로 옮긴다. 이 원칙은 purity라는 미학이 아니라 Runtime 최적화와 correctness를 위한 실행 계약이다.

관련 노트: [Composable과 함께 취소되어야 하는 작업은 LaunchedEffect로 시작한다](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/compose-state-and-effect-contracts/launched-effect-owns-composable-cancellable-work.md), [무거운 작업은 composition 안에 두지 않는다](01_inbox/mobile/android/02_app_framework/jetpack-compose/performance/compose-performance-contracts/heavy-work-does-not-belong-in-composition.md)

출처: [Thinking in Compose](https://developer.android.com/develop/ui/compose/mental-model), [Side-effects in Compose](https://developer.android.com/develop/ui/compose/side-effects)
