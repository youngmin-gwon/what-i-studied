---
title: android-system-map
tags: ["android", "android/foundations"]
aliases: []
date modified: 2026-08-05 11:27:58 +09:00
date created: 2026-08-03 16:59:22 +09:00
---

## Android System Map 은 안드로이드의 런타임, 프레임워크, 서비스 계층을 구조화한 지도다

이 문서는 Android 를 처음 볼 때의 system map 이다. 위쪽 앱 API 에서 아래쪽 하드웨어로 내려가는 목록이 아니라, 요청이 어느 책임 경계를 통과하는지 분류하는 지도다. 세부 구현은 각 정본으로 이동한다.

### 계층과 읽는 순서

1. [계층형 플랫폼](./foundation/android-is-layered-mobile-platform-not-just-an-app-sdk.md) 에서 kernel, native/HAL, runtime, framework service, app framework 를 한 그림으로 잡는다.
2. [Stack boundary](./foundation/android-stack-boundaries-explain-where-a-problem-belongs.md) 에서 증상과 실패 계층을 분리한다.
3. [앱 실행 경로](./foundation/app-launch-crosses-launcher-system-server-zygote-and-activitythread.md) 로 process 생성과 component lifecycle 이 다른 책임임을 확인한다.
4. [보안 계층](./foundation/android-security-is-layered-from-uid-sandbox-to-permissions-and-verified-boot.md) 과 [camera 경로 예시](./foundation/camera-example-crosses-permission-intent-ui-media-hal-and-storage-boundaries.md) 로 하나의 기능이 여러 경계를 지나는 방식을 연습한다.

[Foundation Contracts](./foundation/foundation.md) 는 이 순서를 구성하는 원자 노트의 역할 차이와 추가 기준을 관리하는 하위 지도다.

### Foundation Notes

- [Android는 앱 SDK만이 아니라 계층형 모바일 플랫폼이다](./foundation/android-is-layered-mobile-platform-not-just-an-app-sdk.md)
- [Android stack boundary는 문제가 어느 층에 속하는지 판단하게 해 준다](./foundation/android-stack-boundaries-explain-where-a-problem-belongs.md)
- [앱 실행은 Launcher, system_server, Zygote, ActivityThread를 지나는 경로다](./foundation/app-launch-crosses-launcher-system-server-zygote-and-activitythread.md)
- [Android 보안은 UID sandbox, permission, SELinux, verified boot가 나뉜 계층이다](./foundation/android-security-is-layered-from-uid-sandbox-to-permissions-and-verified-boot.md)
- [Android 지식 지도는 runtime, app framework, services, security, tooling으로 나누어 읽는다](./foundation/android-knowledge-map-is-organized-by-runtime-app-framework-services-security-and-tooling.md)
- [사진 찍기 예시는 permission, intent, UI, media, HAL, storage 경계를 함께 지난다](./foundation/camera-example-crosses-permission-intent-ui-media-hal-and-storage-boundaries.md)

### 문제별 진입 경로

- Runtime/process: [boot/runtime](../../01_system_internals/boot-and-runtime/android-boot-and-runtime.md), [system_server](../../01_system_internals/boot-and-runtime/system-server/system-server.md), [Zygote/runtime](../../01_system_internals/boot-and-runtime/zygote-runtime/zygote-runtime.md)
- Kernel/HAL: [kernel](../../01_system_internals/kernel-and-hal/android-kernel-runtime.md), [HAL/native boundary](../../01_system_internals/kernel-and-hal/hal-native-boundary.md)
- App framework: [app architecture](../../02_app_framework/architecture/android-app-architecture.md), [app components](../../02_app_framework/architecture/app-components/android-app-components.md), [Context](../../02_app_framework/architecture/context/context.md)
- UI/data: [Compose runtime](../../02_app_framework/jetpack-compose/runtime/compose-runtime-and-state-model.md), [Compose UI](../../02_app_framework/jetpack-compose/layout-and-ui/compose-layout-animation-accessibility.md), [storage](../../02_app_framework/data/storage/persistence.md)
- Security/debugging: [security](../../05_security_privacy/security-practices/security-practice/android-security-practice-is-defense-in-depth-not-client-trust.md), [debugging](../../06_testing_performance/debugging/debugging/debugging.md), [performance](../../06_testing_performance/performance/performance/performance.md)
- `onCreate` 이전 launch 지연이나 process 재생성은 Runtime/process 에서 시작한다.
- device 별 camera/audio/sensor 차이는 앱 API 사용법을 확인한 뒤 Kernel/HAL 경계로 내려간다.
- lifecycle, state ownership, navigation 문제는 App framework 에서 시작한다.
- frame 지연은 UI state 계산, main thread, rendering/composition 을 차례로 나누고 UI/data 와 performance 경로를 함께 본다.
- 호출이 `SecurityException` 또는 정책상 거절로 끝나면 permission grant, AppOps, component export, platform policy 를 Security/debugging 에서 분리한다.

### 새 노트 경계

여러 계층을 연결해 문제 위치를 찾게 하는 내용만 이 map 에 둔다. 한 계층의 상세 계약은 해당 영역에 원자 노트로 만들고 여기서는 한 문장과 링크만 유지한다.
