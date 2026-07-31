# Android App Links (권장)

##### Step 1: Intent Filter 선언

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

##### Step 2: Digital Asset Links 파일 호스팅

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

##### Step 3: Compose Navigation 딥링크 처리

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
