---
title: m3-expressive-switch
tags: [android, compose/design-system, m3-expressive, material3, switch]
aliases: ["Switch의 thumb 아이콘과 햅틱은 별도 계약이다"]
date modified: 2026-08-06 14:42:00 +09:00
date created: 2026-08-05 15:25:00 +09:00
---

## Switch의 thumb 아이콘과 햅틱은 별도 계약이다

Material3 `Switch`의 안정적인 공개 계약은 `checked`, `onCheckedChange`, `thumbContent`, `colors`, `interactionSource`다. `thumbContent`로 check 아이콘을 넣을 수 있지만 필수 동작은 아니다. thumb의 내부 애니메이션을 앱이 표준 morphing 수치로 가정해서도 안 된다. `ToggleOn`·`ToggleOff` 햅틱은 Compose UI 1.8.0+에서 쓸 수 있는 선택적 앱 피드백이다.

```kotlin
@Composable
fun HapticSettingSwitch(
    checked: Boolean,
    onCheckedChange: (Boolean) -> Unit,
) {
    val haptics = LocalHapticFeedback.current
    Switch(
        checked = checked,
        onCheckedChange = { next ->
            haptics.performHapticFeedback(
                if (next) HapticFeedbackType.ToggleOn
                else HapticFeedbackType.ToggleOff,
            )
            onCheckedChange(next)
        },
        thumbContent = if (checked) {
            {
                Icon(
                    Icons.Default.Check,
                    contentDescription = null,
                    modifier = Modifier.size(SwitchDefaults.IconSize),
                )
            }
        } else {
            null
        },
        modifier = Modifier.testTag("sync_switch"),
    )
}
```

내부 동작에서 아이콘의 `contentDescription`은 `null`이다. 부모 `Switch`가 role, checked state, toggle action을 이미 제공하므로 자식 아이콘 설명을 추가하면 TalkBack 발화가 중복될 수 있다. 햅틱 호출도 상태 소유자의 승인을 대신하지 않는다. 비동기 저장이 실패할 수 있으면 확정 상태와 낙관적 표시 정책을 따로 설계한다.

```kotlin
@Test
fun switch_updates_checked_semantics() {
    rule.onNodeWithTag("sync_switch")
        .assertIsOff()
        .performClick()
        .assertIsOn()
}
```

관찰 증거로 UI test는 semantics의 on/off 전환을 검증한다. 햅틱은 기기 설정과 하드웨어에 좌우되므로 실제 기기에서 on/off 각각 한 번만 발생하는지 확인하거나, wrapper에 피드백 함수를 주입해 호출 type을 단위 테스트한다. custom thumb의 press shape를 추가한다면 그것은 `Switch` 기본 계약이 아니라 앱 wrapper의 애니메이션·성능 책임이다.

관련 노트: [Material 3 Expressive 디자인 시스템 및 컴포넌트 아키텍처](m3-expressive-architecture.md), [HapticFeedbackType은 UX 인터랙션을 플랫폼 햅틱 type에 매핑한다](../../../04_system_services/device-capabilities/haptics-vibrator/haptic-feedback-patterns.md)

출처: [Material 3 Switch API](https://developer.android.com/reference/kotlin/androidx/compose/material3/Switch.composable), [HapticFeedbackType API](https://developer.android.com/reference/kotlin/androidx/compose/ui/hapticfeedback/HapticFeedbackType)
