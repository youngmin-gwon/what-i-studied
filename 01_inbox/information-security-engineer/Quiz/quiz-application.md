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

### DNS(Domain Name Server)

### HTTP(HyperText Transfer Protocol)

### FTP(File Transfer Protocol)

<details>
<summary>(단답형) 파일 전송 프로토콜 중 <code>FTP</code>보다 단순하며 별도의 인증 절차가 없어 보안에 취약하지만, 부팅 파일 전송 등에 사용되는 프로토콜의 명칭을 쓰시오.</summary>
<blockquote>
<code>TFTP</code> (Trivial File Transfer Protocol)
</blockquote>
</details>

### SNMP(Simple Network Management Protocol)

### DHCP(Dynamic Host Configuration Protocol)

## [8] 웹 애플리케이션 취약점

### SQL Injection 취약점

<details>
<summary>(서술형) <code>SQL 인젝션(Injection)</code> 공격 중 'Blind SQL Injection'의 개념을 설명하고, 이를 탐지하기 위해 공격자가 주로 사용하는 SQL 함수 2가지를 쓰시오.</summary>
<blockquote>
개념: 쿼리 결과가 화면에 직접 노출되지 않는 경우, 참(True) 또는 거짓(False)의 응답 차이나 응답 지연 시간 등을 통해 데이터베이스의 정보를 유추해 나가는 공격 기법이다.<br>
사용 함수: <code>SUBSTR()</code> (문자열 추출), <code>LENGTH()</code> (문자열 길이 확인), <code>SLEEP()</code> (시간 지연 유도) 등.
</blockquote>
</details>

<details>
<summary>(단답형) 데이터베이스에서 사용자의 입력값을 통해 동적으로 SQL 쿼리를 생성할 때 발생하는 <code>SQL Injection</code> 취약점을 근본적으로 방어하기 위해, 많은 프로그래밍 언어의 데이터베이스 접근 API 라이브러리가 지원하는 객체(클래스)의 명칭을 쓰시오.</summary>
<blockquote>
<code>PreparedStatement</code> (또는 Parameterized Query)
</blockquote>
</details>

### XSS(Cross Site Scripting) 취약점

<details>
<summary>(단답형) 사용자의 입력값을 적절히 필터링하지 못해 악성 스크립트가 실행되는 <code>XSS</code> 공격 중, 게시판 등에 스크립트를 저장하여 지속적으로 피해를 입히는 방식의 명칭을 쓰시오.</summary>
<blockquote>
Stored XSS (저장형 XSS)
</blockquote>
</details>

### CSRF(Cross Site Request Forgery) 취약점

<details>
<summary>(서술형) 크로스 사이트 스크립팅(XSS) 공격과 크로스 사이트 요청 위조(CSRF) 공격의 차이점을 '공격 대상'과 '목적' 측면에서 비교하여 서술하시오.</summary>
<blockquote>
<strong>XSS</strong>: 공격 대상은 '클라이언트(사용자)'이며, 사용자의 브라우저에서 악성 스크립트를 실행시켜 세션 쿠키를 탈취하거나 악성 사이트로 리다이렉트 시키는 것이 목적이다.<br>
<strong>CSRF</strong>: 공격 대상은 '서버(애플리케이션)'이며, 인증된 사용자의 권한을 도용하여 공격자가 의도한 행위(비밀번호 변경, 송금 등)를 서버에 요청하고 실행하게 만드는 것이 목적이다.
</blockquote>
</details>

### Server-Side Request Forgery(SSRF) 취약점

### 운영체제 명령 실행(OS Command Execution) 취약점

### 파일 업로드 취약점

### 파일 다운로드 취약점

### 경로 추적(Path Traversal) 취약점

<details>
<summary>(단답형) 공격자가 웹 통신 과정에서 전달되는 파라미터나 헤더 값 등을 조작하여, 다른 사용자의 디렉터리나 민감한 시스템 파일(예: <code>/etc/passwd</code>)에 무단으로 접근하고 이를 열람하는 웹 뷰어 취약점 공격의 명칭을 영소문자 약어로 쓰시오.</summary>
<blockquote>
<code>lfi</code> (Local File Inclusion) 또는 <code>pdt</code> (Path Directory Traversal)
</blockquote>
</details>

### 파일 삽입 취약점

### URL/파라미터 변조 취약점

