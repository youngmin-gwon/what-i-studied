---
title: Modern Android UI는 edge-to-edge, insets, back, adaptive layout을 함께 다룬다
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-03 16:35:57 +09:00
date created: 2026-07-31 23:38:40 +09:00
---

# Modern Android UI는 edge-to-edge, insets, back, adaptive layout을 함께 다룬다

현대 Android UI 는 화면 컴포넌트만 잘 배치하는 것으로 끝나지 않는다. system bars 뒤로 그리는 edge-to-edge, 겹침을 피하는 insets, predictive back, window size 와 posture 에 따른 adaptive navigation 을 함께 설계해야 한다.

target SDK 35 이상 앱은 Android 15 이상 기기에서 edge-to-edge 표시가 적용되므로 tappable UI 와 scrolling content 가 system bars 나 gesture 영역과 충돌하지 않게 insets 를 처리해야 한다.

Back 동작은 단순히 `onBackPressed` 를 가로채는 방식에서 벗어나야 한다. Navigation stack, transition, predictive back progress 가 같은 상태를 기준으로 움직여야 사용자가 뒤로 가기 결과를 예측할 수 있다.

큰 화면과 foldable 에서는 device 이름보다 현재 window 와 posture 가 중요하다. top-level destination 의 chrome 은 compact 에서는 bottom bar, expanded 에서는 rail 이나 drawer 처럼 바뀔 수 있고, pane layout 은 selection 과 back policy 를 함께 보존해야 한다.

관련 노트: [Navigation 3 transition과 predictive back은 같은 stack state를 기준으로 해야 한다](01_inbox/mobile/android/02_app_framework/navigation/navigation3/navigation3-contracts/navigation3-transition-and-back-policy-must-share-stack-state.md), [Window와 posture가 Adaptive Navigation의 입력이다](01_inbox/mobile/android/02_app_framework/navigation/adaptive-navigation/adaptive-navigation-contracts/adaptive-navigation-is-driven-by-window-and-posture.md)

공식 문서: [Edge-to-edge in views](https://developer.android.com/develop/ui/views/layout/edge-to-edge), [Predictive back](https://developer.android.com/guide/navigation/custom-back/predictive-back-gesture), [Build adaptive navigation](https://developer.android.com/develop/adaptive-apps/guides/build-adaptive-navigation)
