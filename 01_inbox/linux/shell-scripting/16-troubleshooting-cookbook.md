---
title: 16-troubleshooting-cookbook
tags: [errors, guide, linux, shell, troubleshooting]
aliases: []
date modified: 2025-12-28 21:03:26 +09:00
date created: 2025-12-28 20:46:05 +09:00
---

## 16. 트러블슈팅 Cookbook

스크립트 실행 중 발생하는 흔한 에러 메시지들의 원인을 분석하고 즉각적인 해결책을 제시합니다.

### 1. 문법 및 실행 에러 (Syntax & Execution)

| 에러 메시지 | 가능한 원인 | 해결 방법 |
| :--- | :--- | :--- |
| `syntax error near unexpected token 'fi'` | `if` 문 또는 `then` 블록 짝이 맞지 않음 | 블록 종료 문구(`fi`)와 세미콜론(`;`) 확인 |
| `bad substitution` | Bash 전용 문법을 POSIX `/bin/sh` 에서 실행함 | Shebang 을 `#!/bin/bash` 로 수정 |
| `binary operator expected` | 변수가 비어있어 비교 연산자가 인자를 못 찾음 | 변수 참조 시 반드시 `"$VAR"` 로 인용 |
| `unbound variable` | `set -u` 가 켜져 있는데 정의 안 된 변수 참조 | `${VAR:-default}` 처럼 기본값 패턴 사용 |
| `Permission denied` | 파일에 실행 권한(`x`)이 없거나 경로 권한 부족 | `chmod +x script.sh` 실행 또는 경로 권한 확인 |

### 2. 데이터 처리 및 리소스 에러

| 에러 메시지 / 증상              | 원인 분석                         | 해결 방안                                    |
| :----------------------- | :---------------------------- | :--------------------------------------- |
| `Broken pipe`            | 파이프 뒤의 명령이 데이터를 다 받기 전 종료됨    | `set -o pipefail` 로 감지하거나 무시(`\|\| true`) |
| `Argument list too long` | 와일드카드(`*`) 확장 결과가 시스템 제한을 초과함 | `find` 와 `xargs` 를 조합하여 나누어 처리             |
| `Text file busy`         | 실행 중인 스크립트 파일을 수정/덮어쓰려 함      | 복사본을 만든 후 `mv` 로 교체하거나 실행 중단              |
| `Cannot allocate memory` | 너무 큰 데이터를 배열에 담으려 함           | 스트리밍(`while read`) 방식으로 변경하여 처리          |

### 3. 환경별 이슈 (Environment Specifics)

| 환경 | 주요 문제 | 해결책 |
| :--- | :--- | :--- |
| **Cron / Task Scheduler** | `PATH` 가 짧아 명령을 찾지 못함 | 스크립트 상단에 `PATH` 를 명시적으로 재설정 |
| **macOS (BSD)** | `sed -i` 또는 `date` 옵션이 리눅스와 다름 | 인플레이스 옵션에 빈 문자열(`''`) 추가 등 분기 |
| **SSH (Non-interactive)** | `.bashrc` 로딩이 안 되어 Alias/함수 미동작 | 설정 파일을 명시적으로 `source` 하거나 절대경로 사용 |

---

### 🔗 연결 문서

- [[15-lab-walkthroughs]] - 실습 랩 워크스루
- [[../shell-scripting]] - 전체 가이드 목록
