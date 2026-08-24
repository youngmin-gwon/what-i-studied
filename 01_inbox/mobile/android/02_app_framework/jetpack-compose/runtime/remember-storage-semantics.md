---
title: remember-storage-semantics
tags: [android, compose/runtime, jetpack-compose]
aliases: [remember, Composition-scoped storage]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-07-31 23:59:00 +09:00
---

## remember는 일반 cache가 아니라 Composition에 귀속된 저장공간이다

### 1. 개념 정의 (What)
`remember { calculation }`는 일반적인 메모리 캐시(예: `HashMap`, `LruCache`)나 전역 싱글톤 저장소가 아니며, **현재 Composable이 화면 트리에 바인딩된 수명주기(Composition Lifetime) 동안만 Slot Table에 객체를 보존하는 연산자**다. Composable이 Composition 트리에서 이탈(Leave/Uncompose)되면 `remember`로 할당된 객체 역시 메모리에서 자동으로 해제(Garbage Collected)된다.

---

### 2. Composition 수명주기 귀속의 필요성 (Why)
일반 캐시나 전역 변수를 UI 상태 저장용으로 사용할 경우 다음과 같은 문제가 발생한다:
- **메모리 누수 및 수명주기 불일치**: 화면이 종료되어도 캐시에 남아 데이터가 낭비되거나 이전 화면 데이터가 덮어씌워짐.
- **다중 인스턴스 충돌**: 동일한 Composable 컴포넌트(예: 독립된 리스트의 10개 카운터 아이템)가 화면에 여러 개 배치될 때 전역 캐시를 공유하면 상태가 꼬이게 됨.

`remember`는 각 Composable 함수 인스턴스의 트리가 살아있는 동안만 상태를 일대일로 격리 보존하는 **Composition-Scoped Storage**를 보장한다.

---

### 3. 내부 동작 메커니즘 (How)

```
[Composition Initial Execution]
   |--> Slot Table 의 현재 슬롯 조회
   |--> 값이 없음 (Empty Slot)
   |--> calculation() 키/값 실행 후 Slot 저장 -> 반환
   
[Recomposition Execution]
   |--> Slot Table 의 현재 슬롯 조회
   |--> 전달된 key1, key2 와 Slot 에 기록된 이전 키 비교
   |-- [키 변경 없음]: Slot 에 저장된 객체 즉시 반환 (연산 스킵)
   |-- [키 변경 됨]: calculation() 재계산 후 Slot 덮어쓰기 -> 새로 갱신된 값 반환
```

1. **Slot Table 저장**: `remember` 호출 시 Compose Compiler는 `$composer.cache()` 호출 코드로 변환한다. 런타임은 Slot Table의 현재 커서 위치에 있는 슬롯을 검사한다.
2. **Key 비교 및 메모제이션**: `remember(key1, key2) { ... }` 형태로 키가 제공되면, 런타임은 이전 프레임의 키 값들과 현재 전달된 키 값을 `equals()`로 대조한다. 키가 동일하면 기존 객체를 반환하고, 키가 변경되었으면 람다를 다시 실행하여 슬롯 값을 갱신한다.
3. **한계점 (Process Death 미보장)**: `remember`는 메모리 상의 Slot Table에만 살아있으므로, 시스템에 의한 프로세스 종료(System-initiated Process Death)나 Activity 재창조 시에는 값이 파괴된다. 이를 방지하려면 Bundle에 보존되는 `rememberSaveable`을 사용해야 한다.

---

### 4. 코드 사례: remember와 rememberSaveable의 비교

```kotlin
@Composable
fun StorageComparisonExample() {
    // 1. Composition 수명주기 동안 보존 (화면 회전/프로세스 재시작 시 초기화됨)
    var transientUiState by remember { mutableStateOf("Initial") }

    // 2. key1 변경 시 재계산되는 remember
    val expensiveResult = remember(transientUiState) {
        computeExpensiveHash(transientUiState)
    }

    // 3. 프로세스 재창조 및 Activity 재생성 시에도 Bundle로 복원되는 상태
    var persistentInput by rememberSaveable { mutableStateOf("") }

    Column {
        TextField(value = transientUiState, onValueChange = { transientUiState = it })
        Text("Computed Hash: $expensiveResult")
        TextField(value = persistentInput, onValueChange = { persistentInput = it })
    }
}
```

---

관련 노트: [Composition은 호출 위치 identity로 remember 값을 보존한다](composition-callsite-identity.md), [rememberSaveable은 small restorable UI state를 위한 것이다](../state-and-effects/remember-saveable.md)

출처: [State and Jetpack Compose](https://developer.android.com/develop/ui/compose/state#state-in-composables)

검증일: 2026-08-05. Compose 공식 가이드의 "remember" 단락을 대조하여 Slot Table 메모제이션, Key 비교 알고리즘, Composition 수명주기 격리 및 rememberSaveable 차이점 서술을 정밀 보강했다.
