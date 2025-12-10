---
title: IEEE 802.15.4 PHY
tags: [frequency, modulation, phy, radio]
aliases: []
date modified: 2025-12-10 00:13:36 +09:00
date created: 2025-12-10 00:09:26 +09:00
---

## 🌐 개요 (Overview)

**IEEE 802.15.4 PHY** 계층은 실제 무선 주파수 (RF) 신호를 쏘고 받는 물리적 하드웨어 규격입니다. 주파수 대역, 변조 방식, 출력 파워 등을 정의합니다.

## 📡 주파수 대역 (Frequency Bands)

가장 대중적인 것은 **2.4 GHz** 대역입니다.

| 대역 (Band) | 지역 (Region) | 채널 수 | 속도 | 특징 |
| :--- | :--- | :--- | :--- | :--- |
| **2.4 GHz**|** 전 세계 (Global)**| 16 개 (11~26 번) | 250 kbps |** 가장 널리 사용됨**. Wi-Fi 와 간섭 가능성 있음. |
| 868 MHz | 유럽 | 1 개 | 20 kbps | 도달 거리가 김. (Sub-GHz) |
| 915 MHz | 북미 | 10 개 | 40 kbps | 도달 거리가 김. (Sub-GHz) |

>[!TIP]
> **Thread** 와**Zigbee** 는 대부분**2.4 GHz O-QPSK** PHY 를 사용합니다.

## 🎛️ 변조 방식 (Modulation) - O-QPSK

2.4 GHz 대역에서는 **O-QPSK**(Offset Quadrature Phase Shift Keying) 와** DSSS** (Direct Sequence Spread Spectrum) 를 사용합니다.
- **강인함**: DSSS 는 데이터를 넓은 주파수에 퍼뜨려서 보내므로, 특정 주파수에 노이즈가 끼어도 복구가 가능합니다. Wi-Fi 보다 느리지만** 간섭에 강합니다**.

## 📶 채널 (Channels)

2.4 GHz 대역의 채널은 5MHz 간격으로 배치됩니다.
- **채널 11, 15, 20, 25** 번이 Wi-Fi 채널 사이사이에 위치하여 간섭이 적은 "꿀 채널"로 불립니다. (특히**25, 26 번** 은 Wi-Fi 채널 11 번 끝자락보다 뒤에 있어 가장 안전합니다.)

## 📏 물리적 특성

- **수신 감도 (Sensitivity)**: 보통 -100 dBm 수준으로 매우 민감하여 미약한 신호도 잘 잡습니다.
- **출력 (TX Power)**: Wi-Fi(100mW~1W) 보다 훨씬 낮은 수~수십 mW 수준을 사용하여 배터리를 아낍니다.
