---
title: "Wakelock"
tags: ["android", "android/glossary"]
aliases: ["Wake lock", "Suspend blocker"]
---

# Wakelock

정의: Wakelock은 device suspend를 지연시켜 특정 작업 중 CPU나 device가 잠들지 않게 하는 suspend blocker 계열 mechanism이다.

혼동 방지: Wakelock은 background work permission이 아니다. 실행 보장, 사용자 가시성, power policy는 WorkManager, foreground service, alarm policy와 따로 판단해야 한다.

정본 링크:
- [Wakelock suspend blocker](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/wakelocks-are-suspend-blockers-not-background-work-permission.md)
- [SystemSuspend arbitration](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/systemsuspend-arbitrates-userspace-wakelocks-and-kernel-suspend.md)
