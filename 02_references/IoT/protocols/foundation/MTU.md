---
title: MTU
tags: [concept, network, performance, parameter]
aliases: [Maximum Transmission Unit, MTU]
---

## 📏 정의 (Definition)

**MTU** (Maximum Transmission Unit)는 네트워크 인터페이스가 한 번에 전송할 수 있는 **[패킷](IPv6.md)**(또는 프레임)의 **최대 크기(Byte)**를 의미합니다.

- 쉽게 말해 **"트럭 한 대에 실을 수 있는 최대 화물의 양"**입니다.
- 이 크기를 초과하는 데이터는 여러 개의 패킷으로 **쪼개져서(Fragmentation)** 전송되어야 합니다.

## 📉 IoT에서의 중요성 (Why it matters)

IoT 환경, 특히 저전력 무선 네트워크에서는 MTU가 성능에 결정적인 영향을 미칩니다.

1.  **단편화 비용 (Fragmentation Cost)**
    - 데이터가 MTU보다 크면 쪼개서 보내야 합니다.
    - 패킷 하나라도 손실되면, 전체 데이터를 다시 조립할 수 없거나 재전송해야 하므로 효율이 급격히 떨어집니다.
2.  **오버헤드 (Overhead)**
    - MTU가 작으면 같은 데이터를 보낼 때 더 많은 패킷을 보내야 하고, 각 패킷마다 헤더(Header)가 붙으므로 배터리 소모가 늘어납니다.
3.  **지연 시간 (Latency)**
    - 쪼개진 패킷들이 모두 도착해서 조립될 때까지 기다려야 하므로 지연이 발생합니다.

## 🗂️ 프로토콜별 MTU 비교

| 프로토콜 | 일반적인 MTU 크기 | 특징 |
| :--- | :--- | :--- |
| **Ethernet** | 1,500 Bytes | 유선 네트워크의 표준. |
| **Wi-Fi** | 2,304 Bytes | 보통 Ethernet과 호환성을 위해 1,500으로 제한하여 사용. |
| **IPv6** | 최소 1,280 Bytes | IPv6 표준을 따르려면 링크는 최소 1280 바이트를 지원해야 함. |
| **IEEE 802.15.4** | **127 Bytes** | Zigbee, Thread가 사용하는 저전력 표준. 매우 작음. |
| **BLE (v4.0)** | 23 Bytes | 기본 ATT MTU. (헤더 3B + 데이터 20B) |
| **BLE (v4.2+)** | **Up to 247+ Bytes** | DLE(Data Length Extension)로 확장 가능. |

---

## 🔍 주요 사례 (Use Cases)

### 1. 6LoWPAN (IPv6 over 802.15.4)

가장 극적인 MTU 차이를 해결하는 사례입니다.

- **문제**: **[IPv6](IPv6.md)**는 최소 **1280 바이트**를 요구하지만, 하위 물리 계층인 **[IEEE 802.15.4](../connectivity/IEEE_802_15_4/IEEE%20802.15.4.md)**는 **127 바이트**밖에 못 보냅니다.
- **해결**: **[6LoWPAN](6LoWPAN.md)** 계층이 중간에서 "코끼리를 냉장고에 넣는 작업"을 수행합니다.
    - **Header Compression**: 헤더를 압축해서 공간을 확보.
    - **Fragmentation**: 1280 바이트 패킷을 여러 개의 127 바이트 프레임으로 쪼개서 전송하고 수신 측에서 재조립.

### 2. Bluetooth (BLE)

BLE 개발에서 MTU는 데이터 전송 속도(Throughput)를 결정하는 핵심 파라미터입니다.

- **ATT MTU**: BLE 연결 시 두 기기가 협상(Exchange MTU Request/Response)하여 결정합니다.
- **기본값 (23 Bytes)**:
    - 초기 BLE는 한 번에 **20 바이트**의 데이터만 보낼 수 있었습니다. (3 바이트는 Opcode/Handle 헤더)
    - 펌웨어 업데이트(OTA) 같은 대용량 전송 시 매우 느립니다.
- **확장 (DLE, Data Length Extension)**:
    - Bluetooth 4.2부터 하드웨어 레벨의 패킷 길이도 늘어났고, MTU를 247 바이트 이상으로 늘려서 한 번에 많은 데이터를 보내 속도를 획기적으로 높일 수 있습니다.

### 3. Matter over Thread

- Matter 메시지는 IPv6 패킷에 담겨 전송됩니다.
- Thread 네트워크 안에서는 6LoWPAN을 통해 쪼개져서 이동하고, Border Router를 통해 Wi-Fi/Ethernet으로 나갈 때는 온전한 IPv6 패킷으로 복원되어 나갑니다.
