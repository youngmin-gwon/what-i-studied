# 위치 기반 메모이제이션 (Positional Memoization)

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
