---
title: recomposition
tags: [android, jetpack-compose, compose/runtime, ui-architecture]
aliases: [Recomposition, 재구성, Recompose]
date modified: 2026-08-06 16:25:00 +09:00
date created: 2026-08-06 16:25:00 +09:00
---

## Recomposition (재구성) 이란 무엇인가

Jetpack Compose 에서 **Recomposition (재구성)** 이란 **"상태(State)가 변경되었을 때, 변경된 데이터를 반영하기 위해 영향받는 Composable 함수들을 다시 실행(Re-execute)하고 UI 트리를 업데이트하는 런타임 메커니즘"** 을 의미한다.

기존 명령형 UI(View 시스템)에서는 `textView.setText()` 처럼 개발자가 직접 UI 요소의 상태를 조작했지만, 선언적 UI인 Compose 에서는 **State 변경 ➔ Recomposition 발생 ➔ 새로운 UI Description 렌더링** 파이프라인으로 동작한다.

```
[State 변경 발생 (e.g. count++)]
         │
         ▼
[Recomposition Phase (재구성)]
- 영향받는 Composable 함수 재실행
- 바뀐 입력값 계산 및 Slot Table 갱신
         │
         ▼
[Layout & Draw Phase]
- 화면 실제 픽셀 재렌더링
```

---

## Recomposition 의 핵심 런타임 특성

1. **스킵 최적화 (Recomposition Skip)**:
   - Composable 함수의 입력 파라미터가 변경되지 않았거나 [불변성(Immutability)](file:///Users/youngmin/Documents/Obsidian/what-i-studied/01_inbox/computer-science/immutability.md) 이 보장되는 경우, Compose 런타임은 해당 함수 실행을 건너뛰어 성능을 최적화한다.

2. **비결정적 및 비동기 실행 특성**:
   - **순서 미보장**: 하위 Composable 함수들이 코드 순서대로 실행되지 않을 수 있다.
   - **병렬 실행**: 런타임 최적화에 의해 여러 코어에서 동시에 실행될 수 있다.
   - **취소 및 재시도 (Cancellation & Preemption)**: Recomposition 이 진행 중일 때 새로운 State 가 들어오면, 진행 중이던 작업을 취소하고 새 State 로 처음부터 다시 계산한다.

3. **Side-Effect 격리 필수**:
   - Recomposition 은 언제든 여러 번 실행되거나 중간에 취소될 수 있으므로, Composable 함수 본문 내에 네트워크 요청이나 전역 변수 변경 같은 [Side Effect](file:///Users/youngmin/Documents/Obsidian/what-i-studied/02_references/computer-science/side-effect.md) 가 들어가면 심각한 오작동이 발생한다.

---

## 연결 문서

- [Pure Function](file:///Users/youngmin/Documents/Obsidian/what-i-studied/01_inbox/computer-science/pure-function.md) - Recomposition 대상이 되는 Composable 의 순수 함수 성질
- [Side Effect](file:///Users/youngmin/Documents/Obsidian/what-i-studied/02_references/computer-science/side-effect.md) - Recomposition 과정에서 격리해야 하는 부작용
- [Composable Body Must Be Fast, Idempotent and Side-Effect Free](file:///Users/youngmin/Documents/Obsidian/what-i-studied/01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/compose-runtime-contracts/composable-body-must-be-fast-idempotent-and-side-effect-free.md) - Recomposition 규약
