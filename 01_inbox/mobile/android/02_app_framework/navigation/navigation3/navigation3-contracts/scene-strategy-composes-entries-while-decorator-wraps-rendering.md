---
title: "SceneStrategy는 entry를 조합하고 SceneDecorator는 렌더링을 감싼다"
tags: [android, android/navigation, android/navigation3]
aliases: ["SceneStrategy는 entry를 조합하고 SceneDecorator는 렌더링을 감싼다"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# SceneStrategy는 entry를 조합하고 SceneDecorator는 렌더링을 감싼다

Navigation 3에서 SceneStrategy는 back stack의 어떤 entry들을 어떤 scene으로 보여줄지 결정하는 확장 지점이다. Adaptive layout이나 multi-pane 표시처럼 여러 entry를 함께 읽는 정책은 strategy 쪽 책임이다.

SceneDecorator나 entry decorator는 이미 선택된 entry/scene의 rendering 주변에 saveable state, ViewModel store, transition 같은 횡단 관심사를 더하는 지점이다. 표시할 entry를 고르는 정책과 렌더링을 감싸는 정책을 섞지 않는다.

## 판단 기준

- 여러 entry를 하나의 visual scene으로 묶는 문제는 SceneStrategy에서 해결한다.
- entry별 saveable state, ViewModel store, transition wrapper는 decorator에서 해결한다.
- scene 선택 정책이 feature content 내부로 새면 route registry와 layout policy가 결합된다.
- adaptive scaffold와 함께 쓸 때는 pane 상태와 scene 상태의 소유자를 하나로 정한다.

관련 노트: [Metadata와 SceneStrategy는 표시 정책을 전달한다](01_inbox/mobile/android/02_app_framework/navigation/navigation3/navigation3-contracts/metadata-and-scene-strategy-carry-display-policy.md), [Navigation 3 Scene과 adaptive scaffold는 서로 다른 레이아웃 문제를 푼다](01_inbox/mobile/android/02_app_framework/navigation/adaptive-navigation/adaptive-navigation-contracts/navigation3-scenes-and-adaptive-scaffolds-solve-different-layout-problems.md)
