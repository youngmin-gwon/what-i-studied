---
title: "OEM API는 stable contract가 없으면 compatibility risk다"
tags: [android, android/oem, android/api]
aliases: [OEM API]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# OEM API는 stable contract가 없으면 compatibility risk다

상위 문서: [Platform customization contracts](01_inbox/mobile/android/01_system_internals/platform-customization/platform-customization-contracts/platform-customization-contracts.md)

OEM-specific API는 특정 제조사나 기기군에서만 동작하는 private 또는 semi-public surface다. 안정적인 SDK, permission, feature declaration, fallback 계약이 없으면 앱은 OS update, device variant, region/carrier build에 취약해진다.

플랫폼 개발자는 OEM API를 만들 때 caller identity, permission, versioning, behavior compatibility를 API 계약으로 문서화해야 한다. 앱 개발자는 public Android SDK나 Jetpack API로 대체 가능한지 먼저 확인해야 한다.

## 실무 규칙

- reflection으로 hidden API를 호출하는 방식은 release compatibility risk로 분류한다.
- OEM feature는 feature flag와 runtime availability check를 둔다.
- permission이 signature/privileged이면 일반 앱 배포 전략과 분리한다.
- 같은 제조사라도 device, region, carrier variant별 차이를 테스트한다.

관련 노트: [앱은 Mainline package 이름보다 API와 feature availability를 확인해야 한다](01_inbox/mobile/android/01_system_internals/platform-modularity/platform-modularity-contracts/apps-should-check-api-feature-availability-not-mainline-package-names.md)
