---
title: 문제모음
tags: []
aliases: []
date modified: 2026-02-25 11:28:51 +09:00
date created: 2026-02-25 10:46:47 +09:00
---

## 🛡️ 정보보안기사 실기 Quiz

### 1. 시스템 보안

<details>
<summary>디스크 스케줄링 중 '엘리베이터 알고리즘'의 명칭은?</summary>
<blockquote>
SCAN 알고리즘<br>
- 원리: 한쪽 끝에서 반대쪽 끝으로 이동하며 경로상의 모든 요청을 처리함.
</blockquote>
</details>

<details>
<summary>IP 관리 시스템에서 발전하여 MAC 기반 통제를 강화한 장비는?</summary>
<blockquote>
NAC (Network Access Control)
- 주요 기능: 접근 제어 및 인증.
</blockquote>
</details>

<details>
<summary>윈도우 시스템에서 사용자 계정 및 패스워드 정보를 암호화하여 저장하는 데이터베이스의 명칭과 해당 파일이 저장되는 레지스트리 경로를 작성하시오.</summary>
<blockquote>
SAM (Security Account Manager), HKEY_LOCAL_MACHINE\SAM
</blockquote>
</details>

<details>
<summary>윈도우에서 지원하는 볼륨 단위 암호화 기능인 BitLocker의 특징 2가지를 서술하시오.</summary>
<blockquote>
1. 윈도우 운영체제에서 제공하는 볼륨 단위 암호화 기능이다.<br>2. 컴퓨터 부팅에 필요한 시스템 파티션 부분까지 암호화하여 보호할 수 있다.
</blockquote>
</details>

<details>
<summary>사용자 계정의 패스워드를 알아내기 위해 가능한 모든 조합을 시도하는 공격 기법과, 의미 있는 단어가 담긴 파일을 대입하는 공격 기법의 명칭을 각각 쓰시오.</summary>
<blockquote>
무차별 대입 공격 (Brute-Force Attack), 사전 공격 (Dictionary Attack)
</blockquote>
</details>

<details>
<summary>리눅스 시스템 로그 중 다음 설명에 해당하는 로그 파일명을 작성하시오.<br>(가) 사용자의 원격 로그인 정보 저장<br>(나) 시스템 부팅 관련 메시지 저장<br>(다) 사용자가 로그인한 마지막 로그 저장</summary>
<blockquote>
(가) 사용자의 원격 로그인 정보 저장: `/var/log/secure`<br>(나) 시스템 부팅 관련 메시지 저장: `/var/log/dmesg`<br>(다) 사용자가 로그인한 마지막 로그 저장: `/var/log/lastlog`
</blockquote>
</details>

<details>
<summary>리눅스의 부팅 과정 중 발생할 수 있는 보안 위협을 방지하기 위해 사용되는 '싱글 모드(Single Mode) 진입 시 패스워드 설정'의 필요성과 설정 방법을 설명하시오.</summary>
<blockquote>
싱글 모드는 루트(root) 권한으로 비밀번호 없이 시스템에 접근하여 설정을 변경할 수 있는 모드이므로, 물리적 접근이 가능한 공격자가 관리자 권한을 탈취하는 것을 방지하기 위해 비밀번호 설정이 필수적이다. `/etc/sysconfig/init` 파일 내의 `SINGLE` 설정을 수정하거나, GRUB 부트로더에 `password`를 설정하여 인증 절차를 강화할 수 있다.
</blockquote>
</details>

<details>
<summary>윈도우 시스템에서 'SAM(Security Account Manager) 파일'의 정의를 쓰고, 이 파일에 대한 공격을 차단하기 위해 적용할 수 있는 보안 대책 2가지를 서술하시오.</summary>
<blockquote>
정의: 사용자 계정 및 암호화된 패스워드 정보를 저장하고 있는 윈도우 레지스트리 데이터베이스이다.<br><br>
보안 대책:<br>
1. 'SAM 계정과 공유의 익명 열거 허용 안 함' 정책을 설정하여 공격자가 계정 정보를 수집하지 못하도록 차단한다.<br>
2. Syskey 등을 사용하여 시스템 부팅 시 추가적인 암호화 키를 요구하도록 설정한다.
</blockquote>
</details>

---
### 2. 네트워크 보안

<details>
<summary>IP 관리 시스템에서 발전하여 MAC 주소를 기반으로 네트워크 접근 제어 및 인증 기능을 수행하는 보안 시스템의 명칭을 쓰시오.</summary>
<blockquote>
NAC (Network Access Control)
</blockquote>
</details>

<details>
<summary>ARP 스푸핑(Spoofing) 공격을 방어하기 위해 ARP 테이블을 정적으로 관리하는 명령어를 작성하시오.</summary>
<blockquote>
arp -s [IP주소] [MAC주소]
</blockquote>
</details>

<details>
<summary>Tcpdump와 같은 도구로 패킷을 스니핑할 때, 목적지 MAC 주소가 자신의 것과 다르더라도 패킷을 폐기하지 않고 수신하기 위해 네트워크 인터페이스에 설정해야 하는 모드의 명칭을 쓰시오.</summary>
<blockquote>
무차별 모드 (Promiscuous Mode)
</blockquote>
</details>

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

---
### 3. 애플리케이션 보안

<details>
<summary>전자상거래 지불 프로토콜에서 주문 정보와 지불 정보를 각각 해시한 후 이를 합쳐 다시 해시하여 서명함으로써, 상점은 지불 정보를 알 수 없고 은행은 주문 내용을 알 수 없게 만드는 기술의 명칭을 쓰시오.</summary>
<blockquote>
이중 서명 (Dual Signature)
</blockquote>
</details>

