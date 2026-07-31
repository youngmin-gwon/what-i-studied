---
title: Wakelock은 background work 권한이 아니라 suspend blocker다
tags: [android, android/kernel, android/power]
aliases: [Wakelock, WakeLock]
date modified: 2026-07-31 23:45:00 +09:00
date created: 2026-07-31 23:45:00 +09:00
---

# Wakelock은 background work 권한이 아니라 suspend blocker다

Wakelock은 “작업을 실행해도 된다”는 권한이 아니라, 특정 조건에서 device가 system suspend로 들어가지 않도록 막는 suspend blocker다. 앱 수준에서는 `PowerManager.WakeLock`으로 주로 partial wake lock을 다루고, system/native 쪽에서는 SystemSuspend 경계와 연결된다.

partial wake lock은 화면이 꺼진 뒤에도 CPU가 계속 필요한 작업에서 사용할 수 있지만, 오래 잡고 있으면 배터리 소모로 이어진다. Android vitals도 background 또는 foreground service 중 잡힌 partial wake lock 시간이 과도한지 관찰한다.

현대 Android에서는 Doze, App Standby, JobScheduler, foreground service policy가 함께 작동한다. Wakelock을 잡았다고 background execution 제한, 네트워크 제한, 작업 스케줄링 제한을 모두 우회하는 것은 아니다.

문서에서는 오래된 `/sys/power/wake_lock` 예제를 앱 개발 패턴처럼 쓰지 않는다. 앱은 framework API와 더 적절한 작업 API를 우선 검토하고, kernel/system 분석에서는 suspend blocker 상태와 wakeup source를 확인한다.

관련 노트: [SystemSuspend는 userspace wakelock과 kernel suspend를 중재한다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/systemsuspend-arbitrates-userspace-wakelocks-and-kernel-suspend.md), [Background restrictions require persistent work state](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/background-restrictions-require-persistent-work-state.md)

근거: [PowerManager.WakeLock](https://developer.android.com/reference/android/os/PowerManager.WakeLock), [Excessive partial wake locks](https://developer.android.com/topic/performance/vitals/excessive-wakelock)
