---
title: CSMA/CA
tags: [network, algorithm, mac, foundation]
aliases: [Carrier Sense Multiple Access with Collision Avoidance]
---

## 🌐 개요 (Overview)
**CSMA/CA**(Carrier Sense Multiple Access with Collision Avoidance)는**[Wi-Fi](../connectivity/Wi-Fi.md)**(IEEE 802.11)와**[Zigbee](../connectivity/Zigbee.md) / [Thread](../thread/Thread.md)** (IEEE 802.15.4)에서 사용하는 매체 접근 제어 방식입니다. 무선 공간은 모두가 공유하는 자원이므로, 서로 부딪히지 않고 "눈치껏" 데이터를 보내는 기술입니다.

## 🚦 동작 원리 (Mechanism)

사람들이 대화할 때 "잠시 듣고 있다가 조용해지면 말하는 것"과 유사합니다. 유선망의 CSMA/CD(충돌 감지)와 달리, 무선은 충돌을 완벽히 감지하기 어렵기 때문에 **충돌 회피(Avoidance)** 에 집중합니다.

1.  **Listen (Carrier Sense)**:
    *   데이터를 보내기 전에 채널이 사용 중인지 들어봅니다(CCA: Clear Channel Assessment).
2.  **Wait (Backoff)**:
    *   채널이 비어 있어도 바로 보내지 않고, 랜덤한 시간(Random Backoff)만큼 기다립니다. 동시에 여러 기기가 말하는 것을 방지하기 위함입니다.
3.  **Send (Transmission)**:
    *   기다린 후에도 채널이 비어있으면 데이터를 전송합니다.
4.  **Confirm (ACK)**:
    *   데이터를 잘 받았다는 수신 측의 응답(ACK)을 받아야 전송 성공으로 간주합니다. ACK가 없으면 충돌로 간주하고 재전송합니다.

## ⚠️ Hidden Node Problem (숨겨진 노드 문제)

A와 C는 서로 너무 멀어서 안 들리지만, 가운데 있는 B에게는 둘 다 들리는 상황입니다.
*   A가 B에게 전송 중일 때, C는 A의 신호를 못 듣고 "채널이 비었네?" 하고 B에게 전송합니다. -> **B에서 충돌 발생!***** 해결책 (RTS/CTS)**:
    *   A가 "나 보낼게(RTS)"라고 외치면, B가 "그래 보내(CTS)"라고 전체에 방송합니다. C는 B의 CTS를 듣고 조용히 기다립니다. (주로 Wi-Fi에서 사용)
