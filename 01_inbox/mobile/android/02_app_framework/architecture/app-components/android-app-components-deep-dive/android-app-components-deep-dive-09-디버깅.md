---
title: android-app-components-deep-dive-09-디버깅
tags: []
aliases: []
date modified: 2026-07-31 16:29:50 +09:00
date created: 2026-07-31 15:29:55 +09:00
---

## 디버깅

상위 노트: [android-app-components-deep-dive](01_inbox/mobile/android/02_app_framework/architecture/app-components/android-app-components-deep-dive.md)

```bash
# Activity 스택 확인
adb shell dumpsys activity activities

# Service 목록
adb shell dumpsys activity services

# BroadcastReceiver 히스토리
adb shell dumpsys activity broadcasts

# ContentProvider 확인
adb shell dumpsys activity providers
```
