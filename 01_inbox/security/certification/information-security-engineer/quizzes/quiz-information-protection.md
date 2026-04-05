---
title: quiz-information-protection
tags: [정보보안기사, 정보보안실기, 정보보호일반]
aliases: []
date modified: 2026-04-05 17:47:31 +09:00
date created: 2026-02-25 10:46:47 +09:00
---

## [17] 정보보안 일반/관리

<details>
<summary>(단답형) 클라이언트와 서버 사이에서 요청을 중계하며, 클라이언트의 IP 주소를 숨기고 캐싱 기능을 통해 성능을 향상시키는 역할을 수행하는 서버는?</summary>
<blockquote>
<strong>정답:</strong> <strong>프록시 서버 (Proxy Server)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 중앙 집중식 서버 없이 네트워크 참여자들이 공동으로 거래 정보를 기록하고 검증하며, '분산 원장 방식(Distributed Ledger)'을 사용하는 기술은?</summary>
<blockquote>
<strong>정답:</strong> <strong>블록체인 (Blockchain)</strong>
</blockquote>
</details>

<details>
<summary>(서술형) 블록체인에서 한 번 기록된 데이터의 위·변조가 사실상 불가능한 기술적 이유(무결성 원리)를 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> 각 블록은 이전 블록의 해시값을 포함하여 체인 형태로 연결되어 있다. 특정 블록의 데이터를 수정하면 해당 블록의 해시값이 변하고, 그 이후의 모든 블록 해시값도 순차적으로 변하기 때문에 네트워크 참여자 과반수의 동의 없이 위조를 수행하는 것이 계산적으로 불가능하기 때문이다.
</blockquote>
</details>

<details>
<summary>(단답형) 비트코인 등에서 사용하는 합의 알고리즘으로, 복잡한 해시 연산을 수행하여 가장 먼저 정답을 찾은 노드에게 블록 생성 권한과 보상을 부여하는 방식은?</summary>
<blockquote>
<strong>정답:</strong> <strong>작업 증명 (PoW: Proof of Work)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 블록체인 네트워크에서 새로운 블록을 생성하기 위해 작업 증명(PoW) 등의 연산을 수행하는 행위를 무엇이라 하는가?</summary>
<blockquote>
<strong>정답:</strong> <strong>채굴 (Mining)</strong>
</blockquote>
</details>

### 정보보호 개요

<details>
<summary>(단답형) 해커가 기업의 내부 네트워크에 침투한 뒤 들키지 않고 장기간에 걸쳐 지속적이고 다양한 공격 기법을 동원하여 은밀하게 기밀 정보를 유출하는 표적형 해킹 패러다임의 영문 약어를 쓰시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>APT (Advanced Persistent Threat)</strong>
</blockquote>
</details>

<details>
<summary>[764] (단답형) 정보보호의 3대 요소(CIA) 중, 인가된 사용자만이 정보에 접근할 수 있도록 보장하는 요소는 무엇인가?</summary>
<blockquote>
<strong>정답:</strong> <strong>기밀성 (Confidentiality)</strong>
</blockquote>
</details>

<details>
<summary>[764] (단답형) 정보보호의 3대 요소 중, 부적절한 변경이나 파괴로부터 정보를 보호하여 정확성과 완전성을 보장하는 요소는 무엇인가?</summary>
<blockquote>
<strong>정답:</strong> <strong>무결성 (Integrity)</strong>
</blockquote>
</details>

<details>
<summary>[764] (단답형) 정보보호의 3대 요소 중, 서비스가 필요한 시점에 인가된 사용자가 지체 없이 정보나 자원을 사용할 수 있도록 보장하는 요소는 무엇인가?</summary>
<blockquote>
<strong>정답:</strong> <strong>가용성 (Availability)</strong>
</blockquote>
</details>

<details>
<summary>[764] (서술형) 정보보호 서비스 중 '부인 방지(Non-repudiation)'의 개념과 이를 구현하기 위한 대표적인 기술을 기술하시오.</summary>
<blockquote>
<strong>정답:</strong>
- 개념: 메시지를 송신하거나 수신한 주체가 나중에 그 사실을 부인하지 못하도록 증명하는 서비스이다.
- 기술: 전자서명 (Digital Signature), 공인인증서 등
</blockquote>
</details>

<details>
<summary>[764] (서술형) 정보보안의 '책임 추적성(Accountability)'을 확보하기 위해 시스템에서 반드시 수행되어야 하는 관리적/기술적 조치사항을 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> 개별 사용자의 활동을 식별할 수 있는 고유 식별자(ID)를 부여하고, 접속 기록, 작업 내역 등을 포함한 모든 행위를 감사 로그(Audit Log)로 기록하여 주기적으로 점검해야 한다.
</blockquote>
</details>

<details>
<summary>[768] (단답형) 두 사용자 간에 사전에 공유된 비밀 키가 없는 상태에서, 공개된 통신 채널을 통해 안전하게 공통의 세션 키를 생성할 수 있도록 고안된 최초의 알고리즘은?</summary>
<blockquote>
<strong>정답:</strong> <strong>디피-헬먼 (Diffie-Hellman) 키 교환 알고리즘</strong>
</blockquote>
</details>

<details>
<summary>[768] (서술형) 디피-헬먼 키 교환 알고리즘의 안전성을 담보하는 수학적 원리는 무엇인가?</summary>
<blockquote>
<strong>정답:</strong> <strong>이산대수 문제 (Discrete Logarithm Problem)</strong>의 계산 복잡성을 근거로 한다. 즉, $g^x \mod p = y$에서 $g, p, y$가 주어졌을 때 지수 $x$를 찾아내는 것이 매우 어렵다는 점을 이용한다.
</blockquote>
</details>

<details>
<summary>[768] (서술형) 디피-헬먼 키 교환 방식이 가지고 있는 치명적인 보안 약점 한 가지와 그 해결 방안을 기술하시오.</summary>
<blockquote>
<strong>정답:</strong>
- 약점: 중간자 공격(Man-In-The-Middle Attack, MITM)에 취약하다. 상대방의 신원을 확인하는 인증 기능이 없기 때문에 공격자가 중간에서 각각과 키 교환을 수행하여 통신을 가로챌 수 있다.
- 해결 방안: 전자서명이나 공개키 인증서(PKI)를 결합하여 사용자 인증 단계를 추가한다.
</blockquote>
</details>

<details>
<summary>[768] (작업형) 디피-헬먼 알고리즘에서 엘리스(Alice)가 $g^a \mod p$를 전송하고, 밥(Bob)이 $g^b \mod p$를 전송했을 때, 두 사람이 최종적으로 공유하게 되는 키 $K$를 산출하는 수식을 기술하시오.</summary>
<blockquote>
<strong>정답:</strong> $K = (g^b)^a \mod p = (g^a)^b \mod p = g^{ab} \mod p$
</blockquote>
</details>

<details>
<summary>[768] (단답형) 세션 키가 노출되더라도 과거에 통신한 다른 세션들의 기밀성이 유지되도록 보장하는 암호학적 성질을 무엇이라 하는가?</summary>
<blockquote>
<strong>정답:</strong> <strong>완전 순방향 비밀성 (PFS: Perfect Forward Secrecy)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 정보보호의 개념 중, 주체가 해당 정보를 볼 권한이 있더라도 업무 수행을 위해 꼭 필요한 경우에만 접근하도록 제한하는 원칙은?</summary>
<blockquote>
<strong>정답:</strong> <strong>알 필요성 (Need-to-Know) 원칙</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 가용성을 확보하기 위하여 동일한 서비스를 제공하는 여러 서버를 하나의 그룹으로 묶어 일부 서버에 장애가 발생해도 중단 없이 서비스를 제공하는 기술은?</summary>
<blockquote>
<strong>정답:</strong> <strong>서버 클러스터링 (Server Clustering)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 여러 개의 디스크를 중복 배열하여 일부 디스크 장애 시에도 정보의 손실을 방지하고 가용성을 높이는 기술의 약칭은?</summary>
<blockquote>
<strong>정답:</strong> <strong>RAID (Redundant Array of Inexpensive Disks)</strong>
</blockquote>
</details>

<details>
<summary>(서술형) 정보보호의 목표 중 <strong>무결성(Integrity)</strong>을 보장하기 위해 사용되는 암호학적 도구 3가지를 기술하시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>암호학적 해시 함수</strong>, <strong>메시지 인증 코드 (MAC)</strong>, <strong>디지털 서명 (전자서명)</strong>
</blockquote>
</details>

<details>
<summary>(서술형) 정보보호의 목표 중 <strong>인증성(Authenticity)</strong>을 '사용자 인증'과 '메시지 인증'의 관점에서 구분하여 설명하시오.</summary>
<blockquote>
<strong>정답:</strong><br>
1. <strong>사용자 인증</strong>: 정보 자산에 접근하는 주체(사용자)의 신원이 주장된 실체와 일치함을 보장하는 것 (지식/소유/생체 기반 인증 등 사용)<br>
2. <strong>메시지 인증</strong>: 수신한 메시지가 제3자가 아닌 올바른 송신자가 보낸 메시지임을 보장하는 것 (MAC, 디지털 서명 등 사용)
</blockquote>
</details>

<details>
<summary>(단답형) 사고나 재해에 대비하여 백업된 데이터를 원본과 물리적으로 떨어진 원격지에 보관하는 관리 방식을 무엇이라 하는가?</summary>
<blockquote>
<strong>정답:</strong> <strong>소산 관리</strong>
</blockquote>
</details>

<details>
<summary>(작업형) 다음 중 성격이 다른 보안 기술 또는 기법 하나를 고르시오.<br>
(가) 장비 이중화, (나) RAID 구성, (다) 백업 및 소산 관리, (라) 일항향 해시 함수 적용</summary>
<blockquote>
<strong>정답:</strong> <strong>(라) 일방향 해시 함수 적용</strong><br>
(※ (가), (나), (다)는 가용성 확보를 위한 기법이며, (라)는 무결성 확보를 위한 기법임)
</blockquote>
</details>

<details>
<summary>(작업형) 메시지 전송 시 <strong>무결성</strong>, <strong>송신처 인증(메시지 인증)</strong>, 그리고 <strong>부인방지</strong> 기능을 한 번에 제공할 수 있는 가장 대표적인 암호학적 수단은?</summary>
<blockquote>
<strong>정답:</strong> <strong>디지털 서명 (또는 전자서명)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 정보보호산업법에 따른 정보보호의 정의에는 정보의 훼손·변조·유출 방지뿐만 아니라, 사고 발생 시의 대응을 위한 어떤 활동이 포함되어 있는가?</summary>
<blockquote>
<strong>정답:</strong> <strong>복구 (Recovery)</strong>
</blockquote>
</details>

### 접근통제(접근제어, Access Control)

<details>
<summary>(기출 25회 5번 문제) (단답형) 보안 통제(Security Control)는 그 역할과 시점에 따라 예방, 탐지, 교정 통제로 나눌 수 있으며, 구현 방식에 따라 물리적, 기술적, 관리적 통제로 분류된다. 다음 ( )에 알맞은 통제 유형을 쓰시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
1. 사고가 발생하기 전에 미리 방지하여 잠재적인 손실을 줄이는 통제: <code>( A )</code><br>
2. 자산에 대한 물리적 접근을 차단하기 위한 시설물이나 경비원 등의 배치: <code>( B )</code> 통제<br>
3. 접근 제어 시스템, 암호화, IDS/IPS 등 시스템에 직접 적용되는 보안 기술: <code>( C )</code> 통제(또는 논리적 통제)
</div>
</summary>
<blockquote>
(A) <strong>예방</strong> (Preventive) 통제<br>
(B) <strong>물리적</strong> (Physical) 통제<br>
(C) <strong>기술적</strong> (Technical) 통제 (또는 논리적 통제)
</blockquote>
</details>

<details>
<summary>(단답형) 공개키 기반 구조(PKI)에서 사용자 인증서의 유효기간이 만료되기 전 사용자 퇴사, 비밀키 유출 등의 이유로 해당 인증서를 사용할 수 없게 되었을 때 인증기관(CA)이 발행하는 폐기된 인증서 목록의 명칭을 영문 약어로 쓰시오.</summary>
<blockquote>
CRL (Certificate Revocation List)
</blockquote>
</details>

<details>
<summary>(서술형) 사용자 인증 방식 중 '지식 기반(What you know)', '소유 기반(What you have)', '생체 기반(Who you are)' 인증의 개념을 각각 설명하고, 이들 중 두 가지 이상을 조합하여 보안성을 높이는 '다중 인증(MFA/2FA)' 방식 중 금융권에서 자주 사용하는 OTP(One Time Password)가 강한 보안을 제공하는 이유를 서술하시오.</summary>
<blockquote>
<strong>지식 기반</strong>: 패스워드나 PIN처럼 사용자의 머릿속에 기억된 정보를 확인하는 방식이다.<br>
<strong>소유 기반</strong>: 스마트카드나 휴대폰처럼 사용자가 물리적으로 소유한 매체를 확인하는 방식이다.<br>
<strong>생체 기반</strong>: 지문이나 홍채처럼 사용자의 고유한 신체적 특성을 확인하는 방식이다.<br><br>
<strong>OTP의 강력한 보안 이유</strong>: OTP는 일회용 비밀번호로, 생성된 패스워드는 단 한 번만 사용 가능하며 일정 시간이 지나면 무효화(Time-based)되거나 횟수(Event-based) 기반으로 변경된다. 따라서 공격자가 네트워크 스니핑 등으로 패스워드를 가로채더라도 재사용 공격(Replay Attack)을 할 수 없기 때문이다.
</blockquote>
</details>

<details>
<summary>(서술형) 대칭키 암호 알고리즘과 비대칭키(공개키) 암호 알고리즘의 장점을 결합하여 통신의 효율성과 기밀성을 함께 확보하는 방식을 설명하시오.</summary>
<blockquote>
데이터 암호화/복호화 속도가 빠른 '대칭키'를 생성하여 대용량의 실제 데이터를 암호화하는 데 사용하고, 이 대칭키를 안전하게 전송하기 위해 키 분배 기능이 뛰어난 수신자의 '비대칭키(공개키)'로 해당 대칭키를 암호화하여 통신하는 하이브리드(Hybrid) 암호화 방식을 사용한다.
</blockquote>
</details>

### 암호학 및 키 관리

<details>
<summary>[774] (서술형) 사용자 인증의 4가지 유형(지식, 소유, 생체, 위치)을 정의하고 각각의 구체적인 예시를 한 가지씩 제시하시오.</summary>
<blockquote>
<strong>정답:</strong>
1. 지식 기반(What you know): 사용자가 기억하는 정보 (예: 패스워드, PIN)
2. 소유 기반(What you have): 사용자가 가지고 있는 매체 (예: 스마트카드, OTP 토큰)
3. 생체 기반(Who you are): 사용자의 고인한 신체적 특성 (예: 지문, 홍채)
4. 위치 기반(Where you are): 사용자의 현재 물리적 위치 (예: GPS, 접속 IP 대역)
</blockquote>
</details>

