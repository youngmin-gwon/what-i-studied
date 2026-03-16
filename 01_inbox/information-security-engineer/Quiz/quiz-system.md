---
title: quiz-system
tags: []
aliases: []
date modified: 2026-03-16 18:00:08 +09:00
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

#### 시스템 기본

##### 사용자 정보

<details>
<summary>리눅스/유닉스 시스템에서 사용자 계정 관련 정보가 저장되며, 콜론(:)을 구분자로 하여 총 7개의 필드로 구성되어 있는 시스템 설정 파일의 절대 경로를 쓰시오.</summary>
<blockquote>
/etc/passwd<br><br>
※ 해당 파일은 사용자 계정명, 패스워드 설정 여부, UID, GID, 설명, 홈 디렉터리, 로그인 쉘 정보를 담고 있습니다.
</blockquote>
</details>

<details>
<summary>다음은 <code>/etc/passwd</code> 파일의 특정 계정 설정 라인이다. 각 빈칸 (가)와 (나)에 들어갈 필드의 정확한 명칭을 차례대로 작성하시오.<br>
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<code>root:x:0:0:root:/root:/bin/bash</code><br>
순서대로 [계정명] : [사용자 패스워드] : <strong>( 가 )</strong> : <strong>( 나 )</strong> : [설명] : [홈 디렉터리] : [로그인 쉘] 이다.
</div>
</summary>
<blockquote>
(가) 사용자 ID (UID)<br>
(나) 사용자 기본 그룹 ID (GID)
</blockquote>
</details>

<details>
<summary>리눅스 시스템의 <code>/etc/passwd</code> 파일 두 번째 필드인 '사용자 패스워드' 영역에 <code>x</code> 기호가 적혀 있는 경우, 시스템이 적용하고 있는 패스워드 보호 정책의 명칭과 실제 암호화된 비밀번호가 보관되는 파일의 절대 경로를 쓰시오.</summary>
<blockquote>
<strong>정책 명칭</strong>: shadow 패스워드 정책<br>
<strong>저장 경로</strong>: /etc/shadow<br><br>
※ x 기호는 비밀번호가 없다는 뜻이 아니라 패스워드가 암호화되어 shadow 파일에 분리 저장되어 있다는 의미입니다.
</blockquote>
</details>

<details>
<summary><code>/etc/passwd</code> 파일에서 리눅스 시스템 관리자(슈퍼 유저)인 root 계정에게 부여하도록 시스템상 예약되어 있는 사용자 ID(UID)의 번호 값을 적으시오.</summary>
<blockquote>
0
</blockquote>
</details>

<details>
<summary>(서술형) 동일한 리눅스 시스템 내에서 서로 다른 계정명을 가지는 두 개의 계정이 <code>/etc/passwd</code> 상에서 동일한 UID 값으로 설정된 경우, 운영체제(시스템)는 이 두 계정을 어떻게 인지하고 처리하는지 서술하시오.</summary>
<blockquote>
시스템은 서로 다른 계정명을 사용하더라도 같은 UID를 가지면 완전히 '동일한 사용자(계정)'로 판단하며, 이에 따라 두 계정은 서로 동일한 파일 접근 권한 및 시스템 통제 권한을 갖게 된다.
</blockquote>
</details>

<details>
<summary>(서술형) 시스템 관리자가 일반 사용자의 UID가 <code>0</code>으로 설정된 계정이 존재하는지 주기적으로 점검해야 하는 보안상 핵심적인 이유를 권한 관점에서 서술하시오.</summary>
<blockquote>
root 계정에 할당되는 UID 0을 일반 계정이 부여받게 되면, 악의적인 사용자가 해당 일반 계정으로 접속하는 즉시 시스템으로부터 최고 관리자(root) 권한으로 취급받게 되어, 이를 통해 악성 파일 설치나 중요 시스템 구성 변조 등 전체 시스템 제어권이 탈취되는 심각한 '권한 상승(탈취)' 취약점이 발생할 수 있기 때문이다.
</blockquote>
</details>

<details>
<summary>리눅스 시스템에서 사용자가 파일을 생성할 때, 생성된 자원(파일 등)의 '소유 그룹(Group Ownership)'을 결정하는 기준으로 작용하며 모든 사용자가 필수적으로 하나씩 소속되어야 하는 그룹을 뜻하는 용어는 무엇인지 쓰시오.</summary>
<blockquote>
기본 그룹 (Primary group)
</blockquote>
</details>

<details>
<summary>시스템에서 특정 사용자 계정(예: <code>algisa</code>)에 부여된 UID 번호, 소속된 기본 그룹(gid) ID 파악은 물론 다른 추가적인 보조 그룹(groups) 내역까지 한 번에 조회하고자 할 때, 콘솔에서 사용할 수 있는 가장 기본적인 유닉스/리눅스 명령어는 무엇인지 쓰시오.</summary>
<blockquote>
<code>id</code><br><br>
※ 예시 명령어: <code>id algisa</code>
</blockquote>
</details>

<details>
<summary>(서술형) 리눅스의 <code>/etc/passwd</code> 파일 맨 마지막 필드인 '로그인 쉘(Login shell)' 구역의 기본 기능과, 공격자가 해당 필드 내용을 다른 경로로 변조하였을 때 우려되는 악용 사례를 보안 관점에서 서술하시오.</summary>
<blockquote>
<strong>기본 기능</strong>: 사용자가 로그인을 완료한 후 커널과 상호작용하기 위해 기본적으로 실행될 쉘 프로그램(예: /bin/bash 등)을 지정하는 기능이다.<br>
<strong>악용 사례</strong>: 공격자가 시스템을 침해하여 본 필드에 정상적인 쉘 대신 악성 프로그램이나 악성 쉘(백도어 등) 파일 경로를 연결해 두면, 이후 사용자가 정상적으로 로그인만 하더라도 본인도 모르게 악성 코드가 백그라운드에서 자동 실행되는 방식으로 악용될 수 있다.
</blockquote>
</details>

##### 그룹 정보 및 패스워드 관리

<details>
<summary>리눅스 시스템에서 그룹과 관련된 정보가 저장되는 파일의 절대 경로와, 해당 파일에서 사용하는 각 항목 간의 구분자, 그리고 필드의 총 개수를 쓰시오.</summary>
<blockquote>
<strong>절대 경로</strong>: /etc/group<br>
<strong>구분자</strong>: 콜론 ( : )<br>
<strong>필드 수</strong>: 4개
</blockquote>
</details>

<details>
<summary>다음은 <code>/etc/group</code> 파일에 기록된 특정 라인이다. 각 빈칸에 해당하는 필드의 명칭을 순서대로 작성하시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<code>dev:x:514:alice,bob,eve</code><br>
순서대로 <strong>( A )</strong> : [그룹 패스워드(일반적으로 사용안함)] : <strong>( B )</strong> : <strong>( C )</strong> 이다.
</div>
</summary>
<blockquote>
(A) 그룹명<br>
(B) 그룹 ID (GID)<br>
(C) 그룹에 소속된 사용자 목록
</blockquote>
</details>

<details>
<summary>시스템에서 무한한 시스템 제어 권한을 행사하는 root 계정(UID 0)과 같이, root 그룹 또한 시스템 최상위 관리 그룹으로 예약되어 있다. 기본적으로 root 그룹에 할당되는 그룹 ID(GID) 번호를 적으시오.</summary>
<blockquote>
0
</blockquote>
</details>

<details>
<summary>시스템에서 로그인한 현재 사용자(본인) 또는 특정 지정 사용자의 전체 ID 관련 정보(사용자 ID, 기본 그룹 ID, 보조 그룹 ID)를 콘솔에서 단번에 확인하고자 할 때 사용하는 명령어(영문 소문자)를 쓰시오.</summary>
<blockquote>
<code>id</code>
</blockquote>
</details>

<details>
<summary>(작업형) 다음 명령어 실행 결과 화면을 보고, 콘솔 명령어가 무엇이었을지 그리고 <code>groups</code> 항목에 나열된 값들이 의미하는 바를 서술하시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
[root@Fedora ~]# <strong>( 명령어 입력 )</strong><br>
uid=519(algisa) gid=514(dev) groups=514(dev),10(wheel)
</div>
</summary>
<blockquote>
<strong>입력한 명령어</strong>: <code>id algisa</code><br>
<strong>groups의 의미</strong>: 해당 사용자(algisa)가 소속되어 있는 '기본 그룹(dev)'과 '보조 그룹(wheel)' 등 추가 권한이 부여된 모든 그룹 목록의 ID(GID)들을 의미한다.
</blockquote>
</details>

<details>
<summary>계정의 비밀번호를 주기적으로 변경하거나 신규 계정의 패스워드를 최초 설정할 때 사용하는 유닉스/리눅스 기본 쉘 명령어(영문 소문자)를 쓰시오.</summary>
<blockquote>
<code>passwd</code>
</blockquote>
</details>

<details>
<summary>(서술형) 리눅스 시스템에서 <code>passwd</code> 명령어를 통한 패스워드 변경 작업을 수행할 때, 보안상 '일반 사용자'의 권한 한계와 '슈퍼 유저(root)'의 권한 범위를 명확히 비교하여 서술하시오.</summary>
<blockquote>
일반 사용자는 오직 자신의 패스워드만 변경할 수 있지만, 슈퍼 유저(root)는 자신은 물론 시스템에 등록된 모든 사용자 계정의 패스워드를 임의로 강제 변경할 수 있는 전결 권한을 가진다.
</blockquote>
</details>

<details>
<summary>(서술형) 어떤 일반 사용자가 자신의 패스워드를 <code>passwd</code> 명령어로 변경하려 할 때와, 슈퍼 유저(root)가 다른 사용자의 패스워드를 변경하려 할 때 입력 단계에서 나타나는 가장 큰 기능적 차이점을 서술하시오.</summary>
<blockquote>
일반 사용자가 자신의 패스워드를 변경하려 할 때는 먼저 변경 전 '현재 패스워드(Current UNIX password)'를 필수로 입력하여 본인 인증을 거쳐야 하지만, 슈퍼 유저(root)가 타 사용자의 패스워드를 변경할 때는 기존 패스워드 확인 과정 없이 즉시 신규 패스워드 설정 모드로 진입한다.
</blockquote>
</details>

<details>
<summary>관리자(root) 권한으로 터미널에 접속한 상태에서 특정 사용자 계정인 <code>algisa</code> 의 패스워드를 강제로 변경(초기화)해주기 위해, 명령 프롬프트에서 입력해야 하는 명령어 전체 구문을 쓰시오.</summary>
<blockquote>
<code>passwd algisa</code>
</blockquote>
</details>

##### 입출력 재지정 (I/O Redirection)

<details>
<summary>리눅스/유닉스 시스템에서 커널에 의해 프로세스가 생성될 때, 해당 프로세스가 기본적인 입출력을 수행하기 위해 기본적으로 자동 오픈(할당)하는 3가지 통신 채널(파일)의 명칭과 각 통신 채널에 부여되는 고유한 파일 번호(FD)를 각각 짝지어 쓰시오.</summary>
<blockquote>
<strong>표준 입력 (STDIN)</strong>: 0<br>
<strong>표준 출력 (STDOUT)</strong>: 1<br>
<strong>표준 에러 (STDERR)</strong>: 2
</blockquote>
</details>

<details>
<summary>(서술형) 유닉스/리눅스의 '입출력 재지정(I/O Redirection)' 기능의 개념을 표준 채널(표준 입력/출력/에러)과 연관 지어 서술하시오.</summary>
<blockquote>
일반적으로 프로세스 실행 시 설정되는 기본 장치인 키보드나 모니터(터미널 화면) 대신, 표준 입력(0), 표준 출력(1), 표준 에러(2)의 방향을 다른 특정 텍스트 파일 등으로 돌려 입력을 받거나 출력결과를 저장하도록 방향을 재지정(Redirection)하는 기능이다.
</blockquote>
</details>

<details>
<summary>명령어 수행 결과 얻어지는 표준 출력이나 표준 에러를 터미널 화면에 띄우지 않고 파일로 덮어쓰거나(overwrite) 추가(append)하기 위해 사용하는 리눅스 터미널 기호 두 가지를 각각 쓰시오.</summary>
<blockquote>
<strong>덮어쓰기 (Overwrite)</strong>: <code>&gt;</code> (또는 <code>1&gt;</code>)<br>
<strong>추가하기 (Append)</strong>: <code>&gt;&gt;</code> (또는 <code>1&gt;&gt;</code>)
</blockquote>
</details>

<details>
<summary>어떤 명령어(예: <code>id alice</code>)의 정상적인 실행 결과(표준 출력)를 터미널 화면이 아닌 <code>id.out</code> 파일에 저장하려 한다. 단, 기존 <code>id.out</code> 파일 내에 이미 저장된 내용을 보존하면서 밑에 이어서 새로운 결과를 기록(Append)하고 싶다면 어떻게 명령어를 작성해야 하는지 전체 문구(기호 포함)를 완성하시오.</summary>
<blockquote>
<code>id alice &gt;&gt; id.out</code> (또는 <code>id alice 1&gt;&gt; id.out</code>)
</blockquote>
</details>

<details>
<summary>파일 식별자인 FD(File Descriptor) 중에서 <code>2</code>가 의미하는 바를 쓰고, 이를 활용하여 에러 메시지를 <code>error.log</code> 파일에 덮어써서 기록하는 방법을 기호와 함께 작성하시오.</summary>
<blockquote>
<strong>의미</strong>: 표준 에러 (STDERR)<br>
<strong>작성 방법</strong>: 명령어 <code>2&gt; error.log</code>
</blockquote>
</details>

<details>
<summary>명령어를 실행할 때, 관리자가 FD 기호를 전혀 명시하지 않고 단순히 기호 <code>&gt;</code>만 썼을 경우, 쉘(shell)은 이 기호 앞에 어떤 FD 번호가 기본으로 생략된 것으로 간주하는지 쓰시오.</summary>
<blockquote>
1 (표준 출력, STDOUT)
</blockquote>
</details>

<details>
<summary>다음 명령어 실행 흐름을 분석하고, 명령어 <code>id bob 1&gt; id.out</code>를 실행했을 때 기존 <code>id.out</code> 파일이 어떻게 변화하는지 서술하시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<code># id alice &gt; id.out</code><br>
<code># cat id.out</code> (결과: uid=529(alice) … )<br>
<code># id bob 1&gt; id.out</code>
</div>
</summary>
<blockquote>
<code>&gt;</code>(또는 <code>1&gt;</code>) 기호는 Overwrite(덮어쓰기) 모드로 동작하기 때문에, 방금 전에 저장해 둔 기존 파일(<code>id.out</code>)의 내용 전체(alice 관련 결과)를 지워버리고 방금 실행한 명령어 결과(bob 관련 결과)만 새롭게 저장하게 된다.
</blockquote>
</details>

<details>
<summary>(작업형) 다음 명령어 입력 결과를 분석하시오. 아래 <code>ls -l a.dat b.dat</code> 명령어를 실행했는데 화면에는 에러 한 줄과 정상 출력 한 줄이 섞여 나왔다. 이를 다시 재지정하기 위해 다음과 같이 명령을 입력했다. <code>ls -l a.dat b.dat 1&gt; ls.out 2&gt; ls.err</code>. 이후 <code>cat ls.err</code> 명령을 입력했을 때 화면에 출력될 것으로 예상되는 내용을 문장 구조로 서술하시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<code>[root@Fedora ~]# ls -l a.dat b.dat</code><br>
<code>ls: cannot access b.dat: No such file or directory</code><br>
<code>-rw-r--r-- 1 root root 0 2024-02-11 16:11 a.dat</code>
</div>
</summary>
<blockquote>
<code>2&gt; ls.err</code> 로 표준 에러가 재지정되었기 때문에, 에러 메시지인 <code>ls: cannot access b.dat: No such file or directory</code> 만이 <code>ls.err</code> 파일에 저장되며 터미널(모니터)에는 아무것도 출력되지 않고 오직 파일 안의 에러 내용만 확인된다.
</blockquote>
</details>

<details>
<summary>(고급) 어떤 명령이 발생시키는 표준 출력(1)과 표준 에러(2) 메시지를 터미널에 띄우지 않고 몽땅 하나의 파일(예: <code>ls.out</code>)에 한데 모아 저장하고 싶다. 이를 처리하기 위한 리눅스 문법에서 <code>표준 에러(2)</code>를 앞서 정해둔 <code>표준 출력(1)</code>의 결과물로 합쳐서 재지정하겠다는 의미로 사용하는 기호와 명령 구성 방식을 파일명을 이용하여 직접 쓰고 해석하시오.</summary>
<blockquote>
<strong>기호 및 명령 구성 예시</strong>: <code>명령어 &gt; ls.out 2&gt;&amp;1</code><br>
<strong>해석</strong>: 우선 <code>&gt; ls.out</code> (즉, <code>1&gt; ls.out</code>)로 명령의 정상 출력 결과(1)를 <code>ls.out</code> 파일로 보내도록 재지정한다. 그 다음 뒤에 오는 <code>2&gt;&amp;1</code> 문법을 이용해, 표준 에러(2) 또한 이미 설정해 둔 표준 출력(&amp;1)의 경로인 동일 파일(ls.out)로 함께 합쳐서 재지정한다는 뜻이다. 이를 통해 정상 메시지와 에러 메시지가 모두 하나의 파일에 저장된다.
</blockquote>
</details>

<details>
<summary>(단답형) 표준 입력(STDIN, 0)의 방향을 키보드가 아닌 특정 '파일'로 재지정하는 기호와, 사용자가 지정한 '종료 문자열'이 나타날 때까지의 입력 내용을 한꺼번에 전달하는 Here-Document 기호를 각각 쓰시오.</summary>
<blockquote>
<strong>파일 입력 재지정</strong>: <code>&lt;</code> (또는 <code>0&lt;</code>)<br>
<strong>Here-Document</strong>: <code>&lt;&lt;</code>
</blockquote>
</details>

<details>
<summary>(서술형) 입출력 재지정 기호 중 <code>&lt;</code>와 <code>&lt;&lt;</code>의 동작 메커니즘의 차이점을 '입력 소스(Source)' 관점에서 비교하여 기술하시오.</summary>
<blockquote>
- <strong><code>&lt;</code> (Input Redirection)</strong>: 시스템에 이미 존재하는 물리적인 <strong>파일</strong>로부터 데이터를 읽어와서 명령어의 표준 입력으로 전달한다.<br>
- <strong><code>&lt;&lt;</code> (Here-Document)</strong>: 별도의 파일 없이 터미널 또는 스크립트 내에서 직접 텍스트를 입력받으며, 미리 지정한 전용 <strong>종료 태그(Delimiter)</strong>가 나오기 전까지의 모든 내용을 하나의 입력 스트림으로 만들어 명령어에 전달한다.
</blockquote>
</details>

<details>
<summary>(작업형) 다음 명령어를 실행하여 <code>memo.txt</code> 파일에 "Hello Linux"와 "Study Redirection"이라는 두 줄의 내용을 직접 입력하여 저장하고자 한다. <code>cat</code> 명령어와 Here-Document(<code>&lt;&lt;</code>) 기호를 사용하여 전체 명령 구문을 완성하시오. (단, 종료 태그는 <code>EOF</code>를 사용한다고 가정)</summary>
<blockquote>
<code>cat &gt; memo.txt &lt;&lt; EOF</code><br>
<code>Hello Linux</code><br>
<code>Study Redirection</code><br>
<code>EOF</code><br>
(※ <code>cat &lt;&lt; EOF &gt; memo.txt</code> 형태도 가능함)
</blockquote>
</details>

##### 파이프(Pipe) 또는 파이프라인(Pipeline) 기능

<details>
<summary>유닉스 초기 시절부터 지원하는 프로세스 간 통신(IPC) 기법의 하나로, 한 프로세스의 표준 출력(Standard Output)을 다른 프로세스의 표준 입력(Standard Input)으로 직접 전달해주는 기능의 명칭은?</summary>
<blockquote>
파이프 (Pipe) 또는 파이프라인 (Pipeline)
</blockquote>
</details>

<details>
<summary>파이프 기능을 적용하여 앞서 실행되는 명령어의 결과 데이터를 뒤따르는 명령어의 입력 데이터로 넘기고자 할 때, 그 명령어 체인 사이에 삽입해야 하는 특수 기호를 쓰시오.</summary>
<blockquote>
<code>|</code> (파이프 기호, 수직선/버티컬 바)
</blockquote>
</details>

<details>
<summary>(서술형) 여러 개의 명령어가 <code>command1 | command2 | command3</code> 형태로 파이프라인을 구축하고 있을 때, 중간에 있는 <code>command2</code> 가 입력과 출력의 관점에서 시스템적으로 어떻게 기능하는지 메커니즘을 구체적으로 서술하시오.</summary>
<blockquote>
<code>command2</code>는 <code>command1</code>이 작업을 마치고 뿜어내는 '표준 출력' 데이터를 자신의 '표준 입력'으로 흡수하여 자체 내부 프로세스로 가공 및 처리한 후, 그 변환된 결과를 다시 자신의 '표준 출력'으로 내보내어 다음 순서인 <code>command3</code>의 '표준 입력'으로 안전하게 전달하는 브릿지(파이프) 역할을 수행한다.
</blockquote>
</details>

<details>
<summary>(작업형) 디렉터리 내에 있는 파일 중 내용이 몹시 긴 파일 <code>syslog</code> 의 출력 결과를 터미널에서 한 번에 스크롤되어 지나가지 않도록 화면 크기 단위로 끊어서 한 페이지씩 조회하고자 한다. 이때 <code>cat</code> 명령과 <code>more</code> 명령을 파이프 기호로 연계하여 하나의 명령 구문으로 작성하시오.</summary>
<blockquote>
<code>cat syslog | more</code>
</blockquote>
</details>

<details>
<summary>파이프 기능과 가장 자주 쓰이는 명령어 중 하나로, 파일 내용이나 들어온 입력 스트림 데이터에서 자신이 지정한 특정 패턴(문자열 등)을 필터링하여 일치하는 '행'만 출력해 주는 핵심 필터링 도구의 명칭은 무엇인지 쓰시오.</summary>
<blockquote>
<code>grep</code>
</blockquote>
</details>

<details>
<summary>(작업형) 사용자 계정 정보가 담겨 있는 저장소인 패스워드 파일의 전체 내용을 불러온 후, 파이프 기법을 이용해 <code>alice</code> 라는 특정 문자열(계정명 등)이 포함된 정보 내역만 필터링해 모니터에 출력하려 한다. 이에 알맞은 명령 구문을 작성하시오.</summary>
<blockquote>
<code>cat /etc/passwd | grep alice</code>
</blockquote>
</details>

<details>
<summary>(작업형) 콘솔을 통해 시스템에서 현재 가동 중인 전체 프로세스 목록(ps -ef)을 모두 확인한 후, 그 수많은 프로세스 속에서 아파치 웹 데몬인 <code>httpd</code> 문자열이 포함된 프로세스 라인만 콕 집어 출력하고자 한다. 파이프를 이용한 전체 조합 명령어를 완성하시오.</summary>
<blockquote>
<code>ps -ef | grep httpd</code>
</blockquote>
</details>

<details>
<summary><code>grep</code> 명령어를 사용할 때 자신이 조건으로 지정한 특정 패턴(문자열) 데이터가 <strong>포함되지 않은</strong>(제외된) 행 데이터만을 거꾸로 화면에 결과로 출력하고자 할 경우 사용해야 하는 문자 옵션을 기호와 함께 쓰시오.</summary>
<blockquote>
<code>-v</code>
</blockquote>
</details>

<details>
<summary>(고급/작업형) 윈도우와는 달리 리눅스 시스템에서 데몬 프로세스를 점검하기 위해 <code>ps -ef | grep vsftpd</code> 명령을 쳤을 때, `vsftpd` 문구가 포함된 내역 뿐 아니라 내가 검색하려고 파이프라인으로 연결하여 입력한 명령 <code>grep vsftpd</code> 프로세스 자체도 결과에 줄바꿈되어 함께 출력된다고 가정하자.<br>이때 다시 한 번 파이프 기호를 연쇄적으로 덧붙여 명령을 내림으로써, 검색을 위해 입력한 grep 구문은 빼고 순수하게 <code>vsftpd</code> 프로세스 라인만 깔끔하게 도출하려 한다. 빈칸에 들어갈 명령어를 작성하시오.<br>
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<code>ps -ef | grep vsftpd |</code> <strong>[ 빈 칸 ]</strong>
</div>
</summary>
<blockquote>
<code>grep -v grep</code>
</blockquote>
</details>

##### 특수 문자 (메타 문자, Meta Character)

<details>
<summary>쉘 명령에서 사전에 정의된 특별한 기능이 있는 문자를 메타 문자라고 한다. 이 중 현재 내 작업 위치와 그 위 디렉터리를 지칭하는 각각의 특수 문자 기호를 쓰시오.</summary>
<blockquote>
<strong>.</strong> : 현재 작업 디렉터리<br>
<strong>..</strong> : 상위 디렉터리
</blockquote>
</details>

<details>
<summary>(작업형) 리눅스 쉘에서 <code>cd ~</code> 명령을 입력하면 사용자는 자신의 홈 디렉터리로 즉시 이동한다. 그렇다면 본인의 홈 디렉터리가 아닌 다른 대리 사용자(예: algisa)의 홈 디렉터리(예: /home/algisa)로 단번에 이동하고자 할 때 사용하는 명령어 구문을 기호를 포함해 작성하시오.</summary>
<blockquote>
<code>cd ~algisa</code>
</blockquote>
</details>

<details>
<summary>리눅스 쉘(터미널)에서 파일 백업 등 오래 걸리는 특정 명령어를 화면 조작 없이 '백그라운드(Background)' 모드로 안보이게 계속 실행시키려 할 때, 명령어 구문 마지막에 덧붙이는 특수 문자 기호는 무엇인지 쓰시오.</summary>
<blockquote>
<code>&</code> (앰퍼샌드 기호)
</blockquote>
</details>

<details>
<summary>쉘 스크립트 작성 시 실행과 무관하게 참고용 설명을 남기기 위해 사용하는 '주석(Comment)' 기호와, 시스템 내부 환경 설정값인 '쉘 변수(Shell Variable)'의 값을 읽어들일 때 변수명 앞에 접두사처럼 붙이는 기호를 각각 차례대로 쓰시오.</summary>
<blockquote>
<strong>주석</strong>: <code>#</code><br>
<strong>쉘 변수 호출</strong>: <code>$</code>
</blockquote>
</details>

<details>
<summary>(서술형) 리눅스의 특수 문자(메타 문자) 중 파일 시스템 검색에 흔히 쓰이는 와일드카드(Wildcard)인 <code>*</code> 기호와 <code>?</code> 기호의 대체(치환) 원리에 대한 차이점을 서술하시오.</summary>
<blockquote>
<code>*</code> 기호는 임의의 문자가 0개 이상(길이 무관) 나타나는 모든 문자열을 와일드카드로 대체하지만, <code>?</code> 기호는 정확히 '임의의 1개 문자' 분량만을 제한적으로 와일드카드 치환(대체)한다.
</blockquote>
</details>

