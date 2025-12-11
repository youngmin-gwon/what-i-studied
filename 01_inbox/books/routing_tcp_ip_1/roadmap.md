---
title: roadmap
tags: []
aliases: []
date modified: 2025-12-11 13:59:33 +09:00
date created: 2025-12-11 10:58:04 +09:00
---

## **Part I: 라우팅 기초 (Routing Basics)**

네트워크의 기본 프로토콜과 라우팅의 핵심 개념을 다루는 기초 단계입니다.

- **[1장: TCP/IP Review (TCP/IP 리뷰)](chapter1.md)**
    - TCP/IP 프로토콜의 계층 구조, IPv4 주소 체계, 서브넷 마스크, ARP, ICMP 등 패킷 포워딩에 필수적인 기본 지식을 복습합니다,.
- **[2장: IPv6 Overview (IPv6 개요)](chapter2.md)**
    - 차세대 프로토콜인 IPv6 의 주소 형식 (Unicast, Anycast, Multicast), 헤더 포맷, 그리고 ARP 를 대체하는 Neighbor Discovery Protocol(NDP) 등을 설명합니다,.
- **[3장: Static Routing (정적 라우팅)](chapter3.md)**
    - 라우터에 수동으로 경로를 설정하는 방법, 부하 분산 (Load Sharing), 그리고 정적 경로의 문제 해결 방법을 다룹니다,.
- **[4장: Dynamic Routing Protocols (동적 라우팅 프로토콜)](chapter4.md)**
    - 거리 벡터 (Distance Vector) 와 링크 상태 (Link State) 프로토콜의 차이, 메트릭, 수렴 (Convergence) 등 동적 라우팅의 공통적인 이론적 배경을 설명합니다,.

## **Part II: 내부 라우팅 프로토콜 (Interior Routing Protocols)**

실제 네트워크에서 사용되는 주요 IGP 들의 동작 원리와 구성을 깊이 있게 다룹니다.

- **[5장: Routing Information Protocol (RIP)](chapter5.md)**
    - 가장 오래된 거리 벡터 프로토콜인 RIPv1 의 동작 (타이머, 홉 카운트) 과 클래스풀 (Classful) 라우팅의 제약 사항을 다룹니다,.
- **[6장: RIPv2, RIPng, and Classless Routing (RIPv2, RIPng 및 클래스리스 라우팅)](chapter6.md)**
    - RIPv1 을 확장하여 서브넷 마스크를 포함시킨 RIPv2(VLSM 지원) 와 IPv6 를 위한 RIPng, 그리고 클래스리스 라우팅의 개념을 설명합니다,.
- **[7장: Enhanced Interior Gateway Routing Protocol (EIGRP)](chapter7.md)**
    - Cisco 전용 프로토콜에서 개방형으로 전환된 EIGRP 의 DUAL 알고리즘, 복합 메트릭, 그리고 빠른 수렴을 위한 메커니즘을 다룹니다,.
- **[8장: OSPFv2 (Open Shortest Path First Version 2)](chapter8.md)**
    - 가장 널리 쓰이는 링크 상태 프로토콜인 OSPF 의 계층적 영역 (Area) 구조, LSA 유형, DR/BDR 선출, SPF 알고리즘 등을 설명합니다,.
- **[9장: OSPFv3](chapter9.md)**
    - IPv6 를 지원하기 위해 새롭게 설계된 OSPFv3 의 특징 (링크 로컬 주소 사용, 주소 정보와 토폴로지 정보의 분리 등) 을 다룹니다,.
- **[10장: Integrated IS-IS (통합 IS-IS)](chapter10.md)**
    - OSI 프로토콜을 위해 개발되었으나 IP 라우팅을 지원하는 통합 IS-IS 의 구조 (Level 1/2 라우팅), TLV 패킷 형식, 그리고 확장성 등을 다룹니다,.

## **Part III: 경로 제어 및 상호 운용성 (Route Control and Interoperability)**

여러 라우팅 프로토콜을 함께 사용하거나 경로를 세밀하게 제어하는 고급 기술을 다룹니다.

- **[11장: Route Redistribution (경로 재분배)](chapter11.md)**
    - 서로 다른 라우팅 프로토콜 간에 경로 정보를 교환하는 방법, 메트릭 변환, 그리고 재분배 시 발생할 수 있는 루프 방지 기술을 설명합니다,.
- **[12장: Default Routes and On-Demand Routing (디폴트 경로와 ODR)](chapter12.md)**
    - 디폴트 경로의 생성 및 전파 방법과, 허브 - 앤 - 스포크 환경에서 CDP 를 이용한 간편한 라우팅 방식인 ODR 을 다룹니다,.
- **[13장: Route Filtering (경로 필터링)](chapter13.md)**
    - 특정 경로의 광고를 차단하거나 수신을 거부하여 트래픽 흐름을 제어하고 라우팅 루프를 방지하는 필터링 기술 (distribute-list 등) 을 설명합니다,.
- **[14장: Route Maps (루트 맵)](chapter14.md)**
    - 복잡한 조건에 따라 경로 속성을 변경하거나 정책 기반 라우팅 (Policy-Based Routing) 을 구현하는 데 사용되는 루트 맵의 활용법을 다룹니다,.
