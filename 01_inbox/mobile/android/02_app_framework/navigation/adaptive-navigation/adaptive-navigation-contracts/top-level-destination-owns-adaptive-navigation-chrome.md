---
title: "Top-level destination은 adaptive navigation chrome의 단위다"
tags: [android, android/navigation, android/adaptive]
aliases: ["Top-level destination은 adaptive navigation chrome의 단위다"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# Top-level destination은 adaptive navigation chrome의 단위다

Top-level destination은 bottom bar, navigation rail, drawer 같은 app chrome에 노출되는 가장 큰 이동 단위다. Adaptive UI에서는 chrome 모양이 window 조건에 따라 바뀌어도 선택된 destination의 의미는 그대로 유지되어야 한다.

Compact window에서는 navigation bar가 자연스럽고, expanded window에서는 rail이나 drawer가 더 적합할 수 있다. 하지만 chrome 전환이 각 destination의 back stack을 초기화하거나 route 의미를 바꾸면 안 된다.

## 판단 기준

- top-level destination은 feature root 또는 앱의 주요 업무 단위로 제한한다.
- window 변화는 chrome component를 바꾸지만 selected destination은 유지한다.
- 각 top-level destination의 내부 stack을 보존할지 초기화할지 명시한다.
- detail screen을 무리하게 top-level destination으로 올리지 않는다.

관련 노트: [Navigation 3 back stack은 저장 가능한 navigation state로 복원해야 한다](01_inbox/mobile/android/02_app_framework/navigation/navigation3/navigation3-contracts/navigation3-back-stack-needs-saveable-restoration.md)

공식 문서: [Build adaptive navigation](https://developer.android.com/develop/adaptive-apps/guides/build-adaptive-navigation)