<details>
<summary>사용자의 입력값을 적절히 필터링하지 못해 악성 스크립트가 실행되는 XSS 공격 중, 게시판 등에 스크립트를 저장하여 지속적으로 피해를 입히는 방식의 명칭을 쓰시오.</summary>
<blockquote>
Stored XSS (저장형 XSS)
</blockquote>
</details>

<details>
<summary>안드로이드 앱의 필수 권한 선언 및 앱 구성 정보를 담고 있는 설정 파일의 명칭을 작성하시오.</summary>
<blockquote>
AndroidManifest.xml
</blockquote>
</details>

<details>
<summary>파일 전송 프로토콜 중 FTP보다 단순하며 별도의 인증 절차가 없어 보안에 취약하지만, 부팅 파일 전송 등에 사용되는 프로토콜의 명칭을 쓰시오.</summary>
<blockquote>
TFTP (Trivial File Transfer Protocol)
</blockquote>
</details>

<details>
<summary>SQL 인젝션(Injection) 공격 중 'Blind SQL Injection'의 개념을 설명하고, 이를 탐지하기 위해 공격자가 주로 사용하는 SQL 함수 2가지를 쓰시오.</summary>
<blockquote>
개념: 쿼리 결과가 화면에 직접 노출되지 않는 경우, 참(True) 또는 거짓(False)의 응답 차이나 응답 지연 시간 등을 통해 데이터베이스의 정보를 유추해 나가는 공격 기법이다.<br>
사용 함수: `SUBSTR()` (문자열 추출), `LENGTH()` (문자열 길이 확인), `SLEEP()` (시간 지연 유도) 등.
</blockquote>
</details>

<details>
<summary>안드로이드 애플리케이션 보안을 위해 소스코드 난독화(Obfuscation)를 수행해야 하는 이유를 리버스 엔지니어링(Reverse Engineering) 관점에서 설명하시오.</summary>
<blockquote>
안드로이드 앱은 디컴파일 도구를 통해 실행파일(.apk)을 소스코드로 쉽게 변환할 수 있어 로직 분석이 용이하다. 난독화는 변수명이나 메서드명을 무의미하게 변경하거나 코드 흐름을 복잡하게 만들어, 공격자가 화이트박스 분석을 통해 취약점을 찾아내거나 소스코드를 도용하는 리버스 엔지니어링 시도를 어렵게 하기 위해 반드시 필요하다.
</blockquote>
</details>

---
### 4. 정보보안 일반 및 관리 법규

<details>
<summary>사용자가 통계적 데이터로부터 개별 항목에 대한 정보를 추론해 내는 보안 위협의 명칭을 작성하시오.</summary>
<blockquote>
추론 (Inference)
</blockquote>
</details>

<details>
<summary>정보보호 관리체계(ISMS)의 수립 및 운영을 위한 국제 표준 번호를 작성하시오.</summary>
<blockquote>
ISO/IEC 27001
</blockquote>
</details>

<details>
<summary>디지털 포렌식의 5대 원칙 중 '동일한 환경에서 분석했을 때 반드시 동일한 결과가 도출되어야 한다'는 원칙의 명칭을 쓰시오.</summary>
<blockquote>
재현의 원칙
</blockquote>
</details>

<details>
<summary>위험 처리 전략 중 4가지 유형(감소, 회피, 전가, 수용)을 나열하고 각각의 의미를 간략히 설명하시오.</summary>
<blockquote>
1. 위험 감소: 보안 장비 도입 등 대책을 강구하여 위험 발생 가능성이나 영향을 낮춤.<br>
2. 위험 회피: 위험이 존재하는 프로세스나 활동을 중단함.<br>
3. 위험 전가: 보험 가입이나 외주 등을 통해 위험의 책임을 제3자에게 넘김.<br>
4. 위험 수용: 현재 위험 수준이 낮아 별도의 대책 없이 위험을 받아들임.
</blockquote>
</details>

<details>
<summary>공공기관이나 기업에서 정보보호 관리체계(ISMS)를 수립할 때 수행하는 '위험 분석(Risk Analysis)'의 4단계 절차를 순서대로 작성하시오.</summary>
<blockquote>
1. 자산 식별: 조직의 정보자산(H/W, S/W, 데이터 등)을 식별하고 중요도를 산정한다.<br>
2. 위협 및 취약점 분석: 자산에 영향을 줄 수 있는 내·외부 위협 요인과 시스템의 약점을 식별한다.<br>
3. 위험 평가: 식별된 위험을 기반으로 발생 가능성과 영향을 계산하여 위험도를 산정한다.<br>
4. 정보보호대책 수립: 목표 위험 수준을 초과하는 위험에 대해 적절한 보호 대책과 이행 계획을 수립한다.
</blockquote>
</details>

<details>
<summary>디지털 포렌식(Digital Forensics)의 '연계 보관성(Chain of Custody) 원칙'에 대해 설명하고, 이를 보장하기 위해 증거물 획득 단계에서 수행해야 할 조치를 서술하시오.</summary>
<blockquote>
원칙: 증거물이 수집된 순간부터 법정에 제출될 때까지 모든 이동 및 관리 경로가 기록되어 위·변조가 없었음을 입증해야 한다는 원칙이다.<br>
조치: 증거물 획득 시 원본 매체의 해시(Hash) 값을 산출하여 기록하고, 증거물 봉인 및 이송 시 담당자 서명을 포함한 인수인계 증명서를 작성하여 관리해야 한다.
</blockquote>
</details>
