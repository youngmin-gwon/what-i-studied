---
title: psi-measures-stall-time-for-memory-pressure
tags: [android, android/kernel, android/memory]
aliases: [Pressure Stall Information, PSI]
date modified: 2026-08-03 17:26:12 +09:00
date created: 2026-07-31 23:45:00 +09:00
---

## PSI 는 free memory 가 아니라 stall time 을 측정한다

Pressure Stall Information(PSI)은 memory, CPU, I/O 부족으로 task 가 실제로 얼마나 기다렸는지를 측정하는 kernel signal 이다. Android lmkd 는 Android 10 이상에서 PSI monitor 기반 memory pressure detection 을 사용할 수 있다.

free memory 숫자는 단독으로 사용자 경험을 잘 설명하지 못한다. page cache, reclaim 가능성, swap, thrashing, allocator latency 에 따라 같은 free memory 라도 체감 성능은 다를 수 있다. PSI 는 task delay 를 직접 관찰하므로 memory pressure severity 를 판단하는 데 더 적합하다.

`some` 은 일부 task 가 resource 를 기다린 시간을, `full` 은 모든 non-idle task 가 막힌 시간을 나타낸다. 이 값은 "메모리가 몇 MB 남았다"가 아니라 "얼마나 실행이 지연됐는가"를 보여준다.

문서에서 PSI 를 쓸 때는 kernel support 와 config 조건도 함께 적어야 한다. Android lmkd 의 PSI 모드는 kernel support 와 `CONFIG_PSI` 같은 설정에 의존한다.

관련 노트: [LMKD는 free memory가 아니라 memory pressure와 process importance로 종료를 결정한다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/lmkd-kills-processes-by-memory-pressure-and-process-importance.md)

근거: [Low memory killer daemon](https://source.android.com/docs/core/perf/lmkd)
