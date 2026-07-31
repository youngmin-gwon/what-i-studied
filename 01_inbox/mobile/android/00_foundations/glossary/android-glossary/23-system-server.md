---
title: "system_server"
tags: ["android", "android/glossary"]
aliases: ["SystemServer", "system server"]
---

# system_server

정의: system_server는 ActivityManager, PackageManager, WindowManager 같은 framework services를 한 process 안에서 시작하고 운영하는 Android core process다.

혼동 방지: system_server는 kernel도 app process도 아니다. 앱 API 호출 상당수는 Binder를 통해 system_server service endpoint로 넘어가며, 여기서 platform policy가 적용된다.

정본 링크:
- [system_server startup contract](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/system-server-starts-framework-services-in-one-process.md)
- [System service policy boundary](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/system-service-is-binder-endpoint-and-platform-policy-enforcer.md)
