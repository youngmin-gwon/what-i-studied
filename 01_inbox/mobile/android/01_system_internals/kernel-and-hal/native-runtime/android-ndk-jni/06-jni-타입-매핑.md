# JNI 타입 매핑

상위 노트: [android-ndk-jni](01_inbox/mobile/android/01_system_internals/kernel-and-hal/native-runtime/android-ndk-jni.md)

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
