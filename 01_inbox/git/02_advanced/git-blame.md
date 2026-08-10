---
title: git-blame
tags: [advanced, archaeology, blame, git]
aliases: [Git Blame, 코드 고고학, 커밋 추적]
date modified: 2026-08-10
date created: 2026-08-10
---

## Git Blame: 코드의 모든 라인을 추적하기

파일의 각 라인이 어느 커밋에서 추가/수정되었는지, 누가 작성했는지를 확인하는 강력한 도구입니다. `blame` 이라는 이름은 "비난"을 의미하지만, 실제로는 **코드 변화의 맥락을 파악**하는 고고학적 도구입니다.

### 💡 Why it matters (Context)

- **코드 변화 추적**: "왜" 이 코드가 이렇게 작성되었는지 커밋 메시지를 통해 이해합니다.
- **책임 파악**: 코드 리뷰 시 구현한 의도를 작성자에게 빠르게 확인할 수 있습니다.
- **리팩토링 의사결정**: "이 로직이 언제부터 여기 있었는가?"를 알면 제거해도 되는지 판단 가능.

---

## 🏗️ Git Blame의 기본 사용법

### 전체 파일 분석

```bash
git blame utils.py
```

출력:

```
e4f5g6h7 (John Doe      2024-01-15 10:32:00 +0900) def calculate_total():
a1b2c3d4 (Jane Smith    2024-01-14 14:22:00 +0900)     total = 0
e4f5g6h7 (John Doe      2024-01-15 10:32:00 +0900)     for item in items:
i7j8k9l0 (Bob Johnson   2024-01-16 09:15:00 +0900)         total += item.price
k1l2m3n4 (Jane Smith    2024-01-17 11:45:00 +0900)     return total
```

각 라인 앞의 정보:
- **커밋 해시**: e4f5g6h7 (첫 7글자)
- **작성자**: John Doe
- **날짜**: 2024-01-15 10:32:00
- **타임존**: +0900

### 특정 범위만 분석

```bash
# 10번째부터 20번째 라인만 분석
git blame -L 10,20 utils.py
```

### 특정 커밋 이후의 변화만 보기

```bash
# v1.5.0 태그 이후의 변화만 표시
git blame -S v1.5.0 utils.py
```

---

## 🏢 실무 사례 (Expert Techniques)

### 케이스 1: 특정 라인의 원인 파악하기

```bash
git blame utils.py | grep "calculate_total"

# 출력: e4f5g6h7 (John Doe 2024-01-15 10:32:00 +0900) def calculate_total():

# 해당 커밋의 상세 정보 확인
git show e4f5g6h7

# 커밋 메시지:
# "Refactor: 성능 개선을 위해 루프 로직 변경"
```

이제 왜 그렇게 구현되었는지 이해할 수 있습니다.

### 케이스 2: 포맷팅 변경으로 인한 혼동 피하기

```bash
# 일반 blame
git blame code.py | head -5
# e4f5g6h7 (Auto Formatter  2024-01-20 00:00:00) function() {
# a1b2c3d4 (Auto Formatter  2024-01-20 00:00:00)     return "hello"

# 공백 무시 옵션으로 실제 로직 변경자 찾기
git blame -w code.py | head -5
# k1l2m3n4 (John Doe       2023-12-15 14:22:00) function() {
# a1b2c3d4 (Jane Smith     2023-12-10 11:45:00)     return "hello"
```

`-w` 옵션은 공백/탭만 변경한 커밋을 무시합니다.

### 케이스 3: 순간이동 추적 (Blame의 Blame)

```bash
# 특정 라인이 어디서 왔는지 추적
git blame code.py | grep "suspicious_line"
# e4f5g6h7 (Unknown User 2024-01-10) suspicious_line()

# 해당 라인이 다른 파일에서 복사되었는지 확인
git log --all -S "suspicious_line" --follow code.py

# 또는 더 자세하게
git log -p --all -S "suspicious_line" -- code.py
```

---

## 📋 주요 옵션 정리

| 옵션 | 설명 |
|:---|:---|
| `-L <start>,<end>` | 특정 라인 범위만 분석 |
| `-w` | 공백/탭 변경 무시 |
| `--ignore-rev <commit>` | 특정 커밋 무시 (예: auto-format 커밋) |
| `--ignore-revs-file <file>` | 파일에 나열된 커밋들 무시 |
| `-C` | 코드 이동 감지 (같은 파일 내) |
| `-CC` | 코드 이동 감지 (다른 파일에서) |
| `--date=short` | 날짜 형식 변경 |

### 자동 포맷팅 커밋 제외하기 (고급)

```bash
# .git-blame-ignore-revs 파일 생성
cat > .git-blame-ignore-revs << 'EOF'
# Formatter: Auto-format all files
e4f5g6h7i8j9k0l1m2n3o4p5q6r7s8t9u0v1w2x3

# CI: Update dependencies
a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0
EOF

# Git 설정에 등록
git config blame.ignoreRevsFile .git-blame-ignore-revs

# 이제 blame에서 이 커밋들이 제외됨
git blame code.py
```

---

## 🚨 흔한 실수 (Common Mistakes)

1. **Blame 으로 "범인" 찾기** ⚠️
   - 마지막 수정자가 로직을 짠 사람이 아닐 수 있습니다.
   - 예: 포맷팅만 수정한 사람, 병합 커밋의 자동 변경 등.
   - 항상 `git show <commit>` 으로 실제 변경 내용을 확인하세요.

2. **대규모 포맷팅 커밋 후 Blame 해석 오류** ❌
   - 전체 코드를 Auto-formatter로 포맷팅한 후 blame하면 모든 라인이 포맷터 커밋으로 보입니다.
   - `-w` 옵션이나 `--ignore-revs-file` 을 반드시 사용하세요.

3. **마지막 수정자와 로직 작성자 혼동** ❌
   - `git blame` 은 "마지막 수정" 을 보여줍니다.
   - 원래 로직의 작성자를 찾으려면 `-C` 옵션으로 코드 이동을 추적하거나 `git log -p` 로 직접 확인해야 합니다.

---

## 🔍 고급 팁: 여러 버전의 Blame 비교

```bash
# 두 커밋 사이의 변화 비교
git blame <commit1> -- file.py > blame1.txt
git blame <commit2> -- file.py > blame2.txt
diff blame1.txt blame2.txt

# 특정 함수의 변화 추적
git log -p -S "function_name" -- file.py
```

---

### 📚 연결 문서

- [Git Bisect](git-bisect.md) - 버그 원인 찾기 (Blame과 함께 사용)
- [Git 인턴십](../00_fundamentals/git-internals.md) - 커밋과 객체 참조 구조
- [트러블슈팅](troubleshooting.md) - 히스토리 추적 중 충돌 해결
