---
title: android-deep-links
tags: [android, android/deep-link, android/app-link, android/navigation]
aliases: [Deep Links, App Links, Dynamic App Links, Universal Links]
date modified: 2026-04-04 00:11:00 +09:00
date created: 2026-04-04 00:11:00 +09:00
---

## Android Deep Links & App Links

딥링크는 URL 을 통해 앱 내 특정 화면으로 직접 진입하는 메커니즘이다. 검색 결과, 푸시 알림, 마케팅 링크, 앱 간 연동의 핵심이다.

> [!NOTE] **iOS 비교: Deep Links vs Universal Links**
> Android 의 App Links 는 iOS 의 **Universal Links** 와 동일한 개념이다.
> - **iOS**: Associated Domains Entitlement + `apple-app-site-association` (AASA) 파일
> - **Android**: Intent Filter + `assetlinks.json` 파일
> 두 플랫폼 모두 **HTTPS 도메인 소유 검증**을 통해 앱과 웹사이트의 신뢰 관계를 증명한다.
> iOS 의 URL Scheme (`myapp://`) 은 Android 의 Custom Scheme Deep Link 와 동일한 레거시 패턴이며, 두 플랫폼 모두 검증된 HTTPS 기반 방식을 권장한다.

### 세 가지 딥링크 종류

| 종류 | URL 패턴 | 검증 | 앱 선택 다이얼로그 |
|------|----------|------|-------------------|
| **Custom Scheme** | `myapp://detail/123` | ❌ 없음 | 다른 앱이 가로챌 수 있음 |
| **App Links** | `https://example.com/detail/123` | ✅ 도메인 검증 | ❌ 바로 앱 열림 |
| **Dynamic App Links** | 서버 설정 변경 가능 | ✅ 도메인 검증 | ❌ 바로 앱 열림 |

> [!CAUTION] **Devil's Advocate : Custom Scheme 은 보안 구멍**
> `myapp://` 같은 커스텀 스킴은 **누구나 등록 가능**하여 악성 앱이 동일한 스킴을 선언해 데이터를 가로챌 수 있다.
> 프로덕션에서는 반드시 **Android App Links** (HTTPS 검증)를 사용해야 한다.

### 1. Custom Scheme Deep Link (레거시)

```xml
<!-- AndroidManifest.xml -->
<activity android:name=".DetailActivity"
    android:exported="true">
    <intent-filter>
        <action android:name="android.intent.action.VIEW" />
        <category android:name="android.intent.category.DEFAULT" />
        <category android:name="android.intent.category.BROWSABLE" />
        <data
            android:scheme="myapp"
            android:host="detail"
            android:pathPrefix="/" />
    </intent-filter>
</activity>
```

```kotlin
// 수신 처리
class DetailActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        
        intent?.data?.let { uri ->
            // myapp://detail/123 → pathSegments[0] = "123"
            val itemId = uri.lastPathSegment
            loadItem(itemId)
        }
    }
}
```

### 2. Android App Links (권장)

#### Step 1: Intent Filter 선언

```xml
<activity android:name=".MainActivity"
    android:exported="true">
    <intent-filter android:autoVerify="true">  <!-- 자동 검증 -->
        <action android:name="android.intent.action.VIEW" />
        <category android:name="android.intent.category.DEFAULT" />
        <category android:name="android.intent.category.BROWSABLE" />
        <data
            android:scheme="https"
            android:host="www.example.com"
            android:pathPrefix="/product" />
    </intent-filter>
</activity>
```

#### Step 2: Digital Asset Links 파일 호스팅

`https://www.example.com/.well-known/assetlinks.json` 에 배포:

```json
[{
    "relation": ["delegate_permission/common.handle_all_urls"],
    "target": {
        "namespace": "android_app",
        "package_name": "com.example.app",
        "sha256_cert_fingerprints": [
            "14:6D:E9:83:C5:73:06:50:D8:EE:B9:95:2F:34:FC:64:16:A0:83:..."
        ]
    }
}]
```

