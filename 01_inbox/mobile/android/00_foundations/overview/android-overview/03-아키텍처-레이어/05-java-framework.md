# Java Framework

앱 개발자가 사용하는 API:

```kotlin
// Activity (화면)
class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
    }
}
```

**주요 시스템 서비스**:

- **ActivityManager**: 앱 생명주기
- **WindowManager**: 화면 관리
- **PackageManager**: 앱 설치/제거
- **LocationManager**: 위치
- **ConnectivityManager**: 네트워크

**상세**: [[android-activity-manager-and-system-services]]

---
