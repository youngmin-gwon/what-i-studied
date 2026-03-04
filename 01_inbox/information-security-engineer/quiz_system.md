---
title: quiz_system
tags: []
aliases: []
date modified: 2026-03-04 18:53:07 +09:00
date created: 2026-02-25 10:46:47 +09:00
---

## 공부노트
### 1. 윈도우 기본 학습

#### 윈도우 인증과정

##### 윈도우 인증 구성 요소

<details>
<summary>시스템 인프라 보안 진단 시 윈도우의 SAM(Security Account Manager) 파일에 대한 접근 통제 설정 상태를 점검하는 것은 매우 중요하다. 다음 빈칸 (A), (B), (C)에 들어갈 알맞은 내용을 작성하시오.<br>
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<strong>[상황 및 조치 사항]</strong><br>
- 점검 목적: 공격자가 계정 정보에 접근하여 패스워드 공격(무차별 대입 등) 시도에 따른 심각한 정보 노출 위협이 발생하는 것을 방지하기 위함이다.<br>
- 설정 경로: SAM 파일은 윈도우 설치 디렉터리 하위에 존재하며, 해당 폴더의 기본 경로는 일반적으로 <code>( A )</code> 이다.<br>
- 양호 기준: 악의적 유출을 막기 위해 SAM 파일에 대해서는 <code>( B )</code> 와 <code>( C )</code> 구룹에게만 접근을 허용하고, 그 외 불필요한 일반 사용자 및 특정 그룹에 대해서는 모든 접근 권한(읽기/쓰기 등)을 제거해야 한다.
</div>
</summary>
<blockquote>
(A) <code>C:\Winnt\System32\config</code> 또는 <code>C:\Windows\System32\config</code> (디렉터리 루트인 <code>C:\Windows</code> 또는 <code>C:\Winnt</code> 로 적어도 무방함)<br>
(B) Administrators<br>
(C) System
</blockquote>
</details>

<details>
<summary>점검 스크립트를 통해 윈도우 서비스 콘솔 및 프로세스를 분석하던 중, 시스템의 가장 핵심적인 보안 서브시스템 런타임 환경 상태를 점검해야 한다는 권고가 나왔다. 앞서 언급된 LSA, SAM 모듈 등 인증 기능 전반을 백그라운드 프로세스 형태로 구동시켜 보안 인증 패키지를 관리하는 이 프로세스(실행 파일)의 명칭(A)은 무엇인지 영문 소문자로 쓰시오.</summary>
<blockquote>
<code>lsass.exe</code> (Local Security Authority Subsystem Service)<br><br>
※ 참고: 서버 운영 관점에서 lsass.exe 프로세스의 과도한 자원 소모, 그리고 악성코드가 이 프로세스를 위장하거나 메모리를 덤프하여 패스워드 정보를 추출(예: Mimikatz 도구 등)하는 공격기법 등이 실무상 가장 흔하게 발생하므로 집중 점검 대상이 됩니다.
</blockquote>
</details>

<details>
<summary>윈도우 시스템에서 사용자 계정 및 패스워드 정보를 암호화하여 저장하는 데이터베이스의 명칭과 해당 파일이 저장되는 레지스트리 경로를 작성하시오.</summary>
<blockquote>
SAM (Security Account Manager), <code>HKEY_LOCAL_MACHINE\SAM</code>
</blockquote>
</details>

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
(A) <code>LSA</code> (Local Security Authority)<br>
(B) <code>SAM</code> (Security Account Manager)<br>
(C) <code>SRM</code> (Security Reference Monitor)
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
<summary>(서술형) 윈도우에서 지원하는 볼륨 단위 암호화 기능인 BitLocker의 특징 2가지를 서술하시오.</summary>
<blockquote>
1. 윈도우 운영체제에서 제공하는 볼륨 단위 암호화 기능이다.<br>2. 컴퓨터 부팅에 필요한 시스템 파티션 부분까지 암호화하여 보호할 수 있다.
</blockquote>
</details>

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
<code>HKEY_LOCAL_MACHINE</code> (HKLM)
</blockquote>
</details>

<details>
<summary>다음의 빈칸 (A), (B), (C) 에 적절한 용어를 기술하시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<strong>[보기]</strong><br>
Windows Server 운영체제에서 사용자 계정관리방식은 워크그룹(Workgroup) 방식과 &lt;string&gt;(A)&lt;/string&gt; 방식이 있으며, 로컬 사용자 계정은 %SystemRoot%\System32\config\&lt;string&gt;(B)&lt;/string&gt; 에 저장되고 있고, &lt;string&gt;(A)&lt;/string&gt; 방식은 &lt;string&gt;(C)&lt;/string&gt; 데이터베이스에 저장된다.
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
애플리케이션 로그: %SystemRoot%\System32\winevt\Logs\&lt;string&gt;(A)&lt;/string&gt;<br>
시스템 로그: %SystemRoot%\System32\winevt\Logs\&lt;string&gt;(B)&lt;/string&gt;<br>
보안 로그: %SystemRoot%\System32\winevt\Logs\&lt;string&gt;(C)&lt;/string&gt;<br>
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
<summary>윈도우 OS는 기본적으로 여러 가지 이벤트 로그를 제공한다. 다음 중 관리자가 시스템으로의 로그온 성공 및 실패, 사용자 계정의 추가 및 삭제 관련 이벤트를 보고자 할 때 어떤 이벤트 로그를 참고해야 하는지 쓰시오.</summary>
<blockquote>
보안(Security) 로그
</blockquote>
</details>

<details>
<summary>마이크로소프트사의 윈도우(Windows) 시스템에서 하나 이상의 볼륨(드라이브)을 암호화하는 기능으로 TPM(신뢰할 수 있는 플랫폼 모듈)을 사용하여 초기 시작 구성 요소의 무결성을 검사하는 암호화 방식을 무엇이라 하는가?</summary>
<blockquote>
비트로커(BitLocker)<br><br>
비트로커(BitLocker): 노트북 분실, 디스크 분리 후 중요 데이터 탈취 등의 이유로 기밀 자료가 유출될 상황을 대비한 윈도우에서 자체적으로 제공하는 디스크 암호화 기술이다.<br>
- TPM (Trusted Platform Module): 하드웨어와 소프트웨어, 펌웨어 인증을 검사하는 전용 칩을 말한다. TPM은 승인 없는 변경을 감지했을 경우 PC는 제한된 모드로 부팅되어 잠재적인 공격자의 악의적인 행위를 차단한다.
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
<summary>(서술형) 윈도우 파일 시스템 구조에서 삭제된 파일의 데이터를 덮어쓰지 않고 남아있는 잉여 공간을 '슬랙 공간(Slack Space)'이라 한다. 이러한 슬랙 공간이 디지털 포렌식 관점에서 중요한 의미를 갖는 이유를 설명하시오.</summary>
<blockquote>
사용자가 고의적으로 중요한 데이터나 악성코드를 은닉할 수 있는 공간이 됨과 동시에, 삭제된 원본 파일의 파편화된 데이터가 남아 있을 가능성이 높아 삭제된 데이터 복원 및 증거 확보 분석의 핵심 대상이 되기 때문이다.
</blockquote>
</details>

#### 윈도우 보안 식별자

<details>
<summary>윈도우 운영체제에서 사용자가 로그인을 수행하면 생성되는 객체로, 해당 사용자와 속한 모든 작업 그룹들에 관한 '보안 식별자(SID)' 정보를 담고 있는 것의 명칭을 쓰시오.</summary>
<blockquote>
접근 토큰 (액세스 토큰, Access Token)
</blockquote>
</details>

<details>
<summary>윈도우 시스템에서 사용자 계정의 고유 식별 번호인 SID 정보가 물리적으로 저장되는 레지스트리 기반 데이터베이스 파일의 명칭과 기본 디렉터리 경로를 쓰시오.</summary>
<blockquote>
<strong>파일 명칭</strong>: SAM (Security Account Manager)<br>
<strong>기본 경로</strong>: %SystemRoot%\System32\config (또는 C:\Windows\System32\config)
</blockquote>
</details>

<details>
<summary>윈도우의 SID 구조인 <code>S-1-5-21-[고유식별자]-[사용자 식별자]</code>에서, 맨 앞의 <code>S-1</code>과 <code>5-21</code>이 각각 공통적으로 무엇을 의미하는지 쓰시오.</summary>
<blockquote>
<strong>S-1</strong>: 윈도우 시스템임을 의미<br>
<strong>5-21</strong>: 해당 시스템이 도메인 컨트롤러(Domain Controller)이거나 단독 시스템(Stand-alone) 환경임을 의미
</blockquote>
</details>

<details>
<summary>SID 구조의 맨 마지막에 위치하는 부분은 사용자 계정별로 부여되는 고유의 사용자 식별자(ID) 값이다. 이 중 내장된 최고 관리자(Administrator), 게스트(Guest), 그리고 일반 사용자 계정에 기본 할당되는 식별 기준 값을 차례대로 쓰시오.</summary>
<blockquote>
<strong>관리자(Administrator)</strong>: 500<br>
<strong>게스트(Guest)</strong>: 501<br>
<strong>일반 사용자</strong>: 1000 이상 (1000부터 순차 부여)
</blockquote>
</details>

<details>
<summary>다음은 윈도우의 SID(보안 식별자) 구조와 확인 명령어에 대한 설명이다. 빈칸에 알맞은 내용을 작성하시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<strong>[명령어 실습 예시]</strong><br>
<code>C:\> ( A )</code><br>
<code>wmic:root\cli> ( B ) list brief</code><br>
<code>AccountType Caption …</code><br>
<code>512 WIN2008-01\Guest … S-1-5-21-…-501</code><br>
</div>
관리자는 위와 같이 윈도우 관리 명령 콘솔인 <code>( A )</code> 환경에서 <code>( B )</code> 명령어를 입력하여 시스템에 등록된 계정별 SID를 한눈에 확인할 수 있다.
</summary>
<blockquote>
(A) WMIC (Windows Management Instrumentation Console)<br>
(B) useraccount
</blockquote>
</details>

<details>
<summary>(서술형) 윈도우 시스템에서 '보안 식별자(SID)'의 정의를 기술하고, 사용자가 로그인한 이후 실행하는 모든 프로세스에 권한이 어떻게 부여되는지 SID와 접근 토큰을 연관 지어 서술하시오.</summary>
<blockquote>
<strong>정의</strong>: 윈도우의 각 사용자나 그룹에 부여되는 고유한 식별 번호이다.<br><br>
<strong>권한 부여 과정</strong>: 사용자가 로그인을 수행하면 사용자 및 소속 그룹의 SID 정보가 담긴 '접근 토큰(액세스 토큰)'이 생성되며, 이후 해당 사용자가 시작하는 모든 프로세스에 이 접근 토큰의 사본이 할당되어 권한이 상속된다.
</blockquote>
</details>

<details>
<summary>(서술형) 동일한 하드웨어 시스템에 윈도우 운영체제를 재설치하고 이전과 완전히 동일한 이름(예: 'user01')으로 계정을 생성하더라도, 이전에 해당 계정으로 암호화하거나 권한을 설정해둔 파일에 즉시 접근할 수 없는 이유를 고유 식별자의 관점에서 서술하시오.</summary>
<blockquote>
운영체제를 설치할 때마다 해당 시스템만의 고유한 식별자(예: 4243233100-3174512425-4165118588)가 새롭게 난수로 생성되어 SID에 반영되므로, 계정 이름이 동일하더라도 전체 SID가 달라지기 때문에 시스템에서는 서로 다른 사용자로 인식하여 접근이 거부된다.
</blockquote>
</details>

#### 윈도우 인증 구조

##### 개요

<details>
<summary>윈도우 운영체제에서 비밀번호를 단순 텍스트로 전달하지 않고, 인증을 안전하게 처리하기 위해 사용하는 기본적인 인증 방식의 명칭은?</summary>
<blockquote>
Challenge & Response 방식
</blockquote>
</details>

