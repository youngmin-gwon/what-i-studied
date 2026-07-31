# `SideEffect` (외부 비-Compose 상태와의 동기화)
* **목적**: Compose 재구성이 성공적으로 완료될 때마다 실행할 작업을 정의합니다.
* **동작**: Compose 상태가 성공적으로 스크린에 반영된 직후에 호출되며, 재구성이 취소되면 실행되지 않습니다.
* **주요 사용처**: 외부 모니터링 도구(Google Analytics 등)에 화면 상태 기록, Compose 관리 밖의 블루투스/네이티브 인스턴스에 현재 상태 반영.

```kotlin
@Composable
fun MyScreen(userStatus: String) {
    // Compose 상태를 Compose 관리 영역 밖의 외부 시스템에 공유할 때 사용
    SideEffect {
        NativeAnalyticsTracker.logUserStatus(userStatus)
    }
    
    Text("User: $userStatus")
}
```

---
