# AppFunctions 프레임워크

앱 개발자가 자신의 앱에 포함된 특정 기능을 시스템 AI 에이전트에게 **도구(Tool)**로 노출하는 신규 API 이다.

##### AppFunction 정의 (Jetpack Library)

```kotlin
@AppFunction(name = "create_note")
suspend fun createNote(
    @AppFunctionParam(name = "title") title: String,
    @AppFunctionParam(name = "content") content: String
): CreateNoteResult {
    // 에이전트의 자연어 요청을 받아 실제 앱 로직 수행
    val noteId = repository.addNote(title, content)
    return CreateNoteResult(id = noteId, status = "Success")
}
```
