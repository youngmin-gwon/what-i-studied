---
title: kernel-debugging-starts-before-logcat-with-bootloader-dmesg-and-trace
tags: [android, android/debugging, android/kernel]
aliases: []
date modified: 2026-08-03 17:26:09 +09:00
date created: 2026-07-31 23:45:00 +09:00
---

## Kernel debugging 은 logcat 이전의 신호에서 시작한다

Kernel 문제는 Android framework logcat 만으로 충분하지 않다. bootloader verified boot state, kernel command line/bootconfig, dmesg, pstore/ramoops, first-stage init log, module load log, Perfetto trace 를 순서대로 봐야 한다.

부팅 전후 문제는 단계가 중요하다. bootloader 가 kernel 을 로드하지 못했는지, kernel panic 이 났는지, first-stage init 이 partition 이나 module 을 준비하지 못했는지, second-stage init 이후 service 가 실패했는지에 따라 증거 위치가 다르다.

실행 중 문제는 subsystem 별 관찰점을 나눈다. memory pressure 는 lmkd/PSI/oom_score_adj 를 보고, power issue 는 wakelock/SystemSuspend/wakeup source 를 보며, SELinux issue 는 `avc: denied` 의 context/class/permission 을 읽는다.

Perfetto 는 kernel scheduling 과 system service 를 같은 timeline 에서 보는 데 유용하지만, 단일 trace 만으로 모든 kernel 원인을 단정하지 않는다. 재현 조건, build branch, device kernel release, vendor module 상태를 같이 기록한다.

관련 노트: [Vendor kernel module은 first-stage init 경계에서 로드된다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/vendor-kernel-modules-load-through-first-stage-init-boundaries.md), [LMKD는 free memory가 아니라 memory pressure와 process importance로 종료를 결정한다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/lmkd-kills-processes-by-memory-pressure-and-process-importance.md)