<details>
<summary>다음은 윈도우 인증 구조인 Challenge & Response 방식의 동작 과정이다. 빈칸 (A), (B), (C)에 알맞은 내용을 작성하시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<strong>[동작 과정]</strong><br>
1. 인증 요청: 사용자가 윈도우 시스템에 인증을 요청한다.<br>
2. ( A ) 생성 및 전송: 인증 요청을 받은 서버는 특수한 규칙 또는 랜덤한 값인 ( A )를 생성하여 사용자에게 전달한다.<br>
3. ( B ) 생성 및 전송: 사용자는 전달받은 ( A ) 값과 자신의 ( C ) 정보를 이용하여 최종적으로 ( B ) 값을 생성해 서버에 응답한다.<br>
4. 응답 확인: 서버는 수신한 ( B ) 값을 검증하여 인증 성공 여부를 기록하고 전달한다.
</div>
</summary>
<blockquote>
(A) Challenge<br>
(B) Response<br>
(C) 암호 (패스워드)
</blockquote>
</details>

<details>
<summary>(서술형) 윈도우 시스템이 단순히 사용자 아이디와 패스워드를 텍스트로 전달하여 인증하는 방식을 채택하지 않고, 굳이 'Challenge & Response' 방식을 사용하는 핵심적인 보안상 이유를 서술하시오.</summary>
<blockquote>
단순히 아이디와 패스워드를 전달하여 인증하는 평문 인중 방식은 네트워크 스니핑을 통한 '정보 노출' 및 탈취한 패스워드를 이용한 '패스워드 재사용(Replay) 공격'에 매우 취약하기 때문이다. 운영체제와 같이 높은 수준의 인증이 필요할 경우, 매번 서버가 생성해주는 임의의 값(Challenge)을 각자의 패스워드와 연산한 뒤 그 결과(Response)만을 보내게 함으로써 원본 패스워드가 노출되는 것을 방지하기 위함이다.
</blockquote>
</details>

##### 인증 암호 알고리즘

<details>
<summary>윈도우 2000, XP 환경의 기본 해시 알고리즘이었으나, 구조적으로 취약하여 크래킹에 노출되기 쉬워 윈도우 비스타 이후 버전부터는 기본적으로 사용할 수 없게 비활성화된 알고리즘의 명칭을 쓰시오.</summary>
<blockquote>
LM (Lan Manager) 해시
</blockquote>
</details>

<details>
<summary>다음 윈도우 패스워드 해시 알고리즘들에 대한 설명 (가), (나), (다)를 읽고 올바른 알고리즘을 쓰시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
(가) 초기 윈도우 시스템의 기본 알고리즘으로 설계되었으나, 패스워드를 짧게 분할하고 대소문자를 구분하지 않아 구조상으로 매우 취약하다.<br>
(나) (가) 알고리즘의 취약점을 일부 개선하여 MD4 해시가 추가된 형태이다.<br>
(다) 윈도우 비스타 이후 시스템의 기본 인증 프로토콜이다. 기존 설정과는 설계 관점이 동떨어진 완전히 다른 복잡한 알고리즘을 통해 해시값을 생성하므로 크래킹 방어력이 강력하다.
</div>
</summary>
<blockquote>
(가) <code>LM</code><br>
(나) <code>NTLM</code><br>
(다) <code>NTLMv2</code>
</blockquote>
</details>

<details>
<summary>(서술형) 윈도우 인증 암호 시스템이 진화하면서 LM(Lan Manager) 알고리즘이 점차 퇴출되고, NTLMv2가 최신 운영체제(윈도우 비스타 이후)의 기본 인증 프로토콜로 굳게 자리 잡게 된 이유를 크래킹 방어 관점에서 자세히 서술하시오.</summary>
<blockquote>
초기 버전인 LM 해시는 패스워드 알고리즘 구조상 복잡성이 매우 떨어져 무차별 대입이나 사전 공격과 같은 크래킹(Brute Force) 공격 시도에 심각하게 취약했기 때문이다. 따라서 기존 해시들을 보완하고 전혀 다른 방식의 높은 복잡성을 지닌 알고리즘을 사용하여 보안 및 안전성을 확실히 확보한 NTLMv2가 도입되어 현재까지 기본 인증 프로토콜로 사용되고 있다.
</blockquote>
</details>

<details>
<summary>윈도우 인증 프로토콜 중 챌린지-응답 방식을 사용하는 구형 프로토콜과 티켓 기반의 현대적 프로토콜의 명칭을 각각 쓰시오.</summary>
<blockquote>
<code>NTLM</code> (NT LAN Manager), <code>Kerberos</code> (커버로스)
</blockquote>
</details>

##### LAN Manager 인증 수준

<details>
<summary>Lan Manager는 네트워크를 통한 여러 공유 작업 시 인증을 담당하는 핵심적인 서비스이다. 보안 분석 및 평가 시 이 시스템의 보호 범위를 정확히 파악하는 것이 중요한데, Lan Manager가 인증을 직접적으로 담당하는 윈도우 네트워크의 대표적인 자원 공유 항목 2가지를 쓰시오.</summary>
<blockquote>
파일 공유, 프린터 공유
</blockquote>
</details>

<details>
<summary>다음은 윈도우 시스템 취약점 진단 점검 항목인 'Lan Manager 인증 수준'과 연관된 내용이다. 빈칸에 들어갈 가장 알맞고 강력한 프로토콜의 명칭(영문)을 쓰시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<strong>[설정 및 조치]</strong><br>
이 보안 설정은 클라이언트/서버 간에 네트워크 로그온에 사용할 C/R 인증 프로토콜과 협상 세션 보안 수준을 결정한다. 만약 이 인증 수준이 취약하게 설정되어 있으면 패스워드 크래킹 및 네트워크 스니핑 공격에 노출될 수 있으므로, 보안 요구 수준을 높여 반드시 <strong>( A )</strong> 만 응답하도록 양호하게 설정해야 한다.
</div>
</summary>
<blockquote>
(A) <code>NTLMv2</code>
</blockquote>
</details>

<details>
<summary>(서술형) 윈도우 시스템 취약점 분석 및 평가 과정에서, 로컬 보안 정책의 『네트워크 보안: LAN Manager 인증 수준』 항목을 점검하여 'LM 및 NTLM'을 완전히 수신 거부하고 가장 방어 수준이 높은 'NTLMv2 응답만 보냄' 모드로 강제 설정할 것을 권고하는 이유를 '세션 보안 결합' 측면에서 구체적으로 서술하시오.</summary>
<blockquote>
해당 LAN Manager 인증 수준 설정은 클라이언트가 당장 사용하는 인증 프로토콜을 규정할 뿐만 아니라, 서버가 허가할 수 있는 '협상된 세션 보안 수준' 및 '서버 인증 수준' 전체에 직접적이고 중대한 영향을 미치기 때문이다. 기존 프로토콜(LM, NTLM)은 익히 알려진 취약점들이 많아 릴레이 공격 등에 악용될 수 있으므로, 가장 진보하고 안전한 NTLMv2 프로토콜 통신만을 협상에서 강제함으로써 네트워크 로그온 및 전체 공유 자원의 세션 보안성을 끌어올리기 위함이다.
</blockquote>
</details>

#### 패스워드 크래킹

##### 사전 공격/사전 대입 공격 (Dictionary Attack)

<details>
<summary>키보드 자판의 일련순(qwer1234 등), 생년월일, 주민등록번호, 영단어 등 사용자들이 패스워드로 자주 선택할 만한 단어 목록을 미리 파일로 구축한 뒤, 이를 대상 시스템에 하나씩 대입하여 패스워드 일치 여부를 알아내는 크래킹 기법의 명칭은?</summary>
<blockquote>
사전 공격 (Dictionary Attack)
</blockquote>
</details>

<details>
<summary>(서술형) 패스워드 크래킹 기법 중 하나인 '사전 공격(Dictionary Attack)'의 원리를 패스워드 설정 관습 측면에서 구체적으로 서술하시오.</summary>
<blockquote>
일반 사용자들이 복잡한 비밀번호 대신 기억하기 쉬운 주민등록번호, 이름, 또는 키보드 자판 일련순 문자열(예: asdf, qwer1234 등)을 흔히 사용한다는 점을 악용하여, 패스워드로 자주 쓰일 법한 단어와 문자열들을 미리 ‘사전(Dictionary) 파일’로 대량 구축해 놓고 이를 하나씩 순서대로 대입해가며 일치 여부를 파악하는 방식이다.
</blockquote>
</details>

##### 무차별 공격/무작위 대입 공격 (Brute Force Attack)

<details>
<summary>일반적으로 '사전 대입 공격'에 실패한 이후 후속으로 사용되며, 발생할 수 있는 모든 경우의 수와 조합의 문자열을 계속해서 하나씩 맹목적으로 대입해보는 크래킹 기법의 명칭은?</summary>
<blockquote>
무차별 대입 공격 (Brute Force Attack)
</blockquote>
</details>

<details>
<summary>(서술형) 무차별 공격(Brute Force Attack)이 사전 공격 방식과 차별화되는 원리와 수행 방식을 설명하시오.</summary>
<blockquote>
사전 파일의 정해진 목록 내에서 대입하는 사전 공격과 달리, 무차별 공격은 패스워드에 사용될 수 있는 문자열의 "모든 범위"를 우선 지정한 뒤, 오직 그 범위 안에서 생성 가능한 모든 극단적 조합의 패스워드를 연산 생성해 하나씩 대입해가며 무작위로 일치 여부를 확인하는 방식이다.
</blockquote>
</details>

##### 혼합 공격 (Hybrid Attack)

<details>
<summary>일반 사용자들이 'goodday' 같은 사전에 나오는 문자열 뒤에 '1234', '1004' 등 간단한 숫자를 덧붙이는 형태의 패스워드를 많이 사용한다는 점을 타겟으로 하여, 특정 사전 파일 문자에 특정 문자나 숫자를 추가로 무작위 대입해보며 확인하는 크래킹 기법의 명칭은?</summary>
<blockquote>
혼합 공격 (Hybrid Attack)
</blockquote>
</details>

<details>
<summary>(서술형) 일반적인 사전 대입 공격과 무작위 대입 공격의 장점을 결합한 '혼합 공격(Hybrid Attack)'의 동작 원리를 서술하시오.</summary>
<blockquote>
기존의 완전한 무작위 대입 공격은 시간이 너무 오래 걸린다는 단점이 있고 순수 사전 공격은 변형된 단어를 잡지 못한다는 한계가 있다. 이에 혼합 공격은 기본적으론 '사전(Dictionary) 파일'에 있는 단어 및 문자열을 기반으로 하되, 그 앞뒤에 일부 문자나 숫자 조합을 추가로 무작위 연산(무차별 대입)해 결합시키며 대입해 공격 성공률을 비약적으로 높인 방식이다.
</blockquote>
</details>

<details>
<summary>다음은 패스워드 크래킹 공격에 관한 지문이다. 빈칸 ( )에 적절한 용어를 쓰시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<strong>[보기]</strong><br>
(A)은/는 패스워드로 자주 사용되는 단어를 사전 파일로 만들어 놓고 자동화된 툴로 사전 파일의 단어를 대입하여 일치 여부를 확인하는 기법이다.<br>
(B)은/는 패스워드로 사용될 수 있는 영문자(대소문자), 숫자, 특수문자 등을 무작위로 패스워드 자리에 대입하여 패스워드를 알아내는 기법이다.<br>
(C)은/는 위 두 가지 공격을 혼합한 방식으로 기존 사전 파일 문자열에 문자, 숫자 등을 추가 대입하여 패스워드를 알아내는 기법이다.
</div>
</summary>
<blockquote>
(A) 사전 공격/사전 대입 공격 (Dictionary Attack)<br>
(B) 무차별 공격/무작위 대입 공격 (Brute Force Attack)<br>
(C) 혼합 공격 (Hybrid Attack)
</blockquote>
</details>

