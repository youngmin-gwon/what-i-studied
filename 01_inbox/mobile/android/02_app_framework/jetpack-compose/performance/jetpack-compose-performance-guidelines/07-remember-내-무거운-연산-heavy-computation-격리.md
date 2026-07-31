# `remember` 내 무거운 연산(Heavy Computation) 격리

상위 노트: [jetpack-compose-performance-guidelines](01_inbox/mobile/android/02_app_framework/jetpack-compose/performance/jetpack-compose-performance-guidelines.md)

`remember`는 화면이 리컴포지션될 때 이전 계산 결과를 보존하여 CPU 낭비를 막아주는 핵심 API입니다.

### 7-1. 오직 "비용이 큰 연산"에만 적용하는 이유
`remember` 역시 공짜가 아닙니다. 내부적으로 Slot Table 인덱스를 확인하고 메모리 캐시를 조회/갱신하는 오버헤드가 발생합니다.
* **단순 연산**: `a + b`, 단순 문자열 이어서 붙이기 등은 `remember` 오버헤드가 더 큽니다.
* **무거운 연산(Heavy Computation)**: Sorting(정렬), Filtering(필터링), Regex 검증, 데이터 변환 연산 등은 리컴포지션마다 재실행되면 CPU 타임을 심각하게 갉아먹으므로 반드시 `remember(key)`로 감싸야 합니다.

```kotlin
// ❌ 단순 연산에 remember 지양 (오버헤드가 더 큼)
val fullName = remember(firstName, lastName) { "$firstName $lastName" }

// 🐳 복잡한 연산 및 필터링에는 필수 적용
val sortedActiveUsers = remember(users) {
    trace("SortActiveUsers") {
        users.filter { it.isActive }
             .sortedByDescending { it.lastLoginTimestamp }
    }
}
```

---
