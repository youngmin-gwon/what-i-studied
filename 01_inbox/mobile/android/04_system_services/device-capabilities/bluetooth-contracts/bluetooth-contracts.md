---
title: bluetooth-contracts
tags: ["android", "android/system-services"]
aliases: ["Bluetooth 접근 계약"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-04 18:00:00 +09:00
---

## Bluetooth 접근 계약

이 지도는 Android 앱이 Bluetooth 기기와 통신할 때 마주치는 계약을 연결 모델 선택, Android 12+ 권한 재설계, GATT 연결 상태 관리, BLE 스캔의 배터리/백그라운드 제약으로 나눈다. **Bluetooth Classic**(RFCOMM 소켓 기반으로 오디오/대용량 직렬 데이터를 스트리밍 전송하는 모델)과 **BLE**(Bluetooth Low Energy GATT 기반으로 개별 속성을 읽고 쓰며 저전력 동작하는 모델)는 이름만 같은 별개의 연결 모델이며, 이 차이를 모르면 권한 설계와 연결 코드 모두 잘못된 모델을 기준으로 작성하게 된다.

### 읽는 순서

1. [Bluetooth Classic과 BLE(GATT)는 서로 다른 연결 모델이다](./bluetooth-classic-and-ble-gatt-are-different-connection-models.md)에서 두 연결 모델의 API 표면과 선택 기준을 먼저 본다.
2. [Android 12+ Bluetooth 런타임 권한은 조건부로만 위치 권한을 대체한다](./android-12-bluetooth-runtime-permissions-conditionally-replace-location-permission.md)에서 `BLUETOOTH_SCAN`/`BLUETOOTH_CONNECT`와 `ACCESS_FINE_LOCATION`의 관계를 확인한다.
3. [BluetoothGatt 콜백 기반 연결은 명시적 상태 머신이 필요하다](./bluetoothgatt-callback-connection-needs-an-explicit-state-machine.md)에서 비동기 콜백이 왜 상태 추적을 강제하는지 본다.
4. [BLE 백그라운드 스캔은 배터리 제약을 받으며 ScanFilter가 필요하다](./ble-background-scanning-is-battery-constrained-and-needs-scan-filters.md)에서 스캔 지속성과 배터리 사이의 트레이드오프를 본다.

### 문제 분류

| 증상 또는 질문 | 먼저 확인할 경계 |
| --- | --- |
| 오디오 스트리밍은 되는데 GATT 기기가 안 붙는다 | Classic 프로파일과 BLE GATT를 같은 API로 다루고 있는지 |
| `SecurityException`이 스캔/연결 시점에 발생 | targetSdk 31+ 에서 `BLUETOOTH_SCAN`/`BLUETOOTH_CONNECT`를 선언했는지, `neverForLocation` 조건을 잘못 판단했는지 |
| `connectGatt()` 호출은 성공했는데 이후 통신이 실패 | 콜백 기반 상태를 실제로 추적하지 않고 연결됐다고 가정했는지 |
| 화면을 끄면 BLE 스캔이 멈춘다 | 백그라운드 스캔에 `PendingIntent` 기반 API나 foreground service를 쓰고 있는지 |

### 책임 경계

- 이 지도는 앱이 Bluetooth 기기에 접근하는 연결/권한/상태 계약만 다룬다. `A2DP`, `HFP` 같은 특정 프로파일의 오디오 코덱 세부나 페어링 UI 흐름의 세부 구현은 다루지 않는다.
- Wi-Fi, 셀룰러, VPN 같은 IP 기반 connectivity는 `01_system_internals/connectivity`가 담당한다. Bluetooth는 IP 스택을 거치지 않는 별도 무선 기술이므로 이 지도가 별도로 다룬다.
- GATT 서비스/characteristic의 데이터 파싱이나 특정 벤더 프로토콜 해석은 이 지도의 범위가 아니다.

### 노트 목록

- [Bluetooth Classic과 BLE(GATT)는 서로 다른 연결 모델이다](./bluetooth-classic-and-ble-gatt-are-different-connection-models.md)
- [Android 12+ Bluetooth 런타임 권한은 조건부로만 위치 권한을 대체한다](./android-12-bluetooth-runtime-permissions-conditionally-replace-location-permission.md)
- [BluetoothGatt 콜백 기반 연결은 명시적 상태 머신이 필요하다](./bluetoothgatt-callback-connection-needs-an-explicit-state-machine.md)
- [BLE 백그라운드 스캔은 배터리 제약을 받으며 ScanFilter가 필요하다](./ble-background-scanning-is-battery-constrained-and-needs-scan-filters.md)

검증일: 2026-08-04. [Bluetooth overview](https://developer.android.com/develop/connectivity/bluetooth), [Bluetooth permissions](https://developer.android.com/develop/connectivity/bluetooth/bt-permissions), [Connect to a GATT server](https://developer.android.com/develop/connectivity/bluetooth/ble/connect-gatt-server), [Communicate with a BLE device in background](https://developer.android.com/develop/connectivity/bluetooth/ble/background)를 기준으로 확인했다.
