---
title: "프로세스 우선순위는 메모리 회수 정책 입력이지 앱 상태의 진실이 아니다"
tags: [android, android/system-internals, android/boot-runtime, android/system-server]
aliases: ["프로세스 우선순위는 메모리 회수 정책 입력이지 앱 상태의 진실이 아니다"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# 프로세스 우선순위는 메모리 회수 정책 입력이지 앱 상태의 진실이 아니다

상위 문서: [system_server와 ActivityManager 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/system-server-contracts.md)

Android의 process priority와 OOM adjustment는 메모리 부족 시 어떤 프로세스를 먼저 회수할지 정하는 정책 입력이다. 이것은 앱의 업무 상태가 안전하게 저장됐다는 의미가 아니며, foreground/visible/perceptible/cached 같은 중요도는 언제든 변할 수 있다.

## 실무 규칙

- cached process는 언제든 종료될 수 있다고 가정한다.
- foreground service로 process를 살리는 것은 사용자에게 보이는 장기 작업에만 사용한다.
- process death 복원은 ViewModel이 아니라 persistent state와 SavedStateHandle, repository 경계에서 설계한다.
- memory pressure 분석은 앱 process 내부 메모리와 시스템 importance를 함께 본다.

## 관련 문서

- [ViewModel은 설정 변경 동안 유지되지만 프로세스 사망 복원까지 보장하지 않는다](01_inbox/mobile/android/02_app_framework/architecture/state-management/viewmodel/viewmodel-survives-configuration-change-not-process-death.md)
- [IPC and process contracts](01_inbox/mobile/android/01_system_internals/ipc-and-process/ipc-process-contracts/ipc-process-contracts.md)

공식 문서: [Processes and app lifecycle](https://developer.android.com/guide/components/activities/process-lifecycle)
