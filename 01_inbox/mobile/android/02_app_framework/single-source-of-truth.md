---
title: single-source-of-truth
tags: [android, architecture, ssot, data-flow]
aliases:
  - SSOT
  - Single Source of Truth
  - 단일 진실 출처
  - Unidirectional Data Flow
  - UDF
date created: 2026-08-06
date modified: 2026-08-06
---

# Single Source of Truth (SSOT) & Unidirectional Data Flow (UDF)

## 1. 개요 및 정의 (Overview & Definition)

**Single Source of Truth (SSOT, 단일 진실 출처)**는 소프트웨어 설계 패턴이자 시스템 내부의 특정 데이터 또는 상태(State)에 대해 오직 **단 하나의 권한 있는 출처(Owner)**만을 두도록 강제하는 데이터 아키텍처 원칙이다.

안드로이드 애플리케이션 개발에서 SSOT 원칙을 적용하면 데이터가 여러 컴포넌트에 파편화되거나 중복 저장되어 동기화가 깨지는 현상을 방지할 수 있다. 앱의 특정 상태(예: 사용자 프로필, 장바구니 목록, 네트워크 접속 상태 등)는 어떠한 상황에서도 오직 한 곳에서만 수정되고 변경될 수 있어야 한다.

---

## 2. 단방향 데이터 흐름 (Unidirectional Data Flow, UDF)

SSOT 원칙을 충실히 구현하기 위해 결합되는 핵심 패턴이 **Unidirectional Data Flow (UDF, 단방향 데이터 흐름)**이다.

```
       +------------------------------------+
       |                                    |
       v                                    |
+--------------+     Events (User Actions)  |
|  UI Element  | ---------------------------+
| (Compose/View)|
+--------------+
       ^
       | UI State (Observables)
       |
+--------------+
|  StateOwner  |
| (ViewModel)  |
+--------------+
       ^
       | Data Streams
       |
+--------------+
|  Data Source |
| (Repository) |
+--------------+
```

### UDF의 핵심 작동 패턴
1. **State Flows Down (상태 하향 전달)**: 권한을 가진 계층(SSOT Owner)에서 하위 계층(예: UI 컴포넌트)으로 불변(Immutable) 상태가 단방향으로 흘러 내려간다.
2. **Events Flow Up (이벤트 상향 전달)**: 사용자 입력이나 시스템 이벤트는 UI에서 상위 계층(ViewModel/Repository)으로 전달되어 상태 변경 요청으로 처리된다.
3. **상태의 예측 가능성 증대**: UI가 직접 상태 데이터를 수정하지 못하며, 오직 이벤트를 상위로 전달한 후 새로운 상태가 생성되어 다시 내려오는 것을 관찰(Observe)하여 화면에 렌더링한다.

---

## 3. 계층별 상태 소유권 (State Ownership)

공식 Android 앱 아키텍처 가이드라인에 따른 계층별 SSOT 소유권 구분은 다음과 같다.

### 1) Repository 계층 (Domain/Data Level SSOT)
- **역할**: 영속성 데이터(Room DB, DataStore 등) 및 원격 서버 API의 데이터 통합 SSOT.
- **특징**: 데이터 교체, 캐싱 메커니즘, 데이터 동기화 정책을 총괄한다. UI 계층이 데이터 원천을 알 필요가 없도록 캡슐화한다.

### 2) ViewModel 계층 (UI State Level SSOT)
- **역할**: 화면(Screen) 단위 비즈니스 로직 처리 및 UI에 최적화된 화면 상태(UI State) 관리.
- **특징**: Repository에서 흘러나오는 데이터 스트림을 가공하여 [stateflow-and-sharedflow](stateflow-and-sharedflow.md) 형태의 불변 UI State 객체로 관리 및 노출한다.

### 3) UI 계층 (View / Jetpack Compose)
- **역할**: 전달받은 불변 UI State를 받아 화면에 화면 요소(Text, Image, Button 등)로 표현.
- **특징**: 상태를 자체적으로 보관하거나 직접 가공(Mutate)하지 않는다. stateless한 구조를 유지하여 화면 재구성(Configuration Change) 또는 Recomposition에 유연하게 대응한다.

---

## 4. 상태 불일치 (State Divergence) 방지 전략

앱 내에서 **상태 불일치(State Divergence)**란 동일한 데이터에 대해 두 개 이상의 장소(예: 로컬 DB와 메모리 변수, ViewModel 내부 변수와 UI 내부 변수)가 서로 다른 값을 가지고 있는 동기화 오류 현상을 의미한다.

### 상태 불일치 방지를 위한 핵심 실천 과제

1. **Read-only 인터페이스 노출 (Encapsulation)**
   - ViewModel 내부에서는 가변 상태(`MutableStateFlow`)를 선언하되, 외부 UI 계층에는 불변 관찰 가능 타입(`StateFlow`)만 노출한다.
   ```kotlin
   private val _uiState = MutableStateFlow(MyUiState())
   val uiState: StateFlow<MyUiState> = _uiState.asStateFlow()
   ```

2. **불변 데이터 모델 (Immutable Data Class) 사용**
   - Kotlin의 `data class`와 `val` 프로퍼티를 사용하여 데이터 변경 시 반드시 객체를 카피(`copy()`)하는 방식을 적용함으로써 부작용(Side-effect)을 사전에 차단한다.

3. **로컬 데이터베이스 중심 SSOT 구축**
   - 네트워크 요청 결과를 직접 UI 상태로 넘기는 대신, 네트워크 결과를 로컬 DB(Room)에 저장하고, UI는 Room의 `Flow`를 관찰하는 **Offline-First** 패턴 적용.

4. **[binder-ipc](../01_system_internals/binder-ipc.md) 경계에서의 데이터 경량화**
   - 컴포넌트 간 복잡한 전체 데이터 상태를 Binder를 통해 파편화하여 주고받지 않고, ID 값만 넘긴 뒤 각 프로세스/컴포넌트의 Repository SSOT에서 최신 데이터를 조회하도록 설계한다.

---
## 연관 문서
- [binder-ipc](../01_system_internals/binder-ipc.md)
- [stateflow-and-sharedflow](stateflow-and-sharedflow.md)
