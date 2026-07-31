---
title: Automatic State Observation is the Compose Flutter rebuild difference
tags: [android, jetpack-compose, compose/runtime]
aliases: [Compose for Flutter developers, A Compose State of Mind]
date modified: 2026-07-31 23:59:00 +09:00
date created: 2026-07-31 23:59:00 +09:00
---

# Automatic State Observation is the Compose Flutter rebuild difference

Flutter 개발자가 Compose를 볼 때 가장 먼저 바꿔야 할 관점은 “Widget 객체를 다시 build한다”가 아니라 “Composable 함수가 어떤 Snapshot State를 읽었는지 Runtime이 추적한다”는 점이다.

Flutter의 `setState`는 개발자가 dirty 범위를 선언하는 명령에 가깝고, Provider/Riverpod은 어떤 Widget이 어떤 provider를 보는지 별도 라이브러리가 추적한다. Compose는 observable state read를 Runtime 모델의 중심에 둔다.

그래서 Compose 성능 판단은 “Composable이 호출되면 나쁘다”가 아니라 “어디에서 state를 읽었고, 어떤 parameter가 skip을 막고, 어떤 work가 composition에 들어갔는가”로 바뀐다. 이것이 `remember`, state hoisting, effect API가 같은 mental model 위에 놓이는 이유다.

관련 노트: [Snapshot State 관찰은 State를 읽은 scope를 invalidation 대상으로 만든다](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/compose-runtime-contracts/snapshot-state-observation-invalidates-state-read-scopes.md), [Compose state owner는 읽고 쓰는 범위의 가장 낮은 공통 owner다](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/compose-runtime-contracts/compose-state-owner-is-the-lowest-common-owner-that-needs-read-or-write.md)

출처: [Thinking in Compose](https://developer.android.com/develop/ui/compose/mental-model), [State and Jetpack Compose](https://developer.android.com/develop/ui/compose/state)
