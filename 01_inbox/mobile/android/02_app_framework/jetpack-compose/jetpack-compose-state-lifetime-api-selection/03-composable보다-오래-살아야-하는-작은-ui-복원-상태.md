# Composable보다 오래 살아야 하는 작은 UI 복원 상태

상위 노트: [[jetpack-compose-state-lifetime-api-selection]]

화면 회전, Activity 재생성, process death 후에도 작은 UI 값이 복원되어야 하면 `rememberSaveable`을 씁니다.

```kotlin
@Composable
fun SearchHeader() {
    var query by rememberSaveable {
        mutableStateOf("")
    }

    TextField(
        value = query,
        onValueChange = { query = it },
    )
}
```

적합한 상태:

- 입력 draft
- 선택된 tab key
- filter enum/string
- 간단한 page id
- 작은 boolean/int/string 상태

부적합한 상태:

- repository, client, database
- bitmap, 큰 list, entity 전체 목록
- auth token, session key 같은 영구 보관 데이터
- 서버에서 다시 받아야 하는 큰 screen data

`rememberSaveable`은 저장소가 아니라 UI 복원 장치입니다. 앱을 껐다 켜도 의미 있게 남아야 하는 데이터는 DataStore/Room으로 내려야 합니다.

---
