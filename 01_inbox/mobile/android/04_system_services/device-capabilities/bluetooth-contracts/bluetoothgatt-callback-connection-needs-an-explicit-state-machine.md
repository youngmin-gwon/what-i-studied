---
title: bluetoothgatt-callback-connection-needs-an-explicit-state-machine
tags: ["android", "android/system-services"]
aliases: ["BluetoothGatt 콜백 기반 연결은 명시적 상태 머신이 필요하다"]
date modified: 2026-08-04 18:00:00 +09:00
date created: 2026-08-04 18:00:00 +09:00
---

## BluetoothGatt 콜백 기반 연결은 명시적 상태 머신이 필요하다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](../../android-system-services-and-device-capabilities.md)
관련 지도: [Bluetooth 접근 계약](./bluetooth-contracts.md)

### 핵심 정의

`device.connectGatt()`는 연결이 완료되기 전에 즉시 `BluetoothGatt` 객체를 반환한다. 공식 문서가 설명하듯, 이 메서드는 연결 결과를 동기적으로 알려주지 않는다.

> "To connect to a GATT server on a BLE device, use the `connectGatt()` method. This method takes three parameters: a `Context` object, `autoConnect` ... and a reference to a `BluetoothGattCallback`"
>
> "The `onConnectionStateChange()` function is triggered when the connection to the device's GATT server changes."

즉 `BluetoothGatt` 객체가 non-null이라는 것은 "연결을 시도할 수단을 얻었다"는 뜻이지 "연결됐다"는 뜻이 아니다. 실제 연결 여부는 `onConnectionStateChange()` 콜백이 비동기로 알려주기 전까지 알 수 없다. 이 비동기성 때문에 앱은 자체 상태 변수로 현재 연결 단계를 명시적으로 추적해야 한다 — 그러지 않으면 `discoverServices()`나 `writeCharacteristic()`을 아직 연결되지 않은 `BluetoothGatt`에 호출해 조용히 실패하거나 예외를 유발한다.

### 메커니즘

`BluetoothProfile`은 네 가지 연결 상태 상수를 정의한다: `STATE_DISCONNECTED`(0), `STATE_CONNECTING`(1), `STATE_CONNECTED`(2), `STATE_DISCONNECTING`(3). `onConnectionStateChange(gatt, status, newState)`가 이 상태 전이를 전달한다. `STATE_CONNECTED`를 받은 뒤에야 `discoverServices()`를 호출할 수 있고, `discoverServices()`의 결과는 다시 `onServicesDiscovered()` 콜백으로 비동기 전달된다.

GATT 연결은 한 번에 하나의 미해결(outstanding) 요청만 처리한다. 예를 들어 `writeCharacteristic()` 호출 결과를 `onCharacteristicWrite()` 콜백으로 받기 전에 다음 `readCharacteristic()`을 호출하면 두 번째 요청이 무시되거나 실패한다. 따라서 앱은 연결 상태뿐 아니라 "현재 어떤 GATT 오퍼레이션이 진행 중인가"까지 큐로 관리해야 하는 경우가 많다. 이것이 GATT 연결에 명시적 상태 머신이 필요한 이유다 — 콜백 기반 API 자체는 상태를 대신 관리해 주지 않는다.

### 코드 예시

