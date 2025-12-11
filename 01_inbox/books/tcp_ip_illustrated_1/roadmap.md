
### **1. 아키텍처 및 주소 지정 (기초)**

네트워크의 기본 원리와 IP 주소 체계를 다룹니다.

*   **[1장: 서론 (Introduction)](chapter1.md)**
    *   **내용:** TCP/IP 프로토콜의 역사, 아키텍처 원칙(패킷 교환, 종단 간 인수), 계층 구조(Layering), 캡슐화 및 다중화, 그리고 표준화 과정(RFC)을 소개합니다.
*   **[2장: 인터넷 주소 아키텍처 (The Internet Address Architecture)](chapter2.md)**
    *   **내용:** IPv4 및 IPv6 주소의 구조, 클래스 기반 주소 지정에서 CIDR(Classless Inter-Domain Routing)로의 전환, 서브넷 마스크, 유니캐스트/멀티캐스트/애니캐스트 주소 유형을 설명합니다.

### **2. 링크 계층 (Link Layer)**

IP 패킷을 물리적으로 전송하는 기술들을 다룹니다.

*   **[3장: 링크 계층 (Link Layer)](chapter3.md)**
    *   **내용:** 이더넷(Ethernet), Wi-Fi(IEEE 802.11), PPP(Point-to-Point Protocol)의 프레임 구조와 동작 방식, 그리고 MTU(최대 전송 단위)와 터널링 기초를 다룹니다.
*   **[4장: ARP (Address Resolution Protocol)](chapter4.md)**
    *   **내용:** IPv4 주소를 하드웨어 주소(MAC)로 변환하는 ARP의 동작, ARP 캐시, 프록시 ARP, 그리고 주소 충돌 감지(ACD)를 설명합니다. (IPv6는 8장의 ND를 사용).

### **3. 네트워크 계층 및 인프라 (Network Layer & Infrastructure)**

IP 패킷의 전달, 제어, 설정 및 보안 관련 인프라를 다룹니다.

*   **[5장: 인터넷 프로토콜 (IP)](chapter5.md)**
    *   **내용:** IPv4 및 IPv6의 헤더 구조, 패킷 전달(Forwarding) 원리, 확장 헤더, 모바일 IP의 기본 개념을 설명하는 IP 계층의 핵심 장입니다.
*   **[6장: 시스템 구성 (DHCP and Autoconfiguration)](chapter6.md)**
    *   **내용:** 호스트가 IP 주소를 얻는 방법인 DHCP(v4/v6)와 IPv6의 상태 비보존 주소 자동 설정(SLAAC), 그리고 릴레이 에이전트의 역할을 다룹니다.
*   **[7장: 방화벽 및 NAT (Firewalls and Network Address Translation)](chapter7.md)**
    *   **내용:** 패킷 필터링 및 프록시 방화벽의 원리, NAT(Network Address Translation)의 동작과 NAT 통과(Traversal) 기술(STUN, TURN, ICE)을 설명합니다.
*   **[8장: ICMP (Internet Control Message Protocol)](chapter8.md)**
    *   **내용:** 오류 보고 및 진단(Ping, Traceroute)을 위한 ICMPv4/v6 메시지, 그리고 IPv6의 핵심인 이웃 발견(Neighbor Discovery, ND) 프로토콜을 다룹니다.
*   **[9장: 브로드캐스팅 및 로컬 멀티캐스팅 (Broadcasting and Local Multicasting)](chapter9.md)**
    *   **내용:** 일대다 통신을 위한 주소 매핑, 그룹 관리 프로토콜(IGMP, MLD), 그리고 스위치에서의 스누핑(Snooping) 기술을 설명합니다.

### **4. 전송 계층 (Transport Layer)**

데이터의 전송 방식을 정의하는 UDP와 TCP를 심도 있게 다룹니다.

*   **[10장: UDP 및 IP 단편화 (User Datagram Protocol and IP Fragmentation)](chapter10.md)**
    *   **내용:** 비연결성 프로토콜인 UDP의 단순한 구조, 체크섬, 그리고 IP 패킷이 MTU보다 클 때 발생하는 단편화(Fragmentation) 과정을 다룹니다.
*   **[11장: DNS (Name Resolution and the Domain Name System)](chapter11.md)**
    *   **내용:** 호스트 이름을 IP 주소로 변환하는 DNS의 계층 구조, 메시지 포맷, 리소스 레코드 유형, 존 전송 및 동적 업데이트를 설명합니다.

### **5. TCP 심화 (TCP Detailed)**

인터넷에서 가장 복잡하고 중요한 프로토콜인 TCP를 6개 장에 걸쳐 상세히 분석합니다.

*   **[12장: TCP 기초 (TCP Preliminaries)](chapter12.md)**
    *   **내용:** 신뢰성 있는 전송을 위한 ARQ, 슬라이딩 윈도우 개념, TCP 헤더 구조 및 옵션 등 기본 이론을 소개합니다.
*   **[13장: TCP 연결 관리 (TCP Connection Management)](chapter13.md)**
    *   **내용:** 연결 수립(3-way handshake)과 종료(4-way handshake), 상태 천이(TIME_WAIT 등), 리셋(RST) 처리 등을 다룹니다.
*   **[14장: TCP 타임아웃과 재전송 (TCP Timeout and Retransmission)](chapter14.md)**
    *   **내용:** RTT 측정 및 RTO(재전송 타이머) 설정 알고리즘, 빠른 재전송(Fast Retransmit), SACK(선택적 확인 응답) 기반 복구 등을 설명합니다.
*   **[15장: TCP 데이터 흐름과 윈도우 관리 (TCP Data Flow and Window Management)](chapter15.md)**
    *   **내용:** 상호작용 데이터(Nagle 알고리즘) 처리, 윈도우 광고를 통한 흐름 제어, 실리 윈도우 신드롬(SWS) 회피 등을 다룹니다.
*   **[16장: TCP 혼잡 제어 (TCP Congestion Control)](chapter16.md)**
    *   **내용:** 네트워크 혼잡을 방지하기 위한 슬로우 스타트, 혼잡 회피, 빠른 회복 알고리즘과 NewReno, CUBIC 등의 발전된 알고리즘을 다룹니다.
*   **[17장: TCP 킵얼라이브 (TCP Keepalive)](chapter17.md)**
    *   **내용:** 유휴 상태의 연결을 유지하거나 죽은 연결을 정리하기 위한 킵얼라이브 메커니즘을 설명합니다.

### **6. 보안 (Security)**

*   **[18장: 보안 프로토콜 (Security: EAP, IPsec, TLS, DNSSEC, and DKIM)](chapter18.md)**
    *   **내용:** 네트워크 보안의 원칙, 암호화 기초, 그리고 각 계층별 주요 보안 프로토콜(IPsec, TLS, DNSSEC 등)을 종합적으로 다룹니다.