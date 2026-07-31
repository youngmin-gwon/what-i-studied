# E2E 테스트 및 UI Automator 연동 기법

E2E 테스트 도구(UI Automator, Appium)가 Compose UI 노드의 `testTag`를 인식할 수 있도록 시스템 차원의 연동 설정이 필요합니다.

### 4-1. `testTagsAsResourceId` 활성화
앱의 최상위 스크린 컨테이너(예: `Scaffold` 또는 메인 레이아웃)에 `testTagsAsResourceId = true` 속성을 추가하면, Compose의 `testTag`가 Android 뷰 계층의 `resource-id`로 노출됩니다.

```kotlin
// app 및 feature 레이어의 화면 최상위 래퍼
Scaffold(
    modifier = Modifier.semantics {
        // Compose testTag를 Android View의 AccessibilityNodeInfo resource-id로 변환
        testTagsAsResourceId = true
    }
) { innerPadding ->
    // ... Layout Content ...
}
```

### 4-2. UI Automator에서의 타겟 탐색 예시
```kotlin
// UI Automator 테스트 클래스
val device = UiDevice.getInstance(InstrumentationRegistry.getInstrumentation())

// resource-id 형태("com.app.package:id/signIn:submitButton") 또는 서브스트링으로 검색
val submitButton = device.findObject(By.res("signIn:submitButton"))
submitButton.click()
```

---
