---
title: git-rerere
tags: [advanced, conflict-resolution, git, rerere]
aliases: [Git Rerere, 충돌 재사용, 자동 해결]
date modified: 2026-08-10
date created: 2026-08-10
---

## Git Rerere: 동일한 충돌을 반복하지 않게 Git이 학습하기

`rerere` 는 "Reuse Recorded Resolution"의 약자로, Git이 충돌 해결 방법을 기억했다가 같은 충돌이 다시 나타날 때 자동으로 적용하는 기능입니다. 같은 브랜치를 여러 번 병합하거나, 복잡한 rebase를 할 때 시간을 절약할 수 있습니다.

### 💡 Why it matters (Context)

- **반복 작업 제거**: 같은 충돌을 수십 번 손으로 해결하지 않아도 됨.
- **재작업 효율화**: Long-running feature branch를 main과 자주 병합할 때 유용.
- **실수 방지**: 한 번 올바르게 해결한 충돌이 다시 발생하면 같은 방식으로 자동 해결.

---

## 🏗️ Rerere 활성화 및 기본 사용법

### Rerere 활성화

```bash
git config rerere.enabled true

# 모든 저장소에 적용하려면
git config --global rerere.enabled true
```

### 자동 커밋 (선택)

```bash
# Rerere가 자동으로 해결한 충돌을 자동으로 스테이징
git config rerere.autoupdate true
```

### Rerere의 동작 방식

Rerere가 활성화되면:

```
1. 충돌 발생
↓
2. Git이 충돌 패턴을 기록 (.git/rr-cache/)
↓
3. 사용자가 수동으로 충돌 해결
↓
4. Git이 해결 방법을 저장
↓
5. 다음에 같은 충돌이 나면 자동 적용
```

---

## 🏢 실무 사례 (Expert Techniques)

### 케이스 1: Long-running Feature Branch와 Main 동기화

```bash
# 오래 진행 중인 feature 브랜치
git checkout feature/large-refactor
git log --oneline --graph | head -5
# 이미 20개의 커밋이 있음

# 한 달 후, Main에서 중요한 변경이 많이 일어남
# feature를 main 최신 버전으로 리베이스
git rebase main

# 충돌 발생! (여러 커밋에서 동일한 충돌)
# conflict in utils.py
# conflict in config.ts
# ...

# 수동으로 첫 번째 충돌 해결
# Rerere가 이 해결책을 기록

git add utils.py
git rebase --continue

# 다시 같은 충돌 발생? Rerere가 자동으로 해결!
# Resolved 'utils.py' using previous resolution.
# Applying: Fix utils logic
# Applying: Add new feature
```

**이점**: 10번의 rebase에서 동일한 충돌이 발생해도, 첫 번째만 수동으로 해결하면 나머지는 모두 자동 해결됨.

### 케이스 2: PR 재베이싱 자동화

```bash
# 팀 워크플로우: 모든 PR은 main에 리베이스 후 merge
# Rerere가 반복되는 병합 충돌을 자동으로 해결

git checkout my-feature
git rebase main

# (첫 번째: 충돌 수동 해결)
# git add .
# git rebase --continue

# 이후 같은 파일의 같은 위치에서 충돌이 나면:
# Resolved '...' using previous resolution.  ← Rerere의 자동 해결
```

### 케이스 3: 여러 브랜치의 동일한 충돌 처리

```bash
# 여러 feature 브랜치가 같은 코드를 수정하고 있을 때
git checkout feature-1
git merge main      # 충돌 발생, 수동 해결

git checkout feature-2
git merge main      # 동일한 충돌 발생?
# Rerere가 feature-1에서의 해결책을 자동 적용!

git checkout feature-3
git merge main      # 역시 자동으로 해결됨!
```

---

## 📊 Rerere 저장소 관리

### 저장된 해결책 확인

```bash
# Rerere 저장소 크기 및 내용 확인
ls -la .git/rr-cache/

# 각 해결책의 해시 확인
git rerere status
```

### 저장된 해결책 제거

```bash
# 특정 해결책 제거
git rerere forget <path>

# 모든 해결책 제거
git rerere clear
```

### 저장된 해결책 테스트

```bash
# Rerere 기반으로 자동 해결을 시뮬레이션
git rerere diff
```

---

## 🚨 흔한 실수 (Common Mistakes)

1. **Rerere 저장소의 잘못된 해결책** ❌
   - 한 번 잘못된 충돌 해결이 저장되면, 같은 충돌이 나올 때마다 그 잘못된 해결책이 적용됩니다.
   - 자동 해결이 의심스러우면 `git rerere status` 로 확인하고, 필요시 `git rerere forget` 으로 삭제하세요.

   ```bash
   # 의심스러운 자동 해결 거부
   git rerere forget <path>
   git status          # 충돌 상태로 복원됨
   # (수동으로 올바르게 해결)
   git add <path>
   git rebase --continue
   ```

2. **Rerere 활성화 후 팀 동기화 누락** ⚠️
   - 개인 PC에서만 rerere를 사용하면, 팀원과 해결책이 달라질 수 있습니다.
   - `.git/rr-cache/` 를 공유 저장소에 커밋하려면 별도의 설정이 필요합니다.

3. **과신으로 인한 자동 병합** ❌
   - `rerere.autoupdate = true` 를 설정하면 자동으로 스테이징되므로, 검토 없이 커밋될 수 있습니다.
   - 항상 `git status` 로 자동 해결 결과를 확인하세요.

   ```bash
   # 안전한 방법
   git rebase main
   # (충돌, rerere가 자동 해결)
   git diff                # 변경 사항 확인
   git rebase --continue   # 확인 후 진행
   ```

---

## 💡 Rerere의 한계와 해결책

### 한계

1. **구조적 변화는 감지 못함**
   - 같은 라인이라도 양쪽 모두에서 변경되면 Rerere가 해결책을 찾지 못할 수 있습니다.

2. **팀 간 공유 어려움**
   - 기본적으로 `.git/rr-cache/` 는 로컬 저장소에만 존재합니다.

### 해결책

```bash
# Rerere 캐시 공유 (고급 설정)
git config rerere.autoupdate true
git config rerere.enabled true

# 팀 공유를 위해 rr-cache를 버전 관리
git add .git/rr-cache
git commit -m "Update rerere cache"
git push
```

---

### 📚 연결 문서

- [명령어 비교](command-comparisons.md) - Merge vs Rebase (충돌 가능성)
- [Interactive Rebase](interactive-rebase.md) - Rebase 중 충돌 해결
- [트러블슈팅](troubleshooting.md) - 복잡한 충돌 수동 해결
