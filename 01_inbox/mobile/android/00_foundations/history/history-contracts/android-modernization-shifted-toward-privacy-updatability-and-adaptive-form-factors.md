---
title: "Android 현대화는 privacy, updatability, adaptive form factor 쪽으로 이동했다"
tags: ["android", "android/foundations"]
aliases: []
date modified: 2026-08-03 16:33:37 +09:00
date created: 2026-07-31 23:04:26 +09:00
---

## Android 현대화는 privacy, updatability, adaptive form factor 쪽으로 이동했다

Android 의 큰 변화는 단순한 UI feature 추가보다 platform constraint 강화에 가깝다. Background execution, permission, package visibility, scoped storage, notification permission, intent hardening 은 앱이 system resource 와 사용자 데이터를 다루는 방식을 바꿨다.

동시에 Mainline, APEX, SDK Extensions, Treble, GKI 는 업데이트와 호환성 경계를 더 잘게 나눴다. Large screen, desktop windowing, XR 같은 form factor 변화는 layout/navigation 을 고정 phone screen 에서 adaptive model 로 옮기고 있다.

history 문서는 이 흐름을 설명하고 세부 구현은 각 canonical map 으로 넘긴다.

관련 노트: [platform modularity](01_inbox/mobile/android/01_system_internals/platform-modularity/android-platform-modularity.md), [large screen](01_inbox/mobile/android/07_platforms/large-screens/large-screen-contracts/large-screen-contracts.md), [XR](01_inbox/mobile/android/07_platforms/xr/xr-contracts/xr-contracts.md), [security practices](01_inbox/mobile/android/05_security_privacy/security-practices/security-practice-contracts/android-security-practice-is-defense-in-depth-not-client-trust.md).

### 판단 기준

새 변화가 privacy 제약 강화, system module 의 독립 업데이트, vendor/framework 호환성, adaptive UI 중 어느 흐름을 바꾸는지 설명할 수 있을 때 이 장기 지도에 연결한다.

### 경계

이 노트는 여러 release 에 걸친 방향만 설명한다. 특정 API 의 도입 시점이나 적용 조건은 version checkpoint 와 해당 canonical area 에서 검증한다.
