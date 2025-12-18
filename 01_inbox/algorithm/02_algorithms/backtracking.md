---
title: backtracking
tags: [algorithm, backtracking, permutation, combination, recursion]
aliases: [백트래킹, 되추적, Permutation, Combination]
date modified: 2025-12-18 11:45:41 +09:00
date created: 2025-12-18 11:45:41 +09:00
---

## Backtracking: "시도 → 실패하면 되돌리기"

**핵심**: **모든 가능성을 탐색**하되, **불가능한 경로는 빠르게 포기 (가지치기)**

Backtracking은 **DFS + 가지치기(Pruning)**입니다. "일단 해보고, 안 되면 되돌아가서 다른 길 시도"

### 💡 Why it matters (Context)

- **N-Queens**: N×N 체스판에 N개 퀸 배치
- **스도쿠 풀이**: 9×9 칸 채우기
- **조합 생성**: "5명 중 3명 뽑기"
- **부분집합 합**: "합이 10이 되는 부분집합"

---

### 🏢 실무 사례

#### Backtracking 활용
- **구글 캘린더**: 회의실 스케줄링 최적화 (Constraint Satisfaction)
- **Sudoku Solver (앱)**: 스도쿠 자동 풀이
- **정규표현식 엔진**: 패턴 매칭 (PCRE, grep)
- **배송 경로 최적화**: 제약 조건 만족 경로 찾기 (TSP 변형)
- **CI/CD 의존성 해결**: 순환 의존성 탐지 및 순서 찾기
- **게임 AI**: 체스/바둑 다음 수 탐색 (Minimax + Pruning)
- **컴파일러**: 구문 분석 (Parsing) 백트래킹

---

## 🎯 Backtracking vs DFS vs Brute Force

| 기법 | 탐색 방식 | 최적화 |
|:---|:---|:---|
| **Brute Force** | 모든 경우 다 봄 | 없음 ❌ |
| **DFS** | 깊이 우선 탐색 | 없음 |
| **Backtracking** | DFS + **가지치기** | ✅ 불가능한 경로 포기 |

> [!IMPORTANT] **핵심 차이**
> Backtracking은 "**일찍 포기**"가 핵심입니다.
> 
> 예: N-Queens에서 이미 같은 행에 퀸이 있으면, 그 경로의 모든 하위 탐색을 **즉시 중단**

---

## 🔧 기본 템플릿

```python
def backtrack(path, choices):
    # 1. 종료 조건 (답을 찾았거나 더 이상 선택 불가)
    if is_solution(path):
        result.append(path[:])  # 복사본 저장!
        return
    
    # 2. 가능한 선택지들을 탐색
    for choice in choices:
        # 3. 가지치기 (Pruning) - 불가능한 경우 건너뛰기
        if not is_valid(choice):
            continue
        
        # 4. 선택
        path.append(choice)
        
        # 5. 다음 단계로 재귀
        backtrack(path, next_choices)
        
        # 6. 선택 취소 (Backtrack!)
        path.pop()
```

**핵심 3단계**: **선택 → 탐색 → 취소**

---

## 🔥 필수 Backtracking 패턴

### Pattern 1: Permutation (순열)

**문제**: [1, 2, 3]의 모든 순열

```python
def permute(nums):
    result = []
    
    def backtrack(path, used):
        # 종료: 모든 숫자를 사용했으면
        if len(path) == len(nums):
            result.append(path[:])
            return
        
        for i in range(len(nums)):
            # 가지치기: 이미 사용한 숫자는 건너뛰기
            if used[i]:
                continue
            
            # 선택
            path.append(nums[i])
            used[i] = True
            
            # 탐색
            backtrack(path, used)
            
            # 취소
            path.pop()
            used[i] = False
    
    backtrack([], [False] * len(nums))
    return result

# [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
```

**시간 복잡도**: O(N! × N) - N개 순열 생성, 각 N 복사

---

### Pattern 2: Combination (조합)

**문제**: [1, 2, 3, 4] 중 2개 선택

