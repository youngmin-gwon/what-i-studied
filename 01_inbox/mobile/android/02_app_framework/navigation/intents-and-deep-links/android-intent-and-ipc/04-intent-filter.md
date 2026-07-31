# Intent Filter

상위 노트: [android-intent-and-ipc](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/android-intent-and-ipc.md)

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
