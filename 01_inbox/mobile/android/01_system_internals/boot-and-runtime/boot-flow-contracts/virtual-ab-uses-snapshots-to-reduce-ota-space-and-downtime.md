---
title: "Virtual A/B는 snapshot으로 OTA 공간과 offline 시간을 줄인다"
tags: [android, android/system-internals, android/boot-runtime, android/boot]
aliases: ["Virtual A/B는 snapshot으로 OTA 공간과 offline 시간을 줄인다"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# Virtual A/B는 snapshot으로 OTA 공간과 offline 시간을 줄인다

상위 문서: [부팅 흐름 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/boot-flow-contracts/boot-flow-contracts.md)

Virtual A/B는 모든 논리 파티션을 물리적으로 두 벌 유지하는 대신 snapshot과 COW 장치를 사용해 업데이트 데이터를 관리한다. 목표는 rollback 가능성을 유지하면서 필요한 추가 공간과 사용자가 기기를 쓰지 못하는 시간을 줄이는 것이다.

## 실무 의미

- OTA 설치 중 새 데이터는 snapshot 또는 COW 장치에 기록될 수 있다.
- 재부팅 후 merge가 userspace에서 진행되며, 실패하면 이전 상태로 되돌릴 수 있어야 한다.
- dynamic partition, metadata partition, dm-user, snapuserd 같은 구성요소와 맞물린다.
- 저장소 부족, merge 중 전원 차단, rollback 가능성을 테스트 시나리오로 다룬다.

## 관련 문서

- [Dynamic partition은 super 안에서 논리 파티션 크기를 조정한다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/boot-flow-contracts/dynamic-partitions-resize-logical-images-inside-super.md)
- [A/B 업데이트는 비활성 slot을 갱신하고 실패 시 이전 slot로 돌아간다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/boot-flow-contracts/ab-updates-write-inactive-slot-and-roll-back-on-failure.md)

공식 문서: [Virtual A/B overview](https://source.android.com/docs/core/ota/virtual_ab)
