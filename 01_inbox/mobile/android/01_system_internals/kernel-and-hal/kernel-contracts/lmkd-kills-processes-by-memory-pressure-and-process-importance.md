---
title: LMKD는 free memory가 아니라 memory pressure와 process importance로 종료를 결정한다
tags: [android, android/kernel, android/memory]
aliases: [LMKD, Low memory killer daemon]
date modified: 2026-07-31 23:45:00 +09:00
date created: 2026-07-31 23:45:00 +09:00
---

# LMKD는 free memory가 아니라 memory pressure와 process importance로 종료를 결정한다

Low memory killer daemon(lmkd)은 Android 시스템의 memory pressure를 감시하고, 압력이 높을 때 덜 중요한 process를 종료해 사용자 체감 성능을 유지한다.

중요한 점은 LMKD가 단순히 “남은 메모리가 특정 MB 아래면 kill”하는 현대 구조가 아니라는 것이다. 역사적으로 in-kernel LMK driver는 free memory threshold에 강하게 의존했지만, 현재 userspace lmkd는 vmpressure 또는 PSI, memory cgroup, swap/thrashing 상태, process importance를 함께 본다.

ActivityManager는 process state를 바탕으로 `oom_score_adj`를 설정한다. lmkd는 kill 후보를 고를 때 이 중요도와 memory pressure를 함께 사용한다. 그래서 foreground process와 cached process는 같은 메모리 사용량이어도 정책적으로 다르게 취급된다.

앱 개발 관점에서는 “내 앱이 왜 죽었는가”를 보려면 crash만 볼 것이 아니라 `am_proc_died`, `lmkd`, `oom_score_adj`, memory pressure, background state를 같이 봐야 한다.

관련 노트: [PSI는 free memory가 아니라 stall time을 측정한다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/psi-measures-stall-time-for-memory-pressure.md), [Process priority is memory reclaim policy input](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/process-priority-is-memory-reclaim-policy-input-not-app-state-truth.md)

근거: [Low memory killer daemon](https://source.android.com/docs/core/perf/lmkd)
