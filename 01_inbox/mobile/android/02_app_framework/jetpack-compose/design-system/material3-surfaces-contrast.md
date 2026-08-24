---
title: material3-surfaces-contrast
tags: [android, compose/design-system, jetpack-compose]
aliases: [on color, surface container]
date modified: 2026-08-06 14:40:00 +09:00
date created: 2026-07-31 23:59:30 +09:00
---

## Material 3 on-color와 surface는 대비와 계층을 연결한다

`onPrimary`, `onPrimaryContainer`, `onSurface`는 대응 배경 위의 텍스트·아이콘 역할이다. `onPrimary`를 임의의 `surface` 위에 놓는 식으로 쌍을 섞으면 `ColorScheme`이 의도한 대비 관계를 잃는다.

```kotlin
@Composable
fun SettingsSection(content: @Composable ColumnScope.() -> Unit) {
    Surface(
        color = MaterialTheme.colorScheme.surfaceContainerLow,
        contentColor = MaterialTheme.colorScheme.onSurface,
        tonalElevation = 1.dp,
        shape = MaterialTheme.shapes.large,
    ) {
        Column(Modifier.padding(16.dp), content = content)
    }
}
```

전달 메커니즘에서 `Surface`의 `contentColor`는 `LocalContentColor`로 하위 `Text`와 `Icon`에 전달된다. 따라서 container/content 쌍을 경계에서 설정하면 자식마다 색을 반복하지 않는다. 다만 자식이 색이나 alpha를 덮어쓰면 이 계약은 더 이상 자동 보장되지 않는다.

Surface container role은 낮고 높은 표면 계층을 tonal 차이로 표현한다. `tonalElevation`도 surface tint 계산에 참여할 수 있지만, 이것이 실제 레이아웃 z-order나 모든 theme에서의 contrast를 대신하지는 않는다.

관찰 증거는 light/dark/dynamic theme의 screenshot과 접근성 contrast 결과다. disabled alpha, 이미지 위 텍스트, custom color는 각각 최종 합성색으로 다시 검사한다.

관련 노트: [Material 3 색상 역할은 고정된 색상이 아닌 의미적 의도를 표현한다](material3-color-roles.md), [접근성 품질은 서비스·검사기·Semantics 검증을 함께 요구한다](../layout-and-ui/accessibility-service-verification.md)

출처: [Material 3 in Compose](https://developer.android.com/develop/ui/compose/designsystems/material3), [Material Design color roles](https://m3.material.io/styles/color/roles)
