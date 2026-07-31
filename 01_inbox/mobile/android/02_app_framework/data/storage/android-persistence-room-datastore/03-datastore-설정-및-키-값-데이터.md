# DataStore (설정 및 키 - 값 데이터)

`SharedPreferences` 의 고질적인 문제(동기 블로킹, 런타임 예외)를 해결하기 위해 도입되었다.

##### Preferences DataStore (단순 키 - 값)

```kotlin
// 정의
val Context.dataStore: DataStore<Preferences> by preferencesDataStore(name = "settings")

object PreferenceKeys {
    val USER_NAME = stringPreferencesKey("user_name")
}

// 읽기 (Flow)
val userName: Flow<String> = context.dataStore.data
    .map { preferences -> preferences[PreferenceKeys.USER_NAME] ?: "" }

// 쓰기 (suspend)
suspend fun updateName(name: String) {
    context.dataStore.edit { preferences ->
        preferences[PreferenceKeys.USER_NAME] = name
    }
}
```

##### Proto DataStore (타입 세이프, 스키마 정의 필수)

프로토콜 버퍼(Protobuf)를 사용하여 복잡한 데이터 구조를 타입 세이프하게 저장한다. **더 강력한 타입 세이프티가 필요할 때** 권장된다.

>[!CAUTION] **SharedPreferences → DataStore 마이그레이션 필수**
>구글은 이미 SharedPreferences 를 레거시로 분류했다. `SharedPreferencesMigration` 클래스를 사용하여 기존 데이터를 안전하게 DataStore 로 옮겨야 한다.
