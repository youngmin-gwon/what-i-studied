---
title: "system_server의 서비스는 호출자 UID/PID로 권한을 검사한다"
tags: ["android", "android/system-services"]
---

# system_server의 서비스는 호출자 UID/PID로 권한을 검사한다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](01_inbox/mobile/android/04_system_services/android-system-services-and-device-capabilities.md)
관련 지도: [시스템 서비스 접근 공통 계약](01_inbox/mobile/android/04_system_services/service-lookup/service-lookup-contracts/service-lookup-contracts.md)

## 핵심 정의

Binder 호출이 system_server에 도달하면, 서비스는 호출자가 선언한 권한 문자열을 신뢰하지 않는다. 대신 커널이 제공하는 호출자의 실제 UID/PID를 `Binder.getCallingUid()` / `Binder.getCallingPid()`로 조회하고, 그 UID가 필요한 permission을 실제로 부여받았는지 `PackageManager`/권한 시스템에 다시 질의한다.

## 메커니즘

1. 앱 프로세스가 Binder 호출을 보낸다.
2. 커널 Binder 드라이버가 호출자의 실제 UID/PID를 요청에 첨부한다. 이 값은 앱이 위조할 수 없다.
3. system_server 서비스는 `checkPermission()` 계열 API로 해당 UID가 필요한 permission을 가졌는지 확인한다.
4. permission이 없으면 `SecurityException`을 던지거나 조용히 실패값을 반환한다(서비스마다 다르다).

이 검사는 앱이 매니페스트에 permission을 선언했는지가 아니라, 설치 시점/런타임에 사용자가 실제로 그 permission을 부여했는지를 본다.

## 판단 기준

- "매니페스트에 permission을 선언했다"와 "런타임에 permission이 grant 상태다"는 다른 사실이다. dangerous permission은 사용자가 거부하거나 나중에 취소할 수 있다.
- 같은 permission이라도 서비스마다 실패 처리 방식이 다르다(예외 vs 빈 리스트 vs null). 각 서비스 노트에서 이 차이를 확인해야 한다.
- 프로세스 간 신뢰 경계는 UID이지 패키지 이름이 아니다. 한 UID를 여러 패키지가 공유하는 `sharedUserId` 구성(레거시)에서는 이 구분이 중요하다.

## 경계

- 이 노트는 permission 승인 여부까지만 다룬다. permission이 승인된 뒤 AppOps가 추가로 거부하는 계층은 [AppOps는 permission 승인 뒤에도 실행 시점 정책을 추가로 거부할 수 있다](01_inbox/mobile/android/04_system_services/service-lookup/service-lookup-contracts/appops-can-deny-after-permission-is-already-granted.md)가 다룬다.
- SELinux 라벨 기반의 커널/native 서비스 접근 통제는 `05_security_privacy/platform-hardening`이 다룬다.

## 관찰 가능한 신호

`adb shell dumpsys package <pkg>`의 `runtime permissions` 섹션에서 실제 grant 상태를 확인할 수 있다. permission이 거부됐는데 앱이 계속 호출을 시도하면 logcat에 `SecurityException` 또는 서비스별 경고가 남는다.

## 공식 문서

- https://developer.android.com/guide/topics/permissions/overview
