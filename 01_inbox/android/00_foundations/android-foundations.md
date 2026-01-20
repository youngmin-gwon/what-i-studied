---
title: android-foundations
tags: [android, android/architecture, android/fundamentals, mobile/os]
aliases: []
date modified: 2026-01-20 15:55:12 +09:00
date created: 2025-12-16 15:22:14 +09:00
---

## Android Foundations

이 묶음은 안드로이드가 어떻게 움직이는지 아주 쉽게 풀어쓴 지도다. 어려운 말은 [android-glossary](android-glossary.md) 에 따로 정리했다.

### 안드로이드가 하는 일
- 스마트폰을 켜고, 앱을 실행하고, 배터리를 아끼고, 데이터를 지키는 일을 동시에 한다.
- 밑바닥에서는 [[android-glossary#리눅스 커널|리눅스 커널]] 이 기초를 잡고, 그 위에 [[android-glossary#binder|Binder]]/[[android-glossary#zygote|Zygote]]/[[android-glossary#art|ART]]/시스템 서비스가 쌓인다.
- 앱은 샌드박스 안에서 돌아가며, 서로와 시스템과 말할 때는 Binder 를 쓴다.

### 앱을 이루는 네 가지
- Activity: 화면을 보여주는 부분. 생명주기를 따라 켜고 끈다. [android-activity-manager-and-system-services](../01_system_internals/android-activity-manager-and-system-services.md)
- Service: 화면 없이 오래 일하는 부분. 음악 재생·위치 기록 같은 일을 맡는다. [android-binder-and-ipc](../01_system_internals/android-binder-and-ipc.md)
- BroadcastReceiver: 짧게 깨어나 알림을 받고 반응한다. 오래 하는 일은 WorkManager 에 넘긴다.
- ContentProvider: 앱 사이에 데이터를 안전하게 공유하는 창구.

### 앱이 실행될 때
- 앱마다 고유한 [[android-glossary#uid|UID]] 가 붙고, 각자 프로세스를 갖는다.
- 메인 스레드는 화면과 입력을 다룬다. 막히면 [[android-glossary#anr|ANR]] 이 뜬다.
- 오래 걸리는 일은 별도 스레드나 WorkManager/JobScheduler 에 맡긴다.

### 설치와 업데이트
- 앱은 [[android-glossary#apk|APK/AAB]] 형태로 온다. 서명이 맞아야 설치·업데이트가 된다.
- 설치 후 [[android-glossary#dex|DEX]] 를 기기에 맞게 최적화한다. 공간을 아끼고 속도를 높이기 위해 일부만 먼저 컴파일한다.

### 실행 엔진
- [[android-glossary#art|ART]] 가 DEX 를 실행한다. 자주 쓰는 코드는 미리 또는 실행 중에 빠르게 만든다.
- [[android-glossary#zygote|Zygote]] 가 공통 클래스를 미리 읽어 두었다가 새 앱을 빠르게 복사해 낸다.

### 리소스와 화면
- 기기 크기, 방향, 언어에 따라 알맞은 리소스를 자동으로 고른다.
- 앱 아이콘은 mipmap 디렉토리에, 일반 이미지는 drawable 디렉토리에 저장한다. mipmap 은 다양한 화면 밀도에 최적화된 아이콘용 구조다.
- 입력은 [android-activity-manager-and-system-services](../01_system_internals/android-activity-manager-and-system-services.md) 와 SurfaceFlinger 가 이어 받아 화면에 그린다.

### 데이터 보관
- 앱 전용 데이터는 앱만 읽을 수 있는 경로에 저장된다.
- 외부 저장소는 [[android-glossary#scoped-storage|Scoped Storage]] 규칙으로 나뉜다.
- 데이터베이스 (Room/SQLite) 나 DataStore 로 구조 있는 데이터를 쓴다.

### 네트워크와 배터리
- 네트워크 연결은 ConnectivityService 가 관리한다. 조건이 안 좋으면 작업을 미룬다.
- 배터리를 아끼기 위해 Doze/App Standby 가 있다. 정확한 알람은 제한된다.
- [[android-glossary#wakelock|Wakelock]] 은 꼭 필요할 때만, 짧게 쥔다.

### 권한
- 민감한 기능은 권한을 요청해 사용자가 허락해야 한다.
- 일부 권한은 한 번만, 또는 앱을 쓰는 동안만 허락할 수 있다.
- 권한 검사는 시스템 서비스가 [[android-glossary#binder|Binder]] 호출을 받을 때마다 한다.

### 배포와 업데이트
- Play 스토어는 점진적 배포, 롤백, 무결성 검사 (Play Integrity) 를 제공한다.
- 시스템은 [[android-glossary#apex|APEX/Mainline]] 로 일부 모듈을 따로 업데이트한다.

### 개발 기본기
- Kotlin/Jetpack 을 권장한다. Compose(새 UI) 와 View(기존 UI) 를 함께 쓸 수 있다.
- Gradle/AGP 로 빌드하고, Lint/Detekt 등으로 품질을 챙긴다.
- [android-performance-and-debug](../06_testing_performance/android-performance-and-debug.md) 에서 성능과 디버깅 흐름을 더 자세히 본다.

### 읽는 순서 제안

[android-architecture-stack](android-architecture-stack.md) → [android-hal-and-kernel](../01_system_internals/android-hal-and-kernel.md) → [android-zygote-and-runtime](../01_system_internals/android-zygote-and-runtime.md) → [android-binder-and-ipc](../01_system_internals/android-binder-and-ipc.md) → [android-activity-manager-and-system-services](../01_system_internals/android-activity-manager-and-system-services.md) → [android-security-and-sandboxing](../05_security_privacy/android-security-and-sandboxing.md) → [android-boot-flow](../01_system_internals/android-boot-flow.md)/[android-init-and-services](../01_system_internals/android-init-and-services.md) → [android-adb-and-images](../06_testing_performance/android-adb-and-images.md) → [android-graphics-and-media](../01_system_internals/android-graphics-and-media.md)/[android-connectivity-and-networking](../01_system_internals/android-connectivity-and-networking.md) → [android-customization-and-oem](../01_system_internals/android-customization-and-oem.md)/[android-os-development-guide](../02_app_framework/android-os-development-guide.md) → [android-evolution-history](android-evolution-history.md) → [android-performance-and-debug](../06_testing_performance/android-performance-and-debug.md)/[android-testing-and-quality](../06_testing_performance/android-testing-and-quality.md).