<details>
<summary>[773] (단답형) 생체 인식 시스템에서 인가되지 않은 사용자를 인가된 사용자로 잘못 판단하여 접근을 허용할 확률을 의미하는 용어는?</summary>
<blockquote>
<strong>정답:</strong> <strong>오인식률 (FAR: False Acceptance Rate)</strong>
</blockquote>
</details>

<details>
<summary>[773] (단답형) 생체 인식 시스템의 성능 지표 중, FAR과 FRR(오거부율)이 같아지는 지점을 의미하며 시스템의 전반적인 정확도를 평가하는 척도는?</summary>
<blockquote>
<strong>정답:</strong> <strong>CER (Crossover Error Rate)</strong> 또는 <strong>EER (Equal Error Rate)</strong>
</blockquote>
</details>

<details>
<summary>(서술형) 접근통제의 3단계 절차인 '식별(Identification)', '인증(Authentication)', '인가(Authorization)'의 차이점을 설명하시오.</summary>
<blockquote>
<strong>정답:</strong>
- 식별: 사용자가 자신이 누구라고 주장하는 단계 (예: ID 입력)
- 인증: 주장하는 정보가 본인임을 증명하는 단계 (예: 패스워드 검증)
- 인가: 인증된 사용자에게 특정 자원에 대한 접근 권한을 부여하는 단계 (예: 읽기/쓰기 권한 부여)
</blockquote>
</details>

<details>
<summary>[778] (단답형) 정보보호 정책 중, 직무 수행을 위해 반드시 필요한 최소한의 정보에만 접근을 허용하는 보안 원칙은 무엇인가?</summary>
<blockquote>
<strong>정답:</strong> <strong>최소 권한의 원칙 (Least Privilege)</strong>
</blockquote>
</details><details>
<summary>(단답형) 자원을 소유한 주체(사용자)가 자신의 판단에 따라 다른 사용자에게 접근 권한을 부여하고 제한하는 접근 통제 방식은?</summary>
<blockquote>
<strong>정답:</strong> <strong>DAC (임의적 접근통제 / Discretionary Access Control)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 주체와 객체에 부여된 보안 등급(Security Level)을 비교하여 시스템에 의해 강제적으로 접근을 통제하는 방식은?</summary>
<blockquote>
<strong>정답:</strong> <strong>MAC (강제적 접근통제 / Mandatory Access Control)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 사용자의 신원보다는 조직 내에서의 직무나 책임에 따라 권한의 묶음(Role)을 부여하고 접근을 통제하는 방식은?</summary>
<blockquote>
<strong>정답:</strong> <strong>RBAC (역할 기반 접근통제 / Role-Based Access Control)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) DAC의 구현 방식 중, 자원(객체)을 기준으로 해당 자원에 접근 가능한 주체들의 목록을 표시하는 방식은?</summary>
<blockquote>
<strong>정답:</strong> <strong>ACL (접근 제어 목록 / Access Control List)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) DAC의 구현 방식 중, 주체(사용자)를 기준으로 해당 주체가 접근할 수 있는 객체들의 목록을 표시하는 방식은?</summary>
<blockquote>
<strong>정답:</strong> <strong>Capability List (자격/능력 목록)</strong>
</blockquote>
</details>

<details>
<summary>(서술형) 기밀성 보장을 위한 <strong>벨-라파듈라(BLP) 모델</strong>의 두 가지 핵심 속성을 쓰고 각각을 설명하시오.</summary>
<blockquote>
<strong>정답:</strong><br>
1. <strong>Simple Security Property (No Read Up)</strong>: 주체는 자신보다 높은 보안 등급의 객체를 읽을 수 없다.<br>
2. <strong>Star Property (*-Property, No Write Down)</strong>: 주체는 자신보다 낮은 보안 등급의 객체에 정보를 기록할 수 없다.
</blockquote>
</details>

<details>
<summary>(서술형) 무결성 보장을 위한 <strong>비바(Biba) 모델</strong>의 두 가지 핵심 속성을 쓰고 각각을 설명하시오.</summary>
<blockquote>
<strong>정답:</strong><br>
1. <strong>Simple Integrity Axiom (No Read Down)</strong>: 주체는 자신보다 무결성 수준이 낮은 객체를 읽을 수 없다.<br>
2. <strong>Star Integrity Axiom (No Write Up)</strong>: 주체는 자신보다 무결성 수준이 높은 객체에 정보를 기록할 수 없다.
</blockquote>
</details>

<details>
<summary>(단답형) 동일한 분야의 상업적 데이터 간 이해 상충(Conflict of Interest)이 발생할 수 있는 경우, 동적으로 접근을 차단하여 기밀성을 보호하는 모델은?</summary>
<blockquote>
<strong>정답:</strong> <strong>만리장성 (Chinese Wall / Brewer-Nash) 모델</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 서로 다른 유형의 인증 요소(예: 지식 기반 + 소유 기반)를 결합하여 보안을 강화하는 방식은?</summary>
<blockquote>
<strong>정답:</strong> <strong>2-Factor 인증 (또는 Multi-Factor 인증)</strong>
</blockquote>
</details>

<details>
<summary>(서술형) 보안의 기본 원칙 중 <strong>직무 분리(Separation of Duties)</strong>의 정의와 목적을 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> 업무의 전 과정을 한 사람이 처리할 수 없도록 권한을 분산시키는 원칙으로, 내부자에 의한 부정한 행위나 의도하지 않은 실수를 방지하는 것이 목적이다.
</blockquote>
</details>

<details>
<summary>(작업형) 다음 중 인증 유형 분류가 다른 하나를 고르시오.<br>
(가) 지문 인식, (나) 홍채 인식, (다) 안면 인식, (라) 서명(필체) 인식</summary>
<blockquote>
<strong>정답:</strong> <strong>(라) 서명(필체) 인식</strong><br>
(※ (가), (나), (다)는 신체적 특성을 이용하는 '존재 기반(Type 3)'이며, (라)는 행위적 특성을 이용하는 '행위 기반(Type 5)'임)
</blockquote>
</details>

### 정보 보호 정책

<details>
<summary>(단답형) 조직의 정보보호 목적과 활동에 관한 방향을 정의하며, 경영진의 의지가 반영된 최상위 보안 문서는?</summary>
<blockquote>
<strong>정답:</strong> <strong>정보보호 정책 (Security Policy)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 정보보호 정책 구현 요소 중, 정책 달성을 위해 필요한 구체적 요구사항을 정의하며 모든 사용자가 준수해야 하는 <strong>강제성</strong>을 가진 문서는?</summary>
<blockquote>
<strong>정답:</strong> <strong>표준 (Standards)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 정책에 따라 특정 시스템 또는 분야별 활동에 도움이 되는 사항을 설명하며, 강제성보다는 <strong>권고적이고 선택적인</strong> 성격을 가지는 문서는?</summary>
<blockquote>
<strong>정답:</strong> <strong>지침 (Guidelines)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 정책, 표준, 지침을 준수하기 위해 수행해야 할 업무들을 <strong>순서에 따라 단계적</strong>으로 상세히 설명한 문서는?</summary>
<blockquote>
<strong>정답:</strong> <strong>절차 (Procedures)</strong>
</blockquote>
</details>

<details>
<summary>(서술형) 정보보호 정책에 반드시 포함되어야 하는 핵심 내용 3가지를 기술하시오.</summary>
<blockquote>
<strong>정답:</strong><br>
1. <strong>최고경영자 등 경영진의 의지 및 방향</strong><br>
2. <strong>조직의 정보보호 역할과 책임 및 대상과 범위</strong><br>
3. <strong>관리적·기술적·물리적 정보보호 활동의 법적/행정적 근거</strong>
</blockquote>
</details>

<details>
<summary>(서술형) 정보보호 정책이 조직의 공식 문서로 인정받아 시행되기 위해 거쳐야 하는 <strong>최종적인 승인 단계</strong>에 대해 서술하시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>최고경영자(CEO)</strong> 또는 최고경영자로부터 권한을 위임받은 자(CISO 등)의 공식적인 <strong>승인</strong>을 받아야 한다.
</blockquote>
</details>

<details>
<summary>(작업형) ISMS-P 인증 기준(1.1.5 정책 수립)에 따라 정책 및 지침의 제·개정 시 수행해야 할 업무 절차를 올바른 순서대로 나열하시오.<br>
(A) 임직원 및 관련자에게 이해하기 쉬운 형태로 전달(게시판, 교육 등)<br>
(B) 이해관계자와 정책 및 시행 문서의 내용에 대해 충분한 협의 및 검토<br>
(C) 최고경영자 또는 권한 위임자로부터 공식 승인 획득</summary>
<blockquote>
<strong>정답:</strong> <strong>(B) → (C) → (A)</strong>
</blockquote>
</details>

<details>
<summary>(작업형) 다음 중 정보보호 정책의 수립 및 운영에 관한 설명으로 올바르지 않은 것은?<br>
(가) 정책은 조직의 환경에 맞게 수립되어야 하며 최상위 수준을 유지해야 한다.<br>
(나) 지침은 표준과 달리 업무의 유연성을 위해 권고적 성격을 가질 수 있다.<br>
(다) 정책 문서는 보안상 기밀이므로 승인권자 외에 평사원에게는 내용을 공개하지 않는다.<br>
(라) 정책과 지침은 제·개정 시 반드시 경영진의 승인을 받아야 한다.</summary>
<blockquote>
<strong>정답:</strong> <strong>(다)</strong><br>
(※ 해설: 수립된 정책 및 시행 문서는 모든 임직원 및 관련자가 준수할 수 있도록 이해하기 쉬운 형태로 <strong>전달 및 공유</strong>되어야 한다.)
</blockquote>
</details>

### 위험 관리

<details>
<summary>(단답형) 조직의 핵심 자산을 보호하기 위해 수용 가능한 수준의 위험도를 정의하고, 이를 유지하기 위한 일련의 분석 및 보안 대책 수립 프로세스는?</summary>
<blockquote>
<strong>정답:</strong> <strong>위험 관리 (Risk Management)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 경영진에 의해 결정되는, 조직에서 받아들일 수 있는 목표 위험 수준을 뜻하는 용어는?</summary>
<blockquote>
<strong>정답:</strong> <strong>DoA (Degree of Assurance / 수용 가능한 목표 위험 수준)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 보안 대책(Safeguard)을 구현한 후에도 사라지지 않고 여전히 남아 있는 위험을 무엇이라 하는가?</summary>
<blockquote>
<strong>정답:</strong> <strong>잔여 위험 (Residual Risk)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 위험 분석의 4대 구성 요소를 기술하시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>자산(Asset), 위협(Threat), 취약성(Vulnerability), 보호 대책(Safeguard 또는 Countermeasure)</strong>
</blockquote>
</details>

<details>
<summary>(서술형) 위험 분석 접근 전략 중 **복합 접근법(Combined Approach)**의 수행 방식과 장점을 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> 고위험(High Risk) 영역에 대해서는 상세 위험 분석을 수행하고, 그 외의 영역은 기준선 접근법을 적용하는 방식이다. 분석 비용과 자원을 효율적으로 사용하면서도 중요한 위험을 빠르게 식별하고 대처할 수 있다는 장점이 있다.
</blockquote>
</details>

<details>
<summary>(서술형) 상세 위험 분석 중 <strong>자산 식별(자산 분석)</strong> 과정에서 <strong>자산 그룹화(Asset Grouping)</strong>를 수행하는 목적을 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> 유형, 중요도, 용도 등이 유사한 자산들을 하나의 그룹으로 묶어 동일한 위험 분석 및 평가를 수행함으로써, 분석에 소요되는 시간과 비용을 최소화하기 위함이다.
</blockquote>
</details>

<details>
<summary>(단답형) 정량적 위험 분석 계산법 중, 위협이 성공했을 때의 예상 손실액(SLE)과 해당 위협의 연간 발생률(ARO)을 곱하여 연간 손해 규모를 추정하는 방식의 약어는?</summary>
<blockquote>
<strong>정답:</strong> <strong>ALE (Annual Loss Expectancy / 연간 예상 손실액)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 특정 자산가치(AV)에 위협이 발생하여 자산에 입히는 손실의 비율(%)을 지칭하는 용어와 해당 수치를 곱해 계산되는 1회 발생 시의 예상 손실액은?</summary>
<blockquote>
<strong>정답:</strong> <strong>노출 계수 (EF: Exposure Factor)</strong>, <strong>단일 예상 손실액 (SLE: Single Loss Expectancy)</strong>
</blockquote>
</details>

<details>
<summary>(서술형) 정성적 위험 분석 방법론 중 <strong>델파이법 (Delphi Method)</strong>의 핵심 수행 방식과 단점을 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> 특정 분야의 전문가 그룹을 구성하여 익명의 토론이나 설문 조사를 통해 합의된 위험 분석 결과에 도달하는 방식이다. 전문가들의 주관적인 판단에 의존하므로 객관적인 수치로 검증하기 어렵고 정확도가 낮을 수 있다는 단점이 있다.
</blockquote>
</details>

<details>
<summary>(작업형) 다음의 사례들이 설명하는 위험 처리 전략을 각각 분류하시오.<br>
(A) 자산 가치보다 보안 솔루션 도입 비용이 크므로 현재의 위험을 감수하기로 함.<br>
(B) 화재 발생 위험에 대비하여 시설 관리 업체에 해당 업무를 위탁하거나 화재 보험에 가입함.<br>
(C) 웹 서버 해킹 사고를 예방하기 위해 취약점 점검 및 보안 패치를 적용함.<br>
(D) 고위험 사업 프로세스를 아예 중단하거나 해당 자산을 매각함.</summary>
<blockquote>
<strong>정답:</strong><br>
(A): <strong>위험 수용 (Risk Acceptance)</strong><br>
(B): <strong>위험 전가 (Risk Transfer)</strong><br>
(C): <strong>위험 감소 (Risk Reduction)</strong><br>
(D): <strong>위험 회피 (Risk Avoidance)</strong>
</blockquote>
</details>

<details>
<summary>(작업형/계산) 자산가치(AV)가 10억 원인 건물에 40년에 한 번 화재(위협)가 발생할 가능성(ARO)이 있고, 화재 발생 시 자산의 약 50%가 손실(EF)될 것으로 예상된다면, 연간 예상 손실액(ALE)은 얼마인가?</summary>
<blockquote>
<strong>정답:</strong> <strong>1,250만 원</strong><br>
(※ 계산: SLE = 10억 x 0.5 = 5억 원 | ALE = 5억 x (1/40) = 1,250만 원)
</blockquote>
</details>

<details>
<summary>(서술형) 위험의 구성 요소 간의 상호관계 도표에 따르면, 위협(Threat)과 취약성(Vulnerability)이 자산(Asset)에 대해 가지는 각각의 역할을 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> 위협은 자산의 취약점을 <strong>악용(Exploit)</strong>하여 공격을 수행하며, 취약성은 자산을 위협에 <strong>노출(Expose)</strong>시키는 역할을 한다.
</blockquote>
</details>

