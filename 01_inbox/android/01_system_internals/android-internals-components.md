---
title: android-internals-components
tags: [android, android/internals, android/system-server]
aliases: []
date modified: 2025-12-16 16:03:13 +09:00
date created: 2025-12-16 15:26:56 +09:00
---

## Android Internals Components android android/internals android/system-server

system_server 안에서 돌고 있는 주요 서비스들을 쉬운 말로 요약했다. 용어는 [android-glossary](../00_foundations/android-glossary.md).

### system_server 가 하는 일
- [[android-glossary#ams|AMS/ATMS]] 로 앱과 화면을 관리한다.
- WindowManager 로 창 위치/크기/회전/입력을 다룬다.
- PackageManager 로 앱 설치/권한 기록/[[android-glossary#dex|dexopt]] 를 조정한다.
- Power/BatteryStats 로 전원 상태와 사용량을 기록한다.
- Connectivity/Telephony 로 네트워크/통신 상태를 조정한다.

### 입력·IME
- InputManager 가 키/터치 이벤트를 읽고 포커스 창에 전달한다.
- IME(InputMethod) 서비스가 키보드 창을 띄우고, Insets 로 화면을 맞춘다.

### 스토리지/파일
- vold/MountService 가 저장소를 마운트하고, [[android-glossary#fbe|FBE]] 키를 관리한다.
- StorageManager 가 용량/할당량을 관리하고, [[android-glossary#scoped-storage|Scoped Storage]] 규칙을 적용한다.

### 미디어/오디오/카메라
- AudioFlinger/Policy 가 소리를 섞고 길을 정한다.
- MediaCodec/Extractor/Drm 이 영상·음성을 인코딩/디코딩한다.
- CameraService 가 카메라 세션을 관리하고 권한을 검사한다.

### 보안/키
- Keystore/KeyMint 가 키를 안전하게 보관하고, StrongBox 가 있으면 하드웨어에서 보호한다.
- LockSettings 가 잠금/지문/얼굴 인증 흐름을 관리한다.

### 통계/로그
- statsd 가 시스템 숫자 (배터리, 네트워크, 앱 사용 등) 를 모은다.
- DropBox/bugreport 가 크래시/ANR/로그를 묶어 보관한다.

### 정책/프로필
- UserManager 가 여러 사용자/프로필을 관리한다 (Work Profile 등).
- DevicePolicyManager 가 기업 기기 정책을 적용한다 (잠금, 앱 허용 목록 등).

### SystemUI
- 상태바/알림/빠른 설정/내비게이션 바를 표시한다. 색상/테마는 Monet 가 결정한다.
- 잠금화면, 알림 순위, 대화·버블, 미디어 컨트롤을 다룬다.

### 디버깅
- `cmd activity/window/input/stats` 등으로 각 서비스를 살필 수 있다.
- Perfetto 로 Binder/입력/SurfaceFlinger/스케줄러를 한 번에 추적한다.

### 더 보기

[android-activity-manager-and-system-services](android-activity-manager-and-system-services.md), [android-boot-flow](android-boot-flow.md), [android-performance-and-debug](../06_testing_performance/android-performance-and-debug.md).
