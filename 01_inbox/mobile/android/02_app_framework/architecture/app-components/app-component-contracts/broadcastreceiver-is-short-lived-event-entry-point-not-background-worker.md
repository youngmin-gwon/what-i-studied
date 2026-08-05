---
title: broadcastreceiver-is-short-lived-event-entry-point-not-background-worker
tags: [android, android/app-components, android/architecture]
aliases: ["BroadcastReceiver는 단명 이벤트 진입점이다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## BroadcastReceiver는 단명 이벤트 진입점이다

**`BroadcastReceiver` 는 시스템이나 외부 앱이 발송한 이벤트 메시지(Intent Broadcast)를 수신하는 순간에만 구동되는 극단적인 단명 진입점(Short-lived Event Entry Point)**이다. 백그라운드 장기 작업 수행용 컴포넌트가 아니다.

---

### 1. 개념 및 핵심 명제 (What)

- **짧은 타임아웃 예산 (ANR Risk)**:
  `onReceive()` 실행 시간은 시스템 지정 타임아웃(메인 스레드 기준 10초 미만)을 초과할 수 없으며, 시간 초과 시 ANR 이 발생한다.
- **WorkManager 비동기 위임**:
  이벤트 수신 후 복잡한 네트워크 조회나 DB 저장이 필요한 경우 `WorkManager` 작업으로 즉시 이관해야 한다.

---

### 2. 관련 문서 및 참조

- 상위 문서: [App Component Contracts](./app-component-contracts.md)
- 공식 문서: [Broadcasts Overview](https://developer.android.com/guide/components/broadcasts)

검증일: 2026-08-05. BroadcastReceiver 타임아웃 규칙 확인 완료.
