# Adaptive Navigation 계약

Adaptive Navigation 은 화면 크기와 입력 환경에 따라 app chrome 과 content 배치를 바꾸는 문제다. Navigation 3 의 back stack 상태와 adaptive scaffold 의 표시 정책을 분리해서 읽는다.

## 정본 노트

- [Adaptive navigation은 device type이 아니라 현재 window와 posture로 결정한다](01_inbox/mobile/android/02_app_framework/navigation/adaptive-navigation/adaptive-navigation-contracts/adaptive-navigation-is-driven-by-window-and-posture.md)
- [Top-level destination은 adaptive navigation chrome의 단위다](01_inbox/mobile/android/02_app_framework/navigation/adaptive-navigation/adaptive-navigation-contracts/top-level-destination-owns-adaptive-navigation-chrome.md)
- [Pane layout은 선택 상태와 back policy를 분리해 보존해야 한다](01_inbox/mobile/android/02_app_framework/navigation/adaptive-navigation/adaptive-navigation-contracts/pane-layout-preserves-selection-and-back-policy.md)
- [표준 adaptive scaffold를 먼저 검토하고 custom layout은 명시적 이유가 있을 때 둔다](01_inbox/mobile/android/02_app_framework/navigation/adaptive-navigation/adaptive-navigation-contracts/standard-adaptive-scaffolds-should-precede-custom-layouts.md)
- [Navigation 3 Scene과 adaptive scaffold는 서로 다른 레이아웃 문제를 푼다](01_inbox/mobile/android/02_app_framework/navigation/adaptive-navigation/adaptive-navigation-contracts/navigation3-scenes-and-adaptive-scaffolds-solve-different-layout-problems.md)

관련 지도: [Android Navigation 진입 계약](01_inbox/mobile/android/02_app_framework/navigation/navigation-contracts/navigation-contracts.md), [Navigation 3 계약](01_inbox/mobile/android/02_app_framework/navigation/navigation3/navigation3-contracts/navigation3-contracts.md)
