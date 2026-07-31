---
title: android-activity-lifecycle-00-개요
tags: []
aliases: []
date modified: 2026-07-31 16:29:01 +09:00
date created: 2026-07-31 16:26:40 +09:00
---

## android activity lifecycle 개요

## [mobile-security](01_inbox/mobile/mobile-security.md) > [android-activity-lifecycle](01_inbox/mobile/android/02_app_framework/architecture/app-components/android-activity-lifecycle.md)

### Activity Lifecycle: Process Mastery

안드로이드 `Activity` 의 생성부터 소멸까지의 복잡한 생명주기(Lifecycle) 변화와 **프로세스 킬(Process Death)** 대응 메커니즘을 심층 분석합니다.

단순히 콜백 함수를 호출하는 것을 넘어, 시스템 리소스가 부족할 때 OS 가 어떻게 프로세스를 관리하고, 사용자가 앱으로 돌아왔을 때 상태를 어떻게 복구하는지 이해하는 것이 목표입니다.

---
