---
title: quiz_system
tags: []
aliases: []
date modified: 2026-03-04 14:27:46 +09:00
date created: 2026-02-25 10:46:47 +09:00
---

## 🛡️ 정보보안기사 실기 Quiz

### 공부노트
#### 1. 윈도우 기본 학습

##### 인증 암호 알고리즘

<details>
<summary>윈도우 인증 프로토콜 중 챌린지-응답 방식을 사용하는 구형 프로토콜과 티켓 기반의 현대적 프로토콜의 명칭을 각각 쓰시오.</summary>
<blockquote>
NTLM (NT LAN Manager), Kerberos (커버로스)
</blockquote>
</details>

##### LAN Manager 인증 수준
#### 패스워드 크래킹
##### 사전 공격/사전 대입 공격
<details>
<summary>사용자 계정의 패스워드를 알아내기 위해 가능한 모든 조합을 시도하는 공격 기법과, 의미 있는 단어가 담긴 파일을 대입하는 공격 기법의 명칭을 각각 쓰시오.</summary>
<blockquote>
무차별 대입 공격 (Brute-Force Attack), 사전 공격 (Dictionary Attack)
</blockquote>
</details>

##### 무차별 공격


<details>
<summary>(서술형) 윈도우 시스템에서 'SAM(Security Account Manager) 파일'의 정의를 쓰고, 이 파일에 대한 공격을 차단하기 위해 적용할 수 있는 보안 대책 2가지를 서술하시오.</summary>
<blockquote>
정의: 사용자 계정 및 암호화된 패스워드 정보를 저장하고 있는 윈도우 레지스트리 데이터베이스이다.<br><br>
보안 대책:<br>
1. 'SAM 계정과 공유의 익명 열거 허용 안 함' 정책을 설정하여 공격자가 계정 정보를 수집하지 못하도록 차단한다.<br>
2. Syskey 등을 사용하여 시스템 부팅 시 추가적인 암호화 키를 요구하도록 설정한다.
</blockquote>
</details>

<details>
<summary>시스템 인프라 보안 진단 시 윈도우의 SAM(Security Account Manager) 파일에 대한 접근 통제 설정 상태를 점검하는 것은 매우 중요합니다. 다음 빈칸 (A), (B), (C)에 들어갈 알맞은 내용을 작성하시오.<br>
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<strong>[상황 및 조치 사항]</strong><br>
- 점검 목적: 공격자가 계정 정보에 접근하여 패스워드 공격(무차별 대입 등) 시도에 따른 심각한 정보 노출 위협이 발생하는 것을 방지하기 위함이다.<br>
- 설정 경로: SAM 파일은 윈도우 설치 디렉터리 하위에 존재하며, 해당 폴더의 기본 경로는 일반적으로 <code>( A )</code> 이다.<br>
- 양호 기준: 악의적 유출을 막기 위해 SAM 파일에 대해서는 <code>( B )</code> 와 <code>( C )</code> 구룹에게만 접근을 허용하고, 그 외 불필요한 일반 사용자 및 특정 그룹에 대해서는 모든 접근 권한(읽기/쓰기 등)을 제거해야 한다.
</div>
</summary>
<blockquote>
(A) C:\Winnt\System32\config 또는 C:\Windows\System32\config (디렉터리 루트인 C:\Windows 또는 C:\Winnt 로 적어도 무방함)<br>
(B) Administrators<br>
(C) System
</blockquote>
</details>

<details>
<summary>점검 스크립트를 통해 윈도우 서비스 콘솔 및 프로세스를 분석하던 중, 시스템의 가장 핵심적인 보안 서브시스템 런타임 환경 상태를 점검해야 한다는 권고가 나왔습니다. 앞서 언급된 LSA, SAM 모듈 등 인증 기능 전반을 백그라운드 프로세스 형태로 구동시켜 보안 인증 패키지를 관리하는 이 프로세스(실행 파일)의 명칭(A)은 무엇인지 영문 소문자로 쓰시오.</summary>
<blockquote>
lsass.exe (Local Security Authority Subsystem Service)<br><br>
※ 참고: 서버 운영 관점에서 lsass.exe 프로세스의 과도한 자원 소모, 그리고 악성코드가 이 프로세스를 위장하거나 메모리를 덤프하여 패스워드 정보를 추출(예: Mimikatz 도구 등)하는 공격기법 등이 실무상 가장 흔하게 발생하므로 집중 점검 대상이 됩니다.
</blockquote>
</details>

<details>
<summary>윈도우 시스템에서 사용자 계정 및 패스워드 정보를 암호화하여 저장하는 데이터베이스의 명칭과 해당 파일이 저장되는 레지스트리 경로를 작성하시오.</summary>
<blockquote>
SAM (Security Account Manager), HKEY_LOCAL_MACHINE\SAM
</blockquote>
</details>

#### 윈도우 보안 식별자

