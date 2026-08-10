---
title: git-filter-repo-and-replace
tags: [advanced, filter-repo, git, history-rewrite, replace]
aliases: [Git Filter-repo, Git Replace, 히스토리 제거, 민감 정보 삭제]
date modified: 2026-08-10
date created: 2026-08-10
---

## Git Filter-repo & Replace: 히스토리를 안전하게 편집하기

때로는 저장소의 전체 히스토리에서 대용량 파일, 민감한 정보, 또는 잘못된 커밋을 제거해야 합니다. `git filter-repo` 는 전체 히스토리를 재작성하고, `git replace` 는 특정 커밋을 다른 버전으로 '교체'합니다.

### 💡 Why it matters (Context)

- **보안**: 실수로 커밋된 API 키, 패스워드, 개인정보를 완전히 제거.
- **저장소 최적화**: 예전에 커밋했던 거대한 바이너리 파일을 역사에서 완전 제거.
- **히스토리 수정**: 이미 공개된 저장소의 과거 커밋을 몰래 수정 (Replace 사용).

---

## 🏗️ Git Filter-repo: 전체 히스토리 정제

### 설치

```bash
pip install git-filter-repo
# 또는
brew install git-filter-repo  # macOS
```

### 기본 사용법

#### 대용량 파일 제거

```bash
# 저장소에서 500MB 이상 모든 파일 찾기
git rev-list --all --objects | \
  sed -n $(git rev-list --objects --all | \
  cut -f1 -d' ' | \
  git cat-file --batch-check | \
  grep blob | \
  sort -k3 -n | \
  tail -n10 | \
  cut -d' ' -f1 | \
  while read hash; do \
    echo -n "-e s/$hash/$hash/p "; \
  done) | cut -d' ' -f2-

# 또는 직접 파일명으로 제거
git filter-repo --path node_modules --invert-paths
# node_modules 디렉토리 제거
```

#### 민감한 정보 제거

```bash
# 모든 커밋에서 특정 문자열 제거
git filter-repo --message-filter 'grep -v "TODO: password"'

# 파일에서 패턴 제거
git filter-repo --path-glob '*.env' --invert-paths
# .env 파일 완전 제거
```

---

## 🏢 실무 사례 (Expert Techniques)

### 케이스 1: 실수로 커밋된 AWS 키 제거

```bash
# 문제: config.json에 AWS_SECRET_KEY가 공개됨
# 파일은 .gitignore에 추가했지만, 이미 저장소에는 여러 커밋에 남아있음

# 1단계: 파일을 저장소에서 완전 제거
git filter-repo --path config.json --invert-paths

# 2단계: 민감 정보가 있는 커밋 모두 제거 (파일 자체도 제거됨)
# 결과: config.json이 최초 추가된 시점부터 모든 커밋에서 제거됨

# 3단계: 강제 푸시 (주의!)
git push origin --force-with-lease --all

# ⚠️ 팀원들에게 새로 clone하도록 요청
```

### 케이스 2: 대용량 빌드 아티팩트 제거

```bash
# 문제: 누군 build/ 디렉토리를 커밋해서 저장소가 500MB로 팽창
git filter-repo --path build --invert-paths

# 또는 여러 경로 제거
git filter-repo \
  --path build --invert-paths \
  --path dist --invert-paths \
  --path node_modules --invert-paths

# 결과: 저장소 크기가 50MB로 축소됨
```

### 케이스 3: 개발자 이름 변경 (개인정보 보호)

```bash
# 모든 커밋의 작성자를 익명으로 변경
git filter-repo --mailmap mailmap.txt

# mailmap.txt 내용:
# New Name <new.email@example.com> <old.email@example.com>
```

---

## 🏗️ Git Replace: 과거 커밋 교체하기 (히스토리 재작성 없음)

`replace` 는 filter-repo와 다르게 **히스토리를 물리적으로 변경하지 않고**, 특정 커밋을 다른 버전으로 '보이게'만 합니다.

### 기본 사용법

```bash
# 과거의 잘못된 커밋 (e4f5g6h)을 새로운 커밋 (a1b2c3d)으로 교체
git replace e4f5g6h a1b2c3d

# 교체 확인
git log --oneline
# (e4f5g6h가 a1b2c3d처럼 보임)

# 교체 취소
git replace -d e4f5g6h
```

