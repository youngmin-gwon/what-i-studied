---
title: advanced-workflows
tags: [advanced, bisect, blame, bundle, filter-repo, git, grep, rebase, rerere, stash, workflow, worktree]
aliases: [Git 고급 워크플로우, Git 숙련가, Power Tools, 고급 Git 활용]
date modified: 2025-12-18 15:22:11 +09:00
date created: 2025-12-18 14:30:00 +09:00
---

## Git 고급 워크플로우: 효율을 극대화하는 전문가의 도구들

숙련된 개발자는 단순히 `add`, `commit`, `push` 만 하지 않습니다. 복잡한 히스토리를 정리하고, 생산성을 높여주는 Git 의 고급 기능을 적재적소에 활용합니다.

### 💡 Why it matters (Context)

- **깔끔한 히스토리**: `rebase` 를 통해 의미 없는 머지 커밋을 줄이고 선형적인 히스토리를 유지합니다.
- **빠른 컨텍스트 스위칭**: `stash` 나 `worktree` 를 사용하여 작업 중인 상태를 안전하게 보관하거나 병렬로 작업합니다.
- **디버깅 가속화**: `bisect` 와 `blame` 을 사용하여 문제의 원인과 수정한 사람을 즉시 찾아냅니다.

---

### 🏢 실무 사례 (Expert Techniques)

- **Parallel Developing**: 현재 브랜치에서 큰 수정을 하던 중 급한 버그 수정 요청이 오면, `stash` 대신 **`git worktree`**로 별도 폴더에서 즉시 작업을 시작합니다.
- **Archeology (코드 고고학)**: 특정 라인이 "왜" 이렇게 구현되었는지 궁금할 때 `git blame` 을 사용하여 해당 라인을 마지막으로 수정한 커밋과 메시지를 확인합니다.
- **Hotfix without History Rewrite**: 이미 배포된 오래된 커밋에 버그가 발견되었을 때, 히스토리를 새로 쓰지 않고도 임시로 객체를 교체하여 테스트해볼 수 있는 **`git replace`**를 활용합니다.

---

## 🏗️ 핵심 고급 기능

### 1. Interactive Rebase (`git rebase -i`)

커밋 히스토리를 다시 쓰는 강력한 도구입니다. (Squash, Reword, Drop, Edit)

### 2. Git Stash vs. Worktree (컨텍스트 스위칭)
- **Stash**: 현재 작업을 잠시 치워두기.
- **Worktree**: 하나의 레포지토리를 여러 개의 워킹 디렉토리로 동시에 체크아웃하기.
  - `git worktree add ../hotfix main`: `main` 브랜치를 별도의 `hotfix` 폴더에 체크아웃하여 즉시 작업 가능.

### 3. Git Bisect & Blame (검색과 책임)
- **Bisect**: 이진 탐색으로 버그 커밋 찾기.
- **Blame**: 파일의 각 라인을 누가, 언제, 어떤 커밋으로 수정했는지 표시.
  - `git blame -L 10,20 utils.py`: 특정 범위만 집중 분석.

### 4. Rerere (Reuse Recorded Resolution)

동일한 충돌 해결을 반복하지 않도록 Git 이 학습하는 기능입니다.

### 5. 히스토리 다시 쓰기 (`filter-repo` & `replace`)
- **filter-repo**: 전체 히스토리에서 대용량 파일이나 민감 정보 영구 삭제.
- **Replace**: 특정 객체를 다른 객체로 '대체'하여 보여주는 매핑 시스템. 히스토리를 물리적으로 바꾸지 않고도 과거의 실수를 바로잡은 것처럼 시뮬레이션할 수 있습니다.

### 6. Git Bundling (`git bundle`)

네트워크가 없는 환경에서 저장소를 바이너리 파일 하나로 전달하기.

### 7. Advanced Searching (`grep` & Log Pickaxe)
- **Git Grep**: 특정 브랜치/커밋 내 고속 검색.
- **Log Pickaxe (`-S`)**: 특정 문자열이 추가/제거된 커밋 찾기.

---

## 🚨 흔한 실수 (Common Mistakes)

1. **Worktree 사용 후 정리 누락**
   - 폴더만 지우면 Git 내부 관리 목록에 남습니다. 반드시 `git worktree remove` 를 사용하세요.
2. **Blame 으로 범인 찾기(?)** ⚠️
   - `blame` 의 목적은 '비난'이 아니라 '맥락 파악'입니다. 마지막 수정자가 로직을 짠 사람이 아니라 단순히 포맷팅 수정을 한 사람일 수도 있음을 유의하세요. (`-w` 옵션으로 공백 무시 가능)

---

### 📚 연결 문서

- [[02_advanced/troubleshooting|트러블슈팅]] - 복구와 충돌 해결
- [[00_fundamentals/git-internals|Git 인턴십]] - 객체와 `replace` 매커니즘의 이해
- [[02_advanced/command-comparisons|명령어 비교]] - Stash vs. Worktree 선택 기준
