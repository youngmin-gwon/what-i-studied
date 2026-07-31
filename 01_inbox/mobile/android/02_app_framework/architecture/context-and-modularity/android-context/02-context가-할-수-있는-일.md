# Context가 할 수 있는 일

상위 노트: [[android-context]]

| 역할                 | 대표 API                                                 | 예시                          |
|:-------------------|:-------------------------------------------------------|:----------------------------|
| 리소스 접근             | `getString()`, `resources`, `assets`                   | 다국어 문자열, 이미지, raw asset 읽기  |
| 컴포넌트 실행            | `startActivity()`, `startService()`, `sendBroadcast()` | 화면 열기, 서비스 시작, 방송 전송        |
| 시스템 서비스 접근         | `getSystemService()`                                   | 알림, 위치, 연결 상태, 클립보드         |
| 앱 저장소 접근           | `filesDir`, `cacheDir`, `getDatabasePath()`            | 앱 내부 파일, 캐시, DB 위치          |
| ContentProvider 접근 | `contentResolver`                                      | 연락처 조회, MediaStore 조회       |
| 권한/패키지 정보          | `checkSelfPermission()`, `packageManager`              | 권한 확인, 앱 버전/패키지 조회          |
| 테마/윈도우 연동          | Activity Context                                       | Dialog, Toast, themed UI 생성 |

예시:

```kotlin
val appName = context.getString(R.string.app_name)

val notificationManager =
    context.getSystemService(NotificationManager::class.java)

val file = File(context.filesDir, "session.json")

val cursor = context.contentResolver.query(
    ContactsContract.Contacts.CONTENT_URI,
    null,
    null,
    null,
    null,
)
```

---
