---
title: "APEX"
tags: ["android", "android/glossary"]
aliases: ["Android Pony EXpress", "Mainline module"]
---

# APEX

정의: APEX는 APK보다 낮은 계층의 system module을 독립적으로 업데이트하기 위한 Android Mainline packaging format이다.

혼동 방지: APEX는 일반 앱 배포 단위가 아니다. boot-time mount, version selection, rollback, partition boundary와 연결되므로 app bundle 또는 APK signing 문제와 분리해 봐야 한다.

정본 링크:
- [APEX package contract](01_inbox/mobile/android/01_system_internals/platform-modularity/platform-modularity-contracts/apex-packages-lower-level-system-modules-that-apk-cannot-model-well.md)
- [APEX activation contract](01_inbox/mobile/android/01_system_internals/platform-modularity/platform-modularity-contracts/apex-activation-uses-boot-time-mounting-version-selection-and-rollback.md)
