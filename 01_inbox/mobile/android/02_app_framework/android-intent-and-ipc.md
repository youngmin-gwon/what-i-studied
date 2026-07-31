---
title: android-intent-and-ipc
tags: []
aliases: []
date modified: 2026-04-05 17:43:07 +09:00
date created: 2026-04-04 00:12:42 +09:00
---

## [[mobile-security]] > [[android-intent-and-ipc]]

### Android Intent & IPC: Messaging Framework

안드로이드 시스템의 핵심 통신 메커니즘인 **Intent**와 프로세스 간 통신(**IPC**)을 심층 분석합니다.

단순히 앱 컴포넌트를 실행하는 도구를 넘어, 시스템 전체의 데이터 흐름을 제어하고 보안 경계를 정의하는 중추적인 역할을 이해하는 것이 목표입니다.

---

---

## 원자 노트

- [[01-context-intent-vs-ios-통신-방식|💡 Context: Intent vs iOS 통신 방식]]
- [[02-intent-의-구성-요소|Intent 의 구성 요소]]
- [[03-explicit-vs-implicit-intent|Explicit vs Implicit Intent]]
- [[04-intent-filter|Intent Filter]]
- [[05-queries-태그-package-visibility-android-11|`<queries>` 태그 (Package Visibility, Android 11+)]]
- [[06-pendingintent|PendingIntent]]
- [[07-activity-result-api-modern|Activity Result API (Modern)]]
- [[08-앱-간-데이터-전달-보안|앱 간 데이터 전달 보안]]
- [[09-디버깅|디버깅]]
- [[10-더-보기|더 보기]]

---

## 정리 기준

이 노트는 원래 긴 가이드였고, H4 섹션을 별도 원자 노트로 분리했습니다.
기존 링크 호환을 위해 이 파일은 허브 노트로 유지합니다.
