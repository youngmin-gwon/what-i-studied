---
title: sensor-manager-synthetic-sensors
tags: ["android", "android/system-services"]
aliases: ["SensorManager는 raw 센서와 합성 센서를 같은 API로 노출한다"]
date modified: 2026-08-06 14:59:18 +09:00
date created: 2026-08-03 17:19:24 +09:00
---

## SensorManager는 raw 센서와 합성 센서를 같은 API로 노출한다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](../../android-system-services-and-device-capabilities.md)
관련 지도: [센서 접근 계약](./sensor.md)

### 핵심 정의

`SensorManager`(기기의 온보드 센서 목록을 열거하고 리스너를 관리하는 시스템 서비스)는 가속도계, 자이로스코프처럼 하드웨어가 직접 측정하는 **raw 센서**(하드웨어가 신호 노이즈와 함께 직접 측정한 원시 물리 데이터)와, 회전 벡터·중력·선형 가속도처럼 여러 raw 센서를 결합해 계산하는 **합성 센서**(synthetic/composite sensor: 복수의 raw 센서 신호를 센서 퓨전 알고리즘으로 결합해 차원 가공된 센서)를 동일한 `Sensor`/`SensorEventListener` API로 노출한다. 앱 코드에서는 둘을 구분하는 별도 인터페이스가 없고 `Sensor.getType()`으로만 구분된다.

### 메커니즘

raw 센서(`TYPE_ACCELEROMETER`, `TYPE_GYROSCOPE`, `TYPE_MAGNETIC_FIELD`)는 하드웨어 값을 그대로 전달하며 노이즈와 드리프트가 있다. 합성 센서(`TYPE_ROTATION_VECTOR`, `TYPE_GRAVITY`, `TYPE_LINEAR_ACCELERATION`, `TYPE_GAME_ROTATION_VECTOR`)는 센서 퓨전 알고리즘이 여러 raw 센서를 결합해 만든 값으로, 벤더 HAL 또는 플랫폼 센서 허브가 계산을 담당한다. 이 계산은 앱이 관여할 수 없는 블랙박스다.

### capability 확인과 리스너 수명

```kotlin
private val rotationSensor by lazy {
    sensorManager.getDefaultSensor(Sensor.TYPE_ROTATION_VECTOR)
}

override fun onResume() {
    super.onResume()
    val sensor = rotationSensor ?: return showNoRotationSensor()
    if (!sensorManager.registerListener(this, sensor, SensorManager.SENSOR_DELAY_GAME)) {
        showSensorRegistrationFailed()
    }
}

override fun onPause() {
    sensorManager.unregisterListener(this)
    super.onPause()
}
```

`getDefaultSensor()`의 null과 `registerListener()`의 false를 별개 실패로 기록한다. `SensorEvent.values`는 프레임워크가 재사용할 수 있으므로 비동기 처리로 넘길 때 복사하고, 요청 주기 상수는 보장 주파수가 아니라 힌트임을 전제로 timestamp를 사용한다.

### 판단 기준

- 방향, 회전, 기울기처럼 이미 잘 알려진 물리량이 필요하면 raw 센서를 직접 합성하지 말고 대응하는 합성 센서(`TYPE_ROTATION_VECTOR` 등)를 우선 사용한다. 벤더가 이미 캘리브레이션과 필터링을 적용했다.
- 자기장 간섭에 민감한 기능(나침반)은 `TYPE_ROTATION_VECTOR`보다 지자기 보정이 필요 없는 `TYPE_GAME_ROTATION_VECTOR`가 더 안정적일 수 있다는 점을 트레이드오프로 고려한다.
- 특정 센서 타입이 기기에 없을 수 있으므로 `getDefaultSensor()`가 null을 반환하는 경우를 항상 처리한다.

### 경계

- 이 노트는 raw/synthetic 구분까지만 다룬다. 배터리 절약을 위한 배칭 설정은 [센서 배칭은 수신 지연과 배터리 사이의 트레이드오프다](sensor-batching-latency.md)가 다룬다.
- 센서 퓨전 알고리즘의 내부 구현이나 벤더별 HAL 세부는 `01_system_internals/kernel-and-hal`이 다룬다.

### 관찰 가능한 신호

`adb shell dumpsys sensorservice`로 기기에 등록된 전체 센서 목록, 각 센서의 벤더/버전, 현재 활성 리스너 수를 확인할 수 있다.

### 공식 문서

- https://developer.android.com/develop/sensors-and-location/sensors/sensors_overview
- https://developer.android.com/develop/sensors-and-location/sensors/sensors_motion

검증일: 2026-08-06. 센서 부재, 등록 실패, event buffer 재사용, lifecycle 해제 흐름을 보강했다.
