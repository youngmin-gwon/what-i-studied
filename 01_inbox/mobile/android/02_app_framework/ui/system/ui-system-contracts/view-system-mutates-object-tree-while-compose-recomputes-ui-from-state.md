---
title: "View System은 object tree를 변경하고 Compose는 state에서 UI를 재계산한다"
tags: ["android", "android/app-framework"]
---

# View System은 object tree를 변경하고 Compose는 state에서 UI를 재계산한다

View System에서는 이미 존재하는 `View` 객체의 속성을 바꾸는 방식으로 화면을 갱신한다. `TextView.text`, `RecyclerView.Adapter`, click listener처럼 객체 reference를 붙잡고 변경하는 코드가 중심이 된다.

Compose에서는 composable 함수가 state를 읽고 UI tree를 다시 계산한다. 같은 결과를 내기 위해 직접 view를 찾아 바꾸지 않고, state를 바꾸면 Compose runtime이 어떤 composable을 다시 실행할지 판단한다.

이 차이 때문에 View System의 "객체를 어디서 잡고 바꿀까"라는 질문은 Compose에서 "state를 어디에 두고 누가 읽을까"라는 질문으로 바뀐다. state는 필요한 가장 낮은 공통 부모에 두고, event는 위로 올리는 구조가 기본이다.

관련 노트: [Compose state owner는 읽고 쓰는 범위의 가장 낮은 공통 owner다](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/compose-runtime-contracts/compose-state-owner-is-the-lowest-common-owner-that-needs-read-or-write.md)

## 판단 기준

- View System의 가변 객체 트리(Mutable View Tree) 변형 방식 대신 Compose의 불변(Immutable) 상태 기반 UI 렌더링 재계산 모델을 적용한다.
- 뷰 객체 참조(View Reference)를 저장하는 대신 State 읽기 스코프(Snapshot State Read Scope)를 명확히 분리하여 Recomposition 성능을 높인다.

## 경계

- Composable 실행 중 외부 상태나 객체 속성을 수동으로 변경(Side Effect)하려는 시도는 렌더링 예측 가능성을 훼손하므로, `SideEffect` 또는 `LaunchedEffect` 블록으로 경계를 획정해야 한다.
