# Jetpack Compose Mental Model (사고 모델: Thinking in Compose)

이 문서는 기존의 명령형(Imperative) UI 프로그래밍 패러다임에서 선언형(Declarative) UI 패러다임으로 전환하기 위한 핵심 개념적 토대와, Jetpack Compose 엔진의 독특한 렌더링/재구성(Recomposition) 메커니즘을 다룹니다.

---

## 1. 선언형 패러다임: UI = f(State)

기존 Android View 시스템은 UI 위계를 직접 탐색하여 데이터 변경을 반영하는 **명령형(Imperative)** 구조(예: `findViewById` 후 `setText()`)를 사용했습니다. 이는 앱이 복잡해질수록 상태 불일치(State Inconsistency) 버그를 유발합니다.

Jetpack Compose는 **선언형(Declarative)** UI 모델을 채택합니다.
* **개념**: 화면 전체를 직접 수정하는 대신, 상태(State)를 입력받아 화면이 어떻게 보여야 하는지 정의하는 **함수(Composable)**를 구현합니다.
* **동작**: 데이터(State)가 변경되면 Compose 프레임워크가 변경된 컴포저블을 자동으로 다시 실행하여 화면을 새 상태로 갱신합니다.

```mermaid
graph LR
    State["1. State (데이터 변경)"] -->|입력| Composable["2. Composable 함수 실행"]
    Composable -->|출력| UI["3. 새로운 UI 생성 및 반영"]
```

---

## 2. 재구성(Recomposition)의 5대 핵심 아키텍처 규칙

재구성은 상태 변경에 따라 Composable 함수를 다시 호출하여 UI 트리를 갱신하는 과정입니다. Compose 엔진은 성능 최적화를 위해 매우 정교하고 독특하게 동작하므로, 개발자는 반드시 다음 5가지 원칙을 숙지해야 합니다.

### 2-1. Composable 함수는 어떤 순서로도 실행될 수 있음 (Execute in any order)
* **설명**: 코드에 작성된 순서대로 컴포저블이 위에서 아래로 순차 실행된다고 가정해서는 안 됩니다.
* **주의**: 부모 컴포저블이 호출되기 전에 자식 컴포저블이 먼저 실행될 수 있으며, 화면에 나타나지 않는 컴포저블은 실행 순서가 뒤로 밀릴 수 있습니다.
* **대응**: 개별 Composable 함수는 완벽하게 격리되고 독립적이어야 하며, 다른 컴포저블의 실행 완료 여부에 의존해서는 안 됩니다.

### 2-2. Composable 함수는 병렬로 실행될 수 있음 (Run in parallel)
* **설명**: Compose는 멀티코어 환경에서 렌더링 성능을 극대화하기 위해 다중 스레드(Parallel)에서 동시에 Composable 함수를 실행할 수 있는 잠재력을 가지고 설계되었습니다.
* **주의**: Composable 내부에서 외부 로컬 변수를 읽거나 수정(Side Effect)할 경우 스레드 안정성(Thread Safety) 문제가 발생합니다.
* **대응**: 모든 Composable 내부에는 부작용(Side Effect)이 없어야 하며(Pure Function), 공유 변수 수정은 반드시 호출자에게 이벤트를 전달(`Callback`)하는 방식으로 처리해야 합니다.

### 2-3. 재구성은 스킵 가능함 (Skipping)
* **설명**: Compose는 스마트 재구성(Smart Recomposition)을 지원하여, 상태 변화가 감지되지 않았거나 파라미터가 변경되지 않은 Composable 노드의 실행을 완전히 건너뜁니다.
* **주의**: 객체의 참조 주소는 같지만 내부 값이 바뀌는 경우(가변 객체), Compose가 변경 사항을 감지하지 못하고 스킵하여 UI 갱신이 누락될 수 있습니다.
* **대응**: 불변(Immutable) 상태 모델을 사용하고 상태를 `mutableStateOf`로 감싸 제공해야 합니다.

### 2-4. 재구성은 낙관적이며 취소될 수 있음 (Optimistic & Cancelable)
* **설명**: Compose는 상태가 변경되는 즉시 재구성을 시작하지만, 재구성이 끝나기 전에 또 다른 상태 변경이 들어오면 기존 재구성을 즉시 파기(Cancel)하고 새로운 상태로 처음부터 다시 실행합니다.
* **주의**: 취소될 가능성이 있는 Composable 실행 도중에 외부 DB 쓰기나 파일 다운로드 등의 무거운 부작용(Side Effect)이 실행되면 비정상적인 데이터 중복이 발생합니다.
* **대응**: Composable 본문 내에 직접 부작용 코드를 작성하지 말고, `LaunchedEffect`, `SideEffect` 등 전용 Effect API를 사용해 생명주기와 동기화해야 합니다.

### 2-5. Composable 함수는 매우 자주 실행될 수 있음 (Run quite frequently)
* **설명**: 애니메이션이나 터치 드래그 반응 시, Composable 함수는 매 프레임(최대 초당 120회)마다 실행될 수 있습니다.
* **주의**: Composable 내부에 직접 I/O 작업, 데이터베이스 쿼리, 큰 리스트 정렬 등의 무거운 로직을 작성하면 화면 프레임이 떨어져 끊김 현상(Jank)이 발생합니다.
* **대응**: 무거운 계산 작업은 `remember`를 통해 연산 결과를 메모이제이션하거나, `ViewModel` 영역으로 완전히 격리해야 합니다.

---

## 3. 요약: 깨끗한 컴포즈 코드를 위한 골든 룰 (Golden Rules)

1. **Pure Function 유지**: Composable 내부에서 외부 값을 수정하는 동작(Side Effect)을 절대 금지합니다.
2. **비동기/무거운 연산 격리**: `ViewModel`에서 상태를 방출하고 비즈니스 로직을 처리하며, Composable 본문 내부에서는 계산 결과를 그리기만 합니다.
3. **단방향 데이터 흐름(UDF)**: 상태(State)는 아래로 흐르고, 이벤트(Event)는 위로 전달되도록 설계하여 결합도를 낮춥니다.

---

## 4. 관련 문서

- [[jetpack-compose-automatic-state-observation-for-flutter-developers]]: Compose Runtime의 automatic state observation을 Flutter 개발자 관점으로 설명합니다.
- [[jetpack-compose-state-management-flutter-comparison]]: `remember`, `rememberSaveable`, state hoisting, ViewModel, Flow API 선택 기준을 비교합니다.
- [[jetpack-compose-side-effects-and-lifecycle]]: Composable body 밖으로 빼야 하는 작업과 effect API를 정리합니다.
