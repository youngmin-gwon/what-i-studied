---
title: OFDMA
tags: [foundation, modulation, wifi6, wireless]
aliases: [Orthogonal Frequency-Division Multiple Access]
---

## 📡 개요 (Overview)

**OFDMA** (Orthogonal Frequency-Division Multiple Access)는 **Wi-Fi 6 (802.11ax)** 에서 도입된 핵심 기술로, 여러 기기가 동시에 무선 채널을 효율적으로 공유할 수 있게 해줍니다.

- **[OFDM](OFDM.md)** 의 확장 버전입니다.
- **IoT 환경**에서 수십~수백 개의 기기가 동시에 연결될 때 성능을 획기적으로 향상시킵니다.

## 🔍 OFDM vs OFDMA

### OFDM (기존 Wi-Fi 4/5)

- **Orthogonal Frequency-Division Multiplexing**: 하나의 채널을 여러 개의 작은 주파수(서브캐리어)로 나눕니다.
- 하지만 **한 번에 한 기기**만 전체 채널을 사용할 수 있습니다.
- 비유: "넓은 고속도로를 한 대의 차만 독점 사용"

### OFDMA (Wi-Fi 6 이후)

- **Multiple Access**: 여러 기기가 **동시에** 서브캐리어를 나눠 쓸 수 있습니다.
- 각 기기에 필요한 만큼만 주파수를 할당합니다 (RU: Resource Unit).
- 비유: "고속도로를 여러 차선으로 나눠서 여러 차가 동시에 달림"

```mermaid
block-beta
  columns 3
  
  block:OFDM["OFDM (Wi-Fi 5)"]
    Device1["Device A (전체 채널 사용)"]
  end
  
  space
  
  block:OFDMA["OFDMA (Wi-Fi 6)"]
    DevA["Device A"]
    DevB["Device B"]
    DevC["Device C"]
  end
  
  OFDM --> OFDMA
```

## 🎯 IoT 에서의 중요성

### 1. 지연 시간 감소 (Lower Latency)

- 작은 데이터를 보내는 센서들이 **대기하지 않고** 즉시 전송할 수 있습니다.
- 예: 온도 센서가 카메라의 대용량 전송을 기다릴 필요가 없음.

### 2. 효율성 증대 (Efficiency)

- 각 기기가 필요한 만큼만 대역폭을 사용하므로 **낭비가 줄어듭니다**.
- 예: 스마트 전구(작은 명령)와 보안 카메라(영상 스트리밍)가 동시에 효율적으로 동작.

### 3. 동시 접속 기기 수 증가

- Wi-Fi 5 에서는 10~20 개 기기가 한계였다면, Wi-Fi 6 는 **수십~수백 개** 를 동시에 처리 가능.

## 🆚 비교: Thread/Zigbee vs Wi-Fi 6 (OFDMA)

| 특징 | **[Thread](../connectivity/Thread.md)/[Zigbee](../connectivity/Zigbee.md)** | **Wi-Fi 6 (OFDMA)** |
| :--- | :--- | :--- |
| **접근 방식** | 메시 네트워크 (Mesh) | 스타 토폴로지 + 효율적 채널 공유 |
| **전력 소모** | 매우 낮음 (배터리 기기용) | 높음 (상시 전원 기기용) |
| **대역폭** | 낮음 (250 kbps) | 매우 높음 (Gbps) |
| **주 용도** | 센서, 스위치 | 카메라, 스피커, 디스플레이 |

> [!TIP]
> **[Matter](../matter/Matter.md)** 는 두 세계의 장점을 결합합니다:
> - 배터리 기기 → **[Thread](../connectivity/Thread.md)** (저전력)
> - 상시 전원 기기 → **Wi-Fi 6** (고속 + OFDMA 효율성)
