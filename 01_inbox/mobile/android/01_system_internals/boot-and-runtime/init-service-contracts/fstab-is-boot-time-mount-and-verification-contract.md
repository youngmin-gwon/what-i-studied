---
title: fstab-is-boot-time-mount-and-verification-contract
tags: [android, android/boot-runtime, android/init, android/system-internals]
aliases: ["fstab은 mount와 검증 플래그를 묶은 부팅 계약이다"]
date modified: 2026-08-04 15:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## fstab 은 mount 와 검증 플래그를 묶은 부팅 계약이다

상위 문서: [init 서비스 계약](init-service-contracts.md)

Android의 `fstab`(File System Table)은 단순한 파일시스템 마운트 경로 지정을 넘어, First-stage init 마운트 여부, dm-verity 무결성 검증, File-Based Encryption(FBE) 암호화 옵션, A/B Slot 선택 정책을 init 프로세스에 지시하는 부팅 계약(Boot Contract) 서식이다.

### 내부 동작 메커니즘 (Internal Mechanism)

1. **위치 및 로딩 우선순위**:
   - Android 12 이상에서 `fstab`은 `vendor_boot` 파티션의 Ramdisk 내부 `/first_stage_ramdisk/fstab.<hardware>` 또는 `/vendor/etc/fstab.<hardware>`에 위치한다.
   - First-stage init은 `fs_mgr` 라이브러리의 `ReadDefaultFstab()`을 호출하여 Device Tree(`/proc/device-tree/firmware/android/fstab`) 또는 파일시스템 내 `fstab`을 파싱한다.
2. **주요 마운트 플래그 (Mount Flags)**:
   - `first_stage_mount`: First-stage init 단계에서 즉시 마운트되어야 하는 핵심 파티션 (`/system`, `/vendor`, `/product`).
   - `latemount`: Second-stage init의 `on late-init` 액션 단계에서 `vold`와 연동되어 마운트되는 파티션(예: `/data`).
   - `slotselect`: A/B 업데이트 기기에서 현재 부팅 Slot Suffix(`_a` 또는 `_b`)를 블록 디바이스명 뒤에 자동 결합.
   - `avb / avb_keys`: AVB VBMeta hash tree verification 적용 지시.
   - `fileencryption=aes-256-xts:aes-256-cts`: `/data` 파티션에 File-Based Encryption(FBE) 적용 지시.
3. **`fs_mgr` C++ 파싱 구조체**: `fs_mgr` 라이브러리는 각 엔트리를 `FstabEntry` 객체로 역직렬화하여 `fs_mgr_flags` 비트마스크 필드에 마운트 옵션을 보관한다.

```mermaid
flowchart TD
    FSTAB["fstab File
(fstab.hardware)"] -->|ReadDefaultFstab()| PARSER["fs_mgr Parser"]
    PARSER -->|FstabEntry.fs_mgr_flags| ENTRY["FstabEntry Struct"]
    ENTRY -->|first_stage_mount| STAGE1["First-stage Mount
(/system, /vendor)"]
    ENTRY -->|avb / avb_keys| AVB["AVB / dm-verity Verification"]
    ENTRY -->|fileencryption| FBE["FBE Encryption Manager (/data)"]
    ENTRY -->|latemount| STAGE2["Second-stage Mount
(/data, /sdcard)"]

    style FSTAB fill:#f9f,stroke:#333,stroke-width:2px
    style AVB fill:#bbf,stroke:#333,stroke-width:2px
```

### 코드 및 구체 예시 (Concrete Snippets)

`system/core/fs_mgr/include/fs_mgr/fstab.h` C++ 구조체 정의 및 `fstab` 파일 예시:

```cpp
// system/core/fs_mgr/include/fs_mgr/fstab.h
namespace android::fs_mgr {

struct FstabEntry {
    std::string blk_device;
    std::string logical_partition_name;
    std::string mount_point;
    std::string fs_type;
    uint64_t flags = 0;
    std::string fs_options;
    struct FstabEntryFsMgrFlags {
        bool wait : 1;
        bool check : 1;
        bool crypt : 1;
        bool nonremovable : 1;
        bool vold_managed : 1;
        bool length : 1;
        bool recovery_only : 1;
        bool no_emulated_sd : 1;
        bool no_trim : 1;
        bool verify : 1;
        bool quota : 1;
        bool slotselect : 1;
        bool latemount : 1;
        bool logical : 1;
        bool checkpoint : 1;
        bool first_stage_mount : 1;
    } fs_mgr_flags = {};
};

bool ReadDefaultFstab(Fstab* fstab);
} // namespace android::fs_mgr
```

전형적인 Android `fstab` 파일 (`fstab.qcom`) 구문 예시:

```text
# src_device                                mount_point    type   flags
system                                      /system        ext4   ro,barrier=1 wait,slotselect,avb=vbmeta,logical,first_stage_mount
vendor                                      /vendor        ext4   ro,barrier=1 wait,slotselect,avb,logical,first_stage_mount
/dev/block/bootdevice/by-name/userdata       /data          f2fs   noatime,nosuid,nodev latemount,wait,check,fileencryption=aes-256-xts:aes-256-cts,keydirectory=/metadata/vold/metadata_encryption
/dev/block/bootdevice/by-name/metadata       /metadata      ext4   noatime,nosuid,nodev wait,formattable,first_stage_mount
```

### 관측 가능 증거 (Observable Evidence)

`adb shell`을 이용해 실행 중인 시스템의 마운트 테이블 및 `fstab` 설정을 점검할 수 있다:

```bash
# 디바이스 fstab 위치 및 파일 내용 확인
adb shell cat /vendor/etc/fstab.*

# 마운트된 파티션의 암호화 및 verity 옵션 확인
adb shell mount | grep -E "(system|vendor|data)"

# fstab 파싱 관련 init 로그 확인
adb shell dmesg | grep -i "init: [fstab]"
```

### 관련 문서

- [First stage init은 second stage가 읽을 최소 파일시스템을 만든다](first-stage-init-builds-minimal-filesystem-for-second-stage.md)
- [AVB는 부팅 이미지의 신뢰와 rollback 방지를 검증한다](../boot-flow-contracts/avb-verifies-boot-images-and-rollback-protection.md)

공식 문서: [Fstab handling](https://source.android.com/docs/core/architecture/bootloader/fstab-handling)
