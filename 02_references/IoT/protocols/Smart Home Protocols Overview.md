---
title: Smart Home Protocols Overview
tags: [index, iot, map, overview]
aliases: [IoT Protocols Map]
date modified: 2025-12-10 15:33:46 +09:00
date created: 2025-12-09 18:49:52 +09:00
---

## 🗺️ 스마트홈 프로토콜 지도 (Map)

이 폴더는 스마트홈을 구성하는 다양한 통신 규약들을 계층별로 정리하고 있습니다.

### 1. 📂 [Matter](matter/Matter.md) (The Language)

스마트홈의 **표준 언어** 입니다. 기기들이 서로 이해할 수 있는 "말"을 정의합니다.

- **[Matter](matter/Matter.md)**: 통합 표준 프로토콜.
- **[Matter Architecture](matter/Matter%20Architecture.md)**: Matter 가 어떻게 동작하는지 설명하는 개념도.
- **[Matter Roles](matter/Matter%20Roles.md)**: 기기들의 역할 (Controller, End Device 등).

### 2. 📂 [Thread](thread/Thread.md) (The Road)

저전력/배터리 기기를 위한 **전용 도로** 입니다.

- **[Thread](thread/Thread.md)**: IP 기반의 저전력 메시 네트워크.
- **[Thread Roles](thread/Thread%20Roles.md)**: FTD, MTD, Leader 등 역할 정의.
- **[Border Router](thread/Border%20Router.md)**: Thread(골목길) 와 Wi-Fi(고속도로) 를 이어주는 관문.

### 3. 📂 [Connectivity](connectivity/Wi-Fi.md) (Transports)

데이터가 지나가는 물리적인 **운송 수단** 들입니다.

- **[Wi-Fi](connectivity/Wi-Fi.md)**: 고속, 대용량, 상시 전원.
- **[IEEE 802.11](connectivity/IEEE_802_11/IEEE%20802.11.md)**: Wi-Fi 의 기술 표준 명세.
- **[Ethernet](connectivity/Ethernet.md)**: 유선, 백본, 최고의 안정성.
- **[Bluetooth](connectivity/Bluetooth.md)**: 초기 설정 (Commissioning) 및 1:1 연결.
- **[Zigbee](connectivity/Zigbee.md)**: Matter 이전의 메시 표준 (Legacy & Stable).
- **[IEEE 802.15.4](connectivity/IEEE_802_15_4/IEEE%20802.15.4.md)**: Zigbee/Thread 의 기반이 되는 저전력 무선 표준.
- **[Z-Wave](connectivity/Z-Wave.md)**: Sub-GHz 대역의 장거리/보안 특화 표준.

### 4. 📂 [Foundation](foundation/CoAP.md) (Core Tech)

프로토콜을 지탱하는 **기반 기술** 들입니다.

- **[CoAP](foundation/CoAP.md)**: IoT 를 위한 가벼운 HTTP (UDP 기반).
- **[IPv6](foundation/IPv6.md)**: 무한한 주소를 제공하는 차세대 인터넷 프로토콜.
- **[6LoWPAN](foundation/6LoWPAN.md)**: IPv6 패킷을 압축하여 저전력 무선으로 전송.
- **[ZCL](foundation/ZCL.md)**: Zigbee 와 Matter 의 데이터 모델 (DNA).
- **[MQTT](foundation/MQTT.md)**: 서버 중심의 메시징 프로토콜 (Pub/Sub).
- **[CSMA/CA](foundation/CSMA-CA.md)**: 무선 네트워크의 충돌 회피 알고리즘.
- **[OFDM](foundation/OFDM.md)**: 고속 데이터 전송을 위한 직교 주파수 분할 변조.
- **[TLV](foundation/TLV.md)**: 효율적인 바이너리 데이터 인코딩.
- **[mDNS](foundation/mDNS.md)**: 로컬 네트워크 기기 자동 발견 (ZeroConf).

---

## 🧩 핵심 개념 요약

>"Matter 는 **언어** 이고, Thread/Wi-Fi 는**도로** 이다."

1. **Application Layer (언어)**: 기기가 "무엇을 할지" 정의합니다.
   - 👉 **[Matter](matter/Matter.md)**, HomeKit, [ZCL](foundation/ZCL.md)
2. **Transport Layer (도로)**: 데이터를 "어떻게 나를지" 정의합니다.
   - 👉 **[Wi-Fi](connectivity/Wi-Fi.md)**,**[Thread](thread/Thread.md)**, [Bluetooth](connectivity/Bluetooth.md)

자세한 아키텍처 설명은 **[Matter Architecture](matter/Matter%20Architecture.md)** 문서를 참고하세요.
