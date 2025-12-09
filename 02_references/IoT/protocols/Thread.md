---
title: Thread
tags: [iot, network, protocol]
aliases: []
date modified: 2025-12-09 18:15:32 +09:00
date created: 2025-12-09 11:59:10 +09:00
---

## 🌐 개요 (Overview)
**Thread**는 IoT 기기를 위해 설계된 저전력 무선 메시 네트워킹 프로토콜입니다. IPv6 와 6LoWPAN 을 기반으로 합니다.

>[!WARNING]
>Thread 는 **Full Stack** 프로토콜이 **아닙니다**. 네트워킹 (Layers 1-4) 만 정의하며 애플리케이션 계층은 정의하지 *않습니다*.
>즉, 메시라는 "도로"는 깔아주지만, 그 위를 달릴 "자동차"(**[[Matter]]**나 HomeKit 같은 프로토콜) 가 필요합니다.

## 🏗️ 프로토콜 스택 (Protocol Stack)

Thread 는 신뢰성 높고 전력 소모가 적은 패킷 전달에 집중합니다.

| 계층 (Layer)                | 기술 (Technology)       | 상세 내용 (Details)                                                     |
| :------------------------ | :-------------------- | :------------------------------------------------------------------ |
| **Layer 7** (Application) | *(Thread 가 정의하지 않음)*  | 일반적으로 **[[Matter]]**, HomeKit, 혹은 Weave 를 사용합니다.                    |
| **Layer 4** (Transport)   | **UDP / DTLS**        | User Datagram Protocol 및 Datagram Transport Layer Security 를 사용합니다. |
| **Layer 3** (Network)     | **IPv6 / 6LoWPAN**    | IPv6 헤더를 압축하여 작은 프레임에 맞춥니다. 메시 라우팅을 지원합니다.                          |
| **Layer 2** (MAC)         | **IEEE 802.15.4 MAC** | [[Zigbee]] 와 동일합니다. CSMA/CA 로 충돌을 회피합니다.                            |
| **Layer 1** (PHY)         | **IEEE 802.15.4 PHY** | **2.4 GHz** 대역 (Zigbee 와 동일). 대역폭은 낮습니다 (~250 kbps).                |

### 🛠️ 주요 구성 요소 (Key Components)
1. **Thread Border Router (TBR)**: Thread 메시 네트워크를 표준 IP 네트워크 ([Wi-Fi](Wi-Fi.md)/이더넷) 와 연결합니다. Zigbee 코디네이터 (하나만 존재) 와 달리, 하나의 메시에 *여러 대*의 보더 라우터가 활성화되어 중복성 (Redundancy) 을 확보할 수 있습니다.
2. **Mesh Architecture (메시 아키텍처)**:
    - **Leader (리더)**: 네트워크 파라미터를 관리합니다. 동적 (Dynamic) 이어서 리더가 고장 나면 다른 라우터가 즉시 역할을 이어받습니다.
    - **Router (라우터)**: 패킷을 전달 (Forwarding) 합니다. 항상 전원이 공급되는 (Mains powered) 장치입니다.
    - **End Device (엔드 디바이스)**:
        - **FED (Full End Device)**: 항상 켜져 있지만 라우팅은 하지 않음.
        - **SED (Sleepy End Device)**: 배터리로 동작하며 대부분 슬립 모드에 있음.
3. **단일 장애 지점 없음 (No Single Point of Failure)**: 자가 치유 (Self-healing) 기능이 있어 전통적인 허브 중심 모델보다 우수합니다.

## 📡 주파수 및 물리적 특성 (vs. Bluetooth/Wi-Fi)

Thread 는 **2.4 GHz** 대역을 사용하지만, **Bluetooth**나 **Wi-Fi**와는 물리적 계층 (PHY) 이 다릅니다.

| 프로토콜       | 주파수 대역      | 채널              | 비고                                              |
| :--------- | :---------- | :-------------- | :---------------------------------------------- |
| **Thread** | 2.4 GHz     | 16 ch (5MHz 간격) | **IEEE 802.15.4** 사용. [Zigbee](Zigbee.md) 와 동일. |
| **BLE**    | 2.4 GHz     | 40 ch (2MHz 간격) | Bluetooth PHY 사용. 서로 호환 안 됨.                    |
| **Wi-Fi**  | 2.4 / 5 GHz | 다양함             | 높은 출력, 넓은 대역폭.                                  |

>[!NOTE] 커미셔닝 (Commissioning) 과 BLE
>[Matter](Matter.md) 기기 설정 시 Thread 기기도 **BLE**를 사용하여 스마트폰과 처음 연결하는 경우가 많습니다. 하지만 이는 **선택 사항**입니다.
>기기에 BLE 칩이 없다면, **보더 라우터**가 대신 중계하거나 QR 코드/NFC 를 통해 설정할 수 있습니다.

## 🏠 스마트홈에서의 역할 (Smart Home Role)
- **저전력 (Low Power)**: 수년간 지속되어야 하는 배터리 구동 센서 (동작 감지, 문 열림 센서 등) 에 적합합니다.
- **IP Native**: IPv6 를 사용하므로, Thread 기기는 메인 네트워크에서 (TBR 을 통해) 직접 주소를 가질 수 있어 앱과의 통합이 매끄럽습니다.
