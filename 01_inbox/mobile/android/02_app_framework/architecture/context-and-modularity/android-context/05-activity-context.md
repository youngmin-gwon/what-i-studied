# Activity Context

상위 노트: [android-context](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/android-context.md)

`Activity` 자체도 `Context`입니다.

```kotlin
class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        val activityContext: Context = this
    }
}
```

Activity Context는 화면, 윈도우, 테마와 연결됩니다.

적합한 예:

```kotlin
AlertDialog.Builder(activityContext)
    .setTitle("삭제")
    .setMessage("정말 삭제할까요?")
    .show()
```

```kotlin
val intent = Intent(activityContext, DetailActivity::class.java)
activityContext.startActivity(intent)
```

Activity Context가 필요한 경우:

```text
Dialog / BottomSheet / Popup처럼 window token이 필요한 UI
Activity theme가 적용된 View 생성
Activity Result / permission launcher와 연결되는 흐름
새 Activity 실행
```

하지만 Activity Context는 수명이 짧습니다. 화면 회전, 다크 모드 변경, 멀티 윈도우 변화 등으로 Activity는 재생성될 수 있습니다.

```kotlin
object BadSingleton {
    // 나쁜 예: Activity가 사라져도 붙잡고 있어 memory leak 가능
    lateinit var context: Context
}
```

> [!IMPORTANT]
> Activity Context를 singleton, Repository, long-running coroutine에 저장하지 마세요. 화면이 사라졌는데 Activity를 계속
> 붙잡아 memory leak을 만들 수 있습니다.

---
