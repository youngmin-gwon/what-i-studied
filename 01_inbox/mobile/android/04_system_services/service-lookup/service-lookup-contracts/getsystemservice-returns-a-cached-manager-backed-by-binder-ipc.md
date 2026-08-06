---
title: getsystemservice-returns-a-service-handle-whose-scope-and-transport-vary
tags: ["android", "android/system-services"]
aliases: []
date modified: 2026-08-06 14:48:27 +09:00
date created: 2026-08-03 17:17:12 +09:00
---

## getSystemService 는 서비스 핸들을 반환하며 범위와 통신 방식은 서비스마다 다르다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](../../android-system-services-and-device-capabilities.md)
배경 지식: [IPC 메커니즘](../../../../../operating-systems/ipc-mechanisms.md)

관련 지도: [시스템 서비스 접근 공통 계약](./service-lookup-contracts.md)

### 핵심 정의

`Context.getSystemService(String)` 또는 `getSystemService(Class)`는 `LocationManager`, `SensorManager`, `TelephonyManager` 같은 시스템 수준 서비스의 핸들을 반환한다. 반환 객체의 동일성, 캐시 범위, Context 의존성은 서비스별 구현 세부다. 공개 API는 모든 매니저가 프로세스 전역 singleton이라고 보장하지 않는다.

### 메커니즘

많은 매니저 메서드는 Binder 프록시를 통해 원격 시스템 서비스에 요청한다. 예를 들어 `LocationManager.getLastKnownLocation()`은 로컬에서 위치를 계산하지 않고 위치 서비스에 요청한다. 다만 모든 작업의 원격 구현이 `system_server`에 있는 것은 아니다. 카메라·오디오·센서처럼 별도 네이티브 서비스나 공유 메모리·소켓 채널을 거치는 API도 있고, 일부 메서드는 로컬 상태만 읽을 수 있다.

따라서 `getSystemService()`를 호출했다는 사실만으로 이후 모든 메서드가 Binder IPC이거나 매 호출이 원격이라고 단정하지 않는다. 해당 매니저의 스레딩·지연·콜백 계약을 API별로 확인한다.

### 판단 기준

- 매니저 인스턴스의 참조 동일성에 의존하지 않는다. 필요한 Context에서 서비스를 얻고, 특히 `WindowManager`와 `LayoutInflater`는 시각적 Context와 연결된 구성·화면 경계를 사용한다.
- 매니저 메서드 호출이 동기적으로 보여도 내부는 IPC 이므로 지연이 있을 수 있다. 반복 호출이나 폴링 루프를 main thread 에서 돌리지 않는다.

### 경계

- 이 노트는 "IPC 가 있다"는 사실까지만 다룬다. Binder 스레드 풀 크기, oneway 호출, death recipient 같은 메커니즘 세부는 `01_system_internals/ipc-and-process` 가 담당한다.
- 서비스가 실제로 요청을 승인할지는 [Binder 서비스는 필요한 호출 경계에서 호출자 신원과 정책을 검사한다](./system-server-checks-caller-uid-and-pid-for-every-call.md) 가 다룬다.

### 관찰 가능한 신호

`adb shell dumpsys <service_name>`(예: `dumpsys location`, `dumpsys sensorservice`)로 system_server 쪽 서비스 상태를 직접 관찰할 수 있다. 매니저 객체 자체는 로컬 프록시이므로 앱 로그만으로는 system_server 의 실제 상태를 알 수 없다.

### 공식 문서

- https://developer.android.com/reference/android/content/Context#getSystemService(java.lang.String)
- https://source.android.com/docs/core/architecture/ipc/binder-overview

검증일: 2026-08-06. `Context.getSystemService()`가 반환하는 객체의 시각적 Context 제약과 Binder 기반 서비스의 다양한 프로세스 배치를 공식 문서로 재확인했다.
