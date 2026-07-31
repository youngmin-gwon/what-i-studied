---
title: Accessibility quality requires service scanner and Semantics verification
tags: [android, jetpack-compose, compose/ui]
aliases: [TalkBack, Accessibility Scanner, Compose UI test]
date modified: 2026-07-31 23:59:30 +09:00
date created: 2026-07-31 23:59:30 +09:00
---

접근성 품질은 코드 스타일만으로 보장되지 않는다. TalkBack으로 포커스 순서, 읽히는 문장, action 가능 여부를 직접 확인하고, Accessibility Scanner로 touch target, contrast, description 누락을 보조 점검한다.

Layout Inspector나 Compose testing은 Semantics tree를 확인하는 데 유용하다. 테스트는 사용자가 이해하는 의미를 검증하되, 테스트 편의를 위해 accessibility label을 오염시키지 않도록 `testTag`와 semantics 목적을 분리한다.

`enableAccessibilityChecks()` 같은 테스트 API의 artifact, import, 지원 버전은 프로젝트의 Compose/AndroidX 버전과 맞춰 확인한다. 공식 예시를 그대로 일반 규칙으로 고정하지 않는다.

관련 노트: [Semantics Tree는 UI 의미를 접근성 서비스와 테스트에 드러낸다](01_inbox/mobile/android/02_app_framework/jetpack-compose/layout-and-ui/compose-ui-contracts/semantics-tree-makes-ui-meaning-visible-to-accessibility-and-tests.md), [Testing quality contracts](01_inbox/mobile/android/06_testing_performance/testing/testing-quality-contracts/testing-quality-contracts.md)

출처: [Test your Compose layout](https://developer.android.com/develop/ui/compose/testing), [Accessibility Scanner](https://support.google.com/accessibility/android/answer/6376570)
