# UI 테스트 타겟팅: `testTag` vs `Semantics` (i18n 대응)

Compose UI 테스트를 작성할 때 노드를 찾는 방식은 **글로벌 다국어(i18n) 지원 및 유지보수성** 측면에서 명확한 역할 분담이 필요합니다.

### 2-1. `testTag` vs `Semantics` 비교 및 모범 가이드

| 구분 | `Modifier.testTag` | `Semantics` (`onNodeWithText`, `contentDescription`) |
| :--- | :--- | :--- |
| **주요 용도** | 테스트 전용 고유 식별자 지정 | 접근성(TalkBack) 및 화면 가시 텍스트 검증 |
| **다국어(i18n) 영향** | **영향 없음** (언어 변경 시에도 태그는 고정) | **높음** (기기 언어가 바뀌거나 문구 수정 시 테스트 실패) |
| **사용 시점** | **상호작용 타겟** (버튼, 입력 필드, 아이콘 클릭) | **결과 검증 (Assertion)** (에러 문구, 타이틀 노출 여부) |

### 2-2. i18n 환경에서의 올바른 테스트 코드 패턴
상호작용할 요소(입력창, 버튼)는 `testTag`로 고정하여 언어 변경 및 텍스트 수정에 테스트 코드가 깨지지 않도록 보호하고, 결과 검증 시에는 `R.string` 리소스를 활용합니다.

```kotlin
@Test
fun signIn_withInvalidPassword_showsErrorMessage() {
    // 1. 클릭 및 입력 타겟: i18n에 영향받지 않도록 testTag 사용
    composeTestRule
        .onNodeWithTag("signIn:idInput")
        .performTextInput("user01")

    composeTestRule
        .onNodeWithTag("signIn:passwordInput")
        .performTextInput("wrong_password")

    composeTestRule
        .onNodeWithTag("signIn:submitButton")
        .performClick()

    // 2. 결과 검증 (Assertion): R.string 리소스를 활용하여 다국어 텍스트 검증
    val context = InstrumentationRegistry.getInstrumentation().targetContext
    val expectedErrorText = context.getString(R.string.error_invalid_password)

    composeTestRule
        .onNodeWithText(expectedErrorText)
        .assertIsDisplayed()
}
```

---
