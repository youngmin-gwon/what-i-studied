---
title: android-hal-and-kernel
tags: []
aliases: []
date modified: 2026-04-05 17:42:40 +09:00
date created: 2026-03-21 16:47:09 +09:00
---

## [[mobile-security]] > [[android-hal-and-kernel]]

### HAL & Kernel: The Hardware Abstraction Layer

앱 개발자는 `Camera API` 를 호출하지만, 실제로 사진을 찍는 것은 삼성, 소니 등 제조사가 만든 하드웨어 드라이버입니다. 이 둘 사이를 표준화된 인터페이스로 이어주는 계층이 바로 **HAL(Hardware Abstraction Layer)**입니다.

---

#### 💡 Context: 왜 하드웨어를 추상화해야 하는가?

- **Project Treble**: 과거에는 OS 업데이트 시 제조사가 드라이버를 매번 재컴파일해야 했습니다. Treble 도입 이후 OS 프레임워크와 하드웨어 구현체가 분리되어 업데이트 속도가 비약적으로 빨라졌습니다.
- **System Stability**: HAL 이 별도 프로세스로 실행됨에 따라, 드라이버 내부의 오류가 발생해도 시스템 전체(System Server)가 크래시되는 것을 방지합니다.
- **Uniform API**: 앱 개발자는 하드웨어의 종류와 관계없이 동일한 안드로이드 표준 API 를 사용할 수 있습니다.

---

#### 🧱 HAL 의 진화 (The Evolution of HAL)

##### 1. Legacy HAL (~ Android 7.0)
- **Link Style**: `.so` 공유 라이브러리 형태.
- **Load**: 시스템 프로세스가 HAL 을 자신의 메모리 공간으로 직접 로드(`dlopen`)했습니다.
- **단점**: HAL 에서 크래시가 나면 시스템 전체가 죽으며 보안적으로도 취약합니다.

##### 2. HIDL (Android 8.0 ~)
- **IPC Style**: HAL 이 별도의 프로세스(`android.hardware.*-service`)로 독립하여 실행됩니다.
- **Communication**: **Binder**를 통해 프레임워크와 통신합니다. (Project Treble 의 핵심)

##### 3. AIDL HAL (Android 11 ~ Current)
- **Next Gen**: 복잡한 HIDL 대신 표준 Binder **AIDL**을 그대로 사용하여 구현이 간소화되었습니다.
- **Standardization**: C++, Java 뿐만 아니라 **Rust**로도 HAL 을 작성할 수 있게 되었습니다.

---

#### 🐧 Kernel: GKI (Generic Kernel Image)

과거 기기마다 파편화되어 있던 커널을 통합하기 위해 Android 12 부터 **GKI**가 도입되었습니다.

- **Core Kernel**: 구글이 배포하는 범용 커널 이미지로, 제조사는 이를 수정할 수 없습니다.
- **Kernel Modules (`.ko`)**: 제조사는 필요한 드라이버만 모듈 형태로 추가합니다.
- **보안**: 커널 취약점 발견 시 구글이 직접 보안 패치를 적용한 커널로 교체하기 쉬워졌습니다.

---

#### 📚 연관 문서 및 심화 학습
- [[android-architecture-stack]] - 안드로이드 전체 계층 구조에서의 HAL
- [[android-binder-and-ipc]] - HAL 과 프레임워크 간의 통신 수단
- [[android-boot-flow]] - 부팅 과정에서의 드라이버 및 파티션 로드
- [[android-kernel]] - 안드로이드 커널 보안 및 특징
