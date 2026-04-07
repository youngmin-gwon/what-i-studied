---
title: android-native-services
tags: [android, system, native, binder, hal]
aliases: [안드로이드 네이티브 서비스]
date modified: 2026-04-07 10:35:00 +09:00
date created: 2026-04-07 10:35:00 +09:00
---

## [[android-ndk-jni]] > [[android-native-services]]

### System-Level native Services: SurfaceFlinger, AudioFlinger & HAL

안드로이드 운영체제(OS)의 핵심 기능은 Java 가 아닌 C/C++ 로 구현된 **Native Service**들이 담당합니다. 이들은 시스템 부팅 시점에 시작되어 저수준 하드웨어 제어와 고성능 리소스 관리를 수행합니다.

---

#### 🏛️ 1. 핵심 시스템 서비스 (Key native Services)

이 서비스들은 `init.rc` 에 의해 시스템 부팅 시점에 실행되며, 프레임워크 계층에서 Binder IPC 를 통해 호출됩니다.

- **SurfaceFlinger**: 화면 합성을 담당. 앱의 버퍼를 조합하여 디스플레이로 전송.
- **AudioFlinger**: 오디오 재생 및 믹싱 관리. 하드웨어 추상화 계층(HAL)과 오디오 하드웨어 간의 통로.
- **MediaServer**: 카메라, 인코더, 오디오 재생(MediaPlayer) 등 멀티미디어 기능을 실행하는 전용 프로세스.
- **Vold (Volume Daemon)**: 스토리지(SD 카드, USB) 마운트 및 암호화 관리.
- **Logd**: 시스템 로그 처리를 위한 전용 데몬 프로세스.

---

#### 🧪 2. 바인더(Binder) IPC 와 Native 코드

프레임워크(Java/Kotlin)에서 Native 서비스를 호출하는 과정:

1. **ServiceManager**: 모든 시스템 서비스의 이름과 위치를 관리하는 허브.
2. **BpInterface / BnInterface**: 
   - **Bp (Binder Proxy)**: 클라이언트 측 프록시 (Framework 에서 호출).
   - **Bn (Binder Native)**: 실제 서비스 구현체 (Native 서비스 프로세스 내부).
3. **AIDL for Native**: C++ 에서도 서비스 인터페이스를 정의하기 위해 AIDL 을 사용합니다. (최신 버전은 NDK Backend 지원)

---

#### 🛠️ 3. HAL (Hardware Abstraction Layer)

하드웨어 제조사가 제공하는 드라이버를 안드로이드가 공통으로 사용할 수 있도록 추상화한 계층입니다.

- **HIDL (HAL Interface Definition Language)**: 프로젝트 트레블(Treble) 이후 도입된 인터페이스 정의 언어.
- **AIDL for HAL (Android 11+)**: HIDL 을 대체하여 시스템과 하드웨어 추상화 계층 간의 표준으로 자리 잡음.

---

#### 🔍 4. Native 서비스 디버깅

- **dumpsys**: `adb shell dumpsys media.camera` 등 특정 네이티브 서비스의 상세 상태 확인.
- **Service List**: `adb shell service list` 로 현재 실행 중인 모든 서비스 객체 확인.
- **System Logs**: `adb logcat -b system` 에서 시스템 레벨의 로그 추적.

---

#### 📚 See Also
- [[android-ndk-jni]] - 앱 수준의 네이티브 개발 (NDK)
- [[android-os-development-guide]] - 안드로이드 OS 빌드 및 소스 구조
- [[android-process-and-memory]] - 서비스 프로세스 관리 방식
