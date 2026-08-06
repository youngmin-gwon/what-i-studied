---
title: android-glossary
tags: ["android", "android/foundations", "android/glossary"]
aliases: ["Android Glossary", "Android 용어집"]
date modified: 2026-08-06 18:51:13 +09:00
date created: 2026-04-07 11:06:51 +09:00
---

## Android Glossary 는 안드로이드 플랫폼의 핵심 개념을 정리한 용어집이다

용어장은 개념의 정본이 아니라 진입점이다. 각 항목은 짧은 정의, 혼동 방지 기준, 더 깊게 읽을 정본 링크만 유지한다. 약어의 뜻을 확인한 뒤 실제 판단은 연결된 subsystem 정본에서 한다.

### 사용하는 순서

1. 증상이나 문서에서 만난 용어를 책임 영역별 목록에서 찾는다.
2. 항목의 `정의` 로 대상 계층을, `혼동 방지` 로 이웃 개념과의 경계를 확인한다.
3. `정본 링크` 중 현재 질문에 가까운 계약 노트로 이동한다. 용어 항목 자체를 구현·운영 기준의 근거로 삼지 않는다.

새 용어 항목은 정의를 확장하는 대신 최소 두 개의 정본 링크가 있을 때 추가한다. 정본이 없으면 먼저 해당 subsystem 에 판단 단위 노트를 만든다.

### 프로세스와 런타임

- [AMS와 ATMS](../../04_system_services/system-server.md)
- [ANR](../../01_system_internals/boot-and-runtime/system-server-contracts/anr-is-responsiveness-contract-violation-not-single-timeout.md)
- [ART](../../01_system_internals/art.md)
- [DEX](../../01_system_internals/android-compilation-pipeline.md)
- [Looper와 Handler](../../02_app_framework/handler-looper-message-queue.md)
- [system_server](../../04_system_services/system-server.md)
- [Zygote](../../01_system_internals/zygote.md)

### IPC 와 서비스

- [Binder](../../01_system_internals/binder-ipc.md)
- [Parcelable](../../01_system_internals/binder-ipc.md)

### 커널과 HAL

- [HAL](../../01_system_internals/hal.md)
- [LMKD](../../01_system_internals/lmk-low-memory-killer.md)
- [Wakelock](../../04_system_services/job-scheduler.md)

### 그래픽과 미디어

- [Surface와 SurfaceFlinger](../../04_system_services/window-manager-service.md)
- [Vsync와 Choreographer](../../02_app_framework/custom-view.md)

### 앱 프레임워크

- [Context](../../../../computer-science/context.md)
- [Scoped Storage](../../05_security_privacy/secure-storage/ce-vs-de-storage.md)

### 백그라운드 작업

- [Doze와 App Standby](../../04_system_services/job-scheduler.md)
- [WorkManager와 JobScheduler](../../04_system_services/job-scheduler.md)

### 보안과 권한

- [AppOps](../../05_security_privacy/appops-and-permissions.md)
- [FBE](../../05_security_privacy/secure-storage/ce-vs-de-storage.md)
- [SELinux](../../01_system_internals/kernel-and-hal/kernel-contracts/selinux-policy-controls-binder-service-and-file-boundaries.md)
- [UID](../../05_security_privacy/appops-and-permissions.md)
- [Verified Boot와 AVB](../overview/foundation-contracts/android-security-is-layered-from-uid-sandbox-to-permissions-and-verified-boot.md)

### 패키징과 업데이트

- [APEX](../../01_system_internals/platform-modularity/android-platform-modularity.md)
- [Play app signing은 업로드 키와 앱 서명 키를 분리한다](../../03_packaging_deployment/distribution/release-distribution-contracts/play-app-signing-separates-upload-key-and-app-signing-key.md)
- [OTA](../../01_system_internals/platform-modularity/android-platform-modularity.md)

### 패키징과 리소스

- [Mipmap](../../02_app_framework/custom-view.md)

### 성능

- [Baseline Profile](../../01_system_internals/dex2oat.md)

### 도구와 진단

- [ADB](../../06_testing_performance/debugging/debugging-contracts/logcat-crash-anr-and-debugger-answer-different-questions.md)
- [Bugreport](../../06_testing_performance/debugging/debugging-contracts/logcat-crash-anr-and-debugger-answer-different-questions.md)
- [Perfetto](../../06_testing_performance/ttid-and-ttfd.md)
