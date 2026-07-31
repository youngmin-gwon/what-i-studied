# Jetpack Compose UI DSL

```kotlin
LazyColumn {
    items(restaurantList) { restaurant ->
        RestaurantRow(restaurant)
    }
}
```

내부적으로 `LazyListScope.() -> Unit` 수신 객체 지정 사용.
