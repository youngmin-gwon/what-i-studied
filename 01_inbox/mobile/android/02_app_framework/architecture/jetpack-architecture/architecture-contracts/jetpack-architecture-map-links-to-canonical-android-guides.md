---
title: jetpack-architecture-map-links-to-canonical-android-guides
tags: [android, android/architecture, android/jetpack]
aliases: ["Jetpack Architecture 문서는 세부 구현을 반복하지 않는 map이어야 한다"]
date modified: 2026-08-04 16:33:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Jetpack Architecture 문서는 세부 구현을 반복하지 않는 map 이어야 한다

Jetpack Architecture 개요 문서는 ViewModel, UI state, Flow, Room, WorkManager, Navigation, Hilt, Compose 의 구현 세부를 다시 설명하는 곳이 아니다. 각 주제는 이미 별도 정본 map 을 가진다.

이 문서의 역할은 어떤 질문이 어느 map 으로 가야 하는지 안내하는 것이다. 화면 상태와 reducer 는 state-management, async stream 은 Flow, 영속 데이터는 storage, 지연 작업은 background-work, 외부 진입과 route 는 navigation/intent, 의존성 lifetime 은 DI, UI runtime 은 Compose 로 보낸다.

이렇게 유지하면 architecture 문서가 카탈로그가 아니라 decision index 가 된다. 같은 내용을 여러 큰 문서가 반복하면서 오래된 API 설명을 남기는 문제도 줄어든다.

관련 노트: [Jetpack Architecture map](../android-jetpack-architecture-map.md), [Flow/StateFlow 정본](../../../data/async-flow/flow-state-contracts/flow-state-contracts.md), [Compose runtime 정본](../../../jetpack-compose/runtime/compose-runtime-and-state-model.md).

공식 문서: [Guide to app architecture](https://developer.android.com/topic/architecture)
