---
title: git-grep-and-pickaxe
tags: [advanced, git, grep, log-pickaxe, search]
aliases: [Git Grep, Git Pickaxe, 코드 검색, 히스토리 검색]
date modified: 2026-08-10
date created: 2026-08-10
---

## Git Grep & Log Pickaxe: 저장소 전체에서 빠르게 검색하기

Git에는 저장소 전체를 대상으로 매우 빠른 검색을 제공하는 두 가지 도구가 있습니다. `git grep` 은 특정 버전의 코드에서 빠르게 검색하고, `git log -S` (Pickaxe)는 특정 문자열이 추가/제거된 커밋을 찾습니다.

### 💡 Why it matters (Context)

- **빠른 검색**: 파일 시스템 검색보다 훨씬 빠름 (indexed 검색).
- **버전별 검색**: 특정 브랜치나 커밋 시점의 코드만 검색.
- **변화 추적**: 문자열이 언제 추가되고 제거되었는지 히스토리에서 추적.

---

## 🏗️ Git Grep: 빠른 코드 검색

### 기본 사용법

```bash
# 현재 상태에서 "function_name" 검색
git grep function_name

# 특정 브랜치에서 검색
git grep function_name main
git grep function_name v1.5.0

# 정규식 검색
git grep -E "async.*function" main
```

### 주요 옵션

```bash
# 파일명만 표시
git grep -l pattern

# 라인 번호와 함께 표시
git grep -n pattern

# 특정 파일 유형만 검색
git grep --include="*.js" pattern
git grep --include="*.py" pattern

# 특정 디렉토리만 검색
git grep pattern -- src/

# 대소문자 무시
git grep -i "API_KEY"
```

### 결과 형식 정렬

```bash
# 파일별로 그룹화
git grep -p pattern
# Output:
# main.js-function calculate() {
# main.js:    const result = pattern_match();

# 통계 정보
git grep -c pattern
# Output:
# utils.js:3
# main.js:5
# helpers.js:2
```

---

## 🏗️ Git Log Pickaxe: 문자열 추가/제거 추적

### 기본 사용법

```bash
# 특정 문자열이 추가/제거된 커밋 찾기
git log -S "function_name"

# 더 상세한 정보 (diff 포함)
git log -p -S "function_name"

# 특정 파일에서만 검색
git log -S "pattern" -- src/main.js
```

### 변화 추적

```bash
# 문자열이 추가된 커밋 (새로 나타남)
git log -S "new_feature" --diff-filter=A

# 문자열이 제거된 커밋 (사라짐)
git log -S "old_feature" --diff-filter=D

# 문자열이 변경된 모든 커밋
git log -S "pattern" --all
```

---

## 🏢 실무 사례 (Expert Techniques)

### 케이스 1: API 엔드포인트 변경 추적

```bash
# 특정 API 엔드포인트가 어떤 파일들에서 사용되는지 확인
git grep "/api/v1/users"

# Output:
# src/services/user.ts:  const url = '/api/v1/users';
# src/api/endpoints.ts:  endpoints: { users: '/api/v1/users' }
# tests/api.test.ts:    expect(call).toContain('/api/v1/users');

# 이 엔드포인트를 언제 추가했는지 확인
git log -p -S "/api/v1/users" | head -30
```

### 케이스 2: 함수명 변경 히스토리

```bash
# 함수명 변경 추적
git log -S "calculateTotal" --oneline

# Output:
# a1b2c3d Refactor: rename calculateTotal to computeSum
# e4f5g6h Add calculateTotal function
# i7j8k9l Use calculateTotal in reports

# 변경 세부 사항 확인
git show a1b2c3d
```

### 케이스 3: 라이브러리 버전 업그레이드 추적

```bash
# React 버전 업그레이드 찾기
git log -p -S "React.version" --all

# Output:
# commit a1b2c3d
# Date: 2024-01-15
#
# -"React 17.0.0"
# +"React 18.0.0"

# 또는 package.json에서만 검색
git log -p -S '"react": "' -- package.json
```

---

## 📊 Grep vs Pickaxe 비교

| 상황 | Grep | Pickaxe |
|:---|:---|:---|
| "현재 코드에서 이 문자열은 어디에?" | ✅ | ❌ |
| "이 문자열을 누가 추가했는가?" | ❌ | ✅ |
| "특정 파일만 검색" | ✅ | ⚠️ (가능하지만 느림) |
| "특정 버전의 코드에서 찾기" | ✅ | ❌ |
| "문자열의 변화 히스토리 추적" | ❌ | ✅ |

---

## 🚨 흔한 실수 (Common Mistakes)

1. **Grep의 정규식 문법 혼동** ❌
   ```bash
   # 잘못된 방법
   git grep "function.*{" | grep -v test  # 느림

   # 올바른 방법
   git grep -E "function.*\{" main   # Git의 기본 정규식 사용
   git grep -E "function\(" -- src/ # 디렉토리 지정
   ```

2. **Pickaxe로 대소문자 무시하지 않음** ❌
   ```bash
   # 결과 없음 (대소문자 일치 필요)
   git log -S "API_KEY"

   # 올바른 방법 (정규식 사용, Git 2.31+)
   git log -S "[Aa][Pp][Ii]_[Kk][Ee][Yy]"
   ```

3. **성능 무시하고 과도한 검색** ❌
   ```bash
   # 느린 쿼리
   git log -S "." --all  # 모든 문자 포함 (거의 모든 커밋)

   # 최적화된 쿼리
   git log -S "specific_function" -- src/  # 범위 제한
   ```

---

## 🔍 고급: 복합 검색

### 여러 조건 결합

```bash
# 특정 함수가 추가되고, 특정 파일에서만
git log -S "new_function" --all -- src/services/

# 특정 기간의 문자열 변화
git log -S "deprecated_api" --since="2024-01-01" --until="2024-01-31"

# 특정 작성자가 추가한 것
git log -S "pattern" --author="john"
```

### 정규식 Pickaxe (Git 2.28+)

```bash
# -S 대신 -G 사용하면 정규식 기반 Pickaxe
# (파일 자체에서 정규식 매칭되는 라인이 변경된 커밋)
git log -G "API_KEY\s*=" -- config.js

# -S와의 차이점
# -S: 문자열이 정확히 추가/제거됨
# -G: 정규식과 매칭하는 라인이 변경됨
```

### 성능 최적화

```bash
# 성능을 위해 범위 제한
git log -S "pattern" main..HEAD  # main과 HEAD 사이만

# 특정 브랜치 제외
git log -S "pattern" --not origin/master  # master에는 없는 것만

# 첫 번째 발견만
git log -S "pattern" -1  # 가장 최근 발견 1개만
```

---

## 💡 실전 팁

### 검색 결과 내보내기

```bash
# Grep 결과를 파일로
git grep "pattern" > search_results.txt

# Pickaxe 결과를 정렬
git log -S "pattern" --oneline | sort -r
```

### 검색 성능 비교

```bash
# Git Grep (빠름)
time git grep "function_name" main
# real    0m0.041s

# System Grep (느림, 전체 파일 스캔)
time grep -r "function_name" .
# real    0m2.342s
```

---

### 📚 연결 문서

- [Git Blame](git-blame.md) - Grep과 함께 사용하여 코드 변화 추적
- [Git Bisect](git-bisect.md) - Pickaxe와 함께 사용하여 버그 찾기
- [Git 인턴십](../00_fundamentals/git-internals.md) - Grep의 인덱싱 메커니즘
