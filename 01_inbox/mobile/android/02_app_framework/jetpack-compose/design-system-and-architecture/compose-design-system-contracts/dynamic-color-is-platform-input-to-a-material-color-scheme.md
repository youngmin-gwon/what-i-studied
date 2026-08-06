---
title: dynamic-color-is-platform-input-to-a-material-color-scheme
tags: [android, compose/design-system, jetpack-compose]
aliases: [Dynamic color, Material You]
date modified: 2026-08-06 14:40:00 +09:00
date created: 2026-07-31 23:59:30 +09:00
---

## Dynamic Color는 Material ColorScheme에 대한 플랫폼 입력이다

Dynamic color는 Android 12(API 31) 이상에서 시스템 색상을 `ColorScheme`으로 만드는 선택지다. 화면이 wallpaper 색을 직접 읽는 기능이 아니다. 테마 경계가 API 수준·사용자 설정·dark mode를 판단하고, 하위 컴포넌트는 semantic color role만 소비한다.

```kotlin
@Composable
fun AppTheme(
    useDynamicColor: Boolean,
    darkTheme: Boolean = isSystemInDarkTheme(),
    content: @Composable () -> Unit,
) {
    val context = LocalContext.current
    val colors = when {
        useDynamicColor && Build.VERSION.SDK_INT >= Build.VERSION_CODES.S ->
            if (darkTheme) dynamicDarkColorScheme(context)
            else dynamicLightColorScheme(context)
        darkTheme -> AppDarkColorScheme
        else -> AppLightColorScheme
    }
    MaterialTheme(colorScheme = colors, content = content)
}
```

선택 메커니즘은 `사용 설정 -> API 31 여부 -> light/dark dynamic scheme -> 브랜드 fallback`이다. 이 경계를 한곳에 두면 일반 화면은 `MaterialTheme.colorScheme.primaryContainer`처럼 의미를 유지하고, dynamic color를 꺼도 컴포넌트 코드는 바뀌지 않는다.

관찰 증거는 API 30과 API 31+ 에뮬레이터, light/dark, dynamic on/off의 최소 8개 조합에서 남긴다. Screenshot diff로 scheme 전환을 확인하고, 텍스트·아이콘 대비는 실제 렌더링 결과에 접근성 검사를 적용한다. Glance, notification 같은 원격 surface는 Compose theme이 자동 전파되지 않으므로 별도 계약으로 다룬다.

관련 노트: [Material 3 색상 역할은 고정된 색상이 아닌 의미적 의도를 표현한다](./material3-color-roles-express-semantic-intent-not-fixed-colors.md), [Glance는 Compose UI가 아니라 RemoteViews 위젯 경계로 렌더링한다](../../../app-widgets/app-widget-contracts/glance-renders-app-widgets-through-remoteviews-not-compose-ui.md)

출처: [Material 3 in Compose](https://developer.android.com/develop/ui/compose/designsystems/material3)
