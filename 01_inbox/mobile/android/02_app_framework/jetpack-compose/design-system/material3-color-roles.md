---
title: material3-color-roles
tags: [android, compose/design-system, jetpack-compose]
aliases: [ColorScheme, Material 3 color roles]
date modified: 2026-08-06 14:40:00 +09:00
date created: 2026-07-31 23:59:30 +09:00
---

## Material 3 색상 역할은 고정 색상이 아니라 의미적 의도를 표현한다

`primary`, `error`, `surface` 같은 `ColorScheme` 속성은 색 이름이 아니라 UI 역할이다. 컴포넌트가 역할을 읽으면 light/dark, dynamic color, 브랜드 palette가 교체되어도 “주요 행동”, “오류”, “표면”이라는 의도는 남는다.

```kotlin
@Composable
fun ErrorBanner(message: String) {
    Surface(
        color = MaterialTheme.colorScheme.errorContainer,
        contentColor = MaterialTheme.colorScheme.onErrorContainer,
        shape = MaterialTheme.shapes.medium,
    ) {
        Text(message, Modifier.padding(16.dp))
    }
}
```

역할 매핑 메커니즘은 다음처럼 컴포넌트 계약에서 결정한다.

| UI 의도 | container role | content role |
|---|---|---|
| 가장 중요한 행동 | `primary` | `onPrimary` |
| 낮은 강조의 주요 영역 | `primaryContainer` | `onPrimaryContainer` |
| 오류 안내 영역 | `errorContainer` | `onErrorContainer` |
| 일반 화면 표면 | `surface` | `onSurface` |

raw `Color(0xFF...)`가 컴포넌트에 흩어지면 theme 전환 시 누락을 찾기 어렵다. 브랜드 고유 색이 필요하면 먼저 프로젝트 semantic role로 이름 붙이고 provider에서 light/dark 값을 매핑한다.

검증은 동일 컴포넌트를 light/dark/dynamic scheme에 렌더링해 screenshot diff를 남기고, 상태별 content contrast와 disabled alpha를 접근성 검사로 확인한다. 색이 바뀌는 것보다 역할 쌍이 유지되는지가 핵심 증거다.

관련 노트: [Material 3 on-color와 surface 계열은 대비와 계층을 함께 만든다](material3-surfaces-contrast.md), [Dynamic color는 Material color scheme에 들어오는 플랫폼 입력이다](dynamic-color-theming.md)

출처: [Material 3 in Compose](https://developer.android.com/develop/ui/compose/designsystems/material3), [Material Design color roles](https://m3.material.io/styles/color/roles)
