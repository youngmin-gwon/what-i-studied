---
title: Thread
tags: [iot, network, protocol]
aliases: []
date modified: 2025-12-09 18:25:26 +09:00
date created: 2025-12-09 11:59:10 +09:00
---

## 🌐 개요 (Overview)
**Thread**는 IoT 기기를 위해 설계된 저전력 무선 메시 네트워킹 프로토콜입니다. IPv6 와 6LoWPAN 을 기반으로 합니다.

>[!WARNING]
>Thread 는 **Full Stack** 프로토콜이 **아닙니다**. 네트워킹 (Layers 1-4) 만 정의하며 애플리케이션 계층은 정의하지 *않습니다*.
>즉, 메시라는 "도로"는 깔아주지만, 그 위를 달릴 "자동차"(**[Matter](../matter/Matter.md)**나 HomeKit 같은 프로토콜) 가 필요합니다.
>👉 **[Matter Architecture](../matter/Matter%20Architecture.md)** 문서에서 Matter(언어) 와 Thread(도로) 의 관계를 자세히 확인하세요.

## 🏗️ 프로토콜 스택 (Protocol Stack)

Thread 는 신뢰성 높고 전력 소모가 적은 패킷 전달에 집중합니다.

| 계층 (Layer) | 기술 (Technology) | 상세 내용 (Details) |
| :--- | :--- | :--- |
| **Layer 7** (Application) | **없음 (None)** | Thread 자체는 애플리케이션을 정의하지 않음. 주로 **[Matter](../matter/Matter.md)**가 사용됨. |
| **Layer 4** (Transport) | **UDP** + 6LoWPAN | IPv6 패킷을 압축하여 전송. |
| **Layer 2-3** (Mac/Network) | **IEEE 802.15.4** | [Zigbee](../connectivity/Zigbee.md) 와 동일한 물리 계층(PHY)을 사용하지만, **IPv6** 라우팅을 수행합니다. |

### 🛠️ 주요 구성 요소 및 역할 (Roles)
> [!TIP] 자세한 역할 정의
> FTD, MTD, Leader 등 각 장치의 역할에 대한 상세 정의는 **[Thread Roles](Thread%20Roles.md)** 문서를 참고하세요.

1. **Border Router (보더 라우터, TBR)**: Thread 네트워크와 인터넷 ([Wi-Fi](../connectivity/Wi-Fi.md)/이더넷)을 연결하는 게이트웨이입니다. **[Thread Border Router](Border%20Router.md)** 문서를 참고하세요.
2. **Router**: 패킷을 중계하는 상시 전원 기기.
3. **End Device**: 배터리로 동작하는 말단 기기. (Deep Sleep 가능 - **SED**)

## 특징

**단일 장애 지점 없음 (No Single Point of Failure)**:- **자가 치유 (Self-Healing)**: 라우터 하나가 고장 나면 자동으로 다른 경로를 찾습니다.
- **안정성 (Reliability)**: 단일 실패 지점 (Single Point of Failure)이 없습니다 (Border Router 도 여러 대 설치 가능).
- **IP 기반**: **[Bluetooth](../connectivity/Bluetooth.md)**나 **[Zigbee](../connectivity/Zigbee.md)**와 달리, 인터넷과 직접 통신이 가능한 **End-to-End Connectivity**를 제공합니다.

## 🌉 Wi-Fi vs Thread vs Zigbee

| 구분 | [Wi-Fi](../connectivity/Wi-Fi.md) | [Thread](Thread.md) | [Zigbee](../connectivity/Zigbee.md) |
| :--- | :--- | :--- | :--- |
| **속도** | 매우 빠름 | 느림 (250kbps) | 느림 (250kbps) |
| **전력 소모** | 높음 | **매우 낮음** | **매우 낮음** |
| **구조** | 스타 토폴로지 (공유기 중심) | **메시 토폴로지** | 메시 토폴로지 |
| **애플리케이션** | HTTP, MQTT 등 다양 | 없음 (Data Agnostic) | ZCL (내장) |

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
