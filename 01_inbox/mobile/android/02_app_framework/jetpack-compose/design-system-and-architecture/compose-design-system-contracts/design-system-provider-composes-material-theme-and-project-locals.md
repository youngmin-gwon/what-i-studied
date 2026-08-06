---
title: design-system-provider-composes-material-theme-and-project-locals
tags: [android, compose/design-system, jetpack-compose]
aliases: [DesignSystemProvider, MaterialTheme]
date modified: 2026-08-06 14:40:00 +09:00
date created: 2026-07-31 23:59:30 +09:00
---

## Design System Provider는 MaterialTheme과 프로젝트 Local을 구성한다

Design system provider는 앱 루트나 명시적인 서브트리 경계에서 `MaterialTheme`과 프로젝트 토큰을 함께 제공한다. 색상·타이포그래피·shape은 `MaterialTheme`으로, Material에 없는 간격이나 컴포넌트 정책만 프로젝트 `CompositionLocal`로 전달한다.

```kotlin
@Immutable
data class AppSpacing(val s: Dp = 8.dp, val m: Dp = 16.dp)

val LocalAppSpacing = staticCompositionLocalOf { AppSpacing() }

@Composable
fun AppDesignSystem(
    darkTheme: Boolean,
    content: @Composable () -> Unit,
) {
    val scheme = if (darkTheme) DarkColors else LightColors
    CompositionLocalProvider(LocalAppSpacing provides AppSpacing()) {
        MaterialTheme(
            colorScheme = scheme,
            typography = AppTypography,
            shapes = AppShapes,
            content = content,
        )
    }
}
```

Provider의 내부 동작과 의존 방향은 `화면 -> 의미 토큰 -> provider의 구체 값`이다. 화면이 `Color(0xFF...)`나 provider 구현을 직접 참조하면 theme 교체와 preview 격리가 어려워진다. 반대로 repository, navigator, 화면별 loading state를 Local에 넣으면 UI 환경과 비즈니스 의존성의 소유권이 섞인다.

관찰 증거는 light/dark 각각에서 동일한 probe Composable을 렌더링해 얻는다. `MaterialTheme.colorScheme`과 프로젝트 Local 값을 읽고, screenshot test는 색·shape 회귀를, Compose UI test는 의미와 동작을 맡긴다. feature preview에서도 provider 하나만 감싸면 기본값 누락을 재현할 수 있어야 한다.

`compositionLocalOf`와 `staticCompositionLocalOf`의 선택은 이름이 아니라 변경 빈도로 결정한다. 자주 바뀌는 값을 `staticCompositionLocalOf`에 넣으면 provider 하위 전체가 재구성될 수 있다.

관련 노트: [CompositionLocal은 트리 범위의 UI 환경 값을 암묵적으로 전달한다](./compositionlocal-passes-tree-scoped-ui-environment-implicitly.md), [Material 3 색상 역할은 고정된 색상이 아닌 의미적 의도를 표현한다](./material3-color-roles-express-semantic-intent-not-fixed-colors.md)

출처: [Material 3 in Compose](https://developer.android.com/develop/ui/compose/designsystems/material3), [Locally scoped data with CompositionLocal](https://developer.android.com/develop/ui/compose/compositionlocal)
