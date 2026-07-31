# Navigation 3의 Entry Provider DSL

```kotlin
val entryProvider = { key ->
    when (key) {
        is HomeKey -> Entry(key) { HomeScreen() }
        is DetailKey -> Entry(key) { DetailScreen(id = key.id) }
        else -> null
    }
}
```

---