<details>
<summary>(작업형) 현재 디렉터리에 <code>ab.dat</code>, <code>a.dat</code>, <code>ab.txt</code>, <code>a.txt</code> 파일들이 존재하고 있다. 이 중에서 파일 이름이 임의의 '단 한 글자'로 되어 있으며 확장자가 <code>.dat</code>로 일치하는 파일(즉, a.dat)만을 정확히 집어내 출력하고자 한다. 와일드카드 문자를 알맞게 사용하여 파일 목록(<code>ls</code>) 출력 명령어를 작성하시오.</summary>
<blockquote>
<code>ls ?.dat</code>
</blockquote>
</details>

<details>
<summary>(작업형) 이번에는 디렉터리에 존재하는 파일들 중 파일 이름이 <code>ab</code>라는 문자열로 시작하기만 하면 뒤를 잇는 확장자나 문자열 길이에 상관없이 무조건 전부 출력하고자 한다. 와일드카드를 사용해 가장 적절한 <code>ls</code> 검색 명령어를 작성하시오.</summary>
<blockquote>
<code>ls ab*</code>
</blockquote>
</details>

<details>
<summary>쉘에서 여러 낱개의 명령어들을 키보드로 한 줄에 길게 기입하여, 첫 번째 명령부터 마지막 명령까지 연속적으로 차례차례 순차 실행하게 해주는 명령 구분자(Separator) 기능의 특수 기호는 무엇인가?</summary>
<blockquote>
<code>;</code> (세미콜론 기호)
</blockquote>
</details>

<details>
<summary>(작업형) 시스템 운영 상태 점검 등을 위해, ①현재 날짜와 시간 확인(<code>date</code>), ②현재 사용 중인 본인의 셸 접속 계정명 확인(<code>whoami</code>), ③본인 계정의 그룹/ID 상세 권한 내역 출력(<code>id</code>)이라는 세 가지 독립적인 명령을 마치 하나의 스크립트처럼 엔터 한 번에 연속 실행되도록 만들고자 한다. 명령 구분자 기호를 사용해 한 줄 코드를 작성하시오.</summary>
<blockquote>
<code>date; whoami; id</code>
</blockquote>
</details>

#### 파일 시스템 응용

##### 파일 시스템 개요

<details>
<summary>(단답형) 물리적인 저장 장치에 파일을 생성, 저장, 관리하기 위한 기법으로, 파티션별로 고유하게 생성되는 논리적인 자료 구조를 무엇이라 하는가?</summary>
<blockquote>
파일 시스템 (File System)
</blockquote>
</details>

<details>
<summary>(단답형) 파일 시스템을 구성하는 주요 블록 요소 중 파일 시스템 자체를 관리하기 위한 정보를 주로 담고 있는 블록은 무엇인가?</summary>
<blockquote>
슈퍼 블록 (Superblock)
</blockquote>
</details>

<details>
<summary>(단답형) 파일의 실제 이름(파일명)은 inode가 아닌 시스템의 어디에서 관리되는가?</summary>
<blockquote>
디렉터리 (Directory)
</blockquote>
</details>

<details>
<summary>(서술형) 리눅스의 파일 시스템을 구성하는 주요 4가지 블록 영역(부트 블록, 슈퍼 블록, 아이노드 리스트, 데이터 블록)에 대해 각 구역의 역할을 간략히 설명하시오.</summary>
<blockquote>
1. 부트 블록(Boot block): 운영체제를 부팅하기 위한 부트스트랩 코드가 저장된다.<br>
2. 슈퍼 블록(Superblock): 파일 시스템 전체를 관리하고 작동시키기 위한 정보를 담고 있다.<br>
3. 아이노드 리스트(inode list): 파일의 속성(주요 시간, 소유자, 접근 권한 등)을 담고 있는 inode 구조체 리스트가 위치한다.<br>
4. 데이터 블록(Data block): 실제 파일의 내용(데이터)이 저장되는 고정 크기의 블록 영역이다.
</blockquote>
</details>

<details>
<summary>(서술형) inode 구조체에 저장되는 시간 속성인 MAC Time의 세 가지 요소를 나열하고, 특히 변경 시간(Last Change Time, ctime)과 수정 시간(Last Modification Time, mtime)의 차이점을 구별하여 서술하시오.</summary>
<blockquote>
- <strong>요소</strong>: Modification Time(수정 시간), Access Time(접근 시간), Change Time(변경 시간)<br>
- <strong>차이점</strong>: Modification Time은 파일의 <strong>'실제 내용(데이터)'</strong>이 수정된 최종 시간이다. 반면, Change Time은 내용이 아닌 소유자나 접근 권한의 변경과 같이 파일의 <strong>'inode 속성 정보'</strong>가 갱신된 시간이다.
</blockquote>
</details>

<details>
<summary>(서술형) 침해 사고 발생 시 시스템 분석을 위해 주로 파일의 inode 시간 정보를 기준으로 타임라인 분석을 수행한다. 공격자가 파일의 속성이나 권한 정보를 무단으로 변경했을 때 MAC Time 중 어떤 시간이 영향을 받는지 설명하시오.</summary>
<blockquote>
공격자가 내용 대신 속성(접근 권한, 소유자 UID 등)을 수정하게 되면 inode 관련 정보가 변경되므로, MAC Time 중 <strong>Last Change Time(변경 시간, ctime)</strong>의 갱신이 발생한다.
</blockquote>
</details>

<details>
<summary>(작업형) 파일 권한 변경, 소유권 수정 등이 아니라, 특정 파일(예: <code>/etc/passwd</code>)의 MAC Time을 포함하여 소유자 및 권한 등의 상세 inode 속성 정보를 리눅스 셸 상에서 직접 확인하고자 할 때 사용하는 가장 기본적인 명령어를 쓰시오.</summary>
<blockquote>
<code>stat /etc/passwd</code>
</blockquote>
</details>

<details>
<summary>(작업형) 공격자가 권한 설정을 공격하기 위해 의도적으로 터미널 셸에서 특정 파일의 속성을 다음과 같이 변경하였다고 가정한다. 이 과정 직후에 파일 시간 검사 시 MAC Time 중 새롭게 변경된 시간은 무엇인가?
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<code>$ chmod 777 target_file.txt</code><br>
<code>$ stat target_file.txt</code>
</div>
</summary>
<blockquote>
Last Change Time (또는 ctime, 변경 시간)
</blockquote>
</details>

<details>
<summary>(작업형) 분석관이 침해 여부 흔적을 확인하고자 <code>cat log_file.txt</code> 명령 등을 사용해 파일 내용을 스크린으로 여러 번 읽어들였다. 이 과정에서 직접적으로 갱신되는 파일의 inode MAC Time 속성은 무엇인가?</summary>
<blockquote>
Access Time (접근 시간)
</blockquote>
</details>

##### 파일 시스템 링크 파일

<details>
<summary>(단답형) 기존 파일과 동일한 inode number를 공유하여, 원본 파일이 삭제되더라도 계속해서 데이터에 접근할 수 있게 해주는 방식의 링크 파일은 무엇인가?</summary>
<blockquote>
하드 링크 (Hard link)
</blockquote>
</details>

<details>
<summary>(단답형) 하드 링크와 달리, inode number 대신 원본 파일에 대한 '파일 경로'를 내용으로 가지며 윈도우의 바로가기 아이콘과 유사한 방식을 가지는 링크를 무엇이라 하는가?</summary>
<blockquote>
심볼릭 링크 (Symbolic link / Soft link)
</blockquote>
</details>

<details>
<summary>(단답형) 파일이나 디렉터리에 생성 제한이 없어 자유롭게 사용할 수 있지만, 원본 파일이 삭제되거나 이동하게 되면 링크가 끊겨서 접근이 불가능해지는 링크 파일은 어떤 종류의 링크인가?</summary>
<blockquote>
심볼릭 링크 (Symbolic link)
</blockquote>
</details>

<details>
<summary>(서술형) 동일한 파일 시스템 영역 내에서만 하드 링크를 생성할 수 있는 이유를 inode 관점에서 서술하시오.</summary>
<blockquote>
하드 링크는 기존 파일과 동일한 <strong>inode number</strong>를 가리키는 방식으로 생성되는데, <strong>inode number는 개별 파일 시스템(파티션)마다 독립적으로 매겨지는 고유한 값</strong>이므로, 다른 파일 시스템의 inode와는 충돌이나 식별 불가 문제가 발생하여 동일 파일 시스템 내에서만 생성될 수 있다.
</blockquote>
</details>

<details>
<summary>(서술형) 원본 파일에 대해 하드 링크와 심볼릭 링크 파일을 각각 만들었을 때, 원본 파일을 삭제(rm)한 후 하드 링크 파일과 심볼릭 링크 파일에 접근할 때 어떠한 현상이 나타나는지 비교하여 설명하시오.</summary>
<blockquote>
하드 링크가 생성되면 해당 inode의 <strong>링크 카운트(link count)</strong>만 1 증가하며 실 데이터는 그대로 존재합니다. 따라서 원본 파일을 삭제(링크 카운트 1 감소)하더라도 링크 카운트가 0이 되지 않기 때문에, <strong>하드 링크 파일은 정상적으로 원본 데이터를 읽을 수 있습니다</strong>.<br>
반면 심볼릭 링크는 대상의 <strong>경로(path) 문자열</strong>만을 가지고 있어, 연결 대상인 원본 파일이 사라지면 대상을 찾지 못하는 연결 끊김(dangling link) 현상이 발생하여 <strong>접근할 수 없게 됩니다</strong>.
</blockquote>
</details>

<details>
<summary>(서술형) 특정 파일에 대해 하드 링크를 새롭게 하나 생성하였을 때 내부 파일 시스템에서 일어나는 변화(inode 및 link count 관점)와, 추후에 그 파일을 삭제할 때 시스템이 내부 데이터를 실제로 삭제하는 기준에 대해 설명하시오.</summary>
<blockquote>
하드 링크를 생성하면 원본 파일과 같은 inode를 참조하는 파일이 추가되므로, <strong>해당 inode의 링트 카운트(link count)가 1 증가</strong>하게 됩니다.<br>
파일 삭제 시 운영체제는 즉시 데이터를 지우지 않고 <strong>링크 카운트를 먼저 1 감소</strong>시키며, 만약 값이 <strong>0이 되는 순간(즉, 이 inode를 참조하는 링크 파일이 더 이상 없을 때)에만 inode 정보 및 실제 데이터를 파일 시스템에서 안전하게 삭제</strong>합니다.
</blockquote>
</details>

<details>
<summary>(작업형) <code>/test/source.txt</code> 라는 기존 파일이 존재할 때, 이 파일에 대한 심볼릭 링크 파일인 <code>/test/sym_link.txt</code> 를 생성하기 위한 명령어를 쓰시오.</summary>
<blockquote>
<code>ln -s /test/source.txt /test/sym_link.txt</code>
</blockquote>
</details>

<details>
<summary>(작업형) 디렉터리 내에서 <code>ls -li</code> 명령을 실행하여 아래와 같은 결과를 확인하였다. 두 파일이 서로 <strong>하드 링크</strong> 관계에 있다는 사실을 유추할 수 있는 결과의 특징 두 가지를 나열하시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<code>164965 -rw-r--r-- 2 root root 11 Feb 8 00:52 abc.dat</code><br>
<code>164965 -rw-r--r-- 2 root root 11 Feb 8 00:52 abc_hl.dat</code>
</div>
</summary>
<blockquote>
1) 첫 번째 필드의 번호인 <strong>inode number가 164965로 완전히 동일</strong>하다.<br>
2) <code>-rw-r--r--</code> 바로 옆에 위치한 <strong>링크 카운트(link count)가 기본값 1이 아닌 2로 증가</strong>되어 있다.
</blockquote>
</details>

<details>
<summary>(작업형) <code>ls -l</code> 명령의 결과로 <code>lrwxrwxrwx 1 root root 11 2024-02-08 16:32 xyz_sl.dat -> /abc.dat</code> 가 표시되었다. 이 결과의 <code>ls</code> 출력 정보만 보았을 때 해당 파일이 심볼릭 링크 파일임을 알 수 있는 특징을 쓰시오.</summary>
<blockquote>
권한 표시 부분의 첫 번째 문자가 디렉터리(<code>d</code>)나 일반 파일(<code>-</code>)이 아닌 링크(Link)를 의미하는 리눅스 문자 <code>l</code>(소문자 엘)로 시작하며, 맨 뒷부분의 파일명 옆에 <code>-> /abc.dat</code> 식으로 원본 대상 경로가 화살표로 함께 표기되기 때문이다.
</blockquote>
</details>

###### ln (Create links)

<details>
<summary>파일에 대한 링크를 생성하는 명령어는?</summary>
<blockquote>
<code>ln</code>
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
<strong>하드링크 (<code>ln file.txt hardlink.txt</code>):</strong><br>
- 같은 inode를 공유, 원본과 동일한 파일<br>
- 원본 삭제되어도 하드링크는 여전히 유효<br>
- 같은 파일시스템 내에서만 생성 가능<br>
- 디렉터리에는 생성 불가<br><br>
<strong>심볼릭 링크 (<code>ln -s file.txt symlink.txt</code>):</strong><br>
- 원본 파일의 경로만 저장하는 별도 파일<br>
- 원본 삭제 시 심볼릭 링크는 깨짐 (dangling link)<br>
- 다른 파일시스템에도 생성 가능<br>
- 디렉터리에도 생성 가능<br><br>
원본 파일 삭제 시 하드링크는 여전히 데이터에 접근 가능하지만, 심볼릭 링크는 접근 불가능하다.
</blockquote>
</details>

##### 디렉터리 관리

<details>
<summary>(단답형) 파일 시스템 내에서 디스크, 프린터, 터미널과 같은 주변 장치를 사용하기 위해 제공되며 블록 단위 혹은 문자 단위로 입출력하는 파일 객체를 무엇이라 하는가?</summary>
<blockquote>
장치 파일 (Device file) 또는 특수 파일 (Special file)
</blockquote>
</details>

<details>
<summary>(단답형) <code>ls -l</code> 명령의 결과에서 맨 앞에 표시되는 첫 번째 기호가 <code>c</code>인 경우, 이는 어떤 종류의 파일을 의미하는가?</summary>
<blockquote>
문자 장치 파일 (Character device file)
</blockquote>
</details>

<details>
<summary>(단답형) <code>ls -l</code> 명령어를 실행했을 때, 접근 권한 정보 바로 우측 위치에 숫자로 표시되며, 동일한 inode를 참조하는 파일의 총개수를 나타내는 필드의 명칭을 무엇이라 하는가?</summary>
<blockquote>
하드 링크 개수 (또는 링크 카운트, Link count)
</blockquote>
</details>

<details>
<summary>(서술형) 리눅스의 입출력 객체 중 일반 파일이 아닌 '디렉터리(Directory)' 파일의 내부 구조적 특징과 역할에 대해 서술하시오.</summary>
<blockquote>
디렉터리 파일은 디렉터리 내에 포함된 파일들의 <strong>'파일명'</strong>과 해당 파일의 고유 식별자인 <strong>'inode number'</strong> 정보만을 매핑하여 목록 형태로 가지고 있는 특별한 파일이다.
</blockquote>
</details>

<details>
<summary>(서술형) 일반 사용자가 <code>ls -l</code> 명령어를 통해 파일의 소유자, 권한, 수정 일시 등의 상세 상태 정보를 출력할 수 있는 원리를 디렉터리와 inode 관점에서 설명하시오.</summary>
<blockquote>
디렉터리는 내부적으로 파일명과 해당 파일의 inode number 정보만 가질 뿐이다. 하지만 <code>ls</code> 명령어에 <code>-l</code> 옵션을 주어 실행할 경우, 파일 시스템은 <strong>매핑된 inode number를 통해 실제 속성 정보가 담긴 inode 구조체를 참조</strong>함으로써 권한, 시간, 크기 등의 상세 데이터를 화면에 출력할 수 있게 된다.
</blockquote>
</details>

<details>
<summary>(서술형) 리눅스 환경에서 설정되는 접근 권한인 읽기(r), 쓰기(w), 실행(x)이 '디렉터리' 객체에 부여되었을 때, 각각 어떤 구체적인 행위를 사용자에게 허용하게 되는지 설명하시오.</summary>
<blockquote>
- <strong>읽기(r)</strong>: 디렉터리에 있는 파일 목록을 읽고 확인할 수 있도록 허용한다.<br>
- <strong>쓰기(w)</strong>: 디렉터리 내부에 새로운 파일이나 디렉터리를 생성하고, 기존의 것을 삭제할 수 있도록 허용한다.<br>
- <strong>실행(x)</strong>: <code>cd</code> 명령 등으로 해당 디렉터리 안으로 진입(이동)할 수 있도록 허용한다.
</blockquote>
</details>

<details>
<summary>(작업형) 특정 작업 디렉터리 내부 전체를 깊이 탐색하여 하위 디렉터리에 존재하는 모든 파일들의 내용까지 화면에 출력하고자 할 때 필요한 <code>ls</code> 명령어의 옵션을 적으시오.</summary>
<blockquote>
<code>ls -R</code>
</blockquote>
</details>

<details>
<summary>(작업형) 셸 터미널에서 파일과 디렉터리를 눈으로 쉽게 구분하기 위해 파일명 맨 끝에 종류를 기호로 표시(디렉터리이면 <code>/</code>, 실행파일이면 <code>*</code>, 심볼릭 링크면 <code>@</code> 등)하도록 하는 <code>ls</code> 명령어의 추가 대문자 옵션을 쓰시오.</summary>
<blockquote>
<code>ls -F</code>
</blockquote>
</details>

<details>
<summary>(작업형) <code>ls -l</code> 명령어 실행 결과 권한 표기 부분이 <code>drwxr-xr-x</code> 로 출력되었다고 가정한다. 해당 권한을 8진수 숫자로 변환한 형태를 적고, 소유 그룹과 기타 사용자에게는 어떠한 권한이 부족한 상태인지 설명하시오.</summary>
<blockquote>
- <strong>8진수 변환값</strong>: <code>755</code><br>
- <strong>설명</strong>: 첫 글자 문자 <code>d</code>는 디렉터리임을 의미하고, 뒤따르는 <code>rwxr-xr-x</code>를 해석하면 소유자는 <code>rwx(7)</code> 권한을 가지나, 소유 그룹 및 기타 사용자는 <code>r-x(5)</code> 권한만 가진다. 따라서 해당 그룹과 사용자들은 디렉터리 내에 파일을 임의로 <strong>생성 또는 삭제할 수 있는 '쓰기(w)' 권한이 제한(제외)</strong>된 상태이다.
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
- <code>'rwsr-xr-x'</code>: 파일 권한 (소유자:<code>rwx</code>, 그룹:<code>r-x</code>, 기타:<code>r-x</code>, 's'는 SetUID 설정)<br>
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
<summary>(단답형) 최상위 루트 디렉터리(/)를 기준으로 목적지까지 거쳐가는 경로를 모두 표시하는 방식을 무엇이라 하는가?</summary>
<blockquote>
절대 경로명 (Absolute pathname)
</blockquote>
</details>

<details>
<summary>(서술형) 파일 시스템 내에서 경로를 지정하는 두 가지 방식인 '절대 경로'와 '상대 경로'의 기준점이 각각 무엇인지 비교하여 서술하시오.</summary>
<blockquote>
- <strong>절대 경로명</strong>: 최상위 루트 디렉터리(<code>/</code>)를 기준으로 경로를 표시한다.<br>
- <strong>상대 경로명</strong>: 현재 작업 중인 디렉터리(<code>.</code>)를 기준으로 경로를 표시한다.
</blockquote>
</details>

<details>
<summary>(작업형) 현재 사용자의 홈 디렉터리 하위에 있는 <code>work/project</code> 디렉터리로 한 번에 이동하기 위한 <code>cd</code> 명령어를 기호(<code>~</code>)를 사용하여 작성하시오.</summary>
<blockquote>
<code>cd ~/work/project</code>
</blockquote>
</details>

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

###### mkdir (Make Directory)

<details>
<summary>(단답형) 운영체제에서 디렉터리를 새로 생성하고자 할 때 사용하는 명령어는 무엇인가?</summary>
<blockquote>
mkdir (Make Directory)
</blockquote>
</details>

<details>
<summary>(서술형) 새로운 디렉터리를 생성할 때 <code>mkdir -p</code> 옵션을 사용해야 하는 구체적인 상황과 해당 옵션의 역할에 대해 설명하시오.</summary>
<blockquote>
<strong>상황</strong>: 존재하지 않는 여러 상위 계층을 포함하는 하위 디렉터리(예: <code>AA/BB/CC</code>)를 한 번에 동시에 생성해야 할 때 사용한다.<br>
<strong>역할</strong>: 계층 구조상 누락된 중간 디렉터리들을 에러 없이 알아서 모두 생성해 준다. 만약 <code>-p</code> 옵션을 사용하지 않으면 중간 경로가 없을 때 생성에 실패한다.
</blockquote>
</details>

<details>
<summary>(작업형) 현재 디렉터리 하위에 <code>work</code> 라는 이름의 디렉터리를 새롭게 생성하는 기본 명령어를 작성하시오.</summary>
<blockquote>
<code>mkdir work</code>
</blockquote>
</details>

<details>
<summary><code>mkdir</code> 명령어를 사용하여 <code>/home/user/project/2024/final</code> 경로의 디렉터리를 상위 디렉터리가 존재하지 않더라도 한 번에 생성하는 명령을 쓰시오.</summary>
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
<summary>(단답형) 기존에 생성되어 있는 디렉터리를 삭제할 때 사용하는 명령어로, 삭제하려는 대상이 반드시 비어 있을 때만 동작하는 명령어는 무엇인가?</summary>
<blockquote>
rmdir (Remove Directory)
</blockquote>
</details>

<details>
<summary>(서술형) <code>rmdir</code> 명령어로 기존 디렉터리를 삭제하려고 할 때, 명령이 정상적으로 성공하기 위해 사전에 반드시 충족되어야 하는 내부 조건은 무엇인지 서술하시오.</summary>
<blockquote>
삭제 대상이 되는 디렉터리 구역 내부에 어떠한 일반 파일이나 하위 디렉터리도 남아있지 않고 <strong>완벽히 비어있어야만</strong> 성공적으로 삭제할 수 있다.
</blockquote>
</details>

<details>
<summary>(작업형) 현재 디렉터리 하위에 비어 있는 <code>AA/BB/CC</code> 라는 형태의 빈 디렉터리 계층 구조를 한 번의 명령어로 모두 삭제하고자 한다. 이를 위해 필요한 <code>rmdir</code> 명령어와 옵션을 작성하시오.</summary>
<blockquote>
<code>rmdir -p AA/BB/CC</code>
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

##### 텍스트 처리

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

##### 텍스트 검색

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

##### 파일 관리

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

##### 파일 내용 조회

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

##### 파일 분할 및 비교

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

##### 파일 권한 관리

###### chmod (Change file permissions)

<details>
<summary>(단답형) 파일이나 디렉터리에 대한 접근 권한을 변경할 때 사용하는 'Change Mode'의 약자인 기본 명령어는 무엇인가?</summary>
<blockquote>
chmod
</blockquote>
</details>

<details>
<summary>(단답형) <code>chmod</code> 명령어에서 기호(Symbolic)를 이용해 권한을 변경할 때, 기존 권한 상태와 관계없이 지정한 권한만으로 완전히 새롭게 할당(설정)하고자 할 때 사용하는 연산자 기호는 무엇인가?</summary>
<blockquote>
<code>=</code> (설정 연산자)
</blockquote>
</details>

<details>
<summary>(단답형) 특정 파일에 대해 <code>chmod</code> 명령을 실행하여 접근 권한을 직접 수정할 수 있는 권한을 가진 주체는, 최고 관리자인 슈퍼 유저(root) 외에 누구뿐인가?</summary>
<blockquote>
해당 파일의 소유자 (User)
</blockquote>
</details>

<details>
<summary>(서술형) <code>chmod</code> 명령의 기호(Symbolic) 모드를 사용할 때 권한을 적용할 대상을 가리키는 식별자 <code>u, g, o, a</code>가 각각 구체적으로 누구를 의미하는지 서술하시오.</summary>
<blockquote>
- <strong>u (user)</strong>: 파일의 소유자<br>
- <strong>g (group)</strong>: 파일의 소유 그룹<br>
- <strong>o (others)</strong>: 소유자나 그룹에 속하지 않은 기타 모든 사용자<br>
- <strong>a (all)</strong>: 위의 세 항목을 모두 포함하는 모든 사용자 (대상을 지정하지 않았을 때의 기본값)
</blockquote>
</details>

<details>
<summary>(서술형) 디렉터리 내부에 포함된 수많은 하위 디렉터리 및 파일의 접근 권한을 한 번의 <code>chmod</code> 명령으로 일괄 변경하고자 한다. 이때 함께 사용해야 하는 통용 옵션 기호와 그 구체적인 역할을 서술하시오.</summary>
<blockquote>
- <strong>옵션</strong>: <code>-R</code><br>
- <strong>역할</strong>: 대상 디렉터리에 포함된 모든 하위 계층별 디렉터리와 내부 파일들의 권한까지 재귀적(Recursive)으로 한꺼번에 일괄 변경한다.
</blockquote>
</details>

<details>
<summary>(서술형) <code>chmod</code> 명령에 파일 권한을 8진수(숫자) 모드로 지정하는 방식을 사용할 때, 기호 문자 <code>r(읽기)</code>, <code>w(쓰기)</code>, <code>x(실행)</code>에 대응하는 각각의 숫자를 적고, 파일 권한이 <code>-rwxr-xr-x</code>로 표시된다면 이를 세 자리 8진수로 어떻게 표현하는지 설명하시오.</summary>
<blockquote>
- <strong>대응 숫자</strong>: <code>r (읽기) = 4</code>, <code>w (쓰기) = 2</code>, <code>x (실행) = 1</code><br>
- <strong>8진수 표현법</strong>: <code>rwxr-xr-x</code>는 <code>(4+2+1) (4+1) (4+1)</code> 로 나열되므로, 결과적으로 8진수 <code>755</code> 로 표현된다.
</blockquote>
</details>

<details>
<summary>(작업형) 현재 디렉터리 내의 <code>service.conf</code> 파일에 대해 기타 사용자(Others)에게 실수로 부여되어 있는 쓰기(w) 권한만을 단독으로 제거하는 <code>chmod</code> 명령어를 기호 모드(Symbolic)를 사용해 작성하시오.</summary>
<blockquote>
<code>chmod o-w service.conf</code>
</blockquote>
</details>

