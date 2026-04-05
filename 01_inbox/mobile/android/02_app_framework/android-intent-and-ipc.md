# [[mobile-security]] > [[android-intent-and-ipc]]

## Android Intent & IPC: Messaging Framework

안드로이드 시스템의 핵심 통신 메커니즘인 **Intent**와 프로세스 간 통신(**IPC**)을 심층 분석합니다. 

단순히 앱 컴포넌트를 실행하는 도구를 넘어, 시스템 전체의 데이터 흐름을 제어하고 보안 경계를 정의하는 중추적인 역할을 이해하는 것이 목표입니다. 

---

### 💡 Context: Intent vs iOS 통신 방식

안드로이드의 Intent 시스템은 iOS에서 분리되어 있는 여러 개념(URL Scheme, Universal Links, XPC, App Intents)을 **하나의 통합된 메시징 표준**으로 처리합니다. 

> [!NOTE] **상호 참조**
> iOS의 유사 기능은 [[apple-interprocess-and-xpc]] 및 [[apple-app-intents]]를 참고하세요.

---

### Intent 의 구성 요소

```kotlin
val intent = Intent().apply {
    action = Intent.ACTION_VIEW          // 무엇을 할 것인가
    data = Uri.parse("https://example.com") // 대상 데이터
    type = "text/html"                    // MIME 타입
    component = ComponentName(             // 명시적 대상 (옵션)
        "com.example", "com.example.MainActivity"
    )
    putExtra("key", "value")              // 추가 데이터
    addCategory(Intent.CATEGORY_BROWSABLE) // 분류
    addFlags(Intent.FLAG_ACTIVITY_NEW_TASK) // 동작 플래그
}
```

| 속성 | 역할 | 예시 |
|------|------|------|
| **action** | 수행할 작업 | `ACTION_VIEW`, `ACTION_SEND`, `ACTION_DIAL` |
| **data** | 작업 대상 URI | `tel:010-1234-5678`, `content://contacts/1` |
| **type** | MIME 타입 | `image/jpeg`, `text/plain` |
| **component** | 명시적 대상 클래스 | `ComponentName(pkg, cls)` |
| **extras** | 번들 데이터 | `putExtra("userId", "123")` |
| **category** | 추가 분류 | `CATEGORY_LAUNCHER`, `CATEGORY_BROWSABLE` |
| **flags** | 동작 제어 | `FLAG_ACTIVITY_CLEAR_TOP` |

### Explicit vs Implicit Intent

#### Explicit Intent (명시적)

대상 컴포넌트를 정확히 지정한다. **앱 내부 화면 전환**에 사용.

```kotlin
// 같은 앱 내에서 Activity 시작
val intent = Intent(this, DetailActivity::class.java).apply {
    putExtra("USER_ID", userId)
}
startActivity(intent)

// 서비스 시작
Intent(this, DownloadService::class.java).also { intent ->
    startService(intent)
}
```

> [!CAUTION] **Devil's Advocate : Single-Activity 시대에서의 Explicit Intent**
> 현대 앱에서 Activity 간 `startActivity(intent)` 호출은 **거의 사라졌다**. 화면 전환은 `Navigation Compose` (또는 Navigation Component)로 처리하며, Explicit Intent 는 **외부 앱 실행**(카메라, 설정 등)이나 **Service 시작** 용도로만 남아있다.
> [android-deep-links](android-deep-links.md) 에서 Navigation 기반 딥링크 처리를 참고하라.

#### Implicit Intent (암시적)

대상을 지정하지 않고 **action + data** 로 시스템에 위임한다.

```kotlin
// 웹페이지 열기
val webIntent = Intent(Intent.ACTION_VIEW, Uri.parse("https://developer.android.com"))
startActivity(webIntent)

// 전화 걸기
val dialIntent = Intent(Intent.ACTION_DIAL, Uri.parse("tel:010-1234-5678"))
startActivity(dialIntent)

// 공유하기
val shareIntent = Intent(Intent.ACTION_SEND).apply {
    type = "text/plain"
    putExtra(Intent.EXTRA_TEXT, "공유할 내용")
}
startActivity(Intent.createChooser(shareIntent, "공유 방법 선택"))
```

#### 안전한 Implicit Intent 사용