```python
def combine(n, k):
    result = []
    
    def backtrack(start, path):
        # 종료: k개를 선택했으면
        if len(path) == k:
            result.append(path[:])
            return
        
        # start부터 시작 (중복 방지)
        for i in range(start, n + 1):
            # 선택
            path.append(i)
            
            # 탐색 (i+1부터 - 자기 자신 제외)
            backtrack(i + 1, path)
            
            # 취소
            path.pop()
    
    backtrack(1, [])
    return result

# combine(4, 2) → [[1,2], [1,3], [1,4], [2,3], [2,4], [3,4]]
```

**핵심**: `start` 매개변수로 **순서 제거** (1,2와 2,1은 같음)

---

### Pattern 3: Subsets (부분집합)

**문제**: [1, 2, 3]의 모든 부분집합 (2^n 개)

```python
def subsets(nums):
    result = []
    
    def backtrack(start, path):
        # 모든 경로가 답! (종료 조건 없음)
        result.append(path[:])
        
        for i in range(start, len(nums)):
            # 선택
            path.append(nums[i])
            
            # 탐색
            backtrack(i + 1, path)
            
            # 취소
            path.pop()
    
    backtrack(0, [])
    return result

# [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]
```

**비트마스크 방법** (더 빠름):
```python
def subsets_bitmask(nums):
    n = len(nums)
    result = []
    
    # 2^n 가지 경우
    for mask in range(1 << n):  # 0 ~ 2^n - 1
        subset = []
        for i in range(n):
            # i번째 비트가 1이면 포함
            if mask & (1 << i):
                subset.append(nums[i])
        result.append(subset)
    
    return result
```

---

### Pattern 4: N-Queens

**문제**: N×N 체스판에 N개 퀸이 서로 공격하지 않게 배치

```python
def solve_n_queens(n):
    result = []
    board = [['.'] * n for _ in range(n)]
    
    def is_valid(row, col):
        # 같은 열 체크
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        
        # 왼쪽 대각선 체크
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        
        # 오른쪽 대각선 체크
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        
        return True
    
    def backtrack(row):
        # 종료: 모든 행에 퀸 배치 성공
        if row == n:
            result.append([''.join(row) for row in board])
            return
        
        # 현재 행의 각 열에 퀸 시도
        for col in range(n):
            # 가지치기: 유효하지 않으면 건너뛰기
            if not is_valid(row, col):
                continue
            
            # 선택
            board[row][col] = 'Q'
            
            # 다음 행으로
            backtrack(row + 1)
            
            # 취소
            board[row][col] = '.'
    
    backtrack(0)
    return result
```

**최적화 버전** (Set 사용):
```python
def solve_n_queens_opt(n):
    result = []
    cols = set()         # 사용된 열
    diag1 = set()        # 사용된 \ 대각선 (row - col)
    diag2 = set()        # 사용된 / 대각선 (row + col)
    
    def backtrack(row, board):
        if row == n:
            result.append(board[:])
            return
        
        for col in range(n):
            # 가지치기: O(1) 체크!
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue
            
            # 선택
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            
            # 탐색
            backtrack(row + 1, board + ['.' * col + 'Q' + '.' * (n - col - 1)])
            
            # 취소
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)
    
    backtrack(0, [])
    return result
```

---

### Pattern 5: Sudoku Solver

```python
def solve_sudoku(board):
    """
    board: 9x9 리스트, '.'는 빈 칸
    """
    def is_valid(row, col, num):
        # 행 체크
        if num in board[row]:
            return False
        
        # 열 체크
        if num in [board[i][col] for i in range(9)]:
            return False
        
        # 3x3 박스 체크
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if board[i][j] == num:
                    return False
        
        return True
    
    def backtrack():
        # 빈 칸 찾기
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    # 1~9 시도
                    for num in '123456789':
                        # 가지치기
                        if not is_valid(i, j, num):
                            continue
                        
                        # 선택
                        board[i][j] = num
                        
                        # 탐색
                        if backtrack():
                            return True  # 성공!
                        
                        # 취소
                        board[i][j] = '.'
                    
                    return False  # 1~9 모두 실패
        
        return True  # 빈 칸 없음 = 완성!
    
    backtrack()
```

---

### Pattern 6: Palindrome Partitioning

**문제**: 문자열을 회문으로만 분할

