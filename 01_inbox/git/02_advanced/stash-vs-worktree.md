---
title: stash-vs-worktree
tags: [advanced, context-switching, git, stash, worktree]
aliases: [Git Stash vs Worktree, 컨텍스트 스위칭, 병렬 작업]
date modified: 2026-08-10
date created: 2026-08-10
---

## Git Stash vs. Worktree: 효율적인 컨텍스트 스위칭의 두 전략

작업 중인 코드를 임시 보관하거나 다른 브랜치에서 긴급 작업을 해야 할 때, `stash` 와 `worktree` 두 가지 방법이 있습니다. 각각의 사용 사례와 장단점을 명확히 이해하면 업무 효율이 크게 향상됩니다.

### 💡 Why it matters (Context)

- **중단 없는 개발**: 긴급 버그 수정이 들어와도 현재 작업을 잃지 않고 빠르게 전환합니다.
- **병렬 작업 능력**: 여러 브랜치를 동시에 작업해야 할 때 효율적으로 관리합니다.
- **팀 협업 생산성**: 컨텍스트 스위칭 오버헤드를 최소화합니다.

---

## 🏗️ Stash vs. Worktree 비교

### Stash: 현재 작업을 일시 보관하기

**사용 시점**: 현재 브랜치에서 작업 중인 상태를 "잠시 치워두고" 다른 일을 처리해야 할 때.

```bash
# 현재 작업 보관
git stash

# 보관된 목록 확인
git stash list
# stash@{0}: WIP on feature-branch: 3a4b5c6 마지막 커밋

# 작업 복원
git stash pop              # 가장 최근 stash 적용 및 제거
git stash apply stash@{0}  # 특정 stash 적용 (제거 안 함)

# Stash 제거
git stash drop stash@{0}
```

**특징**:
- ✅ 간단하고 빠름
- ✅ 단일 브랜치 환경에서 최적화
- ❌ 여러 브랜치를 동시에 작업하기 어려움
- ❌ Stash 복원 중 충돌 가능성 높음

---

### Worktree: 하나의 레포지토리, 여러 워킹 디렉토리

**사용 시점**: 여러 브랜치를 동시에 작업하거나 오래 기다려야 할 상황.

```bash
# 새 worktree 생성 (main 브랜치를 ../hotfix 폴더에서 작업)
git worktree add ../hotfix main

# 작업 디렉토리 변경
cd ../hotfix
# (이곳에서 독립적으로 main 브랜치를 수정/커밋할 수 있음)

# Worktree 목록 확인
git worktree list
# /path/to/repo (branch 'feature')
# /path/to/hotfix (branch 'main')

# 작업 완료 후 정리 (반드시 명시적으로 제거)
git worktree remove hotfix
```

**특징**:
- ✅ 진정한 병렬 작업 (각 worktree는 독립적인 파일 상태)
- ✅ 충돌 위험 없음
- ✅ 테스트와 개발을 동시에 진행 가능
- ❌ 작업 완료 후 정리 필수 (안 하면 Git 내부 관리 목록에 남음)
- ❌ 폴더 관리 필요

---

## 🏢 실무 사례 (Expert Techniques)

### 케이스 1: 기능 개발 중 긴급 버그 수정

```bash
# 기능 개발 중...
# 버그 리포트 들어옴!

# 방법 A: Stash 사용 (빠른 일처리)
git stash                    # 현재 작업 임시 저장
git switch main
git switch -c bugfix/issue-123
# (버그 수정 및 커밋)
git push
git switch feature-branch
git stash pop                # 작업 재개

# 방법 B: Worktree 사용 (병렬 작업)
git worktree add ../bugfix main
cd ../bugfix
# (버그 수정 및 커밋, main 브랜치에서 독립적으로 작업)
git push
cd ../repo
git worktree remove bugfix
# 기능 개발 계속
```

### 케이스 2: 오래 걸리는 빌드 중 다른 작업

```bash
# feature 브랜치에서 큰 작업 중, 빌드 실행
git worktree add ../test feature
cd ../test
npm run build                # 시간이 오래 걸림

# 원래 디렉토리로 이동
cd ../repo
git switch -c another-feature main  # 다른 기능 개발
# (이 동안 ../test에서 빌드가 진행 중)
```

### 케이스 3: 여러 검토 브랜치 동시 검토

```bash
# PR 검토를 위해 여러 브랜치 동시 확인
git worktree add ../pr-review-1 origin/pull/123/head
git worktree add ../pr-review-2 origin/pull/124/head
git worktree add ../pr-review-3 origin/pull/125/head

# 세 개의 폴더에서 각각 다른 코드를 검토할 수 있음
# 검토 완료 후
git worktree remove pr-review-1
git worktree remove pr-review-2
git worktree remove pr-review-3
```

---

## 🚨 흔한 실수 (Common Mistakes)

1. **Worktree 폴더만 삭제하기** ❌
   - 폴더를 직접 지우기만 하면 Git 내부 관리 목록에 여전히 남습니다.
   - 반드시 `git worktree remove` 를 사용하세요.

   ```bash
   # 잘못된 방법
   rm -rf ../hotfix          # ❌ Git이 여전히 이 worktree를 기억함

   # 올바른 방법
   git worktree remove hotfix  # ✅ Git 내부 정보도 함께 제거
   ```

2. **Stash 관리 소홀** ❌
   - 여러 개의 stash를 만들어놓고 어떤 게 어떤 작업인지 까먹을 수 있습니다.
   - 주기적으로 `git stash list` 로 확인하고 불필요한 stash는 제거하세요.

   ```bash
   # 오래된 stash 확인 및 정리
   git stash list
   git stash drop stash@{5}   # 필요 없는 stash 삭제
   ```

3. **Worktree에서 같은 브랜치 체크아웃** ❌
   - 한 레포지토리에서 같은 브랜치를 여러 worktree로 체크아웃할 수 없습니다.
   - 각 worktree는 서로 다른 브랜치를 가져야 합니다.

---

## 📋 선택 기준: Stash vs. Worktree

| 상황 | 추천 | 이유 |
|:---|:---|:---|
| 5분 이내 빠른 작업 전환 | Stash | 빠르고 간단 |
| 긴 시간의 병렬 작업 | Worktree | 독립성 보장 |
| 여러 테스트 실행 동시 진행 | Worktree | 각각 독립적 빌드 |
| 간단한 임시 작업 | Stash | 관리 오버헤드 적음 |
| 팀원과 협업 중 맥락 보존 | Worktree | 파일 상태 실제로 유지 |

---

### 📚 연결 문서

- [명령어 비교](command-comparisons.md) - Git 주요 명령어 비교
- [Git 인턴십](../00_fundamentals/git-internals.md) - 워킹 디렉토리의 내부 구조
- [트러블슈팅](troubleshooting.md) - Stash 복원 중 충돌 해결
