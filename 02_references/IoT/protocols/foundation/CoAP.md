---
title: CoAP
tags: [iot, light-weight, messaging, protocol, udp]
aliases: [RFC 7252]
date modified: 2025-12-10 16:03:27 +09:00
date created: 2025-12-09 18:37:02 +09:00
---

## 🌐 개요 (Overview)

**CoAP (Constrained Application Protocol)** 는 소형 저전력 IoT 기기를 위해 설계된 매우 가벼운 웹 전송 프로토콜입니다. 쉽게 말해 **"IoT 를 위한 다이어트 버전의 HTTP"** 입니다.

>[!NOTE]
>[Matter](../matter/Matter.md) 는 기기 간 통신을 위해 내부적으로 CoAP 를 사용합니다. 우리가 웹에서 HTTP 를 쓰듯, Matter 기기들은 CoAP 를 통해 서로 명령 (TurnOn) 과 상태 (Status) 를 주고받습니다.

## 🏗️ 특징 (Features)

### 1. UDP 기반 (Over UDP)

- HTTP 가 신뢰성 있는 TCP 를 사용하는 것과 달리, CoAP 는 가벼운 **UDP** 를 사용합니다.
- 패킷 오버헤드가 극도로 작아 배터리 구동 기기 (**[Thread](../thread/Thread.md)** 등) 에 최적화되어 있습니다.
- 신뢰성 (메시지 도달 보장) 은 애플리케이션 계층에서 "Confirmable Message" 등을 통해 확보합니다.

### 2. HTTP 와 유사한 구조 (RESTful)

- 개발자에게 친숙한 **GET, POST, PUT, DELETE** 메서드를 사용합니다.
- 예: `coap://[IP주소]/light/state` 로 `PUT` 요청을 보내 불을 켤 수 있습니다.

### 3. 비동기 구독 (Observe)

- 클라이언트가 서버에게 "값 바뀌면 알려줘"라고 요청해두면, 상태가 변할 때마다 자동으로 알림을 줍니다 (HTTP 의 Polling 보다 훨씬 효율적).

## 🏠 Matter 에서의 역할

- **교통 정리**:**[Matter](../matter/Matter.md)** 의 모든 상호작용 (Interaction Model) 은 CoAP 메시지로 포장되어 전송됩니다.
- **효율성**:**[Thread](../thread/Thread.md)** 네트워크 위에서 데이터 트래픽을 최소화하여 느린 속도에서도 쾌적한 반응 속도를 만들어냅니다.

### 🆚 HTTP vs CoAP 비교

| 특징 | **HTTP**|** CoAP** |
| :--- | :--- | :--- |
| **기반 프로토콜**| TCP (무거움, 연결 지향) |** UDP** (가벼움, 비연결) |
| **헤더 크기**| 수십~수백 바이트 |** 4 바이트** (매우 작음) |
| **주 사용처**| 웹 브라우저, 스마트폰 앱 |** IoT 센서**,**[[../matter/Matter]]** 기기 |
| **자원 식별** | URI (http://…) | URI (coap://…) |
