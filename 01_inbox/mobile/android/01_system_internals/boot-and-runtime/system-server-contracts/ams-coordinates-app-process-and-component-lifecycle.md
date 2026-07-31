---
title: "AMS는 앱 프로세스와 컴포넌트 lifecycle을 조율한다"
tags: [android, android/system-internals, android/boot-runtime, android/system-server]
aliases: ["AMS는 앱 프로세스와 컴포넌트 lifecycle을 조율한다"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# AMS는 앱 프로세스와 컴포넌트 lifecycle을 조율한다

상위 문서: [system_server와 ActivityManager 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/system-server-contracts.md)

ActivityManagerService는 앱 프로세스 생성, service, broadcast, provider, process importance, permission check 같은 앱 실행 환경을 조율한다. 앱이 직접 프로세스를 소유하는 것이 아니라 AMS와 Zygote 경로를 통해 process lifecycle이 만들어진다.

## 실무 의미

- 앱 process는 필요할 때 시작되고, 중요도가 낮아지면 시스템에 의해 종료될 수 있다.
- foreground service, bound service, broadcast, provider 사용은 process importance에 영향을 줄 수 있다.
- 앱은 process 생존을 보장받지 못하므로 저장해야 할 상태와 재구성 가능한 상태를 분리해야 한다.

## 관련 문서

- [Zygote socket은 system_server가 앱 프로세스를 요청하는 factory interface다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/zygote-runtime-contracts/zygote-socket-is-system-server-process-factory-interface.md)
- [Android 상태 관리 정본 지도](01_inbox/mobile/android/02_app_framework/architecture/state-management/android-state-management.md)

공식 문서: [Processes and app lifecycle](https://developer.android.com/guide/components/activities/process-lifecycle)
