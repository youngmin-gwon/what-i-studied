---
title: zygote-socket-is-system-server-process-factory-interface
tags: [android, android/boot-runtime, android/runtime, android/system-internals]
aliases: ["Zygote socket은 system_server가 앱 프로세스를 요청하는 factory interface다"]
date modified: 2026-08-03 17:24:09 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Zygote socket 은 system_server 가 앱 프로세스를 요청하는 factory interface 다

상위 문서: [Zygote와 ART 런타임 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/zygote-runtime-contracts/zygote-runtime-contracts.md)

Zygote 는 임의 앱이 직접 호출하는 API 가 아니다. `system_server` 의 ActivityManager 계층이 Unix domain socket 으로 Zygote 에 fork 와 specialization 을 요청하고, Zygote 는 새 process 의 UID, GID, capability, runtime args 를 설정한다.

### 판단 기준

- Zygote socket 권한은 init rc 의 `socket` option 과 SELinux 정책으로 보호된다.
- USAP pool 이 활성화된 기기에서는 일부 앱 프로세스 준비 비용을 미리 지불할 수 있다.
- fork 요청 경로는 Binder 호출과 다르며, 앱 process 가 뜬 뒤 framework attach 가 이어진다.
- Zygote crash 는 앱 프로세스 전반과 system service 안정성에 큰 영향을 준다.

### 관련 문서

- [AMS는 앱 프로세스와 컴포넌트 lifecycle을 조율한다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/ams-coordinates-app-process-and-component-lifecycle.md)
- [service option은 identity, resource, class, socket 계약을 고정한다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/init-service-contracts/service-options-fix-identity-resource-class-and-socket-contracts.md)

공식 문서: [About the Zygote processes](https://source.android.com/docs/core/runtime/zygote)
