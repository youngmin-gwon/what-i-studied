---
title: "AppOps는 권한 외에 앱의 민감한 작업 수행을 세밀하게 제어하고 추적한다"
tags: ["android", "android/glossary"]
aliases: ["App Operations", "AppOpsManager"]
date modified: 2026-08-04 21:00:00 +09:00
date created: 2026-07-31 15:29:55 +09:00
---

## AppOps는 권한 외에 앱의 민감한 작업 수행을 세밀하게 제어하고 추적한다

정의: AppOps 는 permission grant 이후에도 위치, 알림, background access 같은 sensitive operation 을 관찰하거나 차단하는 runtime policy layer 다.

혼동 방지: Manifest permission 이 허용됐다는 사실만으로 모든 operation 이 성공한다고 보면 안 된다. 실제 호출은 permission, AppOps mode, foreground/background 상태, OS version policy 를 함께 통과해야 한다.

정본 링크:

- [AppOps permission contract](../../../05_security_privacy/permissions-and-sandbox/permission-contracts/appops-observes-and-gates-sensitive-operations-after-permission.md)
- [Permission debugging contract](../../../05_security_privacy/permissions-and-sandbox/permission-contracts/permission-debugging-separates-manifest-grant-and-appops-state.md)
