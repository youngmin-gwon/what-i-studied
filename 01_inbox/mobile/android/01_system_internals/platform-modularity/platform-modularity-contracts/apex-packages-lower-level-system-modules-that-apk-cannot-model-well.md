---
title: apex-packages-lower-level-system-modules-that-apk-cannot-model-well
tags: ["android", "android/system-internals"]
aliases: ["APEX는 APK 모델로 다루기 어려운 lower-level system module을 담는다"]
date modified: 2026-08-03 17:26:42 +09:00
date created: 2026-07-31 23:05:30 +09:00
---

## APEX 는 APK 모델로 다루기 어려운 lower-level system module 을 담는다

APEX(Android Pony EXpress)는 Android 10 에서 도입된 package/container format 이다. ART, native service, class library, HAL 처럼 APK 설치 모델만으로는 boot timing 과 system integration 을 다루기 어려운 lower-level component 를 업데이트하기 위해 만들어졌다.

APEX 파일은 package identity 와 version metadata, payload image, public key 같은 요소를 포함하고, apexd 가 boot 과정에서 activation 을 관리한다. 어떤 APEX 는 매우 이른 boot 단계에 필요하므로 일반 APK 처럼 PackageManager 가 준비된 뒤에만 다루는 모델이 맞지 않는다.

APEX 는 "앱 배포 포맷의 다른 이름"이 아니다. platform partition, verified payload, boot activation, rollback, signing key 가 얽힌 system update 경계다.

관련 노트: [APEX activation/rollback](01_inbox/mobile/android/01_system_internals/platform-modularity/platform-modularity-contracts/apex-activation-uses-boot-time-mounting-version-selection-and-rollback.md), [boot/runtime 정본](01_inbox/mobile/android/01_system_internals/boot-and-runtime/android-boot-and-runtime.md), [platform-modularity hub](01_inbox/mobile/android/01_system_internals/platform-modularity/android-platform-modularity.md).

공식 문서: [APEX file format](https://source.android.com/docs/core/ota/apex)
