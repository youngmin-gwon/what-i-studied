---
title: JNI strings and arrays have copy pin and release contracts
tags: [android, android/native, android/system-internals]
aliases: [JNI string, JNI array]
date modified: 2026-07-31 23:58:00 +09:00
date created: 2026-07-31 23:58:00 +09:00
---

# JNI strings and arrays have copy pin and release contracts

JNI string/array API는 raw pointer 접근처럼 보여도 copy 또는 pin이 될 수 있는 runtime contract다. 포인터 주소가 managed object의 실제 주소라고 가정하거나, release 없이 오래 보관하면 GC와 memory behavior를 깨뜨릴 수 있다.

`GetStringUTFChars`와 `NewStringUTF`는 JNI Modified UTF-8 규칙을 전제로 한다. 외부 UTF-8 입력을 그대로 `NewStringUTF`에 넘기는 설계는 인코딩 검증과 변환을 별도 고려해야 한다.

Primitive array 접근에서 `Get<Type>ArrayElements`는 구현에 따라 copy 또는 pin을 반환할 수 있다. 단순 구간 복사는 `Get<Type>ArrayRegion`과 `Set<Type>ArrayRegion`이 release 누락 위험을 줄일 수 있다.

관련 노트: [JNI는 managed runtime과 native code 사이의 명시적 호출 경계다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/jni-is-explicit-boundary-between-managed-runtime-and-native-code.md), [AndroidBitmap native 접근은 format, stride, lock lifetime을 확인해야 한다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/androidbitmap-native-access-requires-format-stride-and-lock-lifetime.md)

출처: [Android JNI tips - strings](https://developer.android.com/ndk/guides/jni-tips#utf-8-and-utf-16-strings), [Android JNI tips - arrays](https://developer.android.com/ndk/guides/jni-tips#primitive-arrays)