##### 개요

<details>
<summary>윈도우 운영체제에서 사용자가 로그인을 수행하면 생성되는 객체로, 해당 사용자와 속한 모든 작업 그룹들에 관한 '보안 식별자(SID)' 정보를 담고 있는 것의 명칭을 쓰시오.</summary>
<blockquote>
접근 토큰 (액세스 토큰, Access Token)
</blockquote>
</details>

<details>
<summary>(서술형) 윈도우 시스템에서 '보안 식별자(SID)'의 정의를 기술하고, 사용자가 로그인한 이후 실행하는 모든 프로세스에 권한이 어떻게 부여되는지 SID와 접근 토큰을 연관 지어 서술하시오.</summary>
<blockquote>
<strong>정의</strong>: 윈도우의 각 사용자나 그룹에 부여되는 고유한 식별 번호이다.<br><br>
<strong>권한 부여 과정</strong>: 사용자가 로그인을 수행하면 사용자 및 소속 그룹의 SID 정보가 담긴 '접근 토큰(액세스 토큰)'이 생성되며, 이후 해당 사용자가 시작하는 모든 프로세스에 이 접근 토큰의 사본이 할당되어 권한이 상속된다.
</blockquote>
</details>

##### 구조 및 실습

<details>
<summary>다음은 윈도우의 SID(보안 식별자) 구조와 확인 명령어에 대한 설명이다. 빈칸 (A), (B), (C)에 알맞은 내용을 작성하시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<strong>[상황 및 설명]</strong><br>
- 특정 사용자의 SID가 <code>S-1-5-21-4243233100…-500</code>으로 확인되었다. 여기서 맨 앞의 'S-1'은 윈도우 시스템을 의미하고, 마지막 식별자(ID) '500'은 ( A ) 계정을 의미한다. 반면 게스트(Guest) 계정은 501, 일반 사용자는 1000 이상의 값을 가진다.<br>
- 시스템 내의 사용자 계정 SID 및 패스워드 정보는 주로 <code>%SystemRoot%\System32\config\</code> 경로에 암호화되어 위치한 ( B ) 파일에 저장되고 관리된다.<br>
- 관리자는 윈도우 관리 명령 콘솔인 ( C ) 환경에서 <code>useraccount list brief</code> 명령어를 실행하여 시스템에 등록된 계정별 SID를 한눈에 확인할 수 있다.
</div>
</summary>
<blockquote>
(A) 관리자 (Administrator)<br>
(B) SAM<br>
(C) WMIC (Windows Management Instrumentation Console)
</blockquote>
</details>

#### 윈도우 인증 구조
##### 개요

<details>
<summary>윈도우 인증 구성 요소 중 다음 빈칸 (A), (B), (C)에 해당하는 영문 약어를 쓰시오.<br>
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<strong>[보기]</strong><br>
(A): 모든 계정의 로그인에 대한 검증 및 접근 권한을 검사하며, 계정명과 SID를 매칭하고 감사 로그를 기록하는 '보안 서브시스템'이다.<br>
(B): 사용자 계정 정보와 암호화된 패스워드 정보를 보유한 데이터베이스를 관리하며, 입력된 정보와 저장된 패스워드를 비교하여 인증 여부를 결정한다.<br>
(C): 인증된 사용자에게 SID를 부여하고, 이를 기반으로 객체(파일, 디렉터리 등)에 대한 접근 허용 여부를 결정하며 관련된 감사 메시지를 생성한다.
</div>
</summary>
<blockquote>
(A) LSA (Local Security Authority)<br>
(B) SAM (Security Account Manager)<br>
(C) SRM (Security Reference Monitor)
</blockquote>
</details>

<details>
<summary>(서술형) 윈도우의 주요 보안 구성 요소인 SRM(Security Reference Monitor)과 LSA(Local Security Authority)는 객체 접근 통제 시 긴밀하게 협력한다. 특히 사용자가 특정 파일이나 디렉터리에 접근하려 할 때, '권한 검사' 및 '감사 로그 처리' 측면에서 두 서비스가 역할을 어떻게 분담하는지 서술하시오.</summary>
<blockquote>
SRM은 사용자에게 부여된 특권 및 SID 기반으로 해당 파일이나 디렉터리에 대한 접근 허용 여부를 검사·결정하고, 그에 대한 '감사 메시지'를 독립적으로 생성한다. LSA는 SRM이 생성하여 전달한 이 감사 메시지를 받아 실제 보안 로그(Event Log)에 '기록'하는 역할을 분담하여 수행한다.
</blockquote>
</details>

<details>
<summary>(서술형) LSA(lsass.exe) 내에서 실제 패스워드 검증을 수행하는 구성 요소와 저장소인 SAM의 관계를 서술하시오.</summary>
<blockquote>
SAM은 계정의 패스워드 해시 값을 보관하는 데이터베이스 역할을 하며, LSA 내의 인증 패키지(MSV1_0 등)가 SAM으로부터 해시 값을 전달받아 사용자가 입력한 값과 비교하여 검증을 수행함.
</blockquote>
</details>

