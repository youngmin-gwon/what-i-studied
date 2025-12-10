---
title: Zigbee
tags: [iot, legacy, protocol]
aliases: []
date modified: 2025-12-10 00:06:40 +09:00
date created: 2025-12-09 11:59:05 +09:00
---

## 🌐 개요 (Overview)
**Zigbee** 는 성숙하고 전력 소모가 적은 무선 메시 네트워킹 표준입니다.**[Thread](../thread/Thread.md)** 나**[Matter](../matter/Matter.md)** 와 달리, 라디오부터 애플리케이션 명령까지 전체 솔루션으로 작동합니다.

>[!NOTE]
>Zigbee 는 **Full Stack** 프로토콜 (1~7 계층) 입니다. 기본적으로 IP(Internet Protocol) 를 사용하지 *않습니다*.

## 🏗️ 프로토콜 스택 (Full Stack)

IP 를 사용하지 않으므로, Zigbee 기기는 라우터나 스마트폰과 직접 통신할 수 없습니다. Zigbee 신호를 네트워크 패킷으로 변환해 줄 **코디네이터 (Coordinator, Hub)** 가 필요합니다.

| 계층 (Layer)                | 기술 (Technology)                  | 상세 내용 (Details)                                                   |
| :------------------------ | :------------------------------- | :---------------------------------------------------------------- |
| **Layer 7**(Application) |** Zigbee Cluster Library (ZCL)** | 기기 기능 (예: On/Off, 색상 제어) 을 정의합니다. ZDO(Zigbee Device Object) 를 포함합니다. |
| **Layer 3-4**(Network)   |**[Zigbee NWK](Zigbee_Core/Zigbee%20NWK.md) / [APS](Zigbee_Core/Zigbee%20APS.md)** | 독점 메시 라우팅 (AODV/Tree 라우팅). 보안 (AES-128) 을 포함합니다.                    |
| **Layer 2**(MAC)         |**[IEEE 802.15.4 MAC](IEEE_802_15_4/IEEE%20802.15.4%20MAC.md)**|**[Thread](../thread/Thread.md)** 와 동일한 계층을 사용합니다.                 |
| **Layer 1**(PHY)         |**[IEEE 802.15.4 PHY](IEEE_802_15_4/IEEE%20802.15.4%20PHY.md)**|** 2.4 GHz** (전 세계 공통). 간혹 Sub-GHz 대역을 사용하기도 합니다 (드묾).              |

### 🛠️ 주요 구성 요소 (Key Components)
1. **Coordinator (코디네이터)**: 네트워크의 "두뇌"입니다. 네트워크당 단 *하나*만 존재합니다. 네트워크를 생성하고 보안 키를 저장합니다.
2. **Router (라우터)**: 상시 전원 기기 (전구, 플러그 등). 신호 범위를 확장 (Mesh) 합니다.
3. **End Device (엔드 디바이스)**: 배터리 구동 기기. 평소엔 슬립 모드에 있습니다.
4. **ZCL**(**[ZCL](../foundation/ZCL.md)**): Zigbee 기기의 표준 언어입니다. 현재**[Matter](../matter/Matter.md)** 의 데이터 모델은 이 ZCL 을 계승하여 만들어졌습니다. (성공적인 유산)

## 🔄 Zigbee to IP Bridging (MQTT)

### 🧩 Bridging Architecture

Zigbee 는 IP 를 모르기 때문에, IP 세상 (Home Assistant 등) 과 대화하려면 **통역사 (Bridge)** 가 필요합니다.

- **Zigbee2MQTT**: 가장 인기 있는 오픈소스 브리지입니다.
    - Zigbee 신호 (ZCL) ↔ **JSON** 변환 ↔**MQTT** 메시지.
    - 예: `Zigbee(On/Off)` → `Serial` → `Z2M` → `MQTT Publish("home/light/set", "ON")`.

## 🆚 Zigbee vs Z-Wave

| 특징 | **Zigbee**|**[Z-Wave](Z-Wave.md)** |
| :--- | :--- | :--- |
| **주파수**|** 2.4 GHz**(Wi-Fi 와 겹침) |** Sub-GHz** (벽 투과 좋음) |
| **개방성**|** 오픈 표준**(여러 칩셋) |** 독점 기술** (Silicon Labs) |
| **시장** | 글로벌, Matter 의 기반 | 북미 중심, 보안 시장 |
| **노드 수** | 이론상 65,000+ (실제 수백 대) | 최대 232 개 (Mesh 한계) |

## 🏠 스마트홈에서의 역할 (Smart Home Role)
- **안정성 (Stability)**: 대규모 메시 네트워크에서 검증된 성능을 자랑합니다 (Philips Hue 가 Zigbee 를 사용).
- **배터리 수명 (Battery Life)**: 소형 센서에 대해 매우 효율적입니다.
- **격리 (Isolation)**:**[Wi-Fi](Wi-Fi.md)** 와 분리된 자체 네트워크 ID (PAN ID) 로 운영되지만, 2.4GHz 대역을 공유하므로 간섭을 피하기 위한 채널 계획 (Channel Planning) 이 필요합니다.