```kotlin
// ✅ 처리할 수 있는 앱이 있는지 확인 (크래시 방지)
val intent = Intent(Intent.ACTION_VIEW, Uri.parse("geo:37.5665,126.9780"))
if (intent.resolveActivity(packageManager) != null) {
    startActivity(intent)
} else {
    // 지도 앱이 설치되어 있지 않음
    Toast.makeText(this, "지도 앱을 설치해주세요", Toast.LENGTH_SHORT).show()
}
```

### Intent Filter

컴포넌트가 수신 가능한 Intent 유형을 선언한다.

```xml
<activity android:name=".ShareReceiverActivity"
    android:exported="true">
    <intent-filter>
        <!-- action: 이 Activity가 처리할 수 있는 작업 -->
        <action android:name="android.intent.action.SEND" />
        
        <!-- category: DEFAULT 필수 (암시적 Intent 수신 조건) -->
        <category android:name="android.intent.category.DEFAULT" />
        
        <!-- data: 처리 가능한 데이터 타입 -->
        <data android:mimeType="text/plain" />
        <data android:mimeType="image/*" />
    </intent-filter>
</activity>
```

**Intent Resolution 규칙:**
1. `action` 이 일치해야 함
2. `category` 가 모두 포함되어야 함 (DEFAULT 는 시스템이 자동 추가)
3. `data` (URI scheme + MIME type)가 일치해야 함

### `<queries>` 태그 (Package Visibility, Android 11+)

Android 11부터 앱이 다른 앱의 존재를 확인하려면 매니페스트에 명시적으로 선언해야 한다.

```xml
<manifest>
    <queries>
        <!-- 특정 패키지 -->
        <package android:name="com.kakao.talk" />
        
        <!-- 특정 Intent를 처리하는 앱 -->
        <intent>
            <action android:name="android.intent.action.SEND" />
            <data android:mimeType="image/*" />
        </intent>
        
        <!-- 특정 Content Provider -->
        <provider android:authorities="com.example.provider" />
    </queries>
</manifest>
```

> [!WARNING] **`<queries>` 없이 `resolveActivity()` 호출하면 null 반환**
> Android 11+ 에서는 `<queries>` 에 선언하지 않은 앱은 보이지 않는다. `QUERY_ALL_PACKAGES` 권한은 구글 플레이 정책상 특수 앱(런처, 보안 앱)만 승인된다.

### PendingIntent

다른 앱(시스템)이 **우리 앱 대신** 나중에 Intent 를 실행할 수 있도록 하는 토큰이다. 주로 **알림(Notification)**, **AlarmManager**, **위젯** 에서 사용된다.

```kotlin
// 알림 클릭 시 실행할 PendingIntent
val intent = Intent(context, MainActivity::class.java).apply {
    flags = Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_CLEAR_TASK
}

val pendingIntent = PendingIntent.getActivity(
    context,
    REQUEST_CODE,
    intent,
    PendingIntent.FLAG_IMMUTABLE  // Android 12+ 필수
)

val notification = NotificationCompat.Builder(context, CHANNEL_ID)
    .setContentTitle("새 메시지")
    .setContentText("확인하세요")
    .setContentIntent(pendingIntent)     // 클릭 시 실행
    .setAutoCancel(true)                 // 클릭 후 알림 제거
    .build()
```

#### PendingIntent 보안 (Android 12+ 필수)

```kotlin
// ✅ FLAG_IMMUTABLE (기본, 대부분의 경우)
// → 수신 앱이 Intent 내용을 수정 불가
PendingIntent.getActivity(ctx, 0, intent, PendingIntent.FLAG_IMMUTABLE)

// ✅ FLAG_MUTABLE (인라인 답장 등 특수한 경우만)
// → 수신 앱이 extras 를 수정 가능
PendingIntent.getActivity(ctx, 0, intent, PendingIntent.FLAG_MUTABLE)

// ✅ FLAG_ONE_SHOT (일회성 작업)
// → 한 번 실행하면 재사용 불가 (리플레이 공격 방지)
PendingIntent.getActivity(ctx, 0, intent,
    PendingIntent.FLAG_IMMUTABLE or PendingIntent.FLAG_ONE_SHOT)
```

