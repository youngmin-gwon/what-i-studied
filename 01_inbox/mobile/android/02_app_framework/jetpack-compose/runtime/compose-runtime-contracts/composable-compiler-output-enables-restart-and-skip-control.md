---
title: composable-compiler-output-enables-restart-and-skip-control
tags: [android, compose/runtime, jetpack-compose]
aliases: [Compose compiler, restartable, skippable]
date modified: 2026-08-04 14:00:00 +09:00
date created: 2026-07-31 23:59:00 +09:00
---

## Composable compiler 출력은 재시작과 skip 제어를 가능하게 한다

`@Composable` 은 단순한 marker 가 아니라 Compose compiler 가 Runtime 과 협력할 호출 문맥을 만들도록 한다. Compiler 는 Composable call graph, restart 가능성, skip 가능성, remember 위치 같은 정보를 Runtime 이 다룰 수 있는 형태로 바꾼다.

`Composer` parameter, restart group, slot operation 같은 세부는 버전별 compiler/runtime 구현 detail 이다. 정본 노트에서는 "컴파일러가 재구성 제어 정보를 만든다"까지만 앱 개발자가 의존할 mental model 로 둔다.

Skippability 는 compiler 가 판단하는 안정성 정보와 Runtime 의 parameter comparison 이 함께 만든다. Kotlin 2.0.20 이후 strong skipping 기본값 같은 버전 조건은 성능 정본에서 따로 다룬다.

이 컴파일러 출력은 눈에 보이는 산출물로 확인할 수 있다. Gradle 에 `composeCompiler { reportsDestination.set(...) }` 를 설정하면 빌드마다 `<module>-composables.txt` 리포트가 생성되고, 각 Composable 옆에 `restartable`, `skippable` 태그와 파라미터별 `stable`/`unstable` 태그가 함께 찍힌다. 예를 들어 `unstable snacks: List<Snack>` 처럼 파라미터가 unstable 로 표시된 함수는 `restartable` 만 붙고 `skippable` 태그가 빠져, 값이 같아도 Compose 가 skip 하지 않는다는 것을 리포트로 확인할 수 있다.

관련 노트: [Compose 안정성과 strong skipping은 skippability에 영향을 준다](01_inbox/mobile/android/02_app_framework/jetpack-compose/performance/compose-performance-contracts/compose-stability-and-strong-skipping-affect-skippability.md), [Composition은 호출 위치 identity로 remember 값을 보존한다](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/compose-runtime-contracts/composition-uses-callsite-identity-to-preserve-remembered-values.md)

출처: [Strong skipping mode](https://developer.android.com/develop/ui/compose/performance/stability/strongskipping)
