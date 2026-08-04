---
title: sensor-batching-trades-latency-for-battery
tags: ["android", "android/system-services"]
aliases: []
date modified: 2026-08-04 15:00:00 +09:00
date created: 2026-08-03 17:29:24 +09:00
---

## 센서 배칭은 수신 지연과 배터리 사이의 트레이드오프다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](01_inbox/mobile/android/04_system_services/android-system-services-and-device-capabilities.md)
관련 지도: [센서 접근 계약](01_inbox/mobile/android/04_system_services/device-capabilities/sensor-contracts/sensor-contracts.md)

### 핵심 정의

`registerListener()`의 `maxReportLatencyUs` 인자는 센서 이벤트를 즉시 AP(애플리케이션 프로세서)로 깨워 전달할지, 하드웨어 FIFO에 모아뒀다가 지정한 지연 시간 안에 배치로 전달할지를 결정한다. 0으로 설정하면 배칭 없이 즉시 전달되고, 값을 늘리면 AP를 덜 깨우는 대신 이벤트 수신이 그만큼 늦어진다.

### 메커니즘

센서 허브(별도 저전력 프로세서를 가진 기기의 경우) 또는 하드웨어 FIFO가 이벤트를 buffer에 쌓는다. AP는 FIFO가 가득 차거나 `maxReportLatencyUs`가 지났을 때만 깨어나 배치로 이벤트를 flush 받는다. `flush()`를 명시적으로 호출하면 배칭된 이벤트를 즉시 강제로 받아올 수 있다.

wakeup 센서(예: significant motion)는 AP가 절전 상태(suspend)여도 시스템을 깨울 수 있고, non-wakeup 센서는 AP가 이미 깨어있을 때만 이벤트를 전달한다. 두 카테고리는 `Sensor.isWakeUpSensor()`로 구분된다.

### 판단 기준

- 실시간성이 중요한 게임 컨트롤, 제스처 인식에는 배칭을 최소화(낮은 latency)한다.
- 만보기, 장시간 활동 추적처럼 지연이 문제되지 않는 기능은 큰 `maxReportLatencyUs`로 배칭해 배터리를 아낀다.
- 화면이 꺼진 상태에서도 이벤트가 필요하면 wakeup 센서를 사용해야 하며, non-wakeup 센서는 이 상태에서 이벤트가 유실되거나 지연될 수 있다.

### 경계

- 이 노트는 배칭/wakeup 설정까지만 다룬다. raw/synthetic 센서 선택 자체는 [SensorManager는 raw 센서와 합성 센서를 같은 API로 노출한다](01_inbox/mobile/android/04_system_services/device-capabilities/sensor-contracts/sensormanager-exposes-raw-and-synthetic-sensors-through-one-api.md)가 다룬다.
- Doze/App Standby가 백그라운드 센서 등록 자체를 제한하는 조건은 `04_system_services/background-and-notifications/background-work-contracts`가 다룬다.

### 관찰 가능한 신호

`adb shell dumpsys sensorservice`에서 센서별 FIFO 최대 이벤트 수와 현재 등록된 리스너의 실제 요청 latency를 확인할 수 있다. 배칭이 기대대로 동작하는지는 이벤트 수신 타임스탬프 간격으로 직접 확인한다.

### 공식 문서

- https://developer.android.com/develop/sensors-and-location/sensors/sensors_overview#sensors-battery
