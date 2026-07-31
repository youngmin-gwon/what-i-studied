# Room Persistence Library (구조화된 데이터)

SQLite 를 안전하고 편리하게 사용할 수 있도록 추상화한 라이브러리다.

##### Entity & DAO

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

##### Database Setup

```kotlin
@Database(entities = [User::class], version = 1)
abstract class AppDatabase : RoomDatabase() {
    abstract fun userDao(): UserDao
}
```
