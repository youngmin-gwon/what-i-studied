---
title: Z-Wave
tags: [iot, protocol, sub-ghz]
aliases: []
date modified: 2025-12-09 18:01:45 +09:00
date created: 2025-12-09 11:59:07 +09:00
---

## 🌐 개요 (Overview)
**Z-Wave**는 신뢰성 높고 지연 시간이 짧은 통신에 최적화된 독점 무선 메시 프로토콜입니다. **Sub-GHz** (1GHz 미만) 주파수 대역에서 작동하므로 [Wi-Fi](Wi-Fi.md)/[Bluetooth](Bluetooth.md)/[Zigbee](Zigbee.md) 의 간섭을 피할 수 있습니다.

>[!NOTE]
>Z-Wave 는 **Full Stack** 프로토콜입니다. 1 계층부터 7 계층까지 교과서적인 정의를 포함하며, Z-Wave Alliance (Silicon Labs) 에 의해 엄격하게 관리됩니다.

## 🏗️ 프로토콜 스택 (Full Stack)

[Zigbee](Zigbee.md) 와 유사하게 Z-Wave 는 비 (非) IP 방식이며 허브 (Hub) 가 필요합니다.

| 계층 (Layer) | 기술 (Technology) | 상세 내용 (Details) |
| :--- | :--- | :--- |
| **Layer 7** (Application) | **Z-Wave Command Classes** | 기기 기능 (Function) 에 대한 엄격한 정의입니다 (상호 운용성이 매우 높음). |
| **Layer 3** (Network) | **Z-Wave Mesh** | 소스 라우팅 (Source Routing). **최대 4 홉 (Hop)** 제한이 있어 네트워크 확장에 신중해야 합니다. |
| **Layer 1-2** (PHY/MAC) | **ITU-T G.9959** | **Sub-GHz 주파수**. 간섭이 적고 벽을 잘 통과합니다. |

### 🛠️ 핵심 기술 사양 (Key Specs)

| 특징 | 상세 내용 | 이점 |
| :--- | :--- | :--- |
| **주파수** | **Sub-1 GHz** (미국 908MHz, 유럽 868MHz) | 2.4GHz 혼잡 완전 회피. 우수한 벽 투과율. |
| **홉 (Hop) 제한** | 최대 **4 회** | 라우팅 복잡도를 낮춰 안정성 확보 (단, 대형 건물엔 불리). |
| **보안** | **S2 (Security 2)** | AES-128 암호화. 은행 수준의 보안 등급 (Access Control) 적용. |
| **신뢰성** | **"신뢰성 장인"** | 엄격한 인증 절차로 브랜드 간 호환성을 100% 보장. |

### 🛠️ 주요 구성 요소 (Key Components)
1. **컨트롤러 (Controller/Hub)**: 네트워크의 마스터입니다. 네트워크 ID (Home ID) 를 관리합니다.
2. **지역 잠금 (Region Locking)**: 주파수가 국가별로 다르기 때문에, 미국용 기기는 유럽 허브와 **작동하지 않습니다**.
3. **Z-Wave Long Range (LR)**: 최신 표준으로, 메시가 아닌 스타 토폴로지를 지원하여 피어 - 투 - 피어 거리를 획기적으로 늘린 기술입니다.

## 🏠 스마트홈에서의 역할 (Smart Home Role)
- **신뢰성 (Reliability)**: 보안 장비 (도어락, 센서) 에 가장 선호되는 "프리미엄" 프로토콜입니다.
- **제한 (Limit)**: 역사적으로 232 개 기기 제한이 있었으나 (가정용으론 충분), LR 및 800 시리즈부터 확장되었습니다.
