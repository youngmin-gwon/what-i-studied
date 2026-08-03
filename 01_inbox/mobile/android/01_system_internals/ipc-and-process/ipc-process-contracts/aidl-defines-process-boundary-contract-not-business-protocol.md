---
title: aidl-defines-process-boundary-contract-not-business-protocol
tags: [android, android/aidl, android/ipc]
aliases: [AIDL]
date modified: 2026-08-03 17:25:23 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## AIDL 은 process boundary 계약이지 비즈니스 프로토콜이 아니다

상위 문서: [IPC and process contracts](01_inbox/mobile/android/01_system_internals/ipc-and-process/ipc-process-contracts/ipc-process-contracts.md)

AIDL 은 client proxy 와 server stub 을 생성해 Binder transaction 형식을 맞춰주는 interface definition 이다. 이것은 process boundary 의 호출 모양을 고정하지만, 비즈니스 의미, retry, idempotency, authorization, version compatibility 를 자동으로 설계해주지는 않는다.

앱 내부 module 사이의 단순 추상화에 AIDL 을 도입하면 오히려 비용과 실패 모드가 커진다. AIDL 은 실제 process boundary 가 있고 그 경계를 안정적으로 유지해야 할 때 의미가 있다.

### 실무 규칙

- AIDL method 는 local function 처럼 보이더라도 실패, 지연, cancellation 을 원격 호출로 다룬다.
- stable AIDL 은 버전 호환성을 API 계약으로 관리해야 하는 경계에만 둔다.
- parcelable 은 전송 schema 이지 domain model 자체가 아니다.
- permission 과 caller identity 검사는 service 구현에서 명시적으로 둔다.

관련 노트: [Bound service는 프로세스 의존성과 IPC API를 노출한다](01_inbox/mobile/android/02_app_framework/architecture/app-components/app-component-contracts/bound-service-exposes-process-dependency-and-ipc-api.md)
