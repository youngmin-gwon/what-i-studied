# Logcat

상위 노트: [[android-debugging-techniques]]

기본 로깅 도구.

```kotlin
import android.util.Log

class MyClass {
    companion object {
        private const val TAG = "MyClass"
    }
    
    fun doSomething() {
        Log.v(TAG, "Verbose message") // 상세 정보
        Log.d(TAG, "Debug message") // 디버그 정보
        Log.i(TAG, "Info message") // 일반 정보
        Log.w(TAG, "Warning message") // 경고
        Log.e(TAG, "Error message") // 에러
        
        // 예외와 함께
        try {
            riskyOperation()
        } catch (e: Exception) {
            Log.e(TAG, "Operation failed", e)
        }
    }
}
```

```bash
# Logcat 필터링
adb logcat TAG:D *:S # TAG 의 DEBUG 이상만 표시

# 패키지별 필터
adb logcat --pid=$(adb shell pidof -s com.example.app)

# 시간 포함
adb logcat -v time

# 파일로 저장
adb logcat -f /sdcard/logcat.txt

# 버퍼 클리어
adb logcat -c
```