<details>
<summary>(서술형) Winlogon이 LSA를 직접 실행하지 않음에도 불구하고, 인증 과정에서 수행하는 핵심적인 역할 2가지를 서술하시오.</summary>
<blockquote>
1. 사용자가 자격 증명을 입력할 수 있는 대화식 로그온 UI를 제공하고 관리함.<br>
2. 사용자가 입력한 정보를 보안 서브시스템인 LSA에 전달하여 인증을 요청하고, 성공 시 액세스 토큰을 받아 사용자 세션을 시작함.
</blockquote>
</details>

<details>
<summary>(서술형) 윈도우의 SRM(Security Reference Monitor)이 커널 모드에서 수행하는 보안 통제 기능을 액세스 토큰과 연계하여 설명하시오.</summary>
<blockquote>
SRM은 사용자가 파일이나 폴더 등 개체에 접근할 때마다, 해당 사용자의 액세스 토큰에 포함된 권한 정보(SID 등)를 개체의 ACL(Access Control List)과 비교하여 접근 허용 여부를 최종적으로 결정하고 감시함.
</blockquote>
</details>

<details>
<summary>(서술형) 도우에서 지원하는 볼륨 단위 암호화 기능인 BitLocker의 특징 2가지를 서술하시오.</summary>
<blockquote>
1. 윈도우 운영체제에서 제공하는 볼륨 단위 암호화 기능이다.<br>2. 컴퓨터 부팅에 필요한 시스템 파티션 부분까지 암호화하여 보호할 수 있다.
</blockquote>
</details>
#### 윈도우 인증과정
##### 윈도우 인증 구성 요소

##### 로컬 인증

<details>
<summary>윈도우 시스템에서 사용자가 로그인을 시도할 때, 로컬 인증과 원격(도메인) 인증은 서로 다른 모듈 및 프로토콜을 사용한다. 로컬 인증 과정에서 LSA 서브시스템이 인증 정보를 넘겨주는 모듈의 명칭(A)과, 도메인 인증 과정에서 LSA가 도메인 컨트롤러(DC)에 인증을 요청하기 위해 사용하는 프로토콜의 명칭(B)을 각각 쓰시오.</summary>
<blockquote>
(A) NTLM<br>
(B) 커버로스 (Kerberos)
</blockquote>
</details>

<details>
<summary>(서술형) 윈도우 운영체제 환경에서 사용자가 로그인 창(Winlogon)을 통해 '로컬 인증'을 수행할 때 거치게 되는 핵심 동작 과정을 구성요소인 LSA, NTLM, SAM의 상호작용 흐름을 중심으로 서술하시오.</summary>
<blockquote>
사용자가 아이디와 패스워드를 입력하면, LSA(Local Security Authority) 서브시스템이 이 인증 정보를 받아 NTLM 모듈로 전달하고, 이를 다시 SAM(Security Account Manager)이 받아 자신의 데이터베이스에 저장된 암호화된 패스워드와 비교하여 최종적으로 로그인 처리를 수행한다.
</blockquote>
</details>

##### 원격 인증

<details>
<summary>윈도우 원격(도메인) 인증 과정에서 커버로스 프로토콜을 이용해 전달받은 인증 정보를 직접 확인하고 검증하는 중앙 주체의 명칭(A)과, 인증 성공 시 해당 주체가 사용자에게 부여하여 프로세스 실행 권한을 증명하는 객체의 명칭(B)을 쓰시오.</summary>
<blockquote>
(A) 도메인 컨트롤러 (DC, Domain Controller)<br>
(B) 접근 토큰 (Access Token)
</blockquote>
</details>

<details>
<summary>윈도우 도메인(Active Directory) 환경에서 중앙 집중식 인증을 위해 Netlogon 서비스가 통신하는 대상의 명칭은?</summary>
<blockquote>
도메인 컨트롤러 (Domain Controller, DC)
</blockquote>
</details>

<details>
<summary>윈도우 '원격(도메인) 인증' 과정은 로컬 인증과 구별되는 처리 주체가 존재한다. 아이디와 패스워드 입력 이후 도메인 컨트롤러(DC)가 인증 처리를 완료하여 사용자가 자원에 접근할 수 있게 되기까지의 핵심 과정을 서술하시오.</summary>
<blockquote>
LSA 서브시스템이 도메인 인증임을 확인한 후, 커버로스(Kerberos) 프로토콜을 이용하여 도메인 컨트롤러(DC)에 인증을 요청한다. 요청을 받은 도메인 컨트롤러는 직접 인증 정보를 확인 및 검증하고, 접속하려는 사용자에게 권한이 부여된 '접근 토큰(Access Token)'을 발급하여 해당 권한으로 프로세스를 실행할 수 있게 한다.
</blockquote>
</details>

