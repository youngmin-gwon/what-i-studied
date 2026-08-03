---
title: "Android 플랫폼 모듈화는 system, vendor, kernel 업데이트 경계를 층위별로 나눈다"
tags: ["android", "android/system-internals"]
aliases: ["Android 플랫폼 모듈화는 system, vendor, kernel 업데이트 경계를 층위별로 나눈다"]
date modified: 2026-08-03 16:30:00 +09:00
date created: 2026-07-31 23:05:30 +09:00
---

# Android 플랫폼 모듈화는 system, vendor, kernel 업데이트 경계를 층위별로 나눈다

Android 플랫폼 모듈화는 하나의 기능이 아니라 fragmentation을 줄이기 위한 여러 update boundary의 조합이다. Mainline은 일부 system component를 독립 module로 만들고, APEX는 lower-level module을 boot-aware package로 담으며, SDK Extensions는 일부 API availability를 platform release 밖에서 표현한다.

Treble과 GKI는 더 낮은 층위의 경계다. Treble은 system image와 vendor implementation을 stable interface로 분리하고, GKI는 common kernel과 vendor kernel module을 KMI 경계로 분리한다.

따라서 "Android가 모듈식이다"라는 말은 어느 층을 말하는지 먼저 정해야 한다. 앱 개발자는 SDK Extension과 feature availability를 확인하고, 플랫폼 개발자는 APEX/Mainline/Treble/GKI 각각의 compatibility contract를 확인한다.

관련 노트: [Mainline 경계](01_inbox/mobile/android/01_system_internals/platform-modularity/platform-modularity-contracts/mainline-updates-selected-system-components-outside-normal-platform-releases.md), [Treble 정본](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/treble-separates-system-and-vendor-through-stable-interfaces.md), [GKI 정본](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/gki-splits-generic-core-from-vendor-modules.md).

공식 문서: [Mainline](https://source.android.com/docs/core/ota/modular-system), [Partitions overview](https://source.android.com/docs/core/architecture/partitions)
