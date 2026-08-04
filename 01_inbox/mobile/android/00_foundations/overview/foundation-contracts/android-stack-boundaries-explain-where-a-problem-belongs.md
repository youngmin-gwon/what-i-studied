---
title: android-stack-boundaries-explain-where-a-problem-belongs
tags: ["android", "android/foundations"]
aliases: []
date modified: 2026-08-03 17:22:46 +09:00
date created: 2026-07-31 23:04:26 +09:00
---

## Android stack boundary 는 문제가 어느 층에 속하는지 판단하게 해 준다

Android 문제를 진단할 때 첫 질문은 "어떤 API 를 썼나"가 아니라 "어느 boundary 가 실패했나"다. UI frame deadline 이면 rendering/runtime 문제이고, app launch 면 Activity/system_server/zygote 문제이며, 외부 호출이면 Intent/Manifest/security boundary 문제다.

Kernel 과 HAL 은 device capability 를 제공하고, native/service layer 는 system policy 를 구현하며, framework 는 app-facing API 와 lifecycle 을 노출한다. 앱 코드는 이 boundary 위에서 상태, navigation, data, background work 를 설계한다.

이 구분을 지키면 같은 내용을 overview, architecture, security, debugging 문서가 반복하지 않는다.

관련 노트: [boot/runtime](../../../01_system_internals/boot-and-runtime/android-boot-and-runtime.md), [graphics/media](../../../01_system_internals/graphics-and-media/android-graphics-media-runtime.md), [app components](../../../02_app_framework/architecture/app-components/android-app-components.md), [debugging](../../../06_testing_performance/debugging/debugging-contracts/debugging-contracts.md).

### 판단 기준

증상의 API 이름이 아니라 마지막으로 성공한 경계와 최초로 실패한 경계를 찾는다. app callback, Binder service, native/HAL, kernel/device 중 증거가 바뀌는 지점을 기준으로 정본을 선택한다.

### 경계

Boundary 분류는 원인 확정이 아니다. 실제 원인은 log, trace, service state, 재현 조건으로 검증하며 상세 진단 절차는 debugging/performance 정본으로 넘긴다.
