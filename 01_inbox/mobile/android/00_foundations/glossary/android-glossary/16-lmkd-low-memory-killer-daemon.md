---
title: "LMKD"
tags: ["android", "android/glossary"]
aliases: ["Low Memory Killer Daemon", "lmkd"]
---

# LMKD

정의: LMKD는 memory pressure와 process importance signal을 바탕으로 Android process를 종료해 system responsiveness를 지키는 daemon이다.

혼동 방지: LMKD kill은 crash와 다르다. 앱 process가 사라졌다면 crash log만 볼 것이 아니라 process importance, memory pressure, foreground service, state persistence를 함께 봐야 한다.

정본 링크:
- [LMKD memory pressure contract](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/lmkd-kills-processes-by-memory-pressure-and-process-importance.md)
- [Process priority contract](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/process-priority-is-memory-reclaim-policy-input-not-app-state-truth.md)
