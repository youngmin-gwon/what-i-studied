---
title: Ethernet
tags: [backbone, iot, network, wired]
aliases: [LAN, Wired Network]
date modified: 2025-12-09 23:59:32 +09:00
date created: 2025-12-09 18:29:27 +09:00
---

## 🌐 개요 (Overview)

**Ethernet (이더넷)** 은 가장 신뢰할 수 있는 유선 네트워킹 기술입니다. 무선 간섭이 전혀 없으며, 최고의 속도와 안정성을 보장합니다. 스마트홈에서는 주로 **허브, 브리지, 보더 라우터, 카메라** 등 핵심 인프라 장비에 사용됩니다.

## 🏗️ 프로토콜 특성

- **계층**: OSI Layer 1 (Physical) & Layer 2 (Data Link).
- **속도**: 100 Mbps, 1 Gbps, 2.5 Gbps 이상 (IoT 기기에는 100 Mbps 로도 충분).
- **매체**: UTP 케이블 (Cat5e, Cat6 등).

### 🔋 PoE (Power over Ethernet)

이더넷의 강력한 장점 중 하나는 데이터와 전력을 케이블 하나로 동시에 공급할 수 있다는 점입니다.

- **활용**: IP CCTV 카메라, 천장형 AP, 스마트 디스플레이.
- **장점**: 별도의 전원 공사가 필요 없어 설치가 깔끔하고 관리가 용이합니다.

## 🏠 스마트홈에서의 역할 (Smart Home Role)

1. **백본 (Backbone)**: 무선 신호가 도달하기 힘든 곳이나, 데이터 트래픽이 집중되는 **[Thread Border Router](../thread/Border%20Router.md)** 및 **스마트홈 허브 (Hub)** 를 연결하는 최적의 수단입니다.
2. **안정성 (Stability)**: [Wi-Fi](Wi-Fi.md) 나 [Zigbee](Zigbee.md) 등 무선 프로토콜은 전파 간섭 (Interference) 에 취약하지만, 이더넷은 완벽한 격리성을 제공합니다.
3. **지연 시간 (Latency)**: 무선 대비 압도적으로 낮은 지연 시간 (Ping) 을 제공하여, 반응 속도가 중요한 자동화 서버 (Home Assistant 등) 에 필수적입니다.

>[!TIP]
>스마트홈을 안정적으로 구축하려면, 이동하지 않는 고정형 허브나 브리지는 가능한 한 **유선 (Ethernet)** 으로 연결하는 것이 "국룰"입니다.
