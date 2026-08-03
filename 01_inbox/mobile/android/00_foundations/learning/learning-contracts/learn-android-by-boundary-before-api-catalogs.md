---
title: "Android 는 API catalog 보다 boundary 단위로 먼저 배운다"
tags: ["android", "android/foundations"]
aliases: []
date modified: 2026-08-03 16:33:52 +09:00
date created: 2026-07-31 23:04:26 +09:00
---

# Android 는 API catalog 보다 boundary 단위로 먼저 배운다

Android 를 처음 배울 때 모든 API 를 나열하면 오래 가지 않는다. 먼저 app lifecycle, process, state owner, permission, storage, background work, rendering, packaging 같은 boundary 를 잡아야 한다.

그 뒤에 Compose, ViewModel, Flow, Room, WorkManager, Navigation, Hilt 같은 도구를 각 boundary 에 배치한다. 이 순서가 잡히면 새 API 가 나와도 어디에 넣어야 하는지 판단하기 쉽다.

관련 노트: [Android Foundations](01_inbox/mobile/android/00_foundations/android-foundation-map.md), [app architecture](01_inbox/mobile/android/02_app_framework/architecture/android-app-architecture.md), [Compose runtime](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/compose-runtime-and-state-model.md).

### 판단 기준

새 API 를 만났을 때 누가 상태를 소유하고, 어떤 lifecycle 에서 유효하며, process 종료 후 무엇이 남고, 실패를 누가 복구하는지 답한 뒤 기존 boundary 에 배치한다.

### 경계

이 노트는 학습 순서를 정하며 개별 API 의 우열이나 사용법은 판단하지 않는다. 도구 선택은 해당 app framework, service, packaging 정본으로 넘긴다.