<details>
<summary>(작업형) 현재 <code>a.sh</code> 라는 스크립트 파일이 생성만 된 상태라 기본적으로 실행 권한이 없다. 이 파일에 대해 특정한 대상 제한 없이 모든 사용자(all)가 실행(x)할 수 있는 권한을 추가로 부여하는 <code>chmod</code> 명령어를 기호 모드 연산자를 사용하여 작성하시오.</summary>
<blockquote>
<code>chmod a+x a.sh</code> (또는 대상을 생략한 <code>chmod +x a.sh</code>)
</blockquote>
</details>

<details>
<summary>(작업형) 보안 강화를 위해 <code>a.sh</code> 파일의 접근 권한을 다음과 같이 8진수 방식을 통해 변경하려고 한다. 소유자(User)에게는 읽고 쓰는 권한만을 주고, 소유 그룹(Group) 및 기타 일반 사용자(Others)에게는 오로지 읽기 권한만을 허용하도록 설정하는 최적의 <code>chmod</code> 단일 명령어를 작성하시오.</summary>
<blockquote>
<code>chmod 644 a.sh</code>
</blockquote>
</details>

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
<summary>(단답형) 'Change Owner'의 약자로, 파일이나 디렉터리의 소유자(Owner)를 변경할 때 사용하는 명령어의 명칭을 쓰시오.</summary>
<blockquote>
<code>chown</code>
</blockquote>
</details>

<details>
<summary>(단답형) <code>chown</code> 명령어 실행 시, 지정한 대상이 심볼릭 링크 파일인 경우 링크가 가리키는 원본이 아닌 '링크 파일 자체'의 소유권을 변경하기 위해 사용하는 옵션 기호를 쓰시오.</summary>
<blockquote>
<code>-h</code>
</blockquote>
</details>

<details>
<summary>웹 서버 디렉터리 /var/www/html의 모든 파일과 하위 디렉터리의 소유자를 www-data로, 그룹도 www-data로 변경하는 명령을 쓰시오.</summary>
<blockquote>
<code>chown -R www-data:www-data /var/www/html</code><br><br>
<code>-R</code> 옵션은 재귀적으로 하위 디렉터리까지 포함하여 소유권을 변경한다. <code>user:group</code> 형태로 소유자와 그룹을 동시에 지정할 수 있다.
</blockquote>
</details>

<details>
<summary>(서술형) <code>chown</code> 명령어를 사용하여 특정 디렉터리의 소유자를 변경할 때, 해당 디렉터리 내부에 포함된 모든 하위 파일과 디렉터리까지 한꺼번에 소유권을 적용하기 위해 사용하는 옵션의 명칭과 동작 원리를 서술하시오.</summary>
<blockquote>
- <strong>옵션 명칭</strong>: R(Recursive)-재귀적 변경<br>
- <strong>동작 원리</strong>: 지정한 디렉터리뿐만 아니라 그 하위에 존재하는 모든 파일과 서브 디렉터리들을 시스템이 끝까지 탐색하며 소유권을 일괄적으로 변경한다.
</blockquote>
</details>

<details>
<summary>(서술형) 일반 사용자 계정(예: algisa)으로 로그인한 상태에서 <code>chown root file.txt</code> 명령을 실행했을 때 'Operation not permitted' 에러가 발생하는 이유를 보안 정책 관점에서 설명하시오.</summary>
<blockquote>
리눅스 보안 정책상 파일의 소유권 변경은 시스템 전체의 보안 및 접근 통제에 중대한 영향을 미치므로, 오직 <strong>슈퍼 유저(root, UID 0) 권한을 가진 사용자만이 실행</strong>할 수 있도록 제한되어 있기 때문이다. 일반 사용자가 자신의 파일 소유권을 임의로 타인(특히 root)에게 넘기는 행위는 시스템 관리 원칙에 어긋나므로 허용되지 않는다.
</blockquote>
</details>

<details>
<summary>(서술형) <code>chown</code> 명령어를 사용하여 파일의 '소유자'와 '소유 그룹'을 동시에 변경하고 싶을 때 사용하는 명령문 형식을 예시와 함께 서술하시오.</summary>
<blockquote>
- <strong>형식</strong>: <code>chown 소유자명:그룹명 파일명</code><br>
- <strong>예시</strong>: <code>chown algisa:dev b.sh</code><br>
- <strong>설명</strong>: 콜론(<code>:</code>) 또는 점(<code>.</code>)을 구분자로 사용하여 소유자와 그룹을 한 번의 명령으로 모두 지정할 수 있다.
</blockquote>
</details>

<details>
<summary>(작업형) 현재 디렉터리에 있는 <code>service.conf</code> 파일의 소유자를 <code>root</code>로, 소유 그룹을 <code>dev</code>로 변경하려 한다. 이를 위해 슈퍼 유저 권한으로 실행해야 하는 단일 <code>chown</code> 명령어를 작성하시오.</summary>
<blockquote>
<code>chown root:dev service.conf</code>
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

<details>
<summary>(단답형) 리눅스 시스템에서 <code>chown</code>이나 <code>chgrp</code> 명령을 사용하여 파일의 소유권이나 그룹을 강제로 변경할 수 있는 권한을 가진 유일한 사용자 계정의 명칭을 쓰시오.</summary>
<blockquote>
root (또는 슈퍼 유저)
</blockquote>
</details>

<details>
<summary>(작업형) 다음 터미널 명령어 실행 과정에서 빈칸 (A)와 (B)에 들어갈 알맞은 명령어를 작성하시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<code>[algisa@Fedora11]$ ls -l b.sh</code><br>
<code>-rw-r--r-- 1 algisa dev 0 2024-02-08 22:13 b.sh</code><br>
<code>[algisa@Fedora11]$ ( A )</code><br>
<code>Password: (비밀번호 입력)</code><br>
<code>[root@Fedora11]# ( B ) root b.sh</code><br>
<code>[root@Fedora11]# ls -l b.sh</code><br>
<code>-rw-r--r-- 1 root dev 0 2024-02-08 22:13 b.sh</code>
</div>
<strong>조건</strong>: (A)는 일반 사용자에서 root로 전환하기 위한 명령이며, (B)는 b.sh 파일의 소유 그룹은 유지한 채 <strong>소유자만</strong> root로 변경하는 명령이다.
</summary>
<blockquote>
(A) <code>su</code> (또는 <code>su -</code>)<br>
(B) <code>chown</code>
</blockquote>
</details>

<details>
<summary>(작업형) 특정 디렉터리 <code>/web_root</code>와 그 하위의 모든 파일들에 대하여 소유 그룹을 <code>www-data</code>로 변경하고자 한다. 재귀적 옵션을 사용하여 <code>chgrp</code> 명령어로 작성하시오.</summary>
<blockquote>
<code>chgrp -R www-data /web_root</code>
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

 <details>
 <summary>(단답형) 파일이나 디렉터리 생성 시 부여될 기본 접근 권한에서 '제거(마스킹)'할 권한을 지정하거나, 현재 설정된 마스크 값을 확인하기 위해 사용하는 명령어의 명칭을 쓰시오.</summary>
 <blockquote>
 <code>umask</code>
 </blockquote>
 </details>

 <details>
 <summary>(단답형) 리눅스 시스템에서 관리자가 <code>umask</code> 값을 설정하여 모든 로그인 사용자에게 공통적으로 적용하고자 할 때 주로 사용되는 시스템 전역 환경 설정 파일의 절대 경로를 쓰시오.</summary>
 <blockquote>
 <code>/etc/profile</code>
 </blockquote>
 </details>

 <details>
 <summary>(단답형) 현재 시스템의 umask 값을 확인하기 위해 인자 없이 <code>umask</code> 명령을 실행했을 때 출력되는 값의 기본 진수를 쓰시오.</summary>
 <blockquote>
 8진수
 </blockquote>
 </details>

 <details>
 <summary>(서술형) 리눅스에서 <code>umask</code> 연산이 권한을 결정할 때 단순한 '산술적 빼기'가 아니라고 말하는 이유를, 특정 비트(예: 실행 권한)의 제거 관점에서 설명하시오.</summary>
 <blockquote>
 <code>umask</code>는 산술적인 뺄셈이 아니라 <strong>비트 마스킹(Bit Masking)</strong> 방식이기 때문이다. '제거(mask)'할 권한이 설정된 비트는 파일 시스템의 기본 권한 비트가 무엇이든 강제로 0으로 만든다. 예를 들어, 기본 권한에 없는 비트를 umask로 제거하더라도 결과가 음수가 되거나 오류가 나지 않고 단지 해당 위치의 비트가 제거된 상태로 유지될 뿐이다.
 </blockquote>
 </details>

 <details>
 <summary>(서술형) 시스템 보안 권고 사항에 따라 <code>umask</code> 값을 <code>022</code>로 설정하였을 때, 새롭게 생성되는 파일이나 디렉터리에 대해 소유 그룹(Group)과 기타 사용자(Others)에게 어떠한 접근이 구체적으로 제한되는지 서술하시오.</summary>
 <blockquote>
 <code>022</code>는 소유 그룹과 기타 사용자의 <strong>쓰기(w, 2) 권한을 제거</strong>한다는 의미이다. 따라서 새롭게 생성된 파일은 소유자만 수정할 수 있고, 디렉터리는 소유자만 내부 파일을 생성하거나 삭제할 수 있도록 제한되어 시스템 자원에 대한 임의 변경을 차단한다.
 </blockquote>
 </details>

 <details>
 <summary>(서술형) <code>umask 027</code>이 설정된 환경에서 생성되는 파일과 디렉터리의 권한 차이를 소유 그룹(Group)과 기타 사용자(Others) 관점에서 설명하시오.</summary>
 <blockquote>
 <code>umask 027</code>은 그룹의 쓰기(2) 권한을 제거하고, 기타 사용자의 모든 권한(rwx, 7)을 제거한다는 의미이다. 이 경우 소유 그룹은 읽기와 실행은 가능하지만 수정은 불가능하며, <strong>기타 사용자(Others)는 해당 파일이나 디렉터리에 대해 어떠한 접근(읽기, 쓰기, 실행)도 할 수 없는</strong> 강력한 보안 상태가 된다.
 </blockquote>
 </details>

 <details>
 <summary>(작업형) 사용자가 <code>umask 333</code>을 설정한 후 <code>touch afile</code> 명령으로 일반 파일을 생성하였다. 이때 생성된 파일의 8진수 접근 권한값과 <code>ls -l</code> 출력 시의 기호 형태를 쓰시오. (단, 파일 기본 권한은 666 기준)</summary>
 <blockquote>
 - <strong>8진수 권한</strong>: <code>444</code><br>
 - <strong>기호 형태</strong>: <code>-r--r--r--</code><br>
 - <strong>풀이</strong>: 기본 666(110 110 110)에서 umask 333(011 011 011)에 해당하는 '쓰기(2)'와 '실행(1)' 비트를 제거하면 444(100 100 100)가 된다.
 </blockquote>
 </details>

 <details>
 <summary>(작업형) 현재 umask가 <code>022</code>인 상태에서 <code>mkdir dir022</code>와 <code>touch file022</code> 명령을 실행하여 각각 디렉터리와 파일을 생성했다. <code>ls -ld</code> 명령어로 확인되는 두 객체의 최종 8진수 접근 권한을 각각 계산하여 쓰시오.</summary>
 <blockquote>
 - <strong>디렉터리(dir022)</strong>: <code>755</code> (777 - 022)<br>
 - <strong>일반 파일(file022)</strong>: <code>644</code> (666 - 022)
 </blockquote>
 </details>

 <details>
 <summary>(작업형) 보안 강화를 위해 새로 생성되는 파일에 대해 소유 그룹은 어떠한 권한도 갖지 못하게 하고(---), 기타 사용자는 오직 읽기 권한(r--)만 갖도록 설정하고자 한다. 이때 필요한 <code>umask</code> 값을 계산하여 쓰고, 설정을 위한 명령어를 작성하시오. (단, 파일 기본 권한은 666 기준)</summary>
 <blockquote>
 - <strong>필요한 umask 값</strong>: <code>062</code> (또는 x까지 고려한 <code>072</code>)<br>
 - <strong>설정 명령어</strong>: <code>umask 062</code> (또는 <code>umask 072</code>)<br>
 - <strong>풀이</strong>: 그룹의 모든 권한(6)을 제거하고 기타 사용자의 쓰기(2) 권한을 제거하면 666에서 604(rw-------r--) 권한이 남게 된다.
 </blockquote>
 </details>

##### 파일 검색

###### find (Find files and directories)

<details>
<summary>시스템에서 SetUID 권한이 설정된 모든 파일을 찾아 보안 점검을 수행하는 명령을 쓰시오.</summary>
<blockquote>
<code>find / -type f -perm -4000 2>/dev/null</code><br><br>
<code>find</code> 명령어는 파일 검색에 사용되며, <code>-perm -4000</code> 옵션으로 SetUID 파일을 찾을 수 있다. <code>2>/dev/null</code>로 에러 메시지를 숨긴다.
</blockquote>
</details>

<details>
<summary>(단답형) <code>find</code> 명령어의 <code>-type</code> 옵션을 사용하여 파일 종류별 검색을 수행할 때, 일반 파일(f), 디렉터리(d) 외에 '심볼릭 링크(Symbolic Link)' 파일만을 특정하여 검색하기 위해 지정해야 하는 문자를 쓰시오.</summary>
<blockquote>
<code>l</code> (소문자 L)
</blockquote>
</details>

<details>
<summary>(단답형) <code>find</code> 명령어로 파일 크기를 조건으로 검색할 때, <code>10MB</code>를 초과하는 크기를 가진 파일들만을 찾고자 한다. 이때 <code>-size</code> 옵션 뒤에 입력해야 하는 정확한 인자 형식을 쓰시오.</summary>
<blockquote>
<code>+10M</code>
</blockquote>
</details>

<details>
<summary>(단답형) <code>find</code> 명령어의 <code>-exec</code> 옵션과 함께 사용되어, 각 검색 결과 파일에 대해 명령 실행을 마무리함을 의미하는 종료 문자를 쓰시오. (단, 백슬래시를 포함한 형태로 작성)</summary>
<blockquote>
<code>\;</code> (또는 <code>\+</code>)
</blockquote>
</details>

<details>
<summary>(단답형) <code>find</code> 명령어의 <code>-exec</code> 옵션을 사용하여 검색된 파일들에 대해 추가 명령을 실행할 때, 검색된 각 파일의 경로(파일명)가 인수로 전달되는 위치를 나타내는 특수 기호 쌍을 쓰시오.</summary>
<blockquote>
<code>{}</code>
</blockquote>
</details>

<details>
<summary>(서술형) <code>find</code> 명령어에서 여러 검색 조건을 조합하기 위해 사용하는 논리 연산 기호인 <code>-a</code>, <code>-o</code>, <code>!</code> 의 의미를 각각 설명하고, 만약 조건 사이에 어떠한 연산 기호도 명시하지 않았을 때 기본적으로 적용되는 논리 연산은 무엇인지 서술하시오.</summary>
<blockquote>
- <strong>-a (또는 -and)</strong>: 두 조건이 모두 참(True)일 때만 결과를 반환한다.<br>
- <strong>-o (또는 -or)</strong>: 두 조건 중 하나라도 참이면 결과를 반환한다.<br>
- <strong>! (또는 -not)</strong>: 뒤따르는 조건의 참/거짓을 반전(부정)한다.<br>
- <strong>기본 연산</strong>: 조건을 나열하고 연산자를 생략하면 기본적으로 <strong>AND(-a)</strong> 연산이 수행된다.
</blockquote>
</details>

<details>
<summary>(서술형) 보안 점검 중 소유자가 존재하지 않는 파일(<code>-nouser</code>)이나 소유 그룹이 존재하지 않는 파일(<code>-nogroup</code>)이 발견되는 이유와, 이러한 상태가 시스템에 미치는 보안 위협 및 관리자가 취해야 할 조치 방법을 서술하시오.</summary>
<blockquote>
- <strong>발생 사유</strong>: 파일의 원래 소유자 계정이나 그룹이 삭제(퇴사 등)되어 시스템에 더 이상 해당 이름이 존재하지 않을 때 발생한다.<br>
- <strong>보안 위협</strong>: 삭제된 UID/GID를 악의적으로 재사용하는 계정이 생성될 경우, 해당 파일에 대한 소유자 권한을 획득하게 되는 권한 상승 위협이 있다.<br>
- <strong>조치 방법</strong>: 불필요한 파일인 경우 <code>rm</code> 명령으로 삭제하고, 필요한 파일인 경우 <code>chown</code> 혹은 <code>chgrp</code> 명령을 사용하여 현재 존재하는 유효한 사용자/그룹으로 소유권을 재지정해야 한다.
</blockquote>
</details>

<details>
<summary>(서술형) <code>find</code> 명령어에서 <code>-perm 644</code>와 <code>-perm -644</code>를 사용하여 파일을 검색할 때, 두 결과값의 차이를 파일 권한 비트의 포함 여부 관점에서 비교하여 서술하시오.</summary>
<blockquote>
- <strong>-perm 644</strong>: 파일의 권한 모드가 정확히 <code>644(rw-r--r--)</code>와 일치하는 파일만 검색한다.<br>
- <strong>-perm -644</strong>: 명시된 <code>644</code> 권한 비트를 모두 포함(Set)하고 있는 파일을 검색한다. 즉, 소유자의 읽기/쓰기 권한과 그룹/기타 사용자의 읽기 권한을 최소한으로 가진 파일을 모두 찾으므로 <code>644</code>, <code>664</code>, <code>755</code>, <code>777</code> 등이 모두 검색 결과에 포함될 수 있다.
</blockquote>
</details>

<details>
<summary>(작업형) 현재 디렉터리(<code>.</code>) 이하의 모든 정규 파일(<code>-type f</code>) 중에서, 소유자가 <code>root</code>이거나(OR) 소유 그룹이 <code>dev</code>인 파일을 검색하여 화면에 출력하고자 한다. 연산 우선순위를 위해 소괄호 기호를 적절히 사용하여 단일 명령어를 작성하시오.</summary>
<blockquote>
<code>find . -type f \( -user root -o -group dev \) -print</code>
</blockquote>
</details>

<details>
<summary>(작업형) 시스템 침해 사고 발생 시 무결성 검증을 위해, 최상위 루트(<code>/</code>) 디렉터리부터 시작하여 최근 10일 이내에 수정 또는 생성된(<code>-mtime</code>) 모든 정규 파일들을 검색하고 그 목록을 <code>/tmp/recent_scan.out</code> 파일에 저장하는 명령어를 작성하시오.</summary>
<blockquote>
<code>find / -type f -mtime -10 > /tmp/recent_scan.out</code>
</blockquote>
</details>

<details>
<summary>(작업형) 보안 가이드라인 상 보안 위협이 되는 'World Writable' 파일(기타 사용자에게 쓰기 권한이 부여된 파일)을 <code>/etc</code> 디렉터리 하위에서 검색하여, 발견된 각 파일의 상세 정보(<code>ls -al</code>)를 화면에 출력하는 명령어를 작성하시오.</summary>
<blockquote>
<code>find /etc -type f -perm -2 -exec ls -al {} \;</code> (또는 <code>find /etc -type f -perm -o+w -exec ls -al {} \;</code>)
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

#### 프로세스 응용

##### 프로세스 개요

<details>
<summary>(단답형) 프로세스가 실행될 때 할당되는 메모리 구조 중, 함수의 로컬 변수, 매개변수, 리턴 값 등이 일시적으로 저장되며 스택 포인터가 가리키는 영역의 명칭을 쓰시오.</summary>
<blockquote>
Stack 영역 (스택 영역)
</blockquote>
</details>

<details>
<summary>(단답형) 프로세스가 생성되면 운영체제(커널)가 프로세스별로 생성하는 관리 정보 자료구조로, PID, PC(Program Counter), 프로세스 상태 등을 저장하고 있는 블록의 명칭(약어)을 쓰시오.</summary>
<blockquote>
PCB (Process Control Block, 프로세스 제어 블록)
</blockquote>
</details>

<details>
<summary>(단답형) 유닉스/리눅스 시스템에서 프로세스가 처음 생성될 때 기본적으로 할당되는 3가지 표준 스트림인 표준 입력(STDIN), 표준 출력(STDOUT), 표준 에러(STDERR)에 각각 대응되는 파일 디스크립터(FD) 번호를 순서대로 쓰시오.</summary>
<blockquote>
0, 1, 2
</blockquote>
</details>

<details>
<summary>(서술형) 리눅스 시스템에서 발생하는 '고아 프로세스(Orphan Process)'와 '좀비 프로세스(Zombie Process)'의 개념적 차이와 발생 원인을 서술하시오.</summary>
<blockquote>
- <strong>고아 프로세스</strong>: 자식 프로세스가 실행 중인 상태에서 부모 프로세스가 먼저 종료된 경우를 말하며, 이 경우 PID 1번인 init(또는 systemd) 프로세스가 새로운 부모가 되어 수용한다.<br>
- <strong>좀비 프로세스</strong>: 자식 프로세스가 모든 실행을 마쳤지만, 부모 프로세스가 자식의 종료 상태 정보(Exit Status)를 회수하지 않아 시스템 커널의 프로세스 테이블에 관리 정보가 남아 있는 상태를 말한다.
</blockquote>
</details>

<details>
<summary>(서술형) CPU가 현재 실행 중인 프로세스에서 다른 프로세스로 제어권을 넘길 때 발생하는 '문맥 교환(Context Switching)'의 정의를 쓰고, 이 과정에서 PCB(Process Control Block)가 수행하는 핵심 역할을 설명하시오.</summary>
<blockquote>
- <strong>정의</strong>: CPU에서 실행 중인 프로세스가 교체될 때, 현재 프로세스의 상태(PC, 레지스트리 정보 등)를 저장하고 새로운 프로세스의 상태로 복원하는 과정을 말한다.<br>
- <strong>PCB의 역할</strong>: 문맥 교환 발생 시, 현재 실행 중인 프로세스의 레지스트리 상태 및 PC 값을 해당 프로세스의 PCB 내 'Register save area'에 저장하고, 다음에 실행할 프로세스의 PCB로부터 이전에 저장해둔 상태 정보를 CPU 레지스트리로 복원하여 실행을 재개할 수 있게 한다.
</blockquote>
</details>

<details>
<summary>(서술형) 커널이 시스템 내의 오픈된 파일을 관리하기 위해 사용하는 3단계 자료구조인 '파일 디스크립터 테이블(PDT/FDT)', '시스템 오픈 파일 테이블(System open-file table)', '액티브 vnode 테이블(Active vnode table)' 간의 관계와 각 테이블의 주요 역할을 서술하시오.</summary>
<blockquote>
1. <strong>파일 디스크립터 테이블</strong>: 개별 프로세스별로 관리되는 테이블로, 정수 값인 FD를 통해 시스템 오픈 파일 테이블의 항목을 가리킨다.<br>
2. <strong>시스템 오픈 파일 테이블</strong>: 시스템 전체에서 오픈된 모든 파일을 관리하며, 오픈 모드(Read/Write), 파일 오프셋(현재 위치), 그리고 해당 파일을 참조하는 횟수(Reference count) 등을 저장한다.<br>
3. <strong>액티브 vnode 테이블</strong>: 파일 시스템의 독립적인 매개체 역할을 하며, 해당 파일의 실제 데이터 위치 정보 등 inode 정보를 캐싱하고 관리한다.
</blockquote>
</details>

<details>
<summary>(단답형) 쉘에서 새 프로그램을 실행할 때, 현재 실행 중인 프로세스의 PID는 그대로 유지하면서 실행 코드와 데이터 이미지만 새로운 프로그램으로 교체(전이)하는 시스템 호출의 명칭을 쓰시오.</summary>
<blockquote>
exec (또는 execve)
</blockquote>
</details>

<details>
<summary>(서술형) 사용자가 쉘에서 <code>./a.out</code> 명령을 입력하여 프로그램을 실행했을 때, 커널 차원에서 <code>fork()</code>와 <code>exec()</code>가 호출되는 상세 과정과 그 과정에서 '터미널 제어권'이 어떻게 이동하는지 설명하시오.</summary>
<blockquote>
1. 쉘 프로세스가 <code>fork()</code>를 호출하여 자신의 복사본인 자식 프로세스를 생성한다.<br>
2. 터미널 제어권이 쉘에서 생성된 자식 프로세스로 넘어간다.<br>
3. 자식 프로세스 내에서 <code>exec()</code>를 호출하여 기존 쉘 이미지를 <code>a.out</code> 실행 이미지로 교체한다.<br>
4. <code>a.out</code> 프로그램이 종료되면 터미널 제어권이 다시 원래의 쉘 프로세스로 반환된다.
</blockquote>
</details>

##### 프로세스 정보 확인

<details>
<summary>(작업형) 다음의 <code>ps -l</code> 명령 실행 결과에서 좀비 프로세스를 식별하고, 해당 프로세스의 PID를 쓰시오. 또한, 이러한 좀비 프로세스가 시스템 가용성에 미치는 부정적 영향과 이를 제거하기 위한 근본적인 해결 방법을 기술하시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<strong>[ps -l 결과]</strong><br>
S UID PID PPID C PRI NI ADDR SZ WCHAN TTY TIME CMD<br>
S 501 1234 1200 0 80 0 - 1234 - pts/0 00:00:01 bash<br>
Z 501 5678 1234 0 80 0 - 0 - pts/0 00:00:00 &lt;defunct&gt;
</div>
</summary>
<blockquote>
- <strong>좀비 프로세스 PID</strong>: 5678 (상태 값이 'Z'이고 CMD 명칭이 '&lt;defunct&gt;'이므로 좀비임)<br>
- <strong>부정적 영향</strong>: 좀비 프로세스는 실제 실행 이미지는 없으나 커널 내 프로세스 테이블의 슬롯을 계속 차지한다. 프로세스 ID는 유한한 자원이므로 좀비 프로세스가 과도하게 늘어나면 새로운 프로세스 생성이 불가능해지는 시스템 장애가 발생할 수 있다.<br>
- <strong>해결 방법</strong>: 좀비 프로세스 자체는 이미 종료된 상태이므로 <code>kill</code> 명령으로 죽일 수 없다. 부모 프로세스(PID: 1234)를 종료시키면 좀비 프로세스들이 고아 프로세스가 되어 init 프로세스에 의해 수집 및 제거되거나, 시스템을 재기동하여 커널 정보를 초기화해야 한다.
</blockquote>
</details>

<details>
<summary>(작업형) 현재 시스템 전체 프로세스 중 좀비 프로세스만을 검색하여 그 상태와 명령어 이름을 확인하고자 할 때, <code>ps</code> 명령의 옵션과 <code>grep</code> 명령을 사용하여 이를 한 줄로 수행하는 명령어를 작성하시오. (단, 결과에 '&lt;defunct&gt;' 문자열이 포함된 행만 추출하도록 작성)</summary>
<blockquote>
<code>ps -ef | grep defunct</code> (또는 <code>ps -el | grep "Z"</code>)
</blockquote>
</details>