##### 레인보우 테이블 (Rainbow Table) 공격

<details>
<summary>패스워드 크래킹 시간을 극단적으로 단축시키기 위해, 특정한 변이 함수를 사용하여 하나의 패스워드에서 출발해 여러 변이 패스워드를 만들고, 각 변이 패스워드의 해시를 고리처럼 연결해 수많은 패스워드/해시 체인(Chain)을 구축해 둔 거대한 데이터베이스 테이블의 명칭은?</summary>
<blockquote>
레인보우 테이블 (Rainbow Table)
</blockquote>
</details>

<details>
<summary>레인보우 테이블을 구성할 때, 하나의 비밀번호 해시값으로부터 무수히 변이된 형태의 새로운 평문 패스워드 체인을 생성하고 연결해 나가기 위해 중간 매개체로 반복적으로 쓰이는 핵심 함수의 명칭을 쓰시오.</summary>
<blockquote>
R (Reduction) 함수
</blockquote>
</details>

<details>
<summary>(서술형) 레인보우 테이블을 이용한 패스워드 크래킹 과정에서, 공격자가 시스템으로부터 '탈취한 해시(Hash)'값 하나만 가지고 어떻게 원래 평문 패스워드를 찾아낼 수 있는지 테이블 내 구조(해시 테이블과 기능)를 연관지어 서술하시오.</summary>
<blockquote>
레인보우 테이블은 방대한 패스워드와 그 해시값들이 생성 변종인 R(Reduction) 함수 체인으로 이어져 있는 데이터베이스이다. 공격자는 탈취한 목표 해시값을 이 테이블 내부의 R 함수 체인에 반복적으로 수행 대입해 본 뒤, 기존에 저장된 해시 테이블 체인 종단값과 매칭되는 지점과 위치를 찾아내어 체인을 역추적하는 방식으로 원본 패스워드를 신속하게 도출해 낸다.
</blockquote>
</details>

##### 고급 패스워드 공격

<details>
<summary>다음 보기에서 설명하는 공격 명칭을 쓰시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<strong>[보기]</strong><br>
윈도우 운영체제에서 Mimikatz(미미카츠)와 같은 도구를 사용하여 등록된 사용자 계정의 NTLM 또는 LM(Lan Manager) 인증용 해시값을 탈취한 후 원격 서버나 서비스에 인증을 시도하는 공격 기법으로 패스워드 자체를 알지 못해도 접속 인증에 성공할 수 있다.
</div>
</summary>
<blockquote>
Pass the Hash 공격<br><br>
Pass the Hash 공격은 패스워드에 대한 해시값을 인증 시에 사용하는 환경에서 사용자(희생자)의 해시값을 획득한 후(탈취한 후) 이를 이용하여 인증을 시도하는 형태의 공격으로 원격 서버나 원격 서비스에 접속할 때 사용자의 실제 패스워드를 모르는 상태에서도 탈취한 사용자의 패스워드 해시값을 이용하여 인증을 시도한다.<br>
- Mimikatz(미미카츠): 윈도우 시스템에서 사용자 계정, 패스워드 등의 자격 증명(Credential) 정보를 수집할 수 있는 도구
</blockquote>
</details>

<details>
<summary>다음 빈칸 ( )에 적절한 용어를 쓰시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<strong>[보기]</strong><br>
( ) 공격은 무작위(무차별) 대입 공격의 일종으로 공격자가 미리 확보해 놓은 사용자(희생자)의 로그인 자격 증명(EX, ID/Password 등)을 다른 사이트(서비스)의 인증 시스템 계정에 무작위로 대입하여 접속을 시도하는 공격 기법을 말한다.
</div>
</summary>
<blockquote>
크리덴셜 스터핑 (Credential Stuffing)<br><br>
크리덴셜 스터핑(Credential Stuffing) 공격은 사용자의 계정, 비밀번호, 기타 여러 가지 신원 확인에 필요한 개인정보(자격 증명, Credential)를 다양한 방식으로 탈취하여 사용자가 이용할 만한 시스템 및 사이트에 방문한 후 무작위로 대입(Stuffing)하는 공격 방식을 말한다.<br>
- 편의를 위해 한 가지 ID와 비밀번호를 여러 시스템/사이트에서 사용하는 사용자의 취약성을 이용한 공격<br>
- 크리덴셜(Credential)의 사전적 의미는 특정인이 해당 자격을 가졌는지를 증명하는 '자격증명'을 말한다. 일반적으로 로그인 시 신원(신분) 확인 목적으로 사용하는 사용자 ID/비밀번호, 생체 정보 등이 크리덴셜에 해당한다.
</blockquote>
</details>

#### 네트워크 취약점

##### Null Session 취약점

<details>
<summary>다음 보기에서 설명하고 있는 취약점은 무엇인가?
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<strong>[보기]</strong><br>
네트워크에 연결된 윈도우 시스템 간에 아이디/패스워드 없이 다른 시스템에 접속할 수 있는 취약점으로 시스템 계정, 비밀번호, 공유 정보가 노출될 수 있으므로 제거해야 한다.
</div>
</summary>
<blockquote>
널 세션 (Null Session) 취약점<br><br>
널 세션(Null Session)이란 윈도우가 설치된 네트워크의 다른 원격 컴퓨터에 사용자명과 패스워드를 널(NULL, 빈 값)로 해서 접속할 수 있게 해 주는 것을 말한다.
</blockquote>
</details>

#### 운영체제 보안 분리

<details>
<summary>다음의 빈칸 (A), (B), (C)에 적절한 용어를 쓰시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<strong>[보기]</strong><br>
운영체제가 관리하는 메모리, 파일, 입출력 장치, 프로세서와 같은 객체들은 여러 프로그램을 통해 공유될 때 운영체제에 의하여 충분한 보호가 이루어져야 하며, 시스템 자원에 대한 기본적인 보호는 한 사용자의 객체를 다른 사용자로부터 격리하는 분리로 이루어진다.<br>
운영체제 보안을 위한 분리에는 물리적 분리, 시간적 분리, 논리적 분리, 암호적 분리 등이 있다.<br>
이 중 (A)은/는 운영체제가 프로그램의 접근을 제한하여 허용된 영역 밖의 객체에 대해서는 접근할 수 없도록 하는 것이고, (B)은/는 다른 프로세스가 인식할 수 없는 방법으로 자신의 데이터와 계산을 감추는 것이며, (C)은/는 프로세스를 서로 다른 시간에 운영하는 것을 말한다.
</div>
</summary>
<blockquote>
(A) 논리적 분리<br>
(B) 암호적 분리<br>
(C) 시간적 분리<br><br>
1) 운영체제 보안의 기능<br>
- 메모리 보호, 파일 보호, 접근 통제, 사용자 인증<br><br>
2) 보호 대상 객체<br>
- 메모리, 공유 및 재사용이 가능한 I/O 장치, 공유 가능한 프로그램 및 서브 프로그램, 공유 데이터<br><br>
3) 운영체제 보안을 위한 분리<br>
- 물리적 분리(Physical separation): 사용자별로 별도의 장비만 사용하도록 제한하는 방법으로 강한 형태의 분리가 되지만 현실적/실용적이지 못하다.<br>
- 시간적 분리(Temporal separation): 프로세스가 동일 시간에 하나씩만 실행되도록 하는 방법으로 동시 실행으로 발생되는 보안 문제를 제거한다.<br>
- 논리적 분리(Logical separation): 프로세스별로 논리적인 영역을 갖도록 하는 방법으로 프로세스는 자신의 영역 안에서는 자유로운 작업을 수행하지만 할당된 영역 밖에서의 작업은 엄격하게 제한된다.<br>
- 암호적 분리(Cryptographic separation): 내부에서 사용되는 정보를 외부에서는 알 수 없도록 암호화하는 방법을 말한다.
</blockquote>
</details>

#### 윈도우 관리 명령어

##### net 명령어

<details>
<summary>다음 보기의 빈 칸 ( )에 적절한 용어를 쓰시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<strong>[보기]</strong><br>
윈도우 서버에서 net 명령을 이용하여 user1, user2 계정이 있는 것을 확인하였다. 그런데 윈도우 서버 재부팅 이후에 user2 계정으로 로그인할 수 없어 그 이유를 확인한 결과 user2 계정의 속성에 (A)이/가 설정되었기 때문이었다. 이를 해제하기 위한 net 명령은 다음과 같다.<br>
[윈도우 cmd 창] <code>C:\> net</code> (B)
</div>
</summary>
<blockquote>
(A) 계정 사용 안 함<br>
(B) <code>net user user2 /active:yes</code><br><br>
1) <code>net user</code> 명령어: 윈도우 시스템에서 로컬 계정을 추가/수정/삭제하거나 로컬 계정 정보를 표시하는 명령어<br>
<code>net user</code> 명령어를 통해 윈도우 시스템의 전체 로컬 계정 정보 확인<br>
계정 속성 확인 결과 user2 계정에만 "계정 사용 안 함" 속성이 설정되어 해당 계정으로 로그인이 불가함<br><br>
2) user2 "계정 사용 안 함" 속성 해제<br>
<code>net user</code>: 전체 로컬 계정 정보 확인<br>
<code>net user 계정명</code>: 해당 계정의 속성 확인<br>
<code>net user 계정명 /active:yes</code>: 해당 계정 사용함(활성 상태)<br>
<code>net user 계정명 /active:no</code>: 해당 계정 사용 안함(비활성 상태)
</blockquote>
</details>

<details>
<summary>정보보안기사 교육기관 관리자는 CCTV 모니터링 중 불 꺼진 사무실에 외부 침입자가 들어와 윈도우 웹 서버 콘솔에 명령을 입력하고 있는 것을 확인했다. 경찰에 신고 후 CCTV를 통해 입력하는 명령을 살펴본 결과 다음과 같았다. 각 명령어의 의미를 간단히 쓰시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<strong>[명령어 실행 내용]</strong><br>
<code>C:\>net user algisa2 @algisa102 /ADD</code><br>
명령을 잘 실행했습니다.<br><br>
<code>C:\>net user</code><br>
WIN2008-81에 대한 사용자 계정<br>
-----------<br>
algisa algisa2 Guest kiwi99<br>
명령을 잘 실행했습니다.<br><br>
<code>C:\>net localgroup administrators algisa2 /ADD</code><br>
명령을 잘 실행했습니다.
</div>
</summary>
<blockquote>
1) <code>net user algisa2 @algisa102 /add</code><br>
- <code>net user</code> 명령을 통해 계정명이 'algisa2'이고 비밀번호가 '@algisa102'인 계정을 생성한다.<br>
- (로컬 계정 생성 명령) <code>net user 계정명 비밀번호 /add</code><br>
- (로컬 계정 삭제 명령) <code>net user 계정명 /delete</code><br><br>
1) <code>net user</code><br>
- 전체 로컬 계정 정보를 확인한다. algisa2 계정이 새롭게 생성된 것을 확인할 수 있다.<br><br>
1) <code>net localgroup administrators algisa2 /add</code><br>
- <code>net localgroup</code> 명령을 통해 'algisa2' 계정을 administrators 그룹에 추가한다.<br>
- (로컬 그룹에 계정 추가 명령) <code>net localgroup 그룹명 계정명 /add</code><br>
- (로컬 그룹에 계정 삭제 명령) <code>net localgroup 그룹명 계정명 /delete</code><br><br>
외부 침입자의 명령 내용을 보면, 관리자 권한의 계정을 몰래 생성하기 위해 algisa2라는 계정을 생성하고 이를 administrators 그룹에 추가하고 있음을 알 수 있다.
</blockquote>
</details>

