---
title: ndk-is-native-library-toolchain-not-app-architecture
tags: [android, android/native, android/system-internals]
aliases: [NDK, Native Development Kit]
date modified: 2026-08-04 22:00:00 +09:00
date created: 2026-07-31 23:58:00 +09:00
---

## NDK는 앱 아키텍처가 아니라 native library toolchain 경계다

상위 문서: [HAL native contracts](hal-native-contracts.md)

Android NDK(Native Development Kit)는 Java/Kotlin 기반의 Android 앱 아키텍처 전체를 대체하는 프레임워크가 아니라, C/C++ 소스 코드를 Android 아키텍처(ARM64, x86_64)용 공유 라이브러리(`.so`)로 크로스 컴파일하고 NDK Stable C API 헤더에 링크하기 위한 **툴체인 및 빌드 도구 집합**이다.

앱의 뷰 라이프사이클, 권한 관리, UI 컴포지션(Jetpack Compose/View)은 여전히 Managed ART 런타임 위에서 실행되어야 하며, 무조건 "C++이 빠르다"는 맹목적 이유로 NDK를 도입하면 JNI 마샬링 비용, 메모리 파편화, 복잡한 ABI 빌드 관리 비용이 발생한다.

---

### 메커니즘: NDK 툴체인 범위 및 App Layering 구조

```mermaid
graph TD
    subgraph Managed App Layer (ART VM)
        A1["Kotlin / Java Application Code\n(Activity, Compose, ViewModel)"]
        A2["Android Framework API\n(ActivityManager, MediaCodec, Camera2)"]
        A1 --> A2
    end

    subgraph JNI Bridge Boundary
        B1["JNI Call Interface (JNIEnv*)"]
    end

    subgraph NDK Native Layer (C/C++)
        C1["Native Shared Library (.so)\n(C++ Engine, OpenCV, Game Logic)"]
        C2["NDK Stable C APIs\n(liblog, libandroid, libjnigraphics, libvulkan, libcamera2ndk)"]
        C1 --> C2
    end

    A1 -->|Invoke Native Method| B1
    B1 --> C1
```

1. **Stable NDK APIs**: Android OS 버전 간 ABI 호환성을 보장하는 공식 NDK API(`liblog.so`, `libandroid.so`, `libvulkan.so`, `libaaudio.so` 등)만 앱 라이브러리가 정적으로 링크할 수 있다. 비공개 내부 C++ 라이브러리(`libcutils.so`, `libutils.so`)를 동적 링크하면 OS 업데이트 시 앱이 크래시된다.
2. **Proper Use-cases**: NDK 도입이 정당화되는 영역은 (1) C/C++ 크로스 플랫폼 물리/게임 엔진 포팅, (2) 오디오 저지연(AAudio) 및 Vulkan 그래픽 렌더링, (3) 신호 처리 및 암호화 연산 같은 CPU 집약적 연산 영역이다.

---

### NDK Stable C API 활용 예시 (NativeWindow & Logging)

```cpp
#include <android/log.h>
#include <android/native_window.h>
#include <android/native_window_jni.h>

#define LOG_TAG "MyNativeEngine"
#define LOGI(...) __android_log_print(ANDROID_LOG_INFO, LOG_TAG, __VA_ARGS__)

extern "C" JNIEXPORT void JNICALL
Java_com_example_app_NativeEngine_initSurface(
        JNIEnv* env, jobject clazz, jobject surface) {
    
    // 1. Java Surface 객체로부터 NativeWindow 획득 (NDK Stable API)
    ANativeWindow* window = ANativeWindow_fromSurface(env, surface);
    if (!window) {
        __android_log_print(ANDROID_LOG_ERROR, LOG_TAG, "Failed to get ANativeWindow");
        return;
    }

    // 2. Native Buffer Format 및 Size 설정
    int32_t width = ANativeWindow_getWidth(window);
    int32_t height = ANativeWindow_getHeight(window);
    LOGI("ANativeWindow initialized: %d x %d", width, height);

    ANativeWindow_setBuffersGeometry(window, width, height, WINDOW_FORMAT_RGBA_8888);

    // 3. ANativeWindow 릴리스
    ANativeWindow_release(window);
}
```

---

### 실무 규칙

- NDK C++ 라이브러리를 빌드할 때 AOSP 내부 비공개 심볼이나 `/system/lib64/`의 프레임워크 전용 `.so` 파일에 직접 링킹을 시도해서는 안 된다. NDK sysroot(`sysroot/usr/include`)에 정의된 헤더만 사용해야 한다.
- ABI별 패키징 용량을 축소하기 위해 Play App Bundle(`.aab`)을 사용하여 사용자의 디바이스 ABI 아키텍처(예: `arm64-v8a`)에 해당하는 `.so` 바이너리만 맞춤형으로 다운로드되도록 배포 구조를 설계해야 한다.

---

### 관측 가능한 증거 (Observable Evidence)

1. **`readelf`를 통한 Native `.so` 파일의 NDK 의존성 심볼 검증**:
   ```bash
   readelf -d libnative-lib.so | grep NEEDED
   # 0x0000000000000001 (NEEDED) Shared library: [liblog.so]
   # 0x0000000000000001 (NEEDED) Shared library: [libandroid.so]
   # 0x0000000000000001 (NEEDED) Shared library: [libc++_shared.so]
   ```
2. **`dumpsys`를 통한 앱 CPU 아키텍처(ABI) 실행 상태 확인**:
   ```bash
   adb shell dumpsys package com.example.app | grep primaryCpuAbi
   # primaryCpuAbi=arm64-v8a
   ```

---

### 관련 문서

- [CMake, Gradle, ABI는 native build와 packaging 계약을 나눈다](cmake-gradle-and-abi-define-native-build-and-packaging.md)
- [JNI는 managed runtime과 native code 사이의 명시적 호출 경계다](jni-is-explicit-boundary-between-managed-runtime-and-native-code.md)
- [Native 성능과 crash debugging은 경계 비용에서 시작한다](native-performance-and-crash-debugging-start-at-the-boundary.md)

공식 문서: [Android NDK Concepts](https://developer.android.com/ndk/guides/concepts), [Android ABIs](https://developer.android.com/ndk/guides/abis)

