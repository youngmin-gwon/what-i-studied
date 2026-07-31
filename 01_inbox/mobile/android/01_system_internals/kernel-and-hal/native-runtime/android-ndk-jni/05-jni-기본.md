# JNI 기본

상위 노트: [android-ndk-jni](01_inbox/mobile/android/01_system_internals/kernel-and-hal/native-runtime/android-ndk-jni.md)

##### Kotlin/Java 에서 네이티브 함수 선언

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

##### C++ 구현

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
