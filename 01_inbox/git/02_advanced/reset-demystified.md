---
title: reset-demystified
tags: [advanced, checkout, git, reset, three-trees]
aliases: [Git Reset 완벽 분석, Reset vs Checkout, Reset 원리]
date modified: 2025-12-18 15:22:16 +09:00
date created: 2025-12-18 15:40:00 +09:00
---

## Reset Demystified: Git 의 가장 강력하고 위험한 도구 마스터하기

`git reset` 과 `git checkout` 은 Git 에서 가장 혼란스러운 명령어입니다. 하지만 **세 가지 나무 (The Three Trees)** 개념을 적용하면, 이 명령어들이 데이터베이스를 어떻게 조작하는지 수학적으로 명확하게 이해할 수 있습니다.

---

### 💡 Why it matters (Context)

- **정교한 복구**: 단순히 '되돌리기'가 아니라, 특정 영역(Index 만, 혹은 Working Directory 까지)만 선택적으로 제어할 수 있습니다.
- **히스토리 관리**: 커밋 메시지를 고치거나, 여러 커밋을 합칠 때(Squash) 내부적으로 어떤 일이 일어나는지 이해하게 됩니다.
- **사고 예방**: `--hard` 옵션이 왜 위험한지, 어떤 상황에서 데이터 유실이 발생하는지 명확히 알 수 있습니다.

---

## 🏗️ Reset 의 3 단계 작동 원리

`git reset [branch/commit]` 명령어는 옵션에 따라 다음 세 단계를 순차적으로 수행합니다.

### 1 단계: HEAD 이동 (`--soft`)
- **수행**: 현재 브랜치가 가리키는 커밋(HEAD)을 대상 커밋으로 옮깁니다.
- **결과**: **Index(Staging Area)와 Working Directory 는 변하지 않습니다.**
- **용도**: 커밋을 취소하고 다시 커밋하고 싶을 때(메시지 수정 등) 사용합니다.

### 2 단계: Index 업데이트 (`--mixed`, 기본값)
- **수행**: 1 단계를 수행한 후, 대상 커밋의 스냅샷 내용으로 **Index 를 덮어씁니다.**
- **결과**: **Working Directory 는 여전히 변하지 않습니다.**
- **용도**: 스테이징된 작업들을 취소하고 파일들을 다시 선별해서 커밋하고 싶을 때 사용합니다.

### 3 단계: Working Directory 업데이트 (`--hard`)
- **수행**: 2 단계를 수행한 후, 대상 커밋의 내용으로 **Working Directory 까지 덮어씁니다.**
- **결과**: **저장하지 않은 모든 수정 사항이 유실됩니다.**
- **용도**: 현재 작업을 완전히 버리고 특정 시점으로 완벽히 돌아가고 싶을 때 사용합니다.

---

## 🔄 Reset vs. Checkout (결정적 차이)

| 명령어 | 핵심 동작 | 안전성 |
| :--- | :--- | :--- |
| **`reset --hard [commit]`** | **브랜치 포인터 자체를 옮김.** (역사를 바꿈) | **위험.** 저장 안 된 작업 유실. |
| **`checkout [commit]`** | **HEAD 포인터만 옮김.** (브랜치는 그대로 두고 구경만 함) | **안전.** 작업 중인 파일이 있으면 경고함. |

>[!IMPORTANT] **파일 단위의 Reset/Checkout**
>특정 파일에 대고 명령을 수행하면(`git reset file.txt`), 브랜치는 움직이지 않고 **해당 파일의 내용만** 영역 간에 복사됩니다.

---

## 🚨 흔한 실수 (Common Mistakes)

1. **공용 브랜치에서 Reset** ❌
   - 이미 Push 된 커밋을 `reset` 으로 지우면 팀원들의 히스토리와 충돌합니다. 공용 브랜치에서는 반드시 `revert` 를 사용하세요.
2. **`reset --hard` 직전 Stash 누락** ❌
   - "잠깐 이전 코드를 확인하고 싶어서" `--hard` 를 썼다가는 현재 코딩 중인 내용이 영구히 사라질 수 있습니다. 습관적으로 `git stash` 를 먼저 하세요.
3. **Reset 후 Index 불일치 착각**
   - `--soft` 를 썼는데 "왜 소스코드가 안 바뀌지?"라고 당황하지 마세요. 소스코드는 Working Directory 에 있고, `--soft` 는 HEAD 만 움직입니다.

---

### 📚 연결 문서

- [[00_fundamentals/basic-concepts|Git 기본 개념]] - 세 가지 나무(Three Trees) 기초
- [[00_fundamentals/git-internals|Git 인턴십]] - HEAD 와 Ref 가 내부적으로 어떻게 저장되는지
- [[02_advanced/troubleshooting|트러블슈팅]] - Reset 실수를 복구하는 `reflog` 활용법
