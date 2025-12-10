---
title: O-QPSK
tags: [foundation, modulation, phy, wireless]
aliases: [Offset Quadrature Phase Shift Keying]
---

## 📡 개요 (Overview)

**O-QPSK** (Offset Quadrature Phase Shift Keying)는 디지털 변조 방식의 일종으로, **[IEEE 802.15.4](../connectivity/IEEE_802_15_4/IEEE%20802.15.4.md)** (Zigbee, Thread) 표준에서 채택한 핵심 변조 기술입니다.

- 기본 QPSK(Quadrature Phase Shift Keying)를 개량하여, 신호의 급격한 변화를 줄이고 전력 효율을 높였습니다.
- **저전력 무선 통신**에 매우 적합합니다.

## ⚙️ 동작 원리 (Mechanism)

### 1. QPSK 의 문제점

- QPSK 는 위상(Phase)을 0°, 90°, 180°, 270° 네 가지로 변조하여 정보를 보냅니다.
- 하지만 180° 로 위상이 급격하게 변하는 경우(예: 0° → 180°), 신호의 진폭(Amplitude)이 순간적으로 0을 지나게 됩니다.
- 이는 증폭기(Amplifier)의 선형성을 요구하며, 결과적으로 **배터리 소모**가 커지고 설계가 복잡해집니다.

### 2. O-QPSK 의 해결책 (Offset)

- **Offset (시간차)**: I(In-phase) 채널과 Q(Quadrature) 채널의 신호 타이밍을 딱 절반 주기(Half Symbol)만큼 **어긋나게(Offset)** 만듭니다.
- **결과**: 위상이 90° 씩만 변하게 되어 180° 널뛰기를 방지합니다.
- **장점**: 진폭의 변화가 줄어들어 전력 효율이 높은 **비선형 증폭기(Non-linear Amplifier)**를 사용할 수 있습니다.

## 🔌 활용 (Applications)

- **[IEEE 802.15.4](../connectivity/IEEE_802_15_4/IEEE%20802.15.4.md)**: 2.4 GHz 대역의 물리 계층 표준 변조 방식.
- **[Zigbee](../connectivity/Zigbee.md)**: O-QPSK 를 사용하여 저전력 메시 네트워크를 구현.
- **[Thread](../thread/Thread.md)**: 마찬가지로 802.15.4 기반이므로 O-QPSK 를 사용.
- **[Matter](../matter/Matter.md)**: Thread 기반의 Matter 연결은 물리적으로 O-QPSK 변조된 신호를 통해 이루어짐.

> [!NOTE]
> **[OFDM](OFDM.md)**과 비교하면, O-QPSK 는 속도(Data Rate)는 낮지만(250 kbps), 회로가 단순하고 전력 소모가 적어 배터리 기반 IoT 센서에 이상적입니다.
