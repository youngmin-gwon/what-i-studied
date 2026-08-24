---
title: hal-native-boundary
tags: ["android", "android/native", "android/system-internals"]
aliases: ["HAL Native Boundary", "안드로이드 HAL 및 네이티브 경계"]
date modified: 2026-08-06 16:42:00 +09:00
date created: 2026-07-31 23:58:00 +09:00
---

## HAL and Native Boundary 개요 및 역할

안드로이드의 **HAL & Native Boundary**는 최하단 [Linux Kernel](../../../../operating-systems/linux-kernel.md) 드라이버 위에 위치하여, 상위 [자바 프레임워크](../boot-and-runtime/system-server/system-server.md) 및 [ART 런타임](../boot-and-runtime/zygote-runtime/art.md), NDK/C++ 라이브러리, 그리고 제조사 [HAL 하드웨어 코드](hal-native/hal-userspace-boundary.md)가 서로 통신하는 유저스페이스(Userspace) 경계 지점이다.

이 인덱스는 [HAL 레퍼런스](hal-native/hal-userspace-boundary.md), Project Treble, Stable AIDL/HIDL, NDK/JNI 네이티브 라이브러리 인터페이스를 체계적으로 연결하는 허브 역할을 수행한다.

---

### 1. 주요 경계 영역 구분 (Boundary Areas)

1. **Platform / Vendor 계층 경계**:
   - 상위 프레임워크와 제조사 [HAL](hal-native/hal-userspace-boundary.md) 코드가 [Binder IPC (Stable AIDL)](../ipc-and-process/binder-ipc.md)를 통해 IPC 경계를 지나는 유저스페이스 영역.
2. **App ➔ Native Code (JNI / NDK) 경계**:
   - 개발자가 C/C++ 로 작성한 NDK 라이브러리가 [ART 런타임](../boot-and-runtime/zygote-runtime/art.md) 환경의 자바 객체와 JNI(Java Native Interface)를 거쳐 주소 메모리를 전달하는 경계.

---

### 2. 문제 발생 시 추적 경로 (Debugging Boundaries)

- **Native Service 생성 또는 등록 실패**: `init.rc`, [Binder IPC](../ipc-and-process/binder-ipc.md), SELinux `avc: denied` 또는 Native Crash(Tombstone) 확인.
- **NDK / JNI 앱 Crash (SIGSEGV / Local Reference Leak)**: C/C++ 메모리 해제 실수, [스레드](../../../../computer-science/thread.md) 바인딩 위반, JNI 참조 수명주기 위반 조사.

---

### 연결 문서 (Reference Links)

- [HAL 레퍼런스](hal-native/hal-userspace-boundary.md) - 안드로이드 하드웨어 추상화 계층 레퍼런스
- [Android Kernel Runtime](android-kernel-runtime.md) - HAL 하부에서 작동하는 리눅스 커널 레퍼런스
- [ART Runtime 레퍼런스](../boot-and-runtime/zygote-runtime/art.md) - NDK/JNI 상위에 존재하는 자바 가상 머신 런타임
- [Binder IPC 레퍼런스](../ipc-and-process/binder-ipc.md) - Native Service 및 HAL 통신 IPC 통로
