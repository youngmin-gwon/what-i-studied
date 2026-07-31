# Single Activity Architecture의 매니페스트 구조

현대 Jetpack Compose의 대세는 **단 하나의 Activity만 두고**, 화면 전환을 모두 Compose 코드(Navigation 라이브러리)로 처리하는 **Single Activity Architecture (SAA)** 입니다.

```xml
<application ...>
    <activity android:name=".MainActivity" android:exported="true">
        <!-- 1. 런처 (앱 아이콘 진입) -->
        <intent-filter>
            <action android:name="android.intent.action.MAIN" />
            <category android:name="android.intent.category.LAUNCHER" />
        </intent-filter>

        <!-- 2. 딥 링크 (모든 웹 링크를 하나의 Activity에서 수신) -->
        <intent-filter android:autoVerify="true">
            <action android:name="android.intent.action.VIEW" />
            <category android:name="android.intent.category.DEFAULT" />
            <category android:name="android.intent.category.BROWSABLE" />
            <data android:scheme="https" android:host="example.com" />
            <data android:pathPrefix="/restaurants" />
            <data android:pathPrefix="/products" />
        </intent-filter>
    </activity>
    </activity>
</application>
```
