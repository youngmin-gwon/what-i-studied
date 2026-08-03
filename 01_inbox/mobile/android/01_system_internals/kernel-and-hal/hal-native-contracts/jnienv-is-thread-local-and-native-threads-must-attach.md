---
title: jnienv-is-thread-local-and-native-threads-must-attach
tags: [android, android/native, android/system-internals]
aliases: [JavaVM, JNIEnv]
date modified: 2026-08-03 17:25:47 +09:00
date created: 2026-07-31 23:58:00 +09:00
---

## JNIEnv is thread local and native threads must attach

`JNIEnv*` 는 현재 thread 의 JNI interface 다. 다른 thread 로 넘겨 재사용할 수 없고, native code 가 thread 를 직접 만들었다면 그 thread 는 JVM 에 attach 된 상태가 아니다.

Native thread 에서 JNI 를 호출하려면 `JavaVM*` 를 보관해 두고 `AttachCurrentThread` 로 attach 한 뒤, thread 종료 전에 `DetachCurrentThread` 를 호출해야 한다. Java/Kotlin 에서 시작된 thread 는 runtime 이 이미 attach 한 상태다.

Class lookup 도 thread 와 class loader 문맥의 영향을 받는다. native worker thread 에서 `FindClass` 를 반복하기보다 `JNI_OnLoad` 나 명확한 managed entry point 에서 필요한 class reference 와 method ID 를 준비하는 패턴을 검토한다.

관련 노트: [JNI reference는 local, global, weak lifetime이 다르다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/jni-references-have-local-global-and-weak-lifetimes.md), [Native 성능과 crash debugging은 경계 비용에서 시작한다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/native-performance-and-crash-debugging-start-at-the-boundary.md)

출처: [Android JNI tips - threads](https://developer.android.com/ndk/guides/jni-tips#threads)
