---
title: "Zygote"
tags: ["android", "android/glossary"]
aliases: ["Android Zygote"]
---

# Zygote

정의: Zygote는 framework class와 resource를 미리 로드한 뒤 app process를 fork해 startup cost와 memory sharing을 줄이는 Android process factory다.

혼동 방지: Zygote는 앱 lifecycle owner가 아니다. system_server가 launch를 요청하고 Zygote가 process를 fork한 뒤, app process가 ActivityThread를 통해 framework에 attach한다.

정본 링크:
- [Zygote preload contract](01_inbox/mobile/android/01_system_internals/boot-and-runtime/zygote-runtime-contracts/zygote-preloads-framework-state-before-app-fork.md)
- [App process specialization](01_inbox/mobile/android/01_system_internals/boot-and-runtime/zygote-runtime-contracts/app-process-specializes-before-activitythread-attaches-to-framework.md)
