---
title: RecyclerView와 LazyColumn은 같은 목록 문제를 푸는 다른 렌더링 계약이다
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-03 16:36:00 +09:00
date created: 2026-07-31 23:38:40 +09:00
---

# RecyclerView와 LazyColumn은 같은 목록 문제를 푸는 다른 렌더링 계약이다

`RecyclerView` 와 `LazyColumn` 은 둘 다 큰 목록을 효율적으로 보여주기 위한 도구지만 같은 API 의 포팅 버전은 아니다. RecyclerView 는 ViewHolder 재사용과 adapter mutation 을 중심으로 동작하고, LazyColumn 은 item key, state, composition 을 중심으로 동작한다.

RecyclerView 에서는 adapter 가 목록 변경을 전달하고 ViewHolder 가 기존 view 에 데이터를 bind 한다. LazyColumn 에서는 item content 가 composable 로 선언되고, Compose runtime 이 필요한 item composition 을 유지하거나 다시 계산한다.

Compose 목록에서 중요한 것은 stable key 와 state 위치다. item 내부 state 가 목록 이동, 삽입, 삭제 중에도 보존되어야 하면 key 를 명시하고, 화면 전체 상태는 ViewModel 이나 상위 state holder 가 소유한다.

따라서 RecyclerView 최적화 습관을 그대로 옮기기보다 "목록 identity 는 key 로, UI 는 state 에서, side effect 는 effect boundary 에서"라는 Compose 계약으로 다시 설계한다.

### 판단 기준

- RecyclerView 는 View 객체 재사용(Recycling & Binding)을 통해 뷰 객체 생성을 최소화하고, LazyColumn 은 화면에 보이는 아이템의 Composable 함수만 Composition 및 Recomposition 하는 방식으로 목록 렌더링을 최적화한다.
- LazyColumn 에서 아이템의 스크롤 위치 보존 및 무효화(Invalidation) 방지를 위해 `key = { item.id }` 파라미터를 통한 고유 식별자(Stable Key) 지정을 기본 규칙으로 적용한다.

### 경계

- View System 의 Adapter/ViewHolder 패턴 의존 습관을 Composable 내부로 들여와 불필요한 상태 가변 객체를 관리하지 않으며, State Hoisting 을 통해 아이템 렌 der 상태를 단방향 데이터 흐름으로 제어한다.
