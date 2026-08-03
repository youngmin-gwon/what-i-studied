---
title: app-launch-crosses-launcher-system-server-zygote-and-activitythread
tags: ["android", "android/foundations"]
aliases: []
date modified: 2026-08-03 17:22:48 +09:00
date created: 2026-07-31 23:04:26 +09:00
---

## 앱 실행은 Launcher, system_server, Zygote, ActivityThread 를 지나는 경로다

앱 아이콘을 탭하는 일은 단순히 `MainActivity.onCreate()` 를 호출하는 것이 아니다. Launcher 가 activity start 를 요청하고, system_server 의 activity/task 관리자가 대상 process 상태를 판단하며, 필요하면 Zygote 가 app process 를 fork 한다.

새 app process 는 framework 에 attach 되고 ActivityThread 를 통해 lifecycle callback 을 받는다. 여기서 Activity lifecycle, process priority, saved state, cold start 성능, permission/security check 가 함께 나타난다.

입문 문서에서는 이 흐름을 세부 sequence diagram 으로 길게 유지하기보다, 각 boundary 의 정본으로 연결하는 것이 낫다.

관련 노트: [AMS lifecycle](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/ams-coordinates-app-process-and-component-lifecycle.md), [Zygote/runtime](01_inbox/mobile/android/01_system_internals/boot-and-runtime/zygote-runtime-contracts/zygote-runtime-contracts.md), [Activity/app components](01_inbox/mobile/android/02_app_framework/architecture/app-components/android-app-components.md), [startup performance](01_inbox/mobile/android/06_testing_performance/performance/performance-contracts/startup-performance-is-measured-by-ttid-and-ttfd.md).

공식 문서: [Application fundamentals](https://developer.android.com/guide/components/fundamentals)
