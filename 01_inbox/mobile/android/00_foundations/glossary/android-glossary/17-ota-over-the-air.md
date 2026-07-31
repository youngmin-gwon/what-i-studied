---
title: "OTA"
tags: ["android", "android/glossary"]
aliases: ["Over The Air update", "A/B update", "Virtual A/B"]
---

# OTA

정의: OTA는 device system image나 module을 network를 통해 업데이트하는 mechanism이며, modern Android에서는 A/B slot과 rollback contract가 핵심이다.

혼동 방지: OTA는 Play app update와 다르다. OS image, partition, slot, verified boot, snapshot merge 같은 device update 흐름을 다룬다.

정본 링크:
- [A/B update contract](01_inbox/mobile/android/01_system_internals/boot-and-runtime/boot-flow-contracts/ab-updates-write-inactive-slot-and-roll-back-on-failure.md)
- [Virtual A/B contract](01_inbox/mobile/android/01_system_internals/boot-and-runtime/boot-flow-contracts/virtual-ab-uses-snapshots-to-reduce-ota-space-and-downtime.md)
