---
title: android-hal-and-kernel
tags: [android, internals, hal, kernel, treble, driver]
aliases: [Android HAL, Treble, HIDL]
date modified: 2025-12-18 05:50:00 +09:00
date created: 2025-12-16 15:22:42 +09:00
---

# HAL & Kernel: The Hardware Bridge

앱 개발자는 `Camera API`를 호출하지만, 실제로 사진을 찍는 것은 삼성, 소니, LG가 만든 하드웨어 드라이버입니다.
이 둘 사이를 이어주는 것이 **HAL(Hardware Abstraction Layer)**입니다.

## 💡 Why it matters (Context)

-   **Fragmentations**: 안드로이드 초기("파편화의 지옥")에는 OS를 업데이트하려면 제조사가 드라이버를 다시 짜야 했습니다. 이 때문에 OS 업데이트가 매우 느렸습니다.
-   **Project Treble**: 이를 해결하기 위해 구글은 **"OS 프레임워크와 하드웨어 구현체의 분리"**를 선언했습니다. 이제 제조사는 드라이버를 건드리지 않고도 안드로이드 버전만 올릴 수 있습니다.
-   **Debugging**: 카메라 미리보기가 녹색으로 깨져서 나온다면? 앱 문제가 아니라 HAL 구현체의 버그일 확률이 높습니다.

---

## 🧱 The Evolution of HAL

### 1. Legacy HAL (~ Android 7.0)
-   **Link Style**: `.so` (공유 라이브러리) 형태.
-   **Load**: 시스템 프로세스(System Server)가 HAL 라이브러리를 **자신의 메모리 공간으로 직접 로드(`dlopen`)**해서 함수를 호출했습니다.
-   **문제점**: HAL에서 크래시가 나면 **시스템 전체가 죽습니다.** 보안적으로도 취약합니다.

### 2. HIDL (Android 8.0 ~)
-   **IPC Style**: HAL이 **별도의 프로세스**(`android.hardware.camera@2.4-service`)로 실행됩니다.
-   **Communication**: Binder를 통해 대화합니다.
-   **안정성**: HAL이 죽어도 시스템은 살 수 있습니다.

### 3. Java/AIDL HAL (Android 11 ~ Current)
-   **Next Gen**: 복잡한 HIDL 언어 대신, 기존 Binder AIDL을 그대로 사용합니다.
-   **Standardization**: C++뿐만 아니라 Java/Rust로도 HAL을 짤 수 있게 되었습니다.

---

## 🏗️ Project Treble Architecture

Treble의 핵심은 **"약속(Contract)"**입니다.

1.  **System Partition (Google)**: 안드로이드 프레임워크. `/system`.
2.  **Vendor Interface (VINTF)**: "우리는 이런 기능을 이런 버전으로 제공한다"는 명세서.
3.  **Vendor Partition (OEM)**: 하드웨어 드라이버 실제 구현체. `/vendor`.

> [!TIP] **GSI (Generic System Image)**
> Treble을 지원하는 모든 기기는 **"순정 안드로이드(GSI)"를 설치해도 부팅이 되어야 한다**는 규칙이 있습니다. 이는 커스텀 롬 개발자들에게 축복이 되었습니다.

---

## 🔌 Kernel: GKI (Generic Kernel Image)

옛날에는 기기마다 커널이 다 달랐습니다(Samsung Kernel, Pixel Kernel...).
Android 12부터는 **GKI**가 도입되었습니다.

-   **Core Kernel**: 구글이 배포하는 범용 커널 이미지. 제조사는 이걸 수정할 수 없습니다.
-   **Kernel Modules (`.ko`)**: 제조사는 필요한 드라이버(터치, 디스플레이)를 **모듈 형태**로만 추가할 수 있습니다.
-   **Effect**: 보안 패치가 나오면 구글이 커널만 쏙 바꿔 끼울 수 있게 되었습니다.

### 📚 연결 문서
- [android-architecture-stack](../00_foundations/android-architecture-stack.md) - HAL의 위치
- [android-binder-and-ipc](android-binder-and-ipc.md) - HAL과 통신하는 수단
- [android-boot-flow](android-boot-flow.md) - Vendor 파티션 마운트 과정
