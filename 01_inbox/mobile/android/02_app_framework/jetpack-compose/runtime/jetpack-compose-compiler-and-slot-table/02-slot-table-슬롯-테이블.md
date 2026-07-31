# Slot Table (슬롯 테이블)

**Slot Table**은 이전 화면 구성(Composition)의 계층 구조와 `remember`를 통해 메모리화된 객체들, 그리고 런타임 상태 값들을 메모리 상에 가지고 있는
**Compose의 실질적인 런타임 메모리 저장소**입니다.

### 2-1. 내부 데이터 저장 구조

Slot Table은 내부적으로 효율적인 쓰기/수정을 위해 **Gap Buffer** 자료구조를 차용합니다.

```
초기 상태 (Gap으로 가득 찬 빈 배열):
[ Gap (Empty Space) ........................................ ]

데이터 삽입 후 (Composition 단계):
[ Group(A) | Slot(State) | Group(B) | Slot(Count) | Gap .... ]
```

* **Group (구조적 경계)**: 컴포지션 내의 분기나 루프, 람다, 함수 시작과 끝 등의 구조 경계를 나눕니다.
* **Slot (값의 보관소)**: `remember`로 할당된 State, Cached 객체, Lambda 인스턴스 등이 들어갑니다.

### 2-2. 조건 분기에 따른 Slot Table 변화 예시

만약 조건에 따라 다른 화면을 노출하는 아래와 같은 코드가 있다면:

```kotlin
@Composable
fun App() {
    val result = getData()
    if (result == null) {
        $composer.start(123) // Group 123
        Loading(...)
        $composer.end()
    } else {
        $composer.start(456) // Group 456
        Header(result)
        Body(result)
        $composer.end()
    }
}
```

```
[데이터가 Null인 경우]
┌────────────┐     ┌──────────────┐
│ Group(123) │ ──> │ Loading State│
└────────────┘     └──────────────┘

[데이터가 로드되어 Null이 아닌 경우 (Recomposition)]
기존 Group(123) 영역이 무효화되고 Gap Buffer가 이동하여 새로운 구조를 삽입합니다.
┌────────────┐     ┌──────────────┐     ┌──────────────┐
│ Group(456) │ ──> │ Header State │ ──> │  Body State  │
└────────────┘     └──────────────┘     └──────────────┘
```

이처럼 **Group ID**를 두어 변경된 범위가 정확히 어디부터 어디까지인지 그룹화하여 효율적으로 트리의 일부 영역을 갈아끼울 수 있게 만듭니다.

---