<details>
<summary>(단답형) 보호 대책 중 '데이터 백업'이나 '재해복구센터(DRC) 운영'과 같이 이미 발생한 사고로 인한 영향을 최소화하거나 정상으로 되돌리기 위한 조치는 어떤 통제 유형에 속하는가?</summary>
<blockquote>
<strong>정답:</strong> <strong>교정 통제 (Corrective Control)</strong>
</blockquote>
</details>

<details>
<summary>[기출 19회 1번 문제] (단답형) 위험관리와 관련하여 다음 ( )에 들어갈 용어를 기술하시오.<br>
(A): 정보 자산이나 자원 자체 (보호 대상)<br>
(B): (A)에 해를 끼칠 수 있는 잠재적인 원인이나 사건<br>
(C): (B)에 의해 악용될 수 있는 (A)에 내재된 보안 약점</summary>
<blockquote>
<strong>정답:</strong> (A) <strong>자산</strong>, (B) <strong>위협</strong>, (C) <strong>취약점</strong>
</blockquote>
</details>

<details>
<summary>[기출 19회 16번 문제] (실무형) 위험평가 보고서의 항목 중 다음의 의미를 기술하시오.<br>
1) 자산 중요도 평가의 목적은?<br>
2) '우려 사항'이란 어떤 의미인가?<br>
3) '가능성'이란 어떤 의미인가?</summary>
<blockquote>
1) <strong>목적</strong>: 정보의 기밀성, 무결성, 가용성(CIA) 관점에서의 가치를 평가하여 <strong>보안 대책 수립의 우선순위</strong>를 결정하기 위함<br>
2) <strong>우려 사항</strong>: 자산에 대한 특정 위협과 취약점이 결합하여 발생할 수 있는 <strong>보안 사고 시나리오</strong><br>
3) <strong>가능성</strong>: 현재의 보안 대책 수준을 고려했을 때, 해당 보안 사고가 실제로 발생할 수 있는 확률이나 빈도
</blockquote>
</details>

<details>
<summary>[기출 20회 2번 문제] (단답형) 위험분석 방법론과 관련하여 다음 ( )에 들어갈 명칭을 쓰시오.<br>
(A): 전문가 집단을 구성하여 토론을 통해 위험을 분석 및 평가하는 방법<br>
(B): 어떤 사건도 기대대로 발생하지 않는다는 근거 하에 발생 가능한 결과들을 추정하는 방법<br>
(C): 위험 항목들의 서술적 순위를 결정하는 방법</summary>
<blockquote>
<strong>정답:</strong> (A) <strong>델파이법 (Delphi Method)</strong>, (B) <strong>시나리오법</strong>, (C) <strong>순위결정법</strong>
</blockquote>
</details>

<details>
<summary>[기출 20회 3번 문제] (단답형) 위험분석 접근 방식과 관련하여 다음 ( )에 들어갈 명칭을 쓰시오.<br>
(A): 보호의 기본 수준을 정하고 체크리스트 기반으로 보안 대책을 선택하는 방식<br>
(B): 자산, 위협, 취약성을 체계적으로 분석하여 위험을 평가하는 방식<br>
(C): 고위험 영역은 상세 위험분석을, 그 외는 베이스라인 접근법을 사용하는 방식</summary>
<blockquote>
<strong>정답:</strong> (A) <strong>베이스라인 (기준) 접근법</strong>, (B) <strong>상세 위험 분석</strong>, (C) <strong>복합 접근법</strong>
</blockquote>
</details>

<details>
<summary>[기출 12회 8번 문제] (단답형) 위험 관리 및 분석의 구성 요소와 관련된 다음 설명이 의미하는 용어를 각각 쓰시오.
1) 조직이 보호해야 할 데이터, 기기, 정보 시스템 등 가치 있는 대상: <strong>( A )</strong><br>
2) 기밀성, 무결성, 가용성을 저해할 수 있는 잠재적 원인 또는 사건: <strong>( B )</strong><br>
3) 자산의 잠재적 약점으로, 위협에 노출되어 실제 피해로 이어질 수 있는 결함: <strong>( C )</strong>
</summary>
<blockquote>
<strong>정답:</strong><br>
(A) <strong>자산 (Asset)</strong><br>
(B) <strong>위협 (Threat)</strong><br>
(C) <strong>취약성 (Vulnerability)</strong>
</blockquote>
</details>

<details>
<summary>[기출 20회 16번 문제] (서술형) 위험 대응 기법 4가지와 구체적인 사례를 설명하시오.</summary>
<blockquote>
1. <strong>위험 수용 (Accept)</strong>: 현재 위험 수준이 낮아 별도 대책 없이 그대로 감수함<br>
2. <strong>위험 감소 (Reduction)</strong>: 보안 대책을 설치하여 위험 수준을 줄임 (가치 평가: <code>감소된 ALE - 운영비용</code>)<br>
3. <strong>위험 회피 (Avoidance)</strong>: 위험이 있는 사업이나 프로세스를 중단하거나 회피함<br>
4. <strong>위험 전가 (Transfer)</strong>: 타사(보험)나 아웃소싱을 통해 책임을 떠넘김 (사례: 보험 가입, 소방 관리 위탁)
</blockquote>
</details>

<details>
<summary>[기출 21회 3번 문제] (단답형) 위험분석 관련하여 다음 물음에 답하시오.<br>
1. 수용 가능한 수준의 위험을 지칭하는 용어를 기술하시오.<br>
2. 위험이 낮으면 원칙적으로 비용 절감을 위해 그냥 두는 것이 맞는가? (O/X)</summary>
<blockquote>
1. <strong>정답:</strong> <strong>DoA (Degree of Assurance, 위험 허용 수준)</strong><br>
2. <strong>정답:</strong> <strong>X</strong> (수용 가능한 수준이어도 지속적인 모니터링이 필요함)
</blockquote>
</details>

<details>
<summary>[기출 21회 8번 문제] (단답형) 위험분석 방법과 관련하여 (A)~(C)에 들어갈 명칭을 기술하시오.<br>
(A): 전문가 집단을 구성하여 토론을 통해 분석하는 방법<br>
(B): 사건이 기대대로 발생하지 않는다는 사실에 근거하여 발생 가능한 결과를 추정하는 방법<br>
(C): 위험 요인들을 정성적 언어로 표현하여 기대 손실을 평가하는 방법</summary>
<blockquote>
<strong>정답:</strong> (A) <strong>델파이법 (Delphi Method)</strong>, (B) <strong>시나리오법</strong>, (C) <strong>퍼지행렬법 (Fuzzy Metrics)</strong>
</blockquote>
</details>

<details>
<summary>[기출 21회 15번 문제] (실무형) 정량적 위험평가 방법인 ALE(Annual Loss Expectancy)와 관련하여 다음 물음에 답하시오.<br>
1. SLE의 정의와 계산 공식을 쓰시오.<br>
2. ALE 계산을 위해 필요한 정보는?<br>
3. 투자 대비 효과인 ROI(%)를 구하는 계산식을 쓰시오. (투입 비용 X, 경감된 ALE 사용)</summary>
<blockquote>
1. <strong>SLE (Single Loss Expectancy)</strong>: 단일 보안 사고당 예상 손실액. 공식: <code>자산 가치(AV) × 노출 계수(EF)</code><br>
2. <strong>ALE 계산 필요 정보</strong>: SLE와 연간 발생률(ARO). 공식: <code>ALE = SLE × ARO</code><br>
3. <strong>ROI(%)</strong> = <code>(ALE - X) / X × 100</code>
</blockquote>
</details>

<details>
<summary>[기출 22회 12번 문제] (단답형) 위험관리와 관련하여 ( )에 들어갈 용어를 기술하시오.<br>
1. (A): 내외부 위협과 취약점으로 인해 자산에서 발생 가능한 위험을 감소시키기 위한 관리적, 물리적, 기술적 대책<br>
2. (B): (A)을 적용한 이후에 잔재하는 위험<br>
3. (C): 조직에서 수용 가능한 목표 위험 수준을 의미하며 경영진의 승인을 받아 관리해야 함</summary>
<blockquote>
<strong>정답:</strong> (A) <strong>정보보호 대책</strong>, (B) <strong>잔여 위험 (Residual Risk)</strong>, (C) <strong>DoA (Degree of Assurance / 위험 수용도)</strong>
</blockquote>
</details>

<details>
<summary>[기출 22회 14번 문제] (서술형) 다음의 위험분석 기법(기준선 접근법, 상세 위험 분석법)에 대하여 개념과 장단점을 설명하시오.</summary>
<blockquote>
1. <strong>기준선 접근법 (Baseline Approach)</strong><br>
- <strong>개념</strong>: 모든 시스템에 대해 공통적으로 적용할 표준 보안 체크리스트를 기반으로 보호 대책을 선택하는 방법<br>
- <strong>장단점</strong>: 분석 비용과 시간이 적게 들지만, 조직 특화된 위험을 간과하거나 과보호/과소보호가 발생할 수 있음<br>
2. <strong>상세 위험 분석 (Detailed Risk Analysis)</strong><br>
- <strong>개념</strong>: 자산 식별, 위협 및 취약점 평가를 순차적으로 수행하여 구체적인 위험 수치를 산출하는 정밀 분석 방법<br>
- <strong>장단점</strong>: 자산별 특성에 맞는 최적의 대책 수립이 가능하지만, 고도의 전문성이 필요하고 시간과 비용이 많이 소요됨
</blockquote>
</details>

<details>
<summary>[기출 23회 11번 문제] (단답형) 위험 관리의 단계 중 다음 (A), (B)에 해당하는 단계명을 쓰시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
(A): 자산의 위협과 취약점을 식별하여 발생 가능한 위험의 크기를 도출하는 과정<br>
(B): 산출된 위험도를 기준(DoA)과 비교하여 대응 여부와 우선순위를 결정하는 과정
</div>
</summary>
<blockquote>
(A) <strong>위험 분석 (Risk Analysis)</strong><br>
(B) <strong>위험 평가 (Risk Evaluation)</strong>
</blockquote>
</details>

<details>
<summary>(기출 23회 12번 문제) (단답형) 위험 관리를 위한 정보자산 분석 절차 중 다음 (A), (B) 에 해당하는 단계를 쓰시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
(A): 조직 내 보호 가치가 있는 모든 자산을 식별하고 상세 목록을 작성함<br>
(B): 식별된 자산의 기밀성, 무결성, 가용성 상실 시 영향을 분석하여 중요도를 부여함
</div>
</summary>
<blockquote>
(A) <strong>정보 자산 식별</strong><br>
(B) <strong>정보 자산 중요도 평가</strong>
</blockquote>
</details>

<details>
<summary>(기출 25회 11번 문제) (서술형) 분석된 위험에 대해 기업이 취할 수 있는 4가지 '위험 처리(Response)' 전략 중 다음 상황에 해당하는 전략의 명칭을 쓰시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
1. 위험으로 인한 예상 손실액보다 방어 비용이 더 클 때, 경영진이 해당 위험을 인식하고 기꺼이 수용하는 것: <code>( A )</code><br>
2. 서버 취약점이 해결되지 않아 해당 서비스를 아예 중단하거나 특정 기능을 사용하지 않는 것: <code>( B )</code><br>
3. 보안 사고 발생 시의 피해를 보험을 통해 보장받거나 외주 업체에 맡기는 것: <code>위험 전가(Transference)</code><br>
4. 보안 장비를 도입하거나 취약점을 패치하여 위험 수준을 낮추는 것: <code>위험 감소(Reduction)</code>
</div>
</summary>
<blockquote>
(A) <strong>위험 수용</strong> (Risk Acceptance)<br>
(B) <strong>위험 회피</strong> (Risk Avoidance)
</blockquote>
</details>

<details>
<summary>(기출 25회 15번 문제) (서술형) 정보 자산의 중요도를 평가할 때 기밀성(Confidentiality) 등급을 매기는 기준에 대한 예시이다. 빈칸에 들어갈 한글 또는 영문 등급명을 쓰시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
1. 상(High): 외부에 유출될 경우 국가 및 기업의 생존에 지대한 영항을 주는 정보<br>
2. <code>( A )</code>: 관련 부서나 이해관계자 등의 한정된 인원에게만 공개되어야 하는 정보<br>
3. <code>( B )</code>: 외부에 공개되어도 기업에 직접적인 피해가 없는 일반 대중을 위한 정보
</div>
</summary>
<blockquote>
(A) <strong>중 (Medium)</strong> (또는 제한적 기밀)<br>
(B) <strong>하 (Low)</strong> (또는 공개 정보)
</blockquote>
</details>

<details>
<summary>(서술형) 위험 처리 전략 중 4가지 유형(감소, 회피, 전가, 수용)을 나열하고 각각의 의미를 간략히 설명하시오.</summary>
<blockquote>
1. 위험 감소: 보안 장비 도입 등 대책을 강구하여 위험 발생 가능성이나 영향을 낮춤.<br>
2. 위험 회피: 위험이 존재하는 프로세스나 활동을 중단함.<br>
3. 위험 전가: 보험 가입이나 외주 등을 통해 위험의 책임을 제3자에게 넘김.<br>
4. 위험 수용: 현재 위험 수준이 낮아 별도의 대책 없이 위험을 받아들임.
</blockquote>
</details>

### 정보보호 관리체계(ISMS)

<details>
<summary>[기출 19회 9번 문제] (단답형) 정보자산 위험 평가 시, 기밀성(C), 무결성(I), 가용성(A)을 기준으로 자산의 가치를 등급화(상, 중, 하)하여 산정하는 핵심 지표의 명칭은?</summary>
<blockquote>
<strong>정답:</strong> <strong>자산 중요도</strong>
</blockquote>
</details>

<details>
<summary>[기출 13회 9번 문제] (단답형) 정보자산의 중요도를 평가할 때 기밀성, 무결성, 가용성을 고려하여 산정하는 핵심 지표의 명칭을 쓰시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>자산 중요도</strong>
</blockquote>
</details>

<details>
<summary>[기출 13회 15회 문제] (서술형) 정보자산 중요도 산정 시 기밀성, 무결성, 가용성 점수가 각각 3, 2, 1점일 때, 최종 자산 중요도를 산출하는 일반적인 산식 2가지를 기술하시오.</summary>
<blockquote>
<strong>정답:</strong><br>
1. <strong>합산 방식:</strong> C + I + A (결과: 6점)<br>
2. <strong>최대값 방식:</strong> Max(C, I, A) (결과: 3점)
</blockquote>
</details>

<details>
<summary>[기출 13회 10번 문제] (서술형) 위험관리 계획 수립 시 포함되어야 하는 주요 항목 4가지를 서술하시오.</summary>
<blockquote>
<strong>정답:</strong><br>
- 위험관리의 목적 및 범위(대상 자산 포함)<br>
- 위험관리 조직의 역할과 책임<br>
- 위험 분석 및 평가 방법론(추진 절차)<br>
- 수용 가능한 위험 수준(DoA) 및 사후 관리 방안
</blockquote>
</details>