<details>
<summary>다음 보기는 윈도우 시스템에서 공유된 폴더(디렉터리)를 해제하는 명령어이다. 빈 칸 ( )에 명령어를 완성하시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<strong>[보기]</strong><br>
( ) c$ /delete
</div>
</summary>
<blockquote>
<code>net share</code><br><br>
명령어 형식: <code>net share 공유 폴더(디렉터리) 이름 /delete</code>
</blockquote>
</details>

#### 윈도우 보안 관리

##### 계정 보안 취약점 분석

<details>
<summary>다음은 한 Windows Server 시스템의 사용자 계정에 관한 정보를 보여주는 그림들이다. 그림이 보여주는 내용을 분석하여 사용자 계정 관리의 보안 취약점들을 지적하시오.
(그림에서 Administrator는 시스템 관리자 계정, Guest는 게스트(guest) 계정, algisa는 일반 사용자 계정이다. 또한 시스템의 C: 디스크는 부트(Boot) 디스크이다.)
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<strong>[문제]</strong><br>
(가) Administrator 계정의 보안 취약점<br>
(나) Guest 계정의 보안 취약점<br>
(다) algisa 계정의 보안 취약점
</div>
</summary>
<blockquote>
<strong>(가) Administrator 계정의 보안 취약점</strong><br>
- Administrator 계정명을 쉽게 유추할 수 없는 이름으로 변경한다.<br>
- 관리자 계정(Administrator)의 최대 암호 사용 기간이 설정되어 있지 않아 공격자의 무차별 공격으로부터 취약하다. '암호 사용 기간 제한 없음' 체크를 해제한다.<br>
- 원격 제어는 접속한 사용자의 세션을 모니터링하거나 제어할 수 있는 설정이다. Administrator 세션에 대하여 외부에서 원격 제어를 하지 못하도록 '원격 제어 가능'을 해제하거나, 원격 제어 구성 시 '사용자의 허가 필요' 항목을 체크하여 Administrator 세션에 대하여 악의적인 원격 제어를 차단한다.<br><br>
<strong>(나) Guest 계정의 보안 취약점</strong><br>
- Administrators 그룹에서 불필요한 Guest 계정을 제거한다.<br><br>
<strong>(다) algisa 계정의 보안 취약점</strong><br>
- Administrators 그룹에서 불필요한 일반 사용자 계정인 algisa 계정을 제거한다.<br>
- C:(파일 시스템)에 일반 사용자(algisa)가 모든 권한을 가지고 있으면 권한 및 소유자 변경 등의 작업이 가능하므로 관리자 외에는 모든 권한을 제거한다.
</blockquote>
</details>

### 2. UNIX/Linux 기본 학습
#### 시스템 기본 명령어

##### 디렉터리 및 파일 탐색 명령어

###### ls (List directory contents)

<details>
<summary>UNIX/Linux에서 현재 디렉터리의 파일과 폴더 목록을 표시하는 기본 명령어는?</summary>
<blockquote>
<code>ls</code>
</blockquote>
</details>

<details>
<summary>ls 명령어에서 숨겨진 파일(.으로 시작하는 파일)을 포함하여 자세한 정보를 긴 형식으로 표시하는 옵션 조합을 쓰시오.</summary>
<blockquote>
<code>ls -la</code><br><br>
- <code>ls -l</code> : 파일의 자세한 정보를 긴 형식으로 표시<br>
- <code>ls -a</code> : 숨겨진 파일(.으로 시작하는 파일)까지 표시<br>
- <code>ls -h</code> : 파일 크기를 사람이 읽기 쉬운 형식으로 표시 (KB, MB, GB)
</blockquote>
</details>

<details>
<summary>(고급) 다음 명령어의 실행 결과를 분석하고, 각 필드가 의미하는 바를 설명하시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<code>$ ls -la /tmp/test.txt</code><br>
<code>-rwsr-xr-x 1 root wheel 2048 Dec 25 10:30 /tmp/test.txt</code>
</div>
</summary>
<blockquote>
- 첫 번째 문자 <code>'-'</code>: 일반 파일을 의미<br>
- <code>'rwsr-xr-x'</code>: 파일 권한 (소유자:rwx, 그룹:r-x, 기타:r-x, 's'는 SetUID 설정)<br>
- <code>'1'</code>: 하드링크 수<br>
- <code>'root'</code>: 파일 소유자<br>
- <code>'wheel'</code>: 그룹 소유자<br>
- <code>'2048'</code>: 파일 크기 (바이트)<br>
- <code>'Dec 25 10:30'</code>: 마지막 수정 시간<br>
- <code>'/tmp/test.txt'</code>: 파일 경로<br><br>
특히 권한 부분에서 's'는 SetUID가 설정되어 있어, 이 파일을 실행할 때 소유자(root) 권한으로 실행됨을 의미한다.
</blockquote>
</details>

###### cd (Change Directory)

<details>
<summary>UNIX/Linux에서 현재 작업 디렉터리를 변경하는 명령어는?</summary>
<blockquote>
<code>cd</code>
</blockquote>
</details>

<details>
<summary>cd 명령어를 사용하여 이전 작업 디렉터리로 돌아가는 명령을 쓰시오.</summary>
<blockquote>
<code>cd -</code><br><br>
- <code>cd ~</code> : 홈 디렉터리로 이동<br>
- <code>cd ..</code> : 상위 디렉터리로 이동<br>
- <code>cd -</code> : 이전 디렉터리로 이동
</blockquote>
</details>

<details>
<summary>(고급) 다음 상황에서 각 명령어 실행 후의 현재 디렉터리 경로를 예측하시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
초기 상태: /home/user/documents/projects<br>
1) <code>$ cd ../../../</code><br>
2) <code>$ cd ./usr/bin</code><br>
3) <code>$ cd -</code><br>
4) <code>$ cd ~user/downloads</code>
</div>
</summary>
<blockquote>
5) /home (3단계 상위로 이동)<br>
6) /home/usr/bin (현재 위치에서 상대경로로 이동, 단 해당 경로가 존재한다고 가정)<br>
7) /home/user/documents/projects (이전 디렉터리로 복귀)<br>
8) /home/user/downloads (user의 홈 디렉터리 하위 downloads로 이동)
</blockquote>
</details>

###### pwd (Print Working Directory)

<details>
<summary>현재 작업 중인 디렉터리의 절대 경로를 출력하는 명령어는?</summary>
<blockquote>
<code>pwd</code>
</blockquote>
</details>

<details>
<summary>(중급) 심볼릭 링크 디렉터리에서 pwd 명령어의 동작을 설명하시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<code>$ ln -s /var/log /home/user/logs</code><br>
<code>$ cd /home/user/logs</code><br>
<code>$ pwd</code> vs <code>$ pwd -P</code>
</div>
</summary>
<blockquote>
- <code>pwd</code> : /home/user/logs (논리적 경로, 심볼릭 링크 경로 그대로 표시)<br>
- <code>pwd -P</code> : /var/log (물리적 경로, 실제 디렉터리 경로 표시)<br><br>
-P 옵션은 심볼릭 링크를 따라가서 실제 물리적 경로를 출력한다.
</blockquote>
</details>

##### 디렉터리 관리 명령어

###### mkdir (Make Directory)

<details>
<summary>새로운 디렉터리를 생성하는 명령어는?</summary>
<blockquote>
<code>mkdir</code>
</blockquote>
</details>

<details>
<summary>mkdir 명령어를 사용하여 "/home/user/project/2024/final" 경로의 디렉터리를 상위 디렉터리가 존재하지 않더라도 한 번에 생성하는 명령을 쓰시오.</summary>
<blockquote>
<code>mkdir -p /home/user/project/2024/final</code><br><br>
-p 옵션은 상위 디렉터리가 존재하지 않을 경우 함께 생성한다.
</blockquote>
</details>

<details>
<summary>(고급) 다음 명령어를 실행했을 때의 결과와 생성된 디렉터리의 권한을 설명하시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<code>$ umask 022</code><br>
<code>$ mkdir -m 755 /tmp/secure_dir</code><br>
<code>$ mkdir /tmp/normal_dir</code>
</div>
</summary>
<blockquote>
- <code>/tmp/secure_dir</code> : 755 권한 (rwxr-xr-x) - <code>-m</code> 옵션으로 명시적 지정<br>
- <code>/tmp/normal_dir</code> : 755 권한 (rwxr-xr-x) - <code>umask 022</code>가 <code>777</code>에서 <code>022</code>를 뺀 결과<br><br>
디렉터리의 기본 권한은 <code>777</code>이고, <code>umask 022</code>가 적용되어 <code>755</code>가 된다. <code>-m</code> 옵션은 <code>umask</code>를 무시하고 지정된 권한을 직접 설정한다.
</blockquote>
</details>

###### rmdir (Remove Directory)

<details>
<summary>빈 디렉터리를 삭제하는 명령어는?</summary>
<blockquote>
<code>rmdir</code>
</blockquote>
</details>

<details>
<summary><code>rmdir</code> 명령어와 <code>rm -rf</code> 명령어의 차이점을 설명하시오.</summary>
<blockquote>
- <code>rmdir</code>: 빈 디렉터리만 삭제 가능, 안전함<br>
- <code>rm -rf</code>: 디렉터리와 그 내용을 강제로 삭제, 위험할 수 있음<br><br>
<code>rmdir</code>은 디렉터리가 비어있지 않으면 삭제를 거부하여 실수로 중요한 파일을 삭제하는 것을 방지한다.
</blockquote>
</details>

##### 파일 내용 조회 명령어

###### cat (Concatenate and display files)

<details>
<summary>파일의 전체 내용을 화면에 출력하는 기본 명령어는?</summary>
<blockquote>
<code>cat</code>
</blockquote>
</details>

<details>
<summary>cat 명령어를 사용하여 파일 내용을 줄 번호와 함께 출력하는 옵션을 쓰시오.</summary>
<blockquote>
<code>cat -n</code><br><br>
- <code>cat -n</code> : 모든 줄에 번호를 표시하여 출력<br>
- <code>cat -b</code> : 비어있지 않은 줄에만 번호를 표시<br>
- <code>cat -s</code> : 연속된 빈 줄을 하나로 압축<br>
- <code>cat -v</code> : 비출력 문자를 시각적으로 표시
</blockquote>
</details>

<details>
<summary>(고급) 다음 명령어들의 실행 결과와 활용 상황을 설명하시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<code>$ cat file1 file2 > merged.txt</code><br>
<code>$ cat > newfile.txt << EOF</code><br>
<code>$ cat /dev/null > logfile.txt</code>
</div>
</summary>
<blockquote>
1) <code>cat file1 file2 > merged.txt</code> : 두 파일을 연결하여 새 파일로 저장<br>
2) <code>cat > newfile.txt</code> << EOF : HERE 문서를 사용하여 텍스트를 입력받아 파일로 저장 (EOF까지 입력받음)<br>
3) <code>cat /dev/null > logfile.txt</code> : 파일의 내용을 완전히 비움 (파일 크기를 0으로 만듦)<br><br>
세 번째 명령은 로그 파일 초기화나 임시 파일 정리 시 자주 사용된다.
</blockquote>
</details>

###### more/less (File content pager)

<details>
<summary>대용량 로그 파일(/var/log/system.log)을 페이지 단위로 조회하면서 앞뒤로 자유롭게 이동할 수 있는 명령을 쓰시오.</summary>
<blockquote>
<code>less /var/log/system.log</code><br><br>
<code>less</code>는 <code>more</code>와 달리 앞뒤로 자유롭게 이동 가능하며, 검색 기능과 더 많은 기능을 제공한다.
</blockquote>
</details>

