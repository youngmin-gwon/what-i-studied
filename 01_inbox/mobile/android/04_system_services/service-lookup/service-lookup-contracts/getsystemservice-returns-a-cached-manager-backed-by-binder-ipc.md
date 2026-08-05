---
title: getsystemservice-returns-a-cached-manager-backed-by-binder-ipc
tags: ["android", "android/system-services"]
aliases: []
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-03 17:17:12 +09:00
---

## getSystemService 는 캐시된 매니저를 반환하고 실제 작업은 Binder IPC 로 위임한다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](../../android-system-services-and-device-capabilities.md)
배경 지식: [IPC 메커니즘](../../../../../operating-systems/ipc-mechanisms.md)

관련 지도: [시스템 서비스 접근 공통 계약](./service-lookup-contracts.md)

### 핵심 정의

`Context.getSystemService(String)` 또는 `getSystemService(Class)` 는 `LocationManager`, `SensorManager`, `TelephonyManager` 같은 매니저 객체를 반환한다. 이 매니저는 프로세스별로 캐시되며, 실제 기능은 매니저 내부가 아니라 system_server 프로세스에 있는 서비스 구현이 갖는다.

### 메커니즘

앱 프로세스에서 매니저의 메서드를 호출하면 매니저는 내부적으로 Binder 프록시를 통해 system_server 의 서비스 스텁을 호출한다. 예를 들어 `LocationManager.getLastKnownLocation()` 은 로컬에서 위치를 계산하지 않고 system_server 의 `LocationManagerService` 에 IPC 요청을 보낸다. 응답은 Binder 스레드 풀을 거쳐 앱 프로세스로 돌아온다.

일부 매니저(`SensorManager` 등)는 저지연 데이터를 위해 공유 메모리나 소켓 기반 채널을 추가로 사용하지만, 서비스 등록·해제·정책 확인은 여전히 Binder 호출을 거친다.

### 판단 기준

- 매니저 인스턴스가 앱마다, 심지어 Activity/Service/Application Context 마다 다를 수 있다는 점을 API 계약으로 가정하지 않는다. 대부분의 시스템 매니저는 프로세스 단위로 공유되지만 일부는 Context 종류에 따라 다르게 동작한다(예: `WindowManager` 는 Activity Context 와 Application Context 에서 다른 디스플레이 정보를 줄 수 있다).
- 매니저 메서드 호출이 동기적으로 보여도 내부는 IPC 이므로 지연이 있을 수 있다. 반복 호출이나 폴링 루프를 main thread 에서 돌리지 않는다.

### 경계

- 이 노트는 "IPC 가 있다"는 사실까지만 다룬다. Binder 스레드 풀 크기, oneway 호출, death recipient 같은 메커니즘 세부는 `01_system_internals/ipc-and-process` 가 담당한다.
- 서비스가 실제로 요청을 승인할지는 [system_server의 서비스는 호출자 UID/PID로 권한을 검사한다](./system-server-checks-caller-uid-and-pid-for-every-call.md) 가 다룬다.

### 관찰 가능한 신호

`adb shell dumpsys <service_name>`(예: `dumpsys location`, `dumpsys sensorservice`)로 system_server 쪽 서비스 상태를 직접 관찰할 수 있다. 매니저 객체 자체는 로컬 프록시이므로 앱 로그만으로는 system_server 의 실제 상태를 알 수 없다.

### 공식 문서

- https://developer.android.com/reference/android/content/Context#getSystemService(java.lang.String)