---

## 🏢 Replace 실무 사례

### 케이스: QA에서 발견한 버그를 배포 전에 수정

```bash
# 상황
# - v1.5.0 배포 예정
# - QA에서 버그 발견
# - 버그를 도입한 커밋이 v1.0.0 (2년 전)
# - 그 커밋 이후 2000개의 커밋이 추가됨
# - Rebase로 고칠 수 없음

# 방법 1: 현재 버전에서 버그 고정
git checkout HEAD
# (버그 수정, 테스트)
git commit -m "Fix: 이전 버그 수정"  # a1b2c3d

# 방법 2: 원본 버그 커밋을 고정 버전으로 교체
git replace e4f5g6h a1b2c3d

# 이제 로그에서 보면 e4f5g6h이 버그 없는 버전으로 보임
git log e4f5g6h~3..e4f5g6h
# (버그 없는 코드로 표시됨)

# 방법 3: 이를 영구화 (선택사항)
git push origin 'refs/replace/*:refs/replace/*'
```

**이점**: 히스토리를 재작성하지 않으므로 다른 팀원들에게 영향 없음.

---

## ⚠️ Filter-repo vs Replace 비교

| 특징 | Filter-repo | Replace |
|:---|:---|:---|
| **범위** | 여러 커밋/파일 대상 | 특정 커밋만 교체 |
| **히스토리 변경** | 물리적 변경 (strong rewrite) | 보이기만 변경 (soft rewrite) |
| **팀 영향** | 강제 푸시 필요 | 영향 최소화 |
| **복구** | 어려움 | 쉬움 (`git replace -d`) |
| **용도** | 민감 정보/큰 파일 제거 | 과거 버그 수정, 히스토리 정리 |

---

## 🚨 흔한 실수 (Common Mistakes)

1. **Filter-repo 후 팀 동기화 누락** ❌
   ```bash
   # 잘못된 방법
   git filter-repo --path node_modules --invert-paths
   git push origin --force  # 팀원들의 로컬 저장소가 깨짐!

   # 올바른 방법
   # 1. 팀에 공지
   # 2. 모든 팀원이 준비되면 강제 푸시
   git push origin --force-with-lease
   # 3. 팀원들에게 새로 clone하도록 요청
   ```

2. **Replace의 임시성 착각** ❌
   ```bash
   git replace e4f5g6h a1b2c3d
   # → 로컬에서만 유효
   # → 팀원들에게는 변경사항이 보이지 않음
   # → 영구화하려면 반드시 refs/replace를 푸시해야 함
   git push origin 'refs/replace/*:refs/replace/*'
   ```

3. **민감 정보 제거 후 캐시 확인 누락** ❌
   ```bash
   # Filter-repo로 파일 제거
   git filter-repo --path secret.txt --invert-paths

   # ⚠️ 하지만 임시 객체(unreachable objects)는 여전히 존재
   git reflog expire --expire=now --all
   git gc --prune=now  # 이제야 완전히 삭제됨
   ```

---

## 🔧 고급: 복잡한 필터링

### 특정 커미터만 제거

```bash
git filter-repo --mailmap mailmap.txt
# mailmap.txt:
# <new@example.com> <old.spam@example.com>
```

### 커밋 크기별 필터링

```bash
# 50MB 이상 파일 모두 제거
git rev-list --all --objects | \
  sed -n $(git rev-list --objects --all | \
  cut -f1 -d' ' | \
  git cat-file --batch-check | \
  grep blob | \
  awk '$3 > 50000000' | \  # 50MB
  cut -d' ' -f1 | \
  while read hash; do \
    echo -n "-e s/$hash/$hash/p "; \
  done) | cut -d' ' -f2- | \
  xargs git filter-repo --path-match
```

---

### 📚 연결 문서

- [Git 인턴십](../00_fundamentals/git-internals.md) - 객체 저장소와 GC 매커니즘
- [트러블슈팅](troubleshooting.md) - Filter-repo 실패 시 복구
- [명령어 비교](command-comparisons.md) - Reset vs Replace의 차이
