---
title: service-lookup-contracts
tags: ["android", "android/system-services"]
aliases: []
date modified: 2026-08-03 17:35:15 +09:00
date created: 2026-08-03 17:16:58 +09:00
---

## 시스템 서비스 접근 공통 계약

이 지도는 location, sensors, telephony 같은 개별 시스템 서비스를 읽기 전에 알아야 하는 공통 기반을 다룬다. `Context.getSystemService()` 호출부터 system_server 의 권한 검사, AppOps 의 실행 시점 거부까지가 모든 개별 서비스가 공유하는 계약이다.

### 읽는 순서

1. [getSystemService는 캐시된 매니저를 반환하고 실제 작업은 Binder IPC로 위임한다](01_inbox/mobile/android/04_system_services/service-lookup/service-lookup-contracts/getsystemservice-returns-a-cached-manager-backed-by-binder-ipc.md) 에서 매니저 객체와 실제 서비스 프로세스를 분리한다.
2. [system_server의 서비스는 호출자 UID/PID로 권한을 검사한다](01_inbox/mobile/android/04_system_services/service-lookup/service-lookup-contracts/system-server-checks-caller-uid-and-pid-for-every-call.md) 에서 permission 검사가 어디서 일어나는지 확인한다.
3. [AppOps는 permission 승인 뒤에도 실행 시점 정책을 추가로 거부할 수 있다](01_inbox/mobile/android/04_system_services/service-lookup/service-lookup-contracts/appops-can-deny-after-permission-is-already-granted.md) 에서 permission 통과와 실제 실행 허용이 다른 이유를 본다.

### 문제 분류

| 증상 | 먼저 확인할 경계 |
| --- | --- |
| `getSystemService` 가 null 을 반환 | Context 종류(Application/Activity/Service)와 서비스 존재 여부 |
| permission 은 granted 인데 API 가 조용히 실패하거나 빈 값 반환 | AppOps mode, 사용자 설정에서의 개별 취소, background 제한 |
| 서비스 호출이 오래 걸리거나 ANR | Binder 왕복이 main thread 를 막고 있는지 |
| 같은 API 가 기기마다 다르게 동작 | system_server 구현이 OEM 커스터마이징의 영향을 받는지 |

### 책임 경계

- 매니저 객체(`LocationManager`, `TelephonyManager` 등)는 로컬 프록시일 뿐이며 실제 상태와 정책은 system_server 프로세스가 갖는다.
- permission 은 "이 기능을 요청할 자격이 있는가"를, AppOps 는 "지금 이 순간 실행을 허용하는가"를 각각 답한다. 이 지도의 개별 서비스 노트는 이 둘의 차이를 반복 설명하지 않고 여기로 링크한다.
- 이 노트는 Binder IPC 메커니즘 자체(marshalling, thread pool, death recipient)를 다루지 않는다. 그 내용은 `01_system_internals/ipc-and-process` 가 담당한다.

### 노트 목록

- [getSystemService는 캐시된 매니저를 반환하고 실제 작업은 Binder IPC로 위임한다](01_inbox/mobile/android/04_system_services/service-lookup/service-lookup-contracts/getsystemservice-returns-a-cached-manager-backed-by-binder-ipc.md)
- [system_server의 서비스는 호출자 UID/PID로 권한을 검사한다](01_inbox/mobile/android/04_system_services/service-lookup/service-lookup-contracts/system-server-checks-caller-uid-and-pid-for-every-call.md)
- [AppOps는 permission 승인 뒤에도 실행 시점 정책을 추가로 거부할 수 있다](01_inbox/mobile/android/04_system_services/service-lookup/service-lookup-contracts/appops-can-deny-after-permission-is-already-granted.md)

검증일: 2026-08-03. `Context.getSystemService()` 와 AppOps 모델은 [Android Context 문서](https://developer.android.com/reference/android/content/Context) 와 [AppOpsManager 문서](https://developer.android.com/reference/android/app/AppOpsManager) 를 기준으로 확인했다.
