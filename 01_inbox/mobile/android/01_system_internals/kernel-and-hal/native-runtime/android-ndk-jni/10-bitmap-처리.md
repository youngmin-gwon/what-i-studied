# Bitmap 처리

상위 노트: [android-ndk-jni](01_inbox/mobile/android/01_system_internals/kernel-and-hal/native-runtime/android-ndk-jni.md)

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
