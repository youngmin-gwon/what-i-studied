---
title: foundation-contracts
tags: ["android", "android/foundations", "index", "map"]
aliases: ["Foundation Contracts Index", "안드로이드 플랫폼 핵심 계약 인덱스"]
date modified: 2026-08-06 16:40:00 +09:00
date created: 2026-08-03 16:59:22 +09:00
---

## Foundation Contracts 는 안드로이드 플랫폼을 관통하는 근본 원칙과 계층 계약 모음이다

본 지도는 안드로이드 시스템 전체를 조망하고 문제 발생 시 최우선 탐색 경로를 결정하는 **원자적 기본 계약(Foundation Contracts) 총괄 인덱스 문서**이다.

처음 읽을 때는 **[1. 플랫폼 계층 구조] ➔ [2. 장애 진단 경계] ➔ [3. 구체 실행 경로]** 순서로 학습을 진행하는 것을 권장한다.

---

### 1. 플랫폼 계층 구조 (Platform Model)

- [Android는 앱 SDK만이 아니라 계층형 모바일 플랫폼이다](android-is-layered-mobile-platform-not-just-an-app-sdk.md)
  - 하드웨어, [Linux Kernel](../../../../../../operating-systems/linux-kernel.md), [HAL](../../../01_system_internals/hal.md), [ART Runtime](../../../01_system_internals/art.md), [system_server](../../../04_system_services/system-server.md), [App Framework](../../../02_app_framework/viewmodel.md)까지 6대 계층 스택 총괄 구조
- [Android 지식 지도는 runtime, app framework, services, security, tooling으로 나누어 읽는다](android-knowledge-map-is-organized-by-runtime-app-framework-services-security-and-tooling.md)
  - 저장소 전체 지식 영역(Canonical Areas) 탐색 지도

---

### 2. 장애 진단 및 보안 경계 (Diagnostic & Security Boundaries)

- [Android stack boundary는 문제가 어느 층에 속하는지 판단하게 해 준다](android-stack-boundaries-explain-where-a-problem-belongs.md)
  - 증상별로 어느 계층(App, Framework, [system_server](../../../04_system_services/system-server.md), [HAL](../../../01_system_internals/hal.md), [Kernel](../../../../../../operating-systems/linux-kernel.md))에 문제가 발생했는지 파악하는 4단계 분류법
- [Android 보안은 UID sandbox, permission, SELinux, verified boot가 나뉜 계층이다](android-security-is-layered-from-uid-sandbox-to-permissions-and-verified-boot.md)
  - [AppOps & 권한](../../../05_security_privacy/appops-and-permissions.md), UID 샌드박스, SELinux 등 5가지 독립 보안 게이트 분해 분석

---

### 3. 구체적 실행 경로 및 시나리오 (End-to-End Execution Flows)

- [앱 실행은 Launcher, system_server, Zygote, ActivityThread를 지나는 경로다](app-launch-crosses-launcher-system-server-zygote-and-activitythread.md)
  - Cold Launch 시 [system_server](../../../04_system_services/system-server.md) ➔ [Zygote IPC](../../../01_system_internals/zygote.md) ➔ [ActivityThread](../../../../../../02_references/computer-science/thread.md) 메인 루프 가동 및 TTID/TTFD 렌더링 경로
- [사진 찍기 예시는 permission, intent, UI, media, HAL, storage 경계를 함께 지난다](camera-example-crosses-permission-intent-ui-media-hal-and-storage-boundaries.md)
  - 외부 카메라 Intent 위임 vs 앱 내 [CameraX / HAL 세션](../../../01_system_internals/hal.md) 직접 점유 2대 경로 비교

---

### 🗺️ 상위 지도 연결

- 상위 시스템 지도: [Android System Map](../android-system-map.md)