<details>
<summary>(작업형) <code>ps -l</code> 결과의 <code>PRI</code>(Priority) 필드와 <code>NI</code>(Nice) 필드의 관계를 설명하고, 특정 프로세스(PID: 4321)의 우선순위를 낮추기 위해(즉, NI 값을 높이기 위해) 사용하는 명령어를 작성하시오. (단, NI 값을 15로 설정한다고 가정)</summary>
<blockquote>
- <strong>관계</strong>: <code>PRI</code>는 시스템에 의해 결정되는 실제 우선순위 값이며, <code>NI</code>는 사용자가 프로세스의 우선순위에 가중치를 주기 위해 설정하는 값이다. 일반적으로 <code>PRI</code> 값은 시스템 기본 우선순위에 <code>NI</code> 값을 더하여 계산되므로, <code>NI</code> 값이 커질수록(Positive) 실제 우선순위는 낮아진다.<br>
- <strong>명령어</strong>: <code>renice 15 -p 4321</code>
</blockquote>
</details>

<details>
<summary>(단답형) <code>ps -el</code> 명령어 실행 결과의 <code>SZ</code> 필드에서 표시되는 프로세스의 메모리 점유 크기를 나타내는 기본 단위(Unit)를 쓰시오.</summary>
<blockquote>
Kbyte (킬로바이트)
</blockquote>
</details>

<details>
<summary>(서술형) <code>ps -el</code> 출력 결과에 나타나는 <code>WCHAN</code> 필드의 구체적인 의미를 기술하고, 이 필드의 값이 공백이 아닌 특정 함수명으로 채워져 있을 때 해당 프로세스의 상태(S 필드)는 어떠한 상황인지 연관 지어 서술하시오.</summary>
<blockquote>
- <strong>의미</strong>: 실행 중이지 않고 Sleep(대기) 상태에 있는 프로세스가 현재 기다리고 있는 커널(시스템) 함수명을 나타낸다.<br>
- <strong>상태 관계</strong>: <code>WCHAN</code>에 값이 존재한다는 것은 해당 프로세스가 특정 자원이나 이벤트를 기다리며 멈춰 있음을 뜻하므로, <code>S</code>(Status) 필드의 값은 대기 상태인 'S'(Interruptible Sleep) 또는 'D'(Uninterruptible Sleep) 중 하나일 가능성이 매우 높다.
</blockquote>
</details>

<details>
<summary>(작업형) 다음의 <code>ps -ef</code> 명령 실행 결과 중 <code>STIME</code>과 <code>TTY</code> 필드 값을 분석하여, 해당 프로세스의 '시작 시간대'와 '제어 터미널 연결 여부'를 각각 판단하여 기술하시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<code>root 10430 1 0 Jan31 ? 00:00:01 /sbin/init</code>
</div>
</summary>
<blockquote>
- <strong>시작 시간대</strong>: 'Jan31'로 표시된 것으로 보아, 현재 날짜 기준으로 당일이 아닌 과거(1월 31일)에 시작된 프로세스임을 알 수 있다. (당일 시작이면 '시:분:초' 형식으로 표시됨)<br>
- <strong>제어 터미널 연결 여부</strong>: <code>TTY</code> 필드 값이 '?'이므로, 해당 프로세스는 사용자의 제어 터미널(pts 등)에 연결되지 않고 백그라운드(데몬 등)에서 동작 중인 상태이다.
</blockquote>
</details>

<details>
<summary>(단답형) 프로세스 그룹을 식별하기 위한 고유 ID로, 일반적으로 해당 그룹의 리더 프로세스(쉘로부터 실행된 프로세스)의 PID 값이 할당되는 식별자의 약칭을 쓰시오.</summary>
<blockquote>
PGID (Process Group ID)
</blockquote>
</details>

<details>
<summary>(단답형) 프로그램을 실행할 때 터미널 제어권을 쉘이 계속 유지하게 하여, 사용자가 추가적인 명령을 바로 입력할 수 있도록 백그라운드 모드로 동작시키는 특수 기호를 쓰시오.</summary>
<blockquote>
&
</blockquote>
</details>

<details>
<summary>(서술형) 프로세스 그룹(Process Group)의 정의와, 커널이 프로세스들을 그룹 단위로 관리하여 얻는 주된 효과를 '터미널 제어권' 관점에서 서술하시오.</summary>
<blockquote>
- <strong>정의</strong>: 쉘에서 실행된 프로세스와 그로부터 파생된 자식 프로세스들의 집합이다.<br>
- <strong>효과</strong>: 커널은 터미널로부터 입력되는 데이터(입력값)와 발생하는 시그널(Ctrl+C 등)을 개별 프로세스가 아닌 '프로세스 그룹' 단위로 전달함으로써, 관련된 프로세스들을 한꺼번에 안전하게 제어하고 관리할 수 있다.
</blockquote>
</details>

<details>
<summary>(서술형) 세션(Session) 및 세션 ID(SID)의 개념을 설명하고, 일반적인 유닉스/리눅스 환경에서 SID가 결정되는 기준과 세션 내에 포함될 수 있는 요소들을 서술하시오.</summary>
<blockquote>
- <strong>개념</strong>: 세션은 사용자가 터미널과 연결되어 있는 논리적인 연결 상태를 의미한다.<br>
- <strong>결정 기준</strong>: 해당 세션의 리더 프로세스(일반적으로 사용자가 최초 로그인했을 때 나타나는 로그인 쉘)의 PID가 해당 세션의 SID로 설정된다.<br>
- <strong>포함 요소</strong>: 하나의 세션 내에는 하나의 포그라운드 프로세스 그룹과 하나 이상의 백그라운드 프로세스 그룹이 존재할 수 있다.
</blockquote>
</details>

<details>
<summary>(작업형) 다음 <code>ps</code> 출력 결과를 분석하여 질문에 답하시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
<strong>[ps -o pid,ppid,pgid,sid,cmd 결과]</strong><br>
PID PPID PGID SID CMD<br>
25443 25441 25443 25443 bash<br>
 4015 25443 4015 25443 parent.out<br>
 4016 4015 4015 25443 child.out
</div>
1. <code>parent.out</code>과 <code>child.out</code>이 동일한 프로세스 그룹에 속해 있음을 나타내는 PGID 값은 무엇인가?<br>
2. 위 상에서 '세션 리더'의 역할을 수행하고 있는 프로세스의 CMD 명칭과 그 근거를 기술하시오.</summary>
<blockquote>
1. 4015<br>
2. <strong>CMD</strong>: bash / <strong>근거</strong>: 모든 프로세스의 SID(25443)가 bash의 PID(25443)와 일치하기 때문에 bash가 해당 세션의 리더라고 판단할 수 있다.
</blockquote>
</details>

<details>
<summary>(작업형) 사용자가 <code>./parent.out &</code> 명령을 입력하여 백그라운드에서 프로그램을 실행했을 때와 <code>./parent.out</code>(포그라운드)으로 실행했을 때를 비교하여, '터미널 제어권'과 '쉘 사용 가능 여부' 측면에서의 차이점을 기술하시오.</summary>
<blockquote>
- <strong>백그라운드(&)</strong>: 터미널 제어권을 쉘(bash)이 그대로 가지고 있으므로 프로그램 실행 중에도 사용자가 쉘에 추가 명령을 입력할 수 있다.<br>
- <strong>포그라운드</strong>: 터미널 제어권이 해당 프로그램(프로세스 그룹)으로 넘어가므로, 프로그램이 종료되거나 중단되기 전까지는 사용자가 쉘을 통해 다른 명령을 실행할 수 없다.
</blockquote>
</details>

<details>
<summary>(작업형) PID가 25443인 bash 쉘에서 <code>parent.out</code>을 포그라운드로 실행하여 PID 4015를 할당받았다. 이후 <code>parent.out</code>이 자식 프로세스 <code>child.out</code>(PID 4016)을 생성했을 때, 자식 프로세스의 PPID와 PGID, SID 값을 예측하여 작성하시오.</summary>
<blockquote>
- <strong>PPID</strong>: 4015 (부모인 parent.out의 PID)<br>
- <strong>PGID</strong>: 4015 (그룹 리더인 parent.out의 PID가 그룹 내 모든 자식에게 상속됨)<br>
- <strong>SID</strong>: 25443 (해당 세션 리더인 bash의 PID가 상속됨)
</blockquote>
</details>

##### 프로세스 간 통신(시그널)

<details>
<summary>(단답형) 시그널 번호를 명시적으로 지정하지 않고 <code>kill</code> 명령을 실행했을 때, 대상 프로세스에 기본값(Default)으로 전달되는 시그널의 명칭과 번호를 쓰시오.</summary>
<blockquote>
SIGTERM (15)
</blockquote>
</details>

<details>
<summary>(단답형) 포그라운드에서 실행 중인 프로세스 그룹을 즉시 종료시키고자 할 때 사용하는 키보드 조합키 <code>Ctrl + C</code>와 <code>Ctrl + \</code>가 각각 발생시키는 시그널의 명칭을 순서대로 쓰시오.</summary>
<blockquote>
SIGINT, SIGQUIT
</blockquote>
</details>

<details>
<summary>(서술형) 유닉스/리눅스 시스템에서 시그널(Signal)이 발생하는 경로를 4가지 상황으로 구분하고, 각각에 해당하는 구체적인 예시 또는 시그널 명칭을 하나씩 기술하시오.</summary>
<blockquote>
1. <strong>에러 상황</strong>: 커널에 의해 발생 (예: 0으로 나누기 연산 시 <code>SIGFPE</code>, 메모리 참조 오류 시 <code>SIGSEGV</code>)<br>
2. <strong>외부 상황</strong>: 사용자의 키보드 입력 등에 의해 발생 (예: <code>Ctrl+C</code> 입력 시 <code>SIGINT</code>)<br>
3. <strong>이벤트 발생</strong>: 특정 시스템 함수나 상황에 의해 발생 (예: <code>alarm()</code> 타이머 만료 시 <code>SIGALRM</code>, 자식 종료 시 <code>SIGCHLD</code>)<br>
4. <strong>인위적 발생</strong>: 시스템 콜이나 명령어로 직접 발생 (예: <code>kill()</code> 함수 호출 또는 <code>kill</code> 명령어 실행)
</blockquote>
</details>

<details>
<summary>(서술형) <code>SIGKILL</code>(9번)과 <code>SIGSTOP</code>(19번) 시그널이 다른 일반적인 시그널들과 구별되는 결정적인 기술적 특징을 '시그널 핸들러'의 관점에서 서술하시오.</summary>
<blockquote>
일반적인 시그널은 프로세스가 무시하거나 별도의 시그널 핸들러 함수를 통해 임의로 처리 정책을 변경할 수 있다. 하지만 <code>SIGKILL</code>과 <code>SIGSTOP</code>은 시스템 관리 및 커널 제어 목적으로 사용되는 특수 시그널이므로, 수신하는 프로세스가 이를 무시하거나 핸들러를 통해 가로채서 처리할 수 없으며 무조건 즉시 종료되도록(또는 정지되도록) 강제된다.
</blockquote>
</details>

<details>
<summary>(작업형) 현재 시스템에 떠 있는 <code>nc -lvp 8081</code> 프로세스(PID: 4498)를 시그널 번호 9를 사용하여 즉시 강제 종료시키는 명령어를 두 가지 형식(번호 사용, 이름 사용)으로 각각 작성하시오.</summary>
<blockquote>
1. 번호 사용: <code>kill -9 4498</code><br>
2. 이름 사용: <code>kill -KILL 4498</code> (또는 <code>kill -SIGKILL 4498</code>)
</blockquote>
</details>

<details>
<summary>(작업형) 실행 중인 프로세스(PID: 4500)에 <code>SIGSTOP</code> 시그널을 전송했을 때 프로세스에 일어나는 변화를 <code>ps -el</code> 명령의 <code>S</code>(Status) 필드 값 변화와 연관 지어 설명하고, 정지된 이 프로세스를 다시 가동시키기 위해 사용해야 할 시그널 명칭을 제안하시오.</summary>
<blockquote>
- <strong>변화</strong>: 프로세스가 즉시 실행을 멈추고 정지 상태가 되며, <code>ps -el</code> 명령으로 확인 시 <code>S</code> 필드의 값이 'T'(Stopped)로 변경된다.<br>
- <strong>후속 조치</strong>: 정지된 프로세스를 다시 가동(Continue)시키기 위해서는 <code>SIGCONT</code>(18번) 시그널을 해당 프로세스에 전송해야 한다.
</blockquote>
</details>

### 3. UNIX/Linux 시스템 관리

#### 시스템 시작과 종료

##### 시스템 런 레벨

<details>
<summary>(단답형) 리눅스 시스템에서 GUI 환경(X-Window)을 지원하는 다중 사용자 모드의 런 레벨 번호를 쓰시오.</summary>
<blockquote>
5
</blockquote>
</details>

<details>
<summary>(단답형) 리눅스 시스템에서 현재 동작 중인 런 레벨을 확인하기 위해 사용하는 명령어를 쓰시오.</summary>
<blockquote>
<code>runlevel</code>
</blockquote>
</details>

<details>
<summary>(단답형) 유닉스/리눅스 시스템 부팅 시 <code>init</code> 프로세스가 참조하여 기본 런 레벨을 결정하는 설정 파일의 경로를 쓰시오.</summary>
<blockquote>
<code>/etc/inittab</code>
</blockquote>
</details>

<details>
<summary>(서술형) 런 레벨 1(Single User Mode)의 특징과 시스템 관리자가 이 모드를 주로 활용하는 구체적인 용도 2가지를 서술하시오.</summary>
<blockquote>
- <strong>특징</strong>: 네트워크 서비스를 지원하지 않는 단일 사용자 모드이며, 오직 루트(root) 관리자만이 시스템에 접근할 수 있다.<br>
- <strong>용도</strong>: 시스템 장애 복구(파일 시스템 체크 등), 루트 관리자 패스워드 분실 시 초기화, 또는 초기 환경 설정 작업 등에 사용된다.
</blockquote>
</details>

<details>
<summary>(서술형) <code>init</code> 프로세스가 특정 런 레벨(예: 3번)로 진입할 때 수행하는 동작 과정을 <code>/etc/rc.d</code> 디렉터리 구조와 연관 지어 설명하시오.</summary>
<blockquote>
<code>init</code> 프로세스는 <code>/etc/inittab</code> 파일에 정의된 기본 런 레벨 또는 명령에 의해 변경된 레벨을 확인한다. 이후 해당 런 레벨에 대응하는 전용 디렉터리(예: <code>/etc/rc.d/rc3.d</code>)로 이동하여, 그 내부에 위치한 스크립트들을 정해진 순서에 따라 실행함으로써 시스템 초기 환경 및 필요한 서비스들을 구동시킨다.
</blockquote>
</details>

<details>
<summary>(서술형) 런 레벨 0(Halt)과 6(Reboot)이 <code>/etc/inittab</code> 파일 내의 <code>initdefault</code>(기본 런 레벨) 항목으로 설정되어서는 안 되는 보안 및 운영상 이유를 서술하시오.</summary>
<blockquote>
운영체제 부팅이 완료되자마자 즉시 시스템을 종료(0번)하거나 무한히 재부팅(6번)하는 루프에 빠지게 되어, 관리자가 정상적인 로그인과 서비스 운영을 전혀 수행할 수 없는 장애 상태가 발생하기 때문이다.
</blockquote>
</details>

<details>
<summary>(작업형) 다음은 런 레벨 3 디렉터리(<code>/etc/rc.d/rc3.d</code>) 내에 존재하는 초기 프로세스 스크립트 파일 목록의 일부이다. 이 파일명들의 가장 앞 문자인 <code>S</code>와 <code>K</code>의 기술적 의미를 각각 설명하고, 뒤따르는 숫자가 갖는 의미를 설명하시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
- K01dnsmasq<br>
- S13rpcbind<br>
- S22messagebus
</div>
</summary>
<blockquote>
- <strong>S (Start)</strong>: 해당 런 레벨로 진입 시 해당 서비를 실행(Start)함을 의미한다.<br>
- <strong>K (Kill/Stop)</strong>: 해당 런 레벨로 진입 시 기존에 실행 중이던 서비스를 중지(Kill)함을 의미한다.<br>
- <strong>숫자</strong>: 프로그램이 실행되거나 종료되는 '우선순위(순서)'를 의미하며, 낮은 숫자일수록 먼저 실행/종료된다.
</blockquote>
</details>

<details>
<summary>(작업형) 한 관리자가 리눅스 서버 점검 중 <code>runlevel</code> 명령을 실행하여 <code>N 3</code>이라는 결과를 확인했다. 이 출력 데이터가 의미하는 내용을 이전 런 레벨과 현재 런 레벨 관점에서 분석하여 서술하시오.</summary>
<blockquote>
- <strong>3</strong>: 현재 시스템이 런 레벨 3(네트워크를 지원하는 다중 사용자 모드)으로 동작 중임을 의미한다.<br>
- <strong>N</strong>: 시스템 부팅 이후 현재까지 런 레벨이 한 번도 변경되지 않았음(None)을 의미한다.
</blockquote>
</details>

<details>
<summary>(작업형) 유닉스(Solaris 등) 시스템에서 현재 런 레벨 정보를 확인하기 위해 사용하는 <code>who</code> 명령어의 옵션과, 시스템이 런 레벨 3으로 구동 중일 때의 출력 예시를 작성하시오.</summary>
<blockquote>
- <strong>옵션</strong>: <code>-r</code> (<code>who -r</code>)<br>
- <strong>출력 예시</strong>: <code>run-level 3 Feb 10 02:20 3 0 S</code> (형식은 시스템에 따라 다를 수 있으나 'run-level 3'이 포함됨)
</blockquote>
</details>

##### 시스템 시작

<details>
<summary>리눅스의 부팅 과정 중 발생할 수 있는 보안 위협을 방지하기 위해 사용되는 '싱글 모드(Single Mode) 진입 시 패스워드 설정'의 필요성과 설정 방법을 설명하시오.</summary>
<blockquote>
싱글 모드는 루트(root) 권한으로 비밀번호 없이 시스템에 접근하여 설정을 변경할 수 있는 모드이므로, 물리적 접근이 가능한 공격자가 관리자 권한을 탈취하는 것을 방지하기 위해 비밀번호 설정이 필수적이다. `/etc/sysconfig/init` 파일 내의 `SINGLE` 설정을 수정하거나, GRUB 부트로더에 `password`를 설정하여 인증 절차를 강화할 수 있다.
</blockquote>
</details>

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

<details>
<summary>(단답형) 시스템에 전원이 공급된 후 가장 먼저 실행되어 CPU, 메모리 등 주요 하드웨어의 이상 유무를 점검하고 하드웨어 정보를 수집하는 과정의 명칭을 쓰시오.</summary>
<blockquote>
바이오스 (BIOS : Basic Input/Output System) 과정
</blockquote>
</details>

<details>
<summary>(단답형) 커널에 의해 생성되는 시스템의 첫 번째 프로세스로, 모든 프로세스의 부모 역할을 수행하며 PID(Process ID) 1번을 할당받는 프로세스의 명칭을 쓰시오.</summary>
<blockquote>
init 프로세스
</blockquote>
</details>

<details>
<summary>(서술형) 유닉스/리눅스의 시스템 부팅 과정을 주요 4단계(BIOS, 부트 프로그램, 커널, init)로 구분하고, 각 단계에서 수행되는 핵심 작업을 단계별로 요약하여 설명하시오.</summary>
<blockquote>
1. <strong>BIOS 과정</strong>: 하드웨어 점검(POST) 및 시스템 하드웨어 정보 수집<br>
2. <strong>부트 프로그램 과정</strong>: 하드디스크에서 커널을 읽어 메모리에 적재하고 커널에 제어권 인도<br>
3. <strong>커널 과정</strong>: 추가 커널 모듈 적재 및 시스템 운영을 위한 내부 자료구조 초기화<br>
4. <strong>init 과정</strong>: PID 1번으로 실행되어 사용자가 시스템을 사용할 수 있도록 초기화 작업(초기 프로세스 기동) 수행
</blockquote>
</details>

<details>
<summary>(서술형) 커널(Kernel)이 메모리에 적재된 이후, 운영체제가 실제로 하드웨어의 모든 기능을 제어하기 위해 수행하는 내부적인 주요 처리 내용 두 가지를 기술하시오.</summary>
<blockquote>
- 하드웨어 점검 완료 및 시스템 운영에 필요한 내부 자료구조 초기화<br>
- 하드디스크로부터 부가적인 커널 모듈을 메모리로 읽어 들여 적재
</blockquote>
</details>

<details>
<summary>(작업형) 시스템 부팅 중 특정 하드웨어 드라이버 로드 실패로 인해 'Kernel Panic' 메시지가 출력되며 부팅이 멈췄다. 이 현상은 부팅 4단계 중 어느 과정에서 발생한 것으로 판단할 수 있으며, 그 단계에서 커널이 수행하려고 했던 작업은 무엇인지 기술하시오.</summary>
<blockquote>
- <strong>단계</strong>: 커널(Kernel) 과정<br>
- <strong>작업 내용</strong>: 커널이 메모리에 적재된 후 하드웨어를 제어하기 위해 하드디스크에서 부가적인 커널 모듈(드라이버 등)을 메모리로 로드하고 초기화하는 과정에서 발생한 것으로 판단할 수 있다.
</blockquote>
</details>

<details>
<summary>(작업형) 리눅스 서버 가동 시 <code>ps -ef</code> 명령을 실행했을 때, <code>init</code> 프로세스의 PPID(부모 프로세스 ID) 값이 0으로 나타나는 기술적인 이유를 부팅 과정과 연관 지어 서술하시오.</summary>
<blockquote>
<code>init</code> 프로세스는 사용자가 실행하는 일반 프로세스와 달리 커널에 의해 직접 생성되는 시스템의 첫 번째 프로세스(PID 1)이기 때문이다. 따라서 논리적으로 부모 프로세스가 존재하지 않음을 나타내기 위해 PPID가 0으로 설정된다.
</blockquote>
</details>

##### 시스템 종료

<details>
<summary>(단답형) 유닉스/리눅스 시스템을 안전하게 종료하기 위해 사용하는 대표적인 명령어의 명칭을 쓰시오.</summary>
<blockquote>
shutdown
</blockquote>
</details>

<details>
<summary>(서술형) 운영 중인 리눅스 서버를 종료하기 직전, 시스템 관리자가 데이터 손실 방지 및 안정성 확보를 위해 반드시 확인하거나 수행해야 할 주의사항 3가지를 기술하시오.</summary>
<blockquote>
1. 현재 접속 중인 사용자들에게 종료 사실을 공지하여 작업을 마무리하도록 안내한다.<br>
2. 운영 중인 주요 서비스(프로세스)들이 안전하게 종료되도록 조치한다.<br>
3. 메모리의 변경 내용을 하드디스크에 갱신(Update/Sync)하여 파일 시스템의 무결성을 유지한다.
</blockquote>
</details>

<details>
<summary>(작업형) 만약 관리자가 <code>shutdown</code> 명령을 사용하지 않고 서버의 전원을 갑자기 차단했을 때, 이후 재부팅 시 발생할 수 있는 파일 시스템 상의 문제점과 이를 방지하기 위한 '종료 전 하드디스크 갱신' 과정의 중요성을 서술하시오.</summary>
<blockquote>
- <strong>문제점</strong>: 메모리에 남아있던 데이터가 디스크에 채 기록되지 않아 파일 시스템의 무결성이 훼손되거나 데이터 상호 불일치(Inconsistency)가 발생할 수 있다.<br>
- <strong>중요성</strong>: 안전한 종료 과정에서는 관리자가 하드디스크를 최신 상태로 갱신하여 커널 메모리의 버퍼 내용과 물리적 디스크 내용을 동시화(Sync)함으로써 파일 시스템의 정합성을 보장해야 한다.
</blockquote>
</details>

#### 사용자 및 그룹 관리

##### 사용자 관리(추가, 변경 및 삭제)

<details>
<summary>리눅스 환경에서 새로 생성되는 사용자 계정의 홈 디렉터리에 자동으로 복사할 기본 설정 파일들(.bashrc 등)을 저장해 두는 디렉터리 경로를 쓰시오.</summary>
<blockquote>
/etc/skel
</blockquote>
</details>

<details>
<summary>(단답형) <code>useradd</code> 또는 <code>usermod</code> 명령어 사용 시, 기존에 존재하는 UID와 중복된 값을 가진 계정을 생성하거나 변경할 수 있도록 허용하는 옵션을 쓰시오.</summary>
<blockquote>
-o (non-unique)
</blockquote>
</details>

<details>
<summary>(단답형) 사용자 계정을 추가할 때 해당 사용자가 속할 '보조 그룹'들을 지정하기 위해 사용하는 옵션을 쓰시오.</summary>
<blockquote>
-G
</blockquote>
</details>

<details>
<summary>(단답형) <code>userdel</code> 명령어로 계정 삭제 시, 해당 사용자의 홈 디렉터리와 메일 함까지 모두 강제로 삭제하기 위해 반드시 포함해야 하는 옵션을 쓰시오.</summary>
<blockquote>
-r
</blockquote>
</details>

<details>
<summary>(서술형) 시스템 관리자가 <code>useradd -o -u 0 hacker</code>와 같은 명령어를 실행했을 때 발생할 수 있는 보안상 위험성을 '권한' 관점에서 서술하시오.</summary>
<blockquote>
<code>-o</code> 옵션은 중복 UID를 허용하며, <code>-u 0</code>은 루트(root) 관리자의 UID를 의미한다. 따라서 <code>hacker</code>라는 이름의 일반 계정처럼 보이지만 실제로는 커널 내부적으로 루트와 동일한 권한(UID 0)을 가지게 되어, 공격자가 관리자 권한을 영구적으로 탈취하는 수단으로 악용될 수 있다.
</blockquote>
</details>

<details>
<summary>(서술형) <code>useradd</code> 명령어에서 사용자의 그룹을 지정하는 <code>-g</code> 옵션과 <code>-G</code> 옵션의 기술적인 차이점을 설명하시오.</summary>
<blockquote>
- <strong>-g 옵션</strong>: 사용자의 '기본 그룹(Primary Group)'을 지정한다. 프로세스 실행 시 기본 GID로 사용된다.<br>
- <strong>-G 옵션</strong>: 사용자가 추가적으로 속하게 될 '보조 그룹(Supplementary Groups)'을 지정한다. 여러 개의 그룹을 쉼표로 구분하여 등록 가능하다.
</blockquote>
</details>

