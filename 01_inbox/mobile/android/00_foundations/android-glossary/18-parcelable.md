# Parcelable

상위 노트: [[android-glossary]]

**정의**: Binder 로 전송하기 위한 객체 직렬화 인터페이스

**상세**:

Java Serializable 보다 빠르다. 객체를 Parcel 로 변환하여 프로세스 간 전달한다. Android Studio 가 자동 생성을 지원한다.

**예시**:

```kotlin
@Parcelize
data class User(
    val id: Int,
    val name: String
) : Parcelable

// Intent로 전달
val intent = Intent(this, DetailActivity::class.java)
intent.putExtra("user", user)
startActivity(intent)

// 수신
val user = intent.getParcelableExtra<User>("user")
```

**관련**: [android-binder-and-ipc](../01_system_internals/android-binder-and-ipc.md)

---
