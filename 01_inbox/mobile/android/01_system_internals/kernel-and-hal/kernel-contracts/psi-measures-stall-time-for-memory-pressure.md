---
title: PSI는 free memory가 아니라 stall time을 측정한다
tags: [android, android/kernel, android/memory]
aliases: [PSI, Pressure Stall Information]
date modified: 2026-07-31 23:45:00 +09:00
date created: 2026-07-31 23:45:00 +09:00
---

# PSI는 free memory가 아니라 stall time을 측정한다

Pressure Stall Information(PSI)은 memory, CPU, I/O 부족으로 task가 실제로 얼마나 기다렸는지를 측정하는 kernel signal이다. Android lmkd는 Android 10 이상에서 PSI monitor 기반 memory pressure detection을 사용할 수 있다.

free memory 숫자는 단독으로 사용자 경험을 잘 설명하지 못한다. page cache, reclaim 가능성, swap, thrashing, allocator latency에 따라 같은 free memory라도 체감 성능은 다를 수 있다. PSI는 task delay를 직접 관찰하므로 memory pressure severity를 판단하는 데 더 적합하다.

`some`은 일부 task가 resource를 기다린 시간을, `full`은 모든 non-idle task가 막힌 시간을 나타낸다. 이 값은 “메모리가 몇 MB 남았다”가 아니라 “얼마나 실행이 지연됐는가”를 보여준다.

문서에서 PSI를 쓸 때는 kernel support와 config 조건도 함께 적어야 한다. Android lmkd의 PSI 모드는 kernel support와 `CONFIG_PSI` 같은 설정에 의존한다.

관련 노트: [LMKD는 free memory가 아니라 memory pressure와 process importance로 종료를 결정한다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/lmkd-kills-processes-by-memory-pressure-and-process-importance.md)

근거: [Low memory killer daemon](https://source.android.com/docs/core/perf/lmkd)
