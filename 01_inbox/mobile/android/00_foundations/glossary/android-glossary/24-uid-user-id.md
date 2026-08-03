---
title: "UID는 안드로이드에서 앱별로 독립된 샌드박스와 권한 경계를 식별하는 단위다"
tags: ["android", "android/glossary"]
aliases: ["Android UID", "Linux UID"]
date modified: 2026-08-01 01:07:50 +09:00
date created: 2026-07-31 15:29:55 +09:00
---

# UID는 안드로이드에서 앱별로 독립된 샌드박스와 권한 경계를 식별하는 단위다

정의: UID 는 Android app sandbox 의 기본 identity 이며, process, file ownership, permission, resource accounting 의 경계를 나누는 Linux user id 다.

혼동 방지: UID 는 로그인 사용자 계정과 같은 개념이 아니다. Android 에서는 앱 설치 단위와 sharedUserId 같은 platform contract 가 UID boundary 를 결정한다.

정본 링크:

- [Android app sandbox](01_inbox/mobile/android/05_security_privacy/platform-hardening/platform-security-contracts/android-app-sandbox-is-uid-and-process-boundary.md)
- [Permission contracts](01_inbox/mobile/android/05_security_privacy/permissions-and-sandbox/permission-contracts/permission-contracts.md)
