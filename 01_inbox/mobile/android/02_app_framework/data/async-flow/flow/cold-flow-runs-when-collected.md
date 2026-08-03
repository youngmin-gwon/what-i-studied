---
title: Cold Flow는 collect될 때 실행된다
tags: [android, android/data, android/async, android/flow]
aliases: ["Cold Flow는 collect될 때 실행된다"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# Cold Flow는 collect될 때 실행된다

Kotlin `Flow`의 기본 형태는 cold stream이다. `flow { ... }` 블록은 선언한 순간 실행되지 않고, collector가 `collect`를 시작할 때마다 실행된다.

이 계약은 repository API를 단순하게 만든다. repository는 "데이터가 바뀌면 흘러나오는 stream"을 `Flow`로 노출하고, ViewModel이나 UI 계층이 필요할 때 수집한다. 아무도 수집하지 않는 Flow는 실행되지 않는 선언일 뿐이다.

같은 upstream을 여러 화면 상태가 공유해야 하면 cold Flow를 그대로 여러 번 collect하지 말고 `shareIn`이나 `stateIn`으로 공유 수명과 replay 정책을 명시한다. 화면 상태로 현재값을 유지해야 한다면 [StateFlow는 현재값이 필요한 화면 상태에 사용하고 Flow는 원천 데이터 흐름에 사용한다](01_inbox/mobile/android/02_app_framework/data/async-flow/flow-state-contracts/stateflow-is-for-current-screen-state-flow-is-for-source-stream.md)를 따른다.

Compose나 Lifecycle UI에서 수집할 때는 화면 수명에 맞춰 collect가 시작되고 멈춰야 한다. 관련 계약은 [Flow는 UI에서 lifecycle-aware API로 수집한다](01_inbox/mobile/android/02_app_framework/data/async-flow/flow-state-contracts/collect-flow-for-ui-with-lifecycle-aware-api.md)에 둔다.

공식 문서: [Flow on Android](https://developer.android.com/kotlin/flow)
