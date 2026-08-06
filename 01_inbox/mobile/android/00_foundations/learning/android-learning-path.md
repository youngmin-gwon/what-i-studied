---
title: android-learning-path
tags: ["android", "android/foundations"]
aliases: []
date modified: 2026-08-05 11:23:51 +09:00
date created: 2026-08-03 16:59:22 +09:00
---

## Android Learning Path 는 안드로이드 개발의 기반을 다지는 학습 경로다

Android learning path 는 resource 목록이 아니라 프로젝트에서 내려야 할 결정까지 이어지는 질문별 routing guide 다.

### 읽는 순서

1. [Boundary 중심 학습](./learning-contracts/learn-android-by-boundary-before-api-catalogs.md) 으로 lifecycle, process, state, permission, storage, background work 를 먼저 구분한다.
2. [학습 자료의 역할](./learning-contracts/official-docs-codelabs-samples-and-talks-answer-different-learning-questions.md) 에 따라 contract 확인, 실습, 통합 예제, mental model 중 현재 필요한 자료를 고른다.
3. Flutter 경험이 있으면 [개념 경계 매핑](./learning-contracts/flutter-developers-should-map-concepts-not-class-names.md) 으로 이름이 비슷한 API 의 lifetime 과 ownership 차이를 확인한다.
4. [프로젝트 결정으로 끝내기](./learning-contracts/learning-path-should-end-at-project-decisions-not-note-consumption.md) 의 질문에 답하고, 답하지 못한 영역의 정본만 더 읽는다.

[Learning Contracts](./learning-contracts/learning-contracts.md) 는 학습 원칙 네 가지의 역할 차이와 새 학습 노트의 경계를 관리하는 하위 지도다.

### Learning Notes

- [Android는 API catalog보다 boundary 단위로 먼저 배운다](./learning-contracts/learn-android-by-boundary-before-api-catalogs.md)
- [공식 문서, Codelab, sample, talk는 서로 다른 학습 질문에 답한다](./learning-contracts/official-docs-codelabs-samples-and-talks-answer-different-learning-questions.md)
- [Flutter 개발자는 class 이름보다 개념 경계를 대응시켜야 한다](./learning-contracts/flutter-developers-should-map-concepts-not-class-names.md)
- [학습 경로의 끝은 문서 소비가 아니라 프로젝트 결정이어야 한다](./learning-contracts/learning-path-should-end-at-project-decisions-not-note-consumption.md)

### 시작 경로

1. [Android는 계층형 플랫폼이다](../overview/foundation-contracts/android-is-layered-mobile-platform-not-just-an-app-sdk.md)
2. [문제 boundary를 찾는다](../overview/foundation-contracts/android-stack-boundaries-explain-where-a-problem-belongs.md)
3. [앱 아키텍처 map으로 이동한다](../../02_app_framework/architecture/android-app-architecture.md)
4. [Compose runtime/state model로 이동한다](../../02_app_framework/jetpack-compose/runtime/compose-runtime-and-state-model.md)

### 문제별 경로

- Android 자체가 처음이면 시작 경로를 그대로 따른다.
- Flutter 에서 넘어왔다면 1, 2 뒤에 개념 경계 매핑을 먼저 읽고 Context, [viewmodel](../../02_app_framework/viewmodel.md), Compose state 를 각각 비교한다.
- 기존 앱 문제를 해결하려면 전체 경로를 순회하지 않고 [Android System Map](../overview/android-system-map.md) 에서 소유 계층을 찾은 뒤 공식 guide/API reference 로 contract 를 확인한다.
- 새 프로젝트를 설계한다면 state owner, persistence, background guarantee, security boundary, test/release gate 를 문장으로 결정할 수 있을 때 학습을 종료한다.

### 경계

이 폴더에는 학습 순서와 자료 선택 기준만 둔다. 특정 library 의 tutorial 이나 sample 해설은 해당 기술 영역에 둔다.

### Learning Spine Chapters
- [01-android-ecosystem-and-contract-surfaces.md](../learning-spine/01-android-ecosystem-and-contract-surfaces.md)
- [02-android-platform-execution-layers-and-call-paths.md](../learning-spine/02-android-platform-execution-layers-and-call-paths.md)
- [03-source-to-installed-package.md](../learning-spine/03-source-to-installed-package.md)
