---
title: quiz_network
tags: []
aliases: []
date modified: 2026-02-26 14:27:53 +09:00
date created: 2026-02-25 10:46:47 +09:00
---

## 🛡️ 정보보안기사 실기 Quiz

### 2. 네트워크 보안

#### 📝 단답형

<details>
<summary>IP 관리 시스템에서 발전하여 MAC 주소를 기반으로 네트워크 접근 제어 및 인증 기능을 수행하는 보안 시스템의 명칭을 쓰시오.</summary>
<blockquote>
NAC (Network Access Control)
</blockquote>
</details>

<details>
<summary>Tcpdump와 같은 도구로 패킷을 스니핑할 때, 목적지 MAC 주소가 자신의 것과 다르더라도 패킷을 폐기하지 않고 수신하기 위해 네트워크 인터페이스에 설정해야 하는 모드의 명칭을 쓰시오.</summary>
<blockquote>
무차별 모드 (Promiscuous Mode)
</blockquote>
</details>

<details>
<summary>IP 단편화(Fragmentation) 프로토콜의 취약점을 이용하여, 조각난 패킷들의 오프셋(Offset)을 겹치게(Overlap) 하거나 변조시켜 수신 측에서 재조합 시 오류와 시스템 과부하를 유발하는 분산서비스거부 공격 기법을 쓰시오.</summary>
<blockquote>
티어드롭 (Teardrop) 공격
</blockquote>
</details>

<details>
<summary>2016년에 처음 발견되었으며, 패스워드가 취약한 IP 카메라, 공유기 등 IoT 장비를 스캐닝하여 악성코드에 감염시킨 후 거대한 봇넷(Botnet)을 형성해 DDoS 공격을 수행하는 대표적 공격용 봇넷의 명칭을 쓰시오.</summary>
<blockquote>
미라이 (Mirai) 봇넷
</blockquote>
</details>

<details>
<summary>점차 고도화되는 보안 위협에 대처하기 위해 이기종 보안 장비 및 솔루션들을 하나의 시스템으로 통합 연동하고, 위협 탐지 및 대응, 침해 사고 등 보안 운영 업무를 '자동화'함으로써 효율성을 극대화하는 플랫폼 또는 기술의 명칭을 영문 약어로 쓰시오.</summary>
<blockquote>
SOAR (Security Orchestration, Automation and Response)
</blockquote>
</details>

<details>
<summary>무선 인증 구조 IEEE 802.1x 에서 AP(Access Point)가 인증 요청을 전달하고 실제 사용자의 권한을 검증하는 서버 프로토콜로 자주 사용되는 인증 서버의 명칭을 쓰시오.</summary>
<blockquote>
RADIUS (또는 TACACS+)
</blockquote>
</details>

<details>
<summary>가상사설망(VPN) 환경에서 IP 패킷의 암호화 및 무결성을 보장하기 위해 주로 사용되며, 네트워크 계층에서 동작하는 널리 알려진 보안 프로토콜 모음(Suite)의 명칭을 쓰시오.</summary>
<blockquote>
IPsec (IP Security)
</blockquote>
</details>

#### ✍️ 서술형

<details>
<summary>IPsec의 터널 모드(Tunnel Mode)와 전송 모드(Transport Mode)의 차이점을 패킷 구조 관점에서 서술하시오.</summary>
<blockquote>
전송 모드는 원래 IP 헤더 뒤에 AH나 ESP 헤더를 삽입하여 데이터(페이로드)만 보호하지만, 터널 모드는 원래의 패킷 전체를 암호화(보호)하고 새로운 외부 IP 헤더를 추가하여 캡슐화한다
</blockquote>
</details>

<details>
<summary>ARP 스푸핑(Spoofing) 공격의 원리를 설명하고, 이 공격이 네트워크 계층(Layer 3)이 아닌 데이터 링크 계층(Layer 2)의 보안 문제인 이유를 기술하시오.</summary>
<blockquote>
원리: 공격자가 로컬 네트워크 상에서 자신의 MAC 주소를 희생자의 IP 주소와 매칭시킨 위조된 ARP 응답 패킷을 지속적으로 전송하여, 희생자의 ARP 캐시 테이블을 오염시키고 패킷을 가로채는 공격이다.<br>
이유: ARP 프로토콜은 IP 주소를 MAC 주소(L2 주소)로 대응시키는 기능을 수행하며, 인증 절차 없이 응답 패킷을 신뢰하는 이더넷(Ethernet) 환경의 구조적 결함을 이용하기 때문이다.
</blockquote>
</details>

