---
title: permission-protection-level-defines-who-can-grant-access
tags: ["android", "android/security-privacy"]
aliases: []
date modified: 2026-08-03 18:13:31 +09:00
date created: 2026-08-01 00:03:59 +09:00
---

## Permission protection level 은 접근 승인 주체를 정의한다

Android permission 의 protection level 은 권한이 어떻게 승인되는지를 정한다. `normal` 은 설치 과정에서 자동으로 허용될 수 있고, `dangerous` 는 사용자가 런타임에 승인해야 하며, `signature` 계열은 같은 서명이나 시스템 신뢰 경계가 승인 주체가 된다.

protection level 은 API 의 민감도와 배포 경계를 드러낸다. 앱이 manifest 에 권한을 선언해도 dangerous permission 은 곧바로 사용 가능해지지 않는다. 반대로 signature permission 은 사용자 다이얼로그로 얻을 수 있는 권한이 아니다.

권한을 설계할 때는 먼저 필요한 데이터나 시스템 기능이 sandbox 밖에 있는지 확인한다. 그런 다음 해당 API 가 어떤 protection level 을 요구하는지 보고, 사용자 승인으로 해결되는 문제인지 배포·서명·시스템 앱 경계가 필요한 문제인지 분리한다.

공식 문서: [Request runtime permissions](https://developer.android.com/training/permissions/requesting)

### 판단 기준

Permission 노트는 manifest 선언, runtime grant, AppOps, sandbox boundary 가 서로 다른 판단 축임을 구분하는 기준으로 읽는다.

### 경계

권한 요청 UX 와 실제 sensitive operation 성공 여부를 같은 문제로 보지 않는다.
