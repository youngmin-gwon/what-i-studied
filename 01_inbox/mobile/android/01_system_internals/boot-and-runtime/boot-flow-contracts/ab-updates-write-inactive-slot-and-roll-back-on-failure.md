---
title: ab-updates-write-inactive-slot-and-roll-back-on-failure
tags: [android, android/boot, android/boot-runtime, android/system-internals]
aliases: ["A/B 업데이트는 비활성 slot을 갱신하고 실패 시 이전 slot로 돌아간다"]
date modified: 2026-08-03 17:22:58 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## A/B 업데이트는 비활성 slot 을 갱신하고 실패 시 이전 slot 로 돌아간다

상위 문서: [부팅 흐름 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/boot-flow-contracts/boot-flow-contracts.md)

A/B 업데이트는 현재 실행 중인 slot 을 건드리지 않고 비활성 slot 에 새 이미지를 쓴 뒤, 다음 부팅에서 새 slot 을 시도한다. 새 slot 이 성공으로 표시되지 않으면 bootloader 는 retry 정책에 따라 이전 slot 로 돌아갈 수 있다.

### 실무 의미

- update_engine 은 실행 중인 시스템에서 비활성 slot 을 갱신한다.
- bootloader 는 active slot, bootable 여부, successful flag, retry count 를 관리한다.
- framework 는 정상 부팅 후 `markBootSuccessful` 경로를 통해 새 slot 을 확정한다.
- 현재 slot 을 직접 수정하면 incremental OTA 와 rollback 안정성을 깨뜨릴 수 있다.

### 관련 문서

- [Virtual A/B는 snapshot으로 OTA 공간과 offline 시간을 줄인다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/boot-flow-contracts/virtual-ab-uses-snapshots-to-reduce-ota-space-and-downtime.md)
- [AVB는 부팅 이미지의 신뢰와 rollback 방지를 검증한다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/boot-flow-contracts/avb-verifies-boot-images-and-rollback-protection.md)

공식 문서: [A/B system updates](https://source.android.com/docs/core/ota/ab), [Implement A/B updates](https://source.android.com/docs/core/ota/ab/ab_implement)
