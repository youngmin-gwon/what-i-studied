---
title: service-is-background-or-remote-work-entry-point-not-general-task-runner
tags: [android, android/app-components, android/architecture]
aliases: ["Service는 백그라운드/원격 작업 진입점이다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Service는 백그라운드/원격 작업 진입점이다

**`Service` 는 화면 UI 없이 백그라운드에서 특정 작업을 실행하거나 외부 프로세스에 원격 API 를 제공하는 OS 컴포넌트 진입점이다. 일반적인 모든 비동기 작업(Async Task)을 실행하는 무분별한 런너가 아니다.**

---

### 1. 개념 및 현대 대체 표준 (What)

- **메인 스레드 구동 유의점**:
  `Service` 콜백(`onStartCommand`)은 기본적으로 앱의 **메인 UI 스레드**에서 실행된다. 서비스 내부에서 긴 계산이나 동기 IO 를 수행하려면 서비스 내부에서 코루틴 스코프를 통해 작업 스레드로 디스패치해야 한다.
- **현대 백그라운드 작업 대체**:
  단순 비동기 갱신이나 네트워크 다운로드는 Service 대신 **`WorkManager`** 를 주력 표준으로 사용한다.

---

### 2. 관련 문서 및 참조

- 상위 문서: [App Component Contracts](./app-component-contracts.md)
- 공식 가이드: [Services Overview](https://developer.android.com/guide/components/services)

검증일: 2026-08-05. Service 개념 및 WorkManager 대체 원칙 검증 완료.