<details>
<summary>(서술형) 아르바이트생의 계정을 <code>userdel worker</code> 명령으로 삭제했다. 이후 신규 사용자가 동일한 아이디 <code>worker</code>를 사용할 경우 발생할 수 있는 잠재적 이슈와 이를 방지하기 위한 권장 옵션을 서술하시오.</summary>
<blockquote>
- <strong>이슈</strong>: <code>-r</code> 옵션 없이 삭제하면 기존 사용자의 홈 디렉터리가 시스템에 그대로 남아있어, 신규 사용자가 동일한 이름으로 생성될 경우 이전 사용자의 데이터를 그대로 상속받거나 보안상 노출될 위험이 있다.<br>
- <strong>방지 옵션</strong>: 반드시 <code>-r</code> 옵션을 사용하여 계정 삭제 시 홈 디렉터리와 메일 스풀을 함께 깔끔하게 제거해야 한다.
</blockquote>
</details>

<details>
<summary>(작업형) 다음 조건에 부합하는 새로운 사용자 <code>dev01</code>을 생성하는 한 줄의 명령어를 작성하시오.
- UID 번호: 700<br>
- 설명(Comment): "Developer 01"<br>
- 로그인 쉘: /bin/bash<br>
- 홈 디렉터리 자동 생성 포함</summary>
<blockquote>
<code>useradd -u 700 -c "Developer 01" -s /bin/bash -m dev01</code>
</blockquote>
</details>

<details>
<summary>(작업형) 관리자가 <code>usermod -G wheel test01</code> 명령을 실행했다. 이후 <code>/etc/group</code> 파일 내에서 <code>wheel</code> 그룹의 정보를 확인했을 때 예상되는 출력 줄의 형태를 기술하시오. (단, 기존 wheel 그룹에 root, algisa가 있었다고 가정)</summary>
<blockquote>
<code>wheel:x:10:root,algisa,test01</code>
</blockquote>
</details>

<details>
<summary>(작업형) 다음 <code>/etc/passwd</code> 설정 내용 중 보안상 가장 큰 위협으로 판단되는 행(Line)을 고르고, 그 이유를 해당 행의 필드 값을 근거로 설명하시오.
<div style="border: 1px solid #777; padding: 10px; margin-top: 10px; border-radius: 5px;">
1. user01:x:500:500::/home/user01:/bin/bash<br>
2. service:x:0:0::/home/service:/bin/bash<br>
3. guest:x:600:600::/home/guest:/sbin/nologin
</div>
</summary>
<blockquote>
- <strong>위험한 행</strong>: 2번 (service)<br>
- <strong>이유</strong>: 세 번째 필드(UID)와 네 번째 필드(GID)가 모두 <code>0</code>으로 설정되어 있다. 이는 <code>service</code>라는 일반 계정 명칭을 사용하고 있지만 권한은 최고 관리자(root)와 완벽히 동일함을 의미하므로, 백도어 계정으로 의심할 수 있다.
</blockquote>
</details>

##### 그룹 관리(추가, 변경 및 삭제)

<details>
<summary>(단답형) 시스템에 새로운 그룹을 추가할 때, 관리자가 특정 그룹 ID(GID)를 수동으로 지정하기 위해 사용하는 옵션을 쓰시오.</summary>
<blockquote>
-g
</blockquote>
</details>

<details>
<summary>(단답형) 기존에 존재하는 그룹의 '그룹 이름'만을 새로운 이름으로 변경하고자 할 때 사용하는 <code>groupmod</code> 명령어의 옵션을 쓰시오.</summary>
<blockquote>
-n
</blockquote>
</details>

<details>
<summary>(단답형) 시스템에 등록된 특정 그룹을 완전히 삭제하기 위해 사용하는 명령어를 쓰시오.</summary>
<blockquote>
groupdel
</blockquote>
</details>

<details>
<summary>(서술형) <code>groupadd -g 600 soc</code> 명령어 실행 시 시스템 내부 설정 파밀(예: <code>/etc/group</code>)에 일어나는 변화를 서술하시오.</summary>
<blockquote>
해당 파일 마지막에 <code>soc</code>라는 이름의 새로운 그룹이 추가되며, 해당 그룹의 GID 번호가 <code>600</code>으로 기록된다.
</blockquote>
</details>

<details>
<summary>(서술형) 새로운 사용자를 각각 생성하여 권한을 제어하지 않고 기존의 '그룹'을 생성/변경하여 관리해야 하는 이유를 권한 관리의 관점에서 서술하시오.</summary>
<blockquote>
다수의 사용자가 동일한 디렉터리나 파일에 접근해야 하는 공동 작업 환경에서, 사용자 개개인에게 개별 인증/권한을 부여하는 대신 하나의 그룹을 생성하고 사용자들을 그룹에 포함시켜 그룹 권한을 부여함으로써 권한 관리를 통합적이고 효율적으로 수행할 수 있기 때문이다.
</blockquote>
</details>

<details>
<summary>(서술형) 특정 사용자가 포함된 보조 그룹을 <code>groupdel</code> 명령을 통해 삭제했을 때 해당 사용자의 권한 관점에서 발생할 수 있는 영향을 서술하시오.</summary>
<blockquote>
해당 보조 그룹에 부여되었던 특정 디렉터리나 파일에 대한 접근 권한(소유 그룹 권한)을 즉각 잃게 되어, 그룹 기반으로 묶여서 제어되던 자원 사용 및 공유가 불가능해진다.
</blockquote>
</details>

<details>
<summary>(작업형) GID 번호가 <code>700</code> 인 <code>sec</code> 라는 이름의 그룹을 시스템에 새롭게 추가하기 위한 한 줄짜리 명령어를 작성하시오.</summary>
<blockquote>
<code>groupadd -g 700 sec</code>
</blockquote>
</details>

<details>
<summary>(작업형) 현재 시스템에 <code>soc</code>라는 그룹이 존재한다. 이 그룹의 명칭을 <code>secure</code>로 변경하고, 그룹의 GID를 <code>800</code>으로 동시에 변경하는 <code>groupmod</code> 명령어 구문을 작성하시오.</summary>
<blockquote>
<code>groupmod -g 800 -n secure soc</code>
</blockquote>
</details>

<details>
<summary>(작업형) 보안 검사 과정에서 <code>unknown</code> 이라는 불필요한 테스트용 그룹이 발견되었다. 이 그룹을 시스템에서 완전히 제거하여 권한 오용의 소지를 없애는 명령어를 작성하시오.</summary>
<blockquote>
<code>groupdel unknown</code>
</blockquote>
</details>

#### 파일 시스템 관리

##### 파일시스템(디스크) 여유 공간 크기 관리(df 명령어)

<details>
<summary>(단답형) 디스크 상의 파일 시스템을 유닉스/리눅스 시스템의 특정 디렉터리에 논리적으로 연결하여 사용자가 접근할 수 있도록 하는 과정을 뜻하는 용어를 쓰시오.</summary>
<blockquote>
마운트(mount)
</blockquote>
</details>

<details>
<summary>(단답형) <code>df</code> 명령어 실행 결과를 관리자가 알아보기 쉽도록 M(메가바이트), G(기가바이트) 단위 등 '사람이 읽기 쉬운(Human Readable)' 용량 단위로 변환 출력해주는 옵션을 쓰시오.</summary>
<blockquote>
-h
</blockquote>
</details>

<details>
<summary>(단답형) 시스템에 마운트되어 있는 특정 파일 시스템(예: <code>/dev/sda1</code>)의 연결을 안전하게 해제하여 분리할 때 사용하는 명령어를 쓰시오.</summary>
<blockquote>
umount
</blockquote>
</details>

<details>
<summary>(서술형) 시스템 관리자가 주기적으로 <code>df</code> 명령을 통해 파일 시스템의 가용 공간을 모니터링하고 임계치를 설정해야 하는 가장 중요한 가용성 관점의 이유를 서술하시오.</summary>
<blockquote>
파일 시스템의 여유 공간이 고갈되면 시스템 구동에 필수적인 로그가 기록되지 못하거나, 새로운 프로세스 생성이 불가하여 데몬이 중단되는 등 치명적인 시스템 서비스 장애(가용성 저하)가 발생할 수 있기 때문이다.
</blockquote>
</details>

<details>
<summary>(서술형) <code>df</code> 명령어를 아무런 인자나 옵션 없이 단독으로 실행했을 때 보여주는 정보의 범위와 내용에 대해 서술하시오.</summary>
<blockquote>
현재 시스템에 마운트되어 있는 <strong>모든 파일 시스템(디스크 파티션)</strong>들의 전체 용량, 사용량, 남은 여유 공간 크기, 사용률, 그리고 각각 마운트된 디렉터리 경로 정보를 모두 나열하여 출력한다.
</blockquote>
</details>

<details>
<summary>(서술형) <code>df -h /tmp</code> 처럼 명령의 인수로 '특정 물리 장치 트리'가 아닌 특정 일반 '디렉터리'를 지정했을 때, <code>df</code> 명령이 화면에 출력해주는 정보의 기준점을 설명하시오.</summary>
<blockquote>
지정한 <code>/tmp</code> 디렉터리 내부 파일들만의 자체 크기가 아니라, 해당 디렉터리가 속해 있는(마운트된) <strong>시스템 파티션이나 디스크의 전체 용량과 전체 남은 여유 공간 상태</strong>를 출력해 준다.
</blockquote>
</details>

<details>
<summary>(작업형) 시스템의 루트(<code>/</code>) 파일 시스템이 위치한 파티션의 남은 여유 용량과 사용률(Use%)을 사람이 보기 편한 단위(K, M, G 등)로 확인하기 위한 명령어를 작성하시오.</summary>
<blockquote>
<code>df -h /</code>
</blockquote>
</details>

<details>
<summary>(작업형) 관리자가 <code>df -h /dev/sda2</code> 명령을 실행하여 <code>Use%</code> 필드가 100%임을 확인했다. 긴급하게 가용성을 확보하기 위해 관리자가 단계적으로 취할 수 있는 대표적인 조치 방안 두 가지를 서술하시오.</summary>
<blockquote>
1. 불필요한 대용량 파일(백업본 등)이나 너무 오래 보관된 각종 로그 파일들을 1차적으로 긴급 삭제하여 즉각적인 여유 공간을 확보한다.<br>
2. 물리적으로 새로운 여분의 디스크 장치를 증설하고 추가로 마운트하여 실질적인 디스크 용량 한도를 넓힌다.
</blockquote>
</details>

<details>
<summary>(작업형) 출력된 <code>df</code> 명령 결과 중 마지막 필드인 <code>Mounted on</code>은 기술적으로 어떤 구체적 의미를 갖는지 서술하시오.</summary>
<blockquote>
해당 물리 디스크 파티션(장치 파일)이 논리적인 리눅스 디렉터리 트리 구조상에서 정확히 <strong>어떤 디렉터리를 연결점(마운트 포인트)으로 삼아 동작하고 있는지 그 진입 경로</strong>를 의미한다.
</blockquote>
</details>

##### 디렉터리(파일)별 파일시스템(디스크) 사용량 관리(du 명령어)

<details>
<summary>(단답형) 특정 디렉터리 내에 존재하는 모든 하위 디렉터리뿐만 아니라, 개별 '파일'들에 대한 각각의 디스크 사용량까지 숨김없이 모두 나열해서 출력하도록 지시하는 <code>du</code> 명령어의 옵션을 쓰시오.</summary>
<blockquote>
-a
</blockquote>
</details>

<details>
<summary>(단답형) 특정 디렉터리의 내부 하위 구조나 요소들 크기를 일일이 출력하지 않고, 해당 디렉터리가 차지하는 '전체(총합)' 크기 하나만을 단일값으로 요약해서 보고 싶을 때 사용하는 <code>du</code> 명령어의 옵션을 쓰시오.</summary>
<blockquote>
-s
</blockquote>
</details>

<details>
<summary>(단답형) <code>df</code> 명령어는 '디스크 파티션' 단위로 공간을 보여준다면, <code>du</code> 명령어는 무엇을 기준으로 크기를 확인하는지 그 대상이 되는 개체 단위 두 가지를 쓰시오.</summary>
<blockquote>
디렉터리, 파일
</blockquote>
</details>

<details>
<summary>(서술형) <code>df</code> 명령어와 <code>du</code> 명령어가 디스크 용량을 다룬다는 점에서는 유사하나, 시스템을 관리하는 기술적 관점과 확인 '목적'에서 어떠한 구별이 있는지 서술하시오.</summary>
<blockquote>
- <strong><code>df</code></strong>: 파일 시스템(파티션) 단위로 '전체 디스크의 가용성(남은 여유 공간)'과 마운트 상태를 전반적으로 파악하고자 할 때 사용된다.<br>
- <strong><code>du</code></strong>: 가용 공간보다는 특정 디렉터리 구조 내부나 개별 파일들이 한정된 공간 안에서 '실제로 얼마나 용량을 소비(사용)하고 있는지'를 구체적으로 추적하고 확인할 때 사용된다.
</blockquote>
</details>

<details>
<summary>(서술형) <code>du -hs /var/log</code> 명령어를 실행했을 때 출력되는 결과값의 형태적 특징을 디렉터리의 하위 요소 출력 여부와 용량 단위를 포함하여 서술하시오.</summary>
<blockquote>
<code>/var/log</code> 내부의 수많은 개별 파일이나 폴더 내역은 전혀 출력되지 않고 생략(<code>-s</code>)되며, 오직 <code>/var/log</code> 디렉터리 자체가 차지하는 합산 총 용량만이 인간이 읽기 쉬운 M이나 G 등의 단위(<code>-h</code>)와 함께 한 줄로 압축되어 출력된다.
</blockquote>
</details>

<details>
<summary>(서술형) 시스템 장애 조사 중 관리자가 루트 디렉터리(`/`) 등 상위 경로에서 주기적으로 <code>du -s *</code> 명령을 수행하는 시스템 운영상의 주된 이유를 '용량 추적' 측면에서 서술하시오.</summary>
<blockquote>
시스템의 디스크 용량이 부족해지는 문제가 생길 때, 최상위 경로의 각 디렉터리별 총 사용량을 요약함으로써 유독 과도하게 용량을 많이 차지하고 비대해진 디렉터리를 색출하고 그 원인(예: 폭증한 로그 폴더)을 하향식으로 효율적으로 추적하기 위해서이다.
</blockquote>
</details>

