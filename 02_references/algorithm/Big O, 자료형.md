---
title: Big O, 자료형
tags: [big-o, concept, interview]
aliases: []
date modified: 2025-12-18 10:14:50 +09:00
date created: 2024-12-09 21:31:10 +09:00
---

- 소프트웨어 디자인할 때 항상 생각해야 되는 질문 -> 크기가 커질까?
  - 크기가 커지면 비효율적인 알고리즘은 시스템에 큰 피해를 줄 수 있음
  - 이 알고리즘이 얼마나 나쁜지 어떻게 측정할까?
- 빅오 (Big-O)
  - 입력값이 무한대로 향할 때 함수의 상한을 설명하는 수학적 표기 방법
  - 주어진 (최선/최악/평균) 경우의 수행시간의 상한을 나타냄
- 알고리즘의 실행 시간 (시간 복잡도) 과 함께 공간 요구사항 (공간 복잡도) 이 어떻게 증가하는지를 분류하는데 사용됨
- 알고리즘의 효율성을 분석하는 데에도 매우 유용하게 활용됨
- 점진적 실행 시간 (Asymptotic Running Time) 을 표기할 때 가장 널리 쓰이는 수학적 표기법 중 하나
- 점진적 실행 시간 = 시간 복잡도 (Time Complexity)
  - 어떤 알고리즘을 수행하는 데 걸리는 시간을 설명하는 계산 복잡도
  - $4n^2+3n+4 = O(n^2)$
- 시간 복잡도 종류
  - $O(1)$ (Constant Time Complexity)
    - 입력값이 아무리 커도 실행시간은 일정
    - 최고의 알고리즘
    - 그런 경우가 잘 없음
    - eg. [[Hash Table|해시테이블]] 의 조회 및 삽입

![[../../_assets/algorithm/o_1_graph.png]]

```dart
void checkFist(List<String> names) {
  if (names.isNotEmpty) {
    print(names.first);
  } else {
    print("no names");
  }
}
```

- $O(log(n))$ (Logarithmic Time)
- 실행 시간은 입력값에 영향을 받기 시작함
- 매우 큰 입력값에도 크게 영향을 받지 않는 편
- 매우 견고한 알고리즘인 편
- eg. [[Binary Search|이진 검색]]

![[../../_assets/algorithm/o_log_n_graph.png]]

```dart
// 1.contains()의 가장 단순한 방법
const numbers = [1,3,56,66,68,80,99,105,450];

bool naiveContains(int value, List<int> list) {
  for (final element in list) {
    if (element == value) {
      return true;
    }
  }
  return false;
}

// 2.contains() 나은 방법(정렬되어있는 경우)
bool betterNaiveContains(int value, List<int> list) {
  if (list.isEmpty) return false;
  final middleIndex = list.length ~/ 2;

  if (value > list[middleIndex]) {
    for (var i = middleIndex; i < list.length; i++) {
      if (list[i] == value) return true;
    }
  } else {
    for (var i = middleIndex; i>=0; i--) {
      if (list[i]==value) return true;
    }
  }

  return false;
}
```

- $O(n)$ (Linear Time Complexity)
- 입력값만큼 실행시간에 영향을 받음
- = 선형시간 알고리즘 (=Linear Time algorithm)
- 알고리즘 수행시간이 입력값에 비례함
- eg. 정렬되지 않은 리스트에서 최댓값 또는 최솟값

![[../../_assets/algorithm/o_n_graph.png]]

```dart
void printNames(List<String> names) {
  for (final name in names) {
    print(name);
  }
}
```

- $O(n*log(n))$ (Quasi-Linear Time Complexity)
  - 큰 데이터 세트에서는 "kind of" linear time
  - 적어도 모든 수에 대해 한번 이상은 비교해야 하는 비교 기반 정렬 알고리즘은 아무리 좋은 알고리즘도 $O(n*log(n))$ 보다 빠를 수 없음
  - 입력값이 최선인 경우, 비교를 건너뛰어 $O(n)$ 이 될 수도 있음
    - eg. [[Tim Sort|팀소트]] (Tim-sort)
  - Dart 의 list.sort 알고리즘은 32 개 이하에서는 [[Insertion Sort|insertion sort]], 그 이상은 [[Quick Sort|Dual-Pivot Quicksort]] 를 사용함
  - eg. [[Merge Sort|병합정렬]]

