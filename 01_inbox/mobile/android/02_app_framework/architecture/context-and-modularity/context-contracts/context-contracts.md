---
title: context-contracts
tags: [android, android/architecture, android/context]
aliases: ["Context 계약"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-04 18:00:00 +09:00
---

## Context 계약

`Context` 아키텍처 계약은 안드로이드 애플리케이션의 컴포넌트 수명, 의존성 경계, 시스템 리소스 접근 제어를 정립하는 가이드라인 세트다.

---

### 하위 계약 노드 목록

- [Context 기본 경계](./context-is-android-environment-capability-not-dependency-container.md): Context 의 본질이 DI 컨테이너가 아니라 OS 환경 접근 역량임을 명시한다.
- [Application Context 경계](./application-context-fits-process-lifetime-work-not-themed-ui.md): 프로세스 단위 수명에 맞는 작업과 UI 부적합성을 설명한다.
- [Activity Context 경계](./activity-context-carries-window-theme-and-short-lifetime.md): Window 및 Theme 을 소유하지만 수명이 짧은 Activity Context 의 특성을 기술한다.
- [컴포넌트 Context 경계](./component-context-lifetime-follows-service-receiver-provider-boundary.md): Service, Receiver, Provider 각 컴포넌트별 특수 Context 계약을 정리한다.
- [LocalContext 경계](./localcontext-is-composition-scoped-android-context-not-flutter-buildcontext.md): Compose UI 내 `LocalContext.current` 의 유효 범위와 주의사항을 밝힌다.
- [ViewModel/Repository Context 경계](./viewmodel-and-repository-should-not-retain-ui-context.md): Architecture Layer 에서 Context 보관 금지 원칙을 다룬다.
- [Context leak 경계](./context-leaks-happen-when-reference-outlives-component-lifetime.md): 참조 수명 불일치로 인한 메모리 누수의 원인과 모니터링 기법을 제시한다.

상위 문서: [Android Context Boundaries](../android-context-boundaries.md)
