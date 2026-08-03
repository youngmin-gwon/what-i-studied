---
title: "product, vendor, odm, system_ext는 customization ownership을 나눈다"
tags: [android, android/aosp, android/partitions]
aliases: [Android partitions, Vendor partition]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# product, vendor, odm, system_ext는 customization ownership을 나눈다

상위 문서: [Platform customization contracts](01_inbox/mobile/android/01_system_internals/platform-customization/platform-customization-contracts/platform-customization-contracts.md)

Android의 customization은 한 디렉터리에 덧붙이는 작업이 아니라 partition별 ownership을 나누는 작업이다. `system`은 공통 framework와 platform code를 담고, `vendor`는 SoC/vendor implementation을, `odm`은 device maker variation을, `product`와 `system_ext`는 제품별 앱, 설정, framework extension을 담는다.

이 경계는 update와 compatibility를 위해 중요하다. framework가 vendor 구현을 마음대로 깨면 Treble 경계가 무너지고, 제품별 앱과 permission을 잘못된 partition에 넣으면 OTA, factory reset, certification, privileged permission 정책이 꼬인다.

## 판단 기준

- 파일 위치는 “누가 소유하고 언제 업데이트하는가”의 결정이다.
- vendor/odm 변경은 HAL, VINTF, sepolicy와 함께 검증한다.
- product/system_ext 변경은 privileged app, sysconfig, permission allowlist, overlay 정책을 같이 본다.
- partition 경계가 애매한 기능은 update 주체와 compatibility 책임부터 정한다.

관련 노트: [Android 플랫폼 모듈화는 system, vendor, kernel 업데이트 경계를 층위별로 나눈다](01_inbox/mobile/android/01_system_internals/platform-modularity/platform-modularity-contracts/android-platform-modularity-splits-update-boundaries-by-system-layer.md)
