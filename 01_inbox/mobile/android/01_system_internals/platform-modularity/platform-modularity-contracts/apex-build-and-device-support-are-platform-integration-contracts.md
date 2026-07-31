---
title: "APEX build와 device support는 앱 개발 API가 아니라 플랫폼 통합 계약이다"
tags: ["android", "android/system-internals"]
---

# APEX build와 device support는 앱 개발 API가 아니라 플랫폼 통합 계약이다

APEX를 만들고 업데이트 가능하게 하려면 Soong module definition, signing key, init service override, kernel support, device makefile, partition policy가 맞아야 한다. 이는 일반 앱 개발자가 Gradle dependency를 추가하는 문제와 다르다.

APEX Mainline module을 지원하려면 loopback driver와 dm-verity 같은 kernel feature가 필요하고, device는 updatable APEX 구성을 포함해야 한다. service를 APEX로 옮길 때도 init `.rc`와 `override` 같은 boot-time service 규칙을 따라야 한다.

따라서 앱 문서에서 APEX build detail을 깊게 설명할 필요는 없다. 이 주제는 AOSP/platform integration 정본에 두고, 앱 개발자는 SDK Extension 또는 feature check 쪽으로 이동한다.

관련 노트: [SDK Extension compile/runtime check](01_inbox/mobile/android/01_system_internals/platform-modularity/platform-modularity-contracts/sdk-extension-compile-sdk-extension-and-runtime-check-are-separate-steps.md), [kernel runtime 정본](01_inbox/mobile/android/01_system_internals/kernel-and-hal/android-kernel-runtime.md), [GKI 정본](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/gki-splits-generic-core-from-vendor-modules.md).

공식 문서: [APEX file format](https://source.android.com/docs/core/ota/apex)
