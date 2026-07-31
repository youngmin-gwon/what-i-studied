# Cold Flow: 누가 구독해야 흐른다

일반적인 `Flow`는 **Cold Stream**입니다.

뜻은 "누군가 `collect`하기 전까지 아무 일도 하지 않는다"입니다.

```kotlin
val flow = flow {
    emit(1)
    emit(2)
    emit(3)
}

flow.collect { value ->
    println(value)
}
```

`flow { ... }` 블록은 선언만으로 실행되지 않습니다. `collect`를 해야 실행됩니다.

> [!NOTE]
> Flow는 수도관 설계도에 가깝습니다. 물이 실제로 흐르는 시점은 누군가 수도꼭지를 여는 `collect` 순간입니다.
