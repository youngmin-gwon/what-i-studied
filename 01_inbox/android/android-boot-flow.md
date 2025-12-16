# Boot Flow & System Images #android #android/boot #android/system-images

[[android-architecture-stack]] · [[android-hal-and-kernel]] · [[android-zygote-and-runtime]]

## 부팅 단계
1. Boot ROM: SoC별 mask ROM이 부트로더 1단계 실행, 서명 검사.
2. Bootloader: fastboot/download 모드, verified boot(VB1/AVB2) chain 수행. A/B slot 선택, rollback index 체크.
3. Kernel + ramdisk: dtb/dtbo 로딩, kernel command line 전달. dm-verity 활성화.
4. init: init.rc 파싱, SELinux policy 로딩, 서비스/파티션 마운트.
5. zygote/system_server 기동: [[android-zygote-and-runtime]] 참고.
6. System UI/Launcher 스타트, 데이터스톱 복원.
- OTA 후 첫 부팅: slot switching, postinstall scripts, dexopt/dalvik cache rebuild, OTA resume-on-reboot credential 해제.

## 파티션 구조
- boot/boot_a/boot_b: 커널+ramdisk. vendor_boot 분리(Android 11+).
- system/system_ext/vendor/odm/product: 파트별 역할 분리. read-only + dm-verity.
- userdata: FBE. metadata 파티션에 key 저장.
- recovery: OTA 적용/공장 초기화. logical partitions(super)로 동적 파티션 관리.
- misc/metadata 파티션이 boot slot/state 저장. super 파티션은 dynamic logical partition table(LPT)로 구성.

## Verified Boot & AVB
- vbmeta 서명 검증. top-level vbmeta가 chain vbmeta_system/vendor 등으로 이어짐.
- rollback protection: fuse/Replay-protected memory(RPMB).
- device locked/unlocked 플래그, fastboot flashing unlock 효과(데이터 초기화).
- dm-verity hash tree, verity metadata. vbmeta flags(e.g., VERIFICATION_DISABLED)로 userdebug 편의 제공.

## A/B OTA
- seamless update: active/inactive slot. update_engine가 payload를 inactive slot에 적용.
- post-install scripts, slot metadata, bootctl. resume-on-reboot로 암호화 잠금 자동 입력.
- non-A/B 기기는 recovery-based OTA.
- payload format: block-based, delta/Full. payload properties(version, block size). payload_verifier 검증.
- dynamic partitions: payload metadata가 super partition LPT를 업데이트, fastbootd에서 flash.\n
- Virtual A/B는 snapshots 기반으로 공간 절약하며 OTA 실패 시 롤백 용이.\n

## Fastboot/Recovery/ADB 모드
- Fastboot: boot image 플래싱, getvar. AVB unlock 여부에 따라 제한.
- Recovery: update.zip 설치, adb sideload. UI는 recovery ramdisk에서 실행.
- ADB: USB/Wi-Fi debugging. secure adb는 RSA key + pairing. `adb root`/`adb disable-verity`는 eng/userdebug에서만.
- fastbootd: userspace fastboot for dynamic partitions; logical partition resize/flash without recovery. slot metadata 관리에 사용.

## System Image 구성
- system.img(ext4/sparse), vendor.img, product.img 등. dynamic partition(super.img)로 묶어 OTA 최적화.
- ramdisk에 init scripts, default.prop. bootconfig(Android 12+)로 커널 cmdline 일부 대체.
- system-as-root: ramdisk가 system 파티션 루트로 마운트.
- OEM는 vbmeta chaining과 rolling key update를 관리해야 함. fastboot flashing lock/unlock이 키 체인에 영향.

## Init 및 서비스 관리
- init language: `service`/`on`/`setprop`/`import`. selabel/oneshot/user/group/capabilities 설정.
- property service: system properties(`ro.*`, `persist.*`) 관리. init trigger와 연동.
- ueventd: 디바이스 노드 권한 설정. vold: storage mount/obb/secure containers.
- `early-init`/`early-boot`/`late-start` 단계별 파이프라인. watchdog/bootstat 로그로 타이밍 측정.

## 부팅 최적화 포인트
- zygote preload 튜닝, dexopt 부팅 후 연기(PGO). lazy HAL/system service init.
- fs-verity/dm-verity overhead 고려. compressed APEX, fused load time.
- bootchart/trace로 boot time 측정.
- init rc minimalism, console spam 제거, parallel service start 여부. initfirststage vs secondstage 차이.\n
- bootstat metrics(boot_complete_time_ms, factory_reset_boot_complete_time_ms 등)으로 회귀 감지. boot resiliency를 위한 watchdog 설정.\n

## Links
- [[android-adb-and-images]]: adb/fastboot 사용법, 이미지 생성.
- [[android-evolution-history]]: system/vendor 분리와 mainline화 배경.
