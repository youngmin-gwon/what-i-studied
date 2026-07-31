# Sizing Strategy

상위 노트: [adaptive-layout-and-navigation](01_inbox/mobile/android/02_app_framework/navigation/adaptive-navigation/adaptive-layout-and-navigation.md)

### 3.1 Window Size Classes

`WindowSizeClass`는 window 크기를 몇 개의 breakpoint로 분류해 layout 결정을 단순화합니다.

공식 문서 기준 width class:

| Class | 기준 | 대표 상황 |
|:---|:---|:---|
| Compact | `< 600dp` | phone portrait |
| Medium | `600dp <= width < 840dp` | tablet portrait, unfolded foldable portrait |
| Expanded | `840dp <= width < 1200dp` | tablet landscape, unfolded foldable landscape |
| Large | `1200dp <= width < 1600dp` | large tablet |
| Extra large | `>= 1600dp` | desktop / large connected display |

height class도 별도로 존재합니다. 대부분의 일반 화면은 width가 더 중요하지만, landscape phone이나 tabletop posture처럼 height가 작아지는 상황에서는 height도 고려해야 합니다.

Compose에서는 `currentWindowAdaptiveInfo()`를 사용해 현재 adaptive 정보를 얻습니다.

```kotlin
val adaptiveInfo = currentWindowAdaptiveInfo(
    supportLargeAndXLargeWidth = true,
)
val windowSizeClass = adaptiveInfo.windowSizeClass
```

관련 문서:

- [Use window size classes](https://developer.android.com/develop/adaptive-apps/guides/use-window-size-classes)

### 3.2 mediaQuery

`mediaQuery`는 Compose에서 현재 window 조건을 선언적으로 질의하는 sizing strategy입니다.

`WindowSizeClass`가 고수준 breakpoint 중심이라면, `mediaQuery`는 layout 내부에서 특정 조건에 맞춰 더 세밀한 분기를 만들 때 유용합니다.

관련 문서:

- [Query information for adaptive layouts with mediaQuery](https://developer.android.com/develop/adaptive-apps/guides/mediaquery)

---
