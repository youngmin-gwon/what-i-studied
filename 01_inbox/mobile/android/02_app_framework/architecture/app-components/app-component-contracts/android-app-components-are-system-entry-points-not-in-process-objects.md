---
title: android-app-components-are-system-entry-points-not-in-process-objects
tags: [android, android/app-components, android/architecture]
aliases: ["안드로이드 앱 컴포넌트는 OS가 호출하는 실행 경계다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## 안드로이드 앱 컴포넌트는 OS가 호출하는 실행 경계다

**안드로이드 컴포넌트는 애플리케이션 개발자가 일반 객체지향 프로그래밍처럼 직접 `new` 키워드로 인스턴스화하는 객체가 아니다. 안드로이드 OS(ActivityManagerService)가 샌드박스를 통과하여 프로세스 내부로 개입하는 시스템 진입점(System Entry Points)**이다.

---

### 1. 개념 및 핵심 명제 (What)

- **OS 주도 생명주기 관리**:
  컴포넌트의 생성, 실행, 파기는 완전히 안드로이드 시스템 프레임워크가 바인딩 및 브로드캐스트로 제어한다.
- **IPC 및 Intent 기반 진입**:
  앱 내부 인스턴스 메서드 직접 호출이 불가능하며, `Intent`, `Binder`, `ContentResolver` 와 같은 OS IPC 매커니즘을 통해서만 진입점이 실행된다.

---

### 2. 관련 문서 및 참조

- 상위 문서: [App Component Contracts](./app-component-contracts.md)
- 공식 가이드: [App Fundamentals](https://developer.android.com/guide/components/fundamentals)

검증일: 2026-08-05. OS 인스턴스화 진입점 구조 검증 완료.
