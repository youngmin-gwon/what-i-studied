---
title: "RoleManager는 권한 묶음이 아니라 기본 앱 자격을 관리한다"
tags: ["android", "android/system-services"]
---

# RoleManager는 권한 묶음이 아니라 기본 앱 자격을 관리한다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](01_inbox/mobile/android/04_system_services/android-system-services-and-device-capabilities.md)
관련 지도: [패키지/사용자/역할 조회 계약](01_inbox/mobile/android/04_system_services/system-state/package-user-role-contracts/package-user-role-contracts.md)

## 핵심 정의

`RoleManager`(Android 10, API 29+)는 기본 SMS 앱, 기본 전화 앱, 갤러리, 브라우저 같은 "역할(role)"에 어떤 앱이 자격을 갖는지, 그리고 사용자가 실제로 어떤 앱을 그 역할로 선택했는지를 관리한다. 역할은 여러 permission을 묶어 자동으로 부여하는 그룹이 아니라, "이 역할을 맡을 자격이 있는 앱 후보 목록"과 "사용자의 선택"을 분리해서 다루는 별도 개념이다.

## 메커니즘

앱이 특정 역할(예: `RoleManager.ROLE_DIALER`)의 후보가 되려면 매니페스트에 해당 역할이 요구하는 인텐트 필터와 permission을 먼저 충족해야 한다. 그 뒤 `RoleManager.createRequestRoleIntent()`로 사용자에게 "이 앱을 기본 전화 앱으로 설정할지" 확인하는 시스템 UI를 띄울 수 있다. 사용자가 승인하면 시스템은 해당 역할에 연결된 특권(예: 기본 전화 앱은 통화 기록에 자동 접근)을 부여한다. 역할 자체는 permission 요청 API와 다른 별도 흐름이다.

## 판단 기준

- 기본 앱으로 등록되길 원하는 기능(전화, SMS, 갤러리, 브라우저 등)이 있다면 개별 permission을 하나씩 요청하지 않고 해당 역할의 요구사항(필수 인텐트 필터, permission)을 먼저 충족했는지 확인한다.
- 역할 자격 요건을 충족하지 못한 상태에서 `createRequestRoleIntent()`를 호출하면 시스템이 요청 자체를 무시하거나 실패로 처리할 수 있다.
- 구버전(Android 9 이하)과의 호환이 필요하면 역할별로 존재했던 이전 방식(예: `Telecom` API의 기본 다이얼러 확인)과의 차이를 별도로 처리해야 한다.

## 경계

- 이 노트는 역할 자격과 사용자 선택 흐름을 다룬다. 역할 승인 이후 실제 permission 검사 메커니즘은 [system_server의 서비스는 호출자 UID/PID로 권한을 검사한다](01_inbox/mobile/android/04_system_services/service-lookup/service-lookup-contracts/system-server-checks-caller-uid-and-pid-for-every-call.md)가 다룬다.
- 다중 사용자/work profile에서 역할이 프로필별로 별도 관리된다는 점은 [UserManager는 여러 사용자와 work profile을 별도 UserHandle로 다룬다](01_inbox/mobile/android/04_system_services/system-state/package-user-role-contracts/usermanager-separates-users-and-work-profiles-by-userhandle.md)와 연결해서 읽는다.

## 관찰 가능한 신호

`adb shell cmd role get-role-holders <role_name>`으로 특정 역할을 현재 어떤 패키지가 보유하고 있는지 확인할 수 있다. `RoleManager.isRoleHeld()`를 앱 코드에서 호출해 런타임에 직접 확인할 수도 있다.

## 공식 문서

- https://developer.android.com/reference/android/app/role/RoleManager
- https://developer.android.com/reference/android/app/role/RoleManager
