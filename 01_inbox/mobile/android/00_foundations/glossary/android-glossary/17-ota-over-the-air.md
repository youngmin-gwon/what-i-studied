---
title: 17-ota-over-the-air
tags: ["android", "android/glossary"]
aliases: ["A/B update", "Over The Air update", "Virtual A/B"]
date modified: 2026-08-03 17:21:34 +09:00
date created: 2026-07-31 15:29:55 +09:00
---

## OTA 는 시스템 업데이트를 무선으로 기기에 다운로드하고 적용하는 메커니즘이다

정의: OTA 는 device system image 나 module 을 network 를 통해 업데이트하는 mechanism 이며, modern Android 에서는 A/B slot 과 rollback contract 가 핵심이다.

혼동 방지: OTA 는 Play app update 와 다르다. OS image, partition, slot, verified boot, snapshot merge 같은 device update 흐름을 다룬다.

정본 링크:

- [A/B update contract](01_inbox/mobile/android/01_system_internals/boot-and-runtime/boot-flow-contracts/ab-updates-write-inactive-slot-and-roll-back-on-failure.md)
- [Virtual A/B contract](01_inbox/mobile/android/01_system_internals/boot-and-runtime/boot-flow-contracts/virtual-ab-uses-snapshots-to-reduce-ota-space-and-downtime.md)
