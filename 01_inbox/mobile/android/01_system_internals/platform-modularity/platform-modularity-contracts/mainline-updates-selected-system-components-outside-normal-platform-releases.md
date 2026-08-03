---
title: mainline-updates-selected-system-components-outside-normal-platform-releases
tags: ["android", "android/system-internals"]
aliases: ["Mainline은 선택된 system component를 정규 플랫폼 release 밖에서 업데이트한다"]
date modified: 2026-08-03 17:26:45 +09:00
date created: 2026-07-31 23:05:30 +09:00
---

## Mainline 은 선택된 system component 를 정규 플랫폼 release 밖에서 업데이트한다

Mainline 은 Android 10 에서 도입된 modular system components 구조다. 목적은 일부 system component 를 Android 전체 OS release 와 분리해 critical bug fix 와 개선을 더 빠르고 넓게 배포하는 것이다.

Mainline update 는 Google Play system update 인프라나 partner OTA 를 통해 전달될 수 있다. GMS 기기에서는 Google 서명과 `com.google.android.*` package prefix 가 보일 수 있고, AOSP key 로 서명된 기기는 `com.android.*` prefix 를 쓸 수 있다.

공식 문서 기준으로 Android 11 이하 Mainline support 는 2025 년 Q4 에 종료되었다. 따라서 오래된 기기까지 같은 update path 가 계속 유지된다고 쓰면 안 된다.

Mainline module 은 아무 system component 나 마음대로 뜯어낸 것이 아니다. 공식 compatibility, stable API/interface, CTS 조건을 만족할 수 있는 component 만 module boundary 를 가진다.

관련 노트: [Mainline module 목록](01_inbox/mobile/android/01_system_internals/platform-modularity/platform-modularity-contracts/mainline-module-list-is-device-and-release-dependent-metadata.md), [APEX package 경계](01_inbox/mobile/android/01_system_internals/platform-modularity/platform-modularity-contracts/apex-packages-lower-level-system-modules-that-apk-cannot-model-well.md), [security practices](01_inbox/mobile/android/05_security_privacy/security-practices/security-practice-contracts/android-security-practice-is-defense-in-depth-not-client-trust.md).

공식 문서: [Mainline](https://source.android.com/docs/core/ota/modular-system)
