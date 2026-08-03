---
title: "Android Glossary는 안드로이드 플랫폼의 핵심 개념을 정리한 용어집이다"
tags: ["android", "android/foundations", "android/glossary"]
aliases: ["Android Glossary", "Android 용어집"]
date modified: 2026-08-01 01:06:59 +09:00
date created: 2026-04-07 11:06:51 +09:00
---

# Android Glossary는 안드로이드 플랫폼의 핵심 개념을 정리한 용어집이다

용어장은 개념의 정본이 아니라 진입점이다. 각 항목은 짧은 정의, 혼동 방지 기준, 더 깊게 읽을 정본 링크만 유지한다. 약어의 뜻을 확인한 뒤 실제 판단은 연결된 subsystem 정본에서 한다.

### 사용하는 순서

1. 증상이나 문서에서 만난 용어를 책임 영역별 목록에서 찾는다.
2. 항목의 `정의`로 대상 계층을, `혼동 방지`로 이웃 개념과의 경계를 확인한다.
3. `정본 링크` 중 현재 질문에 가까운 계약 노트로 이동한다. 용어 항목 자체를 구현·운영 기준의 근거로 삼지 않는다.

새 용어 항목은 정의를 확장하는 대신 최소 두 개의 정본 링크가 있을 때 추가한다. 정본이 없으면 먼저 해당 subsystem에 판단 단위 노트를 만든다.

### 프로세스와 런타임

- [AMS와 ATMS](01_inbox/mobile/android/00_foundations/glossary/android-glossary/02-ams-atms-activitymanagerservice-activitytaskmanagerservice.md)
- [ANR](01_inbox/mobile/android/00_foundations/glossary/android-glossary/03-anr-application-not-responding.md)
- [ART](01_inbox/mobile/android/00_foundations/glossary/android-glossary/07-art-android-runtime.md)
- [DEX](01_inbox/mobile/android/00_foundations/glossary/android-glossary/11-dex-dalvik-executable.md)
- [Looper와 Handler](01_inbox/mobile/android/00_foundations/glossary/android-glossary/15-looper-handler.md)
- [system_server](01_inbox/mobile/android/00_foundations/glossary/android-glossary/23-system-server.md)
- [Zygote](01_inbox/mobile/android/00_foundations/glossary/android-glossary/29-zygote.md)

### IPC 와 서비스

- [Binder](01_inbox/mobile/android/00_foundations/glossary/android-glossary/08-binder.md)
- [Parcelable](01_inbox/mobile/android/00_foundations/glossary/android-glossary/18-parcelable.md)

### 커널과 HAL

- [HAL](01_inbox/mobile/android/00_foundations/glossary/android-glossary/14-hal-hardware-abstraction-layer.md)
- [LMKD](01_inbox/mobile/android/00_foundations/glossary/android-glossary/16-lmkd-low-memory-killer-daemon.md)
- [Wakelock](01_inbox/mobile/android/00_foundations/glossary/android-glossary/27-wakelock.md)

### 그래픽과 미디어

- [Surface와 SurfaceFlinger](01_inbox/mobile/android/00_foundations/glossary/android-glossary/22-surface-surfaceflinger.md)
- [Vsync와 Choreographer](01_inbox/mobile/android/00_foundations/glossary/android-glossary/25-vsync-choreographer.md)

### 앱 프레임워크

- [Context](01_inbox/mobile/android/00_foundations/glossary/android-glossary/10-context.md)
- [Scoped Storage](01_inbox/mobile/android/00_foundations/glossary/android-glossary/20-scoped-storage.md)

### 백그라운드 작업

- [Doze와 App Standby](01_inbox/mobile/android/00_foundations/glossary/android-glossary/12-doze-app-standby.md)
- [WorkManager와 JobScheduler](01_inbox/mobile/android/00_foundations/glossary/android-glossary/28-workmanager-jobscheduler.md)

### 보안과 권한

- [AppOps](01_inbox/mobile/android/00_foundations/glossary/android-glossary/06-appops-app-operations.md)
- [FBE](01_inbox/mobile/android/00_foundations/glossary/android-glossary/13-fbe-file-based-encryption.md)
- [SELinux](01_inbox/mobile/android/00_foundations/glossary/android-glossary/21-selinux-security-enhanced-linux.md)
- [UID](01_inbox/mobile/android/00_foundations/glossary/android-glossary/24-uid-user-id.md)
- [Verified Boot와 AVB](01_inbox/mobile/android/00_foundations/glossary/android-glossary/26-verified-boot-avb.md)

### 패키징과 업데이트

- [APEX](01_inbox/mobile/android/00_foundations/glossary/android-glossary/04-apex-android-pony-express.md)
- [APK와 AAB](01_inbox/mobile/android/00_foundations/glossary/android-glossary/05-apk-aab-android-package-android-app-bundle.md)
- [OTA](01_inbox/mobile/android/00_foundations/glossary/android-glossary/17-ota-over-the-air.md)

### 패키징과 리소스

- [Mipmap](01_inbox/mobile/android/00_foundations/glossary/android-glossary/31-mipmap.md)

### 성능

- [Baseline Profile](01_inbox/mobile/android/00_foundations/glossary/android-glossary/30-baseline-profile.md)

### 도구와 진단

- [ADB](01_inbox/mobile/android/00_foundations/glossary/android-glossary/01-adb-android-debug-bridge.md)
- [Bugreport](01_inbox/mobile/android/00_foundations/glossary/android-glossary/09-bugreport.md)
- [Perfetto](01_inbox/mobile/android/00_foundations/glossary/android-glossary/19-perfetto.md)
