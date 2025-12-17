---
title: algo-pattern-two-pointers
tags: [algorithm, pattern, two-pointers, sliding-window, array]
aliases: [투 포인터, 슬라이딩 윈도우]
date modified: 2025-12-18 05:00:00 +09:00
date created: 2025-12-17 20:00:00 +09:00
---

# Two Pointers & Sliding Window: O(n^2)을 O(n)으로

배열에서 "구간"이나 "쌍(Pair)"을 구할 때, 이중 for loop(`O(n^2)`)를 쓰기 쉽습니다.
하지만 포인터 두 개를 동시에 움직이면 `O(n)`으로 최적화할 수 있습니다.

## 👈👉 Two Pointers (양쪽에서 조이기)

주로 **정렬된 배열**에서 두 수의 합(Two Sum) 등을 찾을 때 씁니다.

1.  `Left`는 0, `Right`는 끝(n-1)에 둡니다.
2.  두 합이 목표보다 크면? `Right`를 줄여서 합을 작게 만듭니다.
3.  두 합이 목표보다 작으면? `Left`를 키워서 합을 크게 만듭니다.
-   **Why O(n)?**: `Left`와 `Right`는 각각 최대 N번만 움직입니다.

---

## 🪟 Sliding Window (창문 밀기)

배열의 **연속된 구간(Subarray)**을 처리할 때 씁니다. 창문틀(Window)을 만들어 오른쪽으로 스르륵 밉니다.

-   **핵심**: 창문이 한 칸 이동할 때, **새로 들어온 놈(Add)**과 **나가는 놈(Remove)**만 처리합니다.
-   **Complexity**: 창문의 크기가 커져도, 각 요소는 창문에 '들어올 때'와 '나갈 때' 딱 두 번만 계산됩니다. -> **O(n)**.

### Context: TCP Sliding Window
TCP 프로토콜도 이 알고리즘을 씁니다.
-   패킷 하나 보내고 ACK 기다리면 너무 느립니다.
-   "아직 ACK 안 왔어도 10개까지는 미리 보내자(Window Size = 10)"라고 약속합니다.
-   ACK가 오면 윈도우를 오른쪽으로 밀어서(Slide) 다음 패킷을 보냅니다. 이를 통해 **네트워크 대역폭을 꽉 채워(Throughput)** 통신합니다.

### 📚 연결 문서
- [[algo-complexity-and-big-o]] - O(n^2) vs O(n) 효율 비교
- [[algo-ds-linear]] - 배열 접근 방식
- [[algo-pattern-search-and-sort]] - 정렬된 상태의 이점