<details>
<summary><code>more</code>와 <code>less</code> 명령어의 주요 차이점을 설명하시오.</summary>
<blockquote>
- <code>more</code>: 앞으로만 이동 가능, 기본적인 페이징 기능<br>
- <code>less</code>: 앞뒤로 자유롭게 이동 가능, 검색 기능, 더 많은 기능 제공<br><br>
<code>less</code>는 <code>more</code>의 확장된 버전으로 "less is more"라는 의미를 가진다.
</blockquote>
</details>

###### head (Display first lines)

<details>
<summary>보안 로그 파일(/var/log/auth.log)에서 가장 최근의 로그인 시도 20건을 확인하는 명령을 쓰시오.</summary>
<blockquote>
<code>tail -n 20 /var/log/auth.log</code><br><br>
<code>tail</code> 명령어는 파일의 마지막 부분을 출력하며, <code>-n</code> 옵션으로 출력할 줄 수를 지정할 수 있다.
</blockquote>
</details>

<details>
<summary>(중급) 다음 명령어들의 실행 결과를 설명하시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<code>$ head -n 20 /var/log/syslog</code><br>
<code>$ head -c 100 binary_file</code><br>
<code>$ head -f logfile.txt</code>
</div>
</summary>
<blockquote>
1) <code>head -n 20 /var/log/syslog</code> : syslog 파일의 처음 20줄을 출력<br>
2) <code>head -c 100 binary_file</code> : binary_file의 처음 100바이트를 출력<br>
3) <code>head -f logfile.txt</code> : 잘못된 옵션, <code>head</code>에는 -f 옵션이 없음 (<code>tail -f</code>와 혼동)<br><br>
<code>head</code>는 기본적으로 10줄을 출력하며, <code>-n</code> 옵션으로 줄 수를 지정할 수 있다.
</blockquote>
</details>

###### tail (Display last lines)

<details>
<summary>웹 서버 액세스 로그를 실시간으로 모니터링하여 새로 추가되는 로그 항목을 지속적으로 화면에 출력하는 명령을 쓰시오.</summary>
<blockquote>
<code>tail -f /var/log/apache2/access.log</code><br><br>
<code>tail -f</code> 옵션은 파일의 끝을 실시간으로 모니터링하여 새로 추가되는 내용을 지속적으로 출력한다. 시스템 관리자가 로그를 실시간으로 모니터링할 때 필수적으로 사용하는 명령어이다.
</blockquote>
</details>

<details>
<summary>(고급) 다음 tail 명령어의 고급 사용법과 실제 활용 상황을 설명하시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<code>$ tail -f /var/log/apache2/access.log</code><br>
<code>$ tail -n +100 large_file.txt</code><br>
<code>$ tail -f file1.log file2.log</code>
</div>
</summary>
<blockquote>
1) <code>tail -f /var/log/apache2/access.log</code> : 실시간으로 로그 파일 모니터링 (새로 추가되는 내용 표시)<br>
2) <code>tail -n +100 large_file.txt</code> : 100번째 줄부터 파일 끝까지 출력<br>
3) <code>tail -f file1.log file2.log</code> : 여러 파일을 동시에 실시간 모니터링<br><br>
<code>tail -f</code>는 시스템 관리자가 로그 모니터링할 때 필수적으로 사용하는 명령어이다.
</blockquote>
</details>

##### 파일 조작 명령어

###### mv (Move/Rename files)

<details>
<summary>현재 디렉터리에 있는 모든 .tmp 확장자 파일을 /tmp/backup/ 디렉터리로 이동시키는 명령을 쓰시오.</summary>
<blockquote>
mv *.tmp /tmp/backup/<br><br>
mv 명령어는 파일 이동과 이름 변경에 사용되며, 와일드카드(*)를 사용하여 여러 파일을 한 번에 처리할 수 있다.
</blockquote>
</details>

<details>
<summary>(중급) 다음 mv 명령어 상황들의 결과를 설명하시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<code>$ mv file.txt /tmp/</code><br>
<code>$ mv file.txt newname.txt</code><br>
<code>$ mv *.log /backup/</code><br>
<code>$ mv dir1 dir2</code> (dir2가 존재하지 않는 경우)
</div>
</summary>
<blockquote>
1) <code>mv file.txt /tmp/</code> : file.txt를 /tmp/ 디렉터리로 이동<br>
2) <code>mv file.txt newname.txt</code> : 현재 디렉터리에서 파일 이름을 newname.txt로 변경<br>
3) <code>mv *.log /backup/</code> : 모든 .log 확장자 파일을 /backup/ 디렉터리로 이동<br>
4) <code>mv dir1 dir2</code> : dir1 디렉터리의 이름을 dir2로 변경<br><br>
<code>mv</code>는 같은 파일시스템 내에서는 실제로 데이터를 이동하지 않고 inode만 변경한다.
</blockquote>
</details>

###### cp (Copy files)

<details>
<summary>중요한 설정 파일 /etc/nginx/nginx.conf의 백업을 동일한 디렉터리에 nginx.conf.backup 이름으로 생성하는 명령을 쓰시오.</summary>
<blockquote>
<code>cp /etc/nginx/nginx.conf /etc/nginx/nginx.conf.backup</code><br><br>
<code>cp</code> 명령어는 파일을 복사할 때 사용하며, 중요한 설정 파일의 백업 생성 시 자주 활용된다.
</blockquote>
</details>

<details>
<summary>(고급) 다음 cp 명령어들의 차이점과 각각의 사용 상황을 설명하시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<code>$ cp -r source_dir target_dir</code><br>
<code>$ cp -a source_dir target_dir</code><br>
<code>$ cp -p file.txt backup.txt</code><br>
<code>$ cp -l file.txt hardlink.txt</code>
</div>
</summary>
<blockquote>
1) <code>cp -r</code> : 디렉터리를 재귀적으로 복사 (권한, 타임스탬프 등은 변경될 수 있음)<br>
2) <code>cp -a</code> : 아카이브 모드로 복사 (-dpR과 동일, 모든 속성 보존)<br>
3) <code>cp -p</code> : 파일의 소유권, 권한, 타임스탬프 등을 보존하여 복사<br>
4) <code>cp -l</code> : 하드링크 생성 (실제 복사가 아닌 같은 inode를 가리키는 링크)<br><br>
백업이나 아카이브 작업 시에는 <code>-a</code> 옵션이 가장 적절하다.
</blockquote>
</details>

###### rm (Remove files)

<details>
<summary>파일을 삭제하는 명령어는?</summary>
<blockquote>
<code>rm</code>
</blockquote>
</details>

<details>
<summary>(위험수준 고급) 다음 <code>rm</code> 명령어들의 위험성과 안전한 대안을 제시하시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<code>$ rm -rf /</code><br>
<code>$ rm -f *.txt</code><br>
<code>$ find /home -name "*.tmp" -exec rm {} \;</code><br>
안전한 삭제 방법은?
</div>
</summary>
<blockquote>
<strong>위험한 명령어들:</strong><br>
1) <code>rm -rf</code> / : 루트 디렉터리부터 모든 파일 시스템 삭제 (시스템 파괴)<br>
2) <code>rm -f *.txt</code> : 확인 없이 모든 .txt 파일 강제 삭제<br>
3) <code>find … -exec rm</code> : 조건에 맞는 모든 파일을 자동 삭제<br><br>
<strong>안전한 대안:</strong><br>
- <code>rm -i</code> 옵션으로 삭제 전 확인<br>
- <code>trash</code> 명령어 사용 (복구 가능)<br>
- 중요 파일은 백업 후 삭제<br>
- <code>find … -ok rm</code> 사용 (각 파일마다 확인)<br>
- 스크립트에서는 절대 경로 사용하고 변수 검증
</blockquote>
</details>

###### ln (Create links)

<details>
<summary>파일에 대한 링크를 생성하는 명령어는?</summary>
<blockquote>
ln
</blockquote>
</details>

<details>
<summary>(고급) 하드링크와 심볼릭 링크의 차이점을 다음 명령어 예시와 함께 설명하시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<code>$ ln file.txt hardlink.txt</code><br>
<code>$ ln -s file.txt symlink.txt</code><br>
원본 파일 삭제 시 각 링크에 미치는 영향은?
</div>
</summary>
<blockquote>
<strong>하드링크 (ln file.txt hardlink.txt):</strong><br>
- 같은 inode를 공유, 원본과 동일한 파일<br>
- 원본 삭제되어도 하드링크는 여전히 유효<br>
- 같은 파일시스템 내에서만 생성 가능<br>
- 디렉터리에는 생성 불가<br><br>
<strong>심볼릭 링크 (ln -s file.txt symlink.txt):</strong><br>
- 원본 파일의 경로만 저장하는 별도 파일<br>
- 원본 삭제 시 심볼릭 링크는 깨짐 (dangling link)<br>
- 다른 파일시스템에도 생성 가능<br>
- 디렉터리에도 생성 가능<br><br>
원본 파일 삭제 시 하드링크는 여전히 데이터에 접근 가능하지만, 심볼릭 링크는 접근 불가능하다.
</blockquote>
</details>

##### 권한 및 소유권 관리 명령어

###### chmod (Change file permissions)

<details>
<summary>스크립트 파일 /home/user/backup.sh에 소유자는 읽기/쓰기/실행 권한을, 그룹과 기타 사용자에게는 읽기와 실행 권한만 부여하는 명령을 쓰시오.</summary>
<blockquote>
<code>chmod 755 /home/user/backup.sh</code><br><br>
<code>755</code> 권한은 <code>rwxr-xr-x</code>를 의미하며, 스크립트 파일에 일반적으로 설정하는 권한이다.
</blockquote>
</details>

<details>
<summary>(중급) 다음 chmod 명령어들의 결과로 설정되는 권한을 8진수와 rwx 형태로 설명하시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<code>$ chmod 755 script.sh</code><br>
<code>$ chmod u+x,g-w,o=r file.txt</code><br>
<code>$ chmod a+w document.txt</code>
</div>
</summary>
<blockquote>
1) <code>chmod 755 script.sh</code><br>
   - 8진수: <code>755</code><br>
   - rwx 형태: <code>rwxr-xr-x</code><br>
   - 소유자: 읽기/쓰기/실행, 그룹: 읽기/실행, 기타: 읽기/실행<br><br>
2) <code>chmod u+x,g-w,o=r file.txt</code><br>
   - 소유자에게 실행 권한 추가<br>
   - 그룹에서 쓰기 권한 제거<br>
   - 기타 사용자는 읽기 권한만<br><br>
3) <code>chmod a+w document.txt</code><br>
   - 모든 사용자(all)에게 쓰기 권한 추가
</blockquote>
</details>

<details>
<summary>(고급) SetUID, SetGID, Sticky bit의 개념과 보안상 주의사항을 설명하시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<code>$ chmod 4755 /usr/bin/sudo</code><br>
<code>$ chmod 2755 /shared/project</code><br>
<code>$ chmod 1777 /tmp</code><br>
각각의 의미와 보안 위험성은?
</div>
</summary>
<blockquote>
<strong>SetUID (4755):</strong><br>
- 파일 실행 시 소유자 권한으로 실행<br>
- 보안 위험: root 소유 파일에 설정 시 권한 상승 공격 가능<br>
- 예: sudo 명령어는 root 권한이 필요<br><br>
<strong>SetGID (2755):</strong><br>
- 파일: 소유 그룹 권한으로 실행<br>
- 디렉터리: 생성되는 파일들이 디렉터리의 그룹을 상속<br>
- 보안 위험: 그룹 권한 상승 가능<br><br>
<strong>Sticky Bit (1777):</strong><br>
- 디렉터리에서 파일 소유자만 자신의 파일 삭제 가능<br>
- 주로 /tmp 디렉터리에 설정<br>
- 보안: 다른 사용자의 파일 삭제 방지<br><br>
<strong>보안 주의사항:</strong><br>
- SetUID/SetGID 파일 정기적 점검 필요<br>
- 불필요한 특수 권한 제거<br>
- <code>find / -perm -4000</code> 명령으로 SetUID 파일 검색
</blockquote>
</details>

