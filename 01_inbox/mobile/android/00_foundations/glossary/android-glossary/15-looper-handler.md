# Looper / Handler

상위 노트: [[android-glossary]]

**정의**: 스레드의 메시지 루프를 관리하는 메커니즘

**상세**:

안드로이드의 **메인 스레드**는 본질적으로 `Looper.loop()` 를 핑핑 도는 무한 루프입니다.

- **Looper**: 우체통 (MessageQueue) 에 편지가 오나 감시하다가, 오면 배달부 (Handler) 에게 줍니다.
- **Handler**: 편지를 보내는 역할 (sendMessage) 과 받는 역할 (handleMessage) 을 동시에 합니다.

**구조**:

```
Thread
 └─ Looper (무한 루프)
     └─ MessageQueue (작업 대기열)
         ├─ Message (UI 업데이트)
         └─ Runnable (postDelayed)
```

**예시**:

```kotlin
// 메인 스레드로 작업 보내기
Handler(Looper.getMainLooper()).post {
    textView.text = "Hello"
}
```

**관련**: [[android-performance-and-debug]]

---
