---
title: Compose stability and strong skipping affect skippability
tags: [android, jetpack-compose, compose/performance]
aliases: [Compose stability, Strong skipping]
date modified: 2026-07-31 23:59:00 +09:00
date created: 2026-07-31 23:59:00 +09:00
---

Compose가 Composable 호출을 skip하려면 입력이 비교 가능한 계약을 가져야 한다. Stability는 “값이 바뀌면 Compose가 알 수 있는가”와 “같은 값 비교가 안전한가”를 compiler가 판단하는 근거다.

Strong skipping은 Compose compiler mode다. 공식 문서 기준 Kotlin 2.0.20부터 기본 활성화되어 restartable Composable을 더 넓게 skippable로 만들고, Composable 내부 lambda를 자동으로 remember할 수 있다.

Strong skipping에서도 비교 규칙은 단순하지 않다. Unstable parameter는 instance equality(`===`)로, stable parameter는 object equality(`equals`)로 비교된다. 따라서 unstable object를 매번 새로 만들면 skip이 여전히 깨질 수 있다.

`@Stable`이나 `@Immutable`은 성능 장식이 아니라 지켜야 할 계약이다. 근거 없이 붙이면 compiler를 속여 잘못된 UI 업데이트를 만들 수 있다.

안정성 개선은 추측이 아니라 compiler report, Layout Inspector, benchmark나 trace로 병목을 확인한 뒤 적용한다.

관련 노트: [@Composable 컴파일 결과는 restart와 skip 제어를 가능하게 한다](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/compose-runtime-contracts/composable-compiler-output-enables-restart-and-skip-control.md), [Compose 성능 최적화는 measure, debug, improve 순환으로 진행한다](01_inbox/mobile/android/02_app_framework/jetpack-compose/performance/compose-performance-contracts/compose-performance-starts-with-measure-debug-improve-loop.md)

출처: [Strong skipping mode](https://developer.android.com/develop/ui/compose/performance/stability/strongskipping), [Stability in Compose](https://developer.android.com/develop/ui/compose/performance/stability)
