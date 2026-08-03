---
title: "RecyclerView와 LazyColumn은 같은 목록 문제를 푸는 다른 렌더링 계약이다"
tags: ["android", "android/app-framework"]
---

# RecyclerView와 LazyColumn은 같은 목록 문제를 푸는 다른 렌더링 계약이다

`RecyclerView`와 `LazyColumn`은 둘 다 큰 목록을 효율적으로 보여주기 위한 도구지만 같은 API의 포팅 버전은 아니다. RecyclerView는 ViewHolder 재사용과 adapter mutation을 중심으로 동작하고, LazyColumn은 item key, state, composition을 중심으로 동작한다.

RecyclerView에서는 adapter가 목록 변경을 전달하고 ViewHolder가 기존 view에 데이터를 bind한다. LazyColumn에서는 item content가 composable로 선언되고, Compose runtime이 필요한 item composition을 유지하거나 다시 계산한다.

Compose 목록에서 중요한 것은 stable key와 state 위치다. item 내부 state가 목록 이동, 삽입, 삭제 중에도 보존되어야 하면 key를 명시하고, 화면 전체 상태는 ViewModel이나 상위 state holder가 소유한다.

따라서 RecyclerView 최적화 습관을 그대로 옮기기보다 "목록 identity는 key로, UI는 state에서, side effect는 effect boundary에서"라는 Compose 계약으로 다시 설계한다.

## 판단 기준

- RecyclerView는 View 객체 재사용(Recycling & Binding)을 통해 뷰 객체 생성을 최소화하고, LazyColumn은 화면에 보이는 아이템의 Composable 함수만 Composition 및 Recomposition하는 방식으로 목록 렌더링을 최적화한다.
- LazyColumn에서 아이템의 스크롤 위치 보존 및 무효화(Invalidation) 방지를 위해 `key = { item.id }` 파라미터를 통한 고유 식별자(Stable Key) 지정을 기본 규칙으로 적용한다.

## 경계

- View System의 Adapter/ViewHolder 패턴 의존 습관을 Composable 내부로 들여와 불필요한 상태 가변 객체를 관리하지 않으며, State Hoisting을 통해 아이템 렌der 상태를 단방향 데이터 흐름으로 제어한다.
