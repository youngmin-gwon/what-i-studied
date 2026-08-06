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

## 1. 개요 및 비유로 이해하는 개념 (Overview & Definition)

**Single Source of Truth (SSOT, 단일 진실 출처)**는 소프트웨어 시스템 내부의 특정 데이터나 상태(State)에 대해 오직 **단 하나의 권한 있는 출처(Owner)**만을 두도록 강제하는 아키텍처 설계 원칙이다.

### 초보자를 위한 은행 장부 비유
만약 나의 계좌 잔액이 은행 중앙 서버, 내 스마트폰 앱, ATM 기기 3곳에 각각 따로 저장되어 있고, 세 곳 모두에서 자유롭게 잔액을 직접 수정할 수 있다면 어떻게 될까? 스마트폰에서 10만 원을 출금했는데 ATM 잔액은 그대로라면 데이터 동기화가 깨지는 심각한 오류(**상태 불일치, State Divergence**)가 발생한다.
이 문제를 해결하는 가장 안전한 방법은 **오직 은행 중앙 서버 하나만을 진짜 원본 장부(SSOT)**로 삼고, 스마트폰 앱이나 ATM은 그 장부의 잔액을 조회(Observe)하거나 수정 요청(Event)만 보낼 수 있도록 제한하는 것이다.

안드로이드 애플리케이션 개발에서도 마찬가지다. 사용자 프로필, 장바구니 목록, 네트워크 연결 상태 등 앱의 핵심 데이터는 오직 한 곳에서만 보관·수정되어야 데이터가 꼬이거나 충돌하는 비동기 버그를 완벽히 막을 수 있다.

---

## 2. 단방향 데이터 흐름 (Unidirectional Data Flow, UDF)

SSOT 원칙을 실전 코드에 적용할 때 세트로 결합되는 핵심 패턴이 바로 **Unidirectional Data Flow (UDF, 단방향 데이터 흐름)**이다.

데이터는 항상 **한쪽 방향으로만 흘러야 한다**는 규칙이다:
1. **상태 하향 전달 (State Flows Down)**: 상태 소유자(SSOT Owner)에서 UI 컴포넌트로 [Immutability (불변성)](../../../computer-science/immutability.md)을 가진 화면 상태(UI State) 데이터가 아래로 흘러 내려간다.
2. **이벤트 상향 전달 (Events Flow Up)**: 사용자 터치나 버튼 클릭 같은 이벤트는 UI에서 상태 소유자([ViewModel](viewmodel.md))로 위로 전달된다.

```mermaid
graph TD
    UI["UI 계층 (Compose / View)"] -->|이벤트 전달 (User Action)| VM["ViewModel (UI State 소유자)"]
    VM -->|데이터 읽기/수정 요청| Repo["Repository (Data SSOT)"]
    Repo -->|최신 데이터 스트림| VM
    VM -->|불변 UI State 전달| UI
```

### UDF가 주는 3가지 이점
- **예측 가능성 (Predictability)**: UI가 직접 데이터를 변경할 수 없으므로 상태가 어디서 왜 바뀌었는지 추적하기 쉽다.
- **테스트 용이성 (Testability)**: 상태 소유자([ViewModel](viewmodel.md))에 가상의 이벤트를 넣어 받아오는 상태값만 검증하면 되므로 단위 테스트가 매우 직관적이다.
- **[Recomposition (재구성)](jetpack-compose/runtime/recomposition.md) 최적화**: Jetpack Compose 환경에서 불변 상태 객체를 전달받아 화면을 그리기 때문에 불필요한 UI 재렌더링을 효과적으로 방지할 수 있다.

---

## 3. 계층별 상태 소유권 (State Ownership)

공식 Android 앱 아키텍처 가이드라인에서는 계층별로 담당하는 SSOT 소유권을 다음과 같이 명확히 구분한다.

