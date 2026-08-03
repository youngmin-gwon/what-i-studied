---
title: zram-is-compressed-swap-policy-not-a-memory-fix
tags: [android, android/kernel, android/memory]
aliases: [mmd, zRAM]
date modified: 2026-08-03 17:26:15 +09:00
date created: 2026-07-31 23:45:00 +09:00
---

## zRAM 은 메모리 부족 해결책이 아니라 압축 swap 정책이다

zRAM 은 block device 처럼 동작하는 압축 메모리 영역을 swap 으로 사용하는 kernel 기능이다. Android 에서는 storage write 를 늘리지 않고 anonymous memory pressure 를 완화하는 수단으로 쓰일 수 있다.

zRAM 은 물리 RAM 을 늘려 주지 않는다. 압축률이 좋을 때는 더 많은 working set 을 RAM 안에 유지할 수 있지만, 압축·해제 CPU 비용, swap policy, reclaim pressure, thermal 상태에 따라 오히려 지연을 만들 수도 있다.

Android 17 이상에서는 memory management daemon(mmd)이 ZRAM 설정과 유지보수 작업을 중앙화하는 방향을 제공한다. mmd 는 ZRAM writeback, recompression, per-process writeback 같은 작업을 system_server 와 분리된 daemon policy 로 다룬다.

따라서 "zRAM 은 디스크 swap 보다 항상 빠르다"나 "zRAM 을 키우면 LMKD 가 필요 없다"는 설명은 부정확하다. 실제 평가는 memory pressure, PSI, lmkd kill, swap in/out, CPU cost 를 함께 본다.

관련 노트: [LMKD는 free memory가 아니라 memory pressure와 process importance로 종료를 결정한다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/lmkd-kills-processes-by-memory-pressure-and-process-importance.md), [PSI는 free memory가 아니라 stall time을 측정한다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/psi-measures-stall-time-for-memory-pressure.md)

근거: [Memory management daemon](https://source.android.com/docs/core/perf/mmd), [Low memory killer daemon](https://source.android.com/docs/core/perf/lmkd)
