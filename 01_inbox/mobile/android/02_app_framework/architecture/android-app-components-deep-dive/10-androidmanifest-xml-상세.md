# AndroidManifest.xml 상세

상위 노트: [[android-app-components-deep-dive]]

앱의 진입점과 컴포넌트 설정을 정의하는 핵심 파일이다.

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools">

    <application
        android:allowBackup="true"
        android:dataExtractionRules="@xml/data_extraction_rules"
        android:fullBackupContent="@xml/backup_rules"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/Theme.Android101"
        tools:targetApi="31">

        <!-- 진입점 Activity -->
        <activity
            android:name=".MainActivity"
            android:exported="true"
            android:label="@string/app_name"
            android:theme="@style/Theme.Android101">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>
</manifest>
```

**주요 속성 설명:**

- `android:exported="true"`: 외부 앱에서 호출 가능 (Android 12+ 필수)
- `ACTION_MAIN` + `CATEGORY_LAUNCHER`: 런처에서 앱 아이콘으로 표시
- `tools:targetApi`: Android Studio 빌드 도구용 힌트 (런타임 무관)