### 1) Repository 계층 (Data Level SSOT)
- **역할**: 영속성 데이터(Room DB, DataStore 등) 및 원격 서버 API 데이터의 통합 단일 진실 출처.
- **특징**: 데이터를 캐싱하고 로컬 DB와 Remote 네트워크 간 동기화를 총괄한다. UI 계층이 실제 데이터가 어디서 오는지 몰라도 되도록 데이터를 캡슐화한다.

### 2) ViewModel 계층 (UI State Level SSOT)
- **역할**: 화면(Screen) 단위 비즈니스 로직 처리 및 UI에 최적화된 화면 상태(UI State)의 단일 진실 출처. ([ViewModel](viewmodel.md) 참고)
- **특징**: Repository에서 흘러나오는 데이터 스트림을 가공하여 [StateFlow & SharedFlow](stateflow-and-sharedflow.md) 형태의 불변 UI State 객체로 관리하고 노출한다.

### 3) UI 계층 (View / Jetpack Compose)
- **역할**: 전달받은 불변 UI State를 화면 픽셀(Text, Image, Button 등)로 표현.
- **특징**: 상태의 오너십을 가지지 않는다(Stateless). 전달받은 상태만 화면에 표현하므로 화면 회전이나 [Recomposition (재구성)](jetpack-compose/runtime/recomposition.md) 시에도 상태가 유실되지 않는다.

---

## 4. 상태 불일치 (State Divergence) 방지 실천 전략

앱 내에서 **상태 불일치(State Divergence)**를 방지하기 위해 실무에서 사용하는 4가지 핵심 패턴은 다음과 같다.

1. **Read-only 인터페이스 노출 (캡슐화)**
   - [ViewModel](viewmodel.md) 내부에서는 가변 상태(`MutableStateFlow`)로 관리하지만, 외부 UI에는 읽기 전용 타입(`StateFlow`)만 노출한다.
   ```kotlin
   private val _uiState = MutableStateFlow(MyUiState())
   val uiState: StateFlow<MyUiState> = _uiState.asStateFlow()
   ```

2. **불변 데이터 모델 ([Immutability](../../../computer-science/immutability.md)) 사용**
   - Kotlin `data class`와 `val` 프로퍼티를 사용하여 데이터 변경 시 반드시 객체를 사본 복사(`copy()`)하여 교체한다. 이는 원본 데이터 훼손 등 [Side Effect (부작용)](../../../../02_references/computer-science/side-effect.md)을 차단한다.

3. **Offline-First 데이터베이스 중심 SSOT 구축**
   - 네트워크 응답 결과를 곧바로 UI에 넘기는 대신, 로컬 DB(Room)에 저장한 후 UI는 Room의 `Flow`를 관찰(Observe)하게 만들어 로컬 DB를 최종 SSOT로 통합한다.

4. **[Binder IPC](../01_system_internals/binder-ipc.md) 경계에서의 데이터 경량화**
   - 프로세스 간 통신 시 커다란 데이터 객체 전체를 넘기지 않고 ID(식별자) 값만 넘긴 후, 각 프로세스/컴포넌트의 Repository SSOT에서 최신 데이터를 조회하도록 설계하여 파편화를 막는다.

---

## 5. 연결 문서 (Related Links)

- [ViewModel](viewmodel.md) - UI State 를 관리하고 UDF 단방향 흐름을 주도하는 뷰모델
- [StateFlow & SharedFlow](stateflow-and-sharedflow.md) - UDF 패턴에서 불변 UI State 와 Event 를 전달하는 반응형 스트림
- [Recomposition (재구성)](jetpack-compose/runtime/recomposition.md) - UDF 상태 변화에 따라 렌더링되는 Compose runtime 메커니즘
- [Binder IPC](../01_system_internals/binder-ipc.md) - 프로세스 경계를 넘어 데이터를 안전하게 전달하기 위한 안드로이드 IPC 메커니즘
- [Immutability (불변성)](../../../computer-science/immutability.md) - SSOT 상태 모델링 시 사이드 이펙트를 막는 데이터 불변성 원칙
- [Side Effect (부작용)](../../../../02_references/computer-science/side-effect.md) - 상태 변개 시 부주의하게 발생할 수 있는 부작용과 예방법
