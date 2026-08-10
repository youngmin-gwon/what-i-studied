---
title: git-bisect
tags: [advanced, debugging, git, bisect]
aliases: [Git Bisect, 이진 탐색, 버그 찾기]
date modified: 2026-08-10
date created: 2026-08-10
---

## Git Bisect: 이진 탐색으로 버그 커밋을 찾아내기

수백 개의 커밋 중에서 어느 커밋에서 버그가 도입되었는지 찾는 것은 악몽입니다. `git bisect` 는 이진 탐색(Binary Search) 알고리즘을 사용하여 단 몇 번의 테스트로 문제의 원인을 찾아냅니다.

### 💡 Why it matters (Context)

- **빠른 버그 원인 파악**: 수백 개의 커밋을 일일이 확인할 필요가 없음.
- **자동화된 검사**: 테스트 스크립트와 결합하여 완전히 자동화된 버그 찾기 가능.
- **팀 커뮤니케이션**: "이 라인을 누가 추가했는가?"를 넘어 "언제 이 버그가 시작되었는가?"를 정확히 파악.

---

## 🏗️ Bisect의 작동 원리

이진 탐색은 범위를 반반씩 나누어 가면서 문제의 원인을 찾습니다.

```
좋은 커밋(Good)                    나쁜 커밋(Bad)
     ↓                                  ↓
  v1.0 ─────── v1.5 ─────── v2.0 ─────── v2.5
              (중간점 검사)
             여기서 버그가 있나?
              ↙              ↘
         v1.0 ─── v1.5    v1.5 ─── v2.0
         (좋음)      (나쁨) → 여기가 원인!
```

---

## 💻 기본 사용법

### 1단계: Bisect 시작

```bash
git bisect start
git bisect bad HEAD         # 현재 커밋(또는 최신)이 버그 있음
git bisect good v1.0        # 이 버전에서는 버그 없음
```

또는 한 줄로:

```bash
git bisect start HEAD v1.0 --
```

### 2단계: 중간 커밋 테스트

Git이 자동으로 중간 커밋을 체크아웃합니다. 그곳에서 버그가 있는지 확인:

```bash
# 테스트 실행
npm test
# or
python -m pytest

# 버그가 있으면
git bisect bad

# 버그가 없으면
git bisect good
```

### 3단계: 반복

Git이 남은 범위의 중간을 다시 체크아웃하고, 위 과정을 반복합니다.

### 4단계: 결과 확인 및 종료

```bash
# 버그를 도입한 첫 번째 커밋 발견!
# Output: e4f5g6h7i8j9k0 is the first bad commit

git bisect reset    # 원래 브랜치로 돌아가기
```

---

## 🏢 실무 사례 (Expert Techniques)

### 케이스 1: 수동 테스트로 버그 찾기

```bash
git bisect start
git bisect bad main         # 현재 main에 버그 있음
git bisect good v1.5.0      # v1.5.0에서는 정상

# Git이 중간 커밋으로 이동, 사용자가 직접 테스트
cd frontend && npm start    # 웹 앱 실행
# 버그 확인됨
git bisect bad

# 다시 중간점 테스트
# (자동 반복)
git bisect good
git bisect bad

# 3~4번 반복하면...
# 버그 원인 커밋 발견!

git show e4f5g6h7          # 버그 커밋 내용 확인
git bisect reset
```

### 케이스 2: 자동화된 Bisect (테스트 스크립트 활용)

```bash
# 테스트 스크립트 작성
cat > test_bug.sh << 'EOF'
#!/bin/bash
npm run build
npm test -- --grep "specific-test"
exit $?
EOF

chmod +x test_bug.sh

# 자동 Bisect 실행
git bisect start
git bisect bad main
git bisect good v1.5.0
git bisect run ./test_bug.sh    # 자동으로 모든 중간점 테스트

# 결과: 첫 번째 실패 커밋 발견!
```

### 케이스 3: 성능 저하의 원인 찾기

```bash
# 성능이 나빠진 커밋 찾기
git bisect start
git bisect bad main
git bisect good v1.0

# 각 중간점에서 벤치마크 실행
# (수동 테스트)
time npm run benchmark

# 느리면 bad, 빠르면 good
git bisect bad
# or
git bisect good
```

---

## 🚨 흔한 실수 (Common Mistakes)

1. **Bad/Good 범위 역설정** ❌
   - `git bisect bad v1.0` (과거) 와 `git bisect good main` (현재) 로 설정하면 잘못된 결과.
   - Good은 정상, Bad는 버그 있음을 기준으로 설정하세요.

2. **Bisect 중 실수로 커밋하기** ❌
   - Bisect 과정 중 코드를 수정하고 커밋하면 검색 범위가 망가집니다.
   - `git bisect reset` 으로 즉시 종료하세요.

3. **자동화 스크립트의 Exit Code 오류** ❌
   - `git bisect run` 사용 시, 스크립트의 exit code가 중요합니다.
   - 0 = 정상(good), 0 이외 = 버그(bad) 로 해석됩니다.

---

## 🔍 추가 팁

### Bisect 상태 저장 및 재개

```bash
# 현재 bisect 상태 저장
git bisect replay log.txt

# 다른 곳에서 상태 복원
git bisect start
git bisect replay log.txt
```

### Bisect 중 특정 커밋 건너뛰기

```bash
# 테스트 불가능한 커밋 (빌드 실패 등)
git bisect skip
```

---

### 📚 연결 문서

- [Git Blame](git-blame.md) - 버그 원인 커밋 발견 후 상세 분석
- [Git 인턴십](../00_fundamentals/git-internals.md) - 커밋 해시와 DAG(방향성 비순환 그래프)
- [트러블슈팅](troubleshooting.md) - Bisect 중 발생하는 충돌 해결
