---
title: android-ndk-jni
tags: [android, android/ndk, android/jni, android/native, cpp]
aliases: []
date modified: 2025-12-16 16:19:14 +09:00
date created: 2025-12-16 16:19:14 +09:00
---

## Android NDK & JNI android android/ndk android/jni android/native

Native Development Kit (NDK) 와 Java Native Interface (JNI) 사용법.

### NDK 란

C/C++ 코드를 Android 에서 실행할 수 있게 하는 도구.

**사용 이유:**
- 성능 최적화 (이미지 처리, 게임 엔진)
- 기존 C/C++ 라이브러리 재사용
- 플랫폼 독립적 코드 공유

### 프로젝트 설정

```kotlin
// build.gradle.kts
android {
    defaultConfig {
        ndk {
            abiFilters += listOf("armeabi-v7a", "arm64-v8a", "x86", "x86_64")
        }
        
        externalNativeBuild {
            cmake {
                cppFlags += "-std=c++17"
                arguments += "-DANDROID_STL=c++_shared"
            }
        }
    }
    
    externalNativeBuild {
        cmake {
            path = file("src/main/cpp/CMakeLists.txt")
            version = "3.22.1"
        }
    }
}
```

### CMakeLists.txt

```cmake
cmake_minimum_required(VERSION 3.22.1)
project("myapp")

# C++ 표준 설정
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 소스 파일
add_library(
    native-lib
    SHARED
    native-lib.cpp
    image_processor.cpp
    utils.cpp
)

# 헤더 파일 경로
target_include_directories(native-lib PRIVATE ${CMAKE_SOURCE_DIR}/include)

# Android 라이브러리 찾기
find_library(log-lib log)
find_library(android-lib android)
find_library(jnigraphics-lib jnigraphics)

# 링크
target_link_libraries(
    native-lib
    ${log-lib}
    ${android-lib}
    ${jnigraphics-lib}
)

# 외부 라이브러리 (예: OpenCV)
add_library(opencv SHARED IMPORTED)
set_target_properties(opencv PROPERTIES IMPORTED_LOCATION
    ${CMAKE_SOURCE_DIR}/../jniLibs/${ANDROID_ABI}/libopencv_java4.so)
target_link_libraries(native-lib opencv)
```

### JNI 기본

#### Kotlin/Java 에서 네이티브 함수 선언

```kotlin
class NativeLib {
    
    companion object {
        init {
            System.loadLibrary("native-lib")
        }
    }
    
    external fun stringFromJNI(): String
    external fun addNumbers(a: Int, b: Int): Int
    external fun processImage(bitmap: Bitmap): Bitmap
}

// 사용
val result = NativeLib().stringFromJNI()
```

#### C++ 구현

```cpp
// native-lib.cpp
#include <jni.h>
#include <string>
#include <android/log.h>

#define TAG "NativeLib"
#define LOGI(...) __android_log_print(ANDROID_LOG_INFO, TAG, __VA_ARGS__)
#define LOGE(...) __android_log_print(ANDROID_LOG_ERROR, TAG, __VA_ARGS__)

extern "C" JNIEXPORT jstring JNICALL
Java_com_example_app_NativeLib_stringFromJNI(
    JNIEnv* env,
    jobject /* this */) {
    
    std::string hello = "Hello from C++";
    return env->NewStringUTF(hello.c_str());
}

extern "C" JNIEXPORT jint JNICALL
Java_com_example_app_NativeLib_addNumbers(
    JNIEnv* env,
    jobject /* this */,
    jint a,
    jint b) {
    
    LOGI("Adding %d + %d", a, b);
    return a + b;
}
```

### JNI 타입 매핑

| Java/Kotlin | JNI | C/C++ |
|-------------|-----|-------|
| boolean | jboolean | unsigned char |
| byte | jbyte | signed char |
| char | jchar | unsigned short |
| short | jshort | short |
| int | jint | int |
| long | jlong | long long |
| float | jfloat | float |
| double | jdouble | double |
| String | jstring | - |
| Object | jobject | - |
| Array | jarray | - |

### 문자열 처리

```cpp
extern "C" JNIEXPORT jstring JNICALL
Java_com_example_app_NativeLib_processString(
    JNIEnv* env,
    jobject /* this */,
    jstring input) {
    
    // Java String → C++ string
    const char* nativeString = env->GetStringUTFChars(input, nullptr);
    std::string cppString(nativeString);
    env->ReleaseStringUTFChars(input, nativeString); // 메모리 해제 필수!
    
    // 처리
    cppString = "Processed: " + cppString;
    
    // C++ string → Java String
    return env->NewStringUTF(cppString.c_str());
}
```

