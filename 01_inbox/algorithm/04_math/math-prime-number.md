---
title: math-prime-number
tags: [algorithm, math, number-theory, prime-number, sieve-of-eratosthenes]
aliases: [소수, 소수 판별, 소인수분해, 에라토스테네스의 체]
date modified: 2025-12-18 15:27:10 +09:00
date created: 2025-12-18 11:52:16 +09:00
---

## Prime Numbers: 소수의 마법

**소수(Prime Number)**는 1 과 자기 자신만으로 나누어떨어지는 1 보다 큰 자연수입니다. 현대 암호학의 근간이자, 수론에서 핵심적인 역할을 합니다.

### 💡 Why it matters (Context)

- **암호학**: 공개키 암호 알고리즘(RSA)의 안전성은 "거대한 두 소수의 곱을 다시 소인수분해하기 어렵다"는 점에 착안합니다.
- **해시 테이블**: 해시 충돌을 줄이기 위해 테이블 크기를 소수로 설정하는 경우가 많습니다.
- **주기성**: 두 톱니바퀴의 이빨 수가 서로소(소수 관계)일 때 마모가 균등해집니다.

---

### 🏢 실무 사례

#### 소수 알고리즘 활용
- **보안/인증**: SSL/TLS 인증서 발급 시 거대 소수 생성 및 판별.
- **데이터베이스**: 인덱스 버킷 크기 최적화 (소수를 사용해 데이터를 고르게 분산).
- **게임 엔진**: 난수 생성기(PRNG)의 주기 설정에 소수 활용.
- **통신**: 주파수 간섭을 최소화하기 위해 소수 단위의 채널 간격 설정.

---

## 🔍 소수 판별 (Primality Test)

### 1. 단순한 방법 (O(N))

2 부터 N-1 까지 모두 나눠보기. (비효율적)

### 2. 최적화된 방법 (O(√N))

N 이 $a \times b$ 라면, 둘 중 하나는 반드시 $\sqrt{N}$ 보다 작거나 같습니다. 따라서 $\sqrt{N}$ 까지만 확인하면 충분합니다.

```python
def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False  # 짝수 제외
    
    # 3부터 루트 n까지 홀수만 확인
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
```

---

## 🕸️ 에라토스테네스의 체 (Sieve of Eratosthenes)

**"대량의 소수를 한꺼번에 구할 때"** 사용하는 가장 효율적인 방법입니다.

### 원리
1. 2 부터 N 까지 모든 수를 나열한다.
2. 아직 지워지지 않은 수 중 가장 작은 수(소수)를 찾는다.
3. 그 수의 **배수**를 모두 지운다.
4. 더 이상 지울 배수가 없을 때까지 반복한다.

```python
def get_primes_sieve(n):
    if n < 2: return []
    
    # 처음에는 모두 소수(True)로 초기화
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            # i가 소수라면, i의 배수들을 모두 False로 (i*i부터 시작 가능)
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
                
    return [i for i, val in enumerate(is_prime) if val]
```

**시간 복잡도**: **O(N log log N)** (사실상 선형 시간에 가까움)

---

## 🔢 소인수분해 (Prime Factorization)

어떤 수를 소수들의 곱으로 나타내는 것입니다.

```python
def prime_factorization(n):
    factors = []
    d = 2
    temp = n
    while d * d <= temp:
        while temp % d == 0:
            factors.append(d)
            temp //= d
        d += 1
    if temp > 1:
        factors.append(temp)
    return factors

# 72 → [2, 2, 2, 3, 3]
```

---

## 🎯 실전 패턴

### Pattern 1: 소수 사이의 거리 (Goldbach's Conjecture)

"2 보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다." → 체를 미리 만들어두고 투 포인터로 접근.

### Pattern 2: 범위 내 소수 개수 쿼리

에라토스테네스의 체 + **누적 합(Prefix Sum)**을 이용해 특정 구간 [a, b]의 소수 개수를 O(1)에 구하기.

---

## 🚨 흔한 실수

1. **1 을 소수로 착각** ❌
   - 소수는 반드시 1 보다 커야 합니다. 코드에서 `n < 2` 예외 처리를 잊지 마세요.
2. **루트 N 까지 범위 미포함** ❌
   - `range(2, int(n**0.5))` 라고 쓰면 루트 N 일 때를 검사하지 않습니다. 반드시 `+ 1` 을 해주세요.
3. **체(Sieve) 메모리 부족**
   - N 이 1 억(10^8)을 넘어가면 배열 크기 때문에 메모리 초과가 발생할 수 있습니다. 이럴 땐 **비트마스킹**이나 **세그먼트 체**를 고려해야 합니다.

---

### 📚 연결 문서
- [GCD & LCM](gcd-lcm.md) - 서로소 관계의 핵심
- [큰 숫자를 다루는 기술](math-modular-and-exponentiation.md) - 소수 모듈러 역원(페르마의 소정리)
- [Big-O](../00_fundamentals/complexity-and-big-o.md) - 루트 N 과 로그 로그 N 의 이해
