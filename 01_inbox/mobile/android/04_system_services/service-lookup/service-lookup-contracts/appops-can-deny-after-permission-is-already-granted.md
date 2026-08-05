---
title: appops-can-deny-after-permission-is-already-granted
tags: ["android", "android/system-services"]
aliases: []
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-03 17:17:39 +09:00
---

## AppOps 는 permission 승인 뒤에도 실행 시점 정책을 추가로 거부할 수 있다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](../../android-system-services-and-device-capabilities.md)

관련 지도: [시스템 서비스 접근 공통 계약](./service-lookup-contracts.md)

### 핵심 정의

**AppOps**(App Operations, `AppOpsManager`)는 런타임 권한(Permission) 승인 상태와 별개로 동작하는 동적 실행 시점 정책 계층이다. 앱이 dangerous permission을 정상적으로 부여받았더라도, 해당 동작에 대응하는 app-op이 `MODE_IGNORED` 또는 `MODE_ERRORED` 상태면 시스템은 데이터 접근 요청을 조용히 무시하거나 거부한다.

### 메커니즘

각 dangerous permission 은 대응하는 app-op 코드를 가진다(예: `android.permission.CAMERA` ↔ `OP_CAMERA`). system_server 서비스는 permission 검사를 통과한 뒤 별도로 `AppOpsManager.noteOp()` 또는 `checkOp()` 를 호출해 app-op 모드를 확인한다.

app-op 모드는 사용자의 세부 설정(예: 위치 접근을 "이 앱 사용 중에만 허용"), 배터리/개인정보 관리 기능의 자동 개입, 또는 OS 의 background 제한에 의해 permission grant 상태와 독립적으로 바뀔 수 있다. `noteOp()` 호출 시점은 대개 실제 데이터 접근 순간이며, 이 시점 기록이 시스템 설정의 "최근 접근" UI 에 나타난다.

### 판단 기준

- permission 이 granted 인데 API 가 예외 없이 빈 데이터나 stale 데이터를 반환하면 permission 보다 AppOps 모드를 먼저 의심한다.
- app-op 모드는 사용자가 설정 화면에서 앱별로 개별 조정할 수 있으므로, 같은 permission 을 가진 두 사용자 기기에서 동작이 다를 수 있다.
- Android 10+ 위치의 "이 앱 사용 중에만" 옵션처럼, 하나의 permission 이 여러 app-op 세분화 상태를 가질 수 있다.

### 경계

- 이 노트는 AppOps 가 permission 과 별도 계층이라는 사실과 관찰 지점까지만 다룬다. 개별 서비스(location, camera 등)에서 AppOps 가 구체적으로 어떤 실패로 나타나는지는 각 클러스터 노트가 다룬다.
- 앱이 스스로 AppOps 를 우회하거나 임의로 재정의하는 것은 시스템 권한 없이는 불가능하며, 이 노트는 그런 우회 방법을 다루지 않는다.

### 관찰 가능한 신호

`adb shell dumpsys appops` 로 패키지별 app-op 모드와 마지막 접근 시각을 확인할 수 있다. `adb shell cmd appops set <pkg> <op> <mode>` 로 특정 op 를 강제 변경해 재현 테스트를 할 수 있다.

### 공식 문서

- https://developer.android.com/reference/android/app/AppOpsManager