---
title: android-adb-and-images
tags: [android, android/adb, android/fastboot, android/tools]
aliases: []
date modified: 2025-12-16 15:41:16 +09:00
date created: 2025-12-16 15:25:10 +09:00
---

## ADB, Fastboot, System Images android android/adb android/fastboot android/tools

[[android-boot-flow]] · [[android-architecture-stack]] · [[android-performance-and-debug]]

### ADB 동작
- client(adb) → server → device daemon(adbd) 3 계층. USB/Bluetooth/Wi-Fi TCP 연결 지원.
- authorization: RSA key pair, device-side whitelist(`~/.android/adbkey`), pairing QR for Wi-Fi.
- transport: shell, exec-in, port forwarding(reverse), file sync(sideload/`adb push/pull`).

### adbd 모드
- user/userdebug/eng 빌드에 따라 root/disable-verity 가능 여부 다름.
- secure adb: ro.secure=1 이면 shell UID 제한. `adb root` 는 eng/userdebug 만 허용.
- daemon runs in separate SELinux domain(adbd), controls allowed commands.
- `adbd --incremental` 이 INCFS 설치를 지원. pair-based Wi-Fi ADB 는 pairing code/QR 요구.
- `adb remount` 는 verity 비활성화 후 system/vendor writable; user builds 는 금지.

### Fastboot
- 부트로더 모드에서 image flash/erase. `fastboot boot <img>` 로 임시 부팅.
- AVB unlock 상태에 따라 flash 제한. `fastboot oem lock/unlock` 데이터 초기화.
- Dynamic partitions: `fastboot flash super`, `fastboot create-logical-partition`.

### System Image 생성
- `m` 또는 `bazel` 빌드 시 out/target/product/<device>/ 디렉터리에 boot/system/vendor/product 이미지 생성.
- `mkbootimg`/`unpackbootimg` 로 boot image 분석. ramdisk cpio, kernel, cmdline, base/offset.
- sparse image format: fastboot/adb push 에 최적화, `simg2img` 로 raw 변환.
- `lpmake`/`lpflash` 로 super image 구성. `img2simg` 로 sparse 변환.
- vendor_boot/boot 이미지는 GKI ramdisk 분리 구조. bootconfig 에서 커널 플래그 주입.

### Boot/Recovery 테스트
- `fastboot boot` 로 테스트 부팅; `adb reboot bootloader/recovery/fastbootd`.
- `adb sideload update.zip` for recovery OTA. `update_engine_client --status` 로 OTA 진행 상황 확인.
- `adb shell getprop ro.boot.slot_suffix` 로 slot 확인. `bootctl set-active-boot-slot`.\n

### App/Service 디버깅
- `adb shell dumpsys`/`cmd` 시리즈: activity, package, window, batterystats, procstats, jobscheduler.
- `adb shell am start/startservice/broadcast` 로 인텐트 주입, `am force-stop`.
- `adb shell setprop` 로 system property 일시 변경. persist properties 는 재부팅 유지.
- `adb shell setenforce 0` 는 userdebug/eng 에서만. `adb bugreport` 로 전체 진단 zip 수집.
- `adb shell cmd stats pull-subconfig`, `cmd media.metrics` 등 서브시스템별 명령. `adb shell perfetto -b` for ring buffer traces.
- multi-device 환경: `adb devices -l`, `ANDROID_SERIAL` env, `-s`/`-t` 스위치. emulator/network test 에서 유용.

### 네트워크/포트 포워딩
- `adb reverse tcp:8081 tcp:8081`(React Native dev server), `adb forward tcp:9222 localabstract:chrome_devtools_remote`.
- Wi-Fi adb: `adb tcpip 5555` → `adb connect <ip>:5555`. pairing 모드 (ADB over Wi-Fi) 권장.
- jdwp forward 로 디버깅: `adb forward tcp:8700 jdwp:<pid>`. WebView/chrome remote debugging.\n

### Trace/Perf 수집
- `adb shell perfetto -c config.pbtx -o trace.perfetto-trace`. `atrace` 는 perfetto 앞단 래퍼.
- bugreport: `adb bugreport bug.zip`(ANR/crash/trace/log 포함). dropbox data 포함.
- `adb shell atrace gfx view sched freq idle binder_driver -t 10 -b 4096` quick traces. `heapprofd`/`meminfo` triggers via `cmd statsd`.
- perfetto UI 로 slicing/metrics 추출. trace-to-text(`perfetto traceconv text`).\n
- screenrecord/screencap via `adb shell screenrecord --bugreport` for repro capture. `adb tcpdump` with root builds for packet capture.

### Emulator/Device farm
- Android Emulator: qemu 기반, goldfish ranchu. AVX/Hypervisor 필수. `adb -s emulator-5554`.
- Gradle Managed Devices/Firebase Test Lab/ADB over SSH. headless/emulator snapshots.
- Emulator features: virtual sensors, GPS playback, hypervisor selection(HAXM/Hypervisor Framework/WSA), foldable/window resizing, cellular throttling.
- snapshot save/quickboot, emulator console(`telnet localhost 5554`). gRPC streaming for cloud emulators.

### 이미지 무결성과 보안
- dm-verity, AVB, vbmeta stitching. `avbtool verify_image`, `avbtool add_hash_footer`.
- `adb disable-verity`/`adb remount` 는 개발 빌드 전용. user 빌드에서는 동작하지 않음.

### 연계 링크
- [[android-boot-flow]]: 부팅 체인과 이미지 관계.
- [[android-customization-and-oem]]: OEM 빌드/플래싱 파이프라인.
- [[android-evolution-history]]: fastbootd/dynamic partition 도입.
