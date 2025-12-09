---
title: MQTT
tags: [iot, messaging, middleware, protocol]
aliases: [Message Queuing Telemetry Transport]
date modified: 2025-12-09 18:36:01 +09:00
date created: 2025-12-09 18:29:44 +09:00
---

## 🌐 개요 (Overview)
**MQTT (Message Queuing Telemetry Transport)**는 경량의 **발행 - 구독 (Publish-Subscribe)** 기반 메시징 프로토콜입니다. 대역폭이 제한적이거나 신뢰할 수 없는 네트워크 환경에서도 효율적으로 동작하도록 설계되었습니다.

>[!NOTE]
>MQTT 는 **Application Layer** 프로토콜이며, 주로 **TCP/IP** 위에서 동작합니다.
> **[[Matter]]**와는 경쟁 관계라기보다 상호 보완적이거나 다른 계층의 솔루션으로 볼 수 있습니다 (Matter 는 자체적인 CoAP 기반 통신을 사용).

## 🏗️ 아키텍처 (Pub/Sub)

전통적인 클라이언트 - 서버 모델과 달리, MQTT 는 **브로커 (Broker)**를 중계자로 사용합니다.

1. **Publisher (발행자)**: "거실 온도가 25 도야"라고 주제 (Topic) 에 메시지를 보냅니다.
2. **Broker (중계자)**: 메시지를 받아서 해당 주제를 구독한 사람들에게 배달합니다. (예: Mosquitto, EMQX)
3. **Subscriber (구독자)**: "거실 온도" 주제를 구독하고 있다가 메시지를 받습니다.

### 🛠️ 주요 특징
- **가벼움 (Lightweight)**: 헤더가 최소 2 바이트로 매우 작습니다.
- **QoS (Quality of Service)**: 메시지 전송 품질을 3 단계로 보장합니다 (0: 최대 한 번, 1: 최소 한 번, 2: 정확히 한 번).
- **Retain Message**: 브로커가 최신 값을 기억하고 있다가, 새로운 구독자가 오면 즉시 알려줍니다.
- **LWT (Last Will and Testament)**: 기기가 실수로 끊어졌을 때 "나 죽었어"라는 유언 메시지를 브로커가 대신 뿌려줍니다 (오프라인 감지에 유용).

## 🏠 스마트홈에서의 역할 (Usage)
- **통합의 제왕 (Integration)**: 서로 다른 제조사의 기기들을 하나로 묶는 "공용 버스" 역할을 합니다.
- **Zigbee2MQTT**: [Zigbee](Zigbee.md) 기기들의 신호 (ZCL) 를 MQTT 메시지 (JSON) 로 변환하여, Home Assistant 같은 플랫폼이 쉽게 제어할 수 있게 해줍니다.
- **커스텀 IoT 기기**: ESP32/Arduino 등으로 DIY 센서를 만들 때 가장 흔히 사용되는 프로토콜입니다.

### 🆚 Matter vs MQTT

| 특징 | **Matter** | **MQTT** |
| :--- | :--- | :--- |
| **방식** | 로컬 표준 규격 (직접 통신 위주) | 중앙집중형 브로커 경유 |
| **데이터** | 표준화된 데이터 모델 (Cluster) | 자유로운 형식 (주로 JSON payload) |
| **용도** | 기기 간 상호운용성 보장 (Plug & Play) | 커스텀 통합, DIY, 서버 연동 |
