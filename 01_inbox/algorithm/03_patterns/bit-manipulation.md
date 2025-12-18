---
title: bit-manipulation
tags: [algorithm, math, bit, optimization, bit-manipulation]
aliases: [비트 연산, 비트 마스킹, Bit Manipulation, Bit Masking]
date modified: 2025-12-18 11:53:38 +09:00
date created: 2025-12-18 11:53:38 +09:00
---

## Bit Manipulation: 비트로 공간과 속도 쥐어짜기

정수를 비트(0과 1) 단위로 직접 조작하여 **극도로 빠른 연산**과 **메모리 절약**을 달성하는 기법입니다.

### 💡 Why it matters (Context)

- **메모리 극대화**: `boolean` 배열 32개 대신 `int` 하나(32개 비트)로 상태 저장.
- **상수 시간 연산**: 산술 연산보다 비트 연산이 CPU 수준에서 훨씬 빠릅니다.
- **집합 표현**: 특정 원소가 있는지 없는지를 비트의 On/Off로 표현 (Subset).

---

### 🏢 실무 사례

#### Bit Manipulation 활용
- **임베디드/커널**: 하드웨어 레지스터 제어 (특정 핀 활성화).
- **네트워크**: 서브넷 마스크(Subnet Mask) 계산 및 패킷 플래그 처리.
- **그래픽스**: ARGB 색상 값 추출 (Shift 연산으로 R, G, B 분리).
- **데이터 압축**: 비트 단위 인코딩 (Huffman Coding 등).
- **암호학**: XOR 연산을 이용한 단순 암호화 및 해시 함수 엔진.

---

## 🛠️ 기초 비트 연산자

| 연산자 | 기호 | 설명 |
|:---|:---:|:---|
| **AND** | `&` | 둘 다 1일 때만 1 |
| **OR** | `\|` | 하나라도 1이면 1 |
| **XOR** | `^` | 서로 다를 때만 1 (암호학 단골) |
| **NOT** | `~` | 비트 반전 |
| **Shift** | `<<`, `>>` | 비트를 왼쪽/오른쪽으로 밀기 |

---

## 🔥 필수 비트 패턴

### 1. n번째 비트 조작 (Bit Masking)
- **i번째 비트 확인**: `num & (1 << i)`
- **i번째 비트 1로 설정**: `num | (1 << i)`
- **i번째 비트 0으로 설정**: `num & ~(1 << i)`
- **i번째 비트 반전 (Toggle)**: `num ^ (1 << i)`

### 2. XOR의 특별한 성질
XOR은 **"같은 것을 두 번 하면 원래대로 돌아온다"**는 성질이 있습니다 (`A ^ B ^ B = A`).
- **중복 없는 숫자 찾기**: 배열에서 모든 숫자가 두 번씩 나오고 하나만 혼자일 때, 모두 XOR 하면 혼자인 숫자가 남습니다.

```python
def find_single_number(nums):
    res = 0
    for n in nums:
        res ^= n
    return res
```

### 3. 홀수/짝수 판별 (가장 빠름)
```python
if num & 1:
    print("홀수")
else:
    print("짝수")
```

### 4. 2의 거듭제곱 확인
```python
# 2의 거듭제곱(2, 4, 8...)은 비트가 딱 하나만 켜져 있음
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0
```

---

## 🎨 비트 마스크 집합 (Bitmask Set)

정수 하나를 집합처럼 사용할 수 있습니다. (원소 개수가 31개 이하일 때)

```python
# 집합 관리 예시
full_set = (1 << n) - 1  # 모든 원소가 포함된 집합
empth_set = 0

# i번 원소 추가
set |= (1 << i)

# i번 원소 포함 여부
if set & (1 << i):
    print("포함됨")

# 모든 부분 집합 순회
for mask in range(1 << n):
    # 각 mask가 하나의 부분 집합
    pass
```

---

## 🚨 흔한 실수 (Common Mistakes)

1. **연산자 우선순위** ⚠️ (가장 위험!)
   - `if num & 1 == 0:` 이라고 쓰면 `1 == 0`이 먼저 계산될 수 있습니다 (언어마다 다름).
   - 반드시 괄호를 치세요: `if (num & 1) == 0:` ✅
2. **부호 비트 (Signed Bit) 주의**
   - 음수를 오른쪽 시프트(`>>`) 할 때 부호 비트가 채워지는 방식(Arithmetic vs Logical)이 언어마다 다를 수 있습니다. (Python은 무한 정수라 독특함)
3. **오버플로우**
   - 32비트 정수 범위를 넘어서는 비트 이동 주의.

---

---

## 📚 관련 문서
- [[04_math/math-modular-and-exponentiation|수학적 기초]] - 비트 분할을 활용한 빠른 거듭제곱 알고리즘
- [[02_algorithms/backtracking|백트래킹]] - 모든 부분집합 생성 시 비트 마스크 활용 최적화
- [[01_data-structures/hash-and-map|해시와 맵]] - 공간 효율성이 극대화된 비트셋(Bitset)의 대안
- [[00_fundamentals/complexity-and-big-o|복잡도 분석]] - 상수 시간($O(1)$)에 실행되는 비트 연산의 특징
- [[01_data-structures/linear|선형 자료구조]] - 비트 수준에서의 데이터 저장 및 처리 원리
