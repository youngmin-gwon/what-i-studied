---
title: android-adb-and-images
tags: [android, android/adb, android/fastboot, android/tools]
aliases: []
date modified: 2025-12-16 20:28:06 +09:00
date created: 2025-12-16 15:25:10 +09:00
---

## ADB, Fastboot, System Images android android/adb android/fastboot android/tools

PC 에서 기기를 다루는 기본 도구를 쉽게 정리했다. 용어는 [android-glossary](../00_foundations/android-glossary.md).

### ADB
- PC↔기기 통신용 다리. 명령 실행, 파일 복사, 로그 보기, 포트 포워딩을 한다.
- RSA 키나 QR 페어링으로 허용해야 한다. [[android-glossary#adb|ADB]] 키는 기기에 저장된다.
- userdebug/eng 빌드는 `adb root`/`adb remount` 가 가능하지만, 일반 사용자 빌드는 안 된다.

### Fastboot
- 부트로더 단계에서 이미지를 굽거나 정보를 읽는다.
- 언락/락 상태에 따라 할 수 있는 일이 달라지며, 언락하면 데이터가 지워진다.
- fastbootd 는 사용자 공간 fastboot 로, 동적 파티션 (super) 을 다룰 때 쓴다.

### 시스템 이미지
- boot/vendor_boot: 커널 + 램디스크.
- system/vendor/product 등은 OS 와 업체 코드.
- super.img 는 여러 파티션을 묶어놓은 큰 그릇.
- [[android-glossary#boot-image|Boot Image]] 포맷은 `mkbootimg` 로 만들고 `unpackbootimg` 로 풀어본다.

### 부팅/복구 테스트
- `fastboot boot <img>` 로 임시 부팅해볼 수 있다.
- `adb reboot bootloader/recovery/fastbootd` 로 모드를 바꾼다.
- `adb sideload update.zip` 으로 리커버리에서 업데이트를 적용한다.

### 디버깅 명령
- `adb shell dumpsys/cmd …` 로 시스템 상태를 본다.
- `adb logcat` 으로 로그를, `adb bugreport` 로 전체 상태를 모은다.
- perfetto/atrace/heapprofd 도 `adb shell` 에서 실행한다.
- screenrecord/screencap 으로 재현 영상을 남길 수 있다.

### 포트 포워딩
- `adb reverse`/`adb forward` 로 PC 와 기기 사이 포트를 잇는다 (웹뷰/디버거/테스트 서버 등).

### 에뮬레이터/원격 장치
- 에뮬레이터는 가상 기기다. 스냅샷으로 빨리 켤 수 있고, 가상 센서/위치/카메라 등을 테스트할 수 있다.
- Wi‑Fi ADB 로 케이블 없이 연결할 수 있지만, 보안을 위해 인증을 거친다.

### 링크

[android-boot-flow](../01_system_internals/android-boot-flow.md), [android-performance-and-debug](android-performance-and-debug.md), [android-customization-and-oem](../01_system_internals/android-customization-and-oem.md).
