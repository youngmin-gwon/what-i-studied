# Room Database

상위 노트: [[android-jetpack-architecture]]

이미 [android-storage-systems](android-storage-systems.md) 에서 다뤘으나 추가 기능 소개.

##### 관계 (Relation)

```kotlin
// 일대다 관계
@Entity
data class User(
    @PrimaryKey val userId: Int,
    val name: String
)

@Entity
data class Post(
    @PrimaryKey val postId: Int,
    val userId: Int,
    val title: String
)

data class UserWithPosts(
    @Embedded val user: User,
    @Relation(
        parentColumn = "userId",
        entityColumn = "userId"
    )
    val posts: List<Post>
)

@Dao
interface UserDao {
    @Transaction
    @Query("SELECT * FROM User")
    fun getUsersWithPosts(): Flow<List<UserWithPosts>>
}
```

##### Migration

```kotlin
val MIGRATION_1_2 = object : Migration(1, 2) {
    override fun migrate(database: SupportSQLiteDatabase) {
        database.execSQL("ALTER TABLE User ADD COLUMN email TEXT")
    }
}

val db = Room.databaseBuilder(context, AppDatabase::class.java, "app_db")
    .addMigrations(MIGRATION_1_2)
    .build()
```

##### FTS (Full-Text Search)

```kotlin
@Entity
@Fts4
data class Article(
    @PrimaryKey @ColumnInfo(name = "rowid") val id: Int,
    val title: String,
    val content: String
)

@Dao
interface ArticleDao {
    @Query("SELECT * FROM Article WHERE Article MATCH :query")
    fun search(query: String): Flow<List<Article>>
}
```
