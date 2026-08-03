---
title: AndroidManifest는 OS가 발견할 컴포넌트와 권한 경계를 선언한다
tags: [android, android/app-components, android/architecture]
aliases: ["AndroidManifest는 OS가 발견할 컴포넌트와 권한 경계를 선언한다"]
date modified: 2026-08-03 16:34:35 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# AndroidManifest는 OS가 발견할 컴포넌트와 권한 경계를 선언한다

AndroidManifest 는 OS 와 build tool 이 앱의 component, permission, feature, intent-filter, metadata 를 발견하는 선언 파일이다. Activity, Service, Receiver, Provider 는 런타임에 아무 클래스나 스캔되어 노출되는 것이 아니라 Manifest 와 관련 metadata 를 통해 OS-visible surface 가 된다.

Manifest 는 navigation 문서만의 주제가 아니다. 외부 앱이 호출할 수 있는 entry point, 필요한 permission, package visibility, provider authority, foreground service type 같은 OS 계약이 여기서 시작된다.

다만 deep link 나 intent-filter matching 의 세부 규칙은 navigation/intent 정본이 담당한다. 이 노트는 app component 관점에서 Manifest 가 왜 아키텍처 경계인지 설명한다.

관련 노트: [Manifest/entry point 정본](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/intent-manifest-contracts/android-manifest-declares-os-visible-components-and-entry-points.md), [intent/manifest 정본](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/intent-manifest-contracts/intent-manifest-contracts.md), [exported/permission 경계](01_inbox/mobile/android/02_app_framework/architecture/app-components/app-component-contracts/exported-and-permission-boundaries-decide-external-component-access.md).

공식 문서: [App Manifest overview](https://developer.android.com/guide/topics/manifest/manifest-intro)
