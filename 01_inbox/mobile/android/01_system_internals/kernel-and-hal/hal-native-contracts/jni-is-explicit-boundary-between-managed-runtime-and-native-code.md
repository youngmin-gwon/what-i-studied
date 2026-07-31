---
title: JNI is explicit boundary between managed runtime and native code
tags: [android, android/native, android/system-internals]
aliases: [JNI]
date modified: 2026-07-31 23:58:00 +09:00
date created: 2026-07-31 23:58:00 +09:00
---

# JNI is explicit boundary between managed runtime and native code

JNI는 Kotlin/Java managed runtime과 C/C++ native code 사이의 호출 경계다. `external` 함수 선언, `System.loadLibrary`, native method registration 또는 symbol lookup이 모두 이 경계를 구성한다.

`jint`, `jlong`, `jobject`, `jstring`, `jarray`는 C++에서 다루는 값처럼 보여도 JNI 호출 규약의 타입이다. 특히 object 계열은 native pointer가 아니라 runtime이 관리하는 reference handle로 취급해야 한다.

긴 함수명 규칙으로 symbol을 찾는 방식보다 `JNI_OnLoad`에서 `RegisterNatives`로 명시 등록하는 방식이 오류를 library load 시점에 드러내고 export symbol을 줄일 수 있다. 어떤 방식을 택하든 class name, method signature, class loader 문맥이 런타임 연결의 일부다.

관련 노트: [JNI reference는 local, global, weak lifetime이 다르다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/jni-references-have-local-global-and-weak-lifetimes.md), [JNIEnv는 thread-local이고 native thread는 attach가 필요하다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/jnienv-is-thread-local-and-native-threads-must-attach.md)

출처: [Android JNI tips](https://developer.android.com/ndk/guides/jni-tips)
