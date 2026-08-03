---
title: special-app-access-is-settings-mediated-capability
tags: ["android", "android/security-privacy"]
aliases: []
date modified: 2026-08-03 18:14:10 +09:00
date created: 2026-08-01 00:03:59 +09:00
---

## Special app access 는 일반 runtime permission 이 아니라 설정 기반 capability 다

Special app access 는 일반 runtime permission dialog 로 얻는 권한이 아니다. 다른 앱 위에 그리기, 시스템 설정 변경, 모든 파일 접근처럼 위험도가 큰 capability 는 별도 설정 화면, 정책 검토, 사용자 확인을 통해 관리된다.

이 권한들은 "요청하면 허용될 수 있는 기능"이 아니라 앱의 제품 요구사항이 정말 해당 capability 를 필요로 하는지 먼저 증명해야 하는 영역이다. Play 정책 검토 대상이 될 수 있고, 사용자가 설정에서 언제든 끌 수 있다.

따라서 구현은 fallback 을 포함해야 한다. capability 가 거부되거나 회수되어도 앱은 핵심 기능을 설명하고 제한된 대안으로 동작해야 한다.

### 판단 기준

Permission 노트는 manifest 선언, runtime grant, AppOps, sandbox boundary 가 서로 다른 판단 축임을 구분하는 기준으로 읽는다.

### 경계

권한 요청 UX 와 실제 sensitive operation 성공 여부를 같은 문제로 보지 않는다.
