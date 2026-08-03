---
title: "ChromeOS 입력은 마우스/트랙패드/키보드를 우선하고 터치는 보조 입력이다"
tags: ["android", "android/platforms"]
---

# ChromeOS 입력은 마우스/트랙패드/키보드를 우선하고 터치는 보조 입력이다

상위 문서: [Android 폼 팩터와 플랫폼 확장 지도](01_inbox/mobile/android/07_platforms/android-platforms-and-form-factors.md)
관련 지도: [ChromeOS 고유 계약](01_inbox/mobile/android/07_platforms/chromeos/chromeos-contracts/chromeos-contracts.md)

## 핵심 정의

대부분의 Chromebook은 터치스크린이 없거나, 있어도 트랙패드/키보드가 주된 입력 수단이다. 휴대폰에서 터치 제스처(길게 누르기로 컨텍스트 메뉴 열기 등)로만 접근 가능하게 설계된 기능은 ChromeOS에서 마우스 우클릭이나 키보드 단축키로도 도달 가능해야 한다.

## 메커니즘

ChromeOS에서 Android 앱은 마우스 이벤트를 `MotionEvent`의 마우스 소스 타입으로, 트랙패드 제스처를 스크롤/포인터 이동으로, 키보드 입력을 일반 `KeyEvent`로 받는다. 우클릭은 시스템이 `ACTION_BUTTON_PRESS`(보조 버튼)로 전달하며, 앱이 이를 별도로 처리하지 않으면 롱프레스로만 열리던 컨텍스트 메뉴가 마우스 사용자에게는 노출되지 않는다. 포인터가 화면 위에 머무는 hover 상태도 터치에는 없는 개념이라 마우스 환경에서만 발생하는 이벤트다.

## 판단 기준

- 롱프레스 전용 인터랙션(컨텍스트 메뉴, 드래그 시작)에는 마우스 우클릭이나 명시적 버튼 같은 대체 경로를 함께 제공한다.
- 텍스트 편집, 탐색이 잦은 화면에는 키보드 단축키(복사/붙여넣기, 탭 이동 등)를 지원해 트랙패드/키보드만으로도 생산성 있게 쓸 수 있게 한다.
- hover 상태를 활용한 시각적 피드백(버튼 강조 등)을 추가하면 데스크톱 사용자에게 더 익숙한 경험을 주지만, 터치 전용 기기에서는 이 이벤트 자체가 발생하지 않는다는 점을 감안해 hover 없이도 기능이 동작하도록 유지한다.

## 경계

- 이 노트는 입력 우선순위 차이를 다룬다. 창 크기/레이아웃 적응은 `07_platforms/large-screens/large-screen-contracts`가, 실행 환경 자체는 [ChromeOS는 Android 앱을 컨테이너에서 실행하고 창을 데스크톱 윈도우로 매핑한다](01_inbox/mobile/android/07_platforms/chromeos/chromeos-contracts/chromeos-runs-android-apps-in-a-container-mapped-to-desktop-windows.md)가 다룬다.
- 물리 입력 장치의 일반 추상화 모델(InputDevice, 소스 타입)은 `04_system_services/device-capabilities/input-accessibility-contracts`가 다룬다.

## 관찰 가능한 신호

Chromebook 실기기나 ChromeOS 에뮬레이터에서 마우스 우클릭, 트랙패드 스크롤, 키보드 Tab 키만으로 앱의 모든 상호작용 요소에 도달 가능한지 직접 조작해 확인한다.

## 공식 문서

- https://developer.android.com/topic/arc
- https://developer.android.com/develop/ui/views/touch-and-input/game-controllers/controller-input
