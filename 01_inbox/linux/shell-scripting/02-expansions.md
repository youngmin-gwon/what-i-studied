---
title: 02. 명령, 인용, 확장 규칙
tags: [linux, shell, bash, expansion]
---

# 02. 명령, 인용, 확장 규칙

셸이 명령을 해석할 때 적용하는 인용(Quoting) 규칙과 단계별 확장(Expansion) 프로세스를 정리합니다.

## 1. 셸 확장 순서 (Expansion Order)

셸은 반드시 아래 순서대로 확장을 수행하므로 우선순위 이해가 중요합니다.

| 순서 | 확장 종류 | 예시 |
| :---: | :--- | :--- |
| **1** | **브레이스 확장 (Brace Expansion)** | `a{b,c}` → `ab ac` |
| **2** | **틸드 확장 (Tilde Expansion)** | `~` → `/home/user` |
| **3** | **파라미터/변수 확장 (Parameter Expansion)** | `$VAR`, `${VAR:-default}` |
| **4** | **명령 치환 (Command Substitution)** | `$(date)`, `` `ls` `` |
| **5** | **산술 확장 (Arithmetic Expansion)** | `$((1+1))` → `2` |
| **6** | **프로세스 대체 (Process Substitution)** | `<(ls)`, `>(grep)` (Bash전용) |
| **7** | **단어 분리 (Word Splitting)** | `$IFS` 기준 (공백, 탭, 개행) |
| **8** | **경로 확장 (Pathname Expansion)** | `*.txt` → `a.txt b.txt` |

## 2. 인용 규칙 (Quoting Rules)

특수 문자의 의미를 제거하고 데이터 본연의 값을 유지하기 위해 사용합니다.

| 종류 | 기호 | 의미 및 특징 |
| :--- | :---: | :--- |
| **Escape Character** | `\` | 바로 다음 한 문자의 특수 의미를 제거 |
| **Single Quotes** | `' '` | 모든 문자를 일반 문자로 취급 (변수 확장 안 됨) |
| **Double Quotes** | `" "` | `$`, `` ` ``, `\`, `!`를 제외한 모든 특수 문자의 의미를 제거 (**변수 확장 됨**) |
| **C-style Strings** | `$' '` | `\n`, `\t` 등 ANSI C 이스케이프 시퀀스를 해석 |

## 3. 파라미터 확장 (Parameter Expansion)

변수 값의 유무나 조건에 따라 동적으로 값을 처리합니다.

| 표현식 | 설명 (var가 설정되지 않았거나 null일 때) |
| :--- | :--- |
| `${var:-word}` | `word`를 결과로 사용 (변수 값은 유지) - **기본값 읽기** |
| `${var:=word}` | `var`에 `word`를 대입하고 결과로 사용 - **기본값 할당** |
| `${var:?msg}` | `msg`를 에러로 출력하고 스크립트 종료 - **필수 인자 체크** |
| `${var:+word}` | `var`가 설정되어 있으면 `word` 사용, 아니면 null (반대 개념) |

## 4. 패턴 제거 및 문자열 치환

| 표현식 | 설명 | 특징 |
| :--- | :--- | :--- |
| `${var#pattern}` | 앞부분부터 짧은 패턴 삭제 | `#` (Small Prefix) |
| `${var##pattern}` | 앞부분부터 긴 패턴 삭제 | `##` (Large Prefix) |
| `${var%pattern}` | 뒷부분부터 짧은 패턴 삭제 | `%` (Small Suffix) |
| `${var%%pattern}` | 뒷부분부터 긴 패턴 삭제 | `%%` (Large Suffix) |
| `${var/pat/repl}` | 첫 번째 매칭되는 패턴을 치환 | `/` |
| `${var//pat/repl}` | 매칭되는 모든 패턴을 치환 | `//` |

## 5. 산술 연산 확장

- **문법**: `$(( expression ))`
- **특징**: 정수 연산만 지원 (부동소수점 불가), 64비트 정수 지원.
- **예시**: `n=$((n + 1))` 또는 `((n++))`

---

## 🔗 연결 문서

- [[01-overview]] - 셸 기본 개념
- [[03-variables-arrays]] - 변수 및 배열 활용
