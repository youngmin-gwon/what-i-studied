---
title: rolemanager-manages-default-app-eligibility-not-permission-bundles
tags: ["android", "android/system-services"]
aliases: ["RoleManager는 권한 묶음이 아니라 기본 앱 자격을 관리한다"]
date modified: 2026-08-06 14:48:27 +09:00
date created: 2026-08-03 17:29:24 +09:00
---

## RoleManager는 권한 묶음이 아니라 기본 앱 자격을 관리한다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](../../android-system-services-and-device-capabilities.md)
배경 지식: [신원 관리](../../../../../security/fundamentals/identity-management.md)
관련 지도: [패키지/사용자/역할 조회 계약](./package-user-role.md)

### 핵심 정의

**RoleManager**(Android 10, API 29+)는 기본 SMS 앱, 기본 전화 앱, 브라우저 같은 특정 "역할(role)"에 어떤 앱이 자격을 갖는지, 그리고 사용자가 실제로 어떤 앱을 그 역할로 선택했는지를 관리하는 OS 매니저다. 역할은 단순 permission 그룹이 아니라, "이 역할을 맡을 자격이 있는 앱 후보 목록"과 "사용자의 선택"을 분리해서 다루는 별도 개념이다. 역할 보유에 따라 시스템이 관련 permission이나 특권을 함께 조정할 수는 있다.

### 메커니즘

앱이 특정 역할(예: `RoleManager.ROLE_DIALER`)의 후보가 되려면 매니페스트에 해당 역할이 요구하는 인텐트 필터와 permission을 먼저 충족해야 한다. 그 뒤 `RoleManager.createRequestRoleIntent()`로 사용자에게 "이 앱을 기본 전화 앱으로 설정할지" 확인하는 시스템 UI를 띄울 수 있다. 사용자가 승인하면 시스템은 해당 역할에 연결된 특권(예: 기본 전화 앱은 통화 기록에 자동 접근)을 부여한다. 역할 자체는 permission 요청 API와 다른 별도 흐름이다.

### 판단 기준

- 기본 앱으로 등록되길 원하는 기능(전화, SMS, 브라우저 등)이 있다면 해당 역할의 요구사항(필수 인텐트 필터, permission)을 먼저 충족했는지 확인한다. 역할 요청이 필요한 런타임 permission 요청을 모두 대체한다고 가정하지 않는다.
- 역할 자격 요건을 충족하지 못한 상태에서 `createRequestRoleIntent()`를 호출하면 시스템이 요청 자체를 무시하거나 실패로 처리할 수 있다.
- 구버전(Android 9 이하)과의 호환이 필요하면 역할별로 존재했던 이전 방식(예: `Telecom` API의 기본 다이얼러 확인)과의 차이를 별도로 처리해야 한다.

### 최소 사용자 승인 흐름

역할이 기기에 존재하는지, 이미 보유했는지를 먼저 확인한다. 시스템 UI의 result code는 사용자 흐름 결과일 뿐 최종 권한 증명이 아니므로 돌아온 뒤 `isRoleHeld()`를 다시 읽는다.

```kotlin
val roles = getSystemService(RoleManager::class.java)
val role = RoleManager.ROLE_DIALER

val requestRole = registerForActivityResult(
    ActivityResultContracts.StartActivityForResult()
) {
    renderDialerRole(roles.isRoleHeld(role))
}

when {
    !roles.isRoleAvailable(role) -> showUnsupportedRole()
    roles.isRoleHeld(role) -> openDialerHome()
    else -> requestRole.launch(roles.createRequestRoleIntent(role))
}
```

요청 UI가 취소되거나 앱이 자격 요건을 잃을 수 있다. 기능 진입 때마다 보유 상태를 확인하고, 미보유 상태에서도 데이터 손실 없이 제한된 UX로 돌아간다.

### 경계

- 이 노트는 역할 자격과 사용자 선택 흐름을 다룬다. 역할 승인 이후 실제 permission 검사 메커니즘은 [Binder 서비스는 필요한 호출 경계에서 호출자 신원과 정책을 검사한다](../../service-lookup/service-lookup/system-server-uid-pid-check.md)가 다룬다.
- 다중 사용자/work profile에서 역할이 프로필별로 별도 관리된다는 점은 [UserManager는 여러 사용자와 work profile을 별도 UserHandle로 다룬다](./user-manager-userhandle.md)와 연결해서 읽는다.

### 관찰 가능한 신호

요청 전후의 `isRoleAvailable()`·`isRoleHeld()`와 Activity result를 함께 기록한다. `adb shell cmd role get-role-holders <role_name>` 결과와 대조하면 "UI는 완료됐지만 보유하지 않음"과 "역할 자체가 없음"을 분리할 수 있다.

### 공식 문서

- https://developer.android.com/reference/android/app/role/RoleManager

검증일: 2026-08-06. `createRequestRoleIntent()`의 승인 UI 계약과 `isRoleAvailable()`/`isRoleHeld()`의 별도 상태 확인 API를 재확인했다.
