# Adaptive Layout

상위 노트: [[android-large-screens]]

##### Navigation Rail (중형 화면)

```kotlin
@Composable
fun MediumScreenLayout() {
    Row {
        NavigationRail {
            items.forEach { item ->
                NavigationRailItem(
                    icon = { Icon(item.icon, null) },
                    label = { Text(item.label) },
                    selected = item == selectedItem,
                    onClick = { selectedItem = item }
                )
            }
        }
        
        // 메인 컨텐츠
        MainContent(modifier = Modifier.weight(1f))
    }
}
```

##### List-Detail (대형 화면)

```kotlin
@Composable
fun ListDetailLayout() {
    Row {
        // 리스트 (1/3)
        ItemList(
            modifier = Modifier.weight(1f),
            onItemClick = { selectedItem = it }
        )
        
        // 디테일 (2/3)
        ItemDetail(
            item = selectedItem,
            modifier = Modifier.weight(2f)
        )
    }
}
```
