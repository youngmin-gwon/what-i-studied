# derivedStateOf

계산된 상태 최적화.

```kotlin
@Composable
fun TodoList(todos: List<Todo>) {
    val highPriorityTodos = remember(todos) {
        derivedStateOf {
            // todos 가 변경될 때만 재계산
            todos.filter { it.priority == Priority.HIGH }
        }
    }
    
    // highPriorityTodos.value 가 실제로 변경될 때만 재구성
    Text("High priority: ${highPriorityTodos.value.size}")
}
```
