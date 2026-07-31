# ANR 분석

상위 노트: [android-debugging-techniques](01_inbox/mobile/android/06_testing_performance/debugging/android-debugging-techniques.md)

ANR (Application Not Responding) 은 메인 스레드가 5 초 이상 블로킹될 때 발생.

##### ANR Trace 확인

```bash
# ANR 발생 시 자동 생성
adb pull /data/anr/traces.txt

# 또는
adb bugreport bugreport.zip
```

**Trace 예시:**

```
"main" prio=5 tid=1 Sleeping
  | group="main" sCount=1 dsCount=0 flags=1 obj=0x74b38080 self=0x7f8c001200
  | sysTid=12345 nice=-10 cgrp=default sched=0/0 handle=0x7f8c456000
  | state=S schedstat=( 1234567890 987654321 123 ) utm=100 stm=50 core=2 HZ=100
  | stack=0x7ffc000000-0x7ffc002000 stackSize=8MB
  | held mutexes=
  at java.lang.Thread.sleep(Native Method)
  at com.example.app.MainActivity.loadData(MainActivity.kt:50)
  at com.example.app.MainActivity.onCreate(MainActivity.kt:30)
```

**해결:**

```kotlin
// ❌ 나쁜 예: 메인 스레드에서 네트워크
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    val data = api.getData() // ANR!
}

// ✅ 좋은 예: 코루틴 사용
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    lifecycleScope.launch {
        val data = withContext(Dispatchers.IO) {
            api.getData()
        }
        updateUI(data)
    }
}
```
