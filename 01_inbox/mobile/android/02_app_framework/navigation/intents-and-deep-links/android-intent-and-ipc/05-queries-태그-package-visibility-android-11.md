# `<queries>` 태그 (Package Visibility, Android 11+)

상위 노트: [[android-intent-and-ipc]]

Android 11 부터 앱이 다른 앱의 존재를 확인하려면 매니페스트에 명시적으로 선언해야 한다.

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

>[!WARNING] **`<queries>` 없이 `resolveActivity()` 호출하면 null 반환**
>Android 11+ 에서는 `<queries>` 에 선언하지 않은 앱은 보이지 않는다. `QUERY_ALL_PACKAGES` 권한은 구글 플레이 정책상 특수 앱(런처, 보안 앱)만 승인된다.