> [!CAUTION] **Android 12+ 에서 Mutability 미지정 시 크래시**
> `FLAG_IMMUTABLE` 또는 `FLAG_MUTABLE` 중 하나를 반드시 지정해야 한다. 미지정 시 `IllegalArgumentException` 발생.

### Activity Result API (Modern)

`startActivityForResult()` / `onActivityResult()` 는 **deprecated** 되었다. 현대적 대안은 `ActivityResultContracts` 이다.

```kotlin
class MyActivity : AppCompatActivity() {

    // 1. 콜백 등록 (onCreate 전에)
    private val pickImage = registerForActivityResult(
        ActivityResultContracts.PickVisualMedia()
    ) { uri: Uri? ->
        uri?.let { handleSelectedImage(it) }
    }
    
    private val requestPermission = registerForActivityResult(
        ActivityResultContracts.RequestPermission()
    ) { isGranted: Boolean ->
        if (isGranted) {
            // 권한 허용됨
        } else {
            // 권한 거부됨
        }
    }
    
    private val takePicture = registerForActivityResult(
        ActivityResultContracts.TakePicture()
    ) { success: Boolean ->
        if (success) {
            // 사진 촬영 성공
        }
    }

    // 2. 실행
    fun onPickImageClick() {
        pickImage.launch(
            PickVisualMediaRequest(ActivityResultContracts.PickVisualMedia.ImageOnly)
        )
    }
    
    fun onRequestCameraClick() {
        requestPermission.launch(Manifest.permission.CAMERA)
    }
}
```

**주요 Contract 종류:**

| Contract | 용도 | 반환 |
|----------|------|------|
| `PickVisualMedia` | Photo Picker (권한 불필요!) | `Uri?` |
| `PickMultipleVisualMedia` | 다중 선택 | `List<Uri>` |
| `TakePicture` | 카메라 촬영 | `Boolean` |
| `RequestPermission` | 단일 권한 요청 | `Boolean` |
| `RequestMultiplePermissions` | 다중 권한 요청 | `Map<String, Boolean>` |
| `OpenDocument` | SAF 파일 선택 | `Uri?` |
| `CreateDocument` | SAF 파일 생성 | `Uri?` |
| `GetContent` | 컨텐츠 선택 | `Uri?` |

#### 커스텀 Contract

```kotlin
class PickUserContract : ActivityResultContract<Unit, User?>() {
    override fun createIntent(context: Context, input: Unit): Intent {
        return Intent(context, UserPickerActivity::class.java)
    }
    
    override fun parseResult(resultCode: Int, intent: Intent?): User? {
        if (resultCode != Activity.RESULT_OK) return null
        return intent?.getParcelableExtra("selected_user")
    }
}

// 사용
private val pickUser = registerForActivityResult(PickUserContract()) { user ->
    user?.let { selectedUser = it }
}
```

### 앱 간 데이터 전달 보안

```kotlin
// ✅ 좋은 예: 명시적 Intent + 권한 제한
val intent = Intent().apply {
    component = ComponentName("com.trusted.app", "com.trusted.app.DataActivity")
    putExtra("data", sensitiveData)
}

// ❌ 나쁜 예: 수신 Intent 데이터를 검증 없이 사용
override fun onCreate(savedInstanceState: Bundle?) {
    val data = intent.getStringExtra("url")
    // ❌ 직접 WebView에 로드 → XSS 공격 위험
    // webView.loadUrl(data!!)
    
    // ✅ 입력 검증 후 사용
    data?.let { url ->
        if (url.startsWith("https://")) {
            webView.loadUrl(url)
        }
    }
}
```

### 디버깅

```bash
# Intent 로 Activity 시작 테스트
adb shell am start -a android.intent.action.VIEW -d "https://example.com"

# 특정 앱의 Activity 시작
adb shell am start -n com.example.app/.MainActivity --es "key" "value"

# Broadcast 전송
adb shell am broadcast -a com.example.MY_ACTION

# PendingIntent 관련 정보
adb shell dumpsys activity intents
```

### 더 보기

[android-app-components-deep-dive](android-app-components-deep-dive.md), [android-deep-links](android-deep-links.md), [android-permissions-deep-dive](../05_security_privacy/android-permissions-deep-dive.md), [android-activity-lifecycle](android-activity-lifecycle.md)
