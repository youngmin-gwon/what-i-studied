---
title: task-window-launch-backstack
tags: ["android", "android/platforms"]
aliases: []
date modified: 2026-08-04 15:35:00 +09:00
date created: 2026-07-31 18:08:32 +09:00
---

## Task 와 새 창 실행은 back stack 재사용을 명시해야 한다

상위 문서: [데스크톱 윈도잉과 멀티태스킹 계약](windowing-multitasking.md)

데스크톱과 multi-window 에서 `Intent` 실행은 단순 화면 이동이 아니라 어느 task, 어느 window, 어느 기존 activity 를 재사용할지 결정하는 상태 전이다. 알림, deep link, 공유, drag-out, New Window 동작이 모두 같은 back stack 으로 합쳐지면 사용자는 다른 문서나 다른 작업으로 튕긴 것처럼 느낀다.

### Intent Launch Flags 및 `onNewIntent` 재사용 메커니즘

```kotlin
// 기존 Document Task 재사용 또는 새 Task Window 생성
fun launchDocumentTarget(context: Context, uri: Uri) {
    val intent = Intent(Intent.ACTION_VIEW, uri).apply {
        setClass(context, DocumentActivity::class.java)
        // 데스크톱 / 멀티윈도우 문서별 독립 Task 창 생성
        addFlags(Intent.FLAG_ACTIVITY_NEW_DOCUMENT)
        addFlags(Intent.FLAG_ACTIVITY_MULTIPLE_TASK)
    }
    context.startActivity(intent)
}

// SingleTop / Re-use 수신 처리
class DocumentActivity : ComponentActivity() {
    override fun onNewIntent(intent: Intent) {
        super.onNewIntent(intent)
        setIntent(intent)
        // 새 Intent 데이터 기반으로 기존 Window 내용 갱신
        loadDocumentFromUri(intent.data)
    }
}
```

### 실무 규칙

- `launchMode`, `taskAffinity`, `Intent` flags, `onNewIntent()` 처리를 작업 단위별로 문서화한다.
- 이미 열린 문서를 재사용할지, 새 window 로 열지, 기존 task 위에 쌓을지 명시한다.
- deep link 와 notification click 이 multi-instance 환경에서 어느 창을 선택하는지 테스트한다.
- 새 task 를 만드는 코드는 뒤로 가기, recents, window title, saved state 까지 함께 검증한다.
- 중복 창 생성, 잘못된 문서 표시, 예측 불가능한 back 동작은 desktop 지원에서 출시 차단 버그로 본다.

### 관측 가능한 증거 (Observable Evidence)

```bash
# 태스크 백스택 구조 및 인스턴스 ID(taskId) 덤프 디버깅
adb shell dumpsys activity activities | grep -E "Stack #|Running activities|TaskRecord"

# 최근 태스크 목록과 각 태스크의 launchFlags 관측
adb shell dumpsys activity recents | grep -E "realActivity|launchFlags"
```

### 관련 문서

- [데스크톱 멀티 인스턴스는 작업 단위와 데이터 소유권을 먼저 정해야 한다](multi-instance-task-boundaries.md)

공식 문서: [Support desktop windowing](https://developer.android.com/develop/adaptive-apps/guides/support-desktop-windowing), [Tasks and the back stack](https://developer.android.com/guide/components/activities/tasks-and-back-stack)

