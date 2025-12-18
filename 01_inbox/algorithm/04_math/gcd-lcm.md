---
title: gcd-lcm
tags: [algorithm, euclidean-algorithm, gcd, lcm, math, number-theory]
aliases: [유클리드 호제법, 최대공약수, 최소공배수]
date modified: 2025-12-18 11:42:47 +09:00
date created: 2025-12-18 10:07:51 +09:00
---

## GCD & LCM: 정수론의 기초 알고리즘

최대공약수 (GCD) 와 최소공배수 (LCM) 는 단순한 수학 공식이 아닙니다. **암호학 (RSA), 해시 함수, 배열 회전** 등 다양한 알고리즘의 핵심 요소입니다.

### 🎯 정의

#### GCD (Greatest Common Divisor)

**최대공약수**: 두 정수의 공통 약수 중 가장 큰 수

- `gcd(12, 18) = 6`
- `gcd(17, 19) = 1` (서로소, Coprime)

#### LCM (Least Common Multiple)

**최소공배수**: 두 정수의 공통 배수 중 가장 작은 수

- `lcm(12, 18) = 36`

#### 🔗 관계식

$$LCM(a, b) = \frac{|a \times b|}{GCD(a, b)}$$

>[!TIP] **왜 곱해서 나누나?**
>12 와 18 의 소인수분해를 보면:
> - `12 = 2² × 3`
> - `18 = 2 × 3²`
> - `gcd = 2 × 3 = 6` (공통 최소 지수)
> - `lcm = 2² × 3² = 36` (각 소인수의 최대 지수)
> - `12 × 18 / 6 = 216 / 6 = 36` ✅

---

### 🧮 Euclidean Algorithm (유클리드 호제법)

**O(log min(a, b))** 로 GCD 를 구하는 고대 알고리즘 (기원전 300 년). 현대 암호학의 기초입니다.

#### 원리

**"두 수의 GCD 는 작은 수와 나머지의 GCD 와 같다"**

```text
gcd(48, 18) 
= gcd(18, 48 % 18)  // 48 = 18 × 2 + 12
= gcd(18, 12)
= gcd(12, 18 % 12)  // 18 = 12 × 1 + 6
= gcd(12, 6)
= gcd(6, 12 % 6)    // 12 = 6 × 2 + 0
= gcd(6, 0)
= 6  // 나머지가 0이면 나누는 수(6)가 GCD
```

#### 구현

```python
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)
```

```swift
// Swift 재귀 버전
func gcd(_ a: Int, _ b: Int) -> Int {
    return b == 0 ? a : gcd(b, a % b)
}

func lcm(_ a: Int, _ b: Int) -> Int {
    return abs(a * b) / gcd(a, b)
}
```

>[!WARNING] **오버플로우 주의**
>`a × b` 계산 시 정수 오버플로우가 날 수 있습니다. 큰 수를 다룰 때는 `a / gcd(a, b) * b` 순서로 계산하세요.

---

### 🔄 Juggling Algorithm (배열 회전)

GCD 를 이용해 **배열을 O(n) 시간, O(1) 공간**으로 회전시키는 알고리즘입니다.

#### 문제

배열 `[1, 2, 3, 4, 5, 6]` 을 왼쪽으로 `k=2` 칸 회전 → `[3, 4, 5, 6, 1, 2]`

#### 원리

GCD(n, k) 개의 **독립적인 사이클 (Cycle)** 로 나눠서 회전합니다.

- `n=6, k=2` → `gcd(6, 2) = 2` → 2 개의 사이클
- **사이클 1**: `[0] → [2] → [4] → [0]` (인덱스: 0, 2, 4)
- **사이클 2**: `[1] → [3] → [5] → [1]` (인덱스: 1, 3, 5)

```cpp
void ArrayRotate(int A[], int n, int k) {
    int d = -1, i, temp, j;
    
    for (i = 0; i < gcd(n, k); i++) { // GCD 개수만큼 사이클
        j = i;
        temp = A[i];
        
        while (1) {
            d = (j + k) % n;  // 다음 위치
            
            if (d == i) {  // 사이클 완성
                break;
            }
            A[j] = A[d];  // 왼쪽으로 이동
            j = d;
        }
        A[j] = temp;  // 사이클의 마지막에 첫 값 배치
    }
}
```

#### 시간 복잡도

- 각 요소를 정확히 한 번씩만 이동: **O(n)**
- 추가 배열 불필요: **O(1) Space**

---

### 🔐 실전 응용

#### 1. RSA 암호화

공개키 암호의 핵심: `gcd(e, φ(n)) = 1` (서로소) 인 `e` 를 찾아야 합니다.

#### 2. Hash Table Probing

충돌 시 `hash + i × step` 으로 탐색할 때, **`gcd(step, tableSize) = 1`** 이어야 모든 슬롯을 탐색할 수 있습니다.

#### 3. 분수 기약분수화

`12/18 = (12÷6) / (18÷6) = 2/3`

---

#---

## 📚 관련 문서
- [[00_fundamentals/complexity-and-big-o|복잡도 분석]] - 유클리드 호제법의 로그 시간($O(\log N)$) 효율성 이해
- [[02_algorithms/search-and-sort|검색과 정렬]] - 정렬된 데이터를 다루는 배열 회전(Array Rotation) 응용
- [[01_data-structures/linear|배열과 리스트]] - 배열의 메모리 레이아웃과 포인터 연산의 기초
- [[04_math/math-prime-number|소수와 수론]] - 최대공약수가 1인 서로소(Coprime) 관계의 중요성
- [[04_math/math-modular-and-exponentiation|나머지 연산]] - 거대 숫자의 연산과 모듈러 역원 계산의 토대
