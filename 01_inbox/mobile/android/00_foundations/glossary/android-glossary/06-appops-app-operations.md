---
title: "AppOps"
tags: ["android", "android/glossary"]
aliases: ["App Operations", "AppOpsManager"]
---

# AppOps

정의: AppOps는 permission grant 이후에도 위치, 알림, background access 같은 sensitive operation을 관찰하거나 차단하는 runtime policy layer다.

혼동 방지: Manifest permission이 허용됐다는 사실만으로 모든 operation이 성공한다고 보면 안 된다. 실제 호출은 permission, AppOps mode, foreground/background 상태, OS version policy를 함께 통과해야 한다.

정본 링크:
- [AppOps permission contract](01_inbox/mobile/android/05_security_privacy/permissions-and-sandbox/permission-contracts/appops-observes-and-gates-sensitive-operations-after-permission.md)
- [Permission debugging contract](01_inbox/mobile/android/05_security_privacy/permissions-and-sandbox/permission-contracts/permission-debugging-separates-manifest-grant-and-appops-state.md)
