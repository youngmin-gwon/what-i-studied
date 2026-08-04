---
title: 23-system-server
tags: ["android", "android/glossary"]
aliases: ["system server", "SystemServer"]
date modified: 2026-08-03 17:20:58 +09:00
date created: 2026-07-31 15:29:55 +09:00
---

## system_server 는 안드로이드 프레임워크의 핵심 서비스들을 호스팅하는 최상위 프로세스다

정의: system_server 는 ActivityManager, PackageManager, WindowManager 같은 framework services 를 한 process 안에서 시작하고 운영하는 Android core process 다.

혼동 방지: system_server 는 kernel 도 app process 도 아니다. 앱 API 호출 상당수는 Binder 를 통해 system_server service endpoint 로 넘어가며, 여기서 platform policy 가 적용된다.

정본 링크:

- [system_server startup contract](../../../01_system_internals/boot-and-runtime/system-server-contracts/system-server-starts-framework-services-in-one-process.md)
- [System service policy boundary](../../../01_system_internals/boot-and-runtime/system-server-contracts/system-service-is-binder-endpoint-and-platform-policy-enforcer.md)
