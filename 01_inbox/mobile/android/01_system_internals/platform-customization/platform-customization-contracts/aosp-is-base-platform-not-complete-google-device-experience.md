---
title: AOSP는 완성된 Google 기기 경험이 아니라 기본 플랫폼이다
tags: [android, android/aosp]
aliases: [AOSP, Android Open Source Project]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# AOSP는 완성된 Google 기기 경험이 아니라 기본 플랫폼이다

상위 문서: [Platform customization contracts](01_inbox/mobile/android/01_system_internals/platform-customization/platform-customization-contracts/platform-customization-contracts.md)

AOSP는 Android framework, system apps, native services, build system, compatibility 기준을 제공하는 open source platform이다. 하지만 Play Store, Google Play services, Google apps, Pixel 전용 기능은 AOSP 자체에 포함된다고 가정하면 안 된다.

이 구분은 앱 개발자와 플랫폼 개발자 모두에게 중요하다. 앱이 Google Play services API에 의존하면 AOSP-only device에서는 같은 방식으로 동작하지 않을 수 있고, OEM은 AOSP 위에 device-specific hardware, vendor implementation, product policy를 조립해야 한다.

## 판단 기준

- “Android에서 된다”와 “GMS 인증 기기에서 된다”를 구분한다.
- platform API, Google Play services API, OEM private API를 같은 안정성으로 보지 않는다.
- 기기 기능은 AOSP source 존재 여부가 아니라 feature declaration, HAL, permission, certification 상태로 확인한다.

관련 노트: [GMS는 AOSP가 아니라 라이선스된 Google services layer다](01_inbox/mobile/android/01_system_internals/platform-customization/platform-customization-contracts/gms-is-licensed-google-services-layer-not-aosp.md)
