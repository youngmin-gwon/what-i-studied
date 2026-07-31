# 부팅 흐름 계약

부팅 흐름은 하드웨어 초기화 순서가 아니라 신뢰 가능한 이미지 선택, 파티션 경계, OTA 복구 가능성, userspace 진입점이 맞물린 계약이다.

## 정본 노트
- [부팅 체인은 신뢰 상태를 확정한 뒤 kernel과 userspace로 넘어간다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/boot-flow-contracts/boot-chain-confirms-trust-before-kernel-and-userspace.md)
- [Bootloader는 검증된 slot을 고르고 Android에 bootconfig를 넘긴다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/boot-flow-contracts/bootloader-selects-verified-slot-and-passes-bootconfig.md)
- [파티션 구조는 system과 vendor의 업데이트 경계를 만든다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/boot-flow-contracts/partitions-define-system-vendor-and-update-boundaries.md)
- [Dynamic partition은 super 안에서 논리 파티션 크기를 조정한다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/boot-flow-contracts/dynamic-partitions-resize-logical-images-inside-super.md)
- [AVB는 부팅 이미지의 신뢰와 rollback 방지를 검증한다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/boot-flow-contracts/avb-verifies-boot-images-and-rollback-protection.md)
- [A/B 업데이트는 비활성 slot을 갱신하고 실패 시 이전 slot로 돌아간다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/boot-flow-contracts/ab-updates-write-inactive-slot-and-roll-back-on-failure.md)
- [Virtual A/B는 snapshot으로 OTA 공간과 offline 시간을 줄인다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/boot-flow-contracts/virtual-ab-uses-snapshots-to-reduce-ota-space-and-downtime.md)
- [부팅 완료는 단일 property가 아니라 관측 가능한 milestone 묶음이다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/boot-flow-contracts/boot-completion-is-observable-milestones-not-one-property.md)
- [부팅 디버깅은 logcat 이전의 kernel, pstore, init 로그에서 시작한다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/boot-flow-contracts/boot-debugging-starts-before-logcat-with-kernel-pstore-init-logs.md)
