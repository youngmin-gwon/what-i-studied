---
title: Bluetooth
tags: [ble, iot, protocol]
aliases: []
date modified: 2025-12-09 17:54:32 +09:00
date created: 2025-12-09 11:59:22 +09:00
---

## 🌐 개요 (Overview)
**Bluetooth**, 특히 **Bluetooth Low Energy (BLE)** 는 헬스케어, 피트니스, 보안 및 홈 엔터테인먼트 산업의 새로운 애플리케이션을 위해 설계된 무선 개인 영역 네트워크 (WPAN) 기술입니다.

>[!NOTE]
>Bluetooth 는 **Full Stack** 프로토콜입니다. 물리적 라디오부터 애플리케이션 프로파일 (GATT) 까지 모든 것을 정의합니다.

## 🏗️ 프로토콜 스택 (Protocol Stack)

BLE 스택은 크게 컨트롤러 (Controller) 와 호스트 (Host) 로 나뉩니다.

| 계층 (Layer)                | 기술 (Technology)      | 상세 내용 (Details)                                                                                                                                             |
| :------------------------ | :------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Layer 7** (Application) | **GATT / GAP**       | **Generic Attribute Profile**: 서비스 (Services) 와 특성 (Characteristics, 데이터) 을 정의합니다.<br>**Generic Access Profile**: 스캔 (Scanning) 및 광고 (Advertising) 를 관리합니다. |
| **Layer 4-6** (Host)      | **L2CAP / ATT / SM** | **Attribute Protocol** (데이터 전송), **Security Manager** (페어링), **L2CAP** (멀티플렉싱).                                                                             |
| **Layer 2** (Link Layer)  | **Link Layer (LL)**  | 라디오 상태 관리 (Advertising, Scanning, Connected).                                                                                                               |
| **Layer 1** (PHY)         | **Bluetooth PHY**    | **2.4 GHz** 대역 (FHSS - 주파수 도약 확산 스펙트럼) 을 사용하여 간섭을 견딥니다.                                                                                                     |

### 🛠️ 주요 구성 요소 (Key Components)
1. **GATT (Generic Attribute Profile)**: BLE 장치가 데이터를 노출하는 방식입니다.
    - **Service (서비스)**: 데이터의 집합 (예: "심박수 서비스").
    - **Characteristic (특성)**: 실제 데이터 포인트 (예: " 심박수 측정값 ").
2. **Point-to-Point (점대점)**: 전통적으로 BLE 는 1:1 통신 (휴대폰 ↔ 트래커) 을 주로 사용했습니다.
3. **Bluetooth Mesh**: BLE 에 유효한 메시 네트워킹을 추가한 표준 (2017) 입니다. [Zigbee](Zigbee.md) 와 같은 라우팅 방식보다는 **Managed Flood**(모든 노드에 메시지 브로드캐스팅) 방식을 사용합니다.
4. **BLE 5.0+**: 이전 버전에 비해 전송 거리 (4x), 속도 (2x), 또는 브로드캐스팅 용량 (8x) 이 대폭 향상되어 스마트홈에서의 활용도가 높아졌습니다.

## 🏠 스마트홈에서의 역할 (Smart Home Role)
- **프로비저닝 (Provisioning)**: 가장 핵심적인 역할입니다. 스마트폰 (기본적으로 Bluetooth 내장) 을 사용하여 디스플레이가 없는 IoT 기기를 설정합니다 (예: 스마트 플러그에 [Wi-Fi](Wi-Fi.md) 비밀번호 전달).
- **센서 (Sensors)**: 저전력 센서 (온도, 근접 센서 등) 에 활용됩니다.
- **[Matter](Matter.md)**: Matter 는 초기 설정 (Commissioning) 단계에서만 **BLE**를 독점적으로 사용합니다. 설정이 완료되면 기기는 [Thread](Thread.md) 또는 [Wi-Fi](Wi-Fi.md) 로 전환하여 통신합니다.
