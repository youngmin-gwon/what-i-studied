---
title: component-communication-uses-intent-binder-uri-and-pendingintent-by-boundary
tags: [android, android/app-components, android/architecture]
aliases: ["컴포넌트 통신은 경계에 따라 Intent, Binder, URI, PendingIntent를 사용한다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## 컴포넌트 통신은 경계에 따라 Intent, Binder, URI, PendingIntent를 사용한다

안드로이드 앱 컴포넌트 간 통신은 대상 컴포넌트의 유효 범위와 프로세스 경계(Process Boundary)에 따라 적절한 IPC 수단(**Intent, Binder, Content URI, PendingIntent**)을 선택하는 아키텍처 계약을 갖는다.

---

### 1. 통신 수단별 사용 사양 (What)

1. **Intent**: 컴포넌트 간 메시지 전달 및 실행 요청 (Explicit / Implicit).
2. **Binder (AIDL/Messenger)**: 프로세스 간 복잡한 고성능 동기/비동기 API 메서드 호출.
3. **Content URI**: `ContentProvider` 및 `FileProvider` 를 통한 보안 규격 데이터/파일 공유.
4. **PendingIntent**: 타 프로세스(NotificationManager, AppWidgetHost)에 내 앱의 컴포넌트 실행 권한을 위임 포장하여 전달.

---

### 2. 관련 문서 및 참조

- 상위 문서: [App Component Contracts](./app-component-contracts.md)
- 공식 가이드: [Intents and Intent Filters](https://developer.android.com/guide/components/intents-filters)

검증일: 2026-08-05. 통신 수단 매핑 확인 완료.
