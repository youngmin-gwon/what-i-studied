---
title: Composition uses callsite identity to preserve remembered values
tags: [android, jetpack-compose, compose/runtime]
aliases: [Slot Table, positional memoization]
date modified: 2026-07-31 23:59:00 +09:00
date created: 2026-07-31 23:59:00 +09:00
---

# Composition uses callsite identity to preserve remembered values

Composition은 Composable 호출의 위치와 구조를 이용해 `remember` 값, group, node 관계를 보존한다. 같은 `remember` 코드라도 호출 위치가 다르면 서로 다른 저장공간이 된다.

조건문, 반복문, list item에서는 호출 구조와 key가 identity에 영향을 준다. item identity를 안정적으로 주지 않으면 위치 변화가 값 보존과 재사용을 흐릴 수 있다.

Slot Table, group, Composer 같은 용어는 Runtime 이해를 위한 내부 모델이다. 디컴파일된 함수 signature나 내부 자료구조를 앱 코드가 의존하는 API처럼 쓰지 않는다.

관련 노트: [remember는 일반 cache가 아니라 Composition에 귀속된 저장공간이다](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/compose-runtime-contracts/remember-is-composition-scoped-storage-not-general-cache.md), [@Composable 컴파일 결과는 restart와 skip 제어를 가능하게 한다](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/compose-runtime-contracts/composable-compiler-output-enables-restart-and-skip-control.md)

출처: [Lifecycle of composables](https://developer.android.com/develop/ui/compose/lifecycle)
