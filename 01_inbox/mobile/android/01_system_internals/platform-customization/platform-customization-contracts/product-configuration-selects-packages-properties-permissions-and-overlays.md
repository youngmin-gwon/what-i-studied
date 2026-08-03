---
title: "product configuration은 package, property, permission, overlay를 선택한다"
tags: [android, android/aosp, android/build]
aliases: [Android product configuration]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# product configuration은 package, property, permission, overlay를 선택한다

상위 문서: [Platform customization contracts](01_inbox/mobile/android/01_system_internals/platform-customization/platform-customization-contracts/platform-customization-contracts.md)

Android product configuration은 “어떤 앱을 넣을지”만 고르는 파일이 아니다. product makefile과 Soong/Make 설정은 package inclusion, system property, permission XML, feature declaration, overlay, partition image 구성을 함께 결정한다.

따라서 customization을 앱 설치 목록으로만 다루면 부팅, 권한, API availability, resource 값, CTS 결과가 서로 어긋난다. 제품 설정은 device behavior의 선언적 계약으로 관리해야 한다.

## 실무 규칙

- 앱 추가는 privileged permission allowlist와 shared UID, signing key 요구사항을 같이 확인한다.
- system property는 runtime feature flag가 아니라 boot-time/system policy 입력일 수 있다.
- feature XML은 Play/device capability 판정에도 영향을 준다.
- overlay와 product package 선택은 같은 변경이라도 책임 경계가 다르다.

관련 노트: [RRO는 target APK를 다시 빌드하지 않고 resource를 바꾼다](01_inbox/mobile/android/01_system_internals/platform-customization/platform-customization-contracts/rro-changes-resources-without-rebuilding-target-apk.md)
