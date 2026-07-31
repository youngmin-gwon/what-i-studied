# `suspend` 함수란?

`suspend`는 "이 함수는 중간에 멈췄다가 다시 이어질 수 있다"는 표시입니다.

```kotlin
suspend fun fetchBenefits(): List<Benefit> {
    return api.getBenefits()
}
```

`suspend` 함수는 일반 함수처럼 값을 반환하지만, 내부에서 네트워크, DB, 파일 작업처럼 오래 걸리는 일을 안전하게 기다릴 수 있습니다.

> [!IMPORTANT]
> `suspend`는 "무조건 백그라운드에서 실행된다"는 뜻이 아닙니다. 단지 **중단 가능하다**는 뜻입니다. 실제로 어느 스레드에서 실행할지는 Coroutine
> Dispatcher가 결정합니다.
