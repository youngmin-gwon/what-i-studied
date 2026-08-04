---
title: 27-wakelock
tags: ["android", "android/glossary"]
aliases: ["Suspend blocker", "Wake lock"]
date modified: 2026-08-03 17:21:14 +09:00
date created: 2026-07-31 15:29:55 +09:00
---

## Wakelock 은 앱이 기기를 슬립 모드로 들어가지 못하게 전원을 유지하는 메커니즘이다

정의: Wakelock 은 device suspend 를 지연시켜 특정 작업 중 CPU 나 device 가 잠들지 않게 하는 suspend blocker 계열 mechanism 이다.

혼동 방지: Wakelock 은 background work permission 이 아니다. 실행 보장, 사용자 가시성, power policy 는 WorkManager, foreground service, alarm policy 와 따로 판단해야 한다.

정본 링크:

- [Wakelock suspend blocker](../../../01_system_internals/kernel-and-hal/kernel-contracts/wakelocks-are-suspend-blockers-not-background-work-permission.md)
- [SystemSuspend arbitration](../../../01_system_internals/kernel-and-hal/kernel-contracts/systemsuspend-arbitrates-userspace-wakelocks-and-kernel-suspend.md)
