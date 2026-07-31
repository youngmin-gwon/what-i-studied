# Ktor DSL (KMP 네트워크)

```kotlin
val client = HttpClient(CIO) {
    install(ContentNegotiation) {
        json(Json { prettyPrint = true })
    }
}
```
