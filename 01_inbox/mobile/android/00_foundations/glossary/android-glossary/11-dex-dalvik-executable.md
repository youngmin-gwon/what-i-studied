---
title: "DEX는 ART 런타임이 실행할 수 있도록 변환된 안드로이드 바이트코드다"
tags: ["android", "android/glossary"]
aliases: ["Dalvik Executable", "dex file"]
date modified: 2026-08-01 01:07:19 +09:00
date created: 2026-07-31 15:29:55 +09:00
---

# DEX는 ART 런타임이 실행할 수 있도록 변환된 안드로이드 바이트코드다

정의: DEX 는 Android runtime 이 실행하는 bytecode format 이며, Kotlin/Java bytecode 가 Android build pipeline 에서 변환된 결과물이다.

혼동 방지: DEX 는 APK 전체와 같지 않다. APK 는 resource, manifest, native library, signing block 까지 포함하는 install artifact 이고, DEX 는 그중 runtime code payload 다.

정본 링크:

- [ART and DEX execution](01_inbox/mobile/android/01_system_internals/boot-and-runtime/zygote-runtime-contracts/art-runs-dex-with-interpretation-jit-and-aot.md)
- [R8 and code optimization](01_inbox/mobile/android/03_packaging_deployment/optimization/build-optimization-contracts/r8-shrinks-optimizes-and-obfuscates-release-builds.md)
