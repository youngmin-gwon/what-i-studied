---
title: service-lookup
tags: ["android", "android/system-services"]
aliases: []
date modified: 2026-08-10 16:07:30 +09:00
date created: 2026-08-03 17:16:58 +09:00
---

## 시스템 서비스 접근 공통 계약

이 지도는 location, sensors, telephony 같은 개별 시스템 서비스를 읽기 전에 알아야 하는 공통 기반을 다룬다. `Context.getSystemService()` 로 핸들을 얻는 단계, Binder 서비스가 필요한 경계에서 수행하는 신원·권한 검사, AppOps 의 실행 시점 정책을 구분한다.

### 주요 메커니즘 및 코드 예시 (Mechanisms & Code Examples)

- **getSystemService()**: Context 를 통해 싱글톤 형태로 관리되는 매니저 객체 반환. 내부적으로 `ServiceManager` 및 [binder ipc](../../../01_system_internals/binder-ipc.md) 활용.
- **Binder 검사**: 시스템 서버가 호출자의 `Binder.getCallingUid()`와 `Pid` 를 확인하여 권한 승인 검증.
- **AppOpsManager**: `checkOp` 혹은 `noteOp` 를 통해 런타임에 동적으로 앱의 권한 접근이 허용되어 있는지 확인.

```kotlin
// getSystemService 예시
val alarmManager = context.getSystemService(Context.ALARM_SERVICE) as AlarmManager
val appOpsManager = context.getSystemService(Context.APP_OPS_SERVICE) as AppOpsManager

// AppOps 상태 확인 예시
val mode = appOpsManager.unsafeCheckOpNoThrow(
    AppOpsManager.OPSTR_FINE_LOCATION,
    Process.myUid(),
    context.packageName
)
```

### 관찰 신호 (Observation Signals)

- `adb shell dumpsys activity services` 등을 통한 매니저 상태와 등록된 옵저버 로그 분석.
- SecurityException 발생 시 호출자의 UID 와 요청된 Permission/AppOps 로그.

### 읽는 순서

1. [Context.getSystemService()](../../get-system-service.md) 에서 공개 API 계약과 구현 세부를 분리한다.
2. [Binder 서비스는 필요한 호출 경계에서 호출자 신원과 정책을 검사한다](./system-server-uid-pid-check.md) 에서 permission 검사가 어디서 일어나는지 확인한다.
3. [AppOps는 permission 승인 뒤에도 실행 시점 정책을 추가로 거부할 수 있다](./appops-permission-denial.md) 에서 permission 통과와 실제 실행 허용이 다른 이유를 본다.

### 문제 분류

| 증상 | 먼저 확인할 경계 |
| --- | --- |
| `getSystemService` 가 null 을 반환 | Context 종류(Application/Activity/Service)와 서비스 존재 여부 |
| permission 은 granted 인데 API 가 조용히 실패하거나 빈 값 반환 | AppOps mode, 사용자 설정에서의 개별 취소, background 제한 |
| 서비스 호출이 오래 걸리거나 ANR | Binder 왕복이 main thread 를 막고 있는지 |
| 같은 API 가 기기마다 다르게 동작 | system_server 구현이 OEM 커스터마이징의 영향을 받는지 |

### 책임 경계

- 매니저 객체는 앱 쪽 핸들이지만 메서드마다 로컬 처리, Binder IPC, 공유 메모리/소켓 채널이 다를 수 있고 원격 서비스가 항상 system_server 에 있는 것도 아니다.
- permission 은 "이 기능을 요청할 자격이 있는가"를, AppOps 는 "지금 이 순간 실행을 허용하는가"를 각각 답한다. 이 지도의 개별 서비스 노트는 이 둘의 차이를 반복 설명하지 않고 여기로 링크한다.
- 이 노트는 Binder IPC 메커니즘 자체(marshalling, thread pool, death recipient)를 다루지 않는다. 그 내용은 `01_system_internals/ipc-and-process` 가 담당한다.

### 노트 목록

- [Context.getSystemService()](../../get-system-service.md)
- [Binder 서비스는 필요한 호출 경계에서 호출자 신원과 정책을 검사한다](./system-server-uid-pid-check.md)
- [AppOps는 permission 승인 뒤에도 실행 시점 정책을 추가로 거부할 수 있다](./appops-permission-denial.md)

검증일: 2026-08-06. `Context.getSystemService()`, Binder caller identity, AppOps 모델을 공식 API 및 Binder 문서와 재대조했다.