![[../../_assets/algorithm/o_n_log_n_graph.png]]

- $O(n^2)$ (Polynomial Time Complexity)
  - [[Bubble Sort|버블 정렬]] 같은 비효율적인 정렬 알고리즘

![[o_n_2_graph.png]]

```dart
void printMoreNames(List<String> names) {
 for (final _ in names) {
   for (final name in names) {
     print(name);
   }
 }
}
```

- $O(2^n)$ (Exponential Time Complexity)
  - $2^n$ 보다 훨씬 오래 걸리는 알고리즘
  - 피보나치수를 재귀로 계산하는 알고리즘
- $O(n!)$ (Factorial Time Complexity)
  - 가장 느린 알고리즘
  - 입력값이 조금만 커도 웬만한 다항시간 내에는 계산이 어려움
  - eg. 각 도시를 방문하고 돌아오는 가장 짧은 경로를 찾는 외판원 문제 (Traveling Salesman Problem = TSP) 를 브루트 포스로 풀이할 때 해당함

![[../../_assets/algorithm/o_graph.png]]

- 공간 복잡도를 나타낼 때도 사용함
- 알고리즘은 흔히 " 시간과 공간의 트레이드오프 (Space-Time tradeoff)" 관계임
  - 빠른 알고리즘은 공간을 많이 사용하고, 공간을 적게 차지하는 알고리즘은 실행 시간이 느림
- 공간 복잡도
- 알고리즘을 수행하기 위해 필요한 메모리양으로 측정
- 시간 복잡도와 같이 big O 로 표현

```dart
// O(n)
List<String> fillList(int length) {
   return List.filled(length, 'a');
}


// O(n^2)
List<String> stuffList(int length) {
   return List.filled(length, 'a' * length);
}
```

- 상한과 최악
  - big O 는 상한 (upper bound) 를 나타냄
  - 하한은?
    - $\Omega$(Big Omega Notation): 알고리즘의 최상의 경우 runtime 측정. 항상 최상의 경우만 낼 수 없기 때문에 big O 만큼 유용하지 않음
    - $\Theta$(Big Theta Notation): 최상과 최악의 경우의 중간을 측정하는 알고리즘
  - 상한과 최악을 혼동하지 않아야 함
    - 빅오 표기법은 정확하게 쓰기에는 너무 길고 복잡한 함수를 ' 적당히 정확하게 ' 표현하려는 방법이기 때문에 최악의 경우/평균적인 경우의 시간 복잡도와는 아무런 계 없는 개념
    - eg. 퀵 정렬을 이용할 경우 [1,4,3,7,8,6,5] 인 경우 최선으로 18 번만 비교하면 되지만, [1,2,3,4,5,6,7] 인 경우 최악으로 48 번 계산해야 함
- 분할 상환 분석 (Amortized Analysis)
  - 시간 또는 메모리를 분석하는 알고리즘의 복잡도를 계산할 때, 알고리즘 전체를 지 않고 최악의 경우만을 살펴보는 것은 비관적이라는 이유로 분할 상환 분석 방법이 등장하는 계기가 됨
  - 빅오와 함께 함수의 동작을 설명할 때 중요한 분석 방법 중 하나
  - 어쩌다 한 번 뿐인일로 복잡도가 높아지는 경우는 정확하지 않다는 방법
  - 최악의 경우를 여러번에 걸쳐 골고루 나눠주는 형태로 알고리즘의 시간 복잡도를 계산하는 방법
  - ex. 동적 배열
  - 더블링이 일어나는 경우는 어쩌다 한번뿐이지만 이런 경우로 인해 시간 복잡도는 $O(n)$ 이 됨
  - 분할 상환을 하게 되면 동적 배열 삽입시 시간 복잡도는 $O(1)$ 이 됨
- 병렬화
  - 딥러닝의 인기로 병렬화가 가능한지 여부가 알고리즘의 우수성을 평가하는 중요한 척도중의 하나가 됨
