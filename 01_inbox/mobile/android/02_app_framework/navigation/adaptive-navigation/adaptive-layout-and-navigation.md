---
title: Adaptive Layout과 Navigation은 화면 조건에 맞게 content pane을 조정하는 설계다
tags: [android, android/adaptive, android/navigation]
aliases: ["Adaptive Layout and Navigation"]
date modified: 2026-08-03 16:36:17 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# Adaptive Layout과 Navigation은 화면 조건에 맞게 content pane을 조정하는 설계다

Adaptive layout and navigation 은 화면 크기, posture, 입력 장치에 따라 app chrome 과 content pane 을 조정하는 설계 축이다. 목적지는 그대로 두고, 표시 방식만 window 조건에 맞게 바꾸는 것이 핵심이다.

### 정본 지도

- [Adaptive Navigation 계약](01_inbox/mobile/android/02_app_framework/navigation/adaptive-navigation/adaptive-navigation-contracts/adaptive-navigation-contracts.md)
- [Adaptive navigation은 device type이 아니라 현재 window와 posture로 결정한다](01_inbox/mobile/android/02_app_framework/navigation/adaptive-navigation/adaptive-navigation-contracts/adaptive-navigation-is-driven-by-window-and-posture.md)
- [Top-level destination은 adaptive navigation chrome의 단위다](01_inbox/mobile/android/02_app_framework/navigation/adaptive-navigation/adaptive-navigation-contracts/top-level-destination-owns-adaptive-navigation-chrome.md)
- [Pane layout은 선택 상태와 back policy를 분리해 보존해야 한다](01_inbox/mobile/android/02_app_framework/navigation/adaptive-navigation/adaptive-navigation-contracts/pane-layout-preserves-selection-and-back-policy.md)

관련 지도: [Large screen contracts](01_inbox/mobile/android/07_platforms/large-screens/large-screen-contracts/large-screen-contracts.md)
