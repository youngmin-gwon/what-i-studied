# Native Debugging (lldb)

상위 노트: [[android-debugging-techniques]]

```bash
# lldb 서버 시작
adb shell
lldb-server platform --listen "*:1234"

# Android Studio 에서
# Run → Attach Debugger to Android Process
# Debugger: Native
```

```cpp
// C++ 코드에 브레이크포인트 설정 가능
extern "C" JNIEXPORT void JNICALL
Java_com_example_app_NativeLib_processImage(
    JNIEnv* env,
    jobject /* this */,
    jobject bitmap) {
    
    // 여기에 브레이크포인트
    AndroidBitmapInfo info;
    AndroidBitmap_getInfo(env, bitmap, &info);
}
```
