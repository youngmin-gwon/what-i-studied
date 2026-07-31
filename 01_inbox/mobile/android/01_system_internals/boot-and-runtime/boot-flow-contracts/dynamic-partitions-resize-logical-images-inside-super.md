# Dynamic partition은 super 안에서 논리 파티션 크기를 조정한다

상위 문서: [부팅 흐름 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/boot-flow-contracts/boot-flow-contracts.md)

Dynamic partition은 `/system`, `/vendor`, `/product` 같은 논리 파티션의 크기를 OTA 시점에 조정할 수 있게 하는 userspace partitioning 구조다. 물리 파티션을 고정 크기로 쪼개는 대신 `super` 안에서 논리 이미지를 관리한다.

## 언제 중요한가

- OTA에서 특정 파티션만 커지고 다른 파티션은 줄어야 할 때
- GSI, Treble, vendor/system 경계를 유지하면서 update package 크기와 저장소 사용량을 관리할 때
- Virtual A/B snapshot merge가 논리 파티션 위에서 동작할 때

## 관련 문서

- [Virtual A/B는 snapshot으로 OTA 공간과 offline 시간을 줄인다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/boot-flow-contracts/virtual-ab-uses-snapshots-to-reduce-ota-space-and-downtime.md)
- [파티션 구조는 system과 vendor의 업데이트 경계를 만든다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/boot-flow-contracts/partitions-define-system-vendor-and-update-boundaries.md)

공식 문서: [Partitions overview](https://source.android.com/docs/core/architecture/partitions), [Virtual A/B overview](https://source.android.com/docs/core/ota/virtual_ab)
