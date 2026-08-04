---
title: 02-ams-atms-activitymanagerservice-activitytaskmanagerservice
tags: ["android", "android/glossary"]
aliases: ["ActivityManagerService", "ActivityTaskManagerService", "AMS", "ATMS"]
date modified: 2026-08-04 16:17:32 +09:00
date created: 2026-07-31 15:29:55 +09:00
---

## AMS 와 ATMS

정의: AMS 는 process 와 component lifecycle 을 조율하고, ATMS 는 activity task, back stack, transition 을 소유하는 system_server 내부 서비스다.

혼동 방지: 앱 입장에서는 둘 다 framework 뒤에 숨은 정책 실행자다. Activity lifecycle callback 은 앱 API 이고, 실제 process importance, task 이동, launch policy 판단은 system service 경계에서 일어난다.

정본 링크:

- [AMS lifecycle contract](../../../01_system_internals/boot-and-runtime/system-server-contracts/ams-coordinates-app-process-and-component-lifecycle.md)
- [ATMS task contract](../../../01_system_internals/boot-and-runtime/system-server-contracts/atms-owns-activity-task-and-back-stack-transitions.md)
