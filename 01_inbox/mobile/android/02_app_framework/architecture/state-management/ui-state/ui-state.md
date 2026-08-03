---
title: UI State는 현재 화면을 그리는 값이고 Action은 상태 변화를 요청하는 신호다
tags: [android, android/architecture, android/state-management, android/ui-state]
aliases: ["Android UI State"]
date modified: 2026-08-03 16:35:29 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# UI State는 현재 화면을 그리는 값이고 Action은 상태 변화를 요청하는 신호다

UI State 는 현재 화면을 다시 그릴 수 있는 값이고, Action/Event 는 상태 변화를 요청하거나 소비 시점이 중요한 신호다.

### 정본 노트

- [UI는 상태를 아래로 받고 사용자 행동을 위로 전달한다](01_inbox/mobile/android/02_app_framework/architecture/state-management/ui-state/ui-receives-state-and-sends-actions-up.md)
- [UiState는 새 collector가 받아도 안전한 현재 화면의 표현이다](01_inbox/mobile/android/02_app_framework/architecture/state-management/ui-state/uistate-represents-current-screen-for-new-collectors.md)
- [복원해야 하는 진행 상태는 일회성 이벤트가 아니라 UiState로 표현한다](01_inbox/mobile/android/02_app_framework/architecture/state-management/ui-state/restorable-progress-belongs-in-uistate-not-one-off-event.md)
- [Snackbar와 Navigation처럼 소비 시점이 중요한 신호만 이벤트 스트림으로 분리한다](01_inbox/mobile/android/02_app_framework/architecture/state-management/ui-state/consumable-signals-belong-in-event-stream.md)
- [상태 소유자는 수명, 변경 주체, 공유 범위로 정한다](01_inbox/mobile/android/02_app_framework/architecture/state-management/ui-state/state-owner-is-chosen-by-lifetime-owner-change-frequency-and-sharing.md)
- [데이터 조회 상태와 사용자 조작 상태는 서로 다른 소유자를 가질 수 있다](01_inbox/mobile/android/02_app_framework/architecture/state-management/ui-state/fetch-state-and-interaction-state-can-have-different-owners.md)
- [화면 상태는 불변 값이고 명시적 전이로만 바뀐다](01_inbox/mobile/android/02_app_framework/architecture/state-management/ui-state/screen-state-is-immutable-and-changes-by-explicit-transitions.md)

상위 지도: [Android 상태 관리 정본 지도](01_inbox/mobile/android/02_app_framework/architecture/state-management/android-state-management.md)