##### SAM 파일 접근통제 설정

<details>
<summary>윈도우 부팅 시 보안 서브시스템(LSA)과 Winlogon을 실행하는 세션 관리 프로세스의 명칭은?</summary>
<blockquote>
SMSS (Session Manager Subsystem)
</blockquote>
</details>

<details>
<summary>윈도우에서 'NT'의 약자와, 현대 윈도우 보안의 근간이 되는 파일 시스템의 명칭을 쓰시오.</summary>
<blockquote>
NT (New Technology), NTFS (NT File System)
</blockquote>
</details>

<details>
<summary>부팅 시 드라이버 및 보안 정책 정보를 담고 있으며, SAM 파일이 실제로 저장되는 레지스트리 루트 키(Hive)의 명칭은?</summary>
<blockquote>
HKEY_LOCAL_MACHINE (HKLM)
</blockquote>
</details>

<details>
<summary>다음의 빈칸 (A), (B), (C) 에 적절한 용어를 기술하시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<strong>[보기]</strong><br>
Windows Server 운영체제에서 사용자 계정관리방식은 워크그룹(Workgroup) 방식과 <string>(A)</strong> 방식이 있으며, 로컬 사용자 계정은 %SystemRoot%\System32\config\<string>(B)</string> 에 저장되고 있고, <string>(A)</string> 방식은 <string>(C)</string> 데이터베이스에 저장된다.
</div>
</summary>
<blockquote>
(A) 도메인 (Domain)<br>
(B) SAM<br>
(C) Active Directory<br><br>

윈도우 서버의 계정관리방식은 다음과 같이 2 개로 구분할 수 있다.<br>

1. Workgroup 방식<br>
	- 각각의 계정과 자원을 시스템별로 관리하는 방식으로 소규모 네트워크에 적합하다.<br>
	- "피어 투 피어"라고도 하며 전용 서버 없이 모든 시스템이 서버이면서 클라이언트 기능을 가지며 서로 동등하다.<br>
	- 서버 관리자가 필요 없으며 보안 관련 정보는 각 시스템의 로컬 디렉터리 데이터베이스(SAM DB)에 의해 제공 된다.<br>
	- Active Directory 가 구축되지 않은 상태로서 다른 시스템에 접근할 때 수시로 엑세스에 필요한 사용자 계정과 암호를 요구한다.<br><br>

2. Domain 방식<br>
	- 모든 계정과 자원을 특정 서버에서 관리하는 중앙 집중식 방식이다.<br>
	- 사용자에게 적절한 사용 권한을 설정하면 사용자는 다른 컴퓨터에 자원을 지정한 권한대로 접근할 수 있다.<br>
	- Active Directory 가 구축된 상태에서 가능하며 기존의 Windows NT 기반의 도메인보다 확장된 기능을 제공한다.<br>
</blockquote>
</details>

<details>
<summary>다음은 윈도우 감사 정책을 서술한 것이다. 빈칸에 맞는 세부 감사 정책을 기술하시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<strong>[보기]</strong><br>
( A ) 정책은 시스템 시작 또는 종료, 보안 로그에 영향을 미치는 이벤트 등을 감사하지 여부를 결정<br>
( B ) 정책은 도메인 컨트롤러에서 도메인 사용자 계정을 인증할 때마다 감사할지 여부를 결정<br>
( C ) 정책은 프로세스 생성, 프로세스 종료, 핸들 복제 및 간접 개체 엑세스 같은 프로세스 관련 이벤트를 감사할지 여부를 결정
</div>
</summary>
<blockquote>
( A ) 시스템 이벤트<br>
( B ) 계정 로그온 이벤트<br>
( C ) 프로세스 추적<br><br>

윈도우 운영체제들의 주요 감사 정책 9 가지는 다음과 같이 분류할 수 있습니다.

<br>

