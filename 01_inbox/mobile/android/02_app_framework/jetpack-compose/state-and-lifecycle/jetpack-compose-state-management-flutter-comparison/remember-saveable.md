# `rememberSaveable`

상위 노트: [jetpack-compose-state-management-flutter-comparison](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-state-management-flutter-comparison.md)

`rememberSaveable`은 `remember`처럼 recomposition 사이에 값을 유지하고, 추가로 Activity 재생성이나 프로세스 복원 상황에서도 저장 가능한
값을 복원합니다.

```kotlin
@Composable
fun LoginForm() {
    var email by rememberSaveable { mutableStateOf("") }

    TextField(
        value = email,
        onValueChange = { email = it },
    )
}
```

`rememberSaveable`이 적합한 상태:

```text
입력창 text
선택된 tab key
현재 열려 있는 page id
간단한 filter 값
작은 enum/string/int/boolean 상태
```

`rememberSaveable`이 부적합한 상태:

```text
Repository
HTTP client
암호화 key
큰 list
bitmap
DB entity 전체 목록
서버에서 다시 받아야 하는 screen data 전체
```

저장 가능한 기본 타입이 아니면 `Saver`를 정의할 수 있습니다.

```kotlin
data class DraftMessage(
    val title: String,
    val body: String,
)

val DraftMessageSaver = listSaver<DraftMessage, String>(
    save = { listOf(it.title, it.body) },
    restore = { DraftMessage(title = it[0], body = it[1]) },
)

@Composable
fun MessageEditor() {
    var draft by rememberSaveable(stateSaver = DraftMessageSaver) {
        mutableStateOf(DraftMessage(title = "", body = ""))
    }
}
```

다만 `Saver`를 만들 수 있다고 해서 아무 데이터나 저장해도 되는 것은 아닙니다. `rememberSaveable`은 작은 UI 복원 상태에만 쓰는 편이 안전합니다.

---
