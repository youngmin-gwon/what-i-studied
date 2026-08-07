---
title: 21-posix-compat
tags: [linux, portability, posix, sh, shell]
aliases: []
date modified: 2025-12-28 21:08:13 +09:00
date created: 2025-12-28 20:46:44 +09:00
---

## 21. POSIX sh 호환 가이드

Bash 전용 기능을 배제하고 `/bin/sh` 또는 BusyBox 등 제한된 환경에서도 동작하는 스크립트 작성법을 정리합니다.

### 1. 핵심 차이 및 대안 (Bash vs POSIX)

| 기능         | Bash 확장 문법            | POSIX 호환 대안                     |
| :--------- | :-------------------- | :------------------------------ |
| **조건문**    | `**condition**`     | `[ condition ]` (인용 엄격 필수)      |
| **산술 연산**  | `(( i++ ))`           | `i=$((i + 1))`                  |
| **배열**     | `arr=(v1 v2)`         | `set -- v1 v2` (위치 매개변수 활용)     |
| **함수 선언**  | `function name { … }` | `name() { … }`                  |
| **로컬 변수**  | `local var="val"`     | 전역 변수 초기화 또는 서브셸 `( )` 활용       |
| **히어 스트링** | `<<< "$VAR"`          | `echo "$VAR" cmd` 또는 `Here-doc` |

### 2. 이식성 낮은 도구의 대안

| 도구 / 기능           | 문제점           | 해결 방안 (Portable Way)                   |
| :---------------- | :------------ | :------------------------------------- |
| **`readlink -f`** | macOS 등에 없음   | `perl`, `python` 원라이너 또는 단계적 `cd`      |
| **`sed -i`**      | GNU/BSD 인자 차이 | `sed … > temp && mv temp file` (정석 방식) |
| **`timeout`**     | 표준 도구 아님      | `perl -e 'alarm 5; exec @ARGV' cmd`    |
| **`date -d`**     | 옵션 표준 아님      | `date` 포맷팅 중심 사용 또는 `perl` 활용          |

### 3. POSIX 표준 체크리스트

- **Quoting**: 모든 변수 참조에는 반드시 더블 쿼트(`"`)를 사용합니다.
- **Shebang**: `#!/bin/sh` 를 사용하여 Bash 전용 기능 로딩을 방지합니다.
- **Built-ins**: `echo` 대신 `printf` 를 사용하여 출력의 이식성을 보장합니다.
- **Tests**: `==` 대신 `=` 를 사용하여 문자열을 비교합니다.

### 4. POSIX 호환 루프 예시

```sh
# 안전한 파일 읽기
while IFS= read -r line; do
  printf '%s\n' "$line"
done < input.txt
```

---

### 🔗 연결 문서

- [20-command-drills](20-command-drills.md) - 커맨드 드릴 세트
- [shell-scripting](../shell-scripting.md) - 전체 가이드 목록