```bash
# 인증서 SHA-256 지문 확인
keytool -list -v -keystore release.keystore | grep SHA256

# 검증 테스트 (Android 12+)
adb shell pm verify-app-links --re-verify com.example.app
adb shell pm get-app-links com.example.app
```

#### Step 3: Compose Navigation 딥링크 처리

```kotlin
@Serializable object Home
@Serializable data class Product(val id: String)
@Serializable data class Profile(val userId: String)

@Composable
fun AppNavigation() {
    val navController = rememberNavController()
    
    NavHost(navController = navController, startDestination = Home) {
        composable<Home> {
            HomeScreen(onProductClick = { id ->
                navController.navigate(Product(id))
            })
        }
        
        composable<Product>(
            deepLinks = listOf(
                navDeepLink<Product>(
                    basePath = "https://www.example.com/product"
                )
            )
        ) { backStackEntry ->
            val product = backStackEntry.toRoute<Product>()
            ProductScreen(productId = product.id)
        }
        
        composable<Profile>(
            deepLinks = listOf(
                navDeepLink<Profile>(
                    basePath = "https://www.example.com/user"
                )
            )
        ) { backStackEntry ->
            val profile = backStackEntry.toRoute<Profile>()
            ProfileScreen(userId = profile.userId)
        }
    }
}
```

### 3. Dynamic App Links (Android 15+)

서버 측에서 딥링크 동작을 **앱 업데이트 없이** 변경할 수 있다.

- URL 매칭 규칙, 쿼리 파라미터, 제외 패턴을 `assetlinks.json` 에서 동적 구성
- A/B 테스트, 캠페인별 라우팅에 유용

### 딥링크에서의 상태 복원

```kotlin
@Composable
fun ProductScreen(productId: String, viewModel: ProductViewModel = hiltViewModel()) {
    // 딥링크 진입 시에도 ViewModel 이 정상 초기화됨
    LaunchedEffect(productId) {
        viewModel.loadProduct(productId)
    }
    
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()
    
    when (uiState) {
        is UiState.Loading -> LoadingIndicator()
        is UiState.Success -> ProductContent((uiState as UiState.Success).product)
        is UiState.Error -> {
            // 딥링크로 진입했으나 상품이 없는 경우 → 홈으로 리다이렉트
            ErrorWithRedirect("상품을 찾을 수 없습니다")
        }
    }
}
```

### 알림(Notification)에서의 딥링크

```kotlin
fun createDeepLinkNotification(context: Context, productId: String) {
    val deepLinkIntent = Intent(
        Intent.ACTION_VIEW,
        Uri.parse("https://www.example.com/product/$productId"),
        context,
        MainActivity::class.java
    )
    
    val pendingIntent = TaskStackBuilder.create(context).run {
        addNextIntentWithParentStack(deepLinkIntent)
        getPendingIntent(0, PendingIntent.FLAG_IMMUTABLE or PendingIntent.FLAG_UPDATE_CURRENT)
    }
    
    val notification = NotificationCompat.Builder(context, CHANNEL_ID)
        .setContentTitle("새 상품 알림")
        .setContentText("관심 상품이 할인 중입니다")
        .setContentIntent(pendingIntent)
        .setAutoCancel(true)
        .build()
    
    NotificationManagerCompat.from(context).notify(NOTIFICATION_ID, notification)
}
```

### 테스트 & 디버깅

```bash
# 딥링크 테스트
adb shell am start -a android.intent.action.VIEW \
    -d "https://www.example.com/product/abc123" \
    com.example.app

# Custom Scheme 테스트
adb shell am start -a android.intent.action.VIEW \
    -d "myapp://detail/123"

# App Links 검증 상태 확인
adb shell pm get-app-links com.example.app

# 도메인 검증 강제 재실행
adb shell pm verify-app-links --re-verify com.example.app

# Intent Filter 매칭 확인
adb shell dumpsys package com.example.app | grep -A5 "intent-filter"
```

### 더 보기

[android-intent-and-ipc](android-intent-and-ipc.md), [android-compose-internals](android-compose-internals.md), [android-app-components-deep-dive](android-app-components-deep-dive.md), [android-activity-lifecycle](android-activity-lifecycle.md)
