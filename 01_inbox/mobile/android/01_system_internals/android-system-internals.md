---
title: android-system-internals
tags: [android, internals, architecture, moc]
aliases: [안드로이드 시스템 인터널스]
date modified: 2026-04-07 10:45:00 +09:00
date created: 2026-04-07 10:45:00 +09:00
---

## [[mobile-security]] > [[android-system-internals]]

### Android System Internals: Architecture & Low-Level Mechanisms

안드로이드의 핵심 동작 원리, 프로세스 생명주기, 그리고 시스템 계층 간의 상호작용을 심층적으로 분석하는 지식 지도입니다.

---

#### 🏛️ 1. 핵심 아키텍처 (Core Architecture)

안드로이드의 전체적인 층구조와 기반 기술에 대해 다룹니다.

- [[android-architecture-stack]]: 전체 계층(Kernel, HAL, Framework) 구조 및 Binder IPC 기본.
- [[android-internals-components]]: `system_server` 내부 구성 요소 및 역할.
- [[android-os-development-guide]]: AOSP 전체 빌드 및 OS 레이어 개발 가이드.

---

#### ⚙️ 2. 부팅 및 런타임 (Boot & Runtime)

시스템이 켜지고 앱이 실행되는 전 과정을 다룹니다.

- [[android-boot-flow]]: 부틀로더부터 런처 실행까지의 흐름.
- [[android-init-and-services]]: `init.rc` 및 기반 데몬 프로세스들.
- [[android-zygote-and-runtime]]: Zygote 프로세스, ART(Android Runtime) 및 앱 포크(fork) 메커니즘.

---

#### 🧬 3. 프로세스 간 통신 및 서비스 (IPC & Services)

서로 다른 앱과 시스템 간의 고속 통신에 대해 다룹니다.

- [[android-binder-and-ipc]]: Binder 드라이버 상세 및 AIDL 통신 원리.
- [[android-activity-manager-and-system-services]]: AMS, WMS 등 주요 프레임워크 서비스 상세.
- [[android-native-services]]: SurfaceFlinger, AudioFlinger 등 C++ 기반 네이티브 서비스.

---

#### 🛠️ 4. 하드웨어 및 커널 (Hardware & Kernel)

물리적 자원 제어와 시스템 저수준 영역에 대해 다룹니다.

- [[android-hal-and-kernel]]: HAL(Hardware Abstraction Layer) 및 HIDL/AIDL 인터페이스.
- [[android-kernel]]: 리눅스 커널 기반의 안드로이드 고유 구현(Wakelocks, LMKD 등).
- [[android-process-and-memory]]: `oom_adj_score` 관리를 통한 메모리 제어 전략.

---

#### 📚 See Also
- [[android-foundations]] - 안드로이드 기본 개념 요약
- [[android-performance-and-debug]] - 시스템 진단 및 프로파일링
- [[android-adb-and-images]] - 시스템 이미지 관리 및 ADB 활용
