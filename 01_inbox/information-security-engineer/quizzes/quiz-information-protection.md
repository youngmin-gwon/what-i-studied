---
title: quiz-information-protection
tags: [정보보안기사, 정보보안실기, 정보보호일반]
aliases: []
date modified: 2026-03-25 09:28:41 +09:00
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
</details>

### 정보 보호 정책

### 위험 관리

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

### Digital Forensic

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

### 공통평가기준(CC: Common Criteria)

### 사회공학 기법

### 정보보호 및 개인정보보호 관리체계(ISMS-P) 인증

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
