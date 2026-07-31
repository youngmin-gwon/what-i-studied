# 전통적인(Multi-Activity) 매니페스트 기본 구조

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.myapp">

    <!-- 권한 요청서 -->
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.CAMERA" />

    <application
        android:label="나의 멋진 식당 앱"
        android:theme="@style/Theme.MyApp">

        <!-- 런처(첫 화면) 액티비티 -->
        <activity android:name=".MainActivity" android:exported="true">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>

        <!-- 딥 링크 전용 액티비티 -->
        <activity android:name=".RestaurantActivity" android:exported="true">
            <intent-filter android:autoVerify="true">
                <action android:name="android.intent.action.VIEW" />
                <category android:name="android.intent.category.DEFAULT" />
                <category android:name="android.intent.category.BROWSABLE" />
                <data android:scheme="https"
                      android:host="example.com"
                      android:pathPrefix="/restaurants" />
            </intent-filter>
        </activity>

    </application>
</manifest>
```

---