### 배열 처리

```cpp
extern "C" JNIEXPORT jintArray JNICALL
Java_com_example_app_NativeLib_processArray(
    JNIEnv* env,
    jobject /* this */,
    jintArray input) {
    
    // 배열 길이
    jsize length = env->GetArrayLength(input);
    
    // Java 배열 → C 배열
    jint* nativeArray = env->GetIntArrayElements(input, nullptr);
    
    // 처리
    for (int i = 0; i < length; i++) {
        nativeArray[i] *= 2;
    }
    
    // C 배열 → Java 배열
    jintArray result = env->NewIntArray(length);
    env->SetIntArrayRegion(result, 0, length, nativeArray);
    
    // 메모리 해제
    env->ReleaseIntArrayElements(input, nativeArray, 0);
    
    return result;
}
```

### 객체와 메서드 호출

```cpp
extern "C" JNIEXPORT void JNICALL
Java_com_example_app_NativeLib_callJavaMethod(
    JNIEnv* env,
    jobject thiz) {
    
    // 클래스 찾기
    jclass clazz = env->GetObjectClass(thiz);
    
    // 메서드 ID 가져오기
    jmethodID methodId = env->GetMethodID(clazz, "onNativeCallback", "(I)V");
    
    if (methodId != nullptr) {
        // Java 메서드 호출
        env->CallVoidMethod(thiz, methodId, 42);
    }
    
    // 정적 메서드 호출
    jmethodID staticMethodId = env->GetStaticMethodID(clazz, "staticMethod", "()V");
    if (staticMethodId != nullptr) {
        env->CallStaticVoidMethod(clazz, staticMethodId);
    }
}

// Kotlin 에서 콜백 정의
class NativeLib {
    fun onNativeCallback(value: Int) {
        Log.d("NativeLib", "Callback: $value")
    }
    
    companion object {
        @JvmStatic
        fun staticMethod() {
            Log.d("NativeLib", "Static method called")
        }
    }
}
```

### Bitmap 처리

```cpp
#include <android/bitmap.h>

extern "C" JNIEXPORT jobject JNICALL
Java_com_example_app_NativeLib_processImage(
    JNIEnv* env,
    jobject /* this */,
    jobject bitmap) {
    
    AndroidBitmapInfo info;
    void* pixels;
    
    // Bitmap 정보 가져오기
    AndroidBitmap_getInfo(env, bitmap, &info);
    
    // Pixel 데이터 잠금
    AndroidBitmap_lockPixels(env, bitmap, &pixels);
    
    // 이미지 처리 (예: 그레이스케일)
    uint32_t* line = (uint32_t*)pixels;
    for (int y = 0; y < info.height; y++) {
        for (int x = 0; x < info.width; x++) {
            uint32_t pixel = line[x];
            
            int r = (pixel >> 16) & 0xFF;
            int g = (pixel >> 8) & 0xFF;
            int b = pixel & 0xFF;
            
            int gray = (r + g + b) / 3;
            
            line[x] = (0xFF << 24) | (gray << 16) | (gray << 8) | gray;
        }
        line = (uint32_t*)((char*)line + info.stride);
    }
    
    // Pixel 데이터 잠금 해제
    AndroidBitmap_unlockPixels(env, bitmap);
    
    return bitmap;
}
```

### 전역 참조 (Global Reference)

```cpp
// 전역 변수
static jobject g_callback = nullptr;

extern "C" JNIEXPORT void JNICALL
Java_com_example_app_NativeLib_setCallback(
    JNIEnv* env,
    jobject /* this */,
    jobject callback) {
    
    // 이전 참조 삭제
    if (g_callback != nullptr) {
        env->DeleteGlobalRef(g_callback);
    }
    
    // 전역 참조 생성 (GC 방지)
    g_callback = env->NewGlobalRef(callback);
}

extern "C" JNIEXPORT void JNICALL
Java_com_example_app_NativeLib_triggerCallback(
    JNIEnv* env,
    jobject /* this */) {
    
    if (g_callback != nullptr) {
        jclass clazz = env->GetObjectClass(g_callback);
        jmethodID methodId = env->GetMethodID(clazz, "onEvent", "()V");
        env->CallVoidMethod(g_callback, methodId);
    }
}

extern "C" JNIEXPORT void JNICALL
Java_com_example_app_NativeLib_cleanup(
    JNIEnv* env,
    jobject /* this */) {
    
    if (g_callback != nullptr) {
        env->DeleteGlobalRef(g_callback);
        g_callback = nullptr;
    }
}
```

