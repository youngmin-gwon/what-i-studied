---
title: exported-and-permission-boundaries-decide-external-component-access
tags: [android, android/app-components, android/architecture]
aliases: ["android:exported와 권한은 외부 컴포넌트 접근 경계를 결정한다"]
date modified: 2026-08-04 13:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## android:exported 와 권한은 외부 컴포넌트 접근 경계를 결정한다

`android:exported` 는 다른 앱이나 시스템이 해당 component 를 직접 호출할 수 있는지 결정하는 핵심 경계다. intent-filter 는 어떤 요청을 받을 수 있는지 광고하지만, 그 자체가 authorization 은 아니다.

외부 접근이 필요한 Activity, Service, Receiver, Provider 는 exported 여부, required permission, URI permission, PendingIntent 위임 범위를 함께 설계해야 한다. 특히 component 에 filter 가 있거나 system surface 와 연결될 때는 암묵적 기본값에 의존하지 않는 편이 안전하다.

이 경계는 보안 문서의 permission model 과 navigation 문서의 intent matching 사이에 놓인다. 어떤 component 를 외부에 열지 결정한 뒤, 어떤 Intent/URI/permission 으로 열지 구체화한다.

두 실패는 서로 다른 신호를 남긴다. exported=false 로 등록 자체가 막히면 (Activity 기준) 호출 측에서 `ActivityNotFoundException` 이 발생하고, 등록은 됐지만 permission 이 없으면 logcat 에 `Permission Denial:` 메시지가 남는다. 예외 이름만으로는 두 경우를 구분할 수 없으므로 logcat 을 함께 확인해야 한다.

관련 노트: [exported attribute 정본](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/intent-manifest-contracts/exported-attribute-defines-external-component-boundary.md), [Android 권한 계약](01_inbox/mobile/android/05_security_privacy/permissions-and-sandbox/permission-contracts/permission-contracts.md), [컴포넌트 통신 경계](01_inbox/mobile/android/02_app_framework/architecture/app-components/app-component-contracts/component-communication-uses-intent-binder-uri-and-pendingintent-by-boundary.md).

공식 문서: [App Manifest overview](https://developer.android.com/guide/topics/manifest/manifest-intro)
