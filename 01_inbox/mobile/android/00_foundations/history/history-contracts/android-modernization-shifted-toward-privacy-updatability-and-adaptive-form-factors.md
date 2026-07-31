---
title: android-modernization-shifted-toward-privacy-updatability-and-adaptive-form-factors
tags: ["android", "android/foundations"]
aliases: []
date modified: 2026-08-01 01:08:00 +09:00
date created: 2026-07-31 23:04:26 +09:00
---

## Android 현대화는 privacy, updatability, adaptive form factor 쪽으로 이동했다

Android 의 큰 변화는 단순한 UI feature 추가보다 platform constraint 강화에 가깝다. Background execution, permission, package visibility, scoped storage, notification permission, intent hardening 은 앱이 system resource 와 사용자 데이터를 다루는 방식을 바꿨다.

동시에 Mainline, APEX, SDK Extensions, Treble, GKI 는 업데이트와 호환성 경계를 더 잘게 나눴다. Large screen, desktop windowing, XR 같은 form factor 변화는 layout/navigation 을 고정 phone screen 에서 adaptive model 로 옮기고 있다.

history 문서는 이 흐름을 설명하고 세부 구현은 각 canonical map 으로 넘긴다.

관련 노트: [platform modularity](01_inbox/mobile/android/01_system_internals/platform-modularity/android-platform-modularity.md), [large screen](01_inbox/mobile/android/07_platforms/large-screens/large-screen-contracts/large-screen-contracts.md), [XR](01_inbox/mobile/android/07_platforms/xr/xr-contracts/xr-contracts.md), [security practices](01_inbox/mobile/android/05_security_privacy/security-practices/security-practice-contracts/android-security-practice-is-defense-in-depth-not-client-trust.md).

### 판단 기준

Foundation 노트는 세부 구현을 반복하지 않고 Android 지식이 어느 계층의 문제인지 찾아가는 입구로 사용한다.

### 경계

학습 순서나 역사 설명은 API 목록을 외우는 방향이 아니라 runtime, framework, service, security, tooling boundary 를 구분하는 방향으로 유지한다.
