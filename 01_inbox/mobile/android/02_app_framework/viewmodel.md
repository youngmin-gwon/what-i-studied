---
title: viewmodel
tags: [android, architecture, mvvm, presentation-layer]
aliases: [ViewModel, View Model, 뷰모델]
date modified: 2026-08-06 16:25:00 +09:00
date created: 2026-08-06 16:25:00 +09:00
---

## ViewModel 이란 무엇인가

Android 및 애플리케이션 아키텍처에서 **ViewModel** 은 **"Presentation Layer(UI 계층)의 상태(UiState)를 보유하고 관리하며, 비즈니스 로직 및 Domain/Data 계층과의 통신을 담당하는 아키텍처 컴포넌트"** 이다.

Android AAC(Android Architecture Components)의 `ViewModel` 은 특히 **Activity/Fragment 의 화면 회전(Configuration Change) 시에도 인스턴스가 파괴되지 않고 유지(Survive)** 되는 라이프사이클 이점을 제공한다.

```
[UI Layer (Composable / Activity)]
         │  ▲
   User  │  │  UI State (StateFlow / LiveData)
  Action │  │  Observation
         ▼  │
   [ ViewModel ] ────────> [ Domain / Data Layer (Repository / UseCase) ]
```

---

## ViewModel 의 핵심 역할과 범주

1. **UI 상태(UiState) 보유 및 제공**:
   - 화면을 그리는 데 필요한 데이터를 `StateFlow`, `LiveData` 형태로 캡슐화하여 제공한다.
   - 단일 진실 출처(Single Source of Truth, SSOT) 역할을 수행한다.

2. **UI 라이프사이클 분리**:
   - `ViewModel` 은 Composable 이나 Activity 보다 더 긴 수명을 가지므로, Context 객체(Activity Context 등)를 직접 참조해서는 안 된다 (메모리 누수 원인).

3. **비즈니스 이벤트 처리**:
   - 버튼 클릭 등 사용자 이벤트를 받아 도메인 유스케이스나 리포지토리를 호출한다.

---

## 주의해야 할 안티패턴

- **UI 기술 상세 포함 (Navigation, Snackbar 직접 호출)**:
  - ViewModel 내부에서 `NavController`, `SnackbarHostState` 등 Pure UI 요소나 뷰 객체를 직접 소유하는 것은 아키텍처 관점 및 단단한 결합(Tight Coupling) 측면에서 안티패턴이다.
- **모든 단순 UI 동작을 ViewModel 에 위임하는 오버엔지니어링**:
  - 클립보드 복사 알림, 텍스트 보이기/숨기기 토글 등 비즈니스 로직과 무관한 순수 UI 상태까지 전부 ViewModel State 로 관리하면 보일러플레이트가 극심해진다. 순수 UI 상태는 Composable 내부 `remember` 로 처리하는 것이 바람직하다.

---

## 연결 문서

- [Pure Function](../../../computer-science/pure-function.md) - ViewModel 과 대비되는 순수 UI 컴포넌트 성질
- [Side Effect](../../../../02_references/computer-science/side-effect.md) - ViewModel 이 비동기 작업을 처리하는 스코프와 부작용
- [Recomposition](jetpack-compose/runtime/recomposition.md) - ViewModel UiState 에 반응하여 일어나는 UI 재구성
