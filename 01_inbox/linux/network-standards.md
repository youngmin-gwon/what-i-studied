---
title: 네트워크 표준
tags: [linux, networking, osi, ieee, standards]
aliases: [Network Standards, OSI Model, IEEE 802, 네트워크 표준, 이더넷]
date modified: 2026-01-06 21:50:00 +09:00
date created: 2026-01-06 21:50:00 +09:00
---

## 🌐 개요 (Overview)

네트워크 계층 모델(OSI, TCP/IP)과 관련 국제 표준에 대해 다룹니다.

---

## 📊 OSI 7계층 모델

**ISO(International Organization for Standardization)** 에서 제정한 네트워크 통신 표준 모델입니다.

| 계층 | 이름 | PDU | 장비 | 프로토콜 예시 |
| :--- | :--- | :--- | :--- | :--- |
| 7 | 응용 (Application) | 데이터 | - | HTTP, FTP, SMTP, DNS |
| 6 | 표현 (Presentation) | 데이터 | - | SSL/TLS, JPEG, MPEG |
| 5 | 세션 (Session) | 데이터 | - | NetBIOS, RPC |
| 4 | 전송 (Transport) | 세그먼트 | - | TCP, UDP |
| **3** | **네트워크 (Network)** | 패킷 | **Router** | IP, ICMP, ARP |
| **2** | **데이터링크 (Data Link)** | 프레임 | **Bridge, Switch** | Ethernet, PPP |
| **1** | **물리 (Physical)** | 비트 | **Repeater, Hub** | 10BASE-T, RS-232 |

> [!IMPORTANT]
> **시험 포인트**: OSI 계층별 장비
> - **Layer 1 (물리)**: Repeater, Hub
> - **Layer 2 (데이터링크)**: Bridge, Switch
> - **Layer 3 (네트워크)**: Router
> - **Router가 가장 많은 계층 지원** (L1~L3)

---

## 📡 네트워크 장비

| 장비 | OSI 계층 | 역할 |
| :--- | :--- | :--- |
| **Repeater** | L1 (물리) | 신호 증폭, 거리 연장 |
| **Hub** | L1 (물리) | 멀티포트 리피터 (브로드캐스트) |
| **Bridge** | L2 (데이터링크) | MAC 주소 기반 프레임 필터링, 세그먼트 연결 |
| **Switch** | L2 (데이터링크) | 멀티포트 브리지 (고속) |
| **Router** | L3 (네트워크) | IP 주소 기반 패킷 라우팅, 네트워크 연결 |

> [!TIP]
> **Bridge 설명**: OSI 데이터링크 계층에서 동작하며, 여러 네트워크 세그먼트를 연결하고 트래픽을 관리합니다.

---

## 🔌 IEEE 802 표준

IEEE (Institute of Electrical and Electronics Engineers)에서 제정한 LAN/MAN 표준입니다.

| 표준 | 이름 | 설명 |
| :--- | :--- | :--- |
| 802.3 | Ethernet | 유선 LAN (CSMA/CD) |
| 802.5 | Token Ring | 토큰 링 방식 |
| **802.6** | **DQDB** | **MAN (Metropolitan Area Network)** 표준 |
| 802.11 | Wi-Fi | 무선 LAN |
| 802.15 | Bluetooth | 개인 영역 네트워크 |

> [!IMPORTANT]
> **시험 포인트**: IEEE 802.6 = **DQDB (Distributed Queue Dual Bus)** = MAN 표준

---

## 🔗 이더넷 매체 표기법

형식: `[속도]BASE-[매체코드]`

| 표기 | 속도 | 매체 | 설명 |
| :--- | :--- | :--- | :--- |
| **10BASE-5** | 10Mbps | 동축 케이블 | Thicknet (두꺼운 동축) |
| **10BASE-2** | 10Mbps | 동축 케이블 | Thinnet (얇은 동축) |
| **10BASE-T** | 10Mbps | UTP | Twisted Pair |
| **100BASE-TX** | 100Mbps | UTP-5 | Fast Ethernet |
| **100BASE-FX** | 100Mbps | 광케이블 | Fast Ethernet (광) |
| **1000BASE-SX** | 1Gbps | 광케이블 | **Short wavelength (단파장)** |
| **1000BASE-LX** | 1Gbps | 광케이블 | **Long wavelength (장파장)** |
| **1000BASE-T** | 1Gbps | UTP | Gigabit Ethernet |

> [!WARNING]
> **시험 포인트**:
> - **SX** = Short (단파장 광케이블)
> - **LX** = Long (장파장 광케이블)
> - **T** = Twisted Pair (UTP)
> - **FX** = Fiber (광케이블)

---

## 🔌 UTP 케이블 배선 (T568B)

T568B 표준 배열 순서:

| 핀 | 색상 |
| :--- | :--- |
| 1 | 흰주 (White-Orange) |
| 2 | 주 (Orange) |
| 3 | 흰녹 (White-Green) |
| 4 | 파 (Blue) |
| 5 | 흰파 (White-Blue) |
| 6 | 녹 (Green) |
| 7 | 흰갈 (White-Brown) |
| 8 | 갈 (Brown) |

> [!TIP]
> **T568B 순서**: 흰주 → 주 → 흰녹 → 파 → 흰파 → 녹 → 흰갈 → 갈

---

## 📦 WAN 기술

| 기술 | 특징 |
| :--- | :--- |
| **X.25** | 패킷 스위칭 (가변 길이), 오류 제어 중심 |
| **Frame Relay** | 프레임 스위칭, X.25보다 빠름 |
| **Cell Relay (ATM)** | **53 바이트 고정 길이 셀**, 고속 전송 |

> [!IMPORTANT]
> **ATM (Asynchronous Transfer Mode)**:
> - Cell Relay 방식
> - 53 바이트 고정 길이 셀
> - 순서대로 전송

---

## 🏢 국제 표준화 기구

| 기구 | 설명 | 주요 업무 |
| :--- | :--- | :--- |
| **ISO** | 국제표준화기구 | **OSI 7계층 모델** 제정 |
| **IEEE** | 전기전자기술자협회 | LAN/MAN 표준 (802.x) |
| **EIA** | 전자산업협회 | RS-232C, UTP 케이블 규격 |
| **ITU-T** | 국제전기통신연합 | 전기 통신 표준화 (정부 간 기구) |
| **ICANN** | 국제인터넷주소관리기구 | IP 주소 할당, 도메인 관리 |
| **IANA** | 인터넷할당번호관리기관 | 포트 번호, 프로토콜 번호 |
| **W3C** | 월드와이드웹컨소시엄 | 웹 표준 (HTML, CSS) |

---

## 🔗 연결 문서 (Related Documents)

- [[network-fundamentals]] - 네트워크 기초 (IP, 서브넷)
- [[network-commands]] - 네트워크 명령어
- [[tcp-ip-model]] - TCP/IP 모델
