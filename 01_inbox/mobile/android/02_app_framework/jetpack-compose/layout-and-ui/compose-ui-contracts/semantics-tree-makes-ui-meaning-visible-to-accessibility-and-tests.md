---
title: semantics-tree-makes-ui-meaning-visible-to-accessibility-and-tests
tags: [android, compose/ui, jetpack-compose]
aliases: [Accessibility, Semantics]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-07-31 23:59:30 +09:00
---

## Semantics Tree makes UI meaning visible to accessibility and tests

**Semantics**(접근성 서비스 및 UI 테스트 프레임워크가 읽을 수 있도록 UI 요소의 의미적 정보를 캡슐화한 정보 트리) Tree 는 화면의 픽셀 구조가 아니라 UI 의 의미를 접근성 서비스와 Compose 테스트가 읽을 수 있는 형태로 제공한다. Text, Button 같은 기본 컴포넌트는 많은 semantics 를 자동으로 제공하지만, custom component 는 역할, 상태, 설명, action 을 명시해야 할 수 있다.

Semantics 는 accessibility 만을 위한 것이 아니다. Compose test 도 semantics 정보를 사용한다. 다만 접근성 서비스가 해석하는 tree 와 테스트가 보는 merged/unmerged tree 를 완전히 동일시하면 안 된다.

장식 이미지는 보통 `contentDescription = null` 로 두고, 사용자에게 의미가 있는 이미지는 설명한다. 시각적 배치만으로 의미를 전달하면 screen reader 와 테스트 모두 취약해진다.

관련 노트: [Semantics 병합, 정리, 탐색 순서는 의미 단위를 조정한다](./semantics-merging-clearing-and-traversal-control-the-unit-of-meaning.md), [Testing quality contracts](../../../../06_testing_performance/testing/testing-quality-contracts/testing-quality-contracts.md)

출처: [Semantics in Compose](https://developer.android.com/develop/ui/compose/accessibility/semantics)
