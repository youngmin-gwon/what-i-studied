---
title: system-server-contracts
tags: [android, android/boot-runtime, android/system-internals, android/system-server]
aliases: ["system_server와 ActivityManager 계약"]
date modified: 2026-08-03 17:23:57 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## system_server 와 ActivityManager 계약

`system_server` 는 framework service 를 시작하고, ActivityManager 계층은 앱 process, component lifecycle, task, ANR, memory pressure 대응을 조율한다.

### 정본 노트

- [system_server는 framework service를 한 프로세스 안에서 시작한다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/system-server-starts-framework-services-in-one-process.md)
- [system service는 Binder endpoint이자 플랫폼 정책 집행자다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/system-service-is-binder-endpoint-and-platform-policy-enforcer.md)
- [AMS는 앱 프로세스와 컴포넌트 lifecycle을 조율한다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/ams-coordinates-app-process-and-component-lifecycle.md)
- [ATMS는 activity, task, back stack 전이를 담당한다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/atms-owns-activity-task-and-back-stack-transitions.md)
- [프로세스 우선순위는 메모리 회수 정책 입력이지 앱 상태의 진실이 아니다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/process-priority-is-memory-reclaim-policy-input-not-app-state-truth.md)
- [ANR은 단일 timeout 숫자가 아니라 responsiveness 계약 위반이다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/anr-is-responsiveness-contract-violation-not-single-timeout.md)
- [Rescue Party는 반복되는 system failure를 단계적으로 복구한다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/rescue-party-recovers-repeated-system-failures-in-stages.md)
- [dumpsys는 system service의 현재 상태를 보는 inspection interface다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/dumpsys-is-system-service-state-inspection-interface.md)

### 경계 규칙

- app component API 설명은 app framework 정본으로 두고, 이 묶음은 system_server 가 lifecycle 과 policy 를 조율하는 경계를 다룬다.
- Binder 의 transaction/thread pool 세부는 IPC 정본으로 넘기고, system service 는 Binder endpoint 라는 사실만 연결한다.
- LMKD/PSI 같은 memory pressure 구현은 kernel 정본으로 넘기고, 이 묶음은 process importance 와 app lifecycle 신호를 다룬다.

관련 지도: [Android App Components](01_inbox/mobile/android/02_app_framework/architecture/app-components/android-app-components.md), [IPC and process contracts](01_inbox/mobile/android/01_system_internals/ipc-and-process/ipc-process-contracts/ipc-process-contracts.md)
