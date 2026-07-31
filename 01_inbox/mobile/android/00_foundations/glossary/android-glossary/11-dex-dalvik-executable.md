---
title: "DEX"
tags: ["android", "android/glossary"]
aliases: ["Dalvik Executable", "dex file"]
---

# DEX

정의: DEX는 Android runtime이 실행하는 bytecode format이며, Kotlin/Java bytecode가 Android build pipeline에서 변환된 결과물이다.

혼동 방지: DEX는 APK 전체와 같지 않다. APK는 resource, manifest, native library, signing block까지 포함하는 install artifact이고, DEX는 그중 runtime code payload다.

정본 링크:
- [ART and DEX execution](01_inbox/mobile/android/01_system_internals/boot-and-runtime/zygote-runtime-contracts/art-runs-dex-with-interpretation-jit-and-aot.md)
- [R8 and code optimization](01_inbox/mobile/android/03_packaging_deployment/optimization/build-optimization-contracts/r8-shrinks-optimizes-and-obfuscates-release-builds.md)
