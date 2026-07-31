---
title: GMS는 AOSP가 아니라 라이선스된 Google services layer다
tags: [android, android/gms, android/aosp]
aliases: [GMS, Google Mobile Services]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# GMS는 AOSP가 아니라 라이선스된 Google services layer다

상위 문서: [Platform customization contracts](01_inbox/mobile/android/01_system_internals/platform-customization/platform-customization-contracts/platform-customization-contracts.md)

Google Mobile Services(GMS)는 AOSP에 포함된 기본 구성물이 아니라 라이선스와 인증을 전제로 제공되는 Google apps/services layer다. Play Store, Google Play services, Google Sign-In, FCM, Google Maps API 같은 기능은 AOSP-only device에서 자동으로 제공되지 않는다.

앱 관점에서는 “Android 기기”라고 해서 Play services dependency가 항상 만족된다고 볼 수 없다. 플랫폼 관점에서는 GMS 탑재가 기술 통합뿐 아니라 compatibility, certification, distribution 계약과 연결된다.

## 실무 규칙

- Play services 의존 기능은 fallback, feature check, graceful degradation을 둔다.
- FCM, Maps, Sign-In, Play Integrity는 platform API가 아니라 Google service dependency로 분류한다.
- OEM certification 상태는 앱 capability 판단과 배포 전략에 영향을 준다.
- AOSP fork나 custom ROM 문서에서는 GMS 포함 여부를 별도 변수로 둔다.

관련 노트: [Play Integrity token은 서버 검증용 risk signal이지 authorization 자체가 아니다](01_inbox/mobile/android/05_security_privacy/integrity-and-attestation/integrity-contracts/play-integrity-token-is-server-verified-risk-signal-not-authorization.md)
