---
title: 06-lifecycle-states-vs-callbacks
tags: []
aliases: []
date modified: 2026-07-31 16:28:49 +09:00
date created: 2026-07-31 16:26:40 +09:00
---

## 🚦 Lifecycle States vs Callbacks

콜백 메서드보다 **상태(State)**를 보는 것이 더 명확합니다.

- **CREATED**: `onCreate` ~ `onDestroy`
- **STARTED**: `onStart` ~ `onStop` (Visible)
- **RESUMED**: `onResume` ~ `onPause` (Interactive)

### 3. Launch Modes & Tasks

Activity 가 스택(Task)에 쌓이는 방식입니다.

- **SingleTop**: "알림 눌렀을 때 이미 켜져 있으면 그거 재사용해줘" (`onNewIntent`)
- **SingleTask**: "이 앱의 메인 화면은 딱 하나만 있어야 해" (카카오톡 채팅방 -> 메인)
