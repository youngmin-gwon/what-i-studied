# Foreground Services (Android 14+ 제한)

사용자가 인지해야 하는 즉각적이고 지속적인 작업(음악 재생, 운동 추적)에 사용한다.

>[!CAUTION] **Devil's Advocate : Foreground Service 남용 금지**
>Android 14 부터 `foregroundServiceType` 선언이 강제되었고, 구글 플레이 정책은 "사용자가 인지할 수 없는 백그라운드 작업은 무조건 WorkManager 를 쓰라"고 강요한다. 타입을 속여서 승인받으려다가는 앱이 삭제될 수 있다.

##### Android 14+ 구현 규칙
1. `AndroidManifest.xml` 에 특정 타입 권한과 서비스 타입 선언
2. `startForeground()` 호출 시 `ForegroundInfo` 전달

```xml
<!-- AndroidManifest.xml -->
<uses-permission android:name="android.permission.FOREGROUND_SERVICE" />
<uses-permission android:name="android.permission.FOREGROUND_SERVICE_DATA_SYNC" />

<service
    android:name=".DataSyncService"
    android:foregroundServiceType="dataSync" />
```
