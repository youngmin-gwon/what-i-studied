---
title: android-storage-systems
tags: [android, android/filesystem, android/scoped-storage, android/storage]
aliases: []
date modified: 2026-01-20 15:55:46 +09:00
date created: 2025-12-16 16:19:14 +09:00
---

## Android Storage Systems android android/storage android/filesystem

안드로이드의 파일 시스템과 저장소 접근 방식을 깊이 있게 다룬다. 기본은 [android-foundations](../00_foundations/android-foundations.md) 참고.

### 저장소 종류

#### 1. 내부 저장소 (Internal Storage)

앱 전용 공간. 다른 앱이 접근할 수 없다.

```kotlin
// 내부 저장소 경로: /data/data/com.example.app/files/
val file = File(filesDir, "myfile.txt")
file.writeText("Hello, World!")

// 캐시 디렉토리: /data/data/com.example.app/cache/
val cacheFile = File(cacheDir, "temp.jpg")
// 시스템이 공간 부족 시 자동 삭제 가능
```

**특징:**
- 앱 삭제 시 함께 삭제됨
- 권한 불필요
- 기기 저장소에 저장 (외장 SD 카드 아님)

#### 2. 외부 저장소 (External Storage)

공유 가능한 저장소. [[android-glossary#scoped-storage|Scoped Storage]] 규칙 적용.

```kotlin
// 앱 전용 외부 저장소: /storage/emulated/0/Android/data/com.example.app/files/
val externalFile = File(getExternalFilesDir(null), "document.pdf")
// 권한 불필요, 앱 삭제 시 함께 삭제

// 공유 저장소 (Android 10+)
// MediaStore 사용 필요
```

### Scoped Storage (Android 10+)

앱이 자신의 파일만 직접 접근하고, 다른 파일은 MediaStore/SAF 를 통해 접근한다.

#### MediaStore API

미디어 파일 (이미지, 비디오, 오디오, 다운로드) 접근.

**이미지 저장:**
```kotlin
fun saveImageToGallery(bitmap: Bitmap, displayName: String) {
    val contentValues = ContentValues().apply {
        put(MediaStore.Images.Media.DISPLAY_NAME, displayName)
        put(MediaStore.Images.Media.MIME_TYPE, "image/jpeg")
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
            put(MediaStore.Images.Media.RELATIVE_PATH, Environment.DIRECTORY_PICTURES)
            put(MediaStore.Images.Media.IS_PENDING, 1)
        }
    }
    
    val resolver = contentResolver
    val uri = resolver.insert(MediaStore.Images.Media.EXTERNAL_CONTENT_URI, contentValues)
    
    uri?.let {
        resolver.openOutputStream(it)?.use { outputStream ->
            bitmap.compress(Bitmap.CompressFormat.JPEG, 95, outputStream)
        }
        
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
            contentValues.clear()
            contentValues.put(MediaStore.Images.Media.IS_PENDING, 0)
            resolver.update(it, contentValues, null, null)
        }
    }
}
```

**이미지 읽기:**
```kotlin
fun loadImagesFromGallery(): List<Uri> {
    val images = mutableListOf<Uri>()
    val projection = arrayOf(
        MediaStore.Images.Media._ID,
        MediaStore.Images.Media.DISPLAY_NAME,
        MediaStore.Images.Media.DATE_ADDED
    )
    
    val sortOrder = "${MediaStore.Images.Media.DATE_ADDED} DESC"
    
    contentResolver.query(
        MediaStore.Images.Media.EXTERNAL_CONTENT_URI,
        projection,
        null,
        null,
        sortOrder
    )?.use { cursor ->
        val idColumn = cursor.getColumnIndexOrThrow(MediaStore.Images.Media._ID)
        
        while (cursor.moveToNext()) {
            val id = cursor.getLong(idColumn)
            val uri = ContentUris.withAppendedId(
                MediaStore.Images.Media.EXTERNAL_CONTENT_URI,
                id
            )
            images.add(uri)
        }
    }
    
    return images
}
```

**비디오 저장:**
```kotlin
@RequiresApi(Build.VERSION_CODES.Q)
fun saveVideoToGallery(videoFile: File, displayName: String) {
    val contentValues = ContentValues().apply {
        put(MediaStore.Video.Media.DISPLAY_NAME, displayName)
        put(MediaStore.Video.Media.MIME_TYPE, "video/mp4")
        put(MediaStore.Video.Media.RELATIVE_PATH, Environment.DIRECTORY_MOVIES)
    }
    
    val uri = contentResolver.insert(
        MediaStore.Video.Media.EXTERNAL_CONTENT_URI,
        contentValues
    )
    
    uri?.let {
        contentResolver.openOutputStream(it)?.use { outputStream ->
            videoFile.inputStream().use { inputStream ->
                inputStream.copyTo(outputStream)
            }
        }
    }
}
```

#### Storage Access Framework (SAF)

사용자가 직접 파일/폴더를 선택하도록 한다.

**파일 선택:**
```kotlin
class MainActivity : AppCompatActivity() {
    private val openDocumentLauncher = registerForActivityResult(
        ActivityResultContracts.OpenDocument()
    ) { uri: Uri? ->
        uri?.let {
            // 선택된 파일 읽기
            contentResolver.openInputStream(it)?.use { inputStream ->
                val text = inputStream.bufferedReader().readText()
                // 사용
            }
        }
    }
    
    fun selectDocument() {
        openDocumentLauncher.launch(arrayOf("text/plain", "application/pdf"))
    }
}
```

**파일 생성:**
```kotlin
private val createDocumentLauncher = registerForActivityResult(
    ActivityResultContracts.CreateDocument("text/plain")
) { uri: Uri? ->
    uri?.let {
        contentResolver.openOutputStream(it)?.use { outputStream ->
            outputStream.write("Hello, SAF!".toByteArray())
        }
    }
}

fun createNewDocument() {
    createDocumentLauncher.launch("myfile.txt")
}
```

**폴더 선택 (트리 접근):**
```kotlin
private val openDocumentTreeLauncher = registerForActivityResult(
    ActivityResultContracts.OpenDocumentTree()
) { uri: Uri? ->
    uri?.let { treeUri ->
        // 영구 권한 획득
        contentResolver.takePersistableUriPermission(
            treeUri,
            Intent.FLAG_GRANT_READ_URI_PERMISSION or Intent.FLAG_GRANT_WRITE_URI_PERMISSION
        )
        
        // 폴더 내 파일 나열
        val documentFile = DocumentFile.fromTreeUri(this, treeUri)
        documentFile?.listFiles()?.forEach { file ->
            Log.d("SAF", "File: ${file.name}")
        }
    }
}
```

### 파일 시스템 구조

```
/data/
├── data/
│   └── com.example.app/          # 앱 내부 저장소
│       ├── files/                # filesDir
│       ├── cache/                # cacheDir
│       ├── code_cache/           # 컴파일된 코드
│       ├── databases/            # SQLite DB
│       └── shared_prefs/         # SharedPreferences
│
├── user/0/com.example.app/       # 사용자별 데이터 (멀티 유저)
│
└── media/0/                      # 미디어 저장소
    └── com.example.app/

/storage/emulated/0/              # 외부 저장소 (주 사용자)
├── Android/
│   └── data/
│       └── com.example.app/      # 앱 전용 외부 저장소
│           ├── files/            # getExternalFilesDir()
│           └── cache/            # getExternalCacheDir()
│
├── DCIM/                         # 카메라 사진
├── Pictures/                     # 일반 이미지
├── Movies/                       # 비디오
├── Music/                        # 음악
├── Download/                     # 다운로드
└── Documents/                    # 문서
```

### 데이터 저장 방법 선택

| 데이터 종류 | 저장 방법 |
|------------|----------|
| 키 - 값 쌍 | SharedPreferences, DataStore |
| 구조화된 데이터 | Room, SQLite |
| 파일 (앱 전용) | 내부 저장소 |
| 미디어 (공유) | MediaStore |
| 문서 (사용자 선택) | SAF |
| 대용량 파일 | 외부 저장소 + 캐시 |

### SharedPreferences

간단한 키 - 값 저장.

```kotlin
// 저장
val sharedPref = getSharedPreferences("my_prefs", Context.MODE_PRIVATE)
with(sharedPref.edit()) {
    putString("username", "john")
    putInt("age", 25)
    putBoolean("is_logged_in", true)
    apply() // 비동기, commit() 은 동기
}

// 읽기
val username = sharedPref.getString("username", "default")
val age = sharedPref.getInt("age", 0)
```

**문제점:**
- UI 스레드에서 읽기 시 블로킹
- 타입 안전성 부족
- 대용량 데이터 부적합

### DataStore (권장)

SharedPreferences 의 현대적 대안.

#### Preferences DataStore

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

#### Proto DataStore (타입 안전)

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

### Room Database

SQLite 위의 추상화 레이어.

```kotlin
// Entity
@Entity(tableName = "users")
data class User(
    @PrimaryKey(autoGenerate = true) val id: Int = 0,
    @ColumnInfo(name = "user_name") val userName: String,
    val age: Int
)

// DAO
@Dao
interface UserDao {
    @Query("SELECT * FROM users")
    fun getAll(): Flow<List<User>>
    
    @Query("SELECT * FROM users WHERE id = :userId")
    suspend fun getById(userId: Int): User?
    
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insert(user: User)
    
    @Update
    suspend fun update(user: User)
    
    @Delete
    suspend fun delete(user: User)
    
    @Query("DELETE FROM users")
    suspend fun deleteAll()
}

// Database
@Database(entities = [User::class], version = 1)
abstract class AppDatabase : RoomDatabase() {
    abstract fun userDao(): UserDao
    
    companion object {
        @Volatile
        private var INSTANCE: AppDatabase? = null
        
        fun getDatabase(context: Context): AppDatabase {
            return INSTANCE ?: synchronized(this) {
                val instance = Room.databaseBuilder(
                    context.applicationContext,
                    AppDatabase::class.java,
                    "app_database"
                )
                .fallbackToDestructiveMigration() // 개발 중에만
                .build()
                INSTANCE = instance
                instance
            }
        }
    }
}

// 사용
class UserRepository(private val userDao: UserDao) {
    val allUsers: Flow<List<User>> = userDao.getAll()
    
    suspend fun insert(user: User) {
        userDao.insert(user)
    }
}
```

### 파일 암호화

#### File-Based Encryption (FBE)

[[android-glossary#fbe|FBE]] 는 사용자별로 파일을 암호화한다.

- **Device Encrypted (DE)**: 부팅 직후 사용 가능, 잠금 해제 불필요
- **Credential Encrypted (CE)**: 사용자 잠금 해제 후 사용 가능

```kotlin
// DE 저장소 사용 (부팅 직후 접근 가능)
val deContext = createDeviceProtectedStorageContext()
val deFile = File(deContext.filesDir, "boot_count.txt")

// CE 저장소 (기본, 잠금 해제 후)
val ceFile = File(filesDir, "user_data.txt")
```

#### EncryptedFile

```kotlin
// build.gradle.kts
dependencies {
    implementation("androidx.security:security-crypto:1.1.0-alpha06")
}

// 마스터 키 생성
val masterKey = MasterKey.Builder(context)
    .setKeyScheme(MasterKey.KeyScheme.AES256_GCM)
    .build()

// 파일 암호화
val file = File(filesDir, "secret.txt")
val encryptedFile = EncryptedFile.Builder(
    context,
    file,
    masterKey,
    EncryptedFile.FileEncryptionScheme.AES256_GCM_HKDF_4KB
).build()

// 쓰기
encryptedFile.openFileOutput().use { outputStream ->
    outputStream.write("Secret data".toByteArray())
}

// 읽기
val text = encryptedFile.openFileInput().bufferedReader().readText()
```

#### EncryptedSharedPreferences

```kotlin
val masterKey = MasterKey.Builder(context)
    .setKeyScheme(MasterKey.KeyScheme.AES256_GCM)
    .build()

val sharedPreferences = EncryptedSharedPreferences.create(
    context,
    "secret_prefs",
    masterKey,
    EncryptedSharedPreferences.PrefKeyEncryptionScheme.AES256_SIV,
    EncryptedSharedPreferences.PrefValueEncryptionScheme.AES256_GCM
)

sharedPreferences.edit {
    putString("api_key", "secret_key_12345")
}
```

### 저장소 공간 관리

```kotlin
// 사용 가능한 공간 확인
fun getAvailableSpace(): Long {
    val stat = StatFs(filesDir.absolutePath)
    return stat.availableBytes
}

// 앱이 사용 중인 공간
fun getAppStorageSize(): Long {
    val storageStatsManager = getSystemService(Context.STORAGE_STATS_SERVICE) as StorageStatsManager
    val uuid = StorageManager.UUID_DEFAULT
    val uid = android.os.Process.myUid()
    
    return if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
        storageStatsManager.queryStatsForUid(uuid, uid).dataBytes
    } else {
        0L
    }
}

// 캐시 정리
fun clearCache() {
    cacheDir.deleteRecursively()
    externalCacheDir?.deleteRecursively()
}
```

### 백업과 복원

#### Auto Backup (Android 6.0+)

```xml
<!-- AndroidManifest.xml -->
<application
    android:allowBackup="true"
    android:fullBackupContent="@xml/backup_rules">
```

```xml
<!-- res/xml/backup_rules.xml -->
<full-backup-content>
    <include domain="file" path="important.txt" />
    <exclude domain="file" path="cache/" />
    <exclude domain="database" path="temp.db" />
</full-backup-content>
```

#### Backup Agent (커스텀)

```kotlin
class MyBackupAgent : BackupAgentHelper() {
    override fun onCreate() {
        SharedPreferencesBackupHelper(this, "my_prefs").also {
            addHelper("prefs", it)
        }
        
        FileBackupHelper(this, "important.txt").also {
            addHelper("files", it)
        }
    }
}
```

### 성능 최적화

```kotlin
// ✅ 버퍼링 사용
file.bufferedWriter().use { writer ->
    writer.write("Large content")
}

// ❌ 작은 쓰기 반복
file.writeText("a")
file.appendText("b") // 매번 파일 열기/닫기

// ✅ 비동기 I/O
lifecycleScope.launch(Dispatchers.IO) {
    val data = file.readText()
    withContext(Dispatchers.Main) {
        textView.text = data
    }
}

// ✅ 메모리 매핑 (대용량 파일)
val channel = FileInputStream(file).channel
val buffer = channel.map(FileChannel.MapMode.READ_ONLY, 0, channel.size())
```

### 디버깅

```bash
# 앱 저장소 확인
adb shell ls -la /data/data/com.example.app/

# 파일 내용 보기
adb shell cat /data/data/com.example.app/files/myfile.txt

# 파일 복사 (기기 → PC)
adb pull /data/data/com.example.app/files/myfile.txt

# 파일 복사 (PC → 기기)
adb push myfile.txt /data/data/com.example.app/files/

# 저장소 사용량
adb shell dumpsys diskstats

# MediaStore 확인
adb shell content query --uri content://media/external/images/media
```

### 더 보기

[android-permissions-deep-dive](../05_security_privacy/android-permissions-deep-dive.md), [android-security-and-sandboxing](../05_security_privacy/android-security-and-sandboxing.md), [android-app-components-deep-dive](android-app-components-deep-dive.md), [android-jetpack-architecture](android-jetpack-architecture.md)
