---
title: android-init-and-services
tags: [android, android/boot, android/init]
aliases: []
date modified: 2025-12-16 15:41:54 +09:00
date created: 2025-12-16 15:34:24 +09:00
---

## Init & Service Lifecycle android android/init android/boot

[[android-boot-flow]] · [[android-hal-and-kernel]] · [[android-os-development-guide]]

### init 개요
- kernel → init(first stage) → second stage init 순으로 실행되며, SELinux 정책 로드와 기본 파일시스템 마운트를 담당.
- init language 는 declarative 한 rc DSL 로 트리거 기반 액션과 서비스 정의를 포함. 파서가 include/import 로 rc 조각을 병합.
- property service 는 init 내부에 존재하며 setprop/prop triggers 를 처리한다.

### rc 문법 주요 요소
- `on <trigger>` 블록: property, boot phase, file/boot events 에 반응. 예: `on boot`, `on property:sys.boot_completed=1`.
- `service <name> <path> [args]`: 실행 바이너리와 옵션. `class main/core/late_start` 로 그룹, `oneshot`/`disabled`/`seclabel`/`user`/`group`/`capabilities`.
- `import /system/etc/init/*.rc` 로 포함. APEX 는 `/apex/*/etc/init/*.rc` 자동 import.
- Commands: `setprop`, `write`, `chmod`, `chown`, `mkdir`, `exec`, `symlink`, `loglevel`, `setrlimit`, `class_start/stop` 등.

### 서비스 클래스와 부팅 단계
- `class core`: init 초기에 시작, property service/ueventd/vold 등 필수.
- `class main`: system_server 와 연관된 서비스. Zygote 시작도 포함.
- `class late_start`: boot completed 이후까지 지연 가능한 서비스.
- property trigger 예: radio up, vold ready, bootanim exit. 부팅 최적화 시 지연 가능한 서비스의 class 를 분리.

### property 시스템
- system properties 는 key/value, 최대 길이 제한. `ro.*`(read-only), `persist.*`(userdata 저장), `sys.*`(runtime) 등 prefix 로 구분.
- selinux rules 로 property write 제한. `ctl.start/stop/restart` 특수 property 는 init 이 서비스 제어.
- `getprop`/`setprop`/`resetprop`(magisk) 사용 시 권한 고려. `ro.debuggable`, `ro.secure` 등 부팅 모드 플래그 중요.

### A/B 및 dynamic partitions 고려
- init 은 slot suffix(`ro.boot.slot_suffix`) 를 참고해 올바른 파티션을 마운트. fstab entry 에 `slotselect` 옵션.
- dynamic partitions(super) 에서는 logical partition mapping 을 device mapper 로 준비 후 마운트.
- first stage init 이 dm-verity hash tree mount, FBE metadata unlock 을 준비.

### fstab 과 스토리지
- `fstab.<board>` 는 mount flags(fileencryption, quota, avb keys) 정의. first stage mount vs late mount 구분.
- FBE: `fileencryption=aes-256-xts:aes-256-cts` + `keydirectory=/metadata/vold/metadata_encryption`. metadata partition 활용.
- adoptable storage/portable storage 는 vold 가 처리; init 은 keymaster/keystore ready 트리거를 기다린다.

### SELinux 통합
- first stage init 에서 정책 로드 후 enforcing 모드 진입. policy checksum mismatch 시 부팅 실패.
- 서비스마다 `seclabel` 지정 또는 seapp_contexts mapping. file_contexts 로 파일 라벨 설정.
- `avc: denied` 발생 시 audit logs 를 통해 policy 수정; neverallow 규칙 검토 필수.
- property_contexts 에 정의되지 않은 property set 은 거부된다. vendor/system 파티션별 컨텍스트 분리 주의.
- permissive 모드는 userdebug/eng 에서만 허용, 제품 빌드에서는 금지. `setenforce 0` 가 boot verifier 에 영향.

### ueventd 와 디바이스 노드
- ueventd 는 커널 uevent 를 수신해 `/dev` 노드 권한/소유자/라벨을 설정. `ueventd.rc` 패턴 매칭 사용.
- modem/camera/sensor 등 노드 권한이 틀리면 HAL 이 실패하므로 bring-up 시 중요 체크 포인트.

