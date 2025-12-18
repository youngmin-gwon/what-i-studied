---
title: hash-and-map
tags: [algorithm, collision, data-structures, dictionary, hash-table, map, security]
aliases: [딕셔너리, 해시 맵, 해시 테이블]
date modified: 2025-12-18 11:41:26 +09:00
date created: 2025-12-17 19:20:00 +09:00
---

## Hash Table: O(1) 의 마법과 대가

배열의 인덱스 접근은 빠르지만, 숫자로만 접근해야 합니다.

**"사람의 언어 (String) 를 배열의 언어 (Index) 로 통역해 주는 기계"**, 그것이 바로 해시 함수입니다.

### 🎩 How Hash Map Works

`dict["apple"] = 100` 을 실행하면 내부적으로 무슨 일이 일어날까요?

1. **Hashing**: `"apple"` 이라는 키를 해시 함수에 넣습니다. -> `948210` 같은 거대한 정수가 나옵니다.
2. **Modulo**: 배열 크기 (Bucket Size) 로 나눕니다. `948210 % 16 = 2`.
3. **Access**: 배열의 `2` 번 인덱스에 값 `100` 을 저장합니다.
    - 이 3 단계는 입력 크기와 상관없이 항상 일정하므로 **O(1)**입니다.

---

### 💥 충돌 (Collision): 비둘기집 원리

해시 함수가 아무리 좋아도, 배열 크기가 한정되어 있다면 서로 다른 키가 같은 인덱스를 가리킬 수밖에 없습니다. (`948210 % 16` 과 `34 % 16` 은 둘 다 `2` 입니다.) 이를 **충돌**이라고 합니다.

#### 해결 전략 (Collision Resolution)

##### 1. Separate Chaining (체이닝)
- **방식**: 각 버킷 (Bucket) 에 **Linked List**를 매달아 둡니다. 충돌이 나면 리스트 뒤에 연결합니다.
- **장점**: 구현이 쉽고 삭제가 안전합니다.
- **단점**: 메모리를 추가로 쓰고, Linked List 특성상 [[algo-ds-linear#Cache Locality (캐시 지역성)|Cache Miss]] 가 많습니다.
- **사용**: **Swift**, Java, Go.

##### 2. Open Addressing (개방 주소법)
- **방식**: 충돌이 나면 옆집 (`index + 1`) 을 봅니다. 빈자리가 나올 때까지 찾습니다 (Probing).
- **장점**: 추가 메모리 (포인터) 가 필요 없고 Cache Line 활용이 좋습니다.
- **단점**: 데이터가 꽉 차면 성능이 급격히 떨어집니다.
- **사용**: Python, Ruby.

---

### 📈 Resizing (재할당)

해시 테이블은 배열이 꽉 차면 성능이 O(n) 에 가까워집니다. 그래서 보통 75% 정도 차면 (**Load Factor 0.75**), 배열 크기를 2 배로 늘립니다.

- **Rehashing**: 단순히 배열만 늘리는 게 아니라, **모든 키를 다시 해싱해서 새 위치로 옮겨야 합니다.** (`modulo` 값이 바뀌니까요)
- **비용**: 이 작업은 **O(n)**입니다. [[algo-complexity-and-big-o#💾 Amortized Analysis (분할 상환 분석)|분할 상환 분석]] 에 따르면 평균은 O(1) 이지만, Rehashing 이 터지는 순간 렉이 걸릴 수 있습니다.

---

### 🛡️ Security: Hash Flooding Attack (해시 플러딩 공격)

공격자가 의도적으로 **같은 해시 값을 가진 키 (악의적인 입력)**를 수십만 개 보낸다면?

모든 데이터가 **한 버킷의 Linked List**에 연결됩니다. 그러면 조회 속도가 O(1) 에서 **O(n)**으로 떨어집니다. 서버의 CPU 는 연결 리스트를 뒤지느라 100% 가 되고 멈춥니다 (DoS).

**방어법 (SipHash)**:
- 해시 함수에 **Random Seed(앱이 켜질 때마다 바뀌는 난수)**를 섞습니다.
- 공격자는 서버의 Seed 를 모르므로 충돌하는 키를 생성할 수 없습니다.
- Swift, Python, Rust 등 현대 언어들은 기본적으로 이 방어 기법을 내장하고 있습니다.

#### 📚 연결 문서
- [[algo-ds-linear]] - 충돌 해결에 쓰이는 Linked List
- [[algo-complexity-and-big-o]] - O(1) 의 의미
- [[apple-foundation]] - Swift Dictionary 구현체
