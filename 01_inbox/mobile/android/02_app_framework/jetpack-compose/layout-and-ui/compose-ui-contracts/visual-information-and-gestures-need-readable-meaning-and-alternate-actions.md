---
title: Visual information and gestures need readable meaning and alternate actions
tags: [android, jetpack-compose, compose/ui]
aliases: [contentDescription, CustomAccessibilityAction]
date modified: 2026-07-31 23:59:30 +09:00
date created: 2026-07-31 23:59:30 +09:00
---

# Visual information and gestures need readable meaning and alternate actions

시각 정보는 접근성 서비스가 읽을 수 있는 의미로 바뀌어야 한다. 아이콘 버튼에는 동작을 설명하는 content description이나 click label이 필요하고, 색상만으로 상태를 전달하지 않는다.

제스처 전용 동작은 대체 action이 필요할 수 있다. swipe, drag, long press처럼 발견하기 어려운 동작은 `CustomAccessibilityAction`이나 명확한 보조 control로 제공한다.

터치 대상은 최소 48dp 기준을 검토하고, text는 사용자 font scale에 대응해야 한다. Material 컴포넌트의 기본 접근성 지원을 쓰는지, custom clickable/semantics를 직접 구성하는지 구분한다.

관련 노트: [Semantics Tree는 UI 의미를 접근성 서비스와 테스트에 드러낸다](01_inbox/mobile/android/02_app_framework/jetpack-compose/layout-and-ui/compose-ui-contracts/semantics-tree-makes-ui-meaning-visible-to-accessibility-and-tests.md), [접근성 품질은 서비스, 검사기, Semantics 테스트로 검증한다](01_inbox/mobile/android/02_app_framework/jetpack-compose/layout-and-ui/compose-ui-contracts/accessibility-quality-requires-service-scanner-and-semantics-verification.md)

출처: [Accessibility in Compose](https://developer.android.com/develop/ui/compose/accessibility), [Accessibility basics](https://developer.android.com/develop/ui/compose/accessibility/api-defaults)
