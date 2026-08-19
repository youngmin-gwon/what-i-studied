---
title: C3-system-service-lookup
tags: [android/system-services, android/binder, android/ipc]
aliases: [시스템 서비스 조회 패턴, System Service Lookup, 시스템 서비스 바인딩]
date created: 2026-08-04 16:00:00 +09:00
date modified: 2026-08-10 21:30:00 +09:00
---

## 시스템 서비스 조회 패턴

안드로이드의 다양한 기능은 `system_server` 프로세스에서 서비스 형태로 호스팅된다. 앱은 `getSystemService()`를 통해 이러한 서비스에 접근하며, 이때 백그라운드에서는 [binder ipc](../../01_system_internals/binder-ipc.md) 통신과 권한 확인 메커니즘이 동작한다. 이 문서는 서비스 조회와 IPC 권한 검사 구조를 설명한다.

### 이 주제를 읽기 전에
이 주제를 이해하기 위해 다음 선수 지식을 권장합니다.
- Binder IPC 및 안드로이드 프로세스 간 통신
- 안드로이드 권한 모델과 AppOps

### 전체 조망도

```mermaid
sequenceDiagram
    participant App as App Process
    participant ServiceManager as ServiceManager
    participant SystemServer as System Server (Binder)
    
    App->>App: getSystemService(Context.LOCATION_SERVICE)
    App->>ServiceManager: getService("location")
    ServiceManager-->>App: IBinder proxy
    App->>SystemServer: Binder IPC call
    SystemServer->>SystemServer: checkCallingUid() & AppOps check
    SystemServer-->>App: Return result
```

### getSystemService 및 권한 검사

#### getSystemService 메커니즘 및 ServiceManager
`getSystemService`는 시스템 서비스의 로컬 프록시(매니저 객체)를 캐싱하여 반환하며, 중앙 디렉터리인 [ServiceManager](../../04_system_services/service-manager.md)를 통해 바인더 프록시를 획득합니다. 실제 핵심 로직은 Binder를 통해 System Server로 전달됩니다.
- [ServiceManager 레퍼런스](../../04_system_services/service-manager.md) - 안드로이드 바인더 중앙 전화번호부 (Handle 0)
- [시스템 서비스 접근 공통 계약](../../04_system_services/service-lookup/service-lookup/service-lookup.md)
- [Context.getSystemService()](../../04_system_services/get-system-service.md)

#### 권한(UID/PID) 및 AppOps 검사
모든 Binder 호출은 시스템 서버 측에서 호출자의 UID와 PID를 확인하여 권한을 검사합니다. 특히 AppOps는 사용자가 권한을 부여한 이후라도 세밀하게 접근을 거부할 수 있는 통제 수단입니다.
- [System server checks caller UID and PID for every call](../../04_system_services/service-lookup/service-lookup/system-server-uid-pid-check.md)
- [AppOps can deny after permission is already granted](../../04_system_services/service-lookup/service-lookup/appops-permission-denial.md)

### 이 주제와 연결된 Worked Example
- [06-permission-granted-but-api-fails.md](../worked-examples/06-permission-granted-but-api-fails.md)

### 이 주제와 연결된 Diagnostic Runbook
- [04-permission-denial.md](../diagnostic-runbooks/04-permission-denial.md)

### 더 깊이 들어갈 때 (Learning Spine)
- [01-android-ecosystem-and-surfaces.md](../learning-spine/01-android-ecosystem-and-surfaces.md)
- [02-android-platform-execution-layers-and-call-paths.md](../learning-spine/02-android-platform-execution-layers-and-call-paths.md)
