---
title: chromeos-input-prioritizes-mouse-trackpad-and-keyboard-over-touch
tags: ["android", "android/platforms"]
aliases: []
date modified: 2026-08-04 15:35:00 +09:00
date created: 2026-08-03 17:30:25 +09:00
---

## ChromeOS 입력은 마우스/트랙패드/키보드를 우선하고 터치는 보조 입력이다

상위 문서: [Android 폼 팩터와 플랫폼 확장 지도](../../android-platforms-and-form-factors.md)

관련 지도: [ChromeOS 고유 계약](./chromeos-contracts.md)

### 핵심 정의

대부분의 Chromebook 은 터치스크린이 없거나, 있어도 트랙패드/키보드가 주된 입력 수단이다. 휴대폰에서 터치 제스처(길게 누르기로 컨텍스트 메뉴 열기 등)로만 접근 가능하게 설계된 기능은 ChromeOS 에서 마우스 우클릭이나 키보드 단축키로도 도달 가능해야 한다.

### 마우스 우클릭 및 Hover 이벤트 처리 메커니즘

ChromeOS 에이전트는 마우스 우클릭을 `MotionEvent.BUTTON_SECONDARY` 로 전달한다. Compose 및 View 에서는 이 이벤트를 감지해 데스크톱 마우스에 호환되는 컨텍스트 메뉴를 띄운다.

```kotlin
// View-based Context Menu / Mouse Right Click handling
override fun onGenericMotionEvent(event: MotionEvent): Boolean {
    if (event.isFromSource(InputDevice.SOURCE_MOUSE)) {
        if (event.action == MotionEvent.ACTION_BUTTON_PRESS &&
            event.actionButton == MotionEvent.BUTTON_SECONDARY
        ) {
            // 마우스 우클릭 감지 -> 팝업 메뉴 표시
            showContextMenu(event.x, event.y)
            return true
        }
    }
    return super.onGenericMotionEvent(event)
}
```

```kotlin
// Compose Mouse Hover & Shortcut handling
@Composable
fun ChromebookInteractiveElement() {
    var isHovered by remember { mutableStateOf(false) }

    Box(
        modifier = Modifier
            .pointerInput(Unit) {
                awaitPointerEventScope {
                    while (true) {
                        val event = awaitPointerEvent()
                        if (event.type == PointerEventType.Enter) isHovered = true
                        if (event.type == PointerEventType.Exit) isHovered = false
                    }
                }
            }
            .background(if (isHovered) Color.LightGray else Color.White)
    ) {
        Text("Desktop Interactive Item")
    }
}
```

### 판단 기준

- 롱프레스 전용 인터랙션(컨텍스트 메뉴, 드래그 시작)에는 마우스 우클릭이나 명시적 버튼 같은 대체 경로를 함께 제공한다.
- 텍스트 편집, 탐색이 잦은 화면에는 키보드 단축키(복사/붙여넣기, 탭 이동 등)를 지원해 트랙패드/키보드만으로도 생산성 있게 쓸 수 있게 한다.
- hover 상태를 활용한 시각적 피드백(버튼 강조 등)을 추가하면 데스크톱 사용자에게 더 익숙한 경험을 주지만, 터치 전용 기기에서는 이 이벤트 자체가 발생하지 않는다는 점을 감안해 hover 없이도 기능이 동작하도록 유지한다.

### 경계

- 이 노트는 입력 우선순위 차이를 다룬다. 창 크기/레이아웃 적응은 `07_platforms/large-screens/large-screen-contracts` 가, 실행 환경 자체는 [ChromeOS는 Android 앱을 컨테이너에서 실행하고 창을 데스크톱 윈도우로 매핑한다](./chromeos-runs-android-apps-in-a-container-mapped-to-desktop-windows.md) 가 다룬다.
- 물리 입력 장치의 일반 추상화 모델(InputDevice, 소스 타입)은 `04_system_services/device-capabilities/input-accessibility-contracts` 가 다룬다.

### 관측 가능한 증거 (Observable Evidence)

```bash
# 1. 마우스 및 포인터 입력 디바이스 이벤트 로깅
adb shell dumpsys input | grep -E "PointerController|Mouse|SOURCE_MOUSE"

# 2. 키보드 및 포인터 호버 이벤트 실시간 수신 로그
adb logcat -v threadtime | grep -E "GenericMotionEvent|PointerEventType"
```

### 공식 문서

- https://developer.android.com/topic/arc
- https://developer.android.com/develop/ui/views/touch-and-input/game-controllers/controller-input

