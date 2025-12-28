---
title: shell-scripting
tags: [bash, index, linux, scripting, shell]
aliases: []
date modified: 2025-12-28 22:26:44 +09:00
date created: 2025-12-28 20:11:14 +09:00
---

## 리눅스 셸 스크립팅 통합 가이드

이 페이지는 Bash 및 POSIX 셸 스크립팅에 관한 모든 문서들을 구조적으로 연결하는 중앙 허브입니다.

### 1. 기초 및 핵심 문법 (Core Syntax)

| 번호 | 문서명 | 주요 내용 |
| :---: | :--- | :--- |
| **00** | [[00-intro]] | 가이드 구성 의도 및 학습 팁 |
| **01** | [[01-overview]] | 셸 역할, 로딩 순서, 명령어 해석 단계 |
| **02** | [[02-expansions]] | 셸 확장 우선순위, 인용(Quoting) 규칙 |
| **03** | [[03-variables-arrays]] | 특수 변수, 문자열 연산, 배열 및 연관 배열 |

### 2. 실행 흐름 및 데이터 제어 (Flow & Data)

| 번호 | 문서명 | 주요 내용 |
| :---: | :--- | :--- |
| **04** | [[04-control-flow]] | 조건문(if/case), 반복문(for/while), 종료 코드 |
| **05** | [[05-functions]] | 함수 정의, 지역 변수, getopts 옵션 파싱 |
| **06** | [[06-io-redirection]] | 표준 스트림, 리디렉션 상세, 히어독, 파이프 |
| **07** | [[07-text-processing]] | grep, sed, awk, coreutils 활용 텍스트 가공 |
| **08** | [[08-process-control]] | 잡 제어, 주요 시그널, trap 을 이용한 자원 정리 |

### 3. 운영 환경 및 최적화 (Environment & Ops)

| 번호 | 문서명 | 주요 내용 |
| :---: | :--- | :--- |
| **09** | [[09-environment-startup]] | PATH 관리, 시작 스크립트, Cron 및 스케줄러 |
| **10** | [[10-debugging-style]] | set 옵션 디버깅, ShellCheck, 스타일 가이드 |
| **11** | [[11-security-performance]] | 입력 검증 보안, 성능 튜닝, GNU/BSD 포터빌리티 |
| **12** | [[12-recipes]] | 필수 스니펫, POSIX 대안, 최종 체크리스트 |

### 4. 실전 대비 및 참조 레퍼런스 (Exam & Reference)

| 번호 | 문서명 | 주요 내용 |
| :---: | :--- | :--- |
| **13** | [[13-mock-exam-qa]] | 핵심 Q&A, 시나리오 해결, 빈출 패턴 |
| **14** | [[14-command-reference]] | 내장 명령 및 텍스트 필터 옵션 사전 |
| **15** | [[15-lab-walkthroughs]] | 단계별 실습 랩(1~10) 가이드 |
| **16** | [[16-troubleshooting-cookbook]] | 흔한 에러 메시지 원인 및 해결책 |
| **17** | [[17-shell-options]] | set/shopt 옵션 심층 분석 |
| **18** | [[18-case-studies]] | 실무 케이스 스터디 및 표준 템플릿 |

### 5. 마무리 및 보충 자료

| 번호 | 문서명 | 주요 내용 |
| :---: | :--- | :--- |
| **19** | [[19-quick-review]] | 시험 직전 초압축 회독 노트 |
| **20** | [[20-command-drills]] | 손에 익히는 커맨드 드릴 세트 |
| **21** | [[21-posix-compat]] | POSIX sh 호환성 가이드 |
| **Roadmap** | [[study-guide]] | 1 주 완성 집중 학습 로드맵 |

---

>[!TIP]
> **Bash 4.x/5.x** 기능을 적극적으로 활용하되, 배포용 스크립트는 **21 번 POSIX 가이드**를 참조하여 호환성을 확보하세요.
