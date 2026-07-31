# DataStore (권장)

상위 노트: [android-storage-systems](01_inbox/mobile/android/02_app_framework/data/storage/android-storage-systems.md)

SharedPreferences 의 현대적 대안.

##### Preferences DataStore

```kotlin
// build.gradle.kts
dependencies {
    implementation("androidx.datastore:datastore-preferences:1.0.0")
}

// DataStore 생성
val Context.dataStore: DataStore<Preferences> by preferencesDataStore(name = "settings")

// 키 정의
object PreferencesKeys {
    val USERNAME = stringPreferencesKey("username")
    val AGE = intPreferencesKey("age")
}

// 저장
suspend fun saveUser(username: String, age: Int) {
    dataStore.edit { preferences ->
        preferences[PreferencesKeys.USERNAME] = username
        preferences[PreferencesKeys.AGE] = age
    }
}

// 읽기 (Flow)
val usernameFlow: Flow<String> = dataStore.data
    .map { preferences ->
        preferences[PreferencesKeys.USERNAME] ?: "default"
    }

// Activity 에서 사용
lifecycleScope.launch {
    usernameFlow.collect { username ->
        textView.text = username
    }
}
```

##### Proto DataStore (타입 안전)

```protobuf
// user_prefs.proto
syntax = "proto3";

option java_package = "com.example.app";
option java_multiple_files = true;

message UserPreferences {
  string username = 1;
  int32 age = 2;
  bool is_logged_in = 3;
}
```

```kotlin
// Serializer
object UserPreferencesSerializer : Serializer<UserPreferences> {
    override val defaultValue: UserPreferences = UserPreferences.getDefaultInstance()
    
    override suspend fun readFrom(input: InputStream): UserPreferences {
        return UserPreferences.parseFrom(input)
    }
    
    override suspend fun writeTo(t: UserPreferences, output: OutputStream) {
        t.writeTo(output)
    }
}

// DataStore 생성
val Context.userPreferencesStore: DataStore<UserPreferences> by dataStore(
    fileName = "user_prefs.pb",
    serializer = UserPreferencesSerializer
)

// 사용
suspend fun updateUsername(username: String) {
    userPreferencesStore.updateData { currentPrefs ->
        currentPrefs.toBuilder()
            .setUsername(username)
            .build()
    }
}
```
