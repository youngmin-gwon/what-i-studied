---
title: "Zygote는 공통 프레임워크 리소스를 미리 로드하고 앱 프로세스를 빠르게 포크(fork)하는 프로세스 템플릿이다"
tags: ["android", "android/glossary"]
aliases: ["Android Zygote"]
date modified: 2026-08-01 01:07:53 +09:00
date created: 2026-07-31 15:29:55 +09:00
---

# Zygote는 공통 프레임워크 리소스를 미리 로드하고 앱 프로세스를 빠르게 포크(fork)하는 프로세스 템플릿이다

정의: Zygote 는 framework class 와 resource 를 미리 로드한 뒤 app process 를 fork 해 startup cost 와 memory sharing 을 줄이는 Android process factory 다.

혼동 방지: Zygote 는 앱 lifecycle owner 가 아니다. system_server 가 launch 를 요청하고 Zygote 가 process 를 fork 한 뒤, app process 가 ActivityThread 를 통해 framework 에 attach 한다.

정본 링크:

- [Zygote preload contract](01_inbox/mobile/android/01_system_internals/boot-and-runtime/zygote-runtime-contracts/zygote-preloads-framework-state-before-app-fork.md)
- [App process specialization](01_inbox/mobile/android/01_system_internals/boot-and-runtime/zygote-runtime-contracts/app-process-specializes-before-activitythread-attaches-to-framework.md)