```kotlin
sealed class GattConnectionState {
    object Disconnected : GattConnectionState()
    object Connecting : GattConnectionState()
    object Connected : GattConnectionState()
    object ServicesDiscovered : GattConnectionState()
}

class GattStateHolder {
    var state: GattConnectionState = GattConnectionState.Disconnected
        private set

    private var bluetoothGatt: BluetoothGatt? = null

    private val callback = object : BluetoothGattCallback() {
        override fun onConnectionStateChange(gatt: BluetoothGatt, status: Int, newState: Int) {
            when (newState) {
                BluetoothProfile.STATE_CONNECTED -> {
                    state = GattConnectionState.Connected
                    // STATE_CONNECTED를 받은 뒤에만 서비스 탐색을 시작한다.
                    gatt.discoverServices()
                }
                BluetoothProfile.STATE_DISCONNECTED -> {
                    state = GattConnectionState.Disconnected
                    gatt.close() // 리소스 누수 방지를 위해 반드시 호출한다.
                    bluetoothGatt = null
                }
            }
        }

        override fun onServicesDiscovered(gatt: BluetoothGatt, status: Int) {
            if (status == BluetoothGatt.GATT_SUCCESS) {
                state = GattConnectionState.ServicesDiscovered
            }
        }
    }

    fun connect(context: Context, device: BluetoothDevice) {
        state = GattConnectionState.Connecting
        bluetoothGatt = device.connectGatt(context, false, callback)
    }
}
```

### 다이어그램

```
STATE_DISCONNECTED (0)
     │ connectGatt()
     ▼
STATE_CONNECTING (1)
     │ onConnectionStateChange(newState = STATE_CONNECTED)
     ▼
STATE_CONNECTED (2) ──discoverServices()──▶ onServicesDiscovered()
     │
     │ disconnect() 또는 원격 기기 연결 끊김
     ▼
STATE_DISCONNECTING (3)
     │ onConnectionStateChange(newState = STATE_DISCONNECTED)
     ▼
STATE_DISCONNECTED (0) ──gatt.close() 필수──▶ 리소스 해제
```

### 판단 기준

- 원격 기기가 항상 켜져 있지 않고 다시 나타날 때 자동으로 붙어야 한다면 `connectGatt(context, autoConnect = true, callback)`을 쓴다. 즉시 연결이 필요하고 실패를 빠르게 알아야 한다면 `autoConnect = false`로 직접 연결한다.
- `STATE_CONNECTED` 콜백을 받기 전에는 어떤 GATT 오퍼레이션도 호출하지 않는다. 상태 머신이 `Connected` 이상일 때만 요청 큐를 진행시킨다.
- 사용을 마친 `BluetoothGatt`는 반드시 `close()`를 호출한다. 공식 문서가 강조하듯, 연결을 정리하지 않으면 리소스가 누수된다.

> "One important step when dealing with Bluetooth connections is to close the connection when you are finished with it. To do this, call the `close()` function on the `BluetoothGatt` object."

### 경계

- 이 노트는 연결 상태 관리까지만 다룬다. 연결에 필요한 런타임 권한 조건은 [Android 12+ Bluetooth 런타임 권한은 조건부로만 위치 권한을 대체한다](./android-12-bluetooth-runtime-permissions-conditionally-replace-location-permission.md)가 다룬다.
- 연결 대상 기기를 찾는 스캔 단계는 [BLE 백그라운드 스캔은 배터리 제약을 받으며 ScanFilter가 필요하다](./ble-background-scanning-is-battery-constrained-and-needs-scan-filters.md)가 다룬다.
- 특정 characteristic의 데이터 인코딩/디코딩은 앱/기기 벤더의 프로토콜 문제이며 이 노트가 다루지 않는다.

### 관찰 가능한 신호

`onConnectionStateChange`나 `onServicesDiscovered`의 `status` 파라미터가 `BluetoothGatt.GATT_SUCCESS`(0)가 아니면 오퍼레이션이 실패한 것이다. `logcat`에서 GATT 관련 태그(`BluetoothGatt`)를 필터링하면 연결 시도, 상태 전이, 실패 코드를 시간순으로 확인할 수 있다. `close()`를 누락하면 이후 새 연결 시도가 실패하거나 이전 콜백이 계속 발화하는 것으로 리소스 누수를 관찰할 수 있다.

### 공식 문서

- [Connect to a GATT server](https://developer.android.com/develop/connectivity/bluetooth/ble/connect-gatt-server)
- [BluetoothProfile](https://developer.android.com/reference/android/bluetooth/BluetoothProfile)

검증일: 2026-08-04.
