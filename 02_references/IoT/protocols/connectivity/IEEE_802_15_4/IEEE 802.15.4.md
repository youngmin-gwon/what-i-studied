---
title: IEEE 802.15.4
tags: [iot, mac, phy, standard]
aliases: [LR-WPAN]
date modified: 2025-12-10 00:12:35 +09:00
date created: 2025-12-10 00:09:15 +09:00
---

## 🌐 개요 (Overview)

**IEEE 802.15.4** 는 저속, 저전력 무선 개인 영역 네트워크 (**LR-WPAN**: Low-Rate Wireless Personal Area Networks) 를 위한 기술 표준입니다.**[Zigbee](../Zigbee.md)**,**[Thread](../../thread/Thread.md)**,**[Matter](../../matter/Matter.md)**, 6LoWPAN 등 대표적인 스마트홈 프로토콜들의 "뿌리"가 되는 가장 중요한 하부 계층 (PHY/MAC) 표준입니다.

## 🎯 설계 목표 (Design Goals)

1. **초저전력 (Ultra Low Power)**: 코인 배터리 하나로 수년간 동작.
2. **저비용 (Low Cost)**: 칩셋 가격 최소화.
3. **저속 (Low Data Rate)**: 250kbps 수준. 대용량 파일 전송보다는 센서 데이터 제어용.

## 🏗️ 기기 유형 (Device Types)

이 표준에서는 기기의 능력에 따라 두 가지로 분류합니다.

1. **FFD (Full Function Device)**:
    - 모든 기능을 갖춘 기기입니다.
    - 네트워크의 코디네이터 (Coordinator) 나 라우터 (Router) 역할을 할 수 있습니다.
    - 상시 전원을 주로 사용합니다.
2. **RFD (Reduced Function Device)**:
    - 기능이 제한된, 아주 단순한 기기입니다.
    - End Device(센서 등) 로만 동작하며 라우팅을 하지 못합니다.
    - 배터리 효율이 극대화됩니다.

## 🕸️ 토폴로지 (Topologies)

- **Star Topology (스타형)**: 하나의 중앙 코디네이터에 여러 기기가 연결. (Wi-Fi 와 유사)
- **Peer-to-Peer Topology (P2P)**: 기기들끼리 서로 연결. 이를 확장하면** Mesh** 네트워크가 됩니다.

## 🗺️ 계층 구조 (Layer Structure)

IEEE 802.15.4 는 OSI 7 계층 중 하위 2 개 계층만 정의합니다.

- **[Layer 2: MAC](IEEE%20802.15.4%20MAC.md)**: 매체 접근 제어.
- **[Layer 1: PHY](IEEE%20802.15.4%20PHY.md)**: 물리적 신호 전송.
- (그 위의 Network/Application 계층은 Zigbee 나 Thread 가 정의합니다.)
