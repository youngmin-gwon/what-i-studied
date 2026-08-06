---
title: accessibility-quality-requires-service-scanner-and-semantics-verification
tags: [android, compose/ui, jetpack-compose]
aliases: [Accessibility Scanner, Compose UI test, TalkBack]
date modified: 2026-08-06 14:45:00 +09:00
date created: 2026-07-31 23:59:30 +09:00
---

## 접근성 품질은 서비스·검사기·Semantics 검증을 함께 요구한다

한 도구로 접근성을 증명할 수는 없다. Compose UI test는 semantics 계약을, Accessibility Test Framework와 Scanner는 알려진 규칙 위반을, TalkBack·Switch Access 같은 서비스는 실제 탐색과 발화를 확인한다.

Compose 1.8.0 이상에서는 테스트 artifact를 추가하고 자동 검사를 실행할 수 있다.

```kotlin
// androidTestImplementation(
//   "androidx.compose.ui:ui-test-junit4-accessibility:<compose-version>"
// )

@get:Rule
val rule = createAndroidComposeRule<ComponentActivity>()

@Test
fun settings_screen_passes_automated_accessibility_checks() {
    rule.setContent { SettingsScreen() }
    rule.enableAccessibilityChecks()
    rule.onRoot().tryPerformAccessibilityChecks()
}
```

자동 검사는 label, touch target, contrast, traversal order 같은 일부 문제를 찾는다. 통과가 자연스러운 발화나 올바른 사용자 흐름을 보장하지는 않는다. 별도의 semantics test로 사용자가 찾는 의미를 assert한다.

```kotlin
rule.onNodeWithContentDescription("동기화")
    .assertIsOn()
    .assertIsEnabled()
```

검증 메커니즘과 관찰 순서는 재현 가능하게 고정한다.

```text
semantics assertion -> 자동 접근성 검사 -> Scanner -> TalkBack 실제 탐색
```

TalkBack에서는 포커스 순서, 한 노드의 발화, 가능한 action, 상태 변경 후 안내를 기록한다. `testTag`는 테스트 선택자이고 사용자 label이 아니므로 테스트 편의를 위해 `contentDescription`을 추가하지 않는다. artifact와 API 버전이 맞지 않으면 자동 검사를 생략했다고 숨기지 말고 지원 범위를 기록한다.

관련 노트: [Semantics 트리는 UI 의미를 접근성 서비스와 테스트에 드러낸다](./semantics-tree-makes-ui-meaning-visible-to-accessibility-and-tests.md), [Testing quality contracts](../../../../06_testing_performance/testing/testing-quality-contracts/testing-quality-contracts.md)

출처: [Compose 접근성 테스트](https://developer.android.com/develop/ui/compose/accessibility/testing), [Compose 접근성](https://developer.android.com/develop/ui/compose/accessibility)
