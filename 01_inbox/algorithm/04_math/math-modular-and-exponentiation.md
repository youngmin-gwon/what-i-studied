---
title: math-modular-and-exponentiation
tags: [algorithm, math, modular, fast-exponentiation, recursion]
aliases: [나머지 연산, 빠른 거듭제곱, 모듈러, 분할 정복을 이용한 거듭제곱]
date modified: 2025-12-18 11:52:16 +09:00
date created: 2025-12-18 11:52:16 +09:00
---

## Modular & Exponentiation: 큰 숫자를 다루는 기술

알고리즘 문제에서 결과값이 너무 커질 경우 **나머지 연산(Modular)**을 요구합니다. 또한 $2^{1000}$ 과 같은 거대한 수를 빠르게 구하기 위해 **빠른 거듭제곱**이 필요합니다.

### 💡 Why it matters (Context)

- **오버플로우 방지**: 컴퓨터가 다룰 수 있는 숫자 범위를 초과하는 경우를 대비해 일정 수로 나눈 나머지만 취합니다.
- **주기성**: 시계나 원형 리스트처럼 특정 범위를 반복하는 구조를 만들 때 사용합니다.
- **암호화**: 공개키 암호학의 핵심 계산 ($C = M^e \mod n$)은 모두 거대한 수의 나머지 연산입니다.

---

### 🏢 실무 사례

#### 활용 분야
- **암호 알고리즘**: RSA, Diffie-Hellman 키 교환에서 모듈러 거듭제곱(Modular Exponentiation) 사용.
- **체크섬/해시**: 데이터 무결성을 검증하기 위한 CRC32, Adler-32 등의 알고리즘.
- **그래픽스**: 텍스처 래핑(Repeat), 색상 값 클램핑.
- **분산 시스템**: Consistent Hashing 을 통한 데이터 노드 배정.
- **게임 개발**: 맵 타일 무한 반복 구현, 난수 생성 알고리즘.

---

## ➗ 나머지 연산 (Modular Arithmetic)

### 성질
나머지 연산은 더하기, 빼기, 곱하기에 대해 분배 법칙이 성립합니다.

1.  $(A + B) \mod M = ((A \mod M) + (B \mod M)) \mod M$
2.  $(A - B) \mod M = ((A \mod M) - (B \mod M) + M) \mod M$ (음수 방지)
3.  $(A \times B) \mod M = ((A \mod M) \times (B \mod M)) \mod M$

> [!CAUTION] **나누기는 안 됩니다!**
> $(A / B) \mod M$ 은 단순히 나눠서 나머지를 취하면 안 됩니다. **페르마의 소정리**를 이용해 **모듈러 역원**을 구해야 합니다.

---

## ⚡ 빠른 거듭제곱 (Fast Exponentiation)

**"분할 정복(Divide & Conquer)을 이용한 지수 법칙"**

$A^{10} = A^5 \times A^5$ 이고, $A^5 = A^2 \times A^2 \times A$ 입니다. 이를 이용하면 $O(N)$ 이 아닌 **$O(\log N)$** 만에 계산 가능합니다.

### 🔧 구현 (Recursive)

```python
def power(a, b, m):
    if b == 0: return 1
    if b == 1: return a % m
    
    # 절반 계산
    half = power(a, b // 2, m)
    
    # 지수가 짝수면 (half * half), 홀수면 (half * half * a)
    if b % 2 == 0:
        return (half * half) % m
    else:
        return (half * half * a) % m
```

### 🔧 구현 (Iterative) - 더 효율적

```python
def fast_pow(base, exp, mod):
    res = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            res = (res * base) % mod
        base = (base * base) % mod
        exp //= 2
    return res
```

---

## 🔑 페르마의 소정리 (Fermat's Little Theorem)

**"모듈러 세계에서의 나눗셈"**

$M$ 이 소수이고 $A$ 가 $M$ 의 배수가 아닐 때, $A^{M-1} \equiv 1 \pmod M$ 입니다.

즉, $A \times A^{M-2} \equiv 1 \pmod M$ 이므로, **$A$ 의 모듈러 역원은 $A^{M-2}$** 입니다.

### 활용: (A / B) mod M 구하기
$$(A \div B) \mod M \Rightarrow (A \times B^{M-2}) \mod M$$

---

## 🎯 실전 패턴

#### Pattern 1: 조합(nCr)의 나머지를 구할 때
팩토리얼 값이 매우 커지므로 중간중간 모듈러를 적용하고, 분모 부분은 페르마의 소정리로 역원을 구해 곱해줍니다.

#### Pattern 2: 거듭제곱 행렬 (Matrix Exponentiation)
피보나치 수열이나 복잡한 점화식을 $O(\log N)$ 만에 해결하고 싶을 때, 행렬의 거듭제곱을 빠른 거듭제곱 방식으로 계산합니다.

---

## 🚨 흔한 실수

1.  **뺄셈 모듈러 누락** ❌
    - `(A - B) % M` 은 결과가 음수가 나올 수 있습니다. 반드시 `(A - B + M) % M` 처럼 처리하세요.
2.  **중간 곱셈 시 오버플로우**
    - `(A * B) % M` 을 할 때 `A * B` 자체가 사용 언어의 정수 범위를 넘지 않는지 확인하세요. (Python은 안전하지만 C++/Java는 `long long` 사용 필수)
3.  **나누기 오해** ❌
    - `(A / B) % M` 을 `(A % M) / (B % M)` 으로 계산하는 실수. 역원을 구해야 합니다.

---

### 📚 연결 문서
- [[04_math/math-prime-number|소수]] - 페르마의 소정리 사용 시 M 이 소수여야 함
- [[04_math/math-combinatorics|조합론]] - nCr 계산 시 모듈러 역원 활용
- [[02_algorithms/dynamic-programming|DP]] - 결과값이 커질 때 모듈러 연산 필수 적용
- [[00_fundamentals/complexity-and-big-o|복잡도]] - $O(\log N)$ 의 효율성
