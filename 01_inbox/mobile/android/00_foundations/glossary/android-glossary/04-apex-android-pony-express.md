---
title: 04-apex-android-pony-express
tags: ["android", "android/glossary"]
aliases: ["Android Pony EXpress", "Mainline module"]
date modified: 2026-08-01 01:07:14 +09:00
date created: 2026-07-31 15:29:55 +09:00
---

## APEX

정의: APEX 는 APK 보다 낮은 계층의 system module 을 독립적으로 업데이트하기 위한 Android Mainline packaging format 이다.

혼동 방지: APEX 는 일반 앱 배포 단위가 아니다. boot-time mount, version selection, rollback, partition boundary 와 연결되므로 app bundle 또는 APK signing 문제와 분리해 봐야 한다.

정본 링크:

- [APEX package contract](01_inbox/mobile/android/01_system_internals/platform-modularity/platform-modularity-contracts/apex-packages-lower-level-system-modules-that-apk-cannot-model-well.md)
- [APEX activation contract](01_inbox/mobile/android/01_system_internals/platform-modularity/platform-modularity-contracts/apex-activation-uses-boot-time-mounting-version-selection-and-rollback.md)