###### chown (Change file ownership)

<details>
<summary>웹 서버 디렉터리 /var/www/html의 모든 파일과 하위 디렉터리의 소유자를 www-data로, 그룹도 www-data로 변경하는 명령을 쓰시오.</summary>
<blockquote>
<code>chown -R www-data:www-data /var/www/html</code><br><br>
<code>-R</code> 옵션은 재귀적으로 하위 디렉터리까지 포함하여 소유권을 변경한다. <code>user:group</code> 형태로 소유자와 그룹을 동시에 지정할 수 있다.
</blockquote>
</details>

<details>
<summary>(중급) 다음 chown 명령어들의 실행 결과를 설명하시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<code>$ chown user1 file.txt</code><br>
<code>$ chown user1:group1 file.txt</code><br>
<code>$ chown :group1 file.txt</code><br>
<code>$ chown -R user1:group1 /home/project/</code>
</div>
</summary>
<blockquote>
1) <code>chown user1 file.txt</code> : 파일 소유자를 user1으로 변경 (그룹은 변경 안됨)<br>
2) <code>chown user1:group1 file.txt</code> : 소유자를 user1, 그룹을 group1로 변경<br>
3) <code>chown :group1 file.txt</code> : 그룹만 group1로 변경 (소유자는 변경 안됨)<br>
4) <code>chown -R user1:group1 /home/project/</code> : 디렉터리와 모든 하위 파일/디렉터리의 소유자와 그룹을 재귀적으로 변경<br><br>
주의: 일반 사용자는 자신이 소유한 파일의 소유자만 변경할 수 있으며, root만 모든 파일의 소유자를 변경할 수 있다.
</blockquote>
</details>

###### chgrp (Change group ownership)

<details>
<summary>파일이나 디렉터리의 그룹 소유자를 변경하는 명령어는?</summary>
<blockquote>
<code>chgrp</code>
</blockquote>
</details>

<details>
<summary><code>chown</code>과 <code>chgrp</code>의 차이점과 사용 상황을 설명하시오.</summary>
<blockquote>
<strong><code>chgrp</code>:</strong><br>
- 그룹 소유자만 변경<br>
- 더 간단한 문법<br>
- 그룹 관리에 특화<br><br>
<strong><code>chown</code>:</strong><br>
- 소유자, 그룹 또는 둘 다 변경 가능<br>
- 더 포괄적인 기능<br>
- user:group 형태로 동시 변경 가능<br><br>
<strong>사용 상황:</strong><br>
- 그룹만 변경: <code>chgrp</code>가 더 직관적<br>
- 소유자와 그룹 동시 변경: <code>chown</code>이 효율적<br>
- 스크립트에서는 <code>chown</code>이 더 유연함
</blockquote>
</details>

###### touch (Create empty files and change timestamps)

<details>
<summary>빈 파일을 생성하거나 파일의 타임스탬프를 변경하는 명령어는?</summary>
<blockquote>
<code>touch</code>
</blockquote>
</details>

<details>
<summary>(고급) 다음 touch 명령어들의 고급 사용법과 실제 활용 상황을 설명하시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<code>$ touch -t 202312251030 important.txt</code><br>
<code>$ touch -r reference.txt newfile.txt</code><br>
<code>$ touch -a logfile.txt</code><br>
<code>$ touch -m datafile.txt</code>
</div>
</summary>
<blockquote>
1) <code>touch -t 202312251030 important.txt</code><br>
   - 특정 시간(2023년 12월 25일 10:30)으로 타임스탬프 설정<br>
   - 용도: 파일 백업 시 원본 시간 정보 보존<br><br>
1) <code>touch -r reference.txt newfile.txt</code><br>
   - reference.txt와 같은 타임스탬프로 설정<br>
   - 용도: 여러 파일의 시간 정보 동기화<br><br>
1) <code>touch -a logfile.txt</code><br>
   - 접근 시간(atime)만 현재 시간으로 변경<br>
   - 용도: 파일 접근 로그 관리<br><br>
1) <code>touch -m datafile.txt</code><br>
   - 수정 시간(mtime)만 현재 시간으로 변경<br>
   - 용도: 빌드 시스템에서 파일 강제 재컴파일 유도<br><br>
실제 활용: 백업 스크립트, 빌드 시스템, 로그 관리, 테스트 환경 구성
</blockquote>
</details>

###### umask (Set default file permissions)

<details>
<summary>새로 생성되는 파일과 디렉터리의 기본 권한을 설정하는 명령어는?</summary>
<blockquote>
<code>umask</code>
</blockquote>
</details>

<details>
<summary>(고급) umask의 동작 원리와 다음 상황에서의 결과를 계산하시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
현재 umask 설정들에 따른 새 파일/디렉터리 권한:<br>
<code>$ umask 022</code> → 파일 권한: ? 디렉터리 권한: ?<br>
<code>$ umask 077</code> → 파일 권한: ? 디렉터리 권한: ?<br>
<code>$ umask 002</code> → 파일 권한: ? 디렉터리 권한: ?
</div>
</summary>
<blockquote>
<strong><code>umask</code> 동작 원리:</strong><br>
- 기본 권한에서 <code>umask</code> 값을 차감<br>
- 파일 기본 권한: <code>666 (rw-rw-rw-)</code><br>
- 디렉터리 기본 권한: <code>777 (rwxrwxrwx)</code><br><br>
<strong>계산 결과:</strong><br>
1) <code>umask 022</code><br>
   - 파일: <code>666</code> - <code>022</code> = <code>644 (rw-r--r--)</code><br>
   - 디렉터리: <code>777</code> - <code>022</code> = <code>755 (rwxr-xr-x)</code><br><br>
2) <code>umask 077</code><br>
   - 파일: <code>666</code> - <code>077</code> = <code>600 (rw-------)</code><br>
   - 디렉터리: <code>777 - 077</code> = <code>700 (rwx------)</code><br><br>
3) <code>umask 002</code><br>
   - 파일: <code>666</code> - <code>002</code> = <code>664 (rw-rw-r--)</code><br>
   - 디렉터리: <code>777</code> - <code>002</code> = <code>775 (rwxrwxr-x)</code><br><br>
<strong>실무 적용:</strong><br>
- <code>022</code>: 일반적인 시스템 기본값<br>
- <code>077</code>: 보안이 중요한 개인 파일<br>
- <code>002</code>: 그룹 작업 환경
</blockquote>
</details>

##### 텍스트 처리 명령어

###### wc (Word Count)

<details>
<summary>시스템에서 현재 실행 중인 프로세스의 총 개수를 확인하는 명령을 ps와 wc를 조합하여 쓰시오.</summary>
<blockquote>
<code>ps aux | wc -l</code><br><br>
<code>ps aux</code>로 모든 프로세스를 출력하고, <code>wc -l</code>로 줄 수를 계산하여 프로세스 개수를 확인할 수 있다.
</blockquote>
</details>

<details>
<summary>(중급) 다음 wc 명령어들의 출력 결과를 설명하시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<code>$ wc /etc/passwd</code><br>
<code>$ wc -l *.log</code><br>
<code>$ ps aux | wc -l</code><br>
<code>$ wc -c large_file.txt</code>
</div>
</summary>
<blockquote>
1) <code>wc /etc/passwd</code> : /etc/passwd 파일의 줄 수, 단어 수, 문자 수를 모두 출력<br>
2) <code>wc -l *.log</code> : 모든 .log 파일의 줄 수만 출력<br>
3) <code>ps aux | wc -l</code> : 현재 실행 중인 프로세스 수 계산<br>
4) <code>wc -c large_file.txt</code> : 파일의 바이트 수(문자 수) 출력<br><br>
옵션: <code>-l</code>(줄), <code>-w</code>(단어), <code>-c</code>(문자), <code>-m</code>(멀티바이트 문자)
</blockquote>
</details>

###### cut (Extract columns)

<details>
<summary>/etc/passwd 파일에서 사용자명(1번째 필드)과 UID(3번째 필드)만 추출하여 출력하는 명령을 쓰시오.</summary>
<blockquote>
<code>cut -d: -f1,3 /etc/passwd</code><br><br>
<code>-d</code>: 옵션으로 콜론을 구분자로 지정하고, <code>-f1,3</code>으로 1번째와 3번째 필드를 추출한다.
</blockquote>
</details>

<details>
<summary>(고급) 다음 cut 명령어들의 실행 결과와 활용 상황을 설명하시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<code>$ cut -d: -f1,3 /etc/passwd</code><br>
<code>$ cut -c1-10 usernames.txt</code><br>
<code>$ ps aux | cut -c1-11,54-</code><br>
<code>$ echo "192.168.1.100" | cut -d. -f4</code>
</div>
</summary>
<blockquote>
1) <code>cut -d: -f1,3 /etc/passwd</code><br>
   - 콜론(:)으로 구분된 필드 중 1번째(사용자명)와 3번째(UID) 필드 추출<br>
   - 활용: 시스템 사용자 정보 분석<br><br>
2) <code>cut -c1-10 usernames.txt</code><br>
   - 각 줄의 1-10번째 문자만 추출<br>
   - 활용: 긴 사용자명을 짧게 표시<br><br>
3) <code>ps aux | cut -c1-11,54-</code><br>
   - 프로세스 목록에서 사용자(1-11문자)와 명령어(54문자부터 끝까지) 추출<br>
   - 활용: 프로세스 모니터링<br><br>
4) <code>echo "192.168.1.100" | cut -d. -f4</code><br>
   - IP 주소에서 마지막 옥텟(100) 추출<br>
   - 활용: 네트워크 스크립트, 로그 분석<br><br>
실무: 로그 분석, CSV 파일 처리, 시스템 모니터링 스크립트
</blockquote>
</details>

###### paste (Merge lines)

<details>
<summary>여러 파일의 줄을 나란히 합치는 명령어는?</summary>
<blockquote>
<code>paste</code>
</blockquote>
</details>

<details>
<summary>(중급) paste와 cut의 조합 활용법을 설명하시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<code>$ paste file1.txt file2.txt</code><br>
<code>$ paste -d, users.txt ages.txt</code><br>
<code>$ paste -s numbers.txt</code>
</div>
</summary>
<blockquote>
1) <code>paste file1.txt file2.txt</code><br>
   - 두 파일의 각 줄을 탭으로 구분하여 나란히 출력<br><br>
2) <code>paste -d, users.txt ages.txt</code><br>
   - 쉼표(,)를 구분자로 사용하여 합치기<br>
   - CSV 형태로 데이터 결합<br><br>
3) <code>paste -s numbers.txt</code><br>
   - 파일의 모든 줄을 하나의 줄로 연결 (수직→수평)<br><br>
<strong>cut과 paste 조합:</strong><br>
- <code>cut</code>으로 필요한 열 추출 → <code>paste</code>로 여러 파일 결합<br>
- 데이터 전처리 및 리포트 생성에 활용<br>
- 예: <code>cut -d: -f1 /etc/passwd | paste - groups.txt</code>
</blockquote>
</details>

###### tr (Translate characters)

<details>
<summary>로그 파일에서 대문자를 모두 소문자로 변환하여 표준화하는 명령을 <code>cat</code>과 <code>tr</code>을 조합하여 쓰시오.</summary>
<blockquote>
<code>cat logfile.txt | tr 'A-Z' 'a-z'</code><br><br>
<code>tr</code> 명령어는 문자를 변환하거나 삭제하는 데 사용되며, 파이프를 통해 입력을 받아 처리한다.
</blockquote>
</details>

<details>
<summary>(고급) 다음 <code>tr</code> 명령어들의 고급 사용법과 정규표현식 활용을 설명하시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<code>$ echo "HELLO WORLD" | tr 'A-Z' 'a-z'</code><br>
<code>$ tr -d '0-9' &lt; mixed.txt</code><br>
<code>$ tr -s ' ' &lt; text.txt</code><br>
<code>$ cat file.txt | tr '\n' ' '</code>
</div>
</summary>
<blockquote>
1) <code>echo "HELLO WORLD" | tr 'A-Z' 'a-z'</code><br>
   - 대문자를 소문자로 변환: "hello world"<br>
   - 활용: 대소문자 정규화<br><br>