<details>
<summary>[기출 19회 14번 문제] (실무형) 자산 식별 목록에 DB서버, 웹서버만 기재되어 있고 DMZ 내 개발 서버가 누락되었을 때 발생할 수 있는 문제점 2가지를 설명하시오.</summary>
<blockquote>
1. <strong>위험 관리 사각지대 발생</strong>: 식별되지 않은 자산에 대해서는 위험 평가나 취약점 분석이 수행되지 않아 잠재적 위협에 노출됨<br>
2. <strong>침투 경로로 악용</strong>: 관리되지 않는 개발 서버가 해커의 최초 침투 경로(Footprinting/Infection)가 되어 내부망 전체로 공격이 확산될 수 있음
</blockquote>
</details>

<details>
<summary>[기출 20회 10번 문제] (단답형) ISMS-P 인증 기준 중 '물리적 정보보호 대책'에 해당하는 주요 사항 3가지를 기술하시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>보호구역 지정(통제구역/제한구역 등), 출입 통제(출입 이력 관리), 물리적 보호설비 운영(UPS/항온항습/화재감지기 등)</strong>
</blockquote>
</details>

<details>
<summary>[기출 13회 6번 문제] (단답형) 사이버 공격이 전개되는 과정을 단계별로 분석하여 각 공격 단계에 적절한 대응 방안을 제시하는 모델의 명칭을 쓰시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>사이버 킬 체인 (Cyber Kill Chain)</strong><br>
<strong>해설:</strong> 록히드 마틴사가 개발한 모델로, 정찰 - 무기화 - 전달 - 취약점 공격 - 설치 - 명령 및 제어 - 행동 등 7단계로 구성됨.
</blockquote>
</details>

<details>
<summary>[기출 13회 11번 문제] (서술형) 물리적 정보보호 대책 중 '통제구역'의 정의와 구체적인 보호 대책 3가지를 기술하시오.</summary>
<blockquote>
<strong>정답:</strong><br>
- <strong>정의:</strong> 정보 자산이 설치된 장소 중 보안이 특히 중요하여 인가된 최소한의 인원만 출입해야 하는 구역 (예: 전산실, 방재실 등)<br>
- <strong>대책 1:</strong> 출입 통제 시스템(생체 인증, 카드키 등) 설치 및 2중 잠금 장치 적용<br>
- <strong>대책 2:</strong> CCTV 설비를 통한 24시간 감시 및 출입 이력 기록/보존<br>
- <strong>대책 3:</strong> 비인가자의 단독 출입 금지 및 인가자 동반 출입 통제
</blockquote>
</details>

<details>
<summary>[789] (작업형) 공공기관이나 기업에서 정보보호 관리체계(ISMS)를 수립할 때 수행하는 '위험 분석(Risk Analysis)'의 4단계 절차를 순서대로 작성하시오.</summary>
<blockquote>
1. 자산 식별: 조직의 정보자산(H/W, S/W, 데이터 등)을 식별하고 중요도를 산정한다.<br>
2. 위협 및 취약점 분석: 자산에 영향을 줄 수 있는 내·외부 위협 요인과 시스템의 약점을 식별한다.<br>
3. 위험 평가: 식별된 위험을 기반으로 발생 가능성과 영향을 계산하여 위험도를 산정한다.<br>
4. 정보보호대책 수립: 목표 위험 수준을 초과하는 위험에 대해 적절한 보호 대책과 이행 계획을 수립한다.
</blockquote>
</details>

<details>
<summary>(단답형) 사용자가 통계적 데이터로부터 개별 항목에 대한 정보를 추론해 내는 보안 위협의 명칭을 작성하시오.</summary>
<blockquote>
추론 (Inference)
</blockquote>
</details>

### 업무 연속성 계획(BCP)/재해복구계획(DRP)

<details>
<summary>[기출 12회 10번 문제] (단답형) 재해 복구 시스템의 운영 형태 중 다음 설명에 해당하는 것을 쓰시오.
1) 주 센터와 동일한 수준의 자원을 백업 센터에 구성하여 실시간 복제가 이루어지는 방식(RTO≒0): <strong>( A )</strong><br>
2) 주 센터와 동일한 수준의 자원은 보유하되 대기 상태로 유지하며 데이터만 동기화하는 방식(RTO<수 시간): <strong>( B )</strong><br>
3) 중요 자원 위주로 구성하며 비동기 복제 등을 통해 주 센터보다 낮은 비용으로 운영하는 방식(RTO<수 일): <strong>( C )</strong><br>
4) 데이터만 백업하고 실제 가동에 필요한 설비는 재해 시 구축하는 가장 낮은 비용의 방식(RTO<수 주): <strong>( D )</strong>
</summary>
<blockquote>
<strong>정답:</strong><br>
(A) <strong>Mirror Site (미러 사이트)</strong><br>
(B) <strong>Hot Site (핫 사이트)</strong><br>
(C) <strong>Warm Site (웜 사이트)</strong><br>
(D) <strong>Cold Site (콜드 사이트)</strong>
</blockquote>
</details>

<details>
<summary>[기출 21회 4번 문제] (단답형) 업무 연속성 계획(BCP) 5단계 중 2~4단계의 명칭을 차례대로 기술하시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>사업영향평가(BIA) → 복구전략수립 → 복구계획수립 (및 이행)</strong>
</blockquote>
</details>

<details>
<summary>[기출 19회 6번 문제] (단답형) BCP 수립 단계 중, 업무가 중단될 경우 발생할 수 있는 손실을 분석하여 복구 목표 시간(RTO)과 목표 시점(RPO)을 결정하는 핵심 절차는 무엇인가?</summary>
<blockquote>
<strong>정답:</strong> <strong>BIA (Business Impact Analysis, 업무 영향도 분석)</strong>
</blockquote>
</details>

<details>
<summary>[기출 21회 12번 문제] (서술형) 재해복구시스템 유형(미러, 핫, 웜, 콜드) 중 미러 사이트의 정의/장단점과 RTO가 가장 오래 걸리는 방식을 쓰시오.</summary>
<blockquote>
1. <strong>미러 사이트 (Mirror Site)</strong>: 주 센터와 동일한 시스템을 실시간 액티브-액티브(Active-Active)로 운영하여 RTO가 거의 0(즉시 복구)임. 하지만 구축 및 유지 비용이 매우 높음<br>
2. <strong>RTO가 가장 긴 방식</strong>: <strong>콜드 사이트 (Cold Site)</strong>. 인프라 공간만 확보하고 장비나 데이터를 평소에 가동하지 않으므로 복구 시 자원 조달 및 데이터 복원에 수일~수주가 소요됨
</blockquote>
</details>

<details>
<summary>(단답형) 정보보호 관리체계(ISMS)의 세부 통제 항목 중 하나로, 물리적 접근 통제를 넘어 시스템 장애, 화재, 지진 등 예기치 않은 재해 발생 시에도 기업의 핵심 비즈니스가 중단되지 않도록 목표 복구 시간(RTO) 내에 시스템과 업무를 복구할 수 있도록 수립하는 체계나 계획의 명칭을 영문 약어로 쓰시오.</summary>
<blockquote>
BCP (Business Continuity Plan, 업무 연속성 계획)
</blockquote>
</details>

<details>
<summary>(단답형) 재해 시 중단된 서비스를 복구하는 데 걸리는 <strong>최대 허용 시간</strong>을 뜻하는 용어와 유실을 감내할 수 있는 <strong>데이터의 손실 허용 시점</strong>을 뜻하는 용어의 약어를 순서대로 기술하시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>RTO (Recovery Time Objective)</strong>, <strong>RPO (Recovery Point Objective)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) BCP 수립의 핵심 단계로, 핵심 업무 프로세스를 식별하고 업무 중단에 따른 영향도를 분석하여 복구 우선순위 및 목표 시간을 결정하는 과정은?</summary>
<blockquote>
<strong>정답:</strong> <strong>BIA (업무 영향 분석 / Business Impact Analysis)</strong>
</blockquote>
</details>

<details>
<summary>(서술형) 재해 복구 계획(DRP)과 업무 연속성 계획(BCP)의 핵심적인 차이점을 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>DRP</strong>는 주로 정보 기술(IT) 인프라와 서비스의 복구에 초점을 맞춘 하위 계획인 반면, <strong>BCP</strong>는 IT뿐만 아니라 인력, 설비, 자금 등 조직의 모든 자원을 대상으로 비즈니스의 생존과 연속성을 보장하기 위한 보다 광범위한 체계이다.
</blockquote>
</details>

<details>
<summary>(서술형) <strong>미러 사이트(Mirror Site)</strong>와 <strong>핫 사이트(Hot Site)</strong>의 복구 방식과 시간(RTO) 차이를 비교 설명하시오.</summary>
<blockquote>
<strong>정답:</strong><br>
1. <strong>Mirror Site</strong>: 주 센터와 동일한 시스템을 구축하여 실시간으로 동시 서비스(Active-Active)를 제공하며, 재해 시 즉시(RTO=0) 복구가 가능하다.<br>
2. <strong>Hot Site</strong>: 실시간 데이터 미러링을 수행하지만 시스템은 대기(Standby) 상태로 유지하며, 재해 시 활성화 절차를 거쳐 수 시간 이내에 복구가 가능하다.
</blockquote>
</details>

<details>
<summary>(서술형) <strong>콜드 사이트(Cold Site)</strong>의 구축 방식과 장단점을 비용과 복구 시간 관점에서 설명하시오.</summary>
<blockquote>
<strong>정답:</strong><br>
- <strong>구축 방식</strong>: 데이터만 원격지에 보관하고 최소한의 장소와 통신 설비만 확보한다.<br>
- <strong>장점</strong>: 구축 및 유지 비용이 가장 저렴하다.<br>
- <strong>단점</strong>: 재해 시 장비를 새로 구매하고 설치해야 하므로 복구에 수 주에서 수 개월이 소요되며 신뢰성이 낮다.
</blockquote>
</details>

<details>
<summary>(단답형) 주 센터와 중요도가 높은 일부 시스템만 원격지에 구축하여, 재해 시 중요 업무를 우선 복구하는 방식의 명칭과 예상되는 RTO 수준은?</summary>
<blockquote>
<strong>정답:</strong> <strong>웜 사이트 (Warm Site)</strong>, <strong>수 일 ~ 수 주 이내</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 유사한 장비를 가진 기업들 간에 재해 발생 시 서로의 시설물을 사용할 수 있도록 체결하는 계약 방식의 명칭은?</summary>
<blockquote>
<strong>정답:</strong> <strong>상호 지원 계약 (Mutual Aid Agreement)</strong>
</blockquote>
</details>

<details>
<summary>(작업형) 업무 연속성 계획(BCP)의 5단계 방법론을 올바른 순서대로 나열하시오.<br>
(A) 복구 전략 개발<br>
(B) 사업 영향 평가 (BIA)<br>
(C) 프로젝트 범위 설정 및 기획<br>
(D) 프로젝트 수행 테스트 및 유지보수<br>
(E) 복구 계획 수립 (문서화)</summary>
<blockquote>
<strong>정답:</strong> <strong>(C) → (B) → (A) → (E) → (D)</strong>
</blockquote>
</details>

<details>
<summary>(작업형) 다음 중 재해 복구 유형(DRS)에 대한 설명으로 올바르지 않은 것은?<br>
(가) 미러 사이트는 데이터 손실이 거의 없으나 구축 비용이 매우 비싸다.<br>
(나) 웜 사이트는 핫 사이트에 비해 복구 시간이 길며 데이터 일부 손실 가능성이 있다.<br>
(다) 콜드 사이트는 RTO가 가장 짧은 방식으로 신속한 업무 재개가 가능하다.<br>
(라) 핫 사이트는 주 센터와 동일한 최신 상태의 데이터를 유지한다.</summary>
<blockquote>
<strong>정답:</strong> <strong>(다)</strong><br>
(※ 해설: 콜드 사이트는 RTO가 가장 <strong>긴</strong> 방식(수 주~수 개월)이며, 가장 짧은 방식은 미러 사이트 또는 핫 사이트이다.)
</blockquote>
</details>

<details>

<summary>(서술형) 전자서명(Digital Signature)의 메커니즘을 '해시 함수'와 '비대칭키 암호화' 관점에서 요약하여 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> 송신자는 메시지 원본을 해시하여 고유한 해시값을 추출한 뒤, 자신의 <strong>개인키(Private Key)</strong>로 암호화하여 전자서명을 생성한다. 수신자는 송신자의 <strong>공개키(Public Key)</strong>로 서명을 복호화하여 얻은 해시값과, 직접 메시지를 해시한 값을 비교하여 일치 여부를 확인한다.
</blockquote>
</details>

<details>
<summary>(단답형) 전자서명을 통해 보장할 수 있는 정보보안의 3대 핵심 목표를 기술하시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>무결성, 인증(신원 확인), 부인 방지</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 전자서명의 요구 조건 중, 서명자만이 고유한 서명을 생성할 수 있어야 하며 제3자가 정당한 서명자의 서명을 흉낼 수 없어야 한다는 원칙은?</summary>
<blockquote>
<strong>정답:</strong> <strong>위조 불가 (Unforgeable)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 전자서명의 요구 조건 중, 서명 대상인 메시지의 내용이 조금이라도 변경되면 서명 검증이 실패해야 한다는 원칙은?</summary>
<blockquote>
<strong>정답:</strong> <strong>변경 불가 (Unalterable)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 전자서명의 요구 조건 중, 한 번 생성된 서명값을 다른 메시지의 서명으로 재사용할 수 없어야 한다는 원칙은?</summary>
<blockquote>
<strong>정답:</strong> <strong>재사용 불가 (Not reusable)</strong>
</blockquote>
</details>

<details>
<summary>(서술형) 스마트 OTP(Smart OTP) 방식이 기존의 토큰형 OTP에 비해 가지는 보안적·편의적 장점을 기술하시오.</summary>
<blockquote>
<strong>정답:</strong> 스마트폰의 <strong>NFC(근거리 무선 통신)</strong> 기능을 활용하여 금융 보안카드를 터치함으로써 자동으로 OTP 번호를 생성 및 입력하므로, 별도의 토큰형 기기를 소지할 필요가 없으며 번호 오입력 실수를 방지할 수 있다.
</blockquote>
</details>

<details>
<summary>[782] (단답형) 공개키 암호 방식을 기반으로 디지털 인증서의 생성, 발급, 관리, 폐지 등을 수행하는 종합적인 보안 체계(환경)를 무엇이라 하는가?</summary>
<blockquote>
<strong>정답:</strong> <strong>공개키 기반 구조 (PKI: Public Key Infrastructure)</strong>
</blockquote>
</details>

<details>
<summary>[782] (단답형) PKI에서 사용자의 신원을 직접 확인(대면 확인)하고 인증서 발급 신청을 대행하는 기관은?</summary>
<blockquote>
<strong>정답:</strong> <strong>등록 기관 (RA: Registration Authority)</strong>
</blockquote>
</details>

