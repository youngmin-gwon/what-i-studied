---
title: OFDM
tags: [foundation, modulation, phy, signal]
aliases: [Orthogonal Frequency Division Multiplexing]
date modified: 2025-12-11 13:37:06 +09:00
date created: 2025-12-10 09:55:45 +09:00
---

## 🌐 개요 (Overview)

**OFDM**(Orthogonal Frequency Division Multiplexing, 직교 주파수 분할 다중화) 은 고속 데이터를 여러 개의 느린 서브캐리어 (Subcarrier) 에 나누어 실어 보내는 변조 기술입니다. **[Wi-Fi](../connectivity/Wi-Fi.md)**(802.11a/g/n/ac/ax) 와 **LTE/5G** 통신의 핵심 기술입니다. (구형 802.15.4/Zigbee 는 [O-QPSK](O-QPSK.md) 를 사용하지만, [Wi-SUN](../connectivity/Wi-SUN.md) 등 최신 표준은 OFDM 을 도입하기도 합니다.)

## 📡 핵심 원리 (Core Principle)

### 1. 나누어 보내기 (FDM)

하나의 빠른 트럭으로 짐을 나르는 대신, 수백 대의 오토바이에 짐을 나누어 동시에 출발시킵니다.

- **장점**: 특정 주파수에 잡음 (Noise) 이 있어도 그 대역의 데이터만 손상되고 나머지는 안전합니다.

### 2. 직교성 (Orthogonality)

일반 FDM 은 주파수 간섭을 막기 위해 채널 사이에 간격 (Guard Band) 을 둬야 해서 낭비가 심합니다.

OFDM 은 수학적으로 서로 간섭하지 않는 (직교하는) 파형을 사용하여 주파수를 **겹쳐서 (Overlapping)** 배치합니다. 이를 통해 주파수 효율을 극대화합니다.

### 3. 심볼 간 간섭 방지 (ISI 제거)

무선 신호는 벽에 반사되어 시간차를 두고 들어옵니다 (Multipath Fading). 데이터가 너무 빠르면 앞 신호의 잔향이 뒤 신호를 방해합니다. OFDM 은 데이터를 천천히 (병렬로) 보내므로 이 반사파 문제를 견디는 힘이 강합니다.

## 🚀 활용 (Uses)

- **Wi-Fi 6 (802.11ax)**: **[OFDMA](OFDMA.md)** 로 발전하여, 하나의 채널을 시간과 주파수로 더 잘게 쪼개 여러 사용자에게 동시에 할당합니다.
- **PLC (전력선 통신)**: 노이즈가 심한 전력선 환경에서도 강인함을 보입니다.
