---
title: composition-uses-callsite-identity-to-preserve-remembered-values
tags: [android, compose/runtime, jetpack-compose]
aliases: [Callsite identity, Positional memoization]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-07-31 23:59:00 +09:00
---

## Composition은 호출 위치 identity로 remember 값을 보존한다

### 1. 개념 정의 (What)
**호출 위치 식별성(Callsite Identity / Positional Memoization)**이란 Compose Runtime이 소스 코드 내에서 `@Composable` 함수나 `remember`가 호출된 정확한 정적 소스 위치(Source Location)와 실행 순서를 고유 키(Key)로 사용하여, Slot Table 상의 해당 상태 값을 식별하고 매핑·보존하는 메커니즘이다.

---

### 2. Callsite Identity와 Positional Memoization의 필요성 (Why)
동일한 Composable 함수(예: `ContactItem()`)가 반복문이나 조건문에서 수십 번 호출될 때, 런타임은 각 호출이 독립된 상태(State)를 보존할 수 있도록 구별해야 한다.

만약 변수 명칭이나 객체 주소로만 상태를 관리하려 하면:
- 루프 내 아이템 위치가 변경되거나 추가/삭제될 때 이전 아이템의 상태(예: 체크박스 선택 상태)가 다른 아이템으로 오염되는 문제가 발생한다.

Callsite Identity는 소스 코드의 위치 구조 및 명시적 키(`key()`)를 결합하여 UI 구성 요소의 고유 식별성을 보장한다.

---

### 3. 내부 동작 메커니즘 (How)

```
// 소스 코드
@Composable
fun CounterList() {
    remember { ... } // Compiler 가 고유 Key 1001 주입 -> $composer.startReplaceableGroup(1001)
    remember { ... } // Compiler 가 고유 Key 1002 주입 -> $composer.startReplaceableGroup(1002)
}
```

1. **컴파일러 정적 키 생성**: Compose Compiler는 컴파일 타임에 AST(Abstract Syntax Tree)를 스캔하여 모든 `@Composable` 함수 호출부와 `remember` 블록에 고유한 정수 키(Integer Key)를 할당하고 `$composer.startReplaceableGroup(generatedKey)` 코드를 주입한다.
2. **Slot Table 커서 대조**: [recomposition](../recomposition.md) 동안 `$composer`는 이전 프레임에서 기록된 Slot Table의 그룹 키와 새로 주입된 키를 비교한다. 키가 동일하면 동일한 Callsite로 판단하여 해당 슬롯의 `remember` 객체 및 하위 트리를 유지한다.
3. **루프와 key() 연산자**: `for` 문이나 `LazyColumn` 항목과 같이 동일한 Callsite에서 여러 개가 생성되는 동적 구조의 경우, 소스 코드 위치만으로는 구별할 수 없다. 이때 `key(item.id) { ... }`를 감싸면 외부 식별자(Explicit Key)가 Callsite Identity에 결합되어, 순서가 재정렬되더라도 상태 오염 없이 정확히 기존 상태를 매핑한다.

---

### 4. 코드 사례: key() 연산자의 유무에 따른 식별성 차이

```kotlin
data class TodoItem(val id: String, val text: String)

@Composable
fun IncorrectTodoList(todos: List<TodoItem>) {
    Column {
        for (todo in todos) {
            // ❌ key() 가 없으면 리스트 맨 앞에 아이템이 추가될 때
            // 기존 0번 항목의 remember 상태가 새 0번 항목으로 잘못 이관됨!
            var isChecked by remember { mutableStateOf(false) }
            CheckboxWithLabel(text = todo.text, checked = isChecked, onCheckedChange = { isChecked = it })
        }
    }
}

@Composable
fun CorrectTodoList(todos: List<TodoItem>) {
    Column {
        for (todo in todos) {
            // ✅ key(todo.id)를 통해 런타임에 동적 Callsite Identity를 보장
            // 아이템 순서가 바뀌거나 맨 앞에 추가되어도 각 todo.id에 종속된 isChecked 상태가 완벽히 보존됨
            key(todo.id) {
                var isChecked by remember { mutableStateOf(false) }
                CheckboxWithLabel(text = todo.text, checked = isChecked, onCheckedChange = { isChecked = it })
            }
        }
    }
}
```

---

관련 노트: [remember는 일반 cache가 아니라 Composition에 귀속된 저장공간이다](./remember-is-composition-scoped-storage-not-general-cache.md), [@Composable 컴파일 결과는 restart와 skip 제어를 가능하게 한다](./composable-compiler-restart-skip.md)

출처: [Under the hood of Jetpack Compose data structures](https://medium.com/androiddevelopers/under-the-hood-of-jetpack-compose-data-structures-gaps-and-slots-a42e564d623d)

검증일: 2026-08-05. Compose Compiler 및 Slot Table 구현체를 대조하여 Positional Memoization, 정적 소스 위치 키 생성, key() 동적 식별자 결합 알고리즘 서술을 정밀 보강했다.
