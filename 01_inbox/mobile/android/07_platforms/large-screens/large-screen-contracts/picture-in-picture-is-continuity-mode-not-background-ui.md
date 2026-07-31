---
title: "PiP는 백그라운드 UI가 아니라 연속 시청을 위한 멀티윈도우 모드다"
tags: ["android", "android/platforms"]
---

# PiP는 백그라운드 UI가 아니라 연속 시청을 위한 멀티윈도우 모드다

상위 문서: [큰 화면 적응 계약](01_inbox/mobile/android/07_platforms/large-screens/large-screen-contracts/large-screen-contracts.md)

Picture-in-Picture는 앱을 항상 위에 띄우는 임의의 overlay가 아니다. Android가 제공하는 특수 multi-window 모드이며 주로 동영상, 영상 통화, 내비게이션처럼 사용자가 다른 작업 중에도 계속 봐야 하는 activity에 적용한다.

## 실무 규칙

- PiP를 지원할 activity는 manifest에 명시하고 PiP 전환 중 configuration change를 처리한다.
- PiP 진입 후에는 재생이나 안내처럼 본질적인 콘텐츠만 남기고 일반 UI chrome은 숨긴다.
- system alert window로 PiP 유사 경험을 만들지 않는다.
- PiP action은 작은 창에서도 의미가 분명한 최소 조작만 제공한다.
- Compose 화면도 activity lifecycle과 media/session 상태를 기준으로 PiP 전환을 설계한다.

## 관련 문서

- [데스크톱 윈도잉에서는 앱 창이 자유롭게 변한다](01_inbox/mobile/android/07_platforms/large-screens/windowing-multitasking-contracts/desktop-windowing-makes-android-app-window-freeform.md)
- [적응형 앱 준비도는 창, posture, 입력 테스트로 판단한다](01_inbox/mobile/android/07_platforms/large-screens/large-screen-contracts/adaptive-app-readiness-requires-window-posture-input-testing.md)

공식 문서: [Use picture-in-picture](https://developer.android.com/develop/ui/views/picture-in-picture)
