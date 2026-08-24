---
title: component-contracts
tags: [android, android/app-components, android/architecture]
aliases: ["App Component Contracts", "앱 컴포넌트 계약"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## 앱 컴포넌트 계약은 OS가 보는 진입점 경계를 설명한다

**`App Component Contracts`** 모음은 4대 앱 컴포넌트가 안드로이드 OS 와 맺는 실행 수명, 권한 내보내기(Exported), 프로세스 우선순위, 경계 간 통신 프로토콜 계약 정본 가이드라인이다.

---

### 하위 정본 계약 노드 목록

- [앱 컴포넌트는 OS entry point다](components-as-entry-points.md)
- [Activity는 사용자 진입점이자 프로세스 우선순위 신호다](activity-process-priority.md)
- [Activity lifecycle 콜백은 가시성과 상호작용 경계를 설명한다](activity-lifecycle-callbacks.md)
- [Configuration change는 Activity를 재생성하지만 모든 화면 상태를 잃지 않는다](configuration-change-handling.md)
- [Process death 복구는 saved state와 persistent source of truth를 필요로 한다](process-death-state-recovery.md)
- [Android task와 app back stack은 OS activity 내비게이션이다](task-and-back-stack.md)
- [Service는 백그라운드/원격 작업 진입점이다](service-execution-boundaries.md)
- [Bound Service는 프로세스 의존성과 IPC API를 노출한다](bound-service-ipc.md)
- [Foreground Service는 사용자에게 보이는 진행 중 작업 계약이다](foreground-service-policies.md)
- [BroadcastReceiver는 단명 이벤트 진입점이다](broadcast-receiver-lifecycle.md)
- [context-registered receiver 수명은 등록한 Context 경계를 따른다](context-registered-receivers.md)
- [ContentProvider는 URI 데이터와 권한 경계를 게시한다](content-provider-uri-permissions.md)
- [FileProvider는 파일 경로 공유 대신 좁은 URI 접근을 허용한다](file-provider-sharing.md)
- [Manifest는 컴포넌트, 권한, 기능, exported 경계를 선언한다](manifest-component-declarations.md)
- [Exported와 permission 경계는 외부 접근을 결정한다](exported-permission-boundaries.md)
- [컴포넌트 통신은 경계에 따라 Intent, Binder, URI, PendingIntent를 사용한다](component-communication-boundaries.md)

상위 문서: [Android App Components](android-app-components.md)
