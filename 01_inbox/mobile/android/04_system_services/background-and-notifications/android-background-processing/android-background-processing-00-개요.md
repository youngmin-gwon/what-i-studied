# android background processing 개요

---
title: android-background-processing
tags: []
aliases: []
date modified: 2026-07-31 15:18:29 +09:00
date created: 2026-04-04 00:22:18 +09:00
---

## [mobile-security](01_inbox/mobile/mobile-security.md) > [android-background-processing](01_inbox/mobile/android/04_system_services/background-and-notifications/android-background-processing.md)

### Background Processing: Execution Strategy

안드로이드 앱이 포그라운드에 있지 않을 때 작업을 수행하는 **WorkManager**, **Foreground Service**, **AlarmManager**의 메커니즘을 심층 분석합니다.

단순히 비동기 처리를 하는 것을 넘어, 사용자 경험(UX)을 해치지 않으면서 배터리 효율을 극대화하고 OS 의 강력한 백그라운드 제약을 어떻게 우회하거나 준수할지 이해하는 것이 목표입니다.

---
