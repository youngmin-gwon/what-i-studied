---
title: android-intent-and-ipc
tags: []
aliases: []
date modified: 2026-04-05 17:43:07 +09:00
date created: 2026-04-04 00:12:42 +09:00
---

## [mobile-security](01_inbox/mobile/mobile-security.md) > [android-intent-and-ipc](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/android-intent-and-ipc.md)

### Android Intent & IPC: Messaging Framework

안드로이드 시스템의 핵심 통신 메커니즘인 **Intent**와 프로세스 간 통신(**IPC**)을 심층 분석합니다.

단순히 앱 컴포넌트를 실행하는 도구를 넘어, 시스템 전체의 데이터 흐름을 제어하고 보안 경계를 정의하는 중추적인 역할을 이해하는 것이 목표입니다.

---

---

## 원자 노트

- [💡 Context: Intent vs iOS 통신 방식](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/android-intent-and-ipc/01-context-intent-vs-ios-%ED%86%B5%EC%8B%A0-%EB%B0%A9%EC%8B%9D.md)
- [Intent 의 구성 요소](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/android-intent-and-ipc/02-intent-%EC%9D%98-%EA%B5%AC%EC%84%B1-%EC%9A%94%EC%86%8C.md)
- [Explicit vs Implicit Intent](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/android-intent-and-ipc/03-explicit-vs-implicit-intent.md)
- [Intent Filter](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/android-intent-and-ipc/04-intent-filter.md)
- [`<queries>` 태그 (Package Visibility, Android 11+)](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/android-intent-and-ipc/05-queries-%ED%83%9C%EA%B7%B8-package-visibility-android-11.md)
- [PendingIntent](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/android-intent-and-ipc/06-pendingintent.md)
- [Activity Result API (Modern)](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/android-intent-and-ipc/07-activity-result-api-modern.md)
- [앱 간 데이터 전달 보안](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/android-intent-and-ipc/08-%EC%95%B1-%EA%B0%84-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%A0%84%EB%8B%AC-%EB%B3%B4%EC%95%88.md)
- [디버깅](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/android-intent-and-ipc/android-intent-and-ipc-09-%EB%94%94%EB%B2%84%EA%B9%85.md)
- [더 보기](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/android-intent-and-ipc/android-intent-and-ipc-10-%EB%8D%94-%EB%B3%B4%EA%B8%B0.md)

---

## 정리 기준

이 노트는 원래 긴 가이드였고, H4 섹션을 별도 원자 노트로 분리했습니다.
기존 링크 호환을 위해 이 파일은 허브 노트로 유지합니다.
