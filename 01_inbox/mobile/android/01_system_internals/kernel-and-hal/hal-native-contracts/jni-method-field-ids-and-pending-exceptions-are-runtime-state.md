---
title: JNI method field IDs and pending exceptions are runtime state
tags: [android, android/native, android/system-internals]
aliases: [JNI exception, jmethodID, jfieldID]
date modified: 2026-07-31 23:58:00 +09:00
date created: 2026-07-31 23:58:00 +09:00
---

`GetMethodID`, `GetStaticMethodID`, `GetFieldID`는 이름과 JNI signature를 runtime metadata로 해석해 ID를 돌려준다. 반복 호출 경로에서는 lookup 비용보다 class reference lifetime과 failure path를 함께 고려해 캐시한다.

JNI 호출이 Java exception을 발생시키면 native stack이 C++ exception처럼 자동 unwind되지 않는다. 현재 thread에 pending exception 상태가 남고, 대부분의 JNI 호출을 계속하면 안 된다.

`ExceptionCheck`, `ExceptionDescribe`, `ExceptionClear`, `Throw`, `ThrowNew`는 “native에서 예외를 던진다”보다 managed 경계로 돌아갈 pending state를 제어하는 API로 이해하는 편이 정확하다.

관련 노트: [JNI reference는 local, global, weak lifetime이 다르다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/jni-references-have-local-global-and-weak-lifetimes.md), [Native 성능과 crash debugging은 경계 비용에서 시작한다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/native-performance-and-crash-debugging-start-at-the-boundary.md)

출처: [Android JNI tips](https://developer.android.com/ndk/guides/jni-tips)
