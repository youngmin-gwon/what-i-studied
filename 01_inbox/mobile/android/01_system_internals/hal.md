---
title: hal
tags: [android, hal, hardware, system-internals]
aliases: []
date modified: 2026-08-06 16:42:09 +09:00
date created: 2026-08-06 16:31:18 +09:00
---

## HAL (Hardware Abstraction Layer)

### 1. 개요 (Overview)

**HAL (Hardware Abstraction Layer, 하드웨어 추상화 계층)**은 안드로이드 프레임워크(Android Framework)와 하위 [리눅스 커널(Linux Kernel)](../../../operating-systems/linux-kernel.md) 디바이스 드라이버 사이에 위치하는 표준 인터페이스 계층입니다.

카메라, 오디오, 센서, 블루투스, 바이트코드 변환기 등 특정 하드웨어의 고유한 구현 세부사항을 숨기고, 상위 프레임워크가 동일한 API 를 통해 다양한 제조사의 하드웨어를 제어할 수 있도록 돕습니다.

---

### 2. HAL 의 핵심 역할 및 존재 이유

1. **상위 프레임워크의 하드웨어 독립성 보장**
   - 안드로이드 자바/코틀린 프레임워크 코드는 카메라 제조사가 퀄컴(Qualcomm), 삼성(Exynos), 미디어텍(MediaTek)이든 상관없이 동일한 카메라 API 를 호출할 수 있습니다.
2. **벤더(Vendor) 코드와 프레임워크의 분리**
   - 하드웨어 제조사(OEM/SoC 벤더)가 제공하는 프로프라이어터리(Proprietary) 바이너리 드라이버와 상위 안드로이드 오픈소스 프로젝트(AOSP) 코드를 분리합니다.

---

### 3. HIDL 및 AIDL Stable HAL

안드로이드 8.0(Project Treble) 이전에는 HAL 이 상위 프레임워크와 동일한 프로세스 내에서 동작하는 공유 라이브러리(`.so`) 형태였습니다. 이로 인해 OS 업데이트 시 벤더 코드까지 모두 재작성해야 하는 문제가 발생했습니다. 이를 해결하기 위해 **Stable HAL** 인터페이스 개념이 도입되었습니다.

#### ① HIDL (HAL Interface Definition Language) - Android 8.0+
- 안드로이드 8.0(Project Treble)에서 도입된 바인더(Binder) 기반 인터페이스 정의 언어입니다.
- **프레임워크 - 벤더 분리**: 프레임워크 프로세스와 HAL 프로세스가 서로 분리되어 IPC(Binder)로 통신하게 되었습니다.
- **독립적 업데이트**: OS(프레임워크)를 업데이트하더라도 벤더 HAL 코드를 수정하거나 다시 빌드할 필요가 없어졌습니다.

#### ② AIDL (Android Interface Definition Language) Stable HAL - Android 11+
- 안드로이드 11 부터 기존의 HIDL 을 대체하고, 안드로이드 전반의 IPC 인터페이스 언어를 **AIDL**로 통일했습니다.
- 기존 앱 간 통신에 쓰이던 AIDL 을 시스템 및 벤더 영역까지 확장하여 **Stable AIDL** 구조를 성립시켰습니다.
- 버전 관리(Versioning)와 이전 버전 호환성이 대폭 강화되어, 안정적인 하드웨어 인터페이스 정의가 가능해졌습니다.

---

### 4. 구조 요약 (Architecture Stack)

```text
+---------------------------------------------------+
|             Android Application Layer             |
+---------------------------------------------------+
|         Java / Kotlin Framework Services          |
+---------------------------------------------------+
|      Stable HAL Interface (AIDL / HIDL)           |  <-- Treble 경계선
+---------------------------------------------------+
|         Vendor HAL Implementation (.so)           |
+---------------------------------------------------+
|        Linux Kernel Device Drivers                |
+---------------------------------------------------+
```

---

### 5. 연관 개념 (Related Notes)
- [Linux Kernel](../../../operating-systems/linux-kernel.md) - HAL 아래에서 하드웨어 장치 제어 드라이버를 제공하는 하위 운영체제 커널
- [ART (Android Runtime)](art.md) - HAL 위 프레임워크 및 앱 프로세스를 구동하는 런타임 환경
- [Binder IPC](binder-ipc.md) - Stable HAL(HIDL/AIDL) 통신에 쓰이는 IPC 메커니즘
- [system_server](../04_system_services/system-server.md) - HAL 을 사용하는 시스템 서비스 프로세스
