---
title: jni-references-have-local-global-and-weak-lifetimes
tags: [android, android/native, android/system-internals]
aliases: [GlobalRef, JNI reference]
date modified: 2026-08-03 17:25:46 +09:00
date created: 2026-07-31 23:58:00 +09:00
---

## JNI references have local global and weak lifetimes

JNI object reference 는 native pointer 가 아니라 runtime handle 이며 수명 규칙이 있다. native method argument 와 대부분의 JNI return object 는 local reference 이고, 현재 native method 호출과 현재 thread 범위에서만 유효하다.

호출 이후에도 객체를 보관해야 하면 `NewGlobalRef` 나 `NewWeakGlobalRef` 로 별도 reference 를 만들어야 한다. global reference 는 `DeleteGlobalRef` 전까지 유효하지만 객체를 붙잡을 수 있으므로 callback/cache 처럼 필요한 경우에만 쓴다.

`jmethodID` 와 `jfieldID` 는 object reference 가 아니므로 global ref 로 감싸지 않는다. `jobject` 값을 `==` 로 비교하거나 map key 로 사용하는 것도 안전한 identity 모델이 아니다.

관련 노트: [JNI는 managed runtime과 native code 사이의 명시적 호출 경계다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/jni-is-explicit-boundary-between-managed-runtime-and-native-code.md), [JNI method/field ID와 pending exception은 runtime state다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/jni-method-field-ids-and-pending-exceptions-are-runtime-state.md)

출처: [Android JNI tips - local and global references](https://developer.android.com/ndk/guides/jni-tips#local-and-global-references)