<table border="1" style="border-collapse: collapse; width: 100%;">
  <thead>
    <tr>
      <th style="padding: 8px; text-align: left; background-color: #f0f0f0; color: #333;">감사 정책 명칭</th>
      <th style="padding: 8px; text-align: left; background-color: #f0f0f0; color: #333;">주요 내용</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 8px;"><strong>시스템 이벤트</strong></td>
      <td style="padding: 8px;">시스템 시작/종료, 보안 로그에 영향을 미치는 이벤트 등 시스템 수준의 동작 감사</td>
    </tr>
    <tr>
      <td style="padding: 8px;"><strong>계정 로그온 이벤트</strong></td>
      <td style="padding: 8px;">계정 식별 및 인증 정보 확인(주로 도메인 컨트롤러에서 인증할 때 생성) 이벤트 감사</td>
    </tr>
    <tr>
      <td style="padding: 8px;"><strong>로그온 이벤트</strong></td>
      <td style="padding: 8px;">로컬 시스템에 계정 로그온/로그오프 하거나 네트워크를 통해 리소스 연결 시도 이벤트 감사</td>
    </tr>
    <tr>
      <td style="padding: 8px;"><strong>프로세스 추적</strong></td>
      <td style="padding: 8px;">프로세스 생성/종료, 간접 개체 액세스 등 애플리케이션 문제 분석에 필요한 상세 이벤트 감사</td>
    </tr>
    <tr>
      <td style="padding: 8px;"><strong>개체 액세스</strong></td>
      <td style="padding: 8px;">파일, 디렉터리, 레지스트리 키 등 SACL이 설정된 개체에 대한 접근 시도 이벤트 감사</td>
    </tr>
    <tr>
      <td style="padding: 8px;"><strong>계정 관리</strong></td>
      <td style="padding: 8px;">사용자 계정, 컴퓨터 계정, 그룹 등의 생성/수정/삭제 및 패스워드 재설정 이벤트 감사</td>
    </tr>
    <tr>
      <td style="padding: 8px;"><strong>정책 변경</strong></td>
      <td style="padding: 8px;">사용자 권한 할당 정책, 스레드 수준의 접근 토큰 수정, 신뢰 관계 변경 등의 보안 정책 수정 감사</td>
    </tr>
    <tr>
      <td style="padding: 8px;"><strong>특권(권한) 사용</strong></td>
      <td style="padding: 8px;">사용자가 시스템 권한(시스템 시간 변경, 백업/복원 등)을 실제로 행사할 때 발생하는 이벤트 감사</td>
    </tr>
    <tr>
      <td style="padding: 8px;"><strong>디렉터리 서비스 액세스</strong></td>
      <td style="padding: 8px;">Active Directory 환경에서 객체에 접근할 때의 도메인 컨트롤러 수준 서비스 접근 로깅 감사</td>
    </tr>
  </tbody>
</table>
</blockquote>
</details>

<details>
<summary>윈도우 시스템의 이벤트 로그는 윈도우 운용 과정 중에서 특정 동작(이벤트)을 체계적으로 기록한 바이너리 로깅 시스템이다. 다음 빈칸 ( A ), ( B ), ( C )에 해당하는 용어를 쓰시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<strong>[보기]</strong><br>
( A ) 로그: Login success/fail, Network login<br>
( B ) 로그: System start/halt, RDP Connection<br>
( C ) 로그: Add/Del member in group, Application error
</div>
</summary>
<blockquote>
( A ) 보안(Security)<br>
( B ) 시스템(System)<br>
( C ) 응용 프로그램(Application)<br><br>

윈도우 이벤트 로그는 버전에 따라 차이가 있지만 가장 기본이 되는 세가지 로그로 응용 프로그램 로그, 보안 로그, 시스템 로그가 있다.<br>

<br>
<table border="1" style="border-collapse: collapse; width: 100%;">
  <thead>
    <tr>
      <th style="padding: 8px; text-align: center; background-color: #f0f0f0; color: #333; width: 30%;">로그 유형</th>
      <th style="padding: 8px; text-align: center; background-color: #f0f0f0; color: #333;">이벤트 유형</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3" style="padding: 8px; text-align: center;"><strong>보안(Security) 로그</strong></td>
      <td style="padding: 8px;">Attempt login, Login success/fail, Network Login</td>
    </tr>
    <tr>
      <td style="padding: 8px;">Create process, Service install</td>
    </tr>
    <tr>
      <td style="padding: 8px;">Start Windows, Off the Windows</td>
    </tr>
    <tr>
      <td rowspan="2" style="padding: 8px; text-align: center;"><strong>시스템(System) 로그</strong></td>
      <td style="padding: 8px;">System start/halt</td>
    </tr>
    <tr>
      <td style="padding: 8px;">RDP Connection</td>
    </tr>
    <tr>
      <td rowspan="3" style="padding: 8px; text-align: center;"><strong>응용 프로그램(Application) 로그</strong></td>
      <td style="padding: 8px;">Add/Del member in group</td>
    </tr>
    <tr>
      <td style="padding: 8px;">Application error</td>
    </tr>
    <tr>
      <td style="padding: 8px;">Start service</td>
    </tr>
  </tbody>
</table>
</blockquote>
</details>

<details>
<summary>윈도우 시스템은 버전에 따라 차이가 있지만 기본적으로 Application, System, Security 이벤트 로그를 가지고 있다. 현재 시스템이 윈도우 7이라 가정할 때 아래 이벤트 로그에 대한 로그 파일명을 쓰시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<strong>[보기]</strong><br>
애플리케이션 로그: %SystemRoot%\System32\winevt\Logs\<string>(A)</string><br>
시스템 로그: %SystemRoot%\System32\winevt\Logs\<string>(B)</string><br>
보안 로그: %SystemRoot%\System32\winevt\Logs\<string>(C)</string><br>
</div>
</summary>
<blockquote>
(A) application.evtx<br>
(B) system.evtx<br>
(C) security.evtx<br><br>

