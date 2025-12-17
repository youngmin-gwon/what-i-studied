---
title: apple-watchos-system
tags: [apple, watchos, system, complications, snapshot, budget]
aliases: []
date modified: 2025-12-17 23:50:00 +09:00
date created: 2025-12-17 23:50:00 +09:00
---

## watchOS System Internals

Apple Watch는 "짧은 상호작용(Glanceable Interaction)"을 위해 설계되었습니다.
사용자는 팔을 2초 이상 들고 있지 않습니다. 따라서 시스템은 앱을 가능한 한 오래 재우고(Suspended), 필요할 때만 아주 잠깐 깨웁니다.

### 💡 왜 이것을 알아야 하나요? (Context)
- **Snapshot Ghost**: "사용자가 앱을 켰는데 예전 데이터가 보여요." -> 시스템이 배터리를 아끼려고 마지막으로 찍은 스냅샷(이미지)을 먼저 보여주기 때문입니다.
- **Complication Budget**: "워치 페이스 날씨가 업데이트 안 돼요." -> 하루에 50번 업데이트 제한(Budget)을 다 써버렸기 때문입니다.
- **Always On Display**: 화면이 꺼지지 않는 AOD 상태에서 내 앱이 어떻게 보여야 하는지(민감 정보 가리기 등) 처리해야 합니다.

---

### 📸 Snapshot-based Lifecycle

watchOS 앱 생명주기의 핵심은 **스냅샷**입니다.

1. **App Switcher & Dock**: 사용자가 Dock 버튼을 누르면, 실제 앱이 실행되는 게 아니라 시스템이 저장해둔 스크린샷들이 나열됩니다.
2. **Snapshot Refresh**: 시스템은 주기적으로 앱을 백그라운드에서 살짝 깨워서(`handleBackgroundTasks`) UI를 업데이트하고 다시 스냅샷을 찍습니다.
3. **Launch**: 사용자가 스냅샷을 탭하면 그제서야 실제 프로세스가 포그라운드로 올라옵니다.

**전략**: `sceneWillResignActive`에서 UI를 최신 상태로 만들어야 합니다. 그래야 스냅샷이 예쁘게 찍힙니다.

---

### ⌚️ Complications & Budget

워치 페이스에 있는 작은 위젯들입니다.
데이터를 실시간으로 가져오는 것이 불가능합니다. **미리(Timeline)** 줘야 합니다.

#### 1. CLKComplicationDataSource
- `getCurrentTimelineEntry`: "지금" 보여줄 데이터.
- `getTimelineEntries(after:limit:)`: "앞으로 2시간 동안" 보여줄 데이터 배열. (예: 1시엔 맑음, 2시엔 흐림)

#### 2. Execution Budget
배터리 보호를 위해 앱당 하루에 약 **50회의 백그라운드 업데이트**만 허용됩니다.
- `reloadTimeline(for:)`을 남발하면 예산이 바닥나서 업데이트가 멈춥니다.
- **Push Notification**을 섞어서 중요한 업데이트만 즉시 반영하는 전략(Background Push)이 필요합니다.

---

### 📱 Communication with iPhone (WCSession)

Watch 앱은 독립적일 수도 있지만, 여전히 iPhone(Companion)과 데이터를 주고받아야 할 때가 많습니다.

- **updateApplicationContext**: 딕셔너리 데이터 덮어쓰기. (가장 최신 상태만 중요할 때)
- **sendMessage**: 즉시 전송. (앱이 켜져 있을 때만 가능, 실패 시 깨움)
- **transferUserInfo**: 큐에 쌓아두고 순차 전송. (급하지 않을 때)
- **transferFile**: 파일 전송.

**주의**: WCSession은 매우 불안정할 수 있습니다. iPhone이 안 켜져 있거나 거리가 멀면 실패합니다. 반드시 에러 처리를 해야 합니다.

### 더 보기
- [[apple-ios-system]] - iOS 백그라운드 정책 비교
- [[apple-swiftui-deep-dive]] - watchOS UI의 표준인 SwiftUI
