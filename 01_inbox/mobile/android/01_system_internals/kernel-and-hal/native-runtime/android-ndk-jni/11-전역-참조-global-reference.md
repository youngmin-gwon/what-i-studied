# 전역 참조 (Global Reference)

상위 노트: [android-ndk-jni](01_inbox/mobile/android/01_system_internals/kernel-and-hal/native-runtime/android-ndk-jni.md)

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
