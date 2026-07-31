---
title: "Android 지식 지도는 runtime, app framework, services, security, tooling으로 나누어 읽는다"
tags: ["android", "android/foundations"]
---

# Android 지식 지도는 runtime, app framework, services, security, tooling으로 나누어 읽는다

Android 학습 순서는 API 이름보다 책임 영역으로 잡는 편이 오래 간다. system internals는 boot/runtime, process, kernel/HAL, graphics/media를 다루고, app framework는 components, Context, state, Compose, data, navigation을 다룬다.

system services는 background work, notification, NFC, assistant/app functions처럼 OS capability와 연결된 주제를 맡는다. security/privacy는 permission, sandbox, attestation, secure storage를 맡고, testing/performance는 검증과 진단 도구를 맡는다.

이 map은 입문자가 "다음에 무엇을 읽어야 하는가"를 결정하기 위한 문서이고, 각 세부 주제를 다시 설명하지 않는다.

관련 노트: [platform modularity](01_inbox/mobile/android/01_system_internals/platform-modularity/android-platform-modularity.md), [packaging/deployment](01_inbox/mobile/android/03_packaging_deployment/android-packaging-deployment.md), [platforms/form factors](01_inbox/mobile/android/07_platforms/android-platforms-and-form-factors.md).

## 판단 기준

Foundation 노트는 세부 구현을 반복하지 않고 Android 지식이 어느 계층의 문제인지 찾아가는 입구로 사용한다.

## 경계

학습 순서나 역사 설명은 API 목록을 외우는 방향이 아니라 runtime, framework, service, security, tooling boundary를 구분하는 방향으로 유지한다.