<details>
<summary>[782] (단답형) PKI에서 인증서 발행 정책을 수립하고 실제로 인증서를 발급 및 폐지하는 핵심적인 신뢰 기관은?</summary>
<blockquote>
<strong>정답:</strong> <strong>인증 기관 (CA: Certificate Authority)</strong>
</blockquote>
</details>

<details>
<summary>[784] (단답형) 공개키 인증서의 표준 형식으로, 버전, 일련번호, 발급자, 유효기간, 주체 정보 등을 포함하고 있는 국제 표준 방식은?</summary>
<blockquote>
<strong>정답:</strong> <strong>X.509</strong> (현재 주로 V3 사용)
</blockquote>
</details>

<details>
<summary>[783] (단답형) 인증서의 유효기간이 만료되기 전이라도 개인키 유출 등의 사유로 신뢰할 수 없게 된 인증서들의 목록을 무엇이라 하는가?</summary>
<blockquote>
<strong>정답:</strong> <strong>인증서 폐지 목록 (CRL: Certificate Revocation List)</strong>
</blockquote>
</details>

<details>
<summary>[783] (서술형) 인증서의 유효성 여부를 확인할 때, 주기적으로 배포되는 CRL 방식의 문제점과 이를 해결하기 위한 실시간 확인 서비스(OCSP)의 장점을 비교 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> CRL은 파일 크기가 커질수록 네트워크 부하가 심해지고 실시간 반영이 어렵다는 단점이 있다. 반면 <strong>OCSP(Online Certificate Status Protocol)</strong>는 서버에 실시간으로 질의하여 즉각적인 유효성 확인이 가능하므로 보안성이 더 높고 효율적이다.
</blockquote>
</details>

<details>
<summary>[784] (단답형) X.509 인증서 구조에서 인증서를 발급한 주체의 명칭(Distinguished Name)을 나타내는 필드는?</summary>
<blockquote>
<strong>정답:</strong> <strong>발급자 (Issuer Name)</strong>
</blockquote>
</details>

<details>
<summary>[783] (단답형) PKI 환경에서 사용자가 자신의 인증서를 폐지하고자 할 때, CA가 폐지 사유를 명시하는 필드에 기입되는 대표적인 사유 한 가지를 쓰시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>주체 개인키 유출 (KeyCompromise)</strong>, CA 침해, 소속 변경 등
</blockquote>
</details>

<details>
<summary>(단답형) 블록체인에서 기존의 프로토콜과 호환되지 않는 완전히 새로운 방식의 업데이트로, 새로운 체인을 생성하여 갈라지는 현상을 무엇이라 하는가?</summary>
<blockquote>
<strong>정답:</strong> <strong>하드 포크 (Hard Fork)</strong>
</blockquote>
</details>

<details>
<summary>(서술형) 블록체인의 '스마트 계약 (Smart Contract)'의 의미를 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> 서면으로 체결하던 계약 조건을 코드로 구현하여 블록체인 상에 기록해 두고, 특정 조건이 충족되면 제3자의 개입 없이 자동으로 계약이 이행되도록 하는 기술이다.
</blockquote>
</details>

<details>
<summary>(단답형) 전 세계 누구나 네트워크 참여가 가능하고 기록을 열람할 수 있는 비트코인, 이더리움과 같은 블록체인 유형은?</summary>
<blockquote>
<strong>정답:</strong> <strong>퍼블릭 블록체인 (Public Blockchain)</strong>
</blockquote>
</details>

<details>
<summary>(서술형) 블록체인의 '이중 지불 (Double Spending)' 문제의 개념을 기술하시오.</summary>
<blockquote>
<strong>정답:</strong> 동일한 디지털 자산(암호화폐)을 동시에 두 번 이상 사용하는 행위로, 분산 네트워크에서 거래 합의 과정을 통해 이를 방지해야 한다.
</blockquote>
</details>

<details>
<summary>[783] (단답형) 인증서 유효성 확인 시, 클라이언트가 직접 CA 서버에 질의하지 않고 미리 발급받은 증명서(Stapled result)를 서버가 대신 제공하여 부하를 줄이는 기술은?</summary>
<blockquote>
<strong>정답:</strong> <strong>OCSP 스테이플링 (OCSP Stapling)</strong>
</blockquote>
</details>

<details>
<summary>[783] (단답형) 인증서 폐지 사유 중, 퇴사나 소속 기관 변경으로 인해 인증서 권한을 박탈해야 하는 경우를 의미하는 용어는?</summary>
<blockquote>
<strong>정답:</strong> <strong>소속 변경 (Affiliation Changed)</strong>
</blockquote>
</details>

### 침해사고 대응

<details>
<summary>(단답형) 정보보호 관련 법령(기반보호법 등)에서 정의하는 침해사고의 원인이 되는 행위로, 해킹, 서비스 거부 공격, 고출력 전자기파 등에 의하여 정보통신망이나 시스템을 공격하는 행위를 무엇이라 하는가?</summary>
<blockquote>
<strong>정답:</strong> <strong>전자적 침해행위</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 침해사고 대응 7단계 절차 중, 사고가 발생하기 전에 미리 침해사고 대응 팀(CERT)을 조직하고 조직적인 대응을 준비하는 단계는?</summary>
<blockquote>
<strong>정답:</strong> <strong>사고 전 준비 (Preparation)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 침해사고 대응 7단계 절차 중, 현재 상황에서 최적의 대응 전략을 결정하고 관리자의 승인을 획득하며 수사기관 공조 여부를 판단하는 단계는?</summary>
<blockquote>
<strong>정답:</strong> <strong>대응 전략 체계화 (Strategy Formulation)</strong>
</blockquote>
</details>

<details>
<summary>(서술형) 침해사고 조사의 **데이터 수집** 단계에서 '호스트 기반 증거'와 '네트워크 기반 증거'의 구체적인 예를 각각 2가지 이상 나열하시오.</summary>
<blockquote>
<strong>정답:</strong><br>
1. <strong>호스트 기반 증거</strong>: 시스템 날짜 및 시간, 휘발성 데이터(메모리, 실행 중인 프로세스 등), 디스크 이미지, 레지스트리 정보 등<br>
2. <strong>네트워크 기반 증거</strong>: IDS/방화벽 로그, 라우터 로그, 웹 서버 로그, 네트워크 패킷 덤프 등
</blockquote>
</details>

<details>
<summary>(서술형) 침해사고 대응 7단계 절차를 순서대로 기술하시오.</summary>
<blockquote>
<strong>정답:</strong> 1. <strong>사고 전 준비</strong>, 2. <strong>사고 탐지</strong>, 3. <strong>초기 대응</strong>, 4. <strong>대응 전략 체계화</strong>, 5. <strong>사고 조사</strong>, 6. <strong>보고서 작성</strong>, 7. <strong>해결</strong>
</blockquote>
</details>

<details>
<summary>(서술형) 침해사고 조사의 **데이터 분석** 단계에서 수행하는 구체적인 활동 3가지를 설명하시오.</summary>
<blockquote>
<strong>정답:</strong><br>
1. <strong>휘발성 데이터 분석</strong>: 네트워크 접속 기록 조사 및 악의적인 코드(백도어, 스니퍼 등) 식별<br>
2. <strong>파일 시간 분석</strong>: 파일 생성/수정 날짜 조사를 통한 공격자의 파일 업로드 및 변조 시점 파악<br>
3. <strong>로그 분석</strong>: 비인가 계정의 접근 기록이나 숨겨진 파일 검색, 스케줄 서비스에 의한 악성 과업 확인 등
</blockquote>
</details>

<details>
<summary>(작업형) 침해사고 발생 시 수집해야 할 **휘발성 데이터(Volatile Data)**에 해당하지 않는 요소는?<br>
(가) 현재 실행 중인 프로세스 및 애플리케이션 목록<br>
(나) 현재 연결된 네트워크 포트 및 소켓 정보<br>
(다) 하드디스크의 비활성 영역 파일 시스템 메타데이터<br>
(라) 시스템 커널 메모리 내 프로세스 정보</summary>
<blockquote>
<strong>정답:</strong> <strong>(다)</strong><br>
(※ 해설: 휘발성 데이터는 전원 차단 시 사라지는 데이터(메모리 정보 등)를 의미하며, 하드디스크에 저장된 메타데이터는 비휘발성 증거에 해당함)
</blockquote>
</details>

<details>
<summary>(단답형) 특정 시점의 시스템 정보(메모리, 파일 시스템 등)를 한 번에 파일이나 이미지 형태로 저장하는 기술을 무엇이라 하는가?</summary>
<blockquote>
<strong>정답:</strong> <strong>스냅샷 (Snapshot)</strong>
</blockquote>
</details>

<details>
<summary>(작업형) 다음 상황에 가장 적절한 침해사고 대응 전략을 서술하시오. "웹 서버에 대규모 분산 서비스 거부(DDoS) 공격이 발생하여 현재 서비스 이용이 불가능한 상태이다."</summary>
<blockquote>
<strong>정답:</strong> dDoS 대응 장비의 설정을 변경하여 공격 트래픽을 차단하고, ISP 협업 및 사이버 대피소 전환을 논의하며 수사기관과의 공조를 통해 공격자의 처벌을 위한 증거를 확보한다.
</blockquote>
</details>

<details>
<summary>(서술형) 디지털 포렌식의 5대 기본 원칙을 모두 기술하고, 그 중 '무결성의 원칙'을 보장하기 위해 일반적으로 사용하는 기술적 수단과 확인 방법을 설명하시오.</summary>
<blockquote>
<strong>정답:</strong><br>
1. <strong>5대 원칙</strong>: 정당성의 원칙, 재현성의 원칙, 무결성의 원칙, 신속성의 원칙, 연계 보관성(Chain of Custody) 원칙<br>
2. <strong>무결성 보장 수단</strong>: <strong>해시(Hash) 함수</strong>를 사용하여 최초 수집 시점의 해시값을 산출해 보관하고, 이후 분석 및 제출 단계에서 산출한 해시값과 비교하여 일치 여부를 확인함으로써 위·변조가 없었음을 입증한다.
</blockquote>
</details>

<details>
<summary>(단답형) 디지털 증거의 수집(획득)부터 이송, 보관, 분석, 법정 제출까지의 각 단계에서 관리 주체와 인수인계 내역을 연속적으로 기록하여 증거의 원본성을 입증하는 원칙은?</summary>
<blockquote>
<strong>정답:</strong> <strong>연계 보관성 원칙 (Chain of Custody)</strong>
</blockquote>
</details>

<details>
<summary>(작업형) 연계 보관성 원칙을 만족시키기 위해 디지털 증거물이 거치는 5가지 주요 단계를 순서대로 기술하시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>획득(수집) → 이송(이동) → 보관 → 분석 → 법정 제출</strong>
</blockquote>
</details>

<details>
<summary>(서술형) 윈도우(Windows) 침해사고 조사 시, 휘발성 데이터 수집을 위해 사용하는 내장 명령어 중 다음의 정보를 확인하기 위한 명령어를 각각 기술하시오.<br>
(A) 시스템의 현재 날짜와 시간 확인<br>
(B) 현재 열린 포트와 연결된 서비스(PID 포함) 확인<br>
(C) 실행 중인 프로세스 목록 및 상세 정보 확인<br>
(D) 외부에서 현재 시스템으로 연결된 세션 정보 확인</summary>
<blockquote>
<strong>정답:</strong><br>
(A): <strong>date /t</strong> 및 <strong>time /t</strong><br>
(B): <strong>netstat -anob</strong><br>
(C): <strong>tasklist /v</strong><br>
(D): <strong>net session</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 범죄학자 에드몽 로카르드가 정의한 원칙으로, "접촉하는 두 물체 간에는 반드시 흔적이 남는다"는 이론은 무엇인가?</summary>
<blockquote>
<strong>정답:</strong> <strong>로카르드의 교환 법칙</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 사진, 동영상, 음악 파일 등 정상적인 미디어 파일 내에 비밀 정보를 은닉하여 감추는 안티 포렌식 기술의 명칭은?</summary>
<blockquote>
<strong>정답:</strong> <strong>스테가노그래피 (Steganography)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 하드디스크에 저장된 데이터를 0, 1 또는 무작위 값으로 여러 번 덮어씌워 소프트웨어적으로 복구를 불가능하게 만드는 기법은?</summary>
<blockquote>
<strong>정답:</strong> <strong>디스크 와이핑 (Disk Wiping)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 디스크에 강력한 자기장을 가하여 데이터를 물리적으로 파괴함으로써 재사용조차 불가능하게 만드는 안티 포렌식 방식은?</summary>
<blockquote>
<strong>정답:</strong> <strong>디스크 디가우징 (Disk Degaussing)</strong>
</blockquote>
</details>

<details>
<summary>(작업형) 다음 중 디지털 증거 수집 방법에 대한 설명으로 올바르지 않은 것은?<br>
(가) <strong>이미징(Imaging)</strong>은 원본 저장 매체의 데이터를 파일 형태의 이미지로 생성하는 것이다.<br>
(나) <strong>복제(Cloning)</strong>는 동일한 용량이나 특성을 가진 다른 저장 매체에 원본과 똑같이 복제하는 것이다.<br>
(다) <strong>복사(Copy)</strong>는 윈도우 탐색기 등을 활용하는 방식으로, 삭제된 파일이나 비할당 영역까지 완벽하게 수집할 수 있어 가장 권장된다.<br>
(라) 모든 수집 과정에서는 무결성 입증을 위한 해시 생성 절차가 수반되어야 한다.</summary>
<blockquote>
<strong>정답:</strong> <strong>(다)</strong><br>
(※ 해설: 단순 복사 방식은 삭제된 파일, 슬랙 공간(Slack Space), 파일 시스템의 메타데이터 등을 수집할 수 없으므로 법적 증거 수집 시에는 권장되지 않으며 이미징 또는 복제 방식을 사용해야 한다.)
</blockquote>
</details>

<details>
<summary>(단답형) 디지털 포렌식 5단계 절차 중, 현장의 디지털 기기로부터 무결성을 보장하며 증거를 획득하는 단계의 명칭은?</summary>
<blockquote>
<strong>정답:</strong> <strong>증거 수집 (Acquisition)</strong>
</blockquote>
</details>

<details>
<summary>(서술형) 디지털 포렌식(Digital Forensics)의 '연계 보관성(Chain of Custody) 원칙'에 대해 설명하고, 이를 보장하기 위해 증거물 획득 단계에서 수행해야 할 조치를 서술하시오.</summary>
<blockquote>
원칙: 증거물이 수집된 순간부터 법정에 제출될 때까지 모든 이동 및 관리 경로가 기록되어 위·변조가 없었음을 입증해야 한다는 원칙이다.<br>
조치: 증거물 획득 시 원본 매체의 해시(Hash) 값을 산출하여 기록하고, 증거물 봉인 및 이송 시 담당자 서명을 포함한 인수인계 증명서를 작성하여 관리해야 한다.
</blockquote>
</details>