1. 윈도우 XP 이하 버전에서는 이벤트 로그파일이 evt 확장자를 가진다.<br>
- 애플리케이션 로그: %SystemRoot%\System32\winevt\Configs\AppEvent.Evt<br>
- 시스템 로그: %SystemRoot%\System32\winevt\Configs\SysEvent.Evt<br>
- 보안 로그: %SystemRoot%\System32\winevt\Configs\SecEvent.Evt<br><br>

1. 윈도우 Vista 이상 버전에서는 이벤트 로그파일이 evtx 확장자를 가진다.<br>
- 애플리케이션 로그: %SystemRoot%\System32\winevt\Logs\application.evtx<br>
- 시스템 로그: %SystemRoot%\System32\winevt\Logs\system.evtx<br>
- 보안 로그: %SystemRoot%\System32\winevt\Logs\security.evtx<br>
</blockquote>
</details>

<details>
<summary>윈도우(Windows) OS 는 기본적으로 시스템을 관리할 수 있는 다양한 유틸리티(도구)들을 제공하고 있다. OS 유틸리티(도구) 중 로그를 조회하고 관리할 수 있는 도구는 무엇인지 쓰시오.</summary>
<blockquote>
Event Viewer<br><br>
이벤트 뷰어는 윈도우 OS에서 로그를 조회하고 관리하는 도구이다. 응용프로그램(application) 로그, 보안(Security) 로그, 시스템(System) 로그의 3가지 로그를 기본 로그로 한다.
</blockquote>
</details>
<details>
<summary>다음 빈칸( ) 에 적절한 용어를 쓰시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<strong>[보기]</strong><br>
( )은/는 윈도우 운영체제 서버 관리자가 로그 관리를 위해 가장 먼저 고려해야 할 정책으로 윈도우 서버에 이것을 설정하면 지정한 이벤트 범주에 대해서만 로그가 남는다.
</div>
</summary>
<blockquote>
감사 정책<br><br>

윈도우 로그 관리와 관련하여 서버 관리자가 가장 먼저 고려해야 할 대상으로 '감사 정책'이 있다. 윈도우 운영체제에서 감사 정책이란 '어떤 로그를 남길지 정의한 규칙'을 말하며 해당 정책에 의해 지정한 이벤트 범주에 대해서만 로그가 남는다.<br>
감사 정책이 구성되어 있지 않거나 설정 수준이 너무 낮으면 보안 관련 문제 발생 시 원인 파악이 어렵고, 설정 수준이 너무 높으면 불필요한 항목이 많아져 중요한 항목과 혼동될 수 있기 때문에 조직의 정책에 따른 적절한 감사 정책 설정이 중요하다.<br>

- 감사 정책 설정 방법: 윈도우 실행 > secpol.msc(로컬 보안 정책)<br>
- 로그 확인: 윈도우 실행 > eventvwr.msc(이벤트 뷰어)
</blockquote>
</details>

<details>
<summary>당신은 서버 관리자로서 윈도우 서버 시스템의 인증 및 접근 권한 내역을 정밀하게 모니터링하기 위해 '이벤트 뷰어' 도구와 '보안 정책'을 병행하여 점검하고 있습니다. SRM(Security Reference Monitor)에 의해 생성된 감사 로그(예: 권한 없는 폴더 접근 시도 실패)를 이벤트 뷰어에서 확인하기 위해 가장 먼저 조회해야 할 3대 기본 로그 분류 중 하나인 부분(A)의 명칭과, 이러한 파일/디렉터리 객체에 대한 접근 여부가 실제로 로그에 남도록 로컬 보안 정책에서 미리 활성화해 두어야 하는 필수 감사 정책(B)의 명칭을 명시하시오.</summary>
<blockquote>
(A) 보안(Security) 이벤트 로그<br>
(B) 개체 액세스 (Object Access) 감사 정책<br><br>
※ 해설: SRM은 SID를 기반으로 객체 접근 시 이를 검증해 메시지를 만들지만, 이 메시지가 LSA를 거쳐 실제 로그로 남기 위해서는 관리자가 '개체 액세스 감사' 정책을 사전에 성공/실패 여부를 남기도록 세팅해두어야 합니다.
</blockquote>
</details>

#### 2. UNIX/Linux 기본 학습
##### 시스템 기본
###### 사용자 정보
###### 그룹 정보
###### 입출력 재지정(I/O Redirection) 기능
###### 파이프 또는 파이프라인 기능
###### 특수 문자(메타 문자, Meta character)