2) <code>tr -d '0-9' &lt; mixed.txt</code><br>
   - 모든 숫자 삭제<br>
   - 활용: 텍스트에서 숫자 제거<br><br>
3) <code>tr -s ' ' &lt; text.txt</code><br>
   - 연속된 공백을 하나로 압축<br>
   - 활용: 텍스트 정리, 로그 파일 정규화<br><br>
4) <code>cat file.txt | tr '\n' ' '</code><br>
   - 모든 줄바꿈을 공백으로 변환 (한 줄로 만들기)<br>
   - 활용: 여러 줄을 하나로 합치기<br><br>
<strong>고급 활용:</strong><br>
- <code>tr -cd '[:print:]'</code> : 출력 가능한 문자만 남기기<br>
- <code>tr '[:lower:]' '[:upper:]'</code> : POSIX 문자 클래스 사용<br>
- dos2unix 효과: <code>tr -d '\r'</code>
</blockquote>
</details>

###### sort (Sort lines)

<details>
<summary>파일의 내용을 정렬하는 명령어는?</summary>
<blockquote>
<code>sort</code>
</blockquote>
</details>

<details>
<summary>(고급) 다음 sort 명령어들의 복잡한 정렬 옵션과 실무 활용을 설명하시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<code>$ sort -k2,2n -k1,1 data.txt</code><br>
<code>$ sort -t: -k3n /etc/passwd</code><br>
<code>$ ls -l | sort -k5rn</code><br>
<code>$ sort -u duplicates.txt</code>
</div>
</summary>
<blockquote>
1) <code>sort -k2,2n -k1,1 data.txt</code><br>
   - 2번째 필드를 숫자로 정렬, 같으면 1번째 필드를 문자로 정렬<br>
   - 복합 정렬 (멀티 키 정렬)<br><br>
2) <code>sort -t: -k3n /etc/passwd</code><br>
   - 콜론(:)을 구분자로 하여 3번째 필드(UID)를 숫자로 정렬<br>
   - 사용자를 UID 순으로 정렬<br><br>
3) <code>ls -l | sort -k5rn</code><br>
   - 파일 크기(5번째 필드)를 숫자로 역순 정렬<br>
   - 큰 파일부터 표시<br><br>
4) <code>sort -u duplicates.txt</code><br>
   - 정렬하면서 중복 제거<br>
   - unique 정렬<br><br>
<strong>주요 옵션:</strong><br>
- <code>-n</code>: 숫자 정렬, <code>-r</code>: 역순, <code>-u</code>: 중복 제거<br>
- <code>-t</code>: 구분자 지정, <code>-k</code>: 키 필드 지정<br>
- <code>-M</code>: 월 이름 정렬, <code>-h</code>: 사람이 읽기 쉬운 숫자 정렬
</blockquote>
</details>

###### uniq (Remove duplicate lines)

<details>
<summary>연속된 중복 줄을 제거하거나 찾는 명령어는?</summary>
<blockquote>
<code>uniq</code>
</blockquote>
</details>

<details>
<summary>(고급) sort와 uniq의 조합 사용법과 차이점을 설명하시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<code>$ sort file.txt | uniq</code><br>
<code>$ sort file.txt | uniq -c</code><br>
<code>$ sort file.txt | uniq -d</code><br>
<code>$ sort file.txt | uniq -u</code><br>
<code>sort -u</code>와 <code>sort | uniq</code>의 차이는?
</div>
</summary>
<blockquote>
1) <code>sort file.txt | uniq</code><br>
   - 전체 파일에서 중복 제거 (정렬 후 uniq)<br><br>
2) <code>sort file.txt | uniq -c</code><br>
   - 각 줄의 출현 횟수와 함께 출력<br>
   - 빈도 분석에 활용<br><br>
3) <code>sort file.txt | uniq -d</code><br>
   - 중복된 줄만 출력 (한 번만)<br>
   - 중복 데이터 찾기<br><br>
4) <code>sort file.txt | uniq -u</code><br>
   - 중복되지 않은 줄만 출력<br>
   - 유일한 데이터만 추출<br><br>
<strong><code>sort -u vs sort | uniq</code>:</strong><br>
- <code>sort -u</code>: 정렬과 동시에 중복 제거 (더 효율적)<br>
- <code>sort | uniq</code>: 정렬 후 별도로 중복 제거 (더 세밀한 제어 가능)<br><br>
<strong>실무 활용:</strong><br>
- 로그 분석: 고유 IP 수 계산<br>
- 데이터 클리닝: 중복 데이터 제거<br>
- 시스템 모니터링: 중복 프로세스 확인
</blockquote>
</details>

##### 파일 분할 및 비교 명령어

###### split (Split files)

<details>
<summary>큰 파일을 여러 개의 작은 파일로 분할하는 명령어는?</summary>
<blockquote>
<code>split</code>
</blockquote>
</details>

<details>
<summary>(고급) 다음 split 명령어들의 용도와 활용 상황을 설명하시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<code>$ split -l 1000 large.log small_</code><br>
<code>$ split -b 100M backup.tar.gz part_</code><br>
<code>$ split -n 5 dataset.txt data_</code><br>
<code>$ split -d -a 3 file.txt chunk_</code>
</div>
</summary>
<blockquote>
1) <code>split -l 1000 large.log small_</code><br>
   - 1000줄씩 분할하여 small_aa, small_ab… 파일 생성<br>
   - 활용: 큰 로그 파일 분석용 분할<br><br>
2) <code>split -b 100M backup.tar.gz part_</code><br>
   - 100MB 단위로 분할<br>
   - 활용: 네트워크 전송, 저장 매체 제약<br><br>
3) <code>split -n 5 dataset.txt data_</code><br>
   - 파일을 5개로 균등 분할<br>
   - 활용: 병렬 처리용 데이터셋 분할<br><br>
4) <code>split -d -a 3 file.txt chunk_</code><br>
   - 숫자 접미사 사용(<code>-d</code>), 3자리 접미사(-a 3)<br>
   - 결과: chunk_000, chunk_001…<br><br>
<strong>실무 활용:</strong><br>
- 로그 분석: 큰 로그 파일 처리<br>
- 백업: 파일 크기 제한<br>
- 병렬 처리: 데이터 분산<br>
- 네트워크: 전송 효율성
</blockquote>
</details>

###### cmp (Compare files)

<details>
<summary>두 파일을 바이트 단위로 비교하는 명령어는?</summary>
<blockquote>
 <code>cmp</code>
</blockquote>
</details>

<details>
<summary>(중급) <code>cmp</code>와 다른 비교 명령어들의 차이점을 설명하시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<code>$ cmp file1.txt file2.txt</code><br>
<code>$ cmp -s file1.txt file2.txt; echo $?</code><br>
<code>$ cmp -l binary1 binary2</code>
</div>
</summary>
<blockquote>
1) <code>cmp file1.txt file2.txt</code><br>
   - 첫 번째 차이점의 위치를 바이트와 줄 번호로 출력<br>
   - 같으면 아무것도 출력하지 않음<br><br>
2) <code>cmp -s file1.txt file2.txt; echo $?</code><br>
   - 조용한 모드(<code>-s</code>), 결과만 종료 코드로 반환<br>
   - <code>0</code>: 동일, <code>1</code>: 다름, <code>2</code>: 오류<br><br>
3) <code>cmp -l binary1 binary2</code><br>
   - 모든 차이점을 바이트 위치와 8진수 값으로 출력<br>
   - 바이너리 파일 비교에 유용<br><br>
<strong>다른 비교 명령어와의 차이:</strong><br>
- <code>cmp</code>: 바이트 단위, 빠름, 간단<br>
- <code>diff</code>: 텍스트 비교, 상세한 차이점<br>
- <code>comm</code>: 정렬된 파일의 공통/고유 요소
</blockquote>
</details>

###### comm (Compare sorted files)

<details>
<summary>정렬된 두 파일의 공통 부분과 고유 부분을 비교하는 명령어는?</summary>
<blockquote>
<code>comm</code>
</blockquote>
</details>

<details>
<summary>(고급) <code>comm</code> 명령어의 출력 형태와 고급 활용법을 설명하시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<code>$ comm file1.txt file2.txt</code><br>
<code>$ comm -12 sorted1.txt sorted2.txt</code><br>
<code>$ comm -23 users_old.txt users_new.txt</code><br>
출력의 3개 열은 무엇을 의미하는가?
</div>
</summary>
<blockquote>
<strong><code>comm</code> 출력 형태 (3개 열):</strong><br>
- 1열: file1에만 있는 줄<br>
- 2열: file2에만 있는 줄<br>
- 3열: 두 파일 공통 줄<br><br>
1) <code>comm file1.txt file2.txt</code><br>
   - 기본 출력: 모든 열 표시<br><br>
2) <code>comm -12 sorted1.txt sorted2.txt</code><br>
   - 1열과 2열 숨김 → 공통 부분만 출력<br>
   - 교집합 구하기<br><br>
3) <code>comm -23 users_old.txt users_new.txt</code><br>
   - 2열과 3열 숨김 → file1에만 있는 항목<br>
   - 삭제된 사용자 찾기<br><br>
<strong>고급 활용:</strong><br>
- <code>comm -13</code>: file2에만 있는 항목 (새로 추가된 것)<br>
- 집합 연산: 교집합, 차집합, 합집합<br>
- 시스템 관리: 사용자/그룹 변화 추적<br>
- 데이터 분석: 목록 비교 및 변화 감지<br><br>
<strong>주의사항:</strong> 파일이 정렬되어 있어야 올바른 결과
</blockquote>
</details>

###### diff (Show differences)

<details>
<summary>두 파일의 차이점을 상세히 보여주는 명령어는?</summary>
<blockquote>
<code>diff</code>
</blockquote>
</details>

<details>
<summary>(전문가급) 다음 diff 명령어들의 출력 형식과 실무 활용을 설명하시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<code>$ diff -u original.txt modified.txt</code><br>
<code>$ diff -r /etc/old/ /etc/new/</code><br>
<code>$ diff -w --ignore-blank-lines file1 file2</code><br>
<code>$ diff -y --left-column file1 file2</code>
</div>
</summary>
<blockquote>
1) <code>diff -u original.txt modified.txt</code><br>
   - Unified format: +/- 기호로 추가/삭제 표시<br>
   - Git과 같은 형식, 가장 일반적<br><br>
2) <code>diff -r /etc/old/ /etc/new/</code><br>
   - 재귀적 디렉터리 비교<br>
   - 시스템 설정 변화 추적<br><br>
3) <code>diff -w --ignore-blank-lines file1 file2</code><br>
   - 공백 무시(<code>-w</code>), 빈 줄 무시<br>
   - 포맷팅 차이 제외하고 내용만 비교<br><br>
4) <code>diff -y --left-column file1 file2</code><br>
   - 나란히 비교(side-by-side)<br>
   - 시각적 비교에 유용<br><br>
<strong>출력 형식:</strong><br>
- 기본: <code>ed</code> 명령어 형식<br>
- <code>-u</code>: Unified (+ - 기호)<br>
- <code>-c</code>: Context (*** --- 기호)<br>
- <code>-y</code>: Side-by-side<br><br>
<strong>실무 활용:</strong><br>
- 소스 코드 버전 비교<br>
- 설정 파일 변화 추적<br>
- 패치 파일 생성<br>
- 백업 검증
</blockquote>
</details>

##### 검색 및 찾기 명령어

###### grep (Search text patterns)

