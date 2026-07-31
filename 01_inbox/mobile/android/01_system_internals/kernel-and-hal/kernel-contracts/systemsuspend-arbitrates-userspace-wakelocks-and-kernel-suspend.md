---
title: SystemSuspend는 userspace wakelock과 kernel suspend를 중재한다
tags: [android, android/kernel, android/power]
date modified: 2026-07-31 23:45:00 +09:00
date created: 2026-07-31 23:45:00 +09:00
---

Android 10부터 SystemSuspend service는 userspace suspend blocker 요청과 kernel suspend 진입 사이의 중재자 역할을 한다. 이전의 libsuspend 중심 구조와 `/sys/power/wake_lock` 직접 접근을 더 구조화된 service 경계로 옮긴 것이다.

SystemSuspend는 wakelock count를 관리하고, suspend thread가 `/sys/power/wakeup_count`와 `/sys/power/state`를 사용해 system suspend를 시도한다. main thread는 Binder/HIDL/AIDL 경계에서 clients의 wakelock 요청을 처리한다.

이 구조의 중요한 효과는 소유권이다. client가 죽으면 Binder driver와 SystemSuspend가 해당 wakelock 정리를 감지할 수 있다. 같은 이름 문자열을 공유하던 오래된 sysfs 방식보다 resource ownership을 추적하기 쉽다.

전원 문제 분석에서는 “앱이 wake lock을 잡았다”와 “시스템이 suspend하지 못했다”를 구분한다. wakeup source, SystemSuspend 상태, app standby, JobScheduler, foreground service 정책을 함께 봐야 한다.

관련 노트: [Wakelock은 background work 권한이 아니라 suspend blocker다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/wakelocks-are-suspend-blockers-not-background-work-permission.md)

근거: [SystemSuspend service](https://source.android.com/docs/core/power/systemsuspend)
