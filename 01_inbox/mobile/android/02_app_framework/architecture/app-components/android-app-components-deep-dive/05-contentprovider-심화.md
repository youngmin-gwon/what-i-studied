# ContentProvider 심화

상위 노트: [[android-app-components-deep-dive]]

앱 간 데이터 공유를 위한 표준 인터페이스.

##### 구현 예시

```kotlin
class MyContentProvider : ContentProvider() {
    private lateinit var database: SQLiteDatabase
    
    companion object {
        const val AUTHORITY = "com.example.provider"
        val CONTENT_URI: Uri = Uri.parse("content://$AUTHORITY/items")
        
        private const val ITEMS = 1
        private const val ITEM_ID = 2
        
        private val uriMatcher = UriMatcher(UriMatcher.NO_MATCH).apply {
            addURI(AUTHORITY, "items", ITEMS)
            addURI(AUTHORITY, "items/#", ITEM_ID)
        }
    }
    
    override fun onCreate(): Boolean {
        database = context?.let { MyDatabaseHelper(it).writableDatabase }
            ?: return false
        return true
    }
    
    override fun query(
        uri: Uri,
        projection: Array<out String>?,
        selection: String?,
        selectionArgs: Array<out String>?,
        sortOrder: String?
    ): Cursor? {
        val cursor = when (uriMatcher.match(uri)) {
            ITEMS -> database.query("items", projection, selection, selectionArgs, null, null, sortOrder)
            ITEM_ID -> {
                val id = uri.lastPathSegment
                database.query("items", projection, "_id=?", arrayOf(id), null, null, sortOrder)
            }
            else -> throw IllegalArgumentException("Unknown URI: $uri")
        }
        cursor.setNotificationUri(context?.contentResolver, uri)
        return cursor
    }
    
    override fun insert(uri: Uri, values: ContentValues?): Uri? {
        val id = database.insert("items", null, values)
        context?.contentResolver?.notifyChange(uri, null)
        return Uri.withAppendedPath(CONTENT_URI, id.toString())
    }
    
    override fun update(uri: Uri, values: ContentValues?, selection: String?, selectionArgs: Array<out String>?): Int {
        val count = database.update("items", values, selection, selectionArgs)
        context?.contentResolver?.notifyChange(uri, null)
        return count
    }
    
    override fun delete(uri: Uri, selection: String?, selectionArgs: Array<out String>?): Int {
        val count = database.delete("items", selection, selectionArgs)
        context?.contentResolver?.notifyChange(uri, null)
        return count
    }
    
    override fun getType(uri: Uri): String? {
        return when (uriMatcher.match(uri)) {
            ITEMS -> "vnd.android.cursor.dir/vnd.$AUTHORITY.items"
            ITEM_ID -> "vnd.android.cursor.item/vnd.$AUTHORITY.items"
            else -> null
        }
    }
}
```

##### 권한 설정

```xml
<provider
    android:name=".MyContentProvider"
    android:authorities="com.example.provider"
    android:exported="true"
    android:readPermission="com.example.READ_ITEMS"
    android:writePermission="com.example.WRITE_ITEMS" />

<permission
    android:name="com.example.READ_ITEMS"
    android:protectionLevel="normal" />
```

##### 사용 예시

```kotlin
// 다른 앱에서 접근
val cursor = contentResolver.query(
    Uri.parse("content://com.example.provider/items"),
    null, null, null, null
)

cursor?.use {
    while (it.moveToNext()) {
        val name = it.getString(it.getColumnIndexOrThrow("name"))
        // 데이터 사용
    }
}
```