<details>
<summary>시스템 로그 파일(/var/log/auth.log)에서 SSH 로그인 실패 기록을 검색하는 명령을 쓰시오.</summary>
<blockquote>
<code>grep "Failed.*ssh" /var/log/auth.log</code><br><br>
<code>grep</code>은 파일에서 특정 패턴을 검색하는 명령어로, 보안 로그 분석에서 핵심적으로 사용된다.
</blockquote>
</details>

<details>
<summary>(전문가급) 다음 grep의 고급 정규표현식과 보안 관련 활용을 설명하시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<code>$ grep -E '^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' access.log</code><br>
<code>$ grep -r --include="*.conf" "password" /etc/</code><br>
<code>$ grep -v '^#\|^$' config.txt</code><br>
<code>$ grep -A 3 -B 2 "ERROR" system.log</code>
</div>
</summary>
<blockquote>
1) <code>grep -E '^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' access.log</code><br>
   - 확장 정규표현식으로 IP 주소 패턴 검색<br>
   - 로그 분석: 접속 IP 추출<br><br>
1) <code>grep -r --include="*.conf" "password" /etc/</code><br>
   - 특정 파일 확장자만 대상으로 재귀 검색<br>
   - 보안 점검: 설정 파일의 패스워드 노출 검사<br><br>
1) <code>grep -v '^#\|^$' config.txt</code><br>
   - 주석(#)과 빈 줄 제외하고 검색<br>
   - 실제 설정 내용만 추출<br><br>
1) <code>grep -A 3 -B 2 "ERROR" system.log</code><br>
   - 에러 발생 전후 맥락(context) 표시<br>
   - 로그 분석: 에러 원인 파악<br><br>
<strong>보안 활용:</strong><br>
- 로그 모니터링: <code>grep "Failed.*ssh" /var/log/auth.log</code><br>
- 취약점 검사: <code>grep -r "eval.*\$_" /var/www/</code><br>
- 권한 검사: <code>find / -perm -4000 | grep -v expected</code><br>
- 네트워크: <code>netstat -an | grep LISTEN</code><br><br>
<strong>성능 팁:</strong><br>
- <code>-F</code>: 문자열 고정 검색 (정규표현식 안 사용)<br>
- <code>-m</code>: 최대 매치 수 제한
</blockquote>
</details>

###### find (Find files and directories)

<details>
<summary>시스템에서 SetUID 권한이 설정된 모든 파일을 찾아 보안 점검을 수행하는 명령을 쓰시오.</summary>
<blockquote>
<code>find / -type f -perm -4000 2>/dev/null</code><br><br>
<code>find</code> 명령어는 파일 검색에 사용되며, <code>-perm -4000</code> 옵션으로 SetUID 파일을 찾을 수 있다. <code>2>/dev/null</code>로 에러 메시지를 숨긴다.
</blockquote>
</details>

<details>
<summary>(전문가급) 다음 find 명령어들의 고급 사용법과 보안 점검 활용을 설명하시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<code>$ find /home -type f -perm -4000 -ls</code><br>
<code>$ find / -name "*.php" -exec grep -l "eval.*\$_POST" {} \;</code><br>
<code>$ find /tmp -type f -mtime +7 -size +100M -delete</code><br>
<code>$ find /var/log -name "*.log" -newermt "2024-01-01" ! -newermt "2024-01-31"</code>
</div>
</summary>
<blockquote>
1) <code>find /home -type f -perm -4000 -ls</code><br>
   - SetUID 파일 검색 및 상세 정보 출력<br>
   - 보안 점검: 권한 상승 가능한 파일 찾기<br><br>
2) <code>find / -name "*.php" -exec grep -l "eval.*\$_POST" {} \;</code><br>
   - PHP 파일에서 위험한 코드 패턴 검색<br>
   - 보안 감사: 코드 인젝션 취약점 검사<br><br>
3) <code>find /tmp -type f -mtime +7 -size +100M -delete</code><br>
   - 7일 이상 된 100MB 이상 파일 삭제<br>
   - 시스템 관리: 임시 파일 정리<br><br>
4) <code>find /var/log -name "*.log" -newermt "2024-01-01" ! -newermt "2024-01-31"</code><br>
   - 특정 날짜 범위의 로그 파일 검색<br>
   - 로그 분석: 기간별 로그 추출<br><br>
<strong>보안 관련 <code>find</code> 활용:</strong><br>
- <code>find / -perm -2 ! -type l -ls</code> : world-writable 파일<br>
- <code>find / -nouser -o -nogroup</code> : 소유자 없는 파일<br>
- <code>find /etc -type f -perm -o+w</code> : 다른 사용자가 쓸 수 있는 설정 파일<br>
- <code>find / -type f -name ".*" -perm -4000</code> : 숨겨진 SetUID 파일<br><br>
<strong>성능 최적화:</strong><br>
- <code>-prune</code>: 특정 디렉터리 제외<br>
- <code>-maxdepth</code>: 검색 깊이 제한<br>
- <code>-daystart</code>: 자정 기준 시간 계산
</blockquote>
</details>

##### 사용자 정보

##### 그룹 정보

##### 입출력 재지정(I/O Redirection) 기능

##### 파이프 또는 파이프라인 기능

##### 특수 문자(메타 문자, Meta character)

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

#### 파일 시스템 응용
##### 파일 시스템 개요
##### 파일 시스템 링크 파일
##### 디렉터리 관리
##### 파일 권한 관리
##### 파일 검색
##### 파일 및 디렉터리 관련 명령어 요약
#### 프로세스 응용
##### 프로세스 개요
##### 프로세스 정보 확인
##### 프로세스 간 통신(시그널)
### 3. UNIX/Linux 시스템 관리
#### 시스템 시작과 종료
##### 시스템 런 레벨
##### 시스템 시작
<details>
<summary>리눅스의 부팅 과정 중 발생할 수 있는 보안 위협을 방지하기 위해 사용되는 '싱글 모드(Single Mode) 진입 시 패스워드 설정'의 필요성과 설정 방법을 설명하시오.</summary>
<blockquote>
싱글 모드는 루트(root) 권한으로 비밀번호 없이 시스템에 접근하여 설정을 변경할 수 있는 모드이므로, 물리적 접근이 가능한 공격자가 관리자 권한을 탈취하는 것을 방지하기 위해 비밀번호 설정이 필수적이다. `/etc/sysconfig/init` 파일 내의 `SINGLE` 설정을 수정하거나, GRUB 부트로더에 `password`를 설정하여 인증 절차를 강화할 수 있다.
</blockquote>
</details>

##### 시스템 종료
#### 사용자 및 그룹 관리
##### 사용자 관리(추가, 변경 및 삭제)

<details>
<summary>리눅스 환경에서 새로 생성되는 사용자 계정의 홈 디렉터리에 자동으로 복사할 기본 설정 파일들(.bashrc 등)을 저장해 두는 디렉터리 경로를 쓰시오.</summary>
<blockquote>
/etc/skel
</blockquote>
</details>

##### 그룹 관리(추가, 변경 및 삭제)
#### 파일 시스템 관리
##### 파일시스템(디스크) 여유 공간 키그 관리(df 명령어)
##### 디렉터리(파일)별 파일시스템(디스크) 사용량 관리(du 명령어)
#### 작업 스케줄 관리
##### cron 서비스(정기적 작업 스케줄 관리 서비스)
### 4. UNIX/Linux 서버 보안
#### 시스템 보안
##### 사용자의 패스워드 관리
<details>
<summary>리눅스 환경에서 사용자 계정의 패스워드 만료일, 암호 변경 최소/최대 일수 등 패스워드 에이징(Aging) 정보를 저장하고 있는 파일의 절대 경로를 쓰시오.</summary>
<blockquote>
/etc/shadow
</blockquote>
</details>

##### 프로세스 실행권한(SUID,SGID)
<details>
<summary>리눅스 시스템에서 사용자 및 그룹 권한을 제어하는 특수 권한인 SetUID의 개념을 설명하고, 보안 관점에서 SetUID 설정 파일이 위험한 이유를 서술하시오.</summary>
<blockquote>
<strong>개념</strong>: 파일 실행 시 해당 파일의 소유자(owner) 권한으로 실행되도록 하는 파일 확장 속성(권한) 설정이다.<br>
<strong>위험한 이유</strong>: 최고 관리자(root) 소유의 파일에 SetUID가 설정되어 있고 취약점이 존재할 경우, 일반 사용자가 해당 파일을 실행하는 동안 일시적으로 루트 권한을 획득하게 되어 침해 사고로 이어질 수 있기 때문이다.
</blockquote>
</details>

#### 네트워크 보안

##### 보안 쉘(SSH)

##### 슈퍼 서버(inetd 데몬)

##### 접근 통제(TCP Wrapper)

<details>
<summary>IP 관리 시스템에서 발전하여 MAC 기반 통제를 강화한 장비는?</summary>
<blockquote>
NAC (Network Access Control)<br>
- 주요 기능: 접근 제어 및 인증.
</blockquote>
</details>

##### xinetd 슈퍼 데몬

#### PAM(장착형 인증 모듈, Pluggable Authentication Modules)

##### 개요

##### PAM 을 사용한 인증 절차

##### PAM 설정파일(/etc/pam.d/remote 설정파일 일부)

##### PAM 활용 예 1 (시스템 취약점 분석, 평가 항목)

##### PAM 활용 예 2(시스템 취약점 분석, 평가 일부 항목)

##### PAM 활용 예 3(시스템 취약점 분석, 평가 일부 항목)

#### 시스템 로그 설정과 관리

##### 개요

##### 유닉스/리눅스 주요 로그 파일

<details>
<summary>리눅스 시스템 로그 중 다음 설명에 해당하는 로그 파일명을 작성하시오.<br>(가) 사용자의 원격 로그인 정보 저장<br>(나) 시스템 부팅 관련 메시지 저장<br>(다) 사용자가 로그인한 마지막 로그 저장</summary>
<blockquote>
(가) 사용자의 원격 로그인 정보 저장: `/var/log/secure`<br>(나) 시스템 부팅 관련 메시지 저장: `/var/log/dmesg`<br>(다) 사용자가 로그인한 마지막 로그 저장: `/var/log/lastlog`
</blockquote>
</details>

#### syslog 설정 및 관리

##### 개요

#### 리눅스 로그 관리

#### 기타 (추가됨)

<details>
<summary>파일 무결성 검사 기능 및 접근 제어를 제공하며, 루트킷(Rootkit) 감염 여부나 파일 시스템의 변경 사항을 주기적으로 모니터링하여 관리자에게 알림을 제공하는 대표적인 오픈소스 기반 침입 탐지 도구(HIDS)의 명칭과 그 탐지 원리를 서술하시오.</summary>
<blockquote>
<strong>명령 및 도구</strong>: 트립와이어 (Tripwire)<br>
<strong>탐지 원리</strong>: 사전에 시스템 내 중요 파일들의 해시(Hash) 값을 계산하여 데이터베이스에 저장해 둔 뒤, 주기적으로 현재 파일들의 해시 값을 재계산하여 원래의 데이터베이스 값과 비교함으로써 위·변조 여부를 탐지한다.
</blockquote>
</details>

### 5. 시스템 해킹

#### 버퍼 오버플로우 공격(Buffer Overflow Attack)

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

#### 레이스 컨디션 공격(Race Condition Attack)

#### 포맷 스트링 공격(Format String Attack)

<details>
<summary>공격자가 악성 스크립트나 명령어를 삽입하기 위해 취약한 C언어 함수(printf, sprintf 등)를 악용하여 메모리를 변조하거나 정보를 유출하는 공격 기법을 '포맷 스트링(Format String) 공격'이라 한다. 메모리의 특정 위치에 값을 쓰기 위해 공격자가 주로 사용하는 포맷 스트링 인자(Format Specifier) 하나를 쓰시오.</summary>
<blockquote>
%n (또는 %hn)
</blockquote>
</details>
