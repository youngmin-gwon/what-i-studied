---
title: "Android 권한 계약"
tags: ["android", "android/security-privacy"]
---

# Android 권한 계약

Android 권한은 sandbox 밖의 데이터나 기능에 접근하기 위한 사용자·시스템 승인 계약이다. 권한 선언, 런타임 요청, 특수 접근, AppOps, UX 설명, 디버깅을 별도 책임으로 나눈다.

## 정본 노트

- [Permission protection level은 접근 승인 주체를 정의한다](01_inbox/mobile/android/05_security_privacy/permissions-and-sandbox/permission-contracts/permission-protection-level-defines-who-can-grant-access.md)
- [Runtime permission은 사용자에게 기능 사용 시점에 요청하는 접근 계약이다](01_inbox/mobile/android/05_security_privacy/permissions-and-sandbox/permission-contracts/runtime-permission-is-user-mediated-access-contract.md)
- [Special app access는 일반 runtime permission이 아니라 설정 기반 capability다](01_inbox/mobile/android/05_security_privacy/permissions-and-sandbox/permission-contracts/special-app-access-is-settings-mediated-capability.md)
- [AppOps는 권한 이후의 민감 작업 실행 상태를 관찰하고 제어한다](01_inbox/mobile/android/05_security_privacy/permissions-and-sandbox/permission-contracts/appops-observes-and-gates-sensitive-operations-after-permission.md)
- [권한 요청 UX는 최소 권한과 사용 시점 설명으로 설계한다](01_inbox/mobile/android/05_security_privacy/permissions-and-sandbox/permission-contracts/permission-request-ux-uses-minimal-point-of-use-explanation.md)
- [권한 디버깅은 manifest, grant state, AppOps를 분리해 확인한다](01_inbox/mobile/android/05_security_privacy/permissions-and-sandbox/permission-contracts/permission-debugging-separates-manifest-grant-and-appops-state.md)

관련 지도: [Android 플랫폼 보안 경계 계약](01_inbox/mobile/android/05_security_privacy/platform-hardening/platform-security-contracts/platform-security-contracts.md)