<details>
<summary>(작업형) <code>/home</code> 디렉터리 내에 있는 각각의 사용자별 폴더가 차지하는 총 요약 용량을, 관리자가 직관적으로 읽기 쉬운 단위(GB, MB 등)로 한눈에 출력하기 위해 사용하는 구체적인 명령어를 작성하시오.</summary>
<blockquote>
<code>du -hs /home/*</code>
</blockquote>
</details>

<details>
<summary>(작업형) <code>du -h /var/log | head -5</code> 명령 실행 시 화면에 출력되는 데이터가 무슨 내용을 담고 있는지 그 의미를 분석하고 파이프(<code>|</code>)의 역할을 결합하여 서술하시오.</summary>
<blockquote>
<code>/var/log</code> 디렉터리와 그 안의 하위 디렉터리들이 각각 사용 중인 디스크 용량을 쉬운 단위(<code>-h</code>)로 나열하여 출력하되, 파이프(<code>|</code>)로 연결된 <code>head -5</code> 필터를 거치게 하여 그 전체 결과 중 상위 5줄까지만 끊어서 화면에 보여준다.
</blockquote>
</details>

<details>
<summary>(작업형) 너무 비대해져서 문제를 유발하고 있는 로그 파일인 <code>/var/log/messages</code> 파일 단일 객체만의 현재 남은 용량이 아니라 '직접 사용 중인 크기(MB 지원)'를 빠르고 직관적으로 확인하기 위해 실행해야 할 명령 구문을 작성하시오.</summary>
<blockquote>
<code>du -h /var/log/messages</code>
</blockquote>
</details>

#### 작업 스케줄 관리

##### cron 서비스(정기적 작업 스케줄 관리 서비스)

<details>
<summary>(단답형) 관리자가 모든 사용자의 예약 작업을 등록/관리하는 용도로 사용하며, 일반적으로 <code>root</code> 권한으로만 편집할 수 있도록 권장되는 cron 작업 등록 파일의 절대 경로를 쓰시오.</summary>
<blockquote>
/etc/crontab
</blockquote>
</details>

<details>
<summary>(단답형) 개별 사용자(예: <code>algisa</code>)가 <code>crontab</code> 명령을 통해 예약 작업을 등록했을 때, 해당 작업 내역이 실제로 저장되는 파일의 절대 경로(계정명 포함)를 쓰시오.</summary>
<blockquote>
/var/spool/cron/algisa
</blockquote>
</details>

<details>
<summary>(단답형) 특정 사용자(예: <code>kiwi99</code>)가 <code>crontab</code> 명령어를 아예 사용할 수 없도록 블랙리스트 방식으로 차단 정책을 적용할 때 설정해야 하는 파일의 명칭(경로 제외)을 쓰시오.</summary>
<blockquote>
cron.deny
</blockquote>
</details>

<details>
<summary>(서술형) 백그라운드 환경에서 정기적으로 실행되는 cron 예약 작업의 결과(표준 출력 및 에러)를 터미널로 출력할 필요가 없을 때 흔히 사용하는 <code>&gt; /dev/null 2&gt;&amp;1</code> 재지정(Redirection) 문법의 구체적인 의미와 목적을 서술하시오.</summary>
<blockquote>
- <strong>의미</strong>:명령어 실행 결과로 발생하는 정상 출력(1)과 에러 메시지(2)를 모두 <code>/dev/null</code> 이라는 특수 블랙홀 장치 파일로 던져버리겠다는 뜻이다.<br>
- <strong>목적</strong>: cron 데몬이 남기는 불필요한 출력물로 인해 시스템 메일이나 로그가 꽉 차는 현상을 방지하기 위해 출력을 완전히 무시(폐기)할 목적으로 사용한다.
</blockquote>
</details>

<details>
<summary>(서술형) <code>/etc/crontab</code> 파일과 <code>/var/spool/cron/</code> 하위에 저장되는 개별 사용자용 crontab 파일에 기록할 때 문법 필드 구성상 어떠한 차이가 존재하는지 '계정명' 관점에서 비교 서술하시오.</summary>
<blockquote>
<code>/etc/crontab</code>은 관리자가 모든 사용자를 관리하는 파멸이므로 시간 설정 뒤에 실행 주체인 <strong>'계정명(User)' 필드가 반드시 필요</strong>하다. 반면, 개별 사용자 파일은 그 파일 자체가 계정을 의미하므로 <strong>'계정명' 필드를 생략</strong>하고 바로 실행할 명령어를 기입한다.
</blockquote>
</details>

<details>
<summary>(서술형) 시스템에 <code>/etc/cron.allow</code> 파일과 <code>/etc/cron.deny</code> 파일이 동시에 존재할 경우, 운영체제의 접근 제어 정책이 어떤 우선순위 메커니즘으로 동작하게 되는지 논리적 흐름을 서술하시오.</summary>
<blockquote>
<code>cron.allow</code> 파일이 항상 <code>cron.deny</code>보다 높은 최우선 순위를 갖는다. 따라서 시스템은 <code>allow</code> 파일을 먼저 검사하여 허용 목록을 100% 신뢰하며, <code>allow</code> 파일이 존재하는 순간 <code>deny</code> 파일의 내용은 완전히 무시되고 작동하지 않게 된다.
</blockquote>
</details>

<details>
<summary>(작업형) 관리자(<code>root</code>)가 <code>/etc/crontab</code> 파일에 아래와 같이 매주 월요일부터 금요일까지 새벽 6시 20분에 <code>/work/batch.sh</code> 스크립트를 <code>root</code> 권한으로 실행하도록 스케줄을 추가하려 한다. 시간 설정 5개 필드(분, 시, 일, 월, 요일)를 정확히 채워서 한 줄의 포맷(형식)을 완성하시오. (단, 요일은 숫자로 표기)</summary>
<blockquote>
<code>20 6 * * 1-5 root /work/batch.sh</code>
</blockquote>
</details>

<details>
<summary>(작업형) 관리자 접속 상태(root)에서 특권 명령어를 사용하여 시스템에 존재하는 일반 계정인 <code>algisa</code> 의 내부에 설정된 cron 작업 목록 전체를 화면에 출력하여 점검(List)하기 위한 명령줄을 작성하시오.</summary>
<blockquote>
<code>crontab -u algisa -l</code> (또는 -u algisa 생략 불가)
</blockquote>
</details>

<details>
<summary>(작업형) <code>0 8-10 * * * algisa /work/batch.sh</code> 이라는 스케줄이 <code>/etc/crontab</code> 파일에 등록되어 있다. 이 작업이 일주일 중 언제, 몇 시 몇 분에 실행되도록 설정되어 있는지 그 주기를 한국어로 명확하게 풀어 쓰시오.</summary>
<blockquote>
매일(월~일 무관, 매월 매일) 8시 정각, 9시 정각, 10시 정각마다 하루 총 3번 <code>algisa</code> 계정 권한으로 작업을 실행한다.
</blockquote>
</details>

### 4. UNIX/Linux 서버 보안

#### 시스템 보안

##### 사용자의 패스워드 관리

<details>
<summary>(단답형) <code>/etc/passwd</code> 파일에서 사용자의 패스워드 필드(두 번째 필드)에 기재되어 있는 문자 <code>x</code>가 기술적으로 의미하는 바를 구체적으로 쓰시오.</summary>
<blockquote>
패스워드를 사용하지 않는다는 의미가 아니며, <strong>shadow 패스워드 정책을 적용하여 실제 암호화된 비밀번호가 <code>/etc/shadow</code> 파일에 별도로 보관되어 있음</strong>을 뜻한다.
</blockquote>
</details>

<details>
<summary>(단답형) 시스템 데몬 계정이나 애플리케이션 계정 등 '로그인 자체가 불필요한 계정'에 대해 우발적인 접속이나 악의적인 로그인을 원천 차단하기 위해 계정의 '로그인 쉘(Login Shell)' 경로로 지정하는 대표적인 가짜(false) 쉘 경로 두 가지를 쓰시오.</summary>
<blockquote>
<code>/sbin/nologin</code> , <code>/bin/false</code>
</blockquote>
</details>

<details>
<summary>(단답형) 시스템의 패스워드 저장 정책을 기존의 '일반 패스워드 정책(<code>/etc/passwd</code> 단일 파일 사용)'에서 보다 안전한 'Shadow 패스워드 정책(별도 파일 분리)'으로 마이그레이션(변경)할 때 사용하는 관리자용 명령어를 쓰시오.</summary>
<blockquote>
<code>pwconv</code>
</blockquote>
</details>

<details>
<summary>(서술형) 악의적인 해커가 백도어 계정을 만들어 시스템의 <code>/etc/passwd</code> 설정에 <code>hacker:x:0:0::/home/hacker:/bin/bash</code> 처럼 삽입했다. UID(User ID) 필드 관점에서 이 행위가 어떠한 심각한 보안 위협을 유발하는지 서술하시오.</summary>
<blockquote>
계정 명칭은 'hacker'일지라도 <strong>UID가 0</strong>으로 설정되어 있기 때문에 리눅스 커널 프로세스 관점에서는 이 계정을 최고 관리자(root)와 완벽히 동일한 권한을 가진 계정으로 인식하게 되어, 시스템 전체의 통제권이 영구적으로 탈취되는 치명적인 루트 권한 스푸핑 위협을 유발한다.
</blockquote>
</details>

<details>
<summary>(서술형) <code>/etc/shadow</code> 파일에 패스워드를 저장할 때 '솔트(Salt)'라는 임의의 문자열을 추가로 섞어 해시하는 기법이 어떻게 '레인보우 테이블 공격(Rainbow Table Attack)'을 효과적으로 무력화할 수 있는지 기술적 근거를 들어 서술하시오.</summary>
<blockquote>
두 사용자가 우연히 동일한 비밀번호를 사용하더라도, 각 계정마다 난수화된 솔트(Salt)가 별도로 부착된 채 해싱되므로 최종 산출되는 암호화된 해시값이 완전히 달라진다. 따라서 사전에 해시값을 대량으로 계산해둔 레인보우 테이블을 대조하여 원래의 패스워드를 맵핑해내는 공격 기법이 의미가 없어진다.
</blockquote>
</details>

<details>
<summary>(서술형) 패스워드 에이징 정보 중 '최대 사용 기간(<code>max_life</code>)'과 '최소 사용 기간(<code>min_life</code>)' 정책을 설정하지 않았을 때 유발될 수 있는 보안 측면의 부작용을 각각 서술하시오.</summary>
<blockquote>
- <strong>최소 사용 기간(min_life) 부재 시</strong>: 사용자가 암호 변경 의무를 회피하기 위해 변경 직후 즉시 이전 암호로 롤백(재사용)해버리는 악의적인 반복 우회 현상이 발생할 수 있다.<br>
- <strong>최대 사용 기간(max_life) 부재 시</strong>: 패스워드 만료일이 사라져 한 번 유출된 패스워드로 공격자가 수십 년간 제약 없이 접속할 수 있게 된다.
</blockquote>
</details>

<details>
<summary>(작업형) 관리자가 보안 점검 중 의심스러운 행위를 하는 <code>kiwi99</code> 계정을 발견하여, 임시 조치로 이 계정의 로컬 패스워드 로그인을 강제로 잠금(Lock) 처리하려고 한다. 이어서 혐의가 벗어져 다시 로그인을 허용(Unlock)하려고 한다. 두 작업을 순서대로 <code>passwd</code> 명령어를 활용하여 각각 작성하시오.</summary>
<blockquote>
1. 잠금(Lock): <code>passwd -l kiwi99</code><br>
2. 해제(Unlock): <code>passwd -u kiwi99</code>
</blockquote>
</details>

<details>
<summary>(작업형) 관리자가 <code>/etc/shadow</code> 파일 내부를 들여다보니 <code>kiwi99</code> 사용자의 두 번째 필드(패스워드 해시)가 <code>$6$S1S1$TyCOb...</code> 의 형태로 기록되어 있었다. <code>$6$</code> 이라는 특정 기호가 의미하는 해시 암호화 알고리즘의 명칭을 식별하시오.</summary>
<blockquote>
SHA-512 알고리즘
</blockquote>
</details>

<details>
<summary>(작업형) <code>/etc/passwd</code> 설정 파일에서 터미널 출력값이 <code>apache:x:48:48:Apache:/var/www:/sbin/nologin</code> 으로 표기된 것을 발견했다. 콜론(<code>:</code>)으로 구분된 총 7가지 속성들의 의미를 순서대로 나열하여 해당 계정의 속성을 풀어 서술하시오.</summary>
<blockquote>
1. 계정명 (<code>apache</code>)<br>
2. 패스워드 위치 식별자 (<code>x</code>, Shadow 사용)<br>
3. 사용자 ID / UID (<code>48</code>)<br>
4. 기본 그룹 ID / GID (<code>48</code>)<br>
5. 계정 설명 / Comment (<code>Apache</code>)<br>
6. 유저의 홈 디렉터리 경로 (<code>/var/www</code>)<br>
7. 로그인 쉘 경로 (<code>/sbin/nologin</code>, 로그인 불가)
</blockquote>
</details>

<details>
<summary>리눅스 환경에서 사용자 계정의 패스워드 만료일, 암호 변경 최소/최대 일수 등 패스워드 에이징(Aging) 정보를 저장하고 있는 파일의 절대 경로를 쓰시오.</summary>
<blockquote>
/etc/shadow
</blockquote>
</details>

##### 프로세스 실행권한(SUID,SGID)

<details>
<summary>(단답형) 유닉스/리눅스 시스템에서 특정 자원(프로세스)에 대한 접근 권한을 판단하는 속성 중, 그 프로세스를 '최초로 실행시킨 실제 사용자'의 고유 식별 번호를 의미하는 영문 약어를 쓰시오.</summary>
<blockquote>
RUID (Real User ID)
</blockquote>
</details>

<details>
<summary>(단답형) 기본적으로 권한이 <code>755</code>로 설정된 <code>a.out</code> 실행 파일에, '사용자(owner)' 관점의 특수 실행 비트인 SUID(SetUID) 권한을 추가로 부여하기 위해 4자리 8진수 숫자를 활용하여 작성하는 <code>chmod</code> 변경 명령어를 쓰시오.</summary>
<blockquote>
<code>chmod 4755 a.out</code>
</blockquote>
</details>

<details>
<summary>(단답형) 리눅스 서버에서 일반 사용자는 <code>/etc/shadow</code> 파일을 직접 열거나 수정할 권한이 없지만, 특정 명령어(실행 파일)에 SUID 권한이 기본적으로 부여되어 있기 때문에 권한 상승을 통해 자신의 암호를 바꿀 수 있다. 이 명령어의 이름을 쓰시오.</summary>
<blockquote>
<code>passwd</code>
</blockquote>
</details>

<details>
<summary>(서술형) 특수 비트(SUID나 SGID)가 전혀 부여되지 않은 일반적인 실행 파일을 실행했을 때, 실행 주체가 되는 사용자의 RUID(Real UID)가 프로세스의 실제 권한(EUID)으로 전이되는 과정을 메커니즘 관점에서 서술하시오.</summary>
<blockquote>
SUID 등 특수 권한이 없으면 파일을 구동시키는 순간 해당 프로세스의 <strong>RUID(실제 사용자 ID)와 EUID(유효 사용자 ID, 자원 접근권)가 동일하게 세팅</strong>된다. 즉, 프로그램을 실행시킨 사람 원래의 권한 그대로 모든 파일 접근 통제를 받게 된다.
</blockquote>
</details>

<details>
<summary>(서술형) 반대로 SUID(SetUID) 특명 권한이 부여된 실행 파일을 임의의 일반 사용자가 실행하였을 경우, 그 프로세스가 백그라운드 메모리에서 동작하는 동안 EUID(Effective UID)가 누구의 권한으로 결정(매핑)되는지 설명하시오.</summary>
<blockquote>
프로그램을 구동하고 있는 사용자가 누구인지와 무관하게, 프로세스가 돌고 있는 그 일시적인 시간 동안만큼은 무조건 <strong>'해당 실행 파일의 원본 소유자(Owner) UID'</strong>가 EUID로 강제 승격 매핑된다.
</blockquote>
</details>

<details>
<summary>(서술형) 관리자(root) 소유의 SUID 파일이 현장 실무에서 꼭 필요한 합법적/기능적 이유 한 가지와, 동시에 만약 불필요한 프로그램에 관리자 소유의 SUID가 켜져 있을 경우 파생될 수 있는 보안 위협을 한 가지씩 서술하시오.</summary>
<blockquote>
- <strong>필요 이유</strong>: 시스템 핵심 파일에 일반 유저의 무분별한 접근을 차단하면서도, 암호 변경처럼 극히 일부의 엄격히 통제된 절차적 접근만 허용해야 할 때 효율적이다.<br>
- <strong>보안 위협</strong>: 검증되지 않거나 버퍼 오버플로우 등의 취약점이 존재하는 파일에 root SUID가 열려있을 경우, 해커가 이를 트리거하여 쉘(Shell)을 획득하면 시스템 전권을 통째로 탈취하는 백도어(Backdoor) 공격의 교두보가 된다.
</blockquote>
</details>

<details>
<summary>(작업형) 특권 권한 관리의 일환으로 기존에 <code>755</code>였던 <code>suid_01</code> 실행 파일의 그룹 통제력을 상향시켜, 누구나 실행 시 '파일 그룹(Group)'의 유효 권한을 임시로 획득할 수 있도록 SGID 권한을 부여하고자 한다. 8진수 모드가 아닌 <strong>심볼릭 기호 모드(Symbolic Mode)</strong>를 사용하여 한 줄의 변경 명령어를 작성하시오.</summary>
<blockquote>
<code>chmod g+s suid_01</code>
</blockquote>
</details>

<details>
<summary>(작업형) 어떤 시스템 파일의 권한 모드를 <code>ls -l</code> 명령으로 확인했더니 문자열 형태가 <code>rwsr-sr-x</code> 로 표현되어 있었다. 여기서 사용자 권한부와 그룹 권한부에 각각 등장한 소문자 <code>s</code> 기호의 합산적 의미를 8진수 기반의 최상위 특수비트 값 수치로 변환하여 분석 서술하시오.</summary>
<blockquote>
- 사용자 권한의 <code>s</code>는 SetUID(4000 대역)을 의미하고,<br>
- 그룹 권한의 <code>s</code>는 SetGID(2000 대역)을 의미한다.<br>
이 두 가지 <code>s</code> 속성이 중복 부과된 상태이므로 특수 권한 비트의 종합은 <code>6000</code> 대역(결과적으로 전체값은 6755) 권한이 융합되어 설정되었음을 알 수 있다.
</blockquote>
</details>

<details>
<summary>(작업형) 파일 소유자 및 그룹 소유자가 모두 <code>root</code> 로 되어 있으면서 SUID와 SGID가 동시에 설정된 실행 파일 <code>suid_01</code>이 존재한다. 만약 UID 500에 속하는 <code>kiwi99</code> 라는 일반 계정으로 이 파일을 실행했을 때, 해당 프로세스가 작동하는 순간 메모리상에서 내부적으로 가지는 유효 권한인 EUID와 EGID 상태값을 정확히 판별하시오.</summary>
<blockquote>
- <strong>EUID</strong>: 파일의 소유자를 따라가므로 <code>root</code> (UID 0) 가 된다.<br>
- <strong>EGID</strong>: 파일의 그룹 소유자를 따라가므로 <code>root</code> (GID 0) 가 된다.<br>
결국 <code>kiwi99</code>가 켰더라도 실행 순간만큼은 완전무결한 root 권한으로 전권을 휘두르게 된다.
</blockquote>
</details>

<details>
<summary>리눅스 시스템에서 사용자 및 그룹 권한을 제어하는 특수 권한인 SetUID의 개념을 설명하고, 보안 관점에서 SetUID 설정 파일이 위험한 이유를 서술하시오.</summary>
<blockquote>
<strong>개념</strong>: 파일 실행 시 해당 파일의 소유자(owner) 권한으로 실행되도록 하는 파일 확장 속성(권한) 설정이다.<br>
<strong>위험한 이유</strong>: 최고 관리자(root) 소유의 파일에 SetUID가 설정되어 있고 취약점이 존재할 경우, 일반 사용자가 해당 파일을 실행하는 동안 일시적으로 루트 권한을 획득하게 되어 침해 사고로 이어질 수 있기 때문이다.
</blockquote>
</details>

#### 네트워크 보안

##### 보안 쉘(SSH)

<details>
<summary>(단답형) 과거의 rlogin, telnet, FTP와 같이 평문을 송수신하여 스니핑 공격에 취약했던 터미널 환경을 대체하기 위해 등장한, 강력한 원격 암호화 터미널 지원 프로토콜(TCP 22번 포트)의 영문 약어를 쓰시오.</summary>
<blockquote>
SSH (Secure Shell)
</blockquote>
</details>

##### 슈퍼 서버(inetd 데몬)

<details>
<summary>(단답형) 여러 개의 네트워크 서비스 데몬들을 백그라운드 메모리에 일일이 상주시킬 경우 발생하는 리소스 낭비를 막고, 클라이언트의 서비스 연결 요청이 올 때마다 적합한 하위 서비스 자식 모듈을 그때그때 호출해주는, 소위 '데몬의 데몬' 역할을 수행하는 슈퍼 서페이스 명칭을 쓰시오.</summary>
<blockquote>
슈퍼 데몬 (inetd / xinetd)
</blockquote>
</details>

<details>
<summary>(단답형) <code>inetd</code> 데몬은 클라이언트로부터 특정 1~65535 포트 번호로 접수된 요청을 인식하면, 해당 포트가 어떤 이름의 서비스인지(명칭 식별 매핑)를 파악하기 위해 시스템 내부의 특정 환경 설정 파일을 읽는다. 이 IANA 기반 포트 정의 파일의 절대 경로를 작성하시오.</summary>
<blockquote>
<code>/etc/services</code>
</blockquote>
</details>

<details>
<summary>(서술형) 개별 프로세스들이 각자 홀로 구동하는 'Stand-Alone' 방식 데몬과, 'inetd/xinetd' 슈퍼 데몬 방식 데몬의 구동적 장단점을 '소비 자원(메모리)'과 '응답 속도'의 반비례적 상관성에 초점을 맞추어 비교 서술하시오.</summary>
<blockquote>
- <strong>Stand-Alone 방식</strong>: 서비스가 늘 메모리 공간에 떠 있으므로 클라이언트 요청에 즉각적인 반응(<strong>빠른 응답 속도</strong>)을 보이지만, 사용 빈도가 낮아도 항상 상주하므로 <strong>자원이 낭비되는 단점</strong>이 있다.<br>
- <strong>inetd 방식</strong>: 백그라운드에서는 슈퍼 데몬 단 하나만 대기하고 있어 <strong>시스템 유휴 자원을 대폭 아낄</strong> 수 있으나, 요청이 올 때마다 새로 개별 자식 데몬을 하드디스크에서 깨우는 과정을 거쳐야 하므로 <strong>반응 속도는 약간 느려진다</strong>.
</blockquote>
</details>

<details>
<summary>(서술형) <code>/etc/inetd.conf</code> 파일의 각 서비스 정의 필드 중 '플래그(Flag)' 항목에 작성되는 <code>wait</code> 옵션과 <code>nowait</code> 옵션의 작동상 차이점을 비동기적 트래픽 처리 관점에서 서술하시오.</summary>
<blockquote>
- <strong><code>nowait</code></strong>: 슈퍼 서버가 A 클라이언트로부터 접속 요청을 받아 하위 데몬을 실행해준 직후, 곧바로 대기 모드로 비동기 복귀하여 다른 클라이언트들의 새로운 요청 분기를 병렬로 동시 수신할 수 있다.<br>
- <strong><code>wait</code></strong>: 슈퍼 데몬이 들어온 현재 요청의 처리가 완벽히 종료될 때까지 Blocking(대기) 상태를 유지하여, 후속 요청을 받을 수 없게 구조화하는 옵션이다.
</blockquote>
</details>

<details>
<summary>(서술형) 시스템 강화 및 보안 감리의 일환으로 서버 점검 시, 흔히 'r-명령어(r-services)'로 불리는 <code>rlogin</code>, <code>rsh</code>, <code>rexec</code> 기능을 서비스 목록에서 반드시 퇴출(비활성화)하라고 권고하는 핵심적인 침해 보안 위험성을 기술하시오.</summary>
<blockquote>
이러한 구형 r-명령어 서비스들은 원격 연결 시, 비밀번호 기반의 강력한 사용자 검증 프로세스를 생략하거나 인증 절차 우회가 매우 용이한 IP 의존성 트러스트 구조를 띄고 있어, 해커의 무차별적인 접속이나 스푸핑(Spoofing) 기법에 의해 서버의 최고 권한이 손쉽게 넘어갈 확률이 매우 막대하기 때문이다.
</blockquote>
</details>

<details>
<summary>(작업형) CentOS/RedHat 리눅스 운영 서버의 <code>/etc/inetd.conf</code> 파일에 기록된 악성 DoS 취약 포트인 <code>chargen</code>, <code>echo</code> 등의 불필요한 테스트용 스트림 서비스가 구동 중이다. 관리자가 해당 설정 파일의 내용을 직접 편집하여 이들을 비활성화하려 한다면 어떠한 기호 기법을 써야 하는지 답안을 작성하시오.</summary>
<blockquote>
해당 서비스 설정이 기재된 텍스트 각 줄의 라인 맨 앞부분에 <strong>주석 기호(<code>#</code>)</strong>를 삽입하여, 시스템 데몬이 해당 환경설정을 실행 모듈로 인식하지 않도록 완전히 무시(주석 처리)하게 만들어야 한다.
</blockquote>
</details>

<details>
<summary>(작업형) 관리자가 불필요한 서비스들을 차단할 목적으로 <code>/etc/inetd.conf</code> 설정 파일 내에 <code>#</code> 마크를 추가하고 저장(Save)하고 빠져나왔다. 그러나 여전히 외부에서 취약 코드로 접속이 가능했다. 설정이 OS 커널 레벨 기능에 온전히 결합되게 하기 위해 관리자가 이어서 필수로 터미널에 내렸어야 할 누락된 후속 명령어 액션을 서술하시오.</summary>
<blockquote>
설정 파일 텍스트만 바뀌었을 뿐 백그라운드 램(메모리)에서 돌고 있는 inetd 프로세스 자체는 옛날 설정을 그대로 쥐고 있으므로, <strong><code>service inetd restart</code> 등의 프로세스 재시작(Restart) 명령어</strong>를 타건하거나 HUP 시그널을 보내 구성 파일을 메모리에 재갱신하도록 만들어야 한다.
</blockquote>
</details>

<details>
<summary>(작업형) <code>/etc/inetd.conf</code> 설정 파일을 점검하다 보니, 어떤 특정 서비스 줄의 2번째 필드인 소켓 타입(Socket Type)에 <code>stream</code> 이라는 표기가 아닌 <strong><code>dgram</code></strong> 이라는 단어가 명시되어 있는 것을 발견하였다. 이를 근거로 해당 서비스 모듈은 4계층 전송 통신 프로토콜 관점에서 <code>TCP</code>와 <code>UDP</code> 중 어떠한 계열의 서비스인지 판단하여 쓰시오.</summary>
<blockquote>
<strong>UDP 계열 프로토콜</strong> 서비스이다. (참고: <code>stream</code>은 TCP, 연결지향성 전송을 의미)
</blockquote>
</details>

##### 접근 통제(TCP Wrapper)

<details>
<summary>(단답형) TCP Wrapper 환경에서 특정 클라이언트의 접근 허용 및 차단을 판별할 때, 우선순위가 가장 높아 시스템 데몬이 무조건 <strong>제일 먼저 참조하여 검사</strong>하는 필터링 설정 파일의 절대 경로를 쓰시오.</summary>
<blockquote>
/etc/hosts.allow
</blockquote>
</details>

<details>
<summary>(서술형) 원격의 한 클라이언트(IP: 192.168.1.50)가 TCP Wrapper로 보호되는 SSH 포트에 접근을 요청했을 때, 데몬이 <code>hosts.allow</code>와 <code>hosts.deny</code>, 그리고 <code>Default Rule</code>을 거치며 최종 통과/차단 결정을 내리는 3단계 논리 프로세스를 서술하시오.</summary>
<blockquote>
1단계: 먼저 <code>hosts.allow</code> 파일을 조회하여 해당 IP가 등록되어 있으면 즉시 접근을 허용하고 검사를 종료한다.<br>
2단계: 1단계에서 일치 항목이 없다면 <code>hosts.deny</code>를 조회하여 존재할 경우 즉시 접근을 차단하고 튕겨낸다.<br>
3단계: 두 파일 어느 곳에도 등록된 룰이 없다면 기본 정책(Default)에 의해 <strong>접근을 자동으로 허용</strong>한다.
</blockquote>
</details>

<details>
<summary>(서술형) 기존의 <code>inetd.conf</code> 설정 파일에서 외부 클라이언트 접근을 TCP Wrapper 기반으로 제어하기 위해서는 6번째 필드(실행 경로) 값을 기존 본래 데몬(예: <code>/usr/sbin/in.telnetd</code>)에서 무조건 <code>/usr/sbin/tcpd</code>로 변경해야 한다. 이렇게 <strong>중간 껍데기(tcpd)</strong>를 씌우는 이유와 역할의 본질을 서술하시오.</summary>
<blockquote>
직접 데몬을 호출해버리면 클라이언트 IP를 검열할 틈이 없기 때문에, 가로채기 역할인 <code>tcpd</code>(TCP Wrapper 프로세스)를 먼저 구동시켜 <code>hosts.allow</code> 및 <code>hosts.deny</code>의 판단 로직을 거치게 한 뒤, 접근이 허가된 선별된 요청에 대해서만 실제 백엔드 오리지널 서비스 모듈(인수 필드)을 구동하기 위함이다.
</blockquote>
</details>

<details>
<summary>(작업형) 관리자가 TCP Wrapper의 <code>/etc/hosts.allow</code> 파일 한 줄에 <code>ALL: ALL EXCEPT in.telnetd : ALL</code> 이라는 보안 룰을 기입하였다. 전체 데몬을 기준으로 어떠한 접속 허용 효과가 초래되는지 그 의미를 기술하시오.</summary>
<blockquote>
특정 예외 처리된 부분인 <strong>telnet (<code>in.telnetd</code>) 서비스를 제외한 나머지 전 서비스 부문에 대해서 전 세계 모든 호스트(ALL)의 접근을 무의미하게 전면 개방(허용)</strong>한다. (바꿔 말해 telnet 접속에 대해서만은 이 파일에서 허용 룰을 부여받지 못한다.)
</blockquote>
</details>

<details>
<summary>(작업형) TCP Wrapper의 <code>hosts.deny</code> 파일에 <code>in.telnetd : 192.168.0.104 : twist /bin/echo "YOU ARE HACKER!"</code> 라는 탐지 룰을 박아두었다. 만약 블랙리스트 대상인 104번 PC가 서버로 텔넷 접근을 시도했을 때, 데몬 단에서 어떠한 차단 프로세스가 펼쳐지고 클라이언트 모니터 화면에는 무슨 결과가 나타나는지 기술하시오.</summary>
<blockquote>
서버는 즉각적으로 해당 소켓 연결의 접속을 거부(차단)할 뿐만 아니라, <code>twist</code> 처리 메커니즘에 의해 연결이 완전히 끊어지기 전 마지막 찰나에 <strong>"YOU ARE HACKER!"</strong> 라는 명시적인 에러 메시지를 104번 공격자 PC 화면 방향으로 직접 쏘아 보내어 출력시키고 강제 종료해 버린다.
</blockquote>
</details>

<details>
<summary>IP 관리 시스템에서 발전하여 MAC 기반 통제를 강화한 장비는?</summary>
<blockquote>
NAC (Network Access Control)<br>
- 주요 기능: 접근 제어 및 인증.
</blockquote>
</details>

##### xinetd 슈퍼 데몬

<details>
<summary>(단답형) 보안 강화를 위해 기존의 구형 <code>inetd</code> 방식을 버리고 <code>xinetd</code> 데몬으로 이전했을 때, 각 개별 서비스 설정 파일 내에서 <strong>이 서비스를 구동할지, 아니면 아예 백그라운드 구동에서 제외시킬지</strong> 결정짓는 최상단 블록 지시어 명칭을 쓰시오.</summary>
<blockquote>
disable
</blockquote>
</details>

<details>
<summary>(단답형) <code>xinetd</code> 데몬 운영 환경에서 외부발 DoS(서비스 거부) 공격이나 트래픽 유발 공격에 대비하여, <strong>'초당 연결될 수 있는 커넥션 개수'</strong>를 1차적으로 강제 임계치 제한을 걸어버리는 통제 지시어를 쓰시오.</summary>
<blockquote>
cps
</blockquote>
</details>

<details>
<summary>(서술형) <code>xinetd</code> 슈퍼 데몬은 자원 고갈 공격을 방어하기 위해 <code>instances</code> 와 <code>per_source</code> 라는 설정 지시자를 제공한다. 겉보기에 모두 트래픽/연결을 억제하는 기능 같지만, 그 통제 범위 측면에서 어떠한 구조적 방향 차이가 있는지 비교 서술하시오.</summary>
<blockquote>
- <strong>instances</strong>: 출발지가 어디든 상관없이, 이 <strong>서버 시스템 자체가 동시에 생성하여 연산 감당할 수 있는 전체 자식 프로세스(서버 개수)의 절대적 최대치 한도</strong>를 묶는 글로벌 제한이다.<br>
- <strong>per_source</strong>: <strong>동일한 단일 출발지(Source) IP 하나</strong>에서만 무도덕하게 여러 개의 연결 세션을 과도하게 맺으려 할 때, 해당 단일 IP의 진입 한도만을 독립적으로 타겟 제한하는 출발지(Source) 통제 기능이다.
</blockquote>
</details>

<details>
<summary>(작업형) 당신은 <code>xinetd</code> 방화벽 룰을 설계하고 있다. <strong>192.168.56.0/24 네트워크 대역</strong>(내부망)의 접근 전체는 허용하되, 그 역영 중 유독 감염이 확인된 <strong>192.168.56.110 단일 IP</strong> 하나만 핀셋으로 접근을 튕기도록 <code>xinetd</code> 서비스 설정 블록에 추가할 2줄의 보안 통제 코드를 차례대로 작성하시오.</summary>
<blockquote>
<code>only_from = 192.168.56.0/24</code><br>
<code>no_access = 192.168.56.110</code>
</blockquote>
</details>

#### PAM(장착형 인증 모듈, Pluggable Authentication Modules)

##### 개요

<details>
<summary>(단답형) 시스템 내에서 로그인, FTP 등 각종 애플리케이션의 인증을 동적으로 통합 관리하고 처리해주기 위해 리눅스가 제공하는 <strong>'장착형(조립형) 인증 모듈'</strong> 공유 라이브러리의 영문 약어(명칭)를 쓰시오.</summary>
<blockquote>
PAM (Pluggable Authentication Modules)
</blockquote>
</details>

<details>
<summary>(단답형) PAM을 활용하는 개별 애플리케이션들의 구체적인 설정 파일(예: <code>login</code>, <code>sshd</code>, <code>su</code> 등) 들이 위치하고 있는 시스템 내부의 <strong>디렉터리 절대 경로</strong>를 쓰시오.</summary>
<blockquote>
<code>/etc/pam.d</code>
</blockquote>
</details>

<details>
<summary>(단답형) PAM 설정 파일의 4가지 필드(type, control, module-path, module-argument) 구조 중, 패스워드 최소 길이 및 복잡도 설정 등 비밀번호 변경/설정 조건을 지정하는 유형의 <code>type</code> 필드 명칭을 영문으로 쓰시오.</summary>
<blockquote>
<code>password</code>
</blockquote>
</details>

##### PAM 을 사용한 인증 절차

<details>
<summary>(서술형) 애플리케이션 개발자가 사용자 인증 기능을 자체적으로 하드코딩하지 않고, PAM 라이브러리에 연동(Plug-in)시켰을 때 얻을 수 있는 <strong>'개발 및 시스템 운영 측면'에서의 주요 이점</strong>을 서술하시오.</summary>
<blockquote>
프로그램 소스 코드를 재수정하지 않고도 독립적인 인증 모듈을 개발/추가할 수 있으며, 시스템 관리자가 필요에 따라 유연하게 새로운 인증 체계(OTP, 생체인증 등)를 선택적으로 갈아 끼워 손쉽게 중앙 통제할 수 있는 막강한 장점이 있다.
</blockquote>
</details>

<details>
<summary>(서술형) PAM 설정 파일의 <code>type</code> 필드 중, <strong><code>auth</code></strong> 유형과 <strong><code>session</code></strong> 유형이 담당하는 각각의 인증 단계 및 구체적인 역할적 차이를 서술하시오.</summary>
<blockquote>
- <strong><code>auth</code></strong>: 패스워드 일치 확인이나 OTP 점검 등 실질적인 사용자의 암호가 맞는지 <strong>신원을 검사(인증)</strong>하는 핵심 역할을 한다.<br>
- <strong><code>session</code></strong>: 인증 처리 전후에 사용자의 홈 디렉터리를 마운트시키거나 메일함을 생성해주는 등 사용자와 시스템 간의 제반 <strong>환경을 수립</strong>시켜주는 사전 준비 및 사후 정리 역할에 중점을 둔다.
</blockquote>
</details>

<details>
<summary>(서술형) PAM 설정 파일의 <code>control</code> 필드에서 <strong><code>requisite</code></strong>와 <strong><code>required</code></strong> 플래그가 인증 <strong>실패 상황</strong>을 인지했을 때, 후속 모듈 처리 및 응답 시나리오 관점에서 어떻게 다르게 동작하는지 서술하시오.</summary>
<blockquote>
- <strong><code>requisite</code></strong>: 인증 모듈 검사가 실패하는 일체 그 즉시 인증을 바로 단절(거부)하고 에러를 밖으로 반환해 버린다.<br>
- <strong><code>required</code></strong>: 인증 모듈이 실패하더라도 해당 실패 상태를 내부적으로 조용히 쥐고만 있을 뿐, 설정 내의 <strong>남은 모듈들을 전부 끝까지 헛실행</strong>해 준 뒤에야 최종적으로 한꺼번에 인증 실패 판정을 내려서 공격자가 어느 단계나 모듈에서 막혔는지 힌트를 얻어채지 못하게 기만/방어한다.
</blockquote>
</details>

##### PAM 설정파일(/etc/pam.d/remote 설정파일 일부)

<details>
<summary>(작업형) 관리자가 PAM을 통해 특정 서비스 설정 파일에 한 줄을 기입하여, 계정의 암호 만료 기간이나 <code>nologin</code> 쉘 규칙 통제 등 '계정 자체가 가진 유효성'을 판단하고자 검사 모듈을 호출하였다. <code>[빈칸] required pam_nologin.so</code> 에 들어갈 올바른 <code>type</code> 지시어 텍스트를 작성하시오.</summary>
<blockquote>
<code>account</code>
</blockquote>
</details>

<details>
<summary>(작업형) <code>auth required pam_securetty.so</code> 라는 PAM 설정 라인이 있다. 이를 공백 기반으로 나뉘는 4가지 구문 형식 필드(<code>type</code>, <code>control</code>, <code>module-path</code>, <code>module-arguments</code>) 명칭에 각각 알맞게 매칭하여 하나하나 분석(명시)하여 작성하시오.</summary>
<blockquote>
- <strong>type</strong>: <code>auth</code><br>
- <strong>control</strong>: <code>required</code><br>
- <strong>module-path</strong>: <code>pam_securetty.so</code><br>
- <strong>module-arguments</strong>: (존재하지 않음, 생략)
</blockquote>
</details>

<details>
<summary>(작업형) PAM 설정 과정 중, 만약 이전까지의 라인 모듈들이 모두 성공했다는 전제하에 <strong>"이 라인의 특정 모듈 인증이 성공하기만 하면, 뒤에 남은 인증 절차들을 과감히 생략하고 즉시 전체 인증을 성공(Satisfy) 처리하여 검사를 조기 종료"</strong> 하도록 편의성 룰을 규정하는 매력적인 <code>control</code> 필드의 플래그 값을 쓰시오.</summary>
<blockquote>
<code>sufficient</code>
</blockquote>
</details>

##### PAM 활용 예 1 (시스템 취약점 분석, 평가 일부 항목)

<details>
<summary>(단답형) 시스템 보안 관점에서 공격자가 네트워크를 통해 원격으로 <code>root</code> 최고 관리자 권한을 직접 획득하는 것을 방지하기 위해, 리눅스가 <code>root</code> 사용자의 로그인 접속을 허용하는 "로컬 물리적 터미널(콘솔)" 목록을 별도로 기재하여 통제하는 설정 파일의 절대 경로를 쓰시오.</summary>
<blockquote>
/etc/securetty
</blockquote>
</details>

<details>
<summary>(단답형) 리눅스 환경에서 외부의 패스워드 무작위 대입 공격(Brute Force Attack)이나 사전 대입 공격 확률을 지연시키고 방어할 목적으로, 비밀번호를 연속으로 틀릴 시 계정을 임시로 잠그는(Lock) 기능을 수행하는 대표적인 PAM 모듈 파일명(확장자 포함)을 쓰시오.</summary>
<blockquote>
pam_tally2.so (또는 pam_tally.so)
</blockquote>
</details>

<details>
<summary>(단답형) 강력한 암호화 프로토콜인 SSH(Secure Shell)를 사용하더라도 공격 표면을 줄이기 위해 원칙적으로 <code>root</code> 계정의 직접적인 원격 로그인은 금지되어야 한다. 이를 강제하기 위해 <code>/etc/ssh/sshd_config</code> 파일에서 반드시 <code>no</code> 로 설정해 주어야 하는 지시어 명칭을 영문으로 쓰시오.</summary>
<blockquote>
PermitRootLogin
</blockquote>
</details>

<details>
<summary>(서술형) 시스템 관리자가 <code>/etc/securetty</code> 파일을 열고 그 안에 적힌 내용 중 <code>pts/0</code>, <code>pts/1</code> 등의 라인들을 전부 지우거나 주석(<code>#</code>) 처리하였다. 이렇게 <code>tty</code>는 남겨둔 채 <strong>가상 터미널(pts) 목록만을 골라 삭제 및 주석 처리한 보안 상의 본질적 이유</strong>를 터미널 개념과 묶어 서술하시오.</summary>
<blockquote>
<code>tty</code>는 관리자가 서버 앞 키보드로 직접 조작하는 안전한 로컬 콘솔 환경인 반면, <code>pts</code>는 외부 네트워크(Telnet, SSH 등 가상 터미널)를 다이렉트로 타고 접속하는 논리적 연결 통로이므로, 이 <code>pts</code> 목록을 지움으로써 외부자가 원격에서 직접 <code>root</code> 계정으로 로그인하는 보안 위협을 원천 봉쇄(거부)하기 위함이다.
</blockquote>
</details>

<details>
<summary>(서술형) PAM 계정 잠금 모듈인 <code>pam_tally2.so</code> 에 인자로 넘겨주는 <strong><code>deny=5</code></strong>와 <strong><code>unlock_time=120</code></strong> 설정이 서로 어떻게 연계되어, 단기간에 수많은 비밀번호를 찔러보는 무차별 공격으로부터 <strong>시스템의 인증 무결성</strong>을 매끄럽게 보호해 내는지 서술하시오.</summary>
<blockquote>
사용자가 패스워드 입력을 연속으로 5회 실패(deny=5)하는 순간 즉시 해당 유저 아이디를 잠그며(Lock), 그 마지막 실패 시점으로부터 정확히 120초(unlock_time=120초, 즉 2분)가 지나가야만 계정 잠금이 자동으로 풀리게 작동하여 암호 사전 대입을 시도하는 해커의 시간적 비용과 공격 주기를 대폭 지연시키는 보호막 역할을 한다.
</blockquote>
</details>

<details>
<summary>(서술형) 리눅스의 <code>pam_tally.so</code> (또는 <code>pam_tally2.so</code>) 모듈 설정 라인 끝부분에 기입할 수 있는 계정 통제 부가 옵션 중, <strong><code>no_magic_root</code></strong> 옵션과 <strong><code>reset</code></strong> 옵션이 가지고 있는 기능을 각각 어떠한 목적으로 제정해 둔 것인지 비교 서술하시오.</summary>
<blockquote>
- <strong><code>no_magic_root</code></strong>: 공격자가 시스템을 마비시킬 목적으로 <code>root</code> 아이디를 의도적으로 수백 번 틀리게 입력하여 최고 관리자 계정을 영원히 접속 불능 상태(DoS)로 빠뜨리는 것을 막기 위해, 오직 <code>root</code> 계정에게만큼은 아무리 실패해도 잠기지 않는 면책(예외) 적용을 부여한다.<br>
- <strong><code>reset</code></strong>: 실패가 누적되어 자칫 잠길 위기에 처했더라도 중간에 단 1번이라도 올바른 패스워드로 정상 로그인에 성공하면, 기존에 위험하게 쌓여있던 모든 '로그인 단기 실패 누적 횟수'를 즉각 0으로 깨끗하게 초기화하여 사용자 편의성을 보장해 준다.
</blockquote>
</details>

<details>
<summary>(작업형) 관리자가 정기 보안 점검 중 사내 사용자인 <code>kiwi99</code>가 2분간 계정이 잠긴 것을 발견하였다. 급하게 잠금을 뚫어주기 위해 특권 명령어를 이용해 <code>kiwi99</code> 계정의 누적 실패 카운트를 일자(Latest failure)와 함께 깔끔하게 <strong>조회(확인)함과 동시에 '0'으로 초기화명령(Reset)</strong>을 쉘 프롬프트에 연달아 한 번에 실행하고자 한다. 실패 횟수 통계를 담당하는 <code>pam_tally2</code> 기반의 명령어와 인수 플래그를 정확히 작성하시오.</summary>
<blockquote>
<code>pam_tally2 -u kiwi99 -r</code> (또는 <code>pam_tally2 -u kiwi99 --reset</code>)
</blockquote>
</details>

<details>
<summary>(작업형) 다음과 같이 PAM 시스템 인증(<code>/etc/pam.d/system-auth</code>) 모음 파일에 계정 잠금 정책 기능을 필수 절차로써 새롭게 추가하려고 한다. 문법의 빈칸에 알맞은 제어 텍스트 문구를 채워 넣어 설정을 온전히 완성하시오.
<code>auth [빈칸] pam_tally2.so deny=5 unlock_time=120</code></summary>
<blockquote>
<code>required</code>
</blockquote>
</details>

<details>
<summary>(작업형) 관리자가 침해 징후를 판별하기 위해 <code>/var/log/secure</code> 로깅 파일의 꼬리 부분을 점검하던 중 다음과 같은 흔적을 발견하였다.
<code>FAILED LOGIN 1 FROM 192.168.197.1 FOR kiwi99, Authentication failure</code>
<code>pam_tally2 (remote:auth): user kiwi99 (500) tally 6, deny 5</code>
이 두 줄의 로그 덩어리가 연속으로 발생한 의미를 '연결 시도의 출발지', '대상 계정', 그리고 '인증 모듈의 작동 최종 결과'의 세 가지 포인트 관점으로 해석하여 서술하시오.</summary>
<blockquote>
192.168.197.1 이라는 위치(출발지)에서 시스템 내에 있는 <code>kiwi99</code> 계정(대상)으로 접속을 인증하려다가 비밀번호가 틀려 1회 실패 기록이 남았으며, 결과적으로 이 누적으로 인해 최종 실패 횟수(tally)가 '6번'에 도달함으로써, 사전에 PAM 모듈 규칙으로 제한해둔 잠금 임계치 조건(deny=5회 초과)을 넘겨버려 <strong>해당 <code>kiwi99</code> 계정이 보안상 강제로 잠금(Account Locked) 조치</strong>되었다는 의미이다.
</blockquote>
</details>

##### PAM 활용 예 2 (시스템 취약점 분석, 평가 일부 항목: su 명령어 사용 제한)

<details>
<summary>(단답형) 권한이 없는 일반 사용자가 무작위 대입 방식을 통해 <code>root</code> 권한을 탈취하는 것을 사전에 차단하기 위해, 오로지 이 특수 그룹에 속한 관리 인원들에게만 <code>su</code> 명령어를 통한 권한 상승을 허용하도록 통제하는 리눅스의 <strong>대표적 관리자 그룹 명칭</strong>을 쓰시오.</summary>
<blockquote>
wheel
</blockquote>
</details>

<details>
<summary>(단답형) PAM 환경에서 <code>/etc/pam.d/su</code> 설정 파일을 통해, <code>su</code> 명령어를 치고 들어오려는 사용자가 지정된 특정 그룹(예: wheel) 소속자인지를 판별하여 인증 권한을 내주는(또는 거부하는) <strong>핵심 플러그인 모듈 파일명(확장자 포함)</strong>을 쓰시오.</summary>
<blockquote>
pam_wheel.so
</blockquote>
</details>

<details>
<summary>(단답형) 터미널 프롬프트에서 시스템 설정 파일 편집 없이, 기존 사용자인 <code>algisa</code> 계정을 <code>wheel</code> 이라는 보조 그룹 속성으로 '덮어씌우지 않고 추가(Append)' 편입시키기 위해 사용하는 <strong><code>usermod</code> 명령어의 대문자 옵션</strong>을 쓰시오.</summary>
<blockquote>
<code>-G</code> (전체 구문 예시: <code>usermod -G wheel algisa</code>)
</blockquote>
</details>

<details>
<summary>(서술형) PAM을 활용하여 <code>su</code> 명령어의 사용을 <code>wheel</code> 그룹으로 철저히 제한(<code>pam_wheel.so</code> 활성화)해 두었다. 이때 <code>wheel</code> 그룹에 들어있지 않은 일반 사용자(예: <code>kiwi99</code>)가 터미널에서 <code>su -</code> 를 치고 <strong>완벽하게 정확한 <code>root</code> 마스터 비밀번호를 알아내 제대로 입력</strong>했다면, 쉘 내부적으로 어떠한 거부 로직과 보안 결과가 벌어지는지 서술하시오.</summary>
<blockquote>
패스워드를 아는 것과 무관하게 PAM의 <code>pam_wheel.so</code> 그룹 검증 모듈 단계에서 자격 미달로 막혀버린다. 터미널에는 고의를 띤 <code>"su: incorrect password"</code> 등의 인증 실패 에러를 띄워 <code>root</code> 권한 상승을 강제로 즉시 차단하며, 백그라운드의 <code>/var/log/secure</code> 로깅 파일에 그룹 권한 부족으로 인한 인증 거부(Access denied) 내역을 남긴다.
</blockquote>
</details>

<details>
<summary>(서술형) <code>/etc/pam.d/su</code> 파일의 보안 통제 로직 중 <code>auth required pam_wheel.so use_uid</code> 라는 구문에서 마주치는 <strong><code>use_uid</code> 인자</strong>가 플러그인 내부에서 수행하는 구체적인 검증 역할과 보안 원리를 서술하시오.</summary>
<blockquote>
<code>su</code>를 요청한 현재 터미널 세션 사용자의 실제 고유 <code>UID</code> 정보를 긁어와, 남의 권한을 사칭한 상태가 아닌 본인 스스로가 <code>wheel</code> 그룹 명단 호적에 정식으로 맵핑(포함)되어 있는지를 엄격하고 견고하게 교차 체크하도록 강제하는 보안용 트리거 옵션이다.
</blockquote>
</details>

<details>
<summary>(서술형) 리눅스와는 궤가 다른 HP-UX나 AIX 등 일부 상용 유닉스 운영체제 계열에서는, PAM 모듈에 전적으로 의존하기보다 근본적인 구조에서 <code>su</code> 명령어의 무분별한 사용을 억제하는 공통된 접근법을 쓴다. 파일 시스템 퍼미션(Permission) 관점에서 이들이 어떠한 보안 점검 원리를 취하는지 서술하시오.</summary>
<blockquote>
자체 보안 설정 파일(예: <code>user</code>, <code>security</code> 등)의 특정 옵션을 활용해 직접 권한 그룹을 묶어둘 뿐만 아니라, 파일 시스템 구조상 <strong><code>/usr/bin/su</code> 나 <code>/bin/su</code> 실행 파일 자체에 부여된 권한을 <code>4750</code> (-rwsr-x---) 등의 형태로 아예 깎아내려</strong> 일반 기타 사용자 계층(Others)은 해당 실행 파일의 호출(접근) 자체를 근원적으로 할 수 없도록 통제하는 방식을 쓴다.
</blockquote>
</details>

<details>
<summary>(작업형) 관리자가 CLI 명령어 툴(<code>usermod</code>)을 쓰지 않고 <code>vi</code> 텍스트 편집기만을 이용해 직접 시스템 설정 파일을 제어하여 일반 사용자 <code>algisa</code>를 <code>wheel</code> 그룹에 편입시키고자 한다. 관리자가 <strong>에디터로 열어야 할 파일의 전체 절대경로</strong>와, 해당 파일 <strong>해석 포맷의 맨 마지막 필드에 조치해야 할 구체적 텍스트 편집 액션</strong>을 한 줄로 쓰시오.</summary>
<blockquote>
<code>/etc/group</code> 시스템 파일을 열어 <code>wheel:x:10:root</code> 로 끝나는 해당 라인 맨 가장자리 필드 끝에 콤마(<code>,</code>)를 붙이고 <code>algisa</code> 계정을 추가로 문열어 적어주면 된다. (예: <code>wheel:x:10:root,algisa</code>)
</blockquote>
</details>

<details>
<summary>(작업형) 어떤 사용자가 관리 포트에 접속하자마자 본인의 그룹을 타진하고자 <code>id kiwi99</code> 명령어를 쳤고, 그 결과 <code>uid=500(kiwi99) gid=508(channel) groups=500(kiwi99),508(channel)</code> 이 출력되었다. <code>PAM pam_wheel</code> 통제가 활성화된 서버라는 전제 조건을 바탕으로, <strong>이 사용자가 <code>su</code> 타건 시 최고 권한을 탈취해 낼 수 있는지 가능성과 그 물리적 근거</strong>를 <code>groups</code> 출력 텍스트를 이용해 판단하여 쓰시오.</summary>
<blockquote>
권한 상승 불가(탈취 불가)하다. <code>groups</code> 필드 결과 목록에 속해 있는 500, 508번 채널 외에 특권을 허락해 주는 단서인 <code>10(wheel)</code> 그룹이 아예 존재하지 않아 물리적으로 걸러지기 때문이다.
</blockquote>
</details>

<details>
<summary>(작업형) 서버 관리자가 <code>/etc/pam.d/su</code> 설정 파일을 열어 보았더니 최상단 첫 줄에 <code>auth sufficient pam_rootok.so</code> 라는 조건 검사 코드가 존재했고, 이 상태에서 저장(wq!)하였다. 이 <strong>단 하나의 모듈 조건 행</strong>이 제대로 가동함으로써 시스템 상에 부여되는 '권한 인증 면책(프리패스)'의 마법 같은 효력과 상황을 서술하시오.</summary>
<blockquote>
현재 <code>su</code> 전환을 요청하는 주체의 권한이 이미 가장 최고 신뢰도 등급인 <strong>'root' 본인이라면</strong>, 다른 하위의 어떤 사용자 계정으로 이동할 때 비밀번호를 일일이 묻고 확인하는 절차 등 뒷줄의 모든 <code>auth</code> 모듈 과정을 생략(Sufficient 조기 만족)하고 <strong>암호 기입의 방해 없이 즉각적으로 계정 스위치를 통과(허용)</strong>하게 해주는 프리패스 효력을 지닌다.
</blockquote>
</details>

##### PAM 활용 예 3 (시스템 취약점 분석, 평가 일부 항목: sudo 명령을 이용한 관리자 권한 부여)

<details>
<summary>(단답형) 다른 사용자의 권한(일반적으로 root)으로 시스템의 특정 명령어를 임시로 실행하고자 할 때, 보안을 위해 널리 사용되는 리눅스의 특권 상승 명령어 명칭을 쓰시오.</summary>
<blockquote>
sudo
</blockquote>
</details>

<details>
<summary>(단답형) 시스템 관리자가 특정 일반 사용자나 그룹에게 <code>sudo</code> 권한을 개별적으로 할당하고 제어하기 위해 직접 정책을 기입하는 시스템 내부 설정 파일의 절대 경로를 쓰시오.</summary>
<blockquote>
/etc/sudoers
</blockquote>
</details>

<details>
<summary>(단답형) <code>sudoers</code> 파일에 정책을 기술할 때, 명령어 실행 인가자는 맞지만 스케줄러나 자동화 스크립트에서 활용할 수 있도록 <strong>실행 시 패스워드를 묻는 프롬프트를 완전히 생략</strong>해버리는 옵션 키워드를 영문으로 쓰시오.</summary>
<blockquote>
<code>NOPASSWD:</code>
</blockquote>
</details>

<details>
<summary>(서술형) 시스템 보안 운영 관점에서, 권한 상승 시 <code>su</code> 명령어를 쓰지 않고 굳이 <strong><code>sudo</code> 명령어의 사용을 실무적으로 권장하는 두 가지 핵심적인 근본 이유</strong>를 서술하시오.</summary>
<blockquote>
첫째, 관리자(root)의 마스터 비밀번호가 무엇인지 다수의 일반 사용자들에게 절대 직접 알려주거나 공유하지 않아도 된다.<br>
둘째, '최소 권한의 원칙'에 입각하여 해당 사용자가 업무에 꼭 필요한 일부 명령어들만 root 권한으로 핀셋 지정하여 제한적으로 허용(통제)할 수 있기 때문이다.
</blockquote>
</details>

<details>
<summary>(서술형) <code>sudoers</code> 파일에 <code>sudo</code> 기능을 개별 사용자 1명이 아니라, '시스템의 특정 그룹(예: devGroup)에 소속된 구성원 전체'에게 한 번에 일괄 부여하려 할 때, 가장 앞단의 '계정명' 필드를 문법적으로 어떻게 작성해야 하는지 그 규칙을 서술하시오.</summary>
<blockquote>
아이디(계정명)를 적는 위치에, 해당 명칭이 '그룹명'임을 시스템이 인식할 수 있도록 앞에 반드시 <strong>퍼센트 기호(<code>%</code>)</strong>를 접두사로 붙여서 기입해야 한다. (작성 예: <code>%devGroup</code>)
</blockquote>
</details>

<details>
<summary>(서술형) 터미널 프롬프트에서 <code>sudo -u algisa /batch/batch.sh</code> 와 같이 명령을 실행하였다. 플래그 없이 사용했던 기존의 기본적인 <code>sudo</code> 동작 방식과 비교하여 쉘 내부의 권한 승격 대상(Target)이 어떻게 달라지는지 서술하시오.</summary>
<blockquote>
아무 옵션이 없을 때는 무조건 시스템 최고 권한인 'root' 계층으로 권한이 올라가 구동되지만, <strong><code>-u</code> (User) 옵션을 명시</strong>하고 계정명(algisa)을 주었기 때문에, 저 스크립트를 돌리는 동안만큼은 최고 관리자가 아니라 <strong>'algisa' 라는 다른 일반 사용자의 제한된 권한으로 한정되어 위임(실행)</strong>된다.
</blockquote>
</details>

<details>
<summary>(작업형) 관리자가 보안 정책을 위반하고 어떠한 제약도 없이 <code>kiwi99</code> 계정이 모든 호스트(서버 접속)에서, root를 포함한 모든 유저의 권한으로, 모든 명령어를 다 타이핑할 수 있도록 <code>sudoers</code> 파일에 허용 구문을 1줄 새로 개통하려고 한다. 포맷(계정명 호스트=(실행권한계정) 명령어)에 맞추어 작성하시오.</summary>
<blockquote>
<code>kiwi99 ALL=(ALL) ALL</code>
</blockquote>
</details>

<details>
<summary>(작업형) 운영팀의 <code>dev01</code> 계정이 <code>/batch/log_batch.sh</code> 파일을 root 권한으로 매일 밤 스케줄링(자동화) 실행하려 한다. 이를 위해 <code>dev01 ALL=(root) /batch/log_batch.sh</code> 룰이 잡혀있는데 이대로 두면 야간에 멈춰서 암호를 입력하라고 프롬프트가 대기하게 된다. 암호 입력을 우회하여 무정지 실행이 되게끔 해당 설정 문구의 중간을 수정해 보시오.</summary>
<blockquote>
<code>pwd</code> 패스워드 생략 플래그를 정해진 위치에 삽입하여 무정지로 통과시킨다.<br>
수정 답안: <code>dev01 ALL=(root) NOPASSWD: /batch/log_batch.sh</code>
</blockquote>
</details>

<details>
<summary>(작업형) 외부 감사자가 시스템을 점검하다 누군가 고의로 <code>sudoers</code> 파일 맨 아랫줄에 <code>ALL ALL=(ALL) ALL</code> 이라는 극도로 위험한 줄을 한 줄 끼워 넣은 것을 발견했다. 구문 구조 상의 빈칸 4가지(계정, 호스트, 실행 주체, 허용 파일)에 대응시켜, 이 설정이 시스템에 미치고 있는 현재의 치명적 파급 효과(의미)를 논리적으로 서술하시오.</summary>
<blockquote>
서버에 존재하는 무수히 많은 <strong>'모든 일반 로그인 계정(ALL)'</strong>이 로그인한 <strong>'모든 서버망(ALL)'</strong> 위에서 <strong>'그 누구의 권한(ALL)'</strong>으로든지 전환할 수 있으며 심지어 <strong>'시스템 내부의 어떠한 명령어 및 파일 실행(ALL)'</strong>까지 제약 없이 모두 가능하다는 뜻으로, 사실상 방어막이 완전히 붕괴되어 아무나 터미널에서 전체 관리자 행세를 할 수 있게 뚫어버린 파멸적 백도어 상황이다.
</blockquote>
</details>

##### PAM 활용 예 4 (시스템 취약점 분석, 평가 일부 항목: sudo 실무 권한 심화)

<details>
<summary>(단답형) <code>/was/batch/log_batch.sh</code> 쉘 스크립트의 소유자와 권한이 <code>-rwx------ root root</code> 로 설정되어 있다. 일반 계정인 <code>algisa</code>가 단순히 터미널에서 <code>/was/batch/log_batch.sh</code> 라고 다이렉트로 입력하여 실행을 시도했을 때, 모니터에 출력되는 <strong>가장 전형적인 리눅스 터미널의 권한 거부 영문 에러 메시지</strong>를 그대로 쓰시오.</summary>
<blockquote>
Permission denied
</blockquote>
</details>

<details>
<summary>(단답형) 위 상황에서 <code>algisa</code> 계정이 <code>sudo /was/batch/log_batch.sh</code> 라고 명령어를 쳤음에도 불구하고 <strong>"algisa is not in the sudoers file. This incident will be reported"</strong> 라는 오류가 출력되었다면, 시스템 보안 관점에서 <code>algisa</code> 계정이 관리자로부터 어떠한 필수 설정 파일에 등재되지 못했기 때문인지 그 파일의 명칭을 쓰시오.</summary>
<blockquote>
/etc/sudoers (또는 sudoers 파일)
</blockquote>
</details>

<details>
<summary>(단답형) <code>sudoers</code> 파일에 <code>algisa ALL=(root, kiwi99, kiwi88) ALL</code> 이라는 설정이 기입되어 있다. 이 상태에서 터미널 접속 관리자가 <code>algisa</code> 계정일 때, <code>sudo -u [특정사용자] cat ~/.bash_profile</code> 구문에서 <code>[특정사용자]</code> 자리에 올 수 없는 계정을 하나 예를 들면 누구인지(명시된 3명 이외) 적으시오.</summary>
<blockquote>
(예시) kiwi77 혹은 명시되지 않은 아무 계정 (해당 룰은 오직 root, kiwi99, kiwi88 세 명으로의 전환만을 허용하기 때문)
</blockquote>
</details>

<details>
<summary>(서술형) <code>sudo</code> 명령어를 사용하여 관리자 권한이 필요한 스크립트를 최초 실행하려고 하면 터미널에 <code>"sudo password for algisa:"</code> 라는 프롬프트가 등장한다. 이 프롬프트가 요구하고 있는 <strong>비밀번호의 진짜(본래) 주인</strong>이 누구인지 시스템 보안 권한 증명(신뢰성) 관점에서 서술하시오.</summary>
<blockquote>
이 프롬프트에서 시스템이 요구하는 암호는 최종 획득하려는 목표인 'root'의 패스워드가 아니라, <strong>현재 <code>sudo</code> 통제기를 마주하고 타이핑을 치고 있는 '본인(즉, algisa 사용자)'의 고유 로그인 비밀번호</strong>이다. 권한을 빌려 쓰기 전에 네가 진짜 algisa가 맞는지 본인 확인(인증) 절차를 거치는 것이다.
</blockquote>
</details>

<details>
<summary>(서술형) <code>sudoers</code> 파일에 부여된 <code>ALL=(ALL) ALL</code> 옵션과 <code>ALL=(ALL) NOPASSWD: ALL</code> 옵션의 실무적 적용 목적과 동작의 차이를 관리자 접근 편리성(자동화) 측면에서 비교 서술하시오.</summary>
<blockquote>
기본 <code>ALL</code>의 경우 명령마다 지속적으로 본인의 비밀번호를 검증받아야 하므로 터미널 대화형 사용에 머무는 반면, <strong><code>NOPASSWD: ALL</code></strong>을 부여하게 되면 모든 권한 스위칭 과정에서 패스워드 검증 절차가 완전히 생략(면제)되므로, 사용자가 쉘 프로비저닝이나 <strong>야간 배치(Batch) 스크립트 등 무인 자동화 작업을 중간 멈춤(블로킹) 없이 원활하게 돌릴 수 있도록 해주는 중대한 차이</strong>가 있다.
</blockquote>
</details>

<details>
<summary>(서술형) 특정한 보안 프로젝트 팀(개발자)인 <code>algisa</code>에게 다른 모든 서버망 명령어 접근은 차단하고, 오직 로컬 장비 내부 1대의 쉘에서 특정 보안 로그 출력기만 관리자급으로 제어하도록 최소 권한 위임을 셋업했다. <code>algisa 192.168.56.100=(ALL) ALL</code> 설정과 <code>algisa ALL=(ALL) /was/batch/log_batch.sh</code> 설정의 권한 박탈 및 제한 방향의 차이점을 서술하시오.</summary>
<blockquote>
전자는 <strong>'장소(호스트명/IP)'</strong>를 철저히 제한하여 무조건 <code>192.168.56.100</code> 서버 상에서만 sudo를 치도록 가두어 놓은 접속망 기반 통제이고, 후자는 접속 장소가 어디든 상관하지 않는 대신 <strong>'실행 가능한 명령어(프로그램)' 종류</strong>를 오직 <code>/was/batch/log_batch.sh</code> 단 한 개 파일로만 극단적으로 압축해 통제하는 행위 기반의 제한 기법이다.
</blockquote>
</details>

<details>
<summary>(작업형) 현재 호스트 PC(로컬)의 터미널이다. 신입 관리자인 <code>algisa</code> 계정이 <code>visudo</code> 명령으로 <code>sudoers</code> 파일을 수정하여, 자기가 소유한 아이디일 경우 <strong>비밀번호를 치지 않고(NOPASSWD) 모든 호스트망에서 root 권한으로 자유롭게 <code>/was/batch/log_batch.sh</code> 파일을 실행</strong>할 수 있도록 맞춤형 룰 한 줄을 작성하려 한다. 포맷에 맞춰 정확한 명령어 텍스트 라인을 완성하시오.</summary>
<blockquote>
<code>algisa ALL=(root) NOPASSWD: /was/batch/log_batch.sh</code> (또는 <code>algisa ALL=(ALL) NOPASSWD: /was/batch/log_batch.sh</code>)
</blockquote>
</details>

<details>
<summary>(작업형) <code>/etc/sudoers</code> 파일에 다음과 같은 룰이 세팅되어 있다.
<code>algisa ALL=(root, kiwi99) ALL</code>
이때 터미널에서 <code>algisa</code> 계정이 자신의 <code>sudo</code> 권한을 이용해 일반 사용자 <code>kiwi77</code>의 <code>~/.bash_profile</code> 파일을 <code>cat</code> 명령어로 읽어보려는 커맨드를 1줄로 작성하고, 그 엔터(Enter) 결과가 시스템 로그 상 어떻게 처리될지 결론 지어 작성하시오.</summary>
<blockquote>
커맨드: <code>sudo -u kiwi77 cat ~kiwi77/.bash_profile</code><br>
결론: <code>sudoers</code> 파일 룰셋에 허용된 스위칭 대상자가 <code>root</code>와 <code>kiwi99</code> 단 2명뿐이므로, 그 외의 인물인 <code>kiwi77</code>로의 전환(권한 대행)은 시스템에 의해 철저하게 <strong>실패(차단) 및 오류("Sorry, user algisa is not allowed...")</strong>를 뱉어내고 접근이 거절된다.
</blockquote>
</details>

<details>
<summary>(작업형) 사용자 <code>kiwi99</code> 계정에게, 자신의 비밀번호를 한 번 입력하여 신원 인증만 거치고 나면 192.168.1.100 번 서버에서 <code>/bin/kill</code> 명령어를 관리자(root) 권한으로 타건할 수 있도록 통제 룰을 부여해야 한다. 설정 파일에 들어갈 적합한 1줄짜리 정규 문법(포맷) 코드를 작성하시오.</summary>
<blockquote>
<code>kiwi99 192.168.1.100=(root) /bin/kill</code> (또는 <code>(ALL) /bin/kill</code>)
</blockquote>
</details>

#### 시스템 로그 설정과 관리

##### 개요

##### 유닉스/리눅스 주요 로그 파일

<details>
<summary>(단답형) 리눅스는 <code>/var/log</code> 디렉터리, 유닉스는 <code>/var/adm</code> 디렉터리에 주로 시스템 로그를 남기는데, 이처럼 시스템에서 남기는 여러 종류의 시스템 로그 파일들의 고정적인 <strong>최종 저장 위치 파일명(경로)을 정의해두고 배포해 주는 환경 설정 파일명(절대경로)</strong>을 쓰시오.</summary>
<blockquote>
/etc/syslog.conf (또는 최신 리눅스의 경우 /etc/rsyslog.conf)
</blockquote>
</details>

<details>
<summary>(단답형) 현재 시스템에 <strong>로그인하여 활동 중인 사용자들의 실시간 접속 상태 정보</strong>를 담고 있는 바이너리 로그 파일로서, <code>w</code>, <code>who</code>, <code>finger</code>, <code>users</code> 명령어 등을 타이핑했을 때 이 파일의 데이터를 읽어와 모니터에 뿌려주는 핵심 원천 파일의 절대 경로를 쓰시오 (Linux 기준).</summary>
<blockquote>
/var/run/utmp (Unix 계열은 /var/adm/utmpx)
</blockquote>
</details>

<details>
<summary>(단답형) 해커가 서버에 지속적으로 접근하기 위해 백도어를 심거나 비밀번호를 알아내고자 <strong>무작위 대입을 시도하다가 누적시킨 모든 '로그인 실패(Failed login)' 기록들</strong>을 담아두는 리눅스 바이너리 파일명(절대경로)을 쓰시오.</summary>
<blockquote>
/var/log/btmp
</blockquote>
</details>

<details>
<summary>(서술형) 리눅스 터미널에서 <code>w kiwi99</code> 명령어를 쳤더니, 열 출력 결과 제일 우측의 <strong><code>WHAT</code> 필드</strong>에 <code>-bash</code> 라는 문구 대신 <code>/usr/bin/vi /etc/passwd</code> 라고 출력되어 있었다. 이 <code>WHAT</code> 필드의 문구가 시스템 운영자(점검자)에게 시사하는 보안 통제 관점에서의 의미를 서술하시오.</summary>
<blockquote>
<code>WHAT</code> 필드는 접속한 사용자가 터미널 위에서 '지금 당장 어떠한 명령어 및 프로세스 작업'을 수행하고 있는지를 실시간으로 보여주는 감시 지표다. 이 문구가 떴다는 것은 <code>kiwi99</code> 계정이 일반적인 쉘 대기 상태(bash)가 아니라 <strong>현재 시스템 계정 정보가 담긴 중요한 환경 파일(<code>/etc/passwd</code>)을 텍스트 에디터(vi)로 열어 수정 또는 열람을 시도하고 있다는 중대한 보안 감시 의미</strong>를 시사한다.
</blockquote>
</details>

<details>
<summary>(서술형) 시스템 침해 사고 발생 시 침투 범위를 분석하기 위해 <code>lastlog</code> 명령어를 수행했다. <code>lastlog</code> 파일이 텍스트(Text) 파일이 아닌 <strong>바이너리(Binary) 포맷으로만 저장되어 관리되는 결정적인 보안상의 이유(목적)</strong>를 파일 무결성 관점에서 서술하시오.</summary>
<blockquote>
바이너리(이진) 형태로 저장하면 관리자가 제공하는 특정 전용 명령어(예: <code>lastlog</code>, <code>last</code>, <code>lastb</code> 등)를 거치지 않고서는 내용을 인간이 읽거나 쉽게 편집기(vi, nano 등)로 고칠 수 없기 때문에, <strong>공격자가 시스템에 침투한 뒤 텍스트 편집기로 자신의 악성 접속 IP 기록만을 정교하게 한 줄씩 지우거나 조작하는 흔적 은폐 행위를 1차적으로 방어(무결성 보장)</strong>하기 위함이다.
</blockquote>
</details>

<details>
<summary>(서술형) SunOS(Solaris)와 같은 유닉스 계열에서 악의적 로그인 시도 실패 기록을 남기는 <code>loginlog</code> 파일은, 1회라도 실패하면 무조건 다 로그에 적어두는 리눅스의 <code>btmp</code> 시스템과 비교하여 <strong>어떠한 조건적 차이(기록 발동 조건)</strong>를 갖고 동작하는지 서술하시오.</summary>
<blockquote>
리눅스는 단 1번이라도 비밀번호를 틀리면 <code>btmp</code>에 족족 실패 이력을 누적하지만, 유닉스(SunOS)의 <code>/var/adm/loginlog</code> 파일 체계는 <strong>동일한 사용자가 연속해서 '5회 이상' 로그인을 연달아 실패했을 경우에 한해서만</strong> 비로소 이상 징후로 판단하여 그 실패 내역 전체를 텍스트로 밀어 넣(기록하)는 차이점을 가지고 있다.
</blockquote>
</details>

<details>
<summary>(작업형) 관리자가 정기 점검을 위해 현재 서버로 실시간 다이렉트 접근해 들어오는 불법 로그인 루트를 점검하려 한다. 수십 개의 <code>utmp</code> 데이터를 모두 열람하는 대신, 시스템 부팅부터의 이력이 담긴 <code>wtmp</code> 를 기반으로 하여 <strong>재부팅(reboot) 관련 정보만을 최근 이력부터 단 5줄로 예쁘게 잘라서 보고자 한다.</strong> 이를 터미널에 한 줄로 조립하여 출력하는 CLI 명령어(파이프 활용)를 정확히 명시하시오.</summary>
<blockquote>
<code>last reboot | head -5</code> (또는 <code>last reboot | head -n 5</code>)
</blockquote>
</details>

<details>
<summary>(작업형) 인사팀과 보안팀의 정기 퇴사자 계정 말소 절차를 위해 <strong>모든 시스템 등록 사용자를 통틀어 <code>kiwi99</code> 라는 특정 1개의 계정이 가장 마지막(최근)에 성공적으로 로그인했던 날짜 일시 기록만을 뽑아서 조회</strong>하려 한다. 이 정보를 읽어내기 위한 <code>lastlog</code> 명령어와 타겟 지정 인자 포맷 라인을 명령어 형태로 정확하게 작성하시오.</summary>
<blockquote>
<code>lastlog -u kiwi99</code>
</blockquote>
</details>

<details>
<summary>(작업형) 시스템 백그라운드 환경에 <code>/var/log/btmp</code> 침해 로그 파일이 거대하게 쌓여가고 있다. 관리자가 현재 악의적으로 무차별 대입(Brute-Force)을 던지고 있는 외부 해커가 어떤 타겟팅 아이디들을 찌르고 있는지 분석하기 위해, 이 <strong>바이너리 로그인 실패 기록 파일을 텍스트 형태로 디코딩하여 볼 수 있도록 쉘 프롬프트에서 치는 기본 복원 열람 명령어</strong> 하나를 명시하시오 (Linux 전용).</summary>
<blockquote>
<code>lastb</code>
</blockquote>
</details>

<details>
<summary>(단답형) 유닉스(SunOS) 시스템 환경에서, 어떤 사용자가 다른 사용자의 권한으로 넘어가려 시도했던 특정 명령어(<code>su</code>)의 성공 및 실패 내역을 문자열 기호로 기록해두는 텍스트 로그 파일의 <strong>절대 경로</strong>를 쓰시오.</summary>
<blockquote>
/var/adm/sulog
</blockquote>
</details>

<details>
<summary>(단답형) 리눅스 환경에서 시스템 데몬들의 구동 상태, 커널과 네트워크 인터페이스의 로드 정보, TCP Wrapper 통제 상태 등 <strong>시스템 운영 전반에 대한 핵심적인 통합 메시지</strong>들을 수집하여 포괄적으로 저장하는 텍스트 로그 파일의 <strong>절대 경로</strong>를 쓰시오.</summary>
<blockquote>
/var/log/messages
</blockquote>
</details>

<details>
<summary>(단답형) 사용자가 시스템에 로그인한 순간부터 로그아웃할 때까지 입력했던 모든 명령어와 터미널 종류, 프로세스 시작 시간 등을 이진(Binary) 형태로 압축해둔 리눅스 <code>pacct</code>(또는 유닉스 <code>pacct</code>) 파일 정보를, 쉘 프롬프트에 <strong>텍스트로 복원하여 읽어내 표시해 주는 명령어</strong>를 쓰시오.</summary>
<blockquote>
lastcomm
</blockquote>
</details>

<details>
<summary>(서술형) 유닉스의 <code>sulog</code> 로그 텍스트를 파싱(분석)하던 중, <code>SU 02/28 00:49 - pts/4 kiwi88-root</code> 라는 일련의 라인들을 다수 발견하였다. 중간에 표기된 기호 <strong><code>-</code></strong> 과 그 뒤의 <strong><code>kiwi88-root</code></strong> 가 정확히 어떤 행위 내역을 지시하는지 해석하고, 이것이 보안 관점에서 어떠한 위협 상황을 시사하는지 서술하시오.</summary>
<blockquote>
중간의 <code>-</code> 기호는 권한 상승을 위한 <code>su</code> 명령이 실패(권한 거부 또는 패스워드 오입력)했음을 뜻한다. 조합해 보면, 터미널(pts/4)을 통해 접속한 일반 권한의 <code>kiwi88</code> 계정이 지속적으로 시스템 최고 관리자인 <code>root</code> 계정으로의 전환을 무단 시도하다가 실패하고 있는, 즉 <strong>관리자 권한 강제 탈취(해킹 시도)가 이뤄지고 있을 가능성이 높은 매우 중대한 보안 위협 징후</strong>를 시사한다.
</blockquote>
</details>

<details>
<summary>(서술형) 서버 관리자는 종종 침해 대응뿐만 아니라 커널 패닉 등 딥다이브한 물리적 오류를 파악하기 위해 리눅스의 <code>/var/log/dmesg</code> 파일을 점검한다. 해당 파일 안에 담겨있는 <strong>데이터의 근원적 출처와 수집 범위</strong>가 무엇인지 시스템 아키텍처 관점에서 서술하시오.</summary>
<blockquote>
운영체제(리눅스)가 가장 처음 <strong>재부팅(Booting)될 때 커널(Kernel)이 직접 인식하고 적재하는 디스크, 메모리, 네트워크 카드 등 하드웨어 디바이스들의 상태 확인 및 오류 메시지들 일체</strong>를 모두 기록해 놓은 근원이기 때문에, 부팅 과정 모니터링 시 스크롤되어 지나가 버린 치명적 커널 에러 내역 등을 나후에 텍스트 형태로 추적 및 트러블슈팅할 목적으로 쓰인다.
</blockquote>
</details>

<details>
<summary>(서술형) 리눅스의 <code>/var/log/secure</code> 파일은 보안 감사 시 가장 1순위로 지목되는 요충지이다. 해당 로그 파일이 서버 내부의 <strong>'결정적인 인증 이벤트'</strong>들을 어떻게 관제하고 있는지 그 대표적인 기록 대상 행동들을 세 가지 이상 나열하여 서술하시오.</summary>
<blockquote>
단순한 앱 실행 로그가 아닌 철저히 <strong>'계정 및 권한'에 밀접한 핵심 인증 내역</strong>만을 전담한다. 대표적으로 ① 백도어를 남기는 시스템 계정/그룹의 신규 생성 및 삭제 상태, ② 외부에서 접근하는 원격 터미널 접속(텔넷, SSH)의 성공 및 실패 내역, ③ 관리자로 빙의하는 <code>su</code> 및 <code>sudo</code> 명령어의 수행 승인 및 실패 내역 등을 중앙에 수집하여 세밀하게 기록한다.
</blockquote>
</details>

<details>
<summary>(작업형) 계정 침해 이력을 점검하기 위해 보안 담당자가 <code>messages</code> 파일을 검색하던 중, <code>Mar 3 21:15:14 localhost xinetd[2178]: START: telnet pid=3902</code> 라는 한 줄을 식별하였다. 리눅스의 표준 <strong>메시지 로그 배열 5단 구성 형식(Format)</strong> 규칙에 대입하여, 위 문장을 공백을 기준으로 쪼갰을 때 나타나는 독립된 5가지 정보(토큰)들이 각각 시계열의 어떤 값을 상징하는지 순서대로 매칭하여 작성하시오.</summary>
<blockquote>
① <code>Mar 3 21:15:14</code>: 로그 메시지 생성 일자 및 시각<br>
② <code>localhost</code>: 로그 메시지를 생성시킨 호스트(통신 서버) 이름<br>
③ <code>xinetd</code>: 로그 메시지를 실제 발생시킨 주체 데몬(프로세스/서비스) 이름<br>
④ <code>[2178]</code>: 로그 메시지를 발생시킨 프로세스의 고유 ID 번호 (PID)<br>
⑤ <code>START: telnet pid=3902</code>: 해당 프로세스가 구동 결과로서 터미널에 남긴 실제 발생 메시지 본문
</blockquote>
</details>

<details>
<summary>(작업형) 의심스러운 사용자 <code>kiwi99</code>가 특정 서버에 침투한 뒤 흔적을 인멸하려 본인의 계정 홈 디렉터리 내에 남아있는 과거 CLI 실행 내역(History)을 교묘하게 삭제하려 한다. 관리자가 이를 사전에 방지하고자, <strong>텍스트 편집기를 열지 않고 오로지 해당 유저 디렉터리에 놓인 숨김 타깃 파일(<code>.bash_history</code>) 내용 중 맨 꼭대기(상단) 5줄 부분만을</strong> 즉석에서 잘라서 터미널 화면에 던지기 위해 쓰는 파이프라인(CLI) 읽기 명령어 1줄을 완성하시오.</summary>
<blockquote>
<code>cat .bash_history | head -5</code> (또는 <code>cat .bash_history | head -n 5</code>)
</blockquote>
</details>

<details>
<summary>(작업형) 리눅스 서버에서, 공격자가 시스템 커맨드를 무결하게 남기는 <code>pacct</code> 로거가 돌아가는 중에도 악성 바이너리를 켰다 강제 종료한 심증이 있다. 불법 악용이 의심되는 단일 특정 사용자인 <code>kiwi99</code> 계정이 <strong>과거부터 지금까지 실행하고 거쳐간 유틸리티 명령어 히스토리만을 모두 출력기 상에 나열해 보기 위해</strong> 필터링을 조립하는 명령어를 영문으로 작성하시오.</summary>
<blockquote>
<code>lastcomm kiwi99</code>
</blockquote>
</details>

<details>
<summary>(단답형) 리눅스 서버에서 주로 파일 송수신 전용 서비스(FTP, vsftpd, proftpd)를 통해 <strong>누가 언제 접속해서 어떤 디렉터리 경로의 파일을 얼만큼의 바이트 크기로 업로드·다운로드 해갔는지</strong>를 고스란히 담아두는 로그 파일명(절대 경로)을 적으시오.</summary>
<blockquote>
/var/log/xferlog
</blockquote>
</details>

<details>
<summary>(단답형) 예약된 시간에 반복적으로 자동화 스크립트나 명령들을 실행시켜 주는 작업 스케줄링 데몬이 남기는 흔적으로, <strong>언제 어떠한 설정(배치) 파일이 권한별로 실행을 시작하고 성공적으로 마쳤는지에 대한 내역</strong>을 관찰할 수 있는 파일명(절대경로)을 적으시오.</summary>
<blockquote>
/var/log/cron
</blockquote>
</details>

<details>
<summary>(단답형) Sendmail 등과 같은 MTA 데몬 시스템과 밀접하게 연동되어, <strong>서버에서 발송되거나 외부 서버로부터 수신된 이메일 패킷의 처리 과정(성공 및 Access denied 에러 등)</strong>을 순서대로 남겨두어 스팸 릴레이나 메일 위변조를 판별하는 용도로 쓰는 파일명을 적으시오.</summary>
<blockquote>
/var/log/maillog
</blockquote>
</details>

<details>
<summary>(서술형) 리눅스의 <code>/var/log/boot.log</code> 파일과 앞서 서술했던 <code>/var/log/dmesg</code> 시스템 파일을 비교 설명해보라. 두 파일 모두 '가동 시간(부팅)'에 관여하지만 <strong>결정적으로 '어느 영역의 로그를 담당하느냐'</strong> 하는 목적에 큰 차이가 있다. 이를 커널과 서비스 관점에서 비교하여 서술하시오.</summary>
<blockquote>
<code>dmesg</code>가 <strong>시스템의 최하단인 커널(운영체제)이 하드웨어(CPU, 네트워크 어댑터 등)를 찾아내고 적재하는 저수준(디바이스) 과정</strong>과 메세지를 기록하는 곳이라면, <code>boot.log</code>는 그 하드웨어가 다 켜진 이후 리눅스의 시작 스크립트(init/systemd)가 올라가면서 <strong>실질적인 응용 프로그램 데몬들(SSH, FTP, HTTP 등)이 정상 구동(OK)되었는지, 혹은 실패(FAILED)했는지의 상위 서비스 제어 상태</strong>를 남기는 곳이라는 목적의 차이가 있다.
</blockquote>
</details>

<details>
<summary>(서술형) 서버의 <code>xferlog</code> 파일 기록 중 <code>a _ o a algisa ftp 0 * c</code> 라는 포맷 행을 발견하였다. 맨 뒤에서부터 5개 필드 항목들 <code>(o a algisa ftp 0 * c)</code>이 FTP 데이터 송수신 상호작용에서 <strong>순서대로 각각 무엇을 지시하고 있는지</strong>를 해석 서술하시오.</summary>
<blockquote>
① <code>o (outgoing)</code>: 서버에서 파일이 외부로 유출(다운로드)되었다는 방향성<br>
② <code>a (anonymous)</code>: 정규 로컬 권한(r)이 아닌 익명 계정으로 접속했다는 접근 모드<br>
③ <code>algisa</code>: 실제로 로그인 시 타이핑 제출한 사용자의 문자열 이름<br>
④ <code>ftp</code>: 해당 로그를 남긴 주체 서비스의 명칭<br>
⑤ <code>0 * c</code>: 인증 방식(0: 없음), 인증 유저ID 사용여부(*), 최종적으로 파일 전송이 성공적으로 완료(c: complete)되었음을 뜻함
</blockquote>
</details>

<details>
<summary>(서술형) 인사 정보 연동 배치 쉘 스크립트가 매일 새벽 4시에 수행되도록 잘 셋업(crontab)해 두었는데 어느 날부터 파일이 동기화되지 않고 있다. 당신은 시스템 엔지니어로써 가장 먼저 <code>/var/log/cron</code>을 열었다. <strong>이 파일에서 반드시 마주해야만 하는, 하지만 에러로 인해 보이지 않을 수도 있는 '특정 구문 및 실행 징후 패턴' 두 가지 구성요소</strong>가 무엇인지 서술하시오.</summary>
<blockquote>
첫째, 설정해둔 '새벽 4시(04:00)'라는 시각 언저리에 데몬이 시작(started)을 알리는 타임스탬프 기록이 정상적으로 찍혀 있는지 여부와,<br>
둘째, 정규 크론 양식인 <code>CMD (/배치경로/쉘파일.sh)</code> 혹은 <code>finished</code> 형태의 실행 구문이 관리자(root) 권한 등을 업고 구체적인 작업 스택 메시지로 출력되어 남았는지를 중점적으로 확인해야 한다.
</blockquote>
</details>

<details>
<summary>(작업형) 서버 관리자가 외부로부터 익명의 해커가 FTP 포트로 다가와 사내의 주요 기술문서(바이너리) 파일들을 무단으로 퍼가고 있는(다운로드) 이상 유출 정황을 의심하고 있다. 보안 감사자가 <strong>이러한 FTP 무단 파일 다이렉트 유출(Outgoing) 흔적만을 빠르게 선별해 내기 위해</strong> 터미널 창에서 <code>xferlog</code> 파일을 상대로 던지는 텍스트 필터형(grep) 읽기 명령어 파이프라인 구조를 작성하시오.</summary>
<blockquote>
<code>cat /var/log/xferlog | grep " o "</code> (파일 다운로드(outgoing)를 상징하는 방향성 지시자 'o'를 기준으로 검색한다. 띄어쓰기를 주어 문맥을 한정하는 것이 좋다.)
</blockquote>
</details>

<details>
<summary>(작업형) 특정 사용자의 비밀번호 변경 완료 메일이 수신처(외부 스팸메일사)로 날아가지 않고 계속 튕기거나 실패 중이라는 민원이 제기되었다. 메일 데몬이 <code>Access denied</code>(수신 거부/접근 통제) 처리 당한 실제 원인 로그 행위를 잡기 위해, <strong>관리자가 실시간으로 계속 쌓이고 뒷단에 추가되는 이메일 로깅 상태를 끊이지 않고 터미널 모니터에서 계속 바라보며 감시할 수 있게 해 주는</strong> 동적 열람 명령어 풀 텍스트(옵션 포함)를 쓰시오.</summary>
<blockquote>
<code>tail -f /var/log/maillog</code>
</blockquote>
</details>

<details>
<summary>(작업형) 리눅스 서버가 재부팅될 때마다 네트워크 컨트롤러 데몬(NetworkManager)이 알 수 없는 원인으로 자꾸 <code>[ FAILED ]</code> 사인을 출력하며 서비스 적재에 실패한다는 심증이 섰다. 무수한 로그들이 다 지나가 버린 터미널 환경에서, <strong>재부팅 관련 어플리케이션 데몬 상태가 텍스트로 적히는 그 한 개의 특정 로그 파일에 <code>FAILED</code> 라는 문자열이 존재하는지만 쏙 뽑아 확인하려 한다.</strong> 이를 위한 명령어 조합 라인을 정확히 기재하시오.</summary>
<blockquote>
<code>grep FAILED /var/log/boot.log</code> (또는 <code>cat /var/log/boot.log | grep FAILED</code>)
</blockquote>
</details>

#### syslog 설정 및 관리

##### 개요

#### 리눅스 로그 관리

### 5. 시스템 해킹

<details>
<summary>파일 무결성 검사 기능 및 접근 제어를 제공하며, 루트킷(Rootkit) 감염 여부나 파일 시스템의 변경 사항을 주기적으로 모니터링하여 관리자에게 알림을 제공하는 대표적인 오픈소스 기반 침입 탐지 도구(HIDS)의 명칭과 그 탐지 원리를 서술하시오.</summary>
<blockquote>
<strong>명령 및 도구</strong>: 트립와이어 (Tripwire)<br>
<strong>탐지 원리</strong>: 사전에 시스템 내 중요 파일들의 해시(Hash) 값을 계산하여 데이터베이스에 저장해 둔 뒤, 주기적으로 현재 파일들의 해시 값을 재계산하여 원래의 데이터베이스 값과 비교함으로써 위·변조 여부를 탐지한다.
</blockquote>
</details>

#### 버퍼 오버플로우 공격(Buffer Overflow Attack)

<details>
<summary>파일 무결성 검사 기능 및 접근 제어를 제공하며, 루트킷(Rootkit) 감염 여부나 파일 시스템의 변경 사항을 주기적으로 모니터링하여 관리자에게 알림을 제공하는 대표적인 오픈소스 기반 침입 탐지 도구(HIDS)의 명칭과 그 탐지 원리를 서술하시오.</summary>
<blockquote>
<strong>명령 및 도구</strong>: 트립와이어 (Tripwire)<br>
<strong>탐지 원리</strong>: 사전에 시스템 내 중요 파일들의 해시(Hash) 값을 계산하여 데이터베이스에 저장해 둔 뒤, 주기적으로 현재 파일들의 해시 값을 재계산하여 원래의 데이터베이스 값과 비교함으로써 위·변조 여부를 탐지한다.
</blockquote>
</details>

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
