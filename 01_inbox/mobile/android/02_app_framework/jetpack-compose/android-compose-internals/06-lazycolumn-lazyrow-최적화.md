# LazyColumn/LazyRow 최적화

상위 노트: [[android-compose-internals]]

```kotlin
@Composable
fun OptimizedList(items: List<Item>) {
    LazyColumn(
        contentPadding = PaddingValues(16.dp),
        verticalArrangement = Arrangement.spacedBy(8.dp)
    ) {
        items(
            items = items,
            key = { it.id },
            contentType = { it.type } // 같은 타입끼리 재사용
        ) { item ->
            when (item.type) {
                ItemType.TEXT -> TextItem(item)
                ItemType.IMAGE -> ImageItem(item)
            }
        }
    }
}

// Sticky Header
@Composable
fun GroupedList(groups: Map<String, List<Item>>) {
    LazyColumn {
        groups.forEach { (header, items) ->
            stickyHeader {
                Text(
                    text = header,
                    modifier = Modifier
                        .fillMaxWidth()
                        .background(Color.Gray)
                        .padding(16.dp)
                )
            }
            
            items(items) { item ->
                ItemCard(item)
            }
        }
    }
}
```
