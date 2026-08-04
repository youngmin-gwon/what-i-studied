---
title: navigation3-metadata-examples-use-kotlin-syntax-but-syntax-is-not-navigation-contract
tags: [android, android/navigation, android/navigation3]
aliases: ["Navigation 3 metadata 예제의 Kotlin 문법은 navigation 계약이 아니다"]
date modified: 2026-08-03 18:12:02 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Navigation 3 metadata 예제의 Kotlin 문법은 navigation 계약이 아니다

Navigation 3 metadata 예제에는 `Map`, `Any`, `object`, `data object`, trailing lambda, infix function, `when`, operator overloading 같은 Kotlin 문법이 함께 등장한다. 이 문법은 예제를 읽기 위한 배경지식이지 navigation state 의 핵심 계약은 아니다.

Navigation 관점에서 중요한 것은 metadata 가 route entry 에 표시 정책을 붙이고, SceneStrategy 나 decorator 가 그 metadata 를 읽어 렌더링을 바꾼다는 점이다. Kotlin 문법 설명은 이 구조를 이해하기 위한 보조 설명으로만 둔다.

### 판단 기준

- metadata key 의 타입 안정성과 소비 위치가 핵심이지 Kotlin 문법 자체가 핵심이 아니다.
- syntax 설명은 route identity, scene policy, decorator 책임을 이해하는 데 필요한 만큼만 둔다.
- Kotlin 문법 노트가 Navigation 3 정본을 대체하지 않게 한다.

관련 노트: [Metadata와 SceneStrategy는 표시 정책을 전달한다](./metadata-and-scene-strategy-carry-display-policy.md)
