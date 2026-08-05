---
title: adaptive-navigation-contracts
tags: [android, android/adaptive, android/navigation]
aliases: ["Adaptive Navigation 계약", "Adaptive Navigation Contracts"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Adaptive Navigation 계약 (Adaptive Navigation Contracts)

Adaptive Navigation을 설계할 때 앱 내 탐색 상태(`NavBackStack`), UI 크롬(Navigation Chrome), 화면 구획(Pane Scaffolds) 간의 책임을 명확히 규정하는 핵심 계약 모음이다.

---

### 계약 체계 개요 (What & Why)

1. **상태와 배치의 분리 계약 (Separation of State and Layout)**:
   - 탐색 백스택(`NavBackStack`) 및 목적지(`NavKey`)는 **앱 탐색 상태(Navigation State)**가 소유한다.
   - 탐색 크롬(Navigation Rail/Bar)과 패널 배치(Single/Dual Pane)는 **윈도우 상태(`WindowAdaptiveInfo`)**가 결정한다.
   - 창 크기가 좁아지거나 넓어져도 목적지 키(`NavKey`)의 의미와 백스택 구조는 훼손되지 않아야 한다.
2. **크롬 소유권 계약 (Top-level Navigation Chrome)**:
   - 하단 바, 내비게이션 레일, 드로어 등의 안드로이드 앱 프레임 크롬은 최상위 목적지(Top-level Destination) 단위로 통제되며, 크롬 전환 시 개별 탭의 내부 백스택 상태가 초기화되지 않는다.
3. **표준 Scaffold 우선 계약 (Standard Scaffold Precedence)**:
   - 커스텀 `Row`/`Column` 및 하드코딩된 Width 분기 대신 Material 3 표준 Adaptive Scaffold(`NavigationSuiteScaffold`, `ListDetailPaneScaffold`)를 최우선 적용한다.

---

### 하위 세부 계약 항목

- [Adaptive navigation은 device type이 아니라 현재 window와 posture로 결정한다](adaptive-navigation-is-driven-by-window-and-posture.md)
- [Top-level destination은 adaptive navigation chrome의 단위다](top-level-destination-owns-adaptive-navigation-chrome.md)
- [표준 adaptive scaffold를 먼저 검토하고 custom layout은 명시적 이유가 있을 때 둔다](standard-adaptive-scaffolds-should-precede-custom-layouts.md)
- [Pane layout은 선택 상태와 back policy를 분리해 보존해야 한다](pane-layout-preserves-selection-and-back-policy.md)
- [Navigation 3 Scene과 adaptive scaffold는 서로 다른 레이아웃 문제를 푼다](navigation3-scenes-and-adaptive-scaffolds-solve-different-layout-problems.md)

---

### 상위 및 연관 지도

- 상위 가이드: [Adaptive Layout and Navigation](../adaptive-layout-and-navigation.md)
- 관련 아키텍처: [Navigation 3 계약](../../navigation3/navigation3-contracts/navigation3-contracts.md)
