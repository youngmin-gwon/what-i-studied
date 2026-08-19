---
title: android-foundation-map
tags: ["android", "android/foundations"]
aliases: []
date modified: 2026-08-06 15:35:57 +09:00
date created: 2026-08-03 16:59:22 +09:00
---

## Android Foundation Map 은 안드로이드 시스템의 전체적인 멘탈 모델을 제공하는 지도다

Android foundations 는 세부 API 설명이 아니라 전체 Android 지식 지도를 제공하는 입구다. 먼저 플랫폼 계층을 잡고, 버전 축과 용어를 확인한 뒤, 실제 문제를 소유한 정본 영역으로 이동한다.

### 읽는 순서

1. [Android System Map](overview/android-system-map.md) 에서 kernel 부터 app 까지 책임 계층을 구분한다.
2. 아래 12 장 Learning Spine 을 순서대로 읽어 source, process, component, state, concurrency, UI, data, security, capability, testing, compatibility 의 인과 관계를 잡는다.
3. [Android Learning Path](learning/android-learning-path.md) 에서 자신의 배경과 프로젝트 질문에 맞는 보충 경로를 고른다.
4. 버전 의존 동작이면 [Android Release History](history/android-release-history.md) 에서 API level, target SDK, extension/minor SDK 축을 분리한다.
5. 낯선 약어는 [Android Glossary](../04_system_services/activity-manager-service.md) 에서 뜻만 확인하고 연결된 정본으로 이동한다.

### Learning Spine

1. [Android 생태계와 계약 표면](learning-spine/01-android-ecosystem-and-surfaces.md)
2. [플랫폼 실행 계층과 호출 경로](learning-spine/02-android-platform-execution-layers-and-call-paths.md)
3. [소스에서 설치 패키지까지](learning-spine/03-source-to-installed-package.md)
4. [Manifest에서 component 실행까지](learning-spine/04-manifest-to-component-execution.md)
5. [화면·프로세스·task·state의 독립 수명](learning-spine/05-independent-lifetimes-of-screen-process-task-and-state.md)
6. [Main thread·Binder·coroutine·durable work 수명](learning-spine/06-main-thread-binder-coroutine-and-durable-work-lifetime.md)
7. [입력·리소스 선택·display frame](learning-spine/07-input-resource-selection-and-display-frame.md)
8. [Data·storage·network·offline recovery](learning-spine/08-data-storage-network-and-offline-recovery.md)
9. [Identity·permission·독립 security gate](learning-spine/09-identity-permission-and-independent-security-gates.md)
10. [Device capability 발견과 background execution](learning-spine/10-device-capability-discovery-and-background-execution.md)
11. [관찰·테스트·품질 feedback](learning-spine/11-observation-testing-and-quality-feedback.md)
12. [Compatibility·update·form factor](learning-spine/12-compatibility-update-and-form-factor.md)

### Maps

- [Android System Map](overview/android-system-map.md) - Android stack 과 문제 boundary.
- [Android Release History](history/android-release-history.md) - version/API/behavior-change timeline.
- [Android Glossary](../04_system_services/activity-manager-service.md) - 용어의 짧은 정의와 정본 링크.
- [Android Learning Path](learning/android-learning-path.md) - 학습 resource 선택과 순서.

### Canonical Areas

- [System Internals](../01_system_internals/android-system-internals-map.md)
- [App Framework](../02_app_framework/android-app-framework-map.md)
- [Compose Runtime and State](../02_app_framework/jetpack-compose/runtime/compose-runtime-and-state-model.md)
- [Packaging and Deployment](../03_packaging_deployment/android-packaging-deployment.md)
- [System Services](../04_system_services/android-system-services-and-device-capabilities.md)
- [Security and Privacy](../05_security_privacy/android-security-and-privacy.md)
- [Platforms and Form Factors](../07_platforms/android-platforms-and-form-factors.md)
- [Topic Synthesis Map](topics/0-android-topics-map.md) - 주제별로 원자 노트를 조합한 33 개 합성 문서 색인.

### 문제 분류

- 앱이 시작되지 않거나 예고 없이 사라진다: component/process 경계를 먼저 나누고 [System Internals](../01_system_internals/android-system-internals-map.md) 와 [App Framework](../02_app_framework/android-app-framework-map.md) 를 함께 본다.
- 권한을 받았는데 API 가 실패한다: manifest grant 만 보지 말고 [Security and Privacy](../05_security_privacy/android-security-and-privacy.md) 에서 AppOps, foreground 상태, OS 정책까지 분리한다.
- background 작업이 늦거나 사라진다: lifecycle callback 과 durable work 를 구분한 뒤 [System Services](../04_system_services/android-system-services-and-device-capabilities.md) 로 이동한다.
- 기기나 Android 버전에 따라 다르게 동작한다: [Android Release History](history/android-release-history.md) 와 [Platforms and Form Factors](../07_platforms/android-platforms-and-form-factors.md) 에서 version 조건과 form factor 조건을 따로 확인한다.

### 경계

이 폴더에는 여러 영역을 잇는 학습·분류 기준만 둔다. 특정 API 사용법, 구현 recipe, subsystem 내부 동작은 해당 canonical area 에 둔다.

### Runbooks and Worked Examples

- [04-permission-denial.md](diagnostic-runbooks/04-permission-denial.md)
- [07-jank-dropped-frames.md](diagnostic-runbooks/07-jank-dropped-frames.md)
- [08-install-update-failure.md](diagnostic-runbooks/08-install-update-failure.md)
- [02-photo-capture-preview-save-upload.md](worked-examples/02-photo-capture-preview-save-upload.md)
- [03-deep-link-to-correct-task-and-screen-state.md](worked-examples/03-deep-link-to-correct-task-and-screen-state.md)
- [06-permission-granted-but-api-fails.md](worked-examples/06-permission-granted-but-api-fails.md)
- [07-compose-jank-from-ui-state-to-surfaceflinger.md](worked-examples/07-compose-jank-from-ui-state-to-surfaceflinger.md)
- [08-signed-artifact-through-play-delivery-to-update.md](worked-examples/08-signed-artifact-through-play-delivery-to-update.md)
- [android-performance-quality-and-build-optimization.md](../06_testing_performance/performance/android-performance-quality-and-build-optimization.md)
