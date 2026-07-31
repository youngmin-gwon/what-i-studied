# Jetpack Compose Compiler & Slot Table Deep Dive

이 문서는 Jetpack Compose 내부에서 UI 트리가 어떻게 구성되고 변경 사항을 감지하는지, 그 중심에 있는 `@Composable` 어노테이션의 컴파일러 변환 원리와
런타임 저장 구조인 **Slot Table**, 그리고 **위치 기반 메모이제이션(Positional Memoization)**의 메커니즘을 상세히 다룹니다.

---

## 1. @Composable 어노테이션의 진짜 역할

우리는 흔히 화면을 그리는 함수 위에 `@Composable`을 붙입니다. 컴포즈 런타임은 이 어노테이션이 붙은 함수들끼리만 상호 호출할 수 있도록 엄격한 호출 제약을 적용합니다.

### 1-1. 컴파일러에 의한 디컴파일 결과 비교

개발자가 코드를 빌드하면 **Compose Compiler Plugin**은 `@Composable` 함수를 추적하여 바이트코드 단에서 완전히 다른 형태의 코드로 강제 변환합니다.

#### 개발자가 작성한 코드

```kotlin
@Composable
fun Counter() {
    var count by remember { mutableStateOf(0) }
    Button(
        text = "Count: $count",
        onPress = { count += 1 }
    )
}
```

#### 컴파일러가 변환한 가상 코드 (Decompiled View)

```kotlin
// 컴파일 후에는 함수 매개변수에 눈에 보이지 않던 Composer와 변경 플래그가 자동 주입됩니다.
fun Counter($composer: Composer, $changed: Int) {
    // 1. 재실행 그룹 시작 (고유 해시 ID 기준)
    val $composer = $composer.startRestartGroup(12345)

    // 2. remember 값 조회 및 메모이제이션
    $composer.startReplaceableGroup(-492369756)
    var count = remember($composer) { mutableStateOf(0) }
    $composer.endReplaceableGroup()

    Button(
        text = "Count: $count",
        onPress = { count += 1 },
        $composer,
    0
    )

    // 3. 그룹 닫기 및 Recomposition 람다 정보 바인딩
    $composer.endRestartGroup()?.updateScope { nextComposer ->
        Counter(nextComposer, $changed)
    }
}
```

### 1-2. 굳이 어노테이션을 강제하는 이유

1. **컨텍스트 전달**: 모든 `@Composable` 함수 호출 체인 안에서 숨겨진 파라미터인 `Composer` 인스턴스를 아래로 계속 전파하기 위함입니다.
2. **구조 분석**: 변경 추적용 정보(`$changed`)를 매개변수로 넘겨주어, 값이 바뀌지 않은 자식 컴포저블을 재실행 없이 스킵(Skip)할 수 있게 판단할 기준을
   마련합니다.

---

## 2. Slot Table (슬롯 테이블)

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

## 3. 위치 기반 메모이제이션 (Positional Memoization)

기반 기술 중 하나인 **Positional Memoization**은 연산 결과를 단순히 "어떤 매개변수 값으로 호출했는가"가 아니라, **"화면(Composition Tree)
상의 어느 위치에서 호출되었는가"**를 기준으로 데이터를 식별하고 재사용합니다.

### 3-1. 동작 메커니즘 예시

```kotlin
@Composable
fun App() {
    // 1번 호출 위치
    val value1 = remember { Math.random() }

    // 2번 호출 위치
    val value2 = remember { Math.random() }
}
```

* **결과**: `value1`과 `value2`는 둘 다 파라미터가 없지만, 서로 다른 난수를 갖게 되며 화면이 재생성(Recomposition)되어도 각자의 이전 값을 그대로
  유지합니다.
* **이유**: `remember`의 내부 코드는 현재 실행 중인 `Composer`에게 **"지금 호출된 위치의 Slot Table 인덱스 번호에 기록되어 있는 값을 반환해
  줘"**라고 요청하기 때문입니다.

### 3-2. remember { } 의 내부 구현 살펴보기

```kotlin
@Composable
inline fun <T> remember(
    key1: Any?,
    crossinline calculation: () -> T
): T {
    // 현재 Composer 위치의 저장된 값을 확인 후, key1의 변경 유무에 따라 캐시 적용 여부 결정
    return currentComposer.cache(currentComposer.changed(key1), calculation)
}

@ComposeCompilerApi
inline fun <T> Composer.cache(invalid: Boolean, block: () -> T): T {
    return rememberedValue().let {
        if (invalid || it === Composer.Empty) {
            val value = block()
            updateRememberedValue(value) // Slot Table에 새로운 값 갱신
            value
        } else {
            it // 변경 사항이 없다면 이전 캐시값 리턴
        }
    } as T
}
```

### 3-3. 위치 기반 메모이제이션이 주는 UX 이점

1. **불필요한 인스턴스 재생성 억제**: 리스트 필터링 연산(`items.filter { ... }`)이나 복잡한 물리 계산 결과를 Recomposition 주기 동안 손쉽게
   보존합니다.
2. **화면 폼 데이터 보존**: 사용자가 텍스트 입력 창에 글을 입력할 때 화면이 재생성되어도 텍스트가 날아가지 않는 근본적인 토대가 바로 이 위치 기반 메모이제이션
   덕분입니다.
