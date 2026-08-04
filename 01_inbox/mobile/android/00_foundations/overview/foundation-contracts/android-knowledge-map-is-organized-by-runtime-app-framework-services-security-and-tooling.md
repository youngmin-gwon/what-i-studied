---
title: android-knowledge-map-is-organized-by-runtime-app-framework-services-security-and-tooling
tags: ["android", "android/foundations"]
aliases: []
date modified: 2026-08-03 17:22:43 +09:00
date created: 2026-07-31 23:04:26 +09:00
---

## Android 지식 지도는 runtime, app framework, services, security, tooling 으로 나누어 읽는다

Android 학습 순서는 API 이름보다 책임 영역으로 잡는 편이 오래 간다. system internals 는 boot/runtime, process, kernel/HAL, graphics/media 를 다루고, app framework 는 components, Context, state, Compose, data, navigation 을 다룬다.

system services 는 background work, notification, NFC, assistant/app functions 처럼 OS capability 와 연결된 주제를 맡는다. security/privacy 는 permission, sandbox, attestation, secure storage 를 맡고, testing/performance 는 검증과 진단 도구를 맡는다.

이 map 은 입문자가 "다음에 무엇을 읽어야 하는가"를 결정하기 위한 문서이고, 각 세부 주제를 다시 설명하지 않는다.

관련 노트: [platform modularity](../../../01_system_internals/platform-modularity/android-platform-modularity.md), [packaging/deployment](../../../03_packaging_deployment/android-packaging-deployment.md), [platforms/form factors](../../../07_platforms/android-platforms-and-form-factors.md).

### 판단 기준

문제를 배치할 때 실행·process·hardware 원인은 system internals, 앱 상태와 API 조합은 app framework, OS capability 사용 정책은 system services, 접근 통제는 security/privacy, 재현과 측정은 testing/performance 로 보낸다.

### 경계

한 문제가 여러 영역을 지나면 최초 실패를 소유한 영역을 중심으로 두고 나머지는 관련 노트로 연결한다. 이 노트에는 각 영역의 상세 목차를 복제하지 않는다.
