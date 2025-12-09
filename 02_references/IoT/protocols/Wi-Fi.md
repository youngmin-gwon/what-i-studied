---
title: Wi-Fi
tags: [high-bandwidth, iot, network]
aliases: []
date modified: 2025-12-09 18:03:32 +09:00
date created: 2025-12-09 11:59:13 +09:00
---

## 🌐 개요 (Overview)
**Wi-Fi (IEEE 802.11)** 는 고대역폭 무선 네트워킹을 위한 보편적인 표준입니다. 스마트홈에서는 허브, 카메라, 그리고 인터넷을 연결하는 중추 (Backbone) 역할을 합니다.

>[!WARNING]
>Wi-Fi 는 기술적으로 **물리 및 데이터 링크 계층** (Layer 1-2) 을 의미합니다.
>그러나 통상적으로 "Wi-Fi 장치"라고 할 때는 **TCP/IP** 와 애플리케이션 계층 (HTTP/MQTT/Matter) 을 포함한 Full Stack 구현을 의미합니다.

## 🏗️ 프로토콜 스택 (Stack)

Wi-Fi 장치는 PC 와 유사하게 완전한 TCP/IP 스택을 실행합니다.

| 계층 (Layer)                | 기술 (Technology)     | 상세 내용 (Details)                                              |
| :------------------------ | :------------------ | :----------------------------------------------------------- |
| **Layer 7** (Application) | **다양함 (Various)**   | 독점 프로토콜 (HTTP/Cloud), **[Matter](Matter.md)**, CoAP, MQTT 등. |
| **Layer 4** (Transport)   | **TCP / UDP**       | [Zigbee](Zigbee.md)/[Thread](Thread.md) 에 비해 오버헤드가 큽니다.      |
| **Layer 3** (Network)     | **IPv4 / IPv6**     | LAN 내에서 주소 지정이 가능합니다.                                        |
| **Layer 2** (MAC)         | **IEEE 802.11 MAC** | 매체 접근 제어, CSMA/CA 를 처리합니다.                                   |
| **Layer 1** (PHY)         | **IEEE 802.11 PHY** | **2.4 GHz / 5 GHz / 6 GHz**. OFDM 변조를 사용합니다.                 |

### 🛠️ IoT 에서의 주요 특징 (Key Components in IoT)
1. **높은 전력 소모 (High Power Consumption)**: 연결 유지 (비콘, Keep-alive) 를 위해 [Zigbee](Zigbee.md)/[Thread](Thread.md) 보다 훨씬 많은 에너지를 소모합니다. 코인 배터리 센서에는 부적합합니다.
2. **스타 토폴로지 (Star Topology)**: 전통적으로 포인트 - 대 - 허브 (라우터) 방식입니다. Wi-Fi Mesh 가 존재하지만, 개별 IoT 장치는 일반적으로 단일 액세스 포인트 (AP) 에 연결됩니다.
3. **대역폭 (Bandwidth)**: 데이터 처리량이 중요한 **비디오 도어벨**, **보안 카메라**, **음성 비서**를 위한 유일한 선택지입니다.

## 🔋 왜 전력을 많이 쓰는가? (Why High Power?)

Wi-Fi 가 센서 (코인 배터리) 에 부적합한 이유는 명확합니다. 설계 목적이 **"빠르고 멀리, 많이"** 보내는 것이기 때문입니다.

1. **높은 대역폭 (Bandwidth)**: 마치 트럭으로 짐을 실어 나르는 것과 같습니다. 많은 데이터를 처리하려면 칩셋이 더 많은 일을 해야 합니다.
2. **높은 송신 출력 (TX Power)**: 벽을 뚫고 멀리 있는 공유기까지 신호를 보내려면 "확성기로 소리치듯" 강하게 쏴야 합니다. (반면 [Zigbee](Zigbee.md) 는 옆 사람에게 속삭이듯 전달합니다.)
3. **상시 연결 (Always-on)**: IP 연결을 유지하기 위해 지속적으로 '살아있음 (Keep-alive)' 신호를 보내야 하므로 깊은 잠 (Sleep) 에 들기 어렵습니다.

## 🏠 스마트홈에서의 역할 (Smart Home Role)
- **백본 (Backbone)**: [Matter](Matter.md)/[Zigbee](Zigbee.md) 브리지를 인터넷에 연결하는 다리 역할을 합니다.
- **상시 전원 기기 (Mains Powered Devices)**: 스마트 플러그, 스크린, 가전제품 (냉장고/오븐) 등 전원 공급이 원활하고 칩 (ESP32 등) 가격이 저렴한 기기에 주로 사용됩니다.
- **Matter over Wi-Fi**: Matter 는 고대역폭 기기를 위해 Wi-Fi 를 사용하며, 이는 [Thread](Thread.md) 와 동일한 로컬 제어 이점을 제공하되 속도가 더 빠릅니다.
