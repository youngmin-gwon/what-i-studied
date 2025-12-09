---
title: IPv6
tags: [network, protocol, internet, foundation]
aliases: [Internet Protocol version 6]
---

## 🌐 개요 (Overview)
**IPv6 (Internet Protocol version 6)**는 IPv4의 주소 고갈 문제를 해결하고 차세대 인터넷 환경을 지원하기 위해 개발된 네트워크 계층 표준입니다. IoT 환경, 특히 **[Matter](../matter/Matter.md)**와 **[Thread](../thread/Thread.md)**에서 핵심적인 역할을 수행합니다.

## 🔑 주요 특징 (Key Features)

1.  **무한한 주소 공간 (Address Space)**:
    *   128비트 주소 체계를 사용하여 약 $3.4 \times 10^{38}$개의 주소를 제공합니다.
    *   모든 IoT 센서에 공인 IP를 부여해도 고갈되지 않습니다.
2.  **헤더 단순화 (Simplified Header)**:
    *   IPv4 헤더의 불필요한 필드를 제거하고 고정 길이 헤더를 사용하여 라우팅 효율성을 높였습니다.
3.  **자동 구성 (SLAAC)**:
    *   DHCP 서버 없이도 기기 스스로 주소를 생성할 수 있는 **Stateless Address Autoconfiguration**을 지원합니다.
4.  **보안 내장 (Built-in Security)**:
    *   IPsec 지원이 필수(Mandatory)사항으로 설계되었습니다.

## 🏗️ 주소 구조 (Address Structure)

`2001:0db8:85a3:0000:0000:8a2e:0370:7334`와 같이 16진수로 표기합니다.

*   **Global Unicast Address**: 인터넷에서 라우팅 가능한 공인 IP.
*   **Link-Local Address (fe80::/10)**: 로컬 네트워크(LAN) 내에서만 유효한 주소. Matter/Thread 네트워크 탐색에 필수적입니다.
*   **Multicast Address (ff00::/8)**: 그룹 통신을 위한 주소. (Broadcast가 삭제되고 Multicast로 대체됨)

## 🏠 IoT에서의 IPv6 (Role in IoT)

**[Thread](../thread/Thread.md)**와 **[Matter](../matter/Matter.md)**는 기본적으로 IPv6 기반입니다.

*   **End-to-End Connectivity**: 클라우드 서버와 전구(End Device)가 NAT 없이 직접 통신할 수 있습니다.
*   **[6LoWPAN](6LoWPAN.md)**: 무거운 IPv6 패킷을 저전력 무선 구간(IEEE 802.15.4)으로 보내기 위해 압축 기술을 사용합니다.
