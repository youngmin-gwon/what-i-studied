---
title: "PackageManager 조회는 Android 11부터 패키지 가시성 제한을 받는다"
tags: ["android", "android/system-services"]
---

# PackageManager 조회는 Android 11부터 패키지 가시성 제한을 받는다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](01_inbox/mobile/android/04_system_services/android-system-services-and-device-capabilities.md)
관련 지도: [패키지/사용자/역할 조회 계약](01_inbox/mobile/android/04_system_services/system-state/package-user-role-contracts/package-user-role-contracts.md)

## 핵심 정의

Android 11(API 30)부터 `PackageManager`의 `getInstalledPackages()`, `getInstalledApplications()`, `queryIntentActivities()` 같은 조회 API는 기본적으로 기기에 설치된 다른 앱을 모두 보여주지 않는다. 앱은 매니페스트의 `<queries>` 요소로 조회하고 싶은 패키지, 인텐트, provider authority를 명시적으로 선언해야 한다.

## 메커니즘

이 제한은 개인정보 보호를 위해 도입됐다. 사용자 기기에 설치된 전체 앱 목록은 사용자의 관심사, 소득 수준, 종교 등을 추론하는 지문(fingerprint)으로 악용될 수 있기 때문이다. `<queries>`에 없는 패키지는 앱 관점에서 "설치되어 있지 않은 것"처럼 보인다. 자기 자신의 패키지, 시스템 패키지 일부, 그리고 자신에게 명시적으로 인텐트를 보낸 적 있는 앱은 이 제한과 무관하게 항상 보인다.

`QUERY_ALL_PACKAGES` permission으로 전체 조회를 우회할 수 있지만 Play 정책상 제한적으로만 승인되며, 대부분의 통상적인 상호운용 목적(공유 대상 앱 목록 등)에는 사용이 거부된다.

## 판단 기준

- 특정 앱과의 연동(딥링크 처리 여부 확인, 특정 브라우저 존재 확인)이 필요하면 대상 패키지명 또는 인텐트 필터를 `<queries>`에 구체적으로 선언한다.
- "설치된 모든 앱 목록"이 정말 제품 요구사항인지 다시 검토한다. 대부분의 경우 특정 카테고리의 인텐트 필터 조회로 대체 가능하다.
- `<queries>`를 과도하게 넓게 선언하면(예: 모든 `ACTION_VIEW` 인텐트) Play 심사에서 사유 소명을 요구받을 수 있다.

## 경계

- 이 노트는 다른 앱을 조회하는 시점의 가시성 제한을 다룬다. 사용자/work profile 분리는 [UserManager는 여러 사용자와 work profile을 별도 UserHandle로 다룬다](01_inbox/mobile/android/04_system_services/system-state/package-user-role-contracts/usermanager-separates-users-and-work-profiles-by-userhandle.md)가 다룬다.
- 앱 설치/업데이트 자체의 흐름(서명, 배포)은 `03_packaging_deployment`가 다룬다.

## 관찰 가능한 신호

`<queries>` 선언 없이 대상 패키지를 조회하면 `queryIntentActivities()`가 빈 리스트를, `getPackageInfo()`가 `NameNotFoundException`을 반환한다. `adb shell dumpsys package <pkg>`의 매니페스트 정보에서 `<queries>` 선언 내용을 확인할 수 있다.

## 공식 문서

- https://developer.android.com/training/package-visibility
- https://developer.android.com/training/package-visibility/declaring
