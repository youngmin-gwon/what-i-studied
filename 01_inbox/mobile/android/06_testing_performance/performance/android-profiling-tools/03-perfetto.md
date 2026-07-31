# Perfetto

상위 노트: [[android-profiling-tools]]

시스템 전체 성능 추적.

##### 사용법

```bash
# 1. 추적 시작
adb shell perfetto \
  -c - --txt \
  -o /data/misc/perfetto-traces/trace \
  <<EOF
buffers: {
    size_kb: 63488
    fill_policy: DISCARD
}
data_sources: {
    config {
        name: "linux.ftrace"
        ftrace_config {
            ftrace_events: "sched/sched_switch"
            ftrace_events: "power/suspend_resume"
            ftrace_events: "sched/sched_wakeup"
            ftrace_events: "sched/sched_waking"
            ftrace_events: "sched/sched_process_exit"
            ftrace_events: "sched/sched_process_free"
            ftrace_events: "task/task_newtask"
            ftrace_events: "task/task_rename"
            atrace_categories: "gfx"
            atrace_categories: "view"
            atrace_categories: "webview"
            atrace_categories: "camera"
            atrace_categories: "dalvik"
            atrace_categories: "power"
        }
    }
}
duration_ms: 10000
EOF

# 2. 앱 실행 및 작업 수행

# 3. 추적 파일 가져오기
adb pull /data/misc/perfetto-traces/trace trace.perfetto-trace

# 4. 분석
# https://ui.perfetto.dev 에서 trace.perfetto-trace 열기
```

##### 코드에서 추적

```kotlin
import android.os.Trace

fun expensiveOperation() {
    Trace.beginSection("ExpensiveOperation")
    try {
        // 작업 수행
        processData()
    } finally {
        Trace.endSection()
    }
}

// Async 추적
fun asyncOperation() {
    val cookie = 1
    Trace.beginAsyncSection("AsyncOperation", cookie)
    
    lifecycleScope.launch {
        delay(1000)
        Trace.endAsyncSection("AsyncOperation", cookie)
    }
}
```
