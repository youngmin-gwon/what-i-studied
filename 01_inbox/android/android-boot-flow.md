---
title: android-boot-flow
tags: [android, android/boot, android/system-images]
aliases: []
date modified: 2025-12-16 20:46:54 +09:00
date created: 2025-12-16 15:24:47 +09:00
---

## Boot Flow & System Images android android/boot android/system-images

기기가 켜질 때 일어나는 일을 순서대로 적었다. 낯선 용어는 [[android-glossary]].

### 순서 한눈에 보기
1. 부트 ROM: 칩에 박힌 코드가 첫 부트로더를 읽는다.
2. 부트로더: [[android-glossary#verified-boot|부팅 무결성]] 을 확인하고, 어느 슬롯을 쓸지 고른다.
3. [[android-glossary#boot-image|커널+램디스크]] 로드: 장치 트리, 명령줄을 건넨다.
4. init: rc 스크립트를 읽고 기본 서비스를 켠다.
5. [[android-glossary#zygote|Zygote]]/[[android-glossary#system-server|system_server]]: 앱 공장과 핵심 서비스가 뜬다.
6. System UI/런처: 사용자가 만나는 화면이 보인다.

### 파티션 구조 (간단)
- boot/vendor_boot: 커널 + 램디스크.
- system/system_ext/vendor/odm/product: OS 와 업체 맞춤 부분.
- userdata: 사용자 데이터, [[android-glossary#fbe|암호화]] 적용.
- super: 위 파티션을 논리적으로 담는 큰 그릇.

### 업데이트 방식
- [[android-glossary#ota|A/B OTA]]: 보이지 않는 슬롯에 미리 설치하고, 다음 부팅 때 바꾼다. 실패하면 되돌릴 수 있다.
- Virtual A/B: 스냅샷을 써서 공간을 덜 차지한다.

### Fastboot/Recovery/ADB 모드
- Fastboot: 부트로더 모드에서 이미지 정보를 읽고 굽는다.
- fastbootd: 사용자 공간 fastboot. 동적 파티션을 손댈 때 쓴다.
- Recovery: update.zip 을 적용하거나 공장 초기화.
- [[android-glossary#adb|ADB]]: USB/Wi‑Fi 디버깅. userdebug/eng 만 루트·verity 해제가 된다.

### Init 와 서비스
- init.rc 는 트리거 (`on boot`, `on property:…`) 와 서비스 정의 (`service name path`) 를 담는다.
- property 서비스가 `setprop` 요청을 받고, 필요하면 서비스 시작/중지를 건드린다.
- [[android-init-and-services]] 에서 더 길게 설명한다.

### 부팅 최적화 포인트
- 필요 없는 서비스는 나중에 켜거나 끈다.
- [[android-glossary#zygote#preload|Preload]] 목록을 조정해 메모리/속도를 균형 잡는다.
- bootstat/trace 로 시간이 어디서 쓰이는지 본다.

### 이미지와 무결성
- system/vendor 등은 dm-verity 로 보호된다.
- [[android-glossary#verified-boot|AVB]] 키가 맞아야 부팅한다. 잠금 해제 시 데이터가 초기화된다.

### 링크

[[android-adb-and-images]], [[android-hal-and-kernel]], [[android-init-and-services]], [[android-evolution-history]].
