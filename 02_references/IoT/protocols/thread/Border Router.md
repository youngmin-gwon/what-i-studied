---
title: Border Router
tags: [bridge, iot, router, thread]
aliases: [Border Router, TBR]
date modified: 2025-12-10 16:29:14 +09:00
date created: 2025-12-09 18:43:18 +09:00
---

## 🌐 개요 (Overview)

**Thread Border Router (TBR)** 는 **[Thread](Thread.md)** 네트워크와 기존의 IP 네트워크 (**[Wi-Fi](../connectivity/Wi-Fi.md)** 또는 **[Ethernet](../connectivity/Ethernet.md)**) 를 연결하는 **게이트웨이** 장치입니다.
과거의 허브 (Hub) 가 프로토콜을 "번역"했다면, 보더 라우터는 단순히 패킷을 "전달 (Routing)"하는 역할을 합니다.

## 🏗️ 역할과 원리

### 1. IP 라우팅 (IP Routing) 및 6LoWPAN 적응

- **IP 라우팅**: 기본적으로 TBR은 패킷의 내용을 건드리지 않고 목적지 주소만 보고 전달합니다.
- **6LoWPAN 적응 (Adaptation Layer)**: 하지만 물리적으로는 "변환"이 일어납니다.
    - **Thread 내부**: 패킷은 **[6LoWPAN](../foundation/6LoWPAN.md)** 기술로 압축되고 조각나서 이동합니다.
    - **TBR의 역할**:
        - **Thread → Wi-Fi**: 압축된 6LoWPAN 패킷을 풀어서 온전한 표준 IPv6 패킷으로 복원(Decompression)하여 Wi-Fi로 보냅니다.
        - **Wi-Fi → Thread**: 큰 IPv6 패킷을 받아서 6LoWPAN으로 압축 및 단편화(Compression & Fragmentation)하여 Thread 망으로 보냅니다.
    - 즉, **내용(Payload)은 건드리지 않지만 패킷의 포장(Header/Framing)은 바꿉니다.**

### 2. 양방향 통신

- **Inbound**: 스마트폰 ([Wi-Fi](../connectivity/Wi-Fi.md)) 에서 보낸 명령을 [Thread](Thread.md) 전구로 전달.
- **Outbound**: [Thread](Thread.md) 센서가 클라우드나 로컬 서버로 상태 정보를 전달.

### 3. 중복성 (Redundancy)

- Zigbee 코디네이터는 네트워크에 단 하나만 존재해야 하지만, Border Router 는 **여러 대** 가 동시에 존재할 수 있습니다.
- 하나가 고장 나면 다른 TBR 이 즉시 역할을 이어받아 네트워크가 끊기지 않습니다.

## 🆚 허브와의 차이점

| 특징       | **기존 IoT 허브**(Zigbee/Z-Wave)                    | ** Thread Border Router**        |
| :------- | :---------------------------------------------- | :------------------------------- |
| **하는 일** | ** 통역 (Translating)**<br>(Zigbee 신호 ↔ IP 패킷 변환) | ** 라우팅 (Routing)**<br>(IP 패킷 전달) |
| **데이터**  | 허브가 내용을 이해하고 가공함                                | 내용은 보지 않고 주소만 보고 전달함             |
| **종속성**  | 특정 제조사 허브에 종속됨 (SmartThings, Hue)               | 제조사 상관없이 표준만 맞으면 호환됨             |

## 🛠️ 대표적인 기기

- **Apple**: HomePod mini, Apple TV 4K (2 세대 이상)
- **Google**: Nest Hub (2 세대), Nest WiFi Pro
- **Amazon**: Echo (4 세대)
- **Samsung**: SmartThings Hub (v3, Station), 일부 TV/냉장고

>[!TIP]
> **[Matter](../matter/Matter.md)** 환경에서는 어떤 제조사의 TBR 을 쓰든 상관없습니다. 모든 Thread 기기는 공통된 Thread 네트워크 (Credential 공유 시) 를 형성합니다.
