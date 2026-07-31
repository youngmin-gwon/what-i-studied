---
title: "AMS와 ATMS"
tags: ["android", "android/glossary"]
aliases: ["ActivityManagerService", "ActivityTaskManagerService", "AMS", "ATMS"]
---

# AMS와 ATMS

정의: AMS는 process와 component lifecycle을 조율하고, ATMS는 activity task, back stack, transition을 소유하는 system_server 내부 서비스다.

혼동 방지: 앱 입장에서는 둘 다 framework 뒤에 숨은 정책 실행자다. Activity lifecycle callback은 앱 API이고, 실제 process importance, task 이동, launch policy 판단은 system service 경계에서 일어난다.

정본 링크:
- [AMS lifecycle contract](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/ams-coordinates-app-process-and-component-lifecycle.md)
- [ATMS task contract](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/atms-owns-activity-task-and-back-stack-transitions.md)
