---
title: "Adaptive navigation은 device type이 아니라 현재 window와 posture로 결정한다"
tags: [android, android/navigation, android/adaptive]
aliases: ["Adaptive navigation은 device type이 아니라 현재 window와 posture로 결정한다"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# Adaptive navigation은 device type이 아니라 현재 window와 posture로 결정한다

Adaptive navigation은 phone/tablet 같은 device label보다 현재 app window의 크기, posture, resizability, multi-window 상태를 기준으로 판단한다. 같은 device라도 window가 줄어들면 compact navigation이 필요할 수 있다.

Android large screen 환경에서는 orientation, aspect ratio, resizability 제한에 기대는 설계가 약하다. navigation chrome과 content layout은 runtime window 변화에 대응해야 한다.

## 판단 기준

- device model 대신 window size class, posture, hinge/fold 상태, input availability를 본다.
- 같은 destination이라도 compact에서는 single pane, expanded에서는 list-detail pane으로 표시될 수 있다.
- window 변화가 route key나 selected destination의 의미를 바꾸면 안 된다.
- phone/tablet 분기보다 app window와 posture 기반 분기를 우선한다.

관련 노트: [Large screen contracts](01_inbox/mobile/android/07_platforms/large-screens/large-screen-contracts/large-screen-contracts.md), [Pane layout은 선택 상태와 back policy를 분리해 보존해야 한다](01_inbox/mobile/android/02_app_framework/navigation/adaptive-navigation/adaptive-navigation-contracts/pane-layout-preserves-selection-and-back-policy.md)

공식 문서: [Get started with adaptive apps](https://developer.android.com/develop/adaptive-apps/guides/get-started-with-adaptive-apps), [Adaptive do's and don'ts](https://developer.android.com/develop/adaptive-apps/guides/adaptive-dos-and-donts)
