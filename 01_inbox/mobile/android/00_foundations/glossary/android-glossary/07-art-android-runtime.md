---
title: "ART는 안드로이드 앱과 시스템 서비스가 실행되는 런타임 환경이다"
tags: ["android", "android/glossary"]
aliases: ["Android Runtime"]
date modified: 2026-08-01 01:07:17 +09:00
date created: 2026-07-31 15:29:55 +09:00
---

# ART는 안드로이드 앱과 시스템 서비스가 실행되는 런타임 환경이다

정의: ART 는 Android app 의 DEX bytecode 를 해석, JIT, AOT compilation 으로 실행하는 runtime 이다.

혼동 방지: ART 성능은 단순히 컴파일러 한 곳의 문제가 아니다. install-time profile, runtime JIT, idle compilation, baseline profile, startup path 가 서로 다른 비용 지점을 가진다.

정본 링크:

- [ART execution contract](01_inbox/mobile/android/01_system_internals/boot-and-runtime/zygote-runtime-contracts/art-runs-dex-with-interpretation-jit-and-aot.md)
- [Profile guided compilation](01_inbox/mobile/android/01_system_internals/boot-and-runtime/zygote-runtime-contracts/profile-guided-compilation-splits-install-runtime-and-idle-costs.md)
