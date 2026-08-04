---
title: desktop-windowing-readiness-is-productivity-validation
tags: ["android", "android/platforms"]
aliases: []
date modified: 2026-08-04 15:35:00 +09:00
date created: 2026-07-31 18:06:11 +09:00
---

## 데스크톱 윈도잉 준비도는 작은 화면 호환성이 아니라 생산성 검증이다

상위 문서: [데스크톱 윈도잉과 멀티태스킹 계약](./windowing-multitasking-contracts.md)

데스크톱 윈도잉 대응은 phone UI 가 깨지지 않는 수준에서 끝나지 않는다. 사용자가 키보드, 포인터, 여러 창, 넓은 정보 공간을 사용해 더 빠르게 작업할 수 있는지 검증해야 한다.

### 데스크톱 생산성 검증 매트릭스 및 구현 예시

| Verification Area | Sub-test Items | Target Quality Signal |
| :--- | :--- | :--- |
| **Window Resizing** | Extremely narrow width, low height, maximized state | Layout reflow without text truncation or floating button clipping |
| **Input Productivity** | Keyboard shortcuts (Ctrl+C, Ctrl+V, Ctrl+Z, Ctrl+S), Hover, Right-click context menu | Native desktop desktop-like UX response |
| **Multi-Tasking** | Multi-window side-by-side editing, Drag-and-drop file import | Concurrent state syncing without data collision |
| **System Insets** | Caption bar interaction, title bar drag | Zero overlap with system close/minimize/maximize buttons |

데스크톱 환경의 생산성을 높이기 위해 뷰 시스템에서는 `onProvideKeyboardShortcuts`를 오버라이드하여 키보드 단축키를 명시적으로 제공해야 하며, Compose에서는 `Modifier.onKeyEvent`를 활용한다.

```kotlin
// View 기반 생산성 입력(단축키) 제공 예시
override fun onProvideKeyboardShortcuts(
    data: MutableList<KeyboardShortcutGroup>?,
    menu: Menu?,
    deviceId: Int
) {
    val shortcutGroup = KeyboardShortcutGroup("Document Editing", listOf(
        KeyboardShortcutInfo("Save", KeyEvent.KEYCODE_S, KeyEvent.META_CTRL_ON),
        KeyboardShortcutInfo("Undo", KeyEvent.KEYCODE_Z, KeyEvent.META_CTRL_ON)
    ))
    data?.add(shortcutGroup)
    super.onProvideKeyboardShortcuts(data, menu, deviceId)
}

// Compose 기반 호버 상태 및 마우스 우클릭(컨텍스트 메뉴) 대응 예시
val interactionSource = remember { MutableInteractionSource() }
val isHovered by interactionSource.collectIsHoveredAsState()

Box(
    modifier = Modifier
        .hoverable(interactionSource)
        .background(if (isHovered) Color.LightGray else Color.Transparent)
        .pointerInput(Unit) {
            awaitPointerEventScope {
                while (true) {
                    val event = awaitPointerEvent()
                    if (event.type == PointerEventType.Press && event.button?.isSecondary == true) {
                        // 우클릭 컨텍스트 메뉴 표시 로직
                    }
                }
            }
        }
) {
    Text("Hover and Right-click Me")
}
```

### 체크 기준

- 창을 매우 좁게, 매우 넓게, 낮은 height 로 바꿔도 핵심 과업이 유지된다.
- list-detail, supporting pane, 도구 패널처럼 넓은 창에서 정보 구조가 좋아진다.
- keyboard shortcut, right click, hover, drag-drop 같은 생산성 입력이 중요한 명령에 연결된다.
- 여러 instance 에서 같은 데이터가 열릴 때 저장, 충돌, focus, notification routing 이 예측 가능하다.
- Adaptive app quality tier 와 Android resizable emulator, 실제 desktop/ChromeOS 환경 테스트를 release checklist 에 포함한다.
- caption bar 가 있는 창과 immersive 전환에서 상단 interactive UI 가 시스템 제어와 겹치지 않는다.

### 관측 가능한 증거 (Observable Evidence)

```bash
# 최상위 데스크톱 창 상태 및 윈도우 인셋 덤프 확인
adb shell dumpsys activity top | grep -E "mBounds|mWindowingMode"

# 자유 형상 윈도잉 모드 성능 및 FPS 모니터링
adb shell dumpsys gfxinfo <package_name> framestats
```

### 관련 문서

- [적응형 앱 준비도는 창, posture, 입력 테스트로 판단한다](../large-screen-contracts/adaptive-app-readiness-requires-window-posture-input-testing.md)

공식 문서: [Adaptive app quality](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality), [Support desktop windowing](https://developer.android.com/develop/adaptive-apps/guides/support-desktop-windowing)

검증일: 2026-08-03. 호환성보다 생산성 높은 Tier 1/2 과업을 목표로 하되 앱 용도에 해당하는 요구사항만 적용한다.

