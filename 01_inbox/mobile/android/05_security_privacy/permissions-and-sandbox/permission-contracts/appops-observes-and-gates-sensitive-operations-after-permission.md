---
title: appops-observes-and-gates-sensitive-operations-after-permission
tags: ["android", "android/security-privacy"]
aliases: []
date modified: 2026-08-03 18:13:28 +09:00
date created: 2026-08-01 00:03:59 +09:00
---

## AppOps 는 권한 이후의 민감 작업 실행 상태를 관찰하고 제어한다

AppOps 는 permission 과 별개로 특정 민감 operation 의 실제 사용 상태를 기록하거나 제한하는 Android 내부 제어 계층이다. 권한이 허용되어도 operation 이 정책, 사용자 설정, privacy dashboard, 자동 회수 상태에 의해 제한될 수 있다.

권한 디버깅에서 manifest 와 runtime grant 만 확인하면 부족하다. 카메라, 마이크, 위치처럼 민감한 operation 은 시스템 UI 의 privacy indicator, dashboard, AppOps 상태와 함께 봐야 한다.

앱 설계 관점에서 AppOps 는 "권한을 받았으니 항상 가능하다"는 가정을 깨는 계층이다. 민감 API 호출 직전마다 현재 상태를 확인하고 실패를 정상 경로로 처리한다.

### 판단 기준

Permission 노트는 manifest 선언, runtime grant, AppOps, sandbox boundary 가 서로 다른 판단 축임을 구분하는 기준으로 읽는다.

### 경계

권한 요청 UX 와 실제 sensitive operation 성공 여부를 같은 문제로 보지 않는다.
