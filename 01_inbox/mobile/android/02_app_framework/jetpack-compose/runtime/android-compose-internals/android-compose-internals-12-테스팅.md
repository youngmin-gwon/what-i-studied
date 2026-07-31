# 테스팅

상위 노트: [android-compose-internals](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/android-compose-internals.md)

```kotlin
class CounterTest {
    @get:Rule
    val composeTestRule = createComposeRule()
    
    @Test
    fun counterIncrementsOnButtonClick() {
        composeTestRule.setContent {
            Counter()
        }
        
        // 초기 상태 확인
        composeTestRule.onNodeWithText("Count: 0").assertExists()
        
        // 버튼 클릭
        composeTestRule.onNodeWithText("Increment").performClick()
        
        // 업데이트된 상태 확인
        composeTestRule.onNodeWithText("Count: 1").assertExists()
    }
    
    @Test
    fun textFieldUpdatesOnInput() {
        composeTestRule.setContent {
            var text by remember { mutableStateOf("") }
            TextField(value = text, onValueChange = { text = it })
        }
        
        composeTestRule.onNode(hasSetTextAction())
            .performTextInput("Hello")
        
        composeTestRule.onNodeWithText("Hello").assertExists()
    }
}
```
