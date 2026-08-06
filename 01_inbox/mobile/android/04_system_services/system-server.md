---
title: system-server
tags: [android, framework, system-server, system-services]
aliases: []
date modified: 2026-08-06 16:44:28 +09:00
date created: 2026-08-06 16:31:19 +09:00
---

## 안드로이드 system_server 프로세스 & 핵심 시스템 서비스

안드로이드 OS 가 부팅을 마치고 앱이 정상적으로 작동하기 위해 필요한 모든 핵심 시스템 서비스는 단 하나의 핵심 자바 프로세스인 **`system_server`** 내부에서 실행되고 관리됩니다.

---

### 1. `system_server` 프로세스란?

`system_server` 는 안드로이드 시스템의 **핵심 백본 프로세스**입니다.

- **생성 과정**: 리눅스 커널 부팅 후 `init` 프로세스가 Zygote 프로세스를 실행하고, Zygote 가 포크(fork)되어 `system_server` 프로세스를 생성합니다.
- **역할**: 안드로이드 프레임워크를 구성하는 수십 개의 자바 기반 시스템 서비스(System Services)들을 초기화하고, 이들을 **ServiceManager**에 등록한 뒤, Binder IPC 요청을 처리하는 이벤트 루프를 실행합니다.

---

### 2. 핵심 시스템 서비스 (Core System Services)

`system_server` 프로세스 내에서는 수많은 서비스가 스레드 또는 개별 객체 형태로 동작합니다. 대표적인 핵심 3 대 서비스는 다음과 같습니다.

#### 2.1 ActivityManagerService (AMS) / ActivityTaskManagerService (ATMS)

- **역할**: 앱 컴포넌트(Activity, Service, BroadcastReceiver, ContentProvider)의 생명주기(Lifecycle) 및 프로세스 생성을 관리합니다.
- **주요 기능**:
  - 새로운 앱 프로세스 포크 요청 (Zygote 통신)
  - 태스크(Task) 및 백스택(BackStack) 관리
  - 메모리 부족 시 중요도가 낮은 앱 프로세스 수거 (OOM Killer 연동)

#### 2.2 WindowManagerService (WMS)

- **역할**: 화면에 그려지는 모든 창(Window)의 레이아웃, Z-order(겹침 순서), 애니메이션, 입력 이벤트 전달을 관리합니다.
- **주요 기능**:
  - 각 앱이 그리는 서피스(Surface)의 위치와 크기 결정
  - 화면 회전, 다중 창(Multi-Window) 처리
  - 터치/키보드 입력 이벤트를 올바른 윈도우로 디스패치

#### 2.3 PackageManagerService (PMS)

- **역할**: 기기에 설치된 모든 앱(.apk)의 정보를 파싱하고 관리합니다.
- **주요 기능**:
  - APK 설치, 업데이트, 삭제 및 파싱
  - 앱 권한(Permissions) 정보 관리 및 검증
  - Explicit / Implicit Intent 에 반응하는 컴포넌트 해소(Intent Resolution)

---

### 3. Binder IPC 디스패치 (Binder IPC Dispatch)

안드로이드에서 일반 애플리케이션 프로세스와 `system_server` 프로세스는 서로 다른 메모리 공간을 사용합니다. 따라서 앱이 시스템 서비스의 기능을 이용하려면 **Binder IPC(Inter-Process Communication)** 를 통과해야 합니다.

```
[ 일반 앱 프로세스 ]
       │
   AIDL Proxy 호출 (예: context.getSystemService())
       │
   [ /dev/binder 커널 드라이버 ]
       │
   Binder Thread Pool 디스패치
       │
[ system_server 프로세스 (AMS, WMS, PMS 등) ]
```

1. **서비스 조회**: 앱은 `ServiceManager.getService("activity")` 등을 통해 시스템 서비스의 Binder 핸들(Proxy)을 획득합니다.
2. **IPC 호출**: 앱이 시스템 메서드를 호출하면 마샬링(Data Serialization)되어 `/dev/binder` 드라이버를 통해 `system_server` 로 전달됩니다.
3. **스레드 풀 디스패치**: `system_server` 내부의 **Binder Thread Pool**이 수신된 IPC 메시지를 언마샬링하고, 해당 시스템 서비스 객체의 `onTransact()` 메서드로 디스패치하여 요청을 수행합니다.
4. **결과 반환**: 작업 수행 결과를 다시 Binder 커널 드라이버를 거쳐 앱 프로세스로 전달합니다.

---

### 4. 연관 문서 및 참고

- [Binder IPC 레퍼런스](../01_system_internals/binder-ipc.md) - 앱과 system_server 통신 IPC 통로
- [Zygote 레퍼런스](../01_system_internals/zygote.md) - system_server 가 포크 요청을 보내는 마스터 프로세스
- [ART Runtime 레퍼런스](../01_system_internals/art.md) - system_server 가 구동되는 자바 런타임 환경
- [HAL 레퍼런스](../01_system_internals/hal.md) - system_server 가 하드웨어를 제어하는 추상화 계층
- [안드로이드 권한 시스템 & AppOps](../05_security_privacy/appops-and-permissions.md)
