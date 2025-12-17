---
title: android-architecture-stack
tags: [android, architecture, binder, hal, internals, kernel]
aliases: [Android Stack, 안드로이드 아키텍처]
date modified: 2025-12-17 21:14:22 +09:00
date created: 2025-12-16 15:22:42 +09:00
---

## Android Architecture: Not Just Linux

"안드로이드는 리눅스다." 이 말은 반은 맞고 반은 틀립니다.

안드로이드는 리눅스 커널을 사용하지만, **Standard Linux 배포판 (Ubuntu, Fedora) 과는 완전히 다른 철학**으로 설계되었습니다.

### 💡 Why it matters (Context)

- **Memory Pressure**: 일반 리눅스는 스왑 (Swap) 을 쓰지만, 안드로이드는 스왑을 쓰지 않습니다 (압축 스왑인 zRAM 만 사용). 그래서 **LMKD(Low Memory Killer Daemon)** 가 앱을 죽이는 기준이 리눅스의 OOM Killer 와 다릅니다. 이 차이를 모르면 "왜 내 앱이 백그라운드만 가면 죽지?"를 이해할 수 없습니다.
- **IPC Performance**: 리눅스의 DBus 는 느립니다. 안드로이드는 **Binder**라는 독자적인 드라이버를 커널에 박아서, 이미지 데이터를 복사 없이 (Zero-copy) 프로세스 간에 넘깁니다.
- **HAL Isolation**: 제조사 (Samsung, Pixel) 마다 카메라 센서가 달라도 앱은 똑같은 `Camera2 API` 를 씁니다. 중간에 **HIDL/AIDL**이 있기 때문입니다.

---

### 🐧 The Kernel: Androidisms

안드로이드 커널은 "Google Common Kernel"에서 파생됩니다. 주요 수정 사항은 **모바일 환경 (배터리, 터치, 메모리 부족)** 을 위해 추가되었습니다.

#### 1. Binder (IPC Driver)
- **Standard Linux**: System V IPC, Socket, DBus.
- **Android**: 프로세스 간 통신 (IPC) 이 너무 빈번해서 (Activity 실행, 센서 데이터 수신 등), 성능을 위해 커널 드라이버인 **Binder**를 만들었습니다.
    - **특징**: 데이터를 커널 공간에서 한 번만 복사합니다 (1-copy).
    - **보안**: 수신 측에서 `getCallingUid()` 로 발신자를 확실히 식별할 수 있습니다.

#### 2. Low Memory Killer Daemon (LMKD)
- **Standard Linux**: OOM Killer 는 시스템이 멈추기 직전에 가장 무거운 놈을 죽입니다.
- **Android**: 사용자 경험 (UX) 이 중요합니다. 메모리가 부족해지기 **전에** 우선순위가 낮은 앱 (Cached App) 부터 정리합니다.
    - `oom_adj_score`: 포그라운드 앱 (-1000) vs 백그라운드 앱 (900+). 점수가 높은 순으로 죽습니다.

#### 3. Wakelocks (Power Management)
- **Philosophy**: 안드로이드는 화면이 꺼지면 CPU 도 재웁니다 (Deep Sleep).
- **Problem**: 음악 앱은 화면이 꺼져도 노래를 틀어야 합니다.
- **Solution**: **Wakelock**을 잡아서 CPU 가 잠들지 못하게 막습니다. (배터리 소모의 주범)

---

### 🔌 Hardware Abstraction Layer (HAL)

앱 개발자는 `android.hardware.camera2` 만 알면 됩니다. 하드웨어가 소니 센서인지 삼성 센서인지는 몰라도 됩니다.

- **Legacy HIDL (Hardware Interface Definition Language)**: Android 8.0(Treble) 부터 도입. 하드웨어 드라이버를 별도 프로세스로 분리해, OS 업데이트 시 드라이버를 다시 컴파일하지 않아도 되게 했습니다.
- **Modern AIDL Stability**: Android 11+ 부터는 Binder AIDL 을 HAL 정의에도 사용합니다.

---

### 🦾 Native Userspace (C++)

자바 (Java/Kotlin) 프레임워크 아래에는 고성능 C++ 데몬들이 있습니다.

- **SurfaceFlinger**: 모든 앱의 `Surface` 를 받아서 화면에 합성 (Composite) 합니다. iOS 의 Render Server 와 같습니다.
- **AudioFlinger**: 여러 앱의 소리를 섞습니다 (Mixing).
- **Netd**: `iptables` 규칙을 설정하고 네트워크 트래픽을 제어합니다.

---

### ☕️ Java API Framework

앱 개발자가 주로 상호작용하는 계층입니다.

- **System Server**: `ActivityManager`, `WindowManager` 등 100 여 개의 시스템 서비스가 이 **하나의 거대 프로세스** 안에서 스레드로 돌아갑니다.
    - 앱이 죽어도 시스템은 살아야 하므로 별도로 존재합니다.
    - Binder 를 통해 앱과 통신합니다.

#### 📚 연결 문서
- [[android-glossary]] - 용어 사전
- [[android-boot-flow]] - 부팅 시 이 레이어들이 초기화되는 순서
- [[reference/android-activity-manager-and-system-services]] - System Server 심화
