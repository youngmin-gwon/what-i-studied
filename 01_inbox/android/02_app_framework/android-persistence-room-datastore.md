---
title: android-persistence-room-datastore
tags: [android, android/persistence, android/room, android/datastore, android/database]
aliases: [Room, DataStore, Persistence, SQLite, SharedPreferences migration]
date modified: 2026-04-04 00:22:00 +09:00
date created: 2026-04-04 00:22:00 +09:00
---

## Android Modern Persistence: Room & DataStore

현대적인 안드로이드 앱은 반응형(Reactive) 데이터 흐름을 기반으로 한다. 단순히 데이터를 저장하고 불러오는 것을 넘어, 데이터의 변화를 감지하고 UI를 자동으로 갱신하는 것이 핵심이다.

> [!NOTE] **iOS 비교: SwiftData vs Room/DataStore**
> - **iOS**: `SwiftData`가 SQLite를 추상화하며, `@Model` 매크로와 `Query`를 통해 선언형 데이터 관리를 제공한다. (iOS 17+)
> - **Android**: `Room`이 SQLite를 추상화하며, `Flow`와의 강력한 통합을 통해 반응형 데이터 스트림을 구축한다. **DataStore**는 `SharedPreferences`를 대체하여 타입 세이프하고 비동기적인 설정 저장을 보장한다.
> 자세한 내용은 [apple-swiftdata-deep-dive](../../apple/03_data_networking/apple-swiftdata-deep-dive.md)를 참고하세요.

### 1. Room Persistence Library (구조화된 데이터)

SQLite를 안전하고 편리하게 사용할 수 있도록 추상화한 라이브러리다.

#### Entity & DAO

```kotlin
@Entity(tableName = "users")
data class User(
    @PrimaryKey val id: String,
    val name: String,
    val age: Int
)

@Dao
interface UserDao {
    @Query("SELECT * FROM users")
    fun getAllUsers(): Flow<List<User>> // 데이터 변화 감지 (Flow)

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insertUser(user: User)

    @Delete
    suspend fun deleteUser(user: User)
}
```

#### Database Setup

```kotlin
@Database(entities = [User::class], version = 1)
abstract class AppDatabase : RoomDatabase() {
    abstract fun userDao(): UserDao
}
```

### 2. DataStore (설정 및 키-값 데이터)

`SharedPreferences`의 고질적인 문제(동기 블로킹, 런타임 예외)를 해결하기 위해 도입되었다.

#### Preferences DataStore (단순 키-값)

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

#### Proto DataStore (타입 세이프, 스키마 정의 필수)

프로토콜 버퍼(Protobuf)를 사용하여 복잡한 데이터 구조를 타입 세이프하게 저장한다. **더 강력한 타입 세이프티가 필요할 때** 권장된다.

> [!CAUTION] **SharedPreferences → DataStore 마이그레이션 필수**
> 구글은 이미 SharedPreferences를 레거시로 분류했다. `SharedPreferencesMigration` 클래스를 사용하여 기존 데이터를 안전하게 DataStore로 옮겨야 한다.

### 🏛️ 아키텍처 연동 (Hilt + Coroutines)

데이터 레이어는 언제나 캡슐화되어야 하며, UI 레이어는 `Flow`를 통해 데이터를 관찰해야 한다.

```kotlin
class UserRepository @Inject constructor(
    private val userDao: UserDao,
    private val userPrefs: DataStore<UserPreferences>
) {
    val users: Flow<List<User>> = userDao.getAllUsers()
    val preferences: Flow<UserPreferences> = userPrefs.data
}
```

### 더 보기
- [android-storage-systems](android-storage-systems.md)
- [android-coroutines-flow](android-coroutines-flow.md)
- [android-jetpack-architecture](android-jetpack-architecture.md)
- [android-viewmodel](android-viewmodel.md)
