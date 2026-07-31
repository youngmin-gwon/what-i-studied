---
title: "ART"
tags: ["android", "android/glossary"]
aliases: ["Android Runtime"]
---

# ART

정의: ART는 Android app의 DEX bytecode를 해석, JIT, AOT compilation으로 실행하는 runtime이다.

혼동 방지: ART 성능은 단순히 컴파일러 한 곳의 문제가 아니다. install-time profile, runtime JIT, idle compilation, baseline profile, startup path가 서로 다른 비용 지점을 가진다.

정본 링크:
- [ART execution contract](01_inbox/mobile/android/01_system_internals/boot-and-runtime/zygote-runtime-contracts/art-runs-dex-with-interpretation-jit-and-aot.md)
- [Profile guided compilation](01_inbox/mobile/android/01_system_internals/boot-and-runtime/zygote-runtime-contracts/profile-guided-compilation-splits-install-runtime-and-idle-costs.md)