<details>
<summary>하드웨어 가상화 기술 중 하나로, 호스트 운영체제 위에 가상화 소프트웨어를 설치하고 그 위에서 각각의 독립된 게스트(Guest) 운영체제를 구동하는 논리적 가상머신 환경 제공자의 명칭을 쓰시오.</summary>
<blockquote>
하이퍼바이저 (Hypervisor)
</blockquote>
</details>

<details>
<summary>디스크 스케줄링 중 '엘리베이터 알고리즘'의 명칭은?</summary>
<blockquote>
SCAN 알고리즘<br>
- 원리: 한쪽 끝에서 반대쪽 끝으로 이동하며 경로상의 모든 요청을 처리함.
</blockquote>
</details>

<details>
<summary>디스크 스케줄링 알고리즘 중 '엘리베이터 알고리즘'이라고 불리는 기법의 명칭을 쓰고, 이 기법이 디스크 암(Arm)의 움직임을 최적화하는 방식을 설명하시오.</summary>
<blockquote>
<strong>명칭</strong>: SCAN 알고리즘<br>
<strong>최적화 방식</strong>: 헤드가 디스크의 한쪽 끝에서 반대쪽 끝으로 이동하면서 그 경로에 있는 모든 입출력 요청을 처리한 후, 반대 방향으로 이동하며 다시 경로상의 요청을 처리하여 디스크 탐색 시간(Seek Time)의 편차를 줄여준다.
</blockquote>
</details>

##### 파일 시스템 응용
###### 파일 시스템 개요
###### 파일 시스템 링크 파일
###### 디렉터리 관리
###### 파일 권한 관리
###### 파일 검색
###### 파일 및 디렉터리 관련 명령어 요약
##### 프로세스 응용
###### 프로세스 개요
###### 프로세스 정보 확인
###### 프로세스 간 통신(시그널)
#### 3. UNIX/Linux 시스템 관리
##### 시스템 시작과 종료
###### 시스템 런 레벨
###### 시스템 시작
<details>
<summary>리눅스의 부팅 과정 중 발생할 수 있는 보안 위협을 방지하기 위해 사용되는 '싱글 모드(Single Mode) 진입 시 패스워드 설정'의 필요성과 설정 방법을 설명하시오.</summary>
<blockquote>
싱글 모드는 루트(root) 권한으로 비밀번호 없이 시스템에 접근하여 설정을 변경할 수 있는 모드이므로, 물리적 접근이 가능한 공격자가 관리자 권한을 탈취하는 것을 방지하기 위해 비밀번호 설정이 필수적이다. `/etc/sysconfig/init` 파일 내의 `SINGLE` 설정을 수정하거나, GRUB 부트로더에 `password`를 설정하여 인증 절차를 강화할 수 있다.
</blockquote>
</details>

###### 시스템 종료
##### 사용자 및 그룹 관리
###### 사용자 관리(추가, 변경 및 삭제)

<details>
<summary>리눅스 환경에서 새로 생성되는 사용자 계정의 홈 디렉터리에 자동으로 복사할 기본 설정 파일들(.bashrc 등)을 저장해 두는 디렉터리 경로를 쓰시오.</summary>
<blockquote>
/etc/skel
</blockquote>
</details>

###### 그룹 관리(추가, 변경 및 삭제)
##### 파일 시스템 관리
###### 파일시스템(디스크) 여유 공간 키그 관리(df 명령어)
###### 디렉터리(파일)별 파일시스템(디스크) 사용량 관리(du 명령어)
##### 작업 스케줄 관리
###### cron 서비스(정기적 작업 스케줄 관리 서비스)
#### 4. UNIX/Linux 서버 보안
##### 시스템 보안
###### 사용자의 패스워드 관리
<details>
<summary>리눅스 환경에서 사용자 계정의 패스워드 만료일, 암호 변경 최소/최대 일수 등 패스워드 에이징(Aging) 정보를 저장하고 있는 파일의 절대 경로를 쓰시오.</summary>
<blockquote>
/etc/shadow
</blockquote>
</details>

###### 프로세스 실행권한(SUID,SGID)
<details>
<summary>리눅스 시스템에서 사용자 및 그룹 권한을 제어하는 특수 권한인 SetUID의 개념을 설명하고, 보안 관점에서 SetUID 설정 파일이 위험한 이유를 서술하시오.</summary>
<blockquote>
<strong>개념</strong>: 파일 실행 시 해당 파일의 소유자(owner) 권한으로 실행되도록 하는 파일 확장 속성(권한) 설정이다.<br>
<strong>위험한 이유</strong>: 최고 관리자(root) 소유의 파일에 SetUID가 설정되어 있고 취약점이 존재할 경우, 일반 사용자가 해당 파일을 실행하는 동안 일시적으로 루트 권한을 획득하게 되어 침해 사고로 이어질 수 있기 때문이다.
</blockquote>
</details>

