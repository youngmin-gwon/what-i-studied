# @Composable 어노테이션의 진짜 역할

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