### 서비스 데몬 관례
- system daemons 는 `-d` 옵션 또는 foreground 실행; init 이 SIGKILL/respawn 관리.
- `writepid` 로 cgroup/OOM adj 파일에 PID 기록. freezer/frozen 그룹을 위한 설정 가능.
- `oneshot` 서비스는 종료 후 respawn 하지 않음. `restart_period` 로 crash loop 완화.
- critical services 는 `onrestart` 블록을 사용해 복구 행동 (인터페이스 재설정, property set) 을 트리거.
- console service(eng) 와 user builds 의 차이를 이해: 콘솔/adb 권한 차이.

### 부팅 최적화 기법
- lazy start: property trigger 로 네트워크/미디어 등 지연 가능한 서비스 늦게 시작.
- parallelism: class grouping 과 dependency 최소화로 병렬 실행. bootchart/perfetto 로 의존성 확인.
- zram/init scripts 최적화, dexopt after boot deferred, app prefetch(preload) 관리.
- boot time budget 테이블을 만들어 각 단계 목표를 설정. blocking I/O 를 비동기로 전환하거나 property trigger 로 지연.\n

### 디버깅/트레이스
- `adb shell cat /proc/uptime`/`logcat -b events -s bootstat`/`dmesg`/`logcat` 으로 타이밍 분석.
- `bootchartd`/`perfetto --txt` with `sched/wm/sf/init` categories. `init.svc.*` properties 로 서비스 상태 체크.
- `ls -l /dev/.coldboot_done`/`/sys/fs/pstore` panic logs. `adb shell setprop persist.sys.boot.disable 1` 등 테스트 플래그.
- `tombstoned`/`debuggerd` 와 연계된 init crash dumps. `cat /proc/last_kmsg`/`/sys/fs/pstore/console-ramoops` for panic.
- init 자체 로그 (`/dev/kmsg` 에 prefix`init:`) 를 grep 하여 trigger 실행 순서 확인.\n

### zygote/system_server 스타트 연계
- init.rc 에서 zygote(zygote64/32/secondary) 서비스를 정의. `zygote` 가 listen socket 을 열고 AMS 가 fork 요청.
- system_server init 은 zygote 의 SystemServer.java entry 로 이어지며, binder/graphics/native services 의존성이 만족되어야 함.
- early-boot/boot_completed broadcast 전에 critical services ready 상태 확인.
- zygote arguments: --runtime-args --setuid/setgid --nice-name --instruction-set. priority/selabel/rlimit 등 init 에서 전달.
- webview/secondary zygote 는 특정 ABI/비트폭 전용으로 빠른 fork 제공.

### updatable components 와 init
- APEX 가 mount 된 후 `/apex/*/etc/init/*.rc` 가 추가되어 mainline 모듈의 daemons 가 등록 (Statsd/ART/Media/NNAPI 등).
- init 은 apexd service ready property 를 감시; apexd late start 가 boot time 에 영향.
- OTA 시 apexd checkpoint/rollback 데이터로 APEX 실패 복구.
- GKI ramdisk 에서는 vendor ramdisk(vendor_boot) 와 병합되어 init rc 가 구성; overlay order 확인 필요.

### 실전 트러블슈팅 체크리스트
- boot loop: last_kmsg/pstore, logcat early buffer, tombstone, watchdog stack. hal/service crash loop? init restart cause? VB/AVB verify?
- selinux denial flood: policy mismatch → audit2allow 로 원인 찾되 최소 정책 수정. neverallow hit 여부.
- fstab mount 실패: avb hash/tree, fsck, dynamic partition mapping 확인. metadata key 문제.
- property not set: context/perms/selinux check, persistent property area corruption.
- service not running: `init.svc.<name>` 값, crash logs, seclabel/permission mismatch.

### Graph Links
- [[android-boot-flow]]: 부팅 시퀀스와 파티션 구조.
- [[android-hal-and-kernel]]: 커널/드라이버/selinux 와의 접점.
- [[android-architecture-stack]]: 상위 프레임워크가 init 구성 위에 서는 방식.
