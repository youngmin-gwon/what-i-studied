# Compose에서 Context: LocalContext

상위 노트: [[android-context]]

Compose에는 Flutter의 `BuildContext`처럼 함수 파라미터로 `context`가 자동으로 들어오지 않습니다.

대신 필요할 때 `LocalContext.current`를 읽습니다.

```kotlin
@Composable
fun ShareButton(fileUri: Uri) {
    val context = LocalContext.current

    Button(
        onClick = {
            val intent = Intent(Intent.ACTION_SEND).apply {
                type = "application/pdf"
                putExtra(Intent.EXTRA_STREAM, fileUri)
                addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION)
            }
            context.startActivity(Intent.createChooser(intent, "공유"))
        }
    ) {
        Text("공유")
    }
}
```

`LocalContext.current`는 보통 현재 Activity Context입니다. 그래서 UI와 가까운 작업에는 편리합니다.

적합한 예:

```text
Intent 실행
Android resource 접근
Toast 표시
Activity Result launcher와 함께 플랫폼 API 호출
ClipboardManager 같은 system service 접근
```

주의할 점:

```kotlin
@Composable
fun BadScreen() {
    val context = LocalContext.current

    // 나쁜 예: Composable 안에서 Repository를 직접 만들고 Context를 오래 보관
    val repository = remember {
        SessionRepository(context)
    }
}
```

이런 객체는 DI나 ViewModel에서 만들고, 필요하면 `applicationContext`를 주입하는 편이 좋습니다.

---
