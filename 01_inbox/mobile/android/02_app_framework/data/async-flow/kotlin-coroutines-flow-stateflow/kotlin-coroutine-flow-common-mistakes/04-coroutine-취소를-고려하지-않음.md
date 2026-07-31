# Coroutine 취소를 고려하지 않음

Coroutine은 취소될 수 있습니다. 특히 화면이 사라지거나 새 검색어가 들어오면 이전 작업이 취소되는 것이 정상입니다.

긴 루프를 직접 돌린다면 취소 가능 지점을 고려해야 합니다.

```kotlin
while (isActive) {
    syncOnce()
    delay(60_000)
}
```
