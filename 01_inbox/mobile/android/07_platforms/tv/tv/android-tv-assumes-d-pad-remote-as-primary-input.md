---
title: android-tv-assumes-d-pad-remote-as-primary-input
tags: ["android", "android/platforms"]
aliases: []
date modified: 2026-08-04 15:35:00 +09:00
date created: 2026-08-03 17:26:50 +09:00
---

## Android TV 는 d-pad/리모컨을 1 차 입력으로 가정한다

상위 문서: [Android 폼 팩터와 플랫폼 확장 지도](../../android-platforms-and-form-factors.md)

관련 지도: [Android TV 계약](./tv.md)

### 핵심 정의

Android TV 기기는 터치스크린이 없는 것을 기본 전제로 한다. 사용자는 리모컨의 방향키(d-pad)와 확인/뒤로 버튼으로만 화면을 조작하며, 일부 기기에 마우스나 터치패드형 리모컨이 있어도 이는 보조 입력이다. 앱은 모든 클릭 가능한 요소를 d-pad 만으로 도달 가능하게 설계해야 한다.

### D-Pad 입력 전달 메커니즘 및 명시적 Focus 연결

d-pad 입력은 `KeyEvent`(`KEYCODE_DPAD_UP/DOWN/LEFT/RIGHT/CENTER`)로 전달된다. View 시스템은 방향키 입력에 따라 포커스를 다음 뷰로 옮기는 기본 알고리즘(뷰의 기하학적 위치 기반)을 갖는다. 복잡한 커스텀 UI에서는 `FocusRequester` 및 `focusProperties` 로 포커스 이동을 명시적으로 제어한다.

```kotlin
@Composable
fun TvFocusNavigationExample() {
    val (item1, item2, item3) = remember { FocusRequester.createRefs() }

    Row {
        Button(
            onClick = { },
            modifier = Modifier
                .focusRequester(item1)
                .focusProperties { right = item2 }
        ) { Text("Item 1") }

        Button(
            onClick = { },
            modifier = Modifier
                .focusRequester(item2)
                .focusProperties { left = item1; right = item3 }
        ) { Text("Item 2") }
    }
}
```

### 판단 기준

- 화면의 모든 상호작용 가능한 요소가 d-pad 만으로 도달 가능한지 방향키만으로 앱을 조작하는 테스트를 반드시 거친다.
- 제스처(스와이프, 핀치 줌) 기반 UI 를 TV 로 그대로 이식하지 않는다. 대응하는 d-pad 조작(좌우 이동, 확인 버튼)으로 재설계해야 한다.
- 터치 기반 시각적 피드백(리플 효과 등)보다 포커스 상태(테두리 강조, 스케일 변화)가 더 중요한 시각 신호다. 포커스가 어디 있는지 항상 명확히 보여야 한다.

### 경계

- 이 노트는 입력 모델까지 다룬다. 화면 레이아웃과 포커스 탐색 패턴 자체는 [10-foot UI는 포커스 기반 탐색을 요구한다](./10-foot-ui-requires-focus-based-navigation.md) 가 다룬다.
- 리모컨 이외의 물리 입력 장치(게임패드 등)에 대한 일반 모델은 `04_system_services/device-capabilities/input-accessibility-contracts` 가 다룬다.

### 관측 가능한 증거 (Observable Evidence)

```bash
# 1. D-Pad Keyevent 명령을 ADB로 송신하여 앱 포커스 이동 시뮬레이션
adb shell input keyevent KEYCODE_DPAD_DOWN
adb shell input keyevent KEYCODE_DPAD_RIGHT
adb shell input keyevent KEYCODE_DPAD_CENTER

# 2. D-Pad 입력 이벤트 로깅 모니터링
adb shell dumpsys input | grep -E "EventHub|Focus"
```

### 공식 문서

- https://developer.android.com/training/tv/start/start
- https://developer.android.com/training/tv/start/navigation

