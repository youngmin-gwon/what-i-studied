---
title: 04-control-flow
tags: [bash, control-flow, linux, shell]
aliases: []
date modified: 2025-12-28 20:54:26 +09:00
date created: 2025-12-28 20:44:34 +09:00
---

## 04. 조건문, 제어 구조, 종료 코드

스크립트의 흐름을 제어하는 조건식과 반복문, 그리고 프로그램의 성공 여부를 알리는 종료 코드 설계 방법을 다룹니다.

### 1. 테스트 표현식 (Test Expressions)

Bash 에서는 세 가지 방식의 테스트를 지원합니다.

| 구분 | 문법 | 특징 |
| :--- | :---: | :--- |
| **Standard Test** | `[ expr ]` | POSIX 호환, 공백 필수, 단어 분리/글로브 발생 |
| **Extended Test** | `[[ expr ]]` | Bash 전용, 패턴(`==`) 및 정규식(`=~`) 매칭 지원, 안전함 |
| **Arithmetic Test** | `(( expr ))` | 산술 연산 결과 평가 (0 이 아니면 참) |

#### 1.1 주요 비교 연산자

| 구분 | 연산자 | 의미 |
| :--- | :--- | :--- |
| **문자열** | `-z str` / `-n str` | 빈 문자열인지 / 비어 있지 않은지 확인 |
| | `str1 == str2` | 두 문자열이 같은지 확인 |
| **파일** | `-e` / `-f` / `-d` | 존재 여부 / 일반 파일 / 디렉터리 확인 |
| | `-r` / `-w` / `-x` | 읽기 / 쓰기 / 실행 권한 확인 |
| | `-s` | 파일 크기가 0 보다 큰지 확인 |
| **숫자** | `-eq` / `-ne` | 같다 / 다르다 |
| | `-lt` / `-gt` | 작다 / 크다 |
| | `-le` / `-ge` | 작거나 같다 / 크거나 같다 |

### 2. 제어 구조 (Control Structures)

| 구문 | 형식 및 특징 |
| :--- | :--- |
| **if 문** | `if [ 조건 ]; then … elif [ 조건 ]; then … else … fi` |
| **case 문** | `case $VAR in pat1) … ;; pat2|pat3) … ;; *) … esac` |
| **for 문** | `for x in 리스트; do … done` (리스트 반복) <br> `for ((i=0; i<n; i++)); do … done` (C 스타일) |
| **while 문** | `while [ 조건 ]; do … done` (조건이 참인 동안 반복) |
| **until 문** | `until [ 조건 ]; do … done` (조건이 참이 될 때까지 반복) |
| **select 문** | 사용자의 메뉴 선택을 받는 루프 (입력값은 `$REPLY` 에 저장) |

### 3. 루프 제어 및 특수 제어

| 명령어 | 설명 |
| :--- | :--- |
| **break [n]** | 루프를 즉시 탈출 (n 은 중첩 레벨) |
| **continue [n]** | 현재 반복을 건너뛰고 다음 반복 시작 |
| **shift [n]** | 위치 매개변수($1, $2…)를 왼쪽으로 이동시킴 |

### 4. 종료 코드 설계 (Exit Codes)

| 코드 | 관례적 의미 |
| :---: | :--- |
| **0** | 성공 (Success) |
| **1** | 일반 실패 (General Error) |
| **2** | 사용법 오류 (Usage Error/Misuse) |
| **126** | 실행 불가 (Command invoked cannot execute) |
| **127** | 명령 없음 (Command not found) |

---

### 🔗 연결 문서

- [[03-variables-arrays]] - 변수 및 배열 활용
- [[05-functions]] - 함수 및 모듈화
