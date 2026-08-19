---
title: window-size-class-classifies-app-window-not-device-type
tags: ["android", "android/platforms"]
aliases: []
date modified: 2026-08-04 15:35:00 +09:00
date created: 2026-07-31 18:06:11 +09:00
---

## 창 크기 클래스는 기기 종류가 아니라 앱 창을 분류한다

상위 문서: [큰 화면 적응 계약](./large-screen.md)

Window size class 는 태블릿인지, 폴더블인지, ChromeOS 인지 판별하는 값이 아니다. 앱에 실제로 주어진 window bounds 를 compact, medium, expanded, large, extra-large 같은 크기 구간으로 해석하는 기준이다.

### 왜 중요한가

같은 기기에서도 분할 화면, 자유 크기 조절, 접힘/펼침, 외부 디스플레이 연결에 따라 앱 창은 계속 바뀐다. `isTablet` 같은 분기는 큰 화면에서 가장 먼저 깨지는 추상화다.

### 메커니즘 및 코드 구현 (Compose Material3 Adaptive)

```kotlin
@Composable
fun AdaptiveAppContent(
    adaptiveInfo: WindowAdaptiveInfo = currentWindowAdaptiveInfo()
) {
    val widthClass = adaptiveInfo.windowSizeClass.windowWidthSizeClass
    val heightClass = adaptiveInfo.windowSizeClass.windowHeightSizeClass

    when (widthClass) {
        WindowWidthSizeClass.COMPACT -> {
            // Mobile Portrait / Split View (< 600dp)
            SinglePaneLayout()
        }
        WindowWidthSizeClass.MEDIUM -> {
            // Small Tablet / Foldable Unfolded (600dp ..< 840dp)
            FlexiblePaneLayout()
        }
        WindowWidthSizeClass.EXPANDED,
        WindowWidthSizeClass.LARGE,
        WindowWidthSizeClass.EXTRA_LARGE -> {
            // Large Tablet / Desktop Multi-window (>= 840dp)
            TwoPaneLayout()
        }
    }
}
```

### 실무 규칙

- 레이아웃 전환은 물리 기기명이 아니라 현재 앱 창 크기와 비율을 기준으로 결정한다.
- 대부분의 화면은 width class 를 중심으로 설계하되, 낮은 height 에서는 two-pane 이 부적절할 수 있다.
- Compose 에서는 Material 3 Adaptive 의 `currentWindowAdaptiveInfo()` 를 우선 고려한다. large 와 extra-large width 구간을 사용할 때는 현재 API 의 `supportLargeAndXLargeWidth = true` 조건을 함께 확인한다.
- Views 기반 화면은 현재 window metrics 를 기준으로 계산하고 deprecated `Display` 크기 API 에 기대지 않는다.

### 기준과 경계

- width 는 compact `<600dp`, medium `600..<840dp`, expanded `840..<1200dp`, large `1200..<1600dp`, extra-large `>=1600dp` 다.
- height 는 별도로 compact `<480dp`, medium `480..<900dp`, expanded `>=900dp` 로 분류한다.
- breakpoint 는 고수준 레이아웃 결정의 출발점이지 모든 컴포넌트의 고정 분기표가 아니다. 실제 콘텐츠 제약과 posture 를 추가로 적용한다.

### 관측 가능한 증거 (Observable Evidence)

```bash
# 디바이스 윈도우 Bounds 및 현재 Configuration 모니터링
adb shell dumpsys window displays | grep -E "mAppWidth|mAppHeight|mBounds"

# Logcat에서 Activity Configuration Change 관측
adb logcat -v threadtime | grep -E "ComponentActivity|onConfigurationChanged"
```

### 관련 문서

- [적응형 레이아웃은 같은 화면을 늘리는 것이 아니라 구조를 바꾼다](./adaptive-layout-changes-structure-not-scale.md)

공식 문서: [Use window size classes](https://developer.android.com/develop/adaptive-apps/guides/use-window-size-classes), [Adaptive do's and don'ts](https://developer.android.com/develop/adaptive-apps/guides/adaptive-dos-and-donts)

검증일: 2026-08-03. breakpoint 와 `currentWindowAdaptiveInfo()` 옵션은 Material 3 Adaptive 업데이트에 따라 다시 확인한다.
