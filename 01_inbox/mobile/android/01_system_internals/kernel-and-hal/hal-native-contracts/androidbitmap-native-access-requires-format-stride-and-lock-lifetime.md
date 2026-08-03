---
title: androidbitmap-native-access-requires-format-stride-and-lock-lifetime
tags: [android, android/native, android/system-internals]
aliases: [AndroidBitmap, Bitmap native access]
date modified: 2026-08-03 17:25:35 +09:00
date created: 2026-07-31 23:58:00 +09:00
---

## AndroidBitmap native access requires format stride and lock lifetime

`AndroidBitmap_*` API 는 managed `Bitmap` 객체와 native pixel buffer 사이의 Android 전용 경계다. JNI object reference 를 받은 뒤 `AndroidBitmap_getInfo` 로 크기, format, stride 를 확인하고, `AndroidBitmap_lockPixels` 로 유효한 접근 범위를 얻는다.

한 행의 실제 바이트 폭을 `width * bytesPerPixel` 로 가정하면 stride padding 에서 깨질 수 있다. 다음 행으로 이동할 때는 `AndroidBitmapInfo.stride` 를 사용한다.

픽셀을 `uint32_t` 같은 타입으로 해석하기 전에 `format` 을 확인하고, 지원하지 않는 format 은 실패시킨다. `lockPixels` 이후의 모든 경로는 `unlockPixels` 를 보장해야 한다.

관련 노트: [JNI string/array 접근은 copy, pin, release 계약이다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/jni-strings-and-arrays-have-copy-pin-and-release-contracts.md), [Native 성능과 crash debugging은 경계 비용에서 시작한다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/native-performance-and-crash-debugging-start-at-the-boundary.md)

출처: [AndroidBitmap NDK reference](https://developer.android.com/ndk/reference/group/bitmap)