<details>
<summary>(서술형) 디지털 포렌식 시 증거 수집 과정에서 지켜야 할 '원본 유지의 원칙'의 개념을 설명하고, 사건사고 조사 시 원본 하드디스크를 복사하여 분석할 때 원본과의 동일성을 입증하기 위해 필수적으로 문서화해야 하는 암호학적 기법 한 가지를 쓰시오.</summary>
<blockquote>
<strong>개념</strong>: 수집된 디지털 증거(원본 데이터)는 조사 및 분석 과정에서 어떠한 형태의 위조, 변조, 훼손도 없이 최초 압수 당시의 상태를 그대로 유지해야 한다는 원칙이다.<br>
<strong>동일성 입증 기법</strong>: 해시 함수 기법 (또는 무결성 해시값 검증). 원본 디스크와 복제된 이미지의 MD5, SHA 등의 해시값을 추출하여 두 값이 100% 일치함을 기록하여 법정에 제출해야 한다.
</blockquote>
</details>

<details>
<summary>[기출 20회 4번 문제] (단답형) 접근통제 정책에 대하여 다음 ( )에 들어갈 용어를 기술하시오.<br>
(A): 사용자나 사용자 그룹에 근거하여 자원에 대한 접근 권한을 부여하고 제한하는 사용자 중심의 접근 제어 방법<br>
(B): 모든 객체는 정보의 비밀 수준에 근거하여 보안 레벨이 주어지고, 허가된 사용자만 접근할 수 있도록 시스템이 강제하는 방법<br>
(C): 사용자와 객체의 상호관계를 '역할'을 기반으로 정의하여 접근 권한을 부여하는 방법</summary>
<blockquote>
<strong>정답:</strong> (A) <strong>DAC (임의적 접근통제)</strong>, (B) <strong>MAC (강제적 접근통제)</strong>, (C) <strong>RBAC (역할기반 접근통제)</strong>
</blockquote>
</details>

<details>
<summary>[771] (서술형) 벨-라파듈라(BLP) 모델의 두 가지 핵심 보안 속성인 <code>No Read Up</code>과 <code>No Write Down</code>의 의미를 기밀성 관점에서 설명하시오.</summary>
<blockquote>
<strong>정답:</strong>
- <strong>No Read Up (Simple Security Property)</strong>: 낮은 보안 등급의 주체(사용자)가 높은 보안 등급의 객체(문서)를 읽을 수 없도록 하여 정보의 기밀성을 유지한다. (Simple Security)
- <strong>No Write Down (*-Property)</strong>: 높은 등급의 정보를 취급하는 주체가 낮은 보안 등급의 객체에 정보를 기록할 수 없도록 하여, 기밀 정보가 하위 등급으로 유출되는 것을 방지한다. (Star Property)
</blockquote>
</details>

<details>
<summary>[771] (서술형) 비바(Biba) 모델의 두 가지 핵심 보안 속성인 <code>No Read Down</code>과 <code>No Write Up</code>의 의미를 무결성 관점에서 설명하시오.</summary>
<blockquote>
<strong>정답:</strong>
- <strong>No Read Down (Simple Integrity Property)</strong>: 높은 무결성 수준의 주체가 낮은 무결성 수준의 객체를 읽지 못하게 하여, 낮은 수준의 데이터로 인해 높은 수준의 주체가 오염되는 것을 방지한다.
- <strong>No Write Up (*-Integrity Property)</strong>: 낮은 무결성 수준의 주체가 높은 무결성 수준의 객체에 데이터를 쓸 수 없도록 하여, 상위 수준의 데이터가 오염되거나 변조되는 것을 차단한다.
</blockquote>
</details>

<details>
<summary>[771] (단답형) 무결성의 3가지 목표(비인가자 변조 방지, 내부자 실수 방지, 일관성 유지)를 모두 충족시키기 위해 고안되었으며, 상용 응용 분야에서 거래의 무결성을 보장하는 데 주로 사용되는 보안 모델은?</summary>
<blockquote>
<strong>정답:</strong> <strong>클락-윌슨 (Clark-Wilson) 모델</strong>
</blockquote>
</details>

<details>
<summary>[771] (단답형) 주체와 객체 간의 이해 상충(Conflict of Interest)이 발생할 수 있는 경우, 이를 방지하기 위해 이전에 접근했던 정보 영역에 따라 다른 정보로의 접근을 동적으로 차단하는 보안 모델은?</summary>
<blockquote>
<strong>정답:</strong> <strong>만리장성 (Chinese Wall / Brewer-Nash) 모델</strong>
</blockquote>
</details>

<details>
<summary>[770] (서술형) 강제적 접근통제(MAC)와 임의적 접근통제(DAC)의 가장 큰 차이점을 정책 결정 주체 관점에서 설명하시오.</summary>
<blockquote>
<strong>정답:</strong>
- <strong>MAC</strong>: 시스템 관리자가 중앙에서 보안 등급과 레이블에 따라 접근 권한을 강제로 결정하며, 객체의 소유자라도 권한을 임의로 변경할 수 없다.
- <strong>DAC</strong>: 자원의 소유자가 자신의 판단에 따라 다른 사용자에게 접근 권한을 부여하거나 취소할 수 있는 유연한 방식이다.
</blockquote>
</details>

<details>
<summary>[770] (단답형) 사용자에게 개별적인 권한을 직접 부여하는 대신, 조직 내에서의 직무나 책임에 따라 권한의 묶음을 정의하고 이를 사용자에게 할당하는 접근통제 방식은?</summary>
<blockquote>
<strong>정답:</strong> <strong>역할 기반 접근통제 (RBAC: Role-Based Access Control)</strong>
</blockquote>
</details>

<details>
<summary>[770] (서술형) 임의적 접근통제(DAC) 환경에서 발생할 수 있는 보안 취약점 중 하나인 '트로이 목마' 공격에 취약한 이유를 기술하시오.</summary>
<blockquote>
<strong>정답:</strong> DAC는 프로세스가 사용자의 권한을 그대로 상속받아 실행되므로, 사용자가 실행한 악성 프로그램(트로이 목마)이 해당 사용자가 소유한 다른 파일들에 접근하여 정보를 유출하거나 변조하는 것을 막을 수 없기 때문이다.
</blockquote>
</details>

<details>
<summary>(단답형) 운영체제의 커널 수준에서 접근통제 및 보안 정책을 강제적으로 실행하여 일반적인 OS보다 높은 수준의 보안을 제공하는 운영체제를 무엇이라 하는가?</summary>
<blockquote>
<strong>정답:</strong> <strong>보안 운영체제 (Secure OS)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 보안 OS나 접근통제 시스템에서 주체가 객체에 접근할 때 사전에 정의된 보안 정책에 부합하는지 여부를 확인하고 결정하는 핵심 엔진(Reference Monitor)의 개념을 쓰시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>참조 모니터 (Reference Monitor)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 정보 시스템 내에서 원하지 않는 정보 흐름이 발생하는 것을 방지하기 위해 사용되는 정적 모델로, BLP나 Biba 모델 등의 기초가 되는 논리적 모델은?</summary>
<blockquote>
<strong>정답:</strong> <strong>정보 흐름 모델 (Information Flow Model)</strong>
</blockquote>
</details>

<details>
<summary>[778] (서술형) 역할 기반 접근통제(RBAC)에서 '직무 분리(Separation of Duties)'의 목적과 효과를 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> 한 사람이 모든 중요한 프로세스를 혼자 처리할 수 없도록 권한을 분산시킴으로써, 내부자에 의한 부정행위나 치명적인 실수를 사전에 예방하고 탐지하는 효과가 있다.
</blockquote>
</details>

<details>
<summary>(단답형) 인터넷에 연결된 서버, 스위치, 라우터뿐만 아니라 IP를 사용하는 각종 IoT 기기의 배너 정보를 수집하여 취약한 지점을 찾아낼 수 있는 '해커들의 검색 엔진'이라 불리는 웹 애플리케이션은?</summary>
<blockquote>
<strong>정답:</strong> <strong>쇼단 (Shodan)</strong>
</blockquote>
</details>

<details>
<summary>(서술형) 딥 웹(Deep Web)과 다크 웹(Dark Web)의 개념적 차이점을 설명하시오.</summary>
<blockquote>
<strong>정답:</strong>
- <strong>딥 웹</strong>: 검색 엔진에 의해 인덱싱되지 않는 웹 공간(개인 이메일, 데이터베이스 등)을 통칭한다.
- <strong>다크 웹</strong>: 딥 웹의 일부분으로, 특정 소프트웨어(Tor 등)를 통해서만 접속 가능한 익명성과 암호화가 보장된 네트워크 공간이다.
</blockquote>
</details>

<details>
<summary>(단답형) 네트워크 트래픽을 여러 층의 암호화된 노드를 거쳐 전송함으로써 사용자의 IP 주소와 위치를 숨기는 익명 네트워크 기술의 명칭은?</summary>
<blockquote>
<strong>정답:</strong> <strong>토르 (Tor, The Onion Router)</strong>
</blockquote>
</details>

<details>
<summary>(서술형) 토르(Tor) 네트워크를 사용할 때, 보안상 가장 취약하여 데이터가 노출될 위험이 있는 노드는 어디이며 그 이유를 기술하시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>출구 노드 (Exit Node)</strong>. 토르 내부망을 벗어나 최종 목적지 서버로 데이터를 전달할 때 마지막 암호화 계층이 해제되므로, 이 노드에서 트래픽을 모니터링하거나 스니핑할 위험이 있다.
</blockquote>
</details>

<details>
<summary>(단답형) 가상 사설망(VPN) 기술 중, 공중망을 통해 데이터를 전송할 때 가상의 전용 회선처럼 안전한 통로를 구축하는 기술을 무엇이라 하는가?</summary>
<blockquote>
<strong>정답:</strong> <strong>터널링 (Tunneling)</strong>
</blockquote>
</details>

<details>
<summary>(서술형) 정보보호 관리체계에서 '자산 식별(Asset Identification)'이 위험 관리의 첫 번째 단계로 강조되는 이유를 기술하시오.</summary>
<blockquote>
<strong>정답:</strong> 보호해야 할 대상이 무엇인지 정확히 파악되지 않으면, 그에 따른 위협이나 취약점 분석이 불가능하며 적절한 보안 대책을 효율적으로 수립할 수 없기 때문이다.
</blockquote>
</details>

<details>
<summary>(단답형) 조직의 보안 수준을 주기적으로 점검하고 개선하기 위해, 내부 직원이 아닌 독립적인 제3자가 객관적으로 보안 상태를 확인하는 활동은?</summary>
<blockquote>
<strong>정답:</strong> <strong>보안 감사 (Security Audit)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 사용자가 열람하고자 하는 파일이나 메뉴 등의 '내용(Content)'에 따라 접근 권한을 다르게 부여하는 세분화된 접근제어 방식은?</summary>
<blockquote>
<strong>정답:</strong> <strong>내용 기반 접근제어 (Content-dependent Access Control)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 접속 시간, 접속 위치, 로그인 실패 횟수 등 요청이 발생하는 '상황(Context)' 정보를 바탕으로 접근을 제어하는 방식은?</summary>
<blockquote>
<strong>정답:</strong> <strong>문맥 기반 접근제어 (Context-dependent Access Control)</strong>
</blockquote>
</details>

<details>
<summary>[771] (서술형) 벨-라파듈라(BLP) 모델이 상용 환경보다 군사적 목적에 더 적합한 이유를 모델의 특성과 관련지어 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> BLP 모델은 오직 정보의 외부 유출 방지(기밀성)에만 집중하고 있어, 비인가된 정보 변경(무결성)이나 데이터의 가용성 측면을 고려하지 않기 때문에 무결성이 중요한 상용 환경에는 적합하지 않다.
</blockquote>
</details>

<details>
<summary>(단답형) 사용자가 시스템에 로그인하여 얻은 권한을 오남용하는 것을 방지하기 위해, 한 사용자가 두 개 이상의 역할을 동시에 가지지 못하게 제한하는 RBAC의 제약 사항은?</summary>
<blockquote>
<strong>정답:</strong> <strong>정적/동적 직무 분리 (SSD / DSD)</strong>
</blockquote>
</details>

<details>
<summary>(서술형) 접근통제 행렬(Access Control Matrix)의 단점인 공간 낭비 문제를 해결하기 위해, 사용자(주체)를 기준으로 자산(객체)에 대한 권한 목록을 관리하는 데이터 구조는 무엇인가?</summary>
<blockquote>
<strong>정답:</strong> <strong>자격 증명 목록 (Capability List)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 반대로 자산(객체)을 기준으로 해당 자산에 접근할 수 있는 사용자(주체)와 권한 목록을 관리하는 리눅스/유닉스의 일반적인 접근통제 목록은?</summary>
<blockquote>
<strong>정답:</strong> <strong>ACL (Access Control List)</strong>
</blockquote>
</details>

<details>
<summary>(서술형) 침해사고 대응 과정에서 '봉쇄(Containment)' 단계의 핵심 목표를 기술하시오.</summary>
<blockquote>
<strong>정답:</strong> 침해 사고가 발생한 지점을 격리하거나 공격 경로를 차단함으로써, 악성 행위가 다른 시스템이나 네트워크로 확산(횡적 이동)되는 피해를 최소화하는 것이다.
</blockquote>
</details>

<details>
<summary>(단답형) 미국(TCSEC)과 유럽(ITSEC)의 보안성 평가 기준을 통합하여 ISO/IEC 15408로 제정된 국제 표준 평가 기준의 명칭(약어 포함)은?</summary>
<blockquote>
<strong>정답:</strong> <strong>공통평가기준 (CC: Common Criteria)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) CC 인증 과정에서 보안성 평가의 범위가 되는 정보시스템이나 특정 정보기술(IT) 제품을 지칭하는 용어와 약어를 기술하시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>평가 대상 (TOE: Target of Evaluation)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 특정 제품의 구현과는 독립적으로 정의되며, 사용자 그룹이 해당 유형의 제품에 대해 요구하는 보안 기능 요구사항을 기술한 문서는?</summary>
<blockquote>
<strong>정답:</strong> <strong>보호 프로파일 (PP: Protection Profile)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 특정 회사의 구체적인 제품의 보안 기능 요구사항과 구현 내용을 상세히 기술하며, 실제 제품 평가의 근거가 되는 문서는?</summary>
<blockquote>
<strong>정답:</strong> <strong>보안 목표 명세서 (ST: Security Target)</strong>
</blockquote>
</details>

<details>
<summary>(서술형) CC 인증의 구성 요소인 **PP(Protection Profile)**와 **ST(Security Target)**의 결정적인 차이점을 '구현 종속성' 관점에서 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>PP</strong>는 특정 구현 기술이나 설계에 종속되지 않는 범용적인 요구사항을 기술하는 반면, <strong>ST</strong>는 실제 특정 제품의 구현 내용에 종속되어 있으며 평가의 기준 데이터로 직접 사용된다.
</blockquote>
</details>

