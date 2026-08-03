---
title: permission-request-ux-uses-minimal-point-of-use-explanation
tags: ["android", "android/security-privacy"]
aliases: []
date modified: 2026-08-03 18:14:09 +09:00
date created: 2026-08-01 00:03:59 +09:00
---

## 권한 요청 UX 는 최소 권한과 사용 시점 설명으로 설계한다

권한 요청 UX 의 기준은 최소 권한과 point-of-use 다. 앱 시작 시 모든 권한을 한 번에 요청하는 방식은 사용자가 기능과 데이터 접근 이유를 연결하기 어렵게 만든다.

먼저 권한 없이 가능한 platform API 나 picker 가 있는지 검토한다. 권한이 필요하다면 사용자가 해당 기능을 시작한 시점에 요청하고, 거부 시에도 앱을 계속 사용할 수 있는 제한 모드를 제공한다.

설명 UI 는 권한 이름보다 기능 결과를 말해야 한다. "카메라 권한 필요"보다 "카드를 촬영해 번호를 입력하려면 카메라 접근이 필요하다"처럼 사용자의 행동과 데이터 접근을 연결한다.

공식 문서: [Request runtime permissions](https://developer.android.com/training/permissions/requesting)

### 판단 기준

Permission 노트는 manifest 선언, runtime grant, AppOps, sandbox boundary 가 서로 다른 판단 축임을 구분하는 기준으로 읽는다.

### 경계

권한 요청 UX 와 실제 sensitive operation 성공 여부를 같은 문제로 보지 않는다.
