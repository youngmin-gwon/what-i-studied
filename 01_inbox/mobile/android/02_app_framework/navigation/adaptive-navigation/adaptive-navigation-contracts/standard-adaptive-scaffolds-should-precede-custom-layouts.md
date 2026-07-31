---
title: "표준 adaptive scaffold를 먼저 검토하고 custom layout은 명시적 이유가 있을 때 둔다"
tags: [android, android/navigation, android/adaptive]
aliases: ["표준 adaptive scaffold를 먼저 검토하고 custom layout은 명시적 이유가 있을 때 둔다"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# 표준 adaptive scaffold를 먼저 검토하고 custom layout은 명시적 이유가 있을 때 둔다

Material 3 Adaptive library는 navigation suite, list-detail, supporting pane 같은 표준 scaffold를 제공한다. 이들은 window size class와 posture에 맞춰 흔한 adaptive UI 문제를 이미 모델링한다.

Custom layout은 표준 scaffold가 표현하지 못하는 product-specific structure가 있을 때 선택한다. 표준 component와 같은 상태를 중복 소유하거나, window 변화마다 별도 route tree를 만들어야 한다면 custom layout의 비용을 다시 검토한다.

## 판단 기준

- top-level chrome 문제는 navigation suite scaffold로 먼저 검토한다.
- list-detail/supporting pane 문제는 canonical layout과 adaptive scaffold로 먼저 검토한다.
- custom layout은 상태 소유자, back policy, resize behavior를 문서화할 수 있을 때만 둔다.
- custom layout이 표준 scaffold와 같은 상태를 중복 관리하면 버그 비용이 커진다.

관련 노트: [Top-level destination은 adaptive navigation chrome의 단위다](01_inbox/mobile/android/02_app_framework/navigation/adaptive-navigation/adaptive-navigation-contracts/top-level-destination-owns-adaptive-navigation-chrome.md)

공식 문서: [Build adaptive navigation](https://developer.android.com/develop/adaptive-apps/guides/build-adaptive-navigation), [Adaptive do's and don'ts](https://developer.android.com/develop/adaptive-apps/guides/adaptive-dos-and-donts)
