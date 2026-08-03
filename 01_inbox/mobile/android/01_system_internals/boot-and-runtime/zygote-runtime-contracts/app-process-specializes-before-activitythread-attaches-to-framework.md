---
title: app-process-specializes-before-activitythread-attaches-to-framework
tags: [android, android/boot-runtime, android/runtime, android/system-internals]
aliases: ["앱 프로세스는 specialization 뒤 ActivityThread로 framework에 attach한다"]
date modified: 2026-08-03 17:24:01 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## 앱 프로세스는 specialization 뒤 ActivityThread 로 framework 에 attach 한다

상위 문서: [Zygote와 ART 런타임 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/zygote-runtime-contracts/zygote-runtime-contracts.md)

새 앱 프로세스는 fork 직후 아직 일반 앱이 아니다. Zygote 가 UID/GID, process name, runtime flags, classpath 같은 앱별 specialization 을 끝내고 나서 `ActivityThread.main()` 경로로 framework 에 attach 한다.

### 실무 의미

- `Application.onCreate()` 는 앱 process 가 framework 에 bind 된 뒤 실행되는 개발자 진입점이다.
- 앱 프로세스 시작 지연은 Zygote fork, class loading, bindApplication, content provider 초기화, Application 초기화 비용이 섞여 나타난다.
- app startup 분석은 process creation 과 첫 화면 draw 를 구분해야 한다.

### 관련 문서

- [앱 시작 성능의 측정 종료점은 실제 콘텐츠가 그려지는 시점으로 정의해야 한다](01_inbox/mobile/android/06_testing_performance/performance/performance-contracts/startup-performance-is-measured-by-ttid-and-ttfd.md)
- [AMS는 앱 프로세스와 컴포넌트 lifecycle을 조율한다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/ams-coordinates-app-process-and-component-lifecycle.md)