### 스레딩

```cpp
#include <pthread.h>

static JavaVM* g_vm = nullptr;

// JNI_OnLoad 에서 JavaVM 저장
JNIEXPORT jint JNI_OnLoad(JavaVM* vm, void* reserved) {
    g_vm = vm;
    return JNI_VERSION_1_6;
}

void* threadFunction(void* arg) {
    JNIEnv* env;
    
    // 현재 스레드를 JVM 에 attach
    g_vm->AttachCurrentThread(&env, nullptr);
    
    // JNI 호출
    jclass clazz = env->FindClass("com/example/app/NativeLib");
    jmethodID methodId = env->GetStaticMethodID(clazz, "onThreadCallback", "()V");
    env->CallStaticVoidMethod(clazz, methodId);
    
    // Detach
    g_vm->DetachCurrentThread();
    
    return nullptr;
}

extern "C" JNIEXPORT void JNICALL
Java_com_example_app_NativeLib_startNativeThread(
    JNIEnv* env,
    jobject /* this */) {
    
    pthread_t thread;
    pthread_create(&thread, nullptr, threadFunction, nullptr);
    pthread_detach(thread);
}
```

### 예외 처리

```cpp
extern "C" JNIEXPORT void JNICALL
Java_com_example_app_NativeLib_throwException(
    JNIEnv* env,
    jobject /* this */) {
    
    jclass exceptionClass = env->FindClass("java/lang/RuntimeException");
    env->ThrowNew(exceptionClass, "Error from native code");
}

// 예외 확인
extern "C" JNIEXPORT jboolean JNICALL
Java_com_example_app_NativeLib_checkException(
    JNIEnv* env,
    jobject /* this */) {
    
    // Java 메서드 호출
    jclass clazz = env->FindClass("com/example/app/SomeClass");
    jmethodID methodId = env->GetMethodID(clazz, "riskyMethod", "()V");
    env->CallVoidMethod(clazz, methodId);
    
    // 예외 발생 확인
    if (env->ExceptionCheck()) {
        env->ExceptionDescribe(); // 로그에 출력
        env->ExceptionClear(); // 예외 클리어
        return JNI_TRUE;
    }
    
    return JNI_FALSE;
}
```

### 성능 최적화

```cpp
// ❌ 나쁜 예: 매번 클래스/메서드 찾기
for (int i = 0; i < 1000; i++) {
    jclass clazz = env->FindClass("com/example/app/MyClass");
    jmethodID methodId = env->GetMethodID(clazz, "method", "()V");
    env->CallVoidMethod(obj, methodId);
}

// ✅ 좋은 예: 한 번만 찾기
jclass clazz = env->FindClass("com/example/app/MyClass");
jmethodID methodId = env->GetMethodID(clazz, "method", "()V");
for (int i = 0; i < 1000; i++) {
    env->CallVoidMethod(obj, methodId);
}

// ✅ 더 좋은 예: 캐싱
static jclass g_clazz = nullptr;
static jmethodID g_methodId = nullptr;

if (g_clazz == nullptr) {
    jclass localClass = env->FindClass("com/example/app/MyClass");
    g_clazz = (jclass)env->NewGlobalRef(localClass);
    g_methodId = env->GetMethodID(g_clazz, "method", "()V");
}

for (int i = 0; i < 1000; i++) {
    env->CallVoidMethod(obj, g_methodId);
}
```

### 디버깅

```bash
# NDK 빌드 로그
./gradlew assembleDebug --info

# Native 크래시 로그
adb logcat | grep "DEBUG"

# lldb 디버깅
# Android Studio → Run → Debug 'app' (C++ 브레이크포인트 설정 가능)

# 심볼 파일 확인
ls app/build/intermediates/cmake/debug/obj/arm64-v8a/
```

### 더 보기

[android-performance-and-debug](../06_testing_performance/android-performance-and-debug.md), [android-gradle-build-system](android-gradle-build-system.md), [android-native-services](../../../../android-native-services.md)