<details>
<summary>IPsec(IP Security) 프로토콜의 두 가지 모드(전송 모드, 터널 모드)와 두 가지 프로토콜(AH, ESP)의 조합에 따른 보안 서비스 제공 차이점을 서술하시오.</summary>
<blockquote>
전송 모드: 원래의 IP 헤더는 유지하고 데이터 부분만 보호하며, 종단 간(End-to-End) 통신에 사용된다.<br>
터널 모드: 원래 패킷 전체를 캡슐화하여 새로운 IP 헤더를 추가하며, 게이트웨이 간(Site-to-Site) VPN 구축에 사용된다.<br>
AH: 데이터의 무결성과 인증은 제공하지만 암호화(기밀성)는 제공하지 않는다.<br>
ESP: 무결성, 인증과 함께 데이터 암호화를 통한 기밀성을 제공한다.
</blockquote>
</details>

<details>
<summary>쿠키 스니핑이나 세션 하이재킹과 같이 네트워크 상에서 평문으로 전송되는 인증 정보를 가로채는 공격을 방어하기 위해 웹 서버 통신에서 필수적으로 적용해야 하는 프로토콜을 쓰고, 그 원리를 간략히 서술하시오.</summary>
<blockquote>
<strong>프로토콜</strong>: HTTPS (또는 SSL/TLS)<br>
<strong>원리</strong>: 애플리케이션 계층과 전송 계층 사이에서 클라이언트와 서버 간의 데이터 전송 구간 전체를 공개키(비대칭키) 알고리즘 방식과 공유키(대칭키) 알고리즘 방식을 함께 사용하여 암호화하므로, 패킷이 도청 유출되더라도 내용을 해독할 수 없어 기밀성을 완벽히 보장한다.
</blockquote>
</details>

<details>
<summary>출발지 IP 주소를 공격 대상의 외부 IP 주소로 위조(Spoofing)하고 목적지 IP 주소를 브로드캐스트 주소로 설정하여 다수의 시스템이 일제히 공격 대상에게 ICMP Echo Reply 응답을 보내 시스템을 마비시키도록 유도하는 공격의 명칭을 쓰고, 그 대응 방안을 라우터 설정 측면에서 설명하시오.</summary>
<blockquote>
<strong>공격 명칭</strong>: 스머프 (Smurf) 공격<br>
<strong>라우터 대응 방안</strong>: 라우터에서 브로드캐스트 패킷의 망 내 진입을 원천 차단하기 위해 Direct Broadcast 패킷 수신 허용 옵션을 비활성화(예: <code>no ip directed-broadcast</code>) 하도록 설정한다.
</blockquote>
</details>

<details>
<summary>내부 네트워크 보호를 위해 방화벽(Firewall)을 구축할 때 사용하는 방식 중, 패킷 필터링(Packet Filtering)과 상태 기반 검사(Stateful Inspection)의 차이점을 보안성과 성능 측면에서 비교 서술하시오.</summary>
<blockquote>
<strong>패킷 필터링</strong>: 네트워크 계층(IP, Port 등)의 헤더 정보만을 단순히 검사하여 차단하므로 처리 속도가 매우 빠르지만, 데이터 내부(Payload)의 내용이나 세션 연결 상태를 추적하지 않아 IP 스푸핑 등 우회 공격에 취약하다.<br>
<strong>상태 기반 검사 (Stateful Inspection)</strong>: 패킷 필터링의 단점을 보완하여, 연결이 성립된 세션의 상태표(State Table)를 유지·추적함으로써, 인가된 세션에 속한 패킷들만 통과시키므로 보안성이 우수하다. 그러나 모든 세션을 추적해야 하므로 메모리와 CPU 자원 소모가 패킷 필터링보다 크다.
</blockquote>
</details>

<details>
<summary>라우팅 경로를 추적하여 네트워크 장애 지점이나 중간 경유 노드를 파악하기 위해 사용하는 진단 유틸리티 명령어(Windows와 Linux 환경 각각)를 쓰고, 이 도구가 사용하는 프로토콜 및 원리를 간략히 설명하시오.</summary>
<blockquote>
<strong>명령어</strong>: Windows에서는 <code>tracert</code>, Linux에서는 <code>traceroute</code><br>
<strong>사용 프로토콜 및 원리</strong>: ICMP(또는 UDP) 패킷을 사용한다. IP 패킷의 헤더 중 TTL(Time to Live) 값을 1부터 순차적으로 증가시키며 전송하고, 패킷이 라우터를 거칠 때마다 TTL이 0이 되면 반환되는 ICMP Time Exceeded 에러 메시지를 수신하여 경유하는 라우터 정보를 점진적으로 알아낸다.
</blockquote>
</details>

#### 💻 실기형 (실무형)

<details>
<summary>ARP 스푸핑(Spoofing) 공격을 방어하기 위해 ARP 테이블을 정적으로 관리하는 명령어를 작성하시오.</summary>
<blockquote>
arp -s [IP주소] [MAC주소]
</blockquote>
</details>