<details>
<summary>(단답형) CC에서 정의하는 제품의 신뢰성 보증 수준을 나타내는 척도의 명칭과, 가장 보증 수준이 높은 최고 등급 단계를 기술하시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>평가 보증 등급 (EAL: Evaluation Assurance Level)</strong>, <strong>EAL 7</strong>
</blockquote>
</details>

<details>
<summary>(서술형) **평가 보증 등급(EAL)**이 높아짐에 따라 평가 과정에서 나타나는 변화를 평가 노력의 3가지 요소(범위, 상세도, 엄격성) 관점에서 기술하시오.</summary>
<blockquote>
<strong>정답:</strong> 등급이 높아질수록 평권의 <strong>범위</strong>가 넓어지고, 개발 프로세스나 분석의 <strong>상세도</strong>가 깊어지며, 검증 및 평가 기법의 <strong>엄격성</strong>이 한층 강화되어 더 높은 신뢰성을 보장하게 된다.
</blockquote>
</details>

<details>
<summary>(작업형) 다음 중 CC 인증 구성 요소에 대한 설명으로 올바르지 않은 것은?<br>
(가) TOE는 인증 신청 기관이 평가받고자 하는 보안 기능의 범위를 지정할 수 있다.<br>
(나) 한 제품은 여러 개의 보호 프로파일(PP)을 준수하도록 개발되어 인증받을 수 있다.<br>
(다) EAL 1은 최저 등급이며 EAL 7은 수학적으로 증명된 가장 엄격한 보증 수준이다.<br>
(라) ST는 PP와 무관하게 작성되어야 하며, PP를 준수할 의무는 없다.</summary>
<blockquote>
<strong>정답:</strong> <strong>(라)</strong><br>
(※ 해설: ST는 해당 제품 유형의 PP를 준수하여 작성될 수 있으며, 실제 인증 시 해당 PP의 준수 여부를 함께 평가받는 것이 일반적이다.)
</blockquote>
</details>

<details>
<summary>(단답형) 사람 사이의 신뢰 관계를 이용하거나 심리적 취약점을 속여 보안 정보를 탈취하는 비기술적인 공격 방법의 명칭은?</summary>
<blockquote>
<strong>정답:</strong> <strong>사회공학 (Social Engineering) 기법</strong>
</blockquote>
</details>

<details>
<summary>(작업형) 사회공학 기법 중 '인간 기반 공격(Human-based Attack)'에 해당하는 구체적인 수법 3가지 이상 나열하시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>직접적 접근(지위 가장), 도청/엿듣기, 쓰레기통 뒤지기, 어깨 너머로 훔쳐보기(Shoulder Surfing)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 개인정보(Private Data)와 낚시(Fishing)의 합성어로, 신뢰할 만한 발신자로 위장한 이메일을 도구로 사용하여 가짜 사이트(피싱 사이트) 접속을 유도하는 수법은?</summary>
<blockquote>
<strong>정답:</strong> <strong>피싱 (Phishing)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) SMS(단문 메시지)와 피싱(Phishing)의 합성어로, 휴대전화 문자 메시지를 이용해 청첩장, 쿠폰 발송 등으로 위장한 링크 클릭을 유도하여 정보를 탈취하는 수법은?</summary>
<blockquote>
<strong>정답:</strong> <strong>스미싱 (Smishing)</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 사용자가 정상적인 URL 주소를 직접 입력하여 접속하더라도, hosts 파일 변조나 DNS 스푸핑 등을 통해 자동으로 가짜 사이트로 이동되게 하여 정보를 탈취하는 고도의 사기 수법은?</summary>
<blockquote>
<strong>정답:</strong> <strong>파밍 (Pharming)</strong>
</blockquote>
</details>

<details>
<summary>(서술형) **피싱(Phishing)**과 **파밍(Pharming)**의 결정적인 차이점을 '사용자의 접속 유도 방식'과 '주요 공격 기술' 관점에서 비교 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>피싱</strong>은 주로 발송된 이메일 내의 가짜 링크를 클릭하도록 사람을 직접 속이는 방식이지만, <strong>파밍</strong>은 사용자가 정식 주소를 입력하더라도 시스템의 <strong>hosts 파일</strong>이나 <strong>네트워크(DNS)</strong>를 기술적으로 조작하여 자동으로 가짜 사이트로 연결한다는 점이 다르다.
</blockquote>
</details>

<details>
<summary>(작업형) 다음 상황이 설명하는 인간 기반 사회공학 공격의 명칭을 무엇이라 하는가? "공격자가 청소 업체 직원으로 위장하여 중요한 암호화 키나 메모가 적힌 폐기물을 찾기 위해 회사의 전산실 폐기물 박스를 조사함"</summary>
<blockquote>
<strong>정답:</strong> <strong>쓰레기통 뒤지기 (Dumpster Diving)</strong>
</blockquote>
</details>

<details>
<summary>(서술형) 사회공학 기법이 기계적·시스템적인 보안 솔루션(방화벽, IDS 등)만으로는 방어하기 어려운 이유를 보안의 '주체' 관점에서 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> 사회공학 기법은 시스템의 기술적 취약점이 아니라 보안 체계의 가장 약한 연결 고리인 **'사람(사용자)'의 심리적 취약성**과 **신뢰**를 공격 대상으로 삼기 때문이다. 따라서 기술적 조치와 더불어 지속적인 교육과 구성원의 보안 인식 제고가 필수적이다.
</blockquote>
</details>

<details>
<summary>(단답형) 정보보호 및 개인정보보호를 위한 일련의 활동이 인증기준에 적합함을 증명하는 제도인 'ISMS-P' 인증의 총 인증항목 개수를 기술하시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>102개</strong> (1영역 16개, 2영역 64개, 3영역 22개)
</blockquote>
</details>

<details>
<summary>(단답형) ISO/IEC 27001 등 국제 표준에서 제시하는 정보보호 관리체계의 라이프사이클 모델로, 계획(Plan) → 실행(Do) → 점검(Check) → 개선(Act)의 4단계를 반복 수행하는 모델은?</summary>
<blockquote>
<strong>정답:</strong> <strong>PDCA 모델</strong>
</blockquote>
</details>

<details>
<summary>(단답형) ISMS-P의 3개 인증 영역 중, 개인정보의 수집, 보유, 제공, 파기 단계별 요구사항을 다루는 영역의 명칭은?</summary>
<blockquote>
<strong>정답:</strong> <strong>개인정보 처리 단계별 요구사항 (3영역)</strong>
</blockquote>
</details>

<details>
<summary>(서술형) 정보보호 정책 수립(1.1.5) 항목과 관련하여, 수립된 정책이 조직 내에서 공식적인 효력을 가지기 위해 반드시 수행해야 하는 두 가지 절차를 기술하시오.</summary>
<blockquote>
<strong>정답:</strong> 1. <strong>최고경영자(또는 경영진)의 승인</strong> 획득 <br> 2. <strong>임직원 및 관련자에게 공표(전달)</strong>
</blockquote>
</details>

<details>
<summary>(서술형) ISMS-P 기준에서 **정보보호 최고책임자(CISO)** 및 **개인정보 보호책임자(CPO)**를 지정할 때, 실질적인 의사결정권과 자원 할당 능력을 보장하기 위해 요구되는 직급상의 요건을 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> 예산, 인력 등 보안 관련 자원을 할당할 수 있는 권한을 가진 <strong>임원급</strong>으로 지정하여야 한다.
</blockquote>
</details>

<details>
<summary>(단답형) 위험 관리의 '정보 자산 식별(1.2.1)' 항목에서, 조직의 업무 특성에 따라 자산 분류 기준을 수립하여 기밀성, 무결성, 가용성 측면에서 산출해야 하는 자산 가치 척도는?</summary>
<blockquote>
<strong>정답:</strong> <strong>중요도</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 위험 관리의 '위험 평가(1.2.3)' 항목에서, 조직의 내·외부 환경 분석을 통해 자산의 취약점을 악용할 수 있는 잠재적 요인을 수집하는 기초 자료는?</summary>
<blockquote>
<strong>정답:</strong> <strong>위협 정보</strong>
</blockquote>
</details>

<details>
<summary>(작업형) '보호 대책 요구사항(2영역)'을 구성하는 12개 분야 중 5개 이상의 분야를 나열하시오.</summary>
<blockquote>
<strong>정답:</strong> (다음 중 5개 선택) <strong>정책/조직/자산관리, 인적보안, 외부자보안, 물리보안, 인증 및 권한관리, 접근통제, 암호화 적용, 정보시스템 도입 및 개발보안, 시스템 및 서비스 운영관리, 시스템 및 서비스 보안관리, 사고 예방 및 대응, 재해복구</strong>
</blockquote>
</details>

<details>
<summary>(단답형) 물리 보안 분야(2.4) 중, 외부 시스템이나 보조 저장 매체 등 허가되지 않은 기기가 보호 구역 내부로 반입되거나 외부로 유출되는 것을 방지하기 위한 통제 항목은?</summary>
<blockquote>
<strong>정답:</strong> <strong>반출입 기기 통제 (2.4.6)</strong>
</blockquote>
</details>

<details>
<summary>(서술형) ISMS 인증과 ISMS-P 인증을 신청할 때, 적용받는 인증 기준 영역의 구성적인 차이점을 설명하시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>ISMS 인증</strong>은 1영역(관리체계 수립 및 운영)과 2영역(보호 대책 요구사항)의 총 80개 항목을 평가받지만, <strong>ISMS-P 인증</strong>은 여기에 3영역(개인정보 처리 단계별 요구사항) 22개 항목을 추가하여 총 102개 항목에 대해 평가를 받는다.
</blockquote>
</details>

<details>
<summary>(단답형) 위험 관리 과정에서 수용 가능한 목표 위험 수준을 설정할 때, 경영진의 의사결정에 의해 결정되는 목표 위험 수치를 무엇이라 하는가?</summary>
<blockquote>
<strong>정답:</strong> <strong>DoA (Degree of Assurance)</strong>
</blockquote>
</details>

<details>
<summary>[기출 12회 9번 문제] (단답형) 정보보호 제품의 보안성을 평가하기 위한 공통 평가 기준(CC, Common Criteria)의 구성요소 3가지를 쓰시오.</summary>
<blockquote>
<strong>정답:</strong> (A) <strong>EAL (Evaluation Assurance Level)</strong>, (B) <strong>PP (Protection Profile)</strong>, (C) <strong>ST (Security Target)</strong><br>
<strong>해석:</strong><br>
- <strong>EAL:</strong> 평가 보증 수준으로, 제품의 보안성을 얼마나 정밀하게 검증했는지를 나타내는 단계(1~7단계)<br>
- <strong>PP:</strong> 사용자(소비자)가 요구하는 보안 기능 요구사항을 집합적으로 정의한 문서<br>
- <strong>ST:</strong> 개발자가 특정 제품(TOE)의 보안 기능을 설명하고 PP와의 부합성을 기술한 문서
</blockquote>
</details>

<details>
<summary>정보보호 관리체계(ISMS)의 수립 및 운영을 위한 국제 표준 번호를 작성하시오.</summary>
<blockquote>
ISO/IEC 27001
</blockquote>
</details>

<details>
<summary>정보보호 및 개인정보보호 관리체계 인증(ISMS-P)에서, 조직 구조의 변경이나 법/규제 변경, 보안 사고 발생 시 조직이 기존에 수립된 정보보안 대책들을 재검토하고 지속적인 개선을 위해 주기적으로 수행해야 하는 활동의 명칭을 쓰시오.</summary>
<blockquote>
사후 심사 (또는 지속적 위험 평가)
</blockquote>
</details>

### 제로 트러스트 (Zero Trust Architecture)

<details>
<summary>(단답형) "절대 믿지 말고, 항상 검증하라(Never Trust, Always Verify)"는 원칙에 기반하며, 내부망일지라도 신뢰하지 않고 모든 접근 요청에 대해 세밀한 인증과 최소 권한을 부여하는 보안 모델의 명칭을 쓰시오.</summary>
<blockquote>
제로 트러스트 (Zero Trust)<br><br>
※ 참고: 기존 보안이 '경계(Perimeter)' 중심이었다면, 제로 트러스트는 '아이덴티티(Identity)' 중심입니다. 네트워크 내부라도 무조건 신뢰하지 않고, 모든 접속 요청마다 사용자 신원, 기기 상태, 문맥(Context)을 매번 검증하는 것이 핵심입니다.
</blockquote>
</details>

<details>
<summary>(서술형) 제로 트러스트 아키텍처에서 '경계 기반 보안(Perimeter-based Security)'의 한계를 극복하는 핵심 개념을 기술하시오.</summary>
<blockquote>
전통적인 경계 보안은 한 번 내부망에 접속하면 내부 자원에 자유롭게 접근할 수 있는 '신뢰 영역'이 존재한다. 제로 트러스트는 <strong>위치에 상관없이</strong> 자격 증명, 기기 상태, 접속 환경 등을 매번 검증하며, 자산 단위로 접근을 제어(Micro-segmentation)하여 내부 위협이나 침투 확산을 원천 차단한다.
</blockquote>
</details>

<details>
<summary>(단답형) 제로 트러스트 모델에서 접근 결정 과정을 관리하는 구성 요소 중, 정책에 따라 리소스 접근 허용 여부를 최종 결정하는 '두뇌' 역할을 하는 곳을 영문 약어로 쓰시오.</summary>
<blockquote>
<code>PDP</code> (Policy Decision Point)<br><br>
※ 참고: 제로 트러스트 아키텍처의 '두뇌'에 해당합니다. 사용자 정보, 기기 보안 상태, 위협 인텔리전스 등 다양한 데이터를 종합하여 특정 리소스에 대한 접근 허용 여부를 동적으로 결정합니다.
</blockquote>
</details>

<details>
<summary>(단답형) PDP의 결정을 실제 리소스 접점에서 실행하여, 사용자와 리소스 사이의 연결을 생성하거나 차단하는 역할을 수행하는 지점의 영문 약어를 쓰시오.</summary>
<blockquote>
<code>PEP</code> (Policy Enforcement Point)<br><br>
※ 참고: PDP의 결정을 실제로 수행하는 '게이트웨이' 역할을 합니다. 사용자와 리소스 사이의 접점(에이전트, 게이트웨이 등)에서 트래픽을 허용하거나 차단하여 보안 정책을 실시간으로 강제합니다.
</blockquote>
</details>

<details>
<summary>(서술형) 제로 트러스트의 7가지 기본 원칙(NIST SP 800-207) 중 '모든 통신은 위치에 상관없이 보호되어야 한다'는 원칙의 의미를 서술하시오.</summary>
<blockquote>
사용자가 기업 내부망(LAN)에 있든 외부망에 있든 동일한 보안 수준의 검증과 암호화가 적용되어야 함을 의미한다. 즉, '내부망은 안전하다'는 전제를 폐기하는 것이다.
</blockquote>
</details>