###### 기타
<details>
<summary>윈도우 파일 시스템 구조에서 삭제된 파일의 데이터를 덮어쓰지 않고 남아있는 잉여 공간을 '슬랙 공간(Slack Space)'이라 한다. 이러한 슬랙 공간이 디지털 포렌식 관점에서 중요한 의미를 갖는 이유를 설명하시오.</summary>
<blockquote>
사용자가 고의적으로 중요한 데이터나 악성코드를 은닉할 수 있는 공간이 됨과 동시에, 삭제된 원본 파일의 파편화된 데이터가 남아 있을 가능성이 높아 삭제된 데이터 복원 및 증거 확보 분석의 핵심 대상이 되기 때문이다.
</blockquote>
</details>

##### 네트워크 보안
###### 보안 쉘(SSH)
###### 슈퍼 서버(inetd 데몬)
###### 접근 통제(TCP Wrapper)
<details>
<summary>IP 관리 시스템에서 발전하여 MAC 기반 통제를 강화한 장비는?</summary>
<blockquote>
NAC (Network Access Control)<br>
- 주요 기능: 접근 제어 및 인증.
</blockquote>
</details>

###### xinetd 슈퍼 데몬
##### PAM(장착형 인증 모듈, Pluggable Authentication Modules)
###### 개요
###### PAM 을 사용한 인증 절차
###### PAM 설정파일(/etc/pam.d/remote 설정파일 일부)
###### PAM 활용 예 1 (시스템 취약점 분석, 평가 항목)
###### PAM 활용 예 2(시스템 취약점 분석, 평가 일부 항목)
###### PAM 활용 예 3(시스템 취약점 분석, 평가 일부 항목)
##### 시스템 로그 설정과 관리
###### 개요
###### 유닉스/리눅스 주요 로그 파일

<details>
<summary>리눅스 시스템 로그 중 다음 설명에 해당하는 로그 파일명을 작성하시오.<br>(가) 사용자의 원격 로그인 정보 저장<br>(나) 시스템 부팅 관련 메시지 저장<br>(다) 사용자가 로그인한 마지막 로그 저장</summary>
<blockquote>
(가) 사용자의 원격 로그인 정보 저장: `/var/log/secure`<br>(나) 시스템 부팅 관련 메시지 저장: `/var/log/dmesg`<br>(다) 사용자가 로그인한 마지막 로그 저장: `/var/log/lastlog`
</blockquote>
</details>

##### syslog 설정 및 관리
###### 개요
##### 리눅스 로그 관리
##### 기타 (추가됨)

<details>
<summary>파일 무결성 검사 기능 및 접근 제어를 제공하며, 루트킷(Rootkit) 감염 여부나 파일 시스템의 변경 사항을 주기적으로 모니터링하여 관리자에게 알림을 제공하는 대표적인 오픈소스 기반 침입 탐지 도구(HIDS)의 명칭과 그 탐지 원리를 서술하시오.</summary>
<blockquote>
<strong>명령 및 도구</strong>: 트립와이어 (Tripwire)<br>
<strong>탐지 원리</strong>: 사전에 시스템 내 중요 파일들의 해시(Hash) 값을 계산하여 데이터베이스에 저장해 둔 뒤, 주기적으로 현재 파일들의 해시 값을 재계산하여 원래의 데이터베이스 값과 비교함으로써 위·변조 여부를 탐지한다.
</blockquote>
</details>

#### 5. 시스템 해킹
##### 버퍼 오버플로우 공격(Buffer Overflow Attack)

<details>
<summary>버퍼오버플로우 공격을 완화할 수 있는 방법으로 스택과 힙 영역에 쉘코드 등을 실행하지 못하도록 하는 메모리 보호기법의 명칭을 쓰시오.</summary>
<blockquote>
DEP/NX bit (데이터 실행 방지)
</blockquote>
</details>

<details>
<summary>메모리 공간에서 버퍼 오버플로우가 발생할 때 실행 흐름이 악성 쉘코드(Shellcode)로 넘어가는 것을 방지하기 위해, 실행 파일이 메모리에 적재될 때마다 스택(Stack), 힙(Heap), 라이브러리 등의 주소를 난수화(Randomize)하여 배치하는 메모리 보안 기법의 명칭을 영문 약어로 쓰시오.</summary>
<blockquote>
ASLR (Address Space Layout Randomization)
</blockquote>
</details>

##### 레이스 컨디션 공격(Race Condition Attack)
##### 포맷 스트링 공격(Format String Attack)

<details>
<summary>공격자가 악성 스크립트나 명령어를 삽입하기 위해 취약한 C언어 함수(printf, sprintf 등)를 악용하여 메모리를 변조하거나 정보를 유출하는 공격 기법을 '포맷 스트링(Format String) 공격'이라 한다. 메모리의 특정 위치에 값을 쓰기 위해 공격자가 주로 사용하는 포맷 스트링 인자(Format Specifier) 하나를 쓰시오.</summary>
<blockquote>
%n (또는 %hn)
</blockquote>
</details>
