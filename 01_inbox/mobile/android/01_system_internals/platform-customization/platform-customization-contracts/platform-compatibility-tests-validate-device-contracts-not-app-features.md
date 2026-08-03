---
title: "Platform compatibility test는 앱 기능이 아니라 device contract를 검증한다"
tags: [android, android/aosp, android/testing]
aliases: [CTS, VTS, GTS]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# Platform compatibility test는 앱 기능이 아니라 device contract를 검증한다

상위 문서: [Platform customization contracts](01_inbox/mobile/android/01_system_internals/platform-customization/platform-customization-contracts/platform-customization-contracts.md)

CTS, VTS, GTS 같은 platform compatibility test는 앱 기능의 QA라기보다 device가 Android compatibility contract를 지키는지 확인하는 release gate다. API behavior, permission, security, HAL/VINTF, media, graphics, networking, Google service integration 같은 범위를 나눠 검증한다.

따라서 테스트 실패는 단순히 “테스트가 까다롭다”가 아니라 platform contract 위반일 수 있다. 문제를 우회하기보다 실패가 어느 layer의 계약을 말하는지 먼저 분류해야 한다.

## 실무 규칙

- CTS 실패는 app behavior, framework API, permission policy를 먼저 본다.
- VTS 실패는 HAL, VINTF, vendor implementation 경계를 본다.
- GTS 실패는 Google service integration과 certification 요구사항을 별도로 본다.
- 테스트 로그는 build fingerprint, target image, device state와 함께 보관한다.

관련 노트: [Testing and quality contracts](01_inbox/mobile/android/06_testing_performance/testing/testing-quality-contracts/testing-quality-contracts.md)
