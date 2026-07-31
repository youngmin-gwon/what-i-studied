---
title: "Runtime permission은 사용자에게 기능 사용 시점에 요청하는 접근 계약이다"
tags: ["android", "android/security-privacy"]
---

# Runtime permission은 사용자에게 기능 사용 시점에 요청하는 접근 계약이다

Runtime permission은 앱이 민감 데이터나 기능을 사용하려는 순간 사용자에게 승인받는 계약이다. Android 6.0(API 23) 이상에서 dangerous permission은 manifest 선언만으로 충분하지 않고, 실행 중에 상태를 확인한 뒤 요청해야 한다.

요청 흐름은 기능 사용 시점에서 시작한다. 먼저 이미 승인되었는지 확인하고, 필요하면 rationale UI로 이유를 설명한 뒤 system permission dialog를 호출한다. 사용자가 거부하면 기능을 중단하거나 제한하되 앱 전체를 막지 않는 degrade 경로를 제공한다.

권한 그룹이나 다이얼로그 문구에 앱 로직을 의존시키지 않는다. 시스템은 권한 그룹과 UI를 바꿀 수 있으므로 앱은 필요한 개별 권한, 실패 시 동작, 재요청 조건을 명시적으로 설계한다.

관련 노트: [권한 요청 UX는 최소 권한과 사용 시점 설명으로 설계한다](01_inbox/mobile/android/05_security_privacy/permissions-and-sandbox/permission-contracts/permission-request-ux-uses-minimal-point-of-use-explanation.md)

공식 문서: [Request runtime permissions](https://developer.android.com/training/permissions/requesting)
