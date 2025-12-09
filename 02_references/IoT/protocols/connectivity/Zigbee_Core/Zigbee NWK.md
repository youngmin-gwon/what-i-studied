---
title: Zigbee NWK
tags: [mesh, network, routing, zigbee]
aliases: [Zigbee Network Layer]
date modified: 2025-12-10 00:13:31 +09:00
date created: 2025-12-10 00:11:24 +09:00
---

## 🌐 개요 (Overview)
**Zigbee NWK (Network Layer)** 는 Zigbee 의 가장 강력한 무기인 **통합 메시 라우팅 (Mesh Routing)** 을 담당하는 계층입니다. **[IEEE 802.15.4](../IEEE_802_15_4/IEEE%20802.15.4.md)** MAC 위에서 동작하며, 데이터 패킷이 목적지까지 안전하게 도달하도록 경로를 찾습니다.

## 🕸️ 주요 기능 (Key Functions)

1. **라우팅 (Routing)**:
    - **AODV (Ad-hoc On-demand Distance Vector)**: 경로가 필요할 때마다 길을 찾는 방식입니다. ("목적지 가는 길 아는 사람?" 하고 방송)
    - **Tree Routing**: 부모 - 자식 관계를 따라 오르락내리락하는 방식입니다.
    - 이 두 가지를 혼합하여 최적의 경로를 관리합니다.
2. **주소 할당 (Addressing)**:
    - 16 비트의 짧은 **Network Address**를 기기에 부여합니다. (마치 IP 주소처럼)
    - 코디네이터는 항상 `0x0000` 입니다.
3. **네트워크 관리 (Management)**:
    - 새로운 기기가 네트워크에 들어오거나 (Join) 나가는 (Leave) 것을 관리합니다.
4. **보안 (Security)**:
    - 전체 네트워크가 공유하는 **Network Key**를 사용하여 패킷을 암호화합니다. 해커가 도청해도 내용을 알 수 없습니다.

## 🧭 메시 라우팅의 원리 (Mesh Mechanism)

- **Route Discovery**: A 가 B 에게 보내고 싶은데 길을 모르면 `RREQ` (Route Request) 를 방송합니다.
- **Re-broadcasting**: 중간에 있는 라우터들이 이 요청을 전달 - 전달합니다.
- **Route Reply**: B 가 요청을 받으면 `RREP` (Route Reply) 를 통해 가장 빠른 길을 알려줍니다.
- **Self-Healing**: 사용하던 경로의 전구가 고장 나면, 자동으로 우회 경로를 탐색하여 복구합니다.
