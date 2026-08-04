---
title: 16-lmkd-low-memory-killer-daemon
tags: ["android", "android/glossary"]
aliases: ["lmkd", "Low Memory Killer Daemon"]
date modified: 2026-08-03 17:21:34 +09:00
date created: 2026-07-31 15:29:55 +09:00
---

## LMKD 는 시스템 메모리가 부족할 때 우선순위가 낮은 프로세스를 종료하여 리소스를 확보한다

정의: LMKD 는 memory pressure 와 process importance signal 을 바탕으로 Android process 를 종료해 system responsiveness 를 지키는 daemon 이다.

혼동 방지: LMKD kill 은 crash 와 다르다. 앱 process 가 사라졌다면 crash log 만 볼 것이 아니라 process importance, memory pressure, foreground service, state persistence 를 함께 봐야 한다.

정본 링크:

- [LMKD memory pressure contract](../../../01_system_internals/kernel-and-hal/kernel-contracts/lmkd-kills-processes-by-memory-pressure-and-process-importance.md)
- [Process priority contract](../../../01_system_internals/boot-and-runtime/system-server-contracts/process-priority-is-memory-reclaim-policy-input-not-app-state-truth.md)
