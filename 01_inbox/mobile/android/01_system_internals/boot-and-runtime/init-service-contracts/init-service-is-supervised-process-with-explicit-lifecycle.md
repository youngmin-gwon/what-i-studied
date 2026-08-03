---
title: init-service-is-supervised-process-with-explicit-lifecycle
tags: [android, android/boot-runtime, android/init, android/system-internals]
aliases: ["init service는 재시작 정책을 가진 supervised process다"]
date modified: 2026-08-03 17:23:42 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## init service 는 재시작 정책을 가진 supervised process 다

상위 문서: [init와 네이티브 서비스 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/init-service-contracts/init-service-contracts.md)

init service 는 `service <name> <pathname> …` 로 선언된 native process 이며, `init` 이 시작, 중지, 재시작, class 제어, socket 생성, crash handling 을 관리한다.

### 판단 기준

- long-running daemon 은 service 로 선언하고 init 의 재시작 정책에 맡긴다.
- `oneshot` 은 종료 후 자동 재시작하지 않을 작업에만 쓴다.
- `disabled` 서비스는 class start 로 자동 시작되지 않고 명시적 start 가 필요하다.
- `onrestart` 는 의존 서비스 정리와 재시작을 표현하지만, 순환 재시작을 만들 수 있으므로 조심한다.

### 관련 문서

- [service option은 identity, resource, class, socket 계약을 고정한다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/init-service-contracts/service-options-fix-identity-resource-class-and-socket-contracts.md)
- [property service는 전역 상태 저장소이자 제한된 제어 plane이다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/init-service-contracts/property-service-is-global-state-store-and-restricted-control-plane.md)

공식 문서: [Android Init Language](https://android.googlesource.com/platform/system/core/+/master/init/README.md)