### 불충분한 세션 관리 취약점

<details>
<summary>(단답형) OWASP Top 10에 포함되는 취약점 중 하나로, 공격자가 웹 애플리케이션의 파라미터를 조작하여 자신에게 허가되지 않은 다른 사용자의 데이터(예: <code>Mypage?id=admin</code>)나 기능에 직접 접근할 수 있도록 허용하는 취약점의 영문 약어를 쓰시오.</summary>
<blockquote>
<code>IDOR</code> (Insecure Direct Object Reference)
</blockquote>
</details>

### 정보누출 취약점

### 기타 웹 애플리케이션 취약점

### 개발 보안관리

<details>
<summary>(단답형) C언어에서 문자열 복사 시 대상 버퍼의 크기를 검사하지 않아 버퍼 오버플로우를 유발할 수 있는 취약한 함수인 <code>strcpy</code>를 대체하여, 지정된 길이(n)만큼만 문자열을 안전하게 복사하도록 권장되는 함수의 명칭을 쓰시오.</summary>
<blockquote>
<code>strncpy</code> (또는 <code>strlcpy</code>)
</blockquote>
</details>

<details>
<summary>(서술형) 안드로이드 애플리케이션 보안을 위해 소스코드 난독화(Obfuscation)를 수행해야 하는 이유를 리버스 엔지니어링(Reverse Engineering) 관점에서 설명하시오.</summary>
<blockquote>
안드로이드 앱은 디컴파일 도구를 통해 실행파일(<code>.apk</code>)을 소스코드로 쉽게 변환할 수 있어 로직 분석이 용이하다. 난독화는 변수명이나 메서드명을 무의미하게 변경하거나 코드 흐름을 복잡하게 만들어, 공격자가 화이트박스 분석을 통해 취약점을 찾아내거나 소스코드를 도용하는 리버스 엔지니어링 시도를 어렵게 하기 위해 반드시 필요하다.
</blockquote>
</details>

<details>
<summary>(서술형) 안드로이드 애플리케이션 보안을 위해 소스코드 난독화(Obfuscation)를 적용할 때의 기대 효과와, 난독화만으로는 완벽한 보안을 담보할 수 없는 한계점을 서술하시오.</summary>
<blockquote>
<strong>기대 효과</strong>: 디컴파일을 통해 소스코드를 복원하더라도 클래스명이나 변수명 등이 암호화/축약되어 있어 공격자가 로직을 분석하고 취약점을 파악하는 데 걸리는 시간과 비용을 크게 증가시킬 수 있다.<br>
<strong>한계점</strong>: 난독화는 코드를 읽기 어렵게 만들 뿐이지 실행 파일 자체가 암호화되는 것은 아니며 취약점 자체를 제거하는 것이 아니므로, 시간과 노력을 들인 구조 분석이나 런타임 메모리 분석 등을 통해 결국 역공학(Reverse Engineering)이 가능하다는 한계가 있다.
</blockquote>
</details>

<details>
<summary>(단답형) 안드로이드 앱의 필수 권한 선언 및 앱 구성 정보를 담고 있는 설정 파일의 명칭을 작성하시오.</summary>
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
<summary>(단답형) 웹 사이트의 루트 디렉터리에 위치하며, 검색 엔진의 웹 크롤러(로봇)가 접근해도 되는 페이지와 접근해서는 안 되는 페이지(관리자 페이지 등)를 명시하여 검색 노출을 제어하는 표준 파일의 명칭을 쓰시오.</summary>
<blockquote>
<code>robots.txt</code>
</blockquote>
</details>

### 기타 웹서버 보안 대책(아파치 기준)

### 웹 로그 분석

### Security Server 구축

## [10] 이메일(E-mail) 보안

### 이메일 시스템 구조

### SMTP 메일 형식

### 메일서버(sendmail) 보안 설정

### 이메일 인증 기술(스팸 메일 방지 기술)

<details>
<summary>(단답형) 최근 랜섬웨어 메일이나 악성 문서 파일 공격을 방어하기 위해 도입되는 기술로, 유입되는 파일에서 문서 구조만 추출하고 스크립트나 매크로 등 위협이 될 수 있는 요소들을 제거한 뒤 안전한 형태(PDF 등)로 재조합하여 내부로 반입하는 기술의 영문 약어를 쓰시오.</summary>
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
