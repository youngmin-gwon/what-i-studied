# Bootloader는 검증된 slot을 고르고 Android에 bootconfig를 넘긴다

상위 문서: [부팅 흐름 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/boot-flow-contracts/boot-flow-contracts.md)

Bootloader는 kernel을 단순히 실행하는 로더가 아니다. 기기 상태, Verified Boot 결과, recovery 진입 여부, A/B slot 상태를 보고 어떤 이미지를 실행할지 결정하고 Android userspace에 필요한 boot parameter를 넘긴다.

## 실무 의미

- Android 12 이상에서는 Android userspace용 `androidboot.*` 정보가 kernel command line 대신 bootconfig로 전달될 수 있다.
- A/B 기기는 active slot, successful flag, retry count를 bootloader와 Boot Control HAL이 함께 관리한다.
- recovery, fastboot, unlocked 상태는 Android framework가 아니라 bootloader 단계의 정책과 맞닿아 있다.

## 관련 문서

- [A/B 업데이트는 비활성 slot을 갱신하고 실패 시 이전 slot로 돌아간다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/boot-flow-contracts/ab-updates-write-inactive-slot-and-roll-back-on-failure.md)
- [AVB는 부팅 이미지의 신뢰와 rollback 방지를 검증한다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/boot-flow-contracts/avb-verifies-boot-images-and-rollback-protection.md)

공식 문서: [Bootloader overview](https://source.android.com/docs/core/architecture/bootloader), [Implement OTA updates](https://source.android.com/docs/core/architecture/bootloader/updating)
