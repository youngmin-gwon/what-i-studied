---
title: package-user-role-contracts
tags: ["android", "android/system-services"]
aliases: ["패키지/사용자/역할 조회 계약"]
date modified: 2026-08-04 15:00:00 +09:00
date created: 2026-08-03 17:29:24 +09:00
---

## 패키지/사용자/역할 조회 계약

이 지도는 다른 앱 조회, 멀티 유저/work profile, 기본 앱 자격이라는 서로 다른 세 조회 표면을 분리한다.

### 읽는 순서

1. [PackageManager 조회는 Android 11부터 패키지 가시성 제한을 받는다](./package-visibility-queries.md)에서 다른 앱을 조회할 때의 제약을 본다.
2. [UserManager는 여러 사용자와 work profile을 별도 UserHandle로 다룬다](./user-manager-userhandle.md)에서 멀티 유저 개념을 정리한다.
3. [RoleManager는 권한 묶음이 아니라 기본 앱 자격을 관리한다](./role-manager-contract.md)에서 역할과 permission의 차이를 본다.

### 문제 분류

| 증상 | 먼저 확인할 경계 |
| --- | --- |
| 다른 앱이 설치돼 있는데 조회 결과에 없음 | 패키지 가시성 선언(`<queries>`) 여부 |
| work profile 기기에서 앱이 개인/업무 프로필을 혼동 | 호출에 사용한 `UserHandle`이 맞는지 |
| 기본 앱으로 등록했는데 시스템이 인식 못 함 | RoleManager 자격 요건(필수 인텐트 필터, permission)을 충족했는지 |

### 책임 경계

- PackageManager 조회는 "어떤 앱이 설치돼 있는가"를 묻고, RoleManager는 "이 앱이 특정 기본 앱 역할을 맡을 자격이 있는가"를 묻는다. 둘은 다른 질문이다.
- UserManager가 다루는 다중 사용자/work profile 분리는 OS 레벨 격리이며, 앱 내부의 사용자 계정 개념(로그인 계정)과는 무관하다.

### 노트 목록

- [PackageManager 조회는 Android 11부터 패키지 가시성 제한을 받는다](./package-visibility-queries.md)
- [UserManager는 여러 사용자와 work profile을 별도 UserHandle로 다룬다](./user-manager-userhandle.md)
- [RoleManager는 권한 묶음이 아니라 기본 앱 자격을 관리한다](./role-manager-contract.md)

검증일: 2026-08-03. [패키지 가시성](https://developer.android.com/training/package-visibility)과 [RoleManager 문서](https://developer.android.com/reference/android/app/role/RoleManager)를 기준으로 확인했다.
