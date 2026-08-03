---
title: modulemetadata-describes-mainline-modules-on-a-device
tags: ["android", "android/system-internals"]
aliases: ["ModuleMetadata는 기기에 있는 Mainline module 목록을 설명한다"]
date modified: 2026-08-03 17:26:46 +09:00
date created: 2026-07-31 23:05:30 +09:00
---

## ModuleMetadata 는 기기에 있는 Mainline module 목록을 설명한다

ModuleMetadata 는 특정 device 에 설치된 Mainline module 목록에 관한 metadata 를 제공하는 module 이다. system server 시작 시 metadata 가 parsing/cache 되고, PackageManager 의 module info API 가 이 정보를 사용할 수 있다.

이 metadata 는 사용자가 외우는 module 목록이 아니라 device state 를 설명하는 데이터다. module name, packageName, hidden 여부 같은 정보를 통해 해당 build 가 어떤 modular system components 를 갖는지 알 수 있다.

하지만 앱 feature gating 을 ModuleMetadata 목록에 직접 묶는 것은 보통 과하다. 사용하려는 API 나 capability 가 있다면 공식 API availability check, SDK Extension, PackageManager feature check 를 우선한다.

관련 노트: [Mainline module 목록](01_inbox/mobile/android/01_system_internals/platform-modularity/platform-modularity-contracts/mainline-module-list-is-device-and-release-dependent-metadata.md), [앱 availability check](01_inbox/mobile/android/01_system_internals/platform-modularity/platform-modularity-contracts/apps-should-check-api-feature-availability-not-mainline-package-names.md).

공식 문서: [ModuleMetadata](https://source.android.com/docs/core/ota/modular-system/metadata)