```python
def partition(s):
    result = []
    
    def is_palindrome(sub):
        return sub == sub[::-1]
    
    def backtrack(start, path):
        # 종료: 문자열 끝까지 처리
        if start == len(s):
            result.append(path[:])
            return
        
        # 현재 위치부터 가능한 모든 분할
        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            
            # 가지치기: 회문이 아니면 건너뛰기
            if not is_palindrome(substring):
                continue
            
            # 선택
            path.append(substring)
            
            # 탐색
            backtrack(end, path)
            
            # 취소
            path.pop()
    
    backtrack(0, [])
    return result

# "aab" → [["a","a","b"], ["aa","b"]]
```

---

### Pattern 7: Word Search (2D Grid)

**문제**: 2D 보드에서 단어 찾기

```python
def exist(board, word):
    rows, cols = len(board), len(board[0])
    
    def backtrack(r, c, index):
        # 종료: 단어 완성
        if index == len(word):
            return True
        
        # 범위 체크 & 문자 일치 체크
        if (r < 0 or r >= rows or c < 0 or c >= cols or
            board[r][c] != word[index]):
            return False
        
        # 선택 (방문 표시)
        temp = board[r][c]
        board[r][c] = '#'  # 방문 마킹
        
        # 4방향 탐색
        found = (backtrack(r+1, c, index+1) or
                 backtrack(r-1, c, index+1) or
                 backtrack(r, c+1, index+1) or
                 backtrack(r, c-1, index+1))
        
        # 취소 (방문 해제)
        board[r][c] = temp
        
        return found
    
    # 모든 시작점 시도
    for i in range(rows):
        for j in range(cols):
            if backtrack(i, j, 0):
                return True
    
    return False
```

---

## 🎓 Backtracking 문제 해결 전략

### 1. **상태 공간 정의**
"무엇을 선택하고, 무엇을 기억할 것인가?"

### 2. **가지치기 조건 찾기**
"어떤 경우에 더 이상 진행할 필요가 없는가?"

```python
# N-Queens: 이미 같은 열에 퀸이 있으면 중단
if col in used_cols:
    continue  # 가지치기!
```

### 3. **복원 확인**
"선택을 취소할 때 상태가 완전히 복원되는가?"

```python
# 잘못된 예 ❌
path.append(choice)  # 선택
# ... 탐색 ...
# path.pop() 누락! - 상태 복원 안 됨

# 올바른 예 ✅
path.append(choice)
backtrack(...)
path.pop()  # 반드시 복원!
```

---

## 🚨 흔한 실수

1. **복사본 저장 안 함** ❌
   ```python
   # 잘못된 방법
   result.append(path)  # ❌ 참조만 저장!
   
   # 올바른 방법
   result.append(path[:])  # ✅ 복사본 저장
   ```

2. **방문 표시 복원 누락**
   ```python
   visited[i] = True
   backtrack(...)
   visited[i] = False  # ✅ 반드시 복원!
   ```

3. **start 인덱스 잘못 설정**
   ```python
   # Combination: i+1로 다음 시작
   for i in range(start, n):
       backtrack(i + 1, ...)  # ✅
   
   # Permutation: 0부터 시작 (used 체크)
   for i in range(n):
       if not used[i]:
           backtrack(...)  # ✅
   ```

4. **재귀 깊이 제한**
   - Python: `sys.setrecursionlimit(10**6)`

---

## ⚡ 최적화 기법

### 1. **조기 종료**
```python
# 답을 하나만 찾으면 되는 경우
if found:
    return True  # 더 이상 탐색 중단
```

### 2. **가지치기 강화**
```python
# N-Queens: Set으로 O(1) 체크
if col in cols:  # O(1) vs 리스트 탐색 O(n)
    continue
```

### 3. **최적화된 순서**
```python
# Sudoku: 선택지가 적은 칸부터 채우기
# (Heuristic - Most Constrained Variable)
```

---

## 🧪 고급 응용

### Constraint Satisfaction Problem (CSP)
- N-Queens, Sudoku의 일반화
- Arc Consistency, Forward Checking

### Combinatorial Optimization
- 외판원 문제 (TSP) - Backtracking + Branch & Bound

---

### 📚 연결 문서
- [[02_algorithms/graph-traversal|그래프 탐색]] - DFS 기초
- [[02_algorithms/dynamic-programming|DP]] - Backtracking vs DP 비교
- [[01_data-structures/tree-and-graph|트리]] - 탐색 공간 트리
- [[00_fundamentals/complexity-and-big-o|복잡도]] - 지수 시간 이해
