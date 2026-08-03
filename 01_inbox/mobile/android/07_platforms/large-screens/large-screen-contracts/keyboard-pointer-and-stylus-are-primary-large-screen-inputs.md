---
title: keyboard-pointer-and-stylus-are-primary-large-screen-inputs
tags: ["android", "android/platforms"]
aliases: []
date modified: 2026-08-03 18:15:33 +09:00
date created: 2026-07-31 18:06:11 +09:00
---

## 키보드, 포인터, 스타일러스는 큰 화면의 기본 입력이다

상위 문서: [큰 화면 적응 계약](01_inbox/mobile/android/07_platforms/large-screens/large-screen-contracts/large-screen-contracts.md)

큰 화면 앱은 터치만 잘 되는 앱이 아니다. 태블릿, 폴더블, ChromeOS, desktop windowing 에서는 키보드, 마우스, 트랙패드, 스타일러스가 기본 입력 경로가 된다.

### 실무 규칙

- Tab, arrow, Enter, Space 같은 기본 keyboard navigation 과 activation 을 검증한다.
- undo, copy, paste, save 같은 플랫폼 관용 shortcut 을 지원하거나 의도적으로 비워 둔 이유를 정한다.
- hover, right click, scroll wheel, trackpad scroll 같은 pointer 동작을 custom component 에서도 처리한다.
- framework 와 Material component 가 제공하는 기본 keyboard/pointer 동작을 우선 사용하되, custom component 와 복잡한 화면의 focus order 는 직접 검증한다.
- 스타일러스 입력은 필기, 그림, 선택, text field 입력 같은 사용 맥락을 분리해 테스트한다.

### 관련 문서

- [드래그 앤 드롭은 창 사이 데이터 이동 계약이다](01_inbox/mobile/android/07_platforms/large-screens/large-screen-contracts/drag-and-drop-is-cross-window-data-contract.md)
- [적응형 앱 준비도는 창, posture, 입력 테스트로 판단한다](01_inbox/mobile/android/07_platforms/large-screens/large-screen-contracts/adaptive-app-readiness-requires-window-posture-input-testing.md)

공식 문서: [Input compatibility on large screens](https://developer.android.com/develop/ui/views/touch-and-input/input-compatibility-on-large-screens), [Get started with adaptive apps](https://developer.android.com/develop/adaptive-apps/guides/get-started-with-adaptive-apps)

검증일: 2026-08-03. 특정 Compose 버전만으로 입력 지원 완료를 추론하지 않고 실제 focus, shortcut, hover, scroll, stylus 과업을 테스트한다.
