---
title: 12-recipes
tags: [checklist, linux, recipes, shell, snippets]
aliases: []
date modified: 2025-12-28 21:23:32 +09:00
date created: 2025-12-28 20:45:38 +09:00
---

## 12. 실전 레시피 및 체크리스트

자주 사용되는 코드 패턴(Snippets)과 스크립트 작성 전후에 반드시 점검해야 할 항목들을 정리합니다.

### 1. 실전 핵심 스니펫 (Core Snippets)

| 용도 | 코드 (Code) | 설명 |
| :--- | :--- | :--- |
| **안전 옵션** | `set -Eeuo pipefail` | 필수 안전 세트 |
| **임시 공간** | `TMP=$(mktemp -d) \|\| exit 1; trap 'rm -rf "$TMP"' EXIT` | 자동 삭제되는 작업장 |
| **파일 읽기** | `while IFS= read -r line; do … done < file` | 가장 안전한 루프 패턴 |
| **명령 확인** | `command -v jq >/dev/null \|\| exit 1` | 외부 의존성 사전 체크 |
| **색상 출력** | `[ -t 1 ] && RED='\e[31m' \|\| RED=''` | 터미널 여부에 따른 색상 적용 |

### 2. 필수 인자 파싱 (getopts 템플릿)

```bash
parse_args() {
  local OPTIND opt
  while getopts 'f:v' opt; do
    case "$opt" in
      f) FILE="$OPTARG" ;;
      v) VERBOSE=1 ;;
      *) usage; exit 2 ;;
    esac
  done
}
```

### 3. POSIX 대안 (배포용 스크립트)

| 기능      | Bash 확장       | POSIX 호환 대안               |
| :------ | :------------ | :------------------------ |
| **조건문** | `**...**`   | `[ … ]` (인용 필수)           |
| **배열**  | `arr=(…)`     | `set -- …` (위치 매개변수 활용)   |
| **실행**  | `local var`   | 전역 변수 초기화로 관리             |
| **경로**  | `readlink -f` | `perl` 또는 `python` 활용 스니펫 |

### 4. 최종 체크리스트 (Final Checklist)

| 체크 항목 | 확인 절차 |
| :--- | :--- |
| **Quoting** | 모든 변수와 경로가 `"` 로 감싸져 있는가? |
| **Shebang** | `#!/usr/bin/env bash` 등 올바른 인터프리터가 지정되었는가? |
| **Error Handling** | 실패 가능한 모든 명령 뒤에 대응 로직이 있는가? |
| **Cleanup** | `trap` 을 통해 임시 파일과 자식 프로세스가 정리되는가? |
| **Analyzing** | `shellcheck` 를 통해 정적 분석을 통과했는가? |

---

### 🔗 연결 문서

- [11-security-performance](11-security-performance.md) - 보안 및 성능 최적화
- [13-mock-exam-qa](13-mock-exam-qa.md) - 모의고사 Q&A
