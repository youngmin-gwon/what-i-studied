---
title: adaptive-navigation-contracts
tags: [android, android/adaptive, android/navigation]
aliases: ["Adaptive Navigation 계약"]
date modified: 2026-08-03 18:11:15 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Adaptive Navigation 계약

Adaptive Navigation 은 화면 크기와 입력 환경에 따라 app chrome 과 content 배치를 바꾸는 문제다. Navigation 3 의 back stack 상태와 adaptive scaffold 의 표시 정책을 분리해서 읽는다.

### 정본 노트

- [Adaptive navigation은 device type이 아니라 현재 window와 posture로 결정한다](./adaptive-navigation-is-driven-by-window-and-posture.md)
- [Top-level destination은 adaptive navigation chrome의 단위다](./top-level-destination-owns-adaptive-navigation-chrome.md)
- [Pane layout은 선택 상태와 back policy를 분리해 보존해야 한다](./pane-layout-preserves-selection-and-back-policy.md)
- [표준 adaptive scaffold를 먼저 검토하고 custom layout은 명시적 이유가 있을 때 둔다](./standard-adaptive-scaffolds-should-precede-custom-layouts.md)
- [Navigation 3 Scene과 adaptive scaffold는 서로 다른 레이아웃 문제를 푼다](./navigation3-scenes-and-adaptive-scaffolds-solve-different-layout-problems.md)

### 판단 기준

- route/back stack 은 앱 navigation state 가 소유하고, chrome 과 pane 배치는 window state 가 결정한다.
- compact/expanded 전환은 같은 목적지를 다른 배치로 표현해야 하며 다른 route 체계로 갈라지면 안 된다.
- 표준 Material adaptive scaffold 가 해결하는 문제인지 먼저 확인한 뒤 custom layout 을 선택한다.

관련 지도: [Android Navigation 진입 계약](../../navigation-contracts/navigation-contracts.md), [Navigation 3 계약](../../navigation3/navigation3-contracts/navigation3-contracts.md)
