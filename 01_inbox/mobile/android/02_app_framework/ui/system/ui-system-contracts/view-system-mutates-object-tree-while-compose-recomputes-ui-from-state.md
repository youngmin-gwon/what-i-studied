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

UI system 노트는 View System과 Compose가 state, tree mutation, layout, side effect를 어디서 처리하는지 비교하는 기준으로 읽는다.

## 경계

API 이름 매핑보다 rendering model, state ownership, insets/back/adaptive boundary를 먼저 본다.
