---
title: oem-api-is-compatibility-risk-unless-backed-by-stable-contract
tags: [android, android/api, android/oem]
aliases: [OEM API]
date modified: 2026-08-03 17:26:29 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## OEM API 는 stable contract 가 없으면 compatibility risk 다

상위 문서: [Platform customization contracts](01_inbox/mobile/android/01_system_internals/platform-customization/platform-customization-contracts/platform-customization-contracts.md)

OEM-specific API 는 특정 제조사나 기기군에서만 동작하는 private 또는 semi-public surface 다. 안정적인 SDK, permission, feature declaration, fallback 계약이 없으면 앱은 OS update, device variant, region/carrier build 에 취약해진다.

플랫폼 개발자는 OEM API 를 만들 때 caller identity, permission, versioning, behavior compatibility 를 API 계약으로 문서화해야 한다. 앱 개발자는 public Android SDK 나 Jetpack API 로 대체 가능한지 먼저 확인해야 한다.

### 실무 규칙

- reflection 으로 hidden API 를 호출하는 방식은 release compatibility risk 로 분류한다.
- OEM feature 는 feature flag 와 runtime availability check 를 둔다.
- permission 이 signature/privileged 이면 일반 앱 배포 전략과 분리한다.
- 같은 제조사라도 device, region, carrier variant 별 차이를 테스트한다.

관련 노트: [앱은 Mainline package 이름보다 API와 feature availability를 확인해야 한다](01_inbox/mobile/android/01_system_internals/platform-modularity/platform-modularity-contracts/apps-should-check-api-feature-availability-not-mainline-package-names.md)
