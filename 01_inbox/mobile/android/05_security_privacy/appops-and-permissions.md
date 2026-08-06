---
title: appops-and-permissions
tags: [android, appops, permissions, security]
aliases: [Android Permission System, AppOps와 권한 시스템]
date modified: 2026-08-06 18:57:26 +09:00
date created: 2026-08-06 16:31:15 +09:00
---

## 안드로이드 권한 시스템 & AppOps (AppOps and Permissions)

### 1. 개요 및 비유로 이해하는 개념 (Overview & Definition)

안드로이드 운영체제는 앱이 사용자의 민감한 개인정보(위치, 연락처, 카메라 등)나 기기 하드웨어 자원(마이크, 센서 등)에 무단으로 접근하는 것을 막기 위해 **2 중 보안 검문소**를 운영합니다. 이 보안 체계의 두 축이 바로 **권한 시스템(Permission System)**과 **AppOps(Application Operations)**입니다.

#### 초보자를 위한 쉬운 비유

- **권한 시스템 (Permission System)**: **"건물 출입증(Keycard)"**과 같습니다. "이 앱이 카메라나 위치 정보 건물에 들어갈 수 있는 1 차 자격이 있는가?"를 검증합니다.
- **AppOps (Application Operations)**: **"실내 보안 경비원(Security Guard)"**과 같습니다. 출입증이 있더라도 "지금 백그라운드 상태인데 마이크를 쓰려 하는가?", "사용자가 카메라 사용 조용히 차단 모드를 켜두었는가?"를 실시간 관찰하며 미세하게 접근을 통제하거나 추적 기록(Audit)합니다.

---

### 2. 안드로이드 권한 시스템과 AppOps 의 핵심 구성 (Core Concepts)

#### 1) 안드로이드 권한 시스템 (Permission System)

권한 시스템은 앱 개발자가 `AndroidManifest.xml` 에 필요한 권한을 명시하고, OS 및 사용자가 승인했는지 확인하는 **1 차 접근 제어 관문**입니다.

- **설치 시점 권한 (Install-time Permissions)**: 앱 설치 시 자동 승인되는 권한 (일반 권한 `INTERNET`, 서명 권한 등).
- **런타임 권한 (Runtime Permissions / Dangerous Permissions)**: 위치(`ACCESS_FINE_LOCATION`), 카메라(`CAMERA`) 등 민감 자원으로, 앱 실행 중 사용자 팝업 대화상자를 통해 직접 동의를 얻어야 합니다.

#### 2) AppOps (Application Operations)

`AppOps` 는 세밀한 **런타임 접근 제어 및 오디팅(Auditing) 메커니즘**입니다.

- **사용 기록 추적 (Auditing)**: 카메라, 마이크, 위치 자원 접근 시 타임스탬프를 기록하고 상단바 녹색 표시등을 활성화합니다.
- **상황별 미세 제어 (Contextual Control)**: 백그라운드 접근 제한, 프라이버시 토글 상태에 따른 동작 제어를 담당합니다.

>런타임 권한과 AppOps 의 세부 동작 차이 및 상세 비교표는 [Runtime Permissions vs AppOps](runtime-permissions-vs-appops.md) 문서에서 확인할 수 있습니다.

---

### 3. 권한 및 AppOps 검증과 SecurityException 흐름 (Operation Flow)

앱이 적절한 권한 없이 보호된 시스템 API(예: 위치 조회, 카메라 열기)를 호출할 때 일어나는 내부 작동 과정입니다.

```mermaid
flowchart TD
    App[App Process] -->|"1. Protected API Call"| FrameworkAPI[Framework Client API]
    FrameworkAPI -->|"2. Binder IPC Request"| SystemServer[System Server Process]
    SystemServer -->|"3. Check Permission & AppOps"| AuthCheck{Permission & AppOps Granted?}
    AuthCheck -->|"Yes"| HardwareResource[Execute Hardware Resource / Return Data]
    AuthCheck -->|"No"| SecurityEx[Throw SecurityException via Binder]
    SecurityEx -->|"4. Uncaught Exception"| AppCrash[App Crash or Handled by Try-Catch]
```

#### 검증 및 발생 4 단계
1. **API 호출**: 앱이 `LocationManager.getLastKnownLocation()` 같은 보호된 함수를 호출합니다.
2. **Binder 통신 전달**: 요청이 [Binder IPC](../01_system_internals/binder-ipc.md)를 통해 [system-server](../04_system_services/system-server.md) 내부의 해당 서비스(예: `LocationManagerService`)로 전달됩니다.
3. **권한 검증 (`checkCallingPermission` & `noteOp`)**:
   - 시스템 서비스는 Binder 통신으로 넘어온 호출 앱의 UID 와 PID 를 확인합니다.
   - `Context.checkCallingPermission()` 및 `AppOpsManager.noteOp()` 을 실행해 권한과 AppOps 모드를 동시 검증합니다.
4. **SecurityException 반환 또는 Silent Ignore**: 권한이나 AppOps 상태가 거부되면 시스템 서비스는 `SecurityException` 을 던져 Binder 응답으로 앱 프로세스에 전달하거나, AppOps 모드에 따라 예외 없이 silent ignore(빈 데이터 반환) 처리합니다.

---

### 4. 초보자가 범하기 쉬운 안티패턴 및 주의사항 (Anti-Patterns & Pitfalls)

1. **런타임 권한만 체크하고 AppOps 의 Silent Ignore 상태를 간과하는 행위**:
   - 권한이 동의되어 있더라도 AppOps 가 `MODE_IGNORED` 상태이면 API 가 `SecurityException` 을 던지는 대신 빈 데이터나 null 을 반환합니다. 데이터가 비어 있을 때 앱이 튕기거나 무한 루프에 빠지지 않게 처리해야 합니다.
2. **`checkSelfPermission` 호출 없이 보호된 API 즉시 실행**:
   - 사용자가 런타임 권한을 거부했거나 설정에서 철회한 상태에서 API 를 호출하면 `SecurityException` 이 발생하여 앱이 비정상 종료됩니다.
3. **`AndroidManifest.xml` 권한 누락**:
   - 코드상에서 런타임 권한 팝업을 띄우더라도 매니페스트 파일에 `<uses-permission>` 이 선언되어 있지 않으면 OS 가 권한 요청 자체를 무시하고 즉시 거부 처리합니다.

---

### 5. 연결 문서 (Related Links)

- [Runtime Permissions vs AppOps](runtime-permissions-vs-appops.md) - 런타임 권한과 AppOps 의 역할 및 동작 차이 상세 비교
- [안드로이드 시스템 서비스 (system-server)](../04_system_services/system-server.md) - 권한 및 AppOps 검증을 수행하는 프레임워크 프로세스
- [Binder IPC](../01_system_internals/binder-ipc.md) - 앱 프로세스와 system-server 간 보안 검증 요청을 전달하는 IPC 메커니즘
