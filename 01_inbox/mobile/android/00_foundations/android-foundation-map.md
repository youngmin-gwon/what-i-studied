---
title: "Android Foundation Map은 안드로이드 시스템의 전체적인 멘탈 모델을 제공하는 지도다"
tags: ["android", "android/foundations"]
---

# Android Foundation Map은 안드로이드 시스템의 전체적인 멘탈 모델을 제공하는 지도다

Android foundations는 세부 API 설명이 아니라 전체 Android 지식 지도를 제공하는 입구다. 먼저 플랫폼 계층을 잡고, 버전 축과 용어를 확인한 뒤, 실제 문제를 소유한 정본 영역으로 이동한다.

## 읽는 순서

1. [Android System Map](01_inbox/mobile/android/00_foundations/overview/android-system-map.md)에서 kernel부터 app까지 책임 계층을 구분한다.
2. [Android Learning Path](01_inbox/mobile/android/00_foundations/learning/android-learning-path.md)에서 자신의 배경과 프로젝트 질문에 맞는 경로를 고른다.
3. 버전 의존 동작이면 [Android Release History](01_inbox/mobile/android/00_foundations/history/android-release-history.md)에서 API level, target SDK, extension/minor SDK 축을 분리한다.
4. 낯선 약어는 [Android Glossary](01_inbox/mobile/android/00_foundations/glossary/android-glossary.md)에서 뜻만 확인하고 연결된 정본으로 이동한다.

## Maps

- [Android System Map](01_inbox/mobile/android/00_foundations/overview/android-system-map.md) - Android stack과 문제 boundary.
- [Android Release History](01_inbox/mobile/android/00_foundations/history/android-release-history.md) - version/API/behavior-change timeline.
- [Android Glossary](01_inbox/mobile/android/00_foundations/glossary/android-glossary.md) - 용어의 짧은 정의와 정본 링크.
- [Android Learning Path](01_inbox/mobile/android/00_foundations/learning/android-learning-path.md) - 학습 resource 선택과 순서.

## Canonical Areas

- [System Internals](01_inbox/mobile/android/01_system_internals/boot-and-runtime/android-boot-and-runtime.md)
- [App Architecture](01_inbox/mobile/android/02_app_framework/architecture/android-app-architecture.md)
- [Compose Runtime and State](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/compose-runtime-and-state-model.md)
- [Packaging and Deployment](01_inbox/mobile/android/03_packaging_deployment/android-packaging-deployment.md)
- [System Services](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/background-work-contracts.md)
- [Security and Privacy](01_inbox/mobile/android/05_security_privacy/security-practices/security-practice-contracts/android-security-practice-is-defense-in-depth-not-client-trust.md)
- [Testing and Debugging](01_inbox/mobile/android/06_testing_performance/debugging/debugging-contracts/debugging-contracts.md)
- [Platforms and Form Factors](01_inbox/mobile/android/07_platforms/android-platforms-and-form-factors.md)

## 문제 분류

- 앱이 시작되지 않거나 예고 없이 사라진다: component/process 경계를 먼저 나누고 [System Internals](01_inbox/mobile/android/01_system_internals/boot-and-runtime/android-boot-and-runtime.md)와 [App Architecture](01_inbox/mobile/android/02_app_framework/architecture/android-app-architecture.md)를 함께 본다.
- UI가 느리거나 frame이 끊긴다: [Compose Runtime and State](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/compose-runtime-and-state-model.md)에서 불필요한 작업을 찾고 [Testing and Debugging](01_inbox/mobile/android/06_testing_performance/debugging/debugging-contracts/debugging-contracts.md)에서 측정 도구를 고른다.
- 권한을 받았는데 API가 실패한다: manifest grant만 보지 말고 [Security and Privacy](01_inbox/mobile/android/05_security_privacy/security-practices/security-practice-contracts/android-security-practice-is-defense-in-depth-not-client-trust.md)에서 AppOps, foreground 상태, OS 정책까지 분리한다.
- background 작업이 늦거나 사라진다: lifecycle callback과 durable work를 구분한 뒤 [System Services](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/background-work-contracts.md)로 이동한다.
- 기기나 Android 버전에 따라 다르게 동작한다: [Android Release History](01_inbox/mobile/android/00_foundations/history/android-release-history.md)와 [Platforms and Form Factors](01_inbox/mobile/android/07_platforms/android-platforms-and-form-factors.md)에서 version 조건과 form factor 조건을 따로 확인한다.

## 경계

이 폴더에는 여러 영역을 잇는 학습·분류 기준만 둔다. 특정 API 사용법, 구현 recipe, subsystem 내부 동작은 해당 canonical area에 둔다.
