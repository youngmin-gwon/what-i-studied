---
title: 14-command-reference
tags: [commands, linux, patterns, reference, shell]
aliases: []
date modified: 2025-12-28 21:23:12 +09:00
date created: 2025-12-28 20:45:58 +09:00
---

## 14. 명령 및 옵션 레퍼런스

시험과 실무에서 빈번하게 사용되는 핵심 명령들의 주요 옵션과 사용 패턴을 정리합니다.

### 1. 셸 내장 명령 (Built-in Commands)

| 명령어 | 주요 옵션 / 특징 | 예시 및 팁 |
| :--- | :--- | :--- |
| **read** | `-r` (원본 유지), `-p` (프롬프트), `-s` (숨김), `-a` (배열) | `read -rp "Enter: " VAL` |
| **declare** | `-i` (정수), `-a` (배열), `-A` (연관 배열), `-r` (읽기 전용), `-x` (내보내기) | `declare -A MAP` |
| **set** | `-e` (실패 시 종료), `-u` (미정의 변수 에러), `-x` (추적) | `set -euo pipefail` |
| **shopt** | `nullglob`, `dotglob`, `globstar` 등 Bash 전용 옵션 제어 | `shopt -s globstar` |
| **printf** | `%s` (문자열), `%d` (정수), `%q` (셸 이스케이프 포맷) | `printf '%q\n' "$PATH"` |

### 2. 텍스트 필터 및 가공 (Text Filters)

| 도구 (Tool) | 빈출 옵션 요약                                                              | 핵심 패턴                      |
| :-------- | :-------------------------------------------------------------------- | :------------------------- |
| **grep**  | `-i` (무시), `-v` (반전), `-E` (확장 정문제), `-r` (재귀), `-o` (매칭만), `-F` (고정) | `grep -Ei 'error \| warn'` |
| **sed**   | `-n` (필요 시만 출력), `-i` (In-place 수정), `s/old/new/g` (치환)               | `sed -i 's/foo/bar/g'`     |
| **awk**   | `-F` (구분자), `$1, $NF, NR, NF, BEGIN, END`                             | `awk -F: '{print $1}'`     |
| **sort**  | `-n` (숫자), `-r` (역순), `-k` (키 정렬), `-u` (고유값)                         | `sort -nrk2`               |
| **xargs** | `-0` (NUL 안전), `-I {}` (치환), `-P` (병렬)                                | `find … \| xargs -0 -P4`   |

### 3. 파일 및 시스템 명령

| 분야 | 명령어 | 주요 기능 및 옵션 |
| :--- | :--- | :--- |
| **탐색** | **find** | `-name`, `-type f/d`, `-mtime`, `-size`, `-exec` |
| **네트워크** | **curl** | `-f` (실패 시 무음), `-s` (조용히), `-L` (리다이렉션 추적), `-o` (저장) |
| **프로세스** | **ps** | `-ef` (전체 목록), `-aux` (상세 정보), `-o` (출력 포맷 지정) |
| **리소스** | **ulimit** | `-n` (파일 오픈 수), `-t` (CPU 시간), `-v` (가상 메모리) |

### 4. 실전 원라이너 (One-Liners)

| 목표              | 코드 (One-Liner)                           |
| :-------------- | :--------------------------------------- |
| **용량 상위 10 개**  | `du -sh * \| sort -h \| tail -n 10`      |
| **중복 제거 카운트**   | `sort \| uniq -c \| sort -nr`            |
| 주석 및 빈 줄 제거 | `grep -Ev '^#\|^$' file` |
| 포트 오픈 체크 | `nc -z -w 1 localhost 22 && echo "Open"` |

---

### 🔗 연결 문서

- [[13-mock-exam-qa]] - 모의고사 Q&A
- [[15-lab-walkthroughs]] - 실습 랩 워크스루
