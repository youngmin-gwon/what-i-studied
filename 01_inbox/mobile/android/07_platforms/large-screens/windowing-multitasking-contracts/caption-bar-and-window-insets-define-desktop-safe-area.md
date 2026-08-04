---
title: caption-bar-and-window-insets-define-desktop-safe-area
tags: ["android", "android/platforms"]
aliases: []
date modified: 2026-08-04 15:35:00 +09:00
date created: 2026-07-31 18:06:11 +09:00
---

## Caption bar 와 window inset 은 데스크톱 UI 의 안전 영역이다

상위 문서: [데스크톱 윈도잉과 멀티태스킹 계약](./windowing-multitasking-contracts.md)

Desktop windowing 의 창 상단에는 시스템이 그리는 caption bar 와 창 제어 영역이 있다. immersive mode 에서도 이 영역은 사라진다고 가정할 수 없고, 앱 UI 는 inset 과 system gesture 영역을 기준으로 안전하게 배치되어야 한다.

### Insets 및 Android 15 `getBoundingRects()` 매커니즘

```kotlin
@Composable
fun DesktopHeaderContent() {
    val insets = WindowInsets.captionBar.asPaddingValues()
    
    Box(
        modifier = Modifier
            .fillMaxWidth()
            .padding(insets)
    ) {
        // Caption bar 높이만큼 상단 여백이 적용된 헤더 UI
        Text("Desktop Safe Header Area")
    }
}

// View-based Android 15 (API 35) Bounding Rect Exclusion
fun applyCaptionBarExclusion(view: View) {
    ViewCompat.setOnApplyWindowInsetsListener(view) { v, insets ->
        val captionInsets = insets.getInsets(WindowInsetsCompat.Type.captionBar())
        val rects = insets.toWindowInsets()?.getBoundingRects(WindowInsetsCompat.Type.captionBar())
        // 시스템 버튼(닫기/최대화) 영역 제외 계산 적용
        insets
    }
}
```

### 실무 규칙

- caption bar 가 보일 때 콘텐츠가 닫기, 최대화, 드래그 영역과 겹치지 않게 한다.
- custom header 를 그릴 때도 시스템의 interactive caption element 는 시스템이 소유한다는 점을 전제로 둔다.
- `WindowInsets.captionBar` 와 caption bar visibility 로 영역을 계산하고 높이를 하드코딩하지 않는다.
- Android 15(API 35)의 `WindowInsets.getBoundingRects()` 로 닫기와 최대화 같은 시스템 요소의 점유 영역을 제외한다.
- 탭, 검색창처럼 상단 interactive UI 를 둘 때 `setSystemGestureExclusionRects()` 가 필요한지 별도로 판단한다.

### 관측 가능한 증거 (Observable Evidence)

```bash
# 윈도우 인셋 덤프에서 captionBar 및 inset bounds 관측
adb shell dumpsys window windows | grep -A 10 "mCaptionInsets"

# Insets 변경 이벤트 로그 확인
adb logcat -v threadtime | grep -E "InsetsController|onApplyWindowInsets"
```

### 관련 문서

- [데스크톱 윈도잉에서는 앱 창이 자유롭게 변한다](./desktop-windowing-makes-android-app-window-freeform.md)
- [적응형 레이아웃은 같은 화면을 늘리는 것이 아니라 구조를 바꾼다](../large-screen-contracts/adaptive-layout-changes-structure-not-scale.md)

공식 문서: [Support desktop windowing](https://developer.android.com/develop/adaptive-apps/guides/support-desktop-windowing)

검증일: 2026-08-03. immersive mode 에서도 desktop header bar 가 존재할 수 있고 시스템 interactive caption element 는 계속 시스템이 그린다.

