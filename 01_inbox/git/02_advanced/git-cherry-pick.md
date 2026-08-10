---
title: git-cherry-pick
tags: [advanced, cherry-pick, git, merging, workflow]
aliases: [Cherry Pick, 특정 커밋 가져오기, cherry-pick 기술]
date modified: 2026-08-10
date created: 2026-08-10
---

## Cherry-Pick: 특정 커밋만 골라 담기

`git cherry-pick` 은 특정 브랜치의 커밋 중 **원하는 것들만** 현재 브랜치에 복사(반영)하는 강력한 도구입니다. 완전한 브랜치 병합은 아니지만, 특정 수정 사항만 다른 브랜치에 적용해야 할 때 매우 유용합니다.

---

### 💡 Why it matters (Context)

- **선택적 병합**: 전체 브랜치를 병합하지 않고, 특정 커밋들만 현재 작업에 적용할 수 있습니다.
- **핫픽스 배포**: 프로덕션에서 발견된 버그를 먼저 `develop` 브랜치에서 수정한 후, `main` 브랜치에 선택적으로 적용합니다.
- **백포트(Backport)**: 최신 버전에서 고쳐진 기능을 구 버전에 적용할 때 매우 효율적입니다.

---

## 🏗️ Cherry-Pick의 기본 사용법

### 단일 커밋 선택하기

```bash
# 특정 커밋을 현재 브랜치에 적용
git cherry-pick <commit-hash>

# 예: 다른 브랜치의 특정 커밋 가져오기
git cherry-pick feature/bug-fix~3
```

### 여러 커밋을 연속으로 적용하기

```bash
# 범위 지정: A 이후부터 B까지의 모든 커밋 적용
git cherry-pick <commit-A>..<commit-B>

# 주의: commit-A는 포함 안 됨. A를 포함하려면:
git cherry-pick <commit-A>^..<commit-B>
```

### 여러 커밋을 개별적으로 적용하기

```bash
# 여러 커밋을 한 번에 지정
git cherry-pick <commit-1> <commit-2> <commit-3>
```

---

## 🏗️ 실무 시나리오

### 시나리오 1: 버그픽스 핫포트

프로덕션 브랜치(`main`)에서 중대한 버그가 발견되었고, 동시에 개발 중인 `develop` 브랜치도 있을 때:

```bash
# main에서 버그를 수정한 커밋: abc123

# develop 브랜치로 이동
git checkout develop

# main의 버그픽스 커밋을 develop에 적용
git cherry-pick abc123
```

### 시나리오 2: 선택적 기능 적용

`feature/auth` 브랜치에서 여러 개의 커밋 중 인증(Authentication) 관련 커밋만 현재 작업에 적용:

```bash
# feature/auth의 특정 커밋들 확인
git log feature/auth

# 필요한 커밋만 체리픽
git cherry-pick commit1 commit2 commit3
```

---

## 🏗️ 충돌 처리 (Conflict Resolution)

Cherry-pick 중에 충돌이 발생할 수 있습니다. 이는 rebase나 merge와 유사하게 처리합니다.

### 충돌 발생 시 대응

```bash
# 충돌 발생 시 자동으로 일시 중지됨
# 파일을 수정한 후...

git add <resolved-file>

# cherry-pick 계속 진행
git cherry-pick --continue

# 또는 cherry-pick 취소
git cherry-pick --abort
```

### 자동 병합 전략 지정

```bash
# 재귀적 병합(기본값)
git cherry-pick -X recursive <commit>

# 우리의 버전을 우선시
git cherry-pick -X ours <commit>

# 그들의 버전을 우선시
git cherry-pick -X theirs <commit>
```

---

## 🏗️ Cherry-Pick vs. Merge vs. Rebase

| 기능 | 사용 시기 | 히스토리 |
|:---|:---|:---|
| **Merge** | 전체 브랜치를 통합 | 병합 커밋 생성 (비선형) |
| **Rebase** | 선형 히스토리 유지 | 커밋들을 재생(Replay) - 선형 |
| **Cherry-Pick** | 특정 커밋만 선택 | 선택된 커밋들만 복사 - 선형 |

**Key Difference**: Cherry-pick은 **원본 커밋의 작성자와 메시지는 보존**하지만, **새로운 커밋 해시를 가집니다.**

---

## 🚨 흔한 실수 (Common Mistakes)

1. **Cherry-Pick의 남용** ❌
   - 너무 자주 cherry-pick을 사용하면, 여러 브랜치에 비슷한 코드가 산재되어 관리가 어려워집니다. 가능하면 merge나 rebase를 사용하세요.

2. **같은 커밋을 여러 번 Cherry-Pick** ❌
   - 이미 cherry-pick된 커밋을 다시 cherry-pick하면 충돌이 발생합니다. `git log`로 확인 후 진행하세요.

3. **공용 브랜치에서의 Cherry-Pick 남용** ⚠️
   - Cherry-pick은 히스토리를 '새로 쓰는' 것이므로, 공용 브랜치에서는 신중하게 사용해야 합니다.

4. **충돌 해결 후 Commit 누락** ❌
   - Cherry-pick 충돌을 해결한 후 반드시 `git add`로 스테이징한 후 `--continue`를 사용해야 합니다.

---

### 📚 연결 문서

- [Reset 완벽 분석](reset-demystified.md) - 커밋과 히스토리 조작의 기본 원리
- [고급 머지 전략](advanced-merging.md) - 충돌 처리의 심화 기술
- [브랜치 전략](../01_strategies/branching-strategies.md) - 워크플로우에서의 cherry-pick 역할
- [Interactive Rebase](interactive-rebase.md) - 히스토리 재작성의 다른 방식
- [커밋 메시지](../01_strategies/commit-messages.md) - Cherry-pick된 커밋의 메시지 관리
