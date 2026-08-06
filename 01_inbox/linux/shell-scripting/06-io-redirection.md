---
title: 06-io-redirection
tags: [bash, io, linux, redirection, shell]
aliases: []
date modified: 2025-12-28 22:30:49 +09:00
date created: 2025-12-28 20:44:41 +09:00
---

## 06. 표준 입출력, 리디렉션, 파이프

데이터의 흐름을 제어하는 표준 스트림과 리디렉션, 그리고 명령들을 연결하는 파이프라인의 원리를 다룹니다.

### 1. 표준 스트림 (Standard Streams)

| 스트림 | 파일 디스크립터 (FD) | 설명 |
| :--- | :---: | :--- |
| **stdin** | 0 | 표준 입력 (키보드 등) |
| **stdout** | 1 | 표준 출력 (터미널 화면) |
| **stderr** | 2 | 표준 에러 (터미널 화면, 에러 전용) |

### 2. 리디렉션 연산자 (Redirection)

| 연산자 | 방향 | 설명 |
| :--- | :---: | :--- |
| `>` | output | 파일로 출력 (기존 내용 **덮어쓰기**) |
| `>>` | output | 파일 끝에 내용 **추가 (Append)** |
| `<` | input | 파일의 내용을 입력으로 사용 |
| `2>` | error | 표준 에러만 따로 파일로 출력 |
| `&>` | both | 표준 출력과 에러를 한꺼번에 리디렉션 (Bash) |
| `2>&1` | both | stderr 을 stdout 이 향하는 곳으로 보냄 |

### 3. 히어독 및 히어스트링 (Here-doc/string)

| 구분 | 문법 | 특징 |
| :--- | :--- | :--- |
| **Here-doc** | `<<EOF … EOF` | 여러 줄의 텍스트를 입력으로 전달 (변수 확장됨) |
| **Quoted Here-doc** | `<<'EOF' … EOF` | 텍스트를 리터럴 그대로 전달 (**변수 확장 안 됨**) |
| **Here-string** | `<<< "$var"` | 단일 변수/문자열을 한 줄 입력으로 전달 (Bash) |

### 4. 파이프라인 (Pipelines)
- **문법**: `cmd1 | cmd2 | cmd3`
- **특징**: `cmd1` 의 stdout 이 `cmd2` 의 stdin 으로 연결됩니다.
- **종료 코드**: 기본적으로 마지막 명령(`cmd3`)의 결과만 반영되나, `set -o pipefail` 설정 시 중간 실패를 감지할 수 있습니다.

### 5. 프로세스 대체 (Process Substitution)

Bash 전용 기능으로, 명령의 결과를 파일처럼 취급할 수 있게 합니다.

|    기호    | 설명                       | 예시                                   |
| :------: | :----------------------- | :----------------------------------- |
| `<(cmd)` | 명령의 출력을 입력 파일처럼 사용       | `diff <(ls dir1) <(ls dir2)`         |
| `>(cmd)` | 파일에 쓰는 출력 대신 명령의 입력으로 전달 | `cmd \| tee >(grep ERROR > err.log)` |

### 6. 주요 가상 장치 (/dev/null, /dev/zero)

리디렉션 시 매우 자주 활용되는 특수 파일들입니다.

| 장치 (Device) | 별칭 | 역할 및 활용 | 예시 |
| :--- | :--- | :--- | :--- |
| **`/dev/null`** | **Black Hole** | 모든 입력을 버리고, 읽으면 즉시 종료됨 | `cmd > /dev/null 2>&1` (모든 출력 숨기기) |
| **`/dev/zero`** | **Zero Filler** | 읽을 때마다 0(NULL) 값을 무한히 제공 | `dd if=/dev/zero of=file bs=1M count=10` (10MB 빈 파일 생성) |

---
### 🔗 연결 문서
- [05-functions](05-functions.md) - 함수 및 모듈화
- [07-text-processing](07-text-processing.md) - 텍스트 처리 툴킷