<details>
<summary>(단답형) 제로 트러스트 구현을 위한 핵심 기술 중 하나로, 네트워크를 아주 작은 단위로 쪼개어 특정 서버나 서비스 간의 통신만 선별적으로 허용하는 기술을 무엇이라 하는가?</summary>
<blockquote>
마이크로 세그멘테이션 (Micro-segmentation)<br><br>
※ 참고: 네트워크를 워크로드나 서비스 단위로 아주 세밀하게 분할하여 관리합니다. 이를 통해 공격자가 내부망에 한 번 침투하더라도 다른 서버로 확산되는 '횡적 이동(Lateral Movement)'을 물리적으로 차단하는 효과가 있습니다.
</blockquote>
</details>

<details>
<summary>(서술형) 제로 트러스트 환경에서 '기기 상태 확인(Device Posture)'이 중요한 이유를 보안 관점에서 설명하시오.</summary>
<blockquote>
인가된 사용자일지라도 탈취되거나 보안 패치가 되지 않은 취약한 기기를 통해 접속할 경우 내부망 전체가 위험해질 수 있다. 따라서 접속 시점에 기기의 OS 버전, 백신 실행 여부, 탈옥 여부 등을 실시간 확인하여 접근 권한을 동적으로 부여하기 위함이다.
</blockquote>
</details>

<details>
<summary>(단답형) 사용자 계정과 기기 정보뿐만 아니라 접속 시간, 위치, 이상 행위 여부 등 다양한 '맥락' 정보를 분석하여 접근을 제어하는 제로 트러스트의 특성을 무엇이라 하는가?</summary>
<blockquote>
문맥 기반 접근 제어 (Context-aware Access Control)
</blockquote>
</details>

<details>
<summary>(단답형) 제로 트러스트 프레임워크 중 하나로, 사용자에게 자산이나 네트워크 전체를 노출하지 않고 필요한 애플리케이션에만 안전하게 연결해주는 기술의 영문 약어를 쓰시오.</summary>
<blockquote>
<code>ZTNA</code> (Zero Trust Network Access)<br><br>
※ 참고: 과거의 VPN을 대체하는 기술로, 사용자에게 네트워크 전체에 대한 IP 접근권을 주는 대신 인증된 특정 '애플리케이션'에만 안전하게 연결해줍니다. 자산을 외부에 노출하지 않는 '검은색 네트워크(Dark Network)' 환경을 구현합니다.
</blockquote>
</details>

<details>
<summary>(작업형) 제로 트러스트 도입 시나리오의 빈칸 (A), (B)를 채우시오.<br>
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
- 단계 1: <code>( A )</code> 을(를) 통해 네트워크 전반의 가시성을 확보하고 세부 통제 단위를 정의한다.<br>
- 단계 2: 단일 인증 수단이 아닌 <code>( B )</code> (을)를 필수 적용하여 계정 정보 유출에 대비한 다중 방어 체계를 구축한다.
</div>
</summary>
<blockquote>
(A) 마이크로 세그멘테이션<br>
(B) MFA (Multi-Factor Authentication, 다중 요소 인증)
</blockquote>
</details>

### MITRE ATT&CK 및 침해사고 분석

<details>
<summary>(단답형) 사이버 공격자의 전술(Tactics), 기법(Techniques), 상식(Common Knowledge)을 체계적으로 분류한 글로벌 지식 베이스로, 대응 중심의 보안 체계를 구축하는 데 사용되는 이 프레임워크는?</summary>
<blockquote>
<code>MITRE ATT&CK</code> (마이터 어택)<br><br>
※ 참고: 실제 공격 사례를 바탕으로 공격자의 행동 양식을 체계화한 매트릭스입니다. 보안 장비의 탐지 범위를 점검하거나, 위협 헌팅 시나리오를 작성할 때 전 세계적으로 가장 널리 쓰이는 표준 프레임워크입니다.
</blockquote>
</details>

<details>
<summary>(서술형) MITRE ATT&CK 프레임워크에서 'Tactics(전술)'와 'Techniques(기법)'의 차이점을 설명하시오.</summary>
<blockquote>
<strong>Tactics</strong>는 공격자가 달성하려는 궁극적인 보안 목표(예: 권한 상승, 데이터 유출 등)를 의미하며 'Why'에 해당한다. <strong>Techniques</strong>는 그 목표를 달성하기 위해 사용하는 구체적인 수단이나 방법(예: 프로세스 인젝션, 무차별 대입 등)을 의미하며 'How'에 해당한다.
</blockquote>
</details>

<details>
<summary>(단답형) 공격자가 공격의 효율성을 높이기 위해 사용하는 스크립트, 도구, 코드 조각 등을 의미하며 ATT&CK 매트릭스의 하위 요소로 정의되는 이것은?</summary>
<blockquote>
절차 (Procedures) (또는 TTP의 P)
</blockquote>
</details>

<details>
<summary>(서술형) 보안 운영 센터(SOC)에서 MITRE ATT&CK을 활용하여 '보안 장비의 탐지 공백(Gap Analysis)'을 분석하는 방법을 기술하시오.</summary>
<blockquote>
현재 보유한 보안 장비(IDS, EDR 등)가 ATT&CK 매트릭스 상의 어떤 기법들을 탐지할 수 있는지 매핑해본다. 이를 통해 장비가 탐지하지 못하는 빈 영역(Gap)을 파악하고 하니팟 도입이나 룰 보강 등의 대책을 세울 수 있다.
</blockquote>
</details>

<details>
<summary>(단답형) 공격자가 초기 침투 후 내부망의 다른 시스템으로 공격 범위를 넓혀가는 단계적 과정을 ATT&CK 전술 중 무엇이라 하는가?</summary>
<blockquote>
횡적 이동 (Lateral Movement)<br><br>
※ 참고: 공격자가 내부망에 초기 진입한 후, 더 가치 있는 정보가 있는 다른 시스템을 찾기 위해 망 내부를 가로질러 이동하는 단계입니다. 제로 트러스트와 마이크로 세그멘테이션이 이를 방어하는 핵심 대책입니다.
</blockquote>
</details>

<details>
<summary>(서술형) ATT&CK 프레임워크가 '사이버 킬 체인(Cyber Kill Chain)' 모델과 비교하여 실무적으로 가지는 장점을 대응 관점에서 서술하시오.</summary>
<blockquote>
사이버 킬 체인은 공격 단계(7단계)를 선형적으로 정의하여 한 단계만 끊으면 된다는 개념이나, ATT&CK은 실제 공격 현장의 방대한 기법들을 비선형적인 매트릭스 형태로 제공하여 실질적인 탐지 시나리오를 만들고 정교한 위협 헌팅을 수행하는 데 훨씬 유리하다.
</blockquote>
</details>

<details>
<summary>(단답형) 공격자가 사용하는 특정 공격 그룹이나 악성코드 캠페인의 정보를 ATT&CK 기법과 연결하여 관리하는 리소스의 명칭은?</summary>
<blockquote>
공격 그룹 (Groups) (예: APT38, Lazarus 등)
</blockquote>
</details>

<details>
<summary>(서술형) ATT&CK의 'Persistence(지속성)' 전술에 해당하는 기법 중 하니를 제시하고 그 보안적 위험을 설명하시오.</summary>
<blockquote>
<strong>예시 기법</strong>: 레지스트리 Run 키 등록, 스케줄 작업 생성 등<br>
<strong>위험성</strong>: 시스템이 재부팅되더라도 악성코드가 자동으로 다시 실행되도록 구성하여, 공격자가 대상 시스템에 대한 장기적인 접근 권한을 유지하게 만든다.
</blockquote>
</details>

<details>
<summary>(단답형) 침해사고 분석 시, 공격자가 사용한 IP, 해시값, 도메인 등을 의미하며 위협 정보를 공유할 때 사용하는 이 지표의 명칭은?</summary>
<blockquote>
<code>IoC</code> (Indicator of Compromise, 침해 지표)<br><br>
※ 참고: 악성코드의 해시(Hash), 공격자 IP, C&C 서버 도메인 등 '공격의 흔적'을 의미합니다. 보안 커뮤니티에서 IoC를 신속하게 공유함으로써 유사한 공격을 전파 전에 차단하는 위협 인텔리전스(TI)의 기초가 됩니다.
</blockquote>
</details>

<details>
<summary>(작업형) 다음 상황을 ATT&CK 전술 단계로 나누시오.<br>
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
1) 이메일 피싱을 통해 직원의 PC를 감염시킴: <code>( A )</code><br>
2) 관리자 계정의 해시 정보를 탈취하여 관리자 권한을 획득함: <code>( B )</code><br>
3) 수집된 내부 기밀 문서를 외부 C&C 서버로 전송함: <code>( C )</code>
</div>
</summary>
<blockquote>
(A) 초기 침투 (Initial Access)<br>
(B) 권한 상승 (Privilege Escalation)<br>
(C) 유출 (Exfiltration)
</blockquote>
</details>

### 망 분리 및 자산 보안 관리

<details>
<summary>[기출 12회 11번 문제] (단답형/서술형) 네트워크 보안 강화를 위한 망 분리(Network Separation) 기술 중, 서버 측에 가상 머신(VM)을 생성하여 사용자에게 할당하고 접속하도록 하는 논리적 망 분리 방식을 무엇이라 하는가?</summary>
<blockquote>
<strong>정답:</strong> <strong>VDI (Virtual Desktop Infrastructure, 가상 데스크톱 인프라)</strong> (또는 SBC 기반 망 분리)
</blockquote>
</details>

<details>
<summary>[기출 12회 12번 문제] (단답형) 정보보호 관리체계(ISMS) 인증 시 보안 장비(방화벽, IPS 등)의 계정 관리와 관련된 다음 물음에 답하시오.
1) 제조사에서 초기 설정한 기본 계정을 그대로 사용하는 것을 금지하는 보안 원칙: <strong>( A )</strong><br>
2) 한 사람 이상의 운영자가 동일한 계정을 공유하여 사용하는 것을 금지하는 원칙: <strong>( B )</strong><br>
3) 관리자가 일정 횟수 이상 로그인 실패 시 일정 시간 동안 접속을 차단하는 기능: <strong>( C )</strong>
</summary>
<blockquote>
<strong>정답:</strong><br>
(A) <strong>디폴트 계정(Default Account) 사용 금지</strong> (또는 패스워드 변경 정책)<br>
(B) <strong>1인 1계정 할당</strong> (또는 계정 공유 금지)<br>
(C) <strong>임계값 기반 로그인 잠금 (Login Lockout)</strong>
</blockquote>
</details>

### SOAR (보안 운영 자동화 및 대응)

<details>
<summary>(단답형) 다양한 보안 솔루션에서 발생하는 경고 정보를 통합하고, 표준화된 대응 절차에 따라 사고 처리를 자동화하여 보안 운영의 효율성을 극대화하는 플랫폼의 영문 약어를 쓰시오.</summary>
<blockquote>
<code>SOAR</code> (Security Orchestration, Automation and Response)<br><br>
※ 참고: 보안 관제의 '자동화 엔진'입니다. 수많은 보안 장비의 로그 중 사람이 일일이 대응하기 어려운 반복적인 작업을 자동 처리하여 사고 대응 속도(MTTR)를 높이고 관제 인력의 피로도를 낮춰줍니다.
</blockquote>
</details>

<details>
<summary>(서술형) SOAR의 핵심 구성 요소 중 하나인 '플레이북(Playbook)'의 개념과 역할을 서술하시오.</summary>
<blockquote>
<strong>개념</strong>: 특정 보안 이벤트(예: 악성 IP 탐지)가 발생했을 때 수행해야 할 대응 단계를 워크플로우 형태로 정형화한 시나리오이다.<br>
<strong>역할</strong>: 사람의 개입 없이 IP 차단, 티켓 생성, 담당자 알림 등을 자동 실행하여 대응 시간(MTTR)을 단축시킨다.
</blockquote>
</details>

<details>
<summary>(단답형) 여러 보안 장비(방화벽, EDR, SIEM 등)의 API를 연동하여 하나의 통합된 흐름으로 제어하는 기능을 SOAR의 3요소 중 무엇이라 하는가?</summary>
<blockquote>
보안 오케스트레이션 (Security Orchestration)
</blockquote>
</details>

<details>
<summary>(서술형) 보안 운영에서 SIEM과 SOAR의 관계 및 차이점을 '분석'과 '대응' 관점에서 비교 서술하시오.</summary>
<blockquote>
<strong>SIEM</strong>은 이기종 장비의 로그를 수집·상관분석하여 이상 징후를 '탐지'하고 알람을 주는 데 집중한다. <strong>SOAR</strong>는 SIEM에서 넘겨받은 알람을 바탕으로 미리 정의된 절차에 따라 실제 '대응(조치)' 작업을 자동화하여 처리하는 데 중점을 둔다.
</blockquote>
</details>

<details>
<summary>(단답형) SOAR 도입의 주요 지표 중 하나로, 침해 사고가 발생한 시점부터 대응이 완료될 때까지 걸리는 평균 시간을 의미하는 용어는?</summary>
<blockquote>
<code>MTTR</code> (Mean Time To Respond / Remediation)<br><br>
※ 참고: 보안 사고 발생 시점부터 조치가 완료될 때까지의 평균 시간을 의미합니다. SOAR 도입의 가장 큰 목적 중 하나는 이 MTTR을 획기적으로 줄여 공격자가 머무는 시간(Dwell Time)을 최소화하는 것입니다.
</blockquote>
</details>

<details>
<summary>(서술형) SOAR가 보안 담당자의 '경고 피로(Alert Fatigue)'를 해결하는 원리를 기술하시오.</summary>
<blockquote>
매일 발생하는 수만 건의 보안 경고 중 단순 반복적이거나 오탐으로 판명된 이벤트들을 플레이북이 자동 처리하거나 필터링해준다. 이를 통해 담당자는 실제 확인이 필요한 고위험 이벤트 분석에만 집중할 수 있게 된다.
</blockquote>
</details>

<details>
<summary>(작업형) SOAR를 이용한 '악성 이메일 대응' 플레이북의 빈칸 (A), (B)를 순서대로 채우시오.<br>
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
1) SIEM으로부터 의심 메일 알람 수신<br>
2) 메일 본문의 URL을 위협 인텔리전스(TI) 서버에 조회하여 <code>( A )</code> 검사 수행<br>
3) 악성 확인 시, 메일 서버에서 해당 메일 일괄 삭제 및 유포지 IP <code>( B )</code> 조치 수행
</div>
</summary>
<blockquote>
(A) 평판 (Reputation) (또는 악성 여부)<br>
(B) 차단 (Blocking)
</blockquote>
</details>

<details>
<summary>[기출 24회 8번 문제] (단답형) 기업 내부의 기밀 정보가 외부로 유출되는 것을 감시하고 차단하는 데이터 유출 방지(DLP) 시스템의 3가지 주요 구성 요소를 각각 쓰시오.</summary>
<blockquote>
<strong>정답:</strong> <strong>Endpoint (또는 디바이스), Network, Storage</strong><br>
<strong>해설:</strong> DLP는 데이터의 위치와 상태(사용중, 전송중, 저장중)에 따라 엔드포인트 솔루션, 네트워크 게이트웨이, 저장매체 전체를 보호 범위로 합니다.
</blockquote>
</details>
