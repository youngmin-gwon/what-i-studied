---
title: android-history-is-a-map-of-platform-contract-changes-not-a-feature-list
tags: ["android", "android/foundations"]
aliases: []
date modified: 2026-08-03 17:22:11 +09:00
date created: 2026-07-31 23:04:26 +09:00
---

## Android history 는 기능 목록이 아니라 platform contract 변화 지도다

Android version history 는 새 기능 암기표가 아니라 어떤 contract 가 바뀌었는지 보는 timeline 이다. runtime, permission, storage, distribution, update, UI, form factor, security boundary 가 언제 바뀌었는지가 중요하다.

예를 들어 Android 5.0의 Dalvik$\rightarrow$ART AOT 전환 및 SELinux Enforcing 전면 적용, Android 7.0의 JIT/AOT Hybrid 런타임 및 A/B Seamless Update, Android 8.0의 Treble (System/Vendor 분리) 및 background execution limit, Android 10의 Scoped Storage 및 Mainline APEX 모듈식 업데이트, Android 11의 Virtual A/B 스냅샷 업데이트, Android 13의 AIDL HAL 전면 전환 및 notification/media 권한 세분화는 플랫폼 전체의 계약 구조와 앱 개발·디버깅 기준을 근본적으로 바꿨다.

따라서 오래된 version 별 기능 나열은 정본으로 유지하지 않고, 주요 platform contract 전환점과 관련 정본 링크로 압축한다.

관련 노트: [permissions](../../../05_security_privacy/permissions-and-sandbox/permission-contracts/permission-contracts.md), [file/storage](../../../02_app_framework/data/storage/file-access-contracts/file-access-contracts.md), [platform modularity](../../../01_system_internals/platform-modularity/android-platform-modularity.md), [Compose runtime](../../../02_app_framework/jetpack-compose/runtime/compose-runtime-and-state-model.md).

### 판단 기준

release 를 기록할 때는 새 기능 수보다 기존 앱의 설계·테스트 기준을 바꾼 contract 가 무엇인지 먼저 적는다. 영향 받는 앱 조건을 설명할 수 없는 변화는 timeline 의 핵심 항목으로 올리지 않는다.

### 경계

이 노트는 변화의 선별 기준만 다룬다. 각 permission, storage, update, UI contract 의 현재 동작과 migration 절차는 연결된 정본 및 공식 behavior changes 문서가 소유한다.
