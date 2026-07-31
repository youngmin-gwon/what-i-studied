# SharedPreferences

상위 노트: [[android-storage-systems]]

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
