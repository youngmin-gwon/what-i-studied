# Jetpack Glance (권장)

`RemoteViews` 를 직접 다루는 대신, Compose 의 선언형 문법을 사용하여 위젯을 정의한다.

##### GlanceWidget 구현

```kotlin
class MyAppWidget : GlanceAppWidget() {

    override suspend fun provideGlance(context: Context, id: GlanceId) {
        // 데이터 준비 (DataStore 등에서 읽어오기)
        val data = repository.getData()

        provideContent {
            GlanceContent(data)
        }
    }

    @Composable
    private fun GlanceContent(data: MyData) {
        Column(
            modifier = GlanceModifier.fillMaxSize()
                .background(GlanceTheme.colors.surface),
            verticalAlignment = Alignment.CenterVertically,
            horizontalAlignment = Alignment.CenterHorizontally
        ) {
            Text(text = data.title, style = TextStyle(fontSize = 18.sp))
            Button(text = "새로고침", onClick = actionRunCallback<RefreshAction>())
        }
    }
}
```
