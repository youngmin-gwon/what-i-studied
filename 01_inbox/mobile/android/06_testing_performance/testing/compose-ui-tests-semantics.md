---
title: compose-ui-tests-semantics
tags: ["android", "android/testing-performance"]
aliases: ["Compose UI 테스트는 testTag 와 semantics 를 분리한다"]
date created: 2026-07-31 17:32:53 +09:00
date modified: 2026-08-06 14:48:27 +09:00
---

## Compose UI 테스트는 testTag 와 semantics 를 분리한다

상위 문서: [Android 성능, 품질, 빌드 최적화 지도](../android-performance-testing-map.md)
관련 지도: [테스트 품질 계약](testing-quality.md)

Compose UI 테스트는 비주얼 레이아웃 트리가 아닌 접근성 및 의미 기반의 Semantics Tree를 기반으로 탐색(Matcher) 및 조작(Action)을 수행하며, 다국어/디자인 변경에 둔감하도록 엔지니어링 전용 `Modifier.testTag()`와 사용자 보조 기술용 `Semantics`를 분리 지정해야 한다.

### 1. Compose Semantics Tree 및 Selector 메커니즘

- **Layout Node Tree vs Semantics Tree**:
  - Compose 렌더링 엔진은 화면 레이아웃 트리를 그린 후, 조작 및 접근성을 위해 병합된 `SemanticsNode` 트리를 별도로 파생시킨다.
- **Merged vs Unmerged Tree**:
  - `Button` 내부의 `Text` composable은 기본적으로 상위 Button 노드로 병합(Merged)된다.
  - 클릭 가능 영역 내부의 개별 Text 노드를 탐색하려면 `useUnmergedTree = true` 플래그를 명시한다.
- **`Modifier.testTag()`**:
  - 다국어 변경, 레이아웃 리팩터링에도 변함없는 테스트 안정적 고유 식별자. `testTagsAsResourceId = true` 설정 시 UI Automator resource-id로 자동 노출.
- **`SemanticsProperties`**:
  - `Role.Button`, `ContentDescription`, `StateDescription`, `Text` 등 보조 기술(TalkBack) 및 엑세서빌리티 검증용 계약.

### 2. Layout Node Tree vs Semantics Tree 병합 구조

```mermaid
graph TD
    subgraph Layout Node Tree
        RootLayout[Box] --> ButtonLayout[Surface]
        ButtonLayout --> TextLayout[Text: 'Submit']
        ButtonLayout --> IconLayout[Icon]
    end

    subgraph Semantics Tree (Merged)
        RootSemantics[SemanticsNode: Box] --> ButtonSemantics["SemanticsNode: Button<br/>Role: Button<br/>Text: 'Submit'<br/>TestTag: 'login:submit'"]
    end

    ButtonLayout -. Merged into .-> ButtonSemantics
    TextLayout -. Merged into .-> ButtonSemantics
```

### 3. ComposeTestRule 및 Semantics Matcher Kotlin 코드 구체 예시

```kotlin
import androidx.compose.ui.semantics.Role
import androidx.compose.ui.test.*
import androidx.compose.ui.test.junit4.createComposeRule
import org.junit.Rule
import org.junit.Test

class LoginScreenTest {

    @get:Rule
    val composeTestRule = createComposeRule()

    @Test
    fun loginButton_disabled_whenPasswordEmpty() {
        composeTestRule.setContent {
            LoginScreen(
                uiState = LoginUiState(username = "user@test.com", password = "")
            )
        }

        // 1. testTag를 이용한 입력창 지정 및 텍스트 작성
        composeTestRule
            .onNodeWithTag("login:usernameInput")
            .assertIsDisplayed()

        // 2. Semantics Role & Enabled 상태 assertion (접근성 및 버튼 상태 검증)
        composeTestRule
            .onNode(
                hasTestTag("login:submitButton") and 
                hasRole(Role.Button)
            )
            .assertIsNotEnabled()
            
        // 3. ToggleableState (Checkbox, Switch) assertion
        composeTestRule
            .onNodeWithTag("login:rememberMeCheckbox")
            .assertIsOff()
    }

    @Test
    fun printSemanticsTreeDump() {
        composeTestRule.setContent { LoginScreen(uiState = LoginUiState()) }
        
        // 전체 시맨틱 트리를 로그캣으로 프린트 덤프
        composeTestRule.onRoot().printToLog("COMPOSE_TREE")
    }
}
```

### 4. 관측 가능한 실행 증거 (Observable Evidence)

#### `printToLog()` 시맨틱 트리 Logcat 덤프 출력

```text
D/COMPOSE_TREE: printToLog:
    Printing with condition:Everything
    Node #1 at (l=0, t=0, r=1080, b=2400)px
     |-Node #2 at (l=48, t=120, r=1032, b=280)px
     |  Tag: 'login:usernameInput'
     |  Text: [user@test.com]
     |  Actions: [SetText, RequestFocus]
     |-Node #3 at (l=48, t=320, r=1032, b=480)px
     |  Tag: 'login:submitButton'
     |  Role: 'Button'
     |  Disabled: []
     |  Actions: [OnClick]
```

### 5. Compose 테스트 선택자 작성 원칙

- **문구 기반 Selector 지양**: UI 텍스트(예: `"로그인하기"`)로 버튼을 클릭하는 셀렉터는 i18n 번역 파일 수정만으로 테스트가 깨지므로 `testTag`를 사용한다.
- **의미 검증엔 Semantics 사용**: 버튼의 비활성화 상태는 `assertIsNotEnabled()`로 검증한다. 체크박스·스위치처럼 `ToggleableState`를 노출하는 노드는 `assertIsOn()`/`assertIsOff()`를 사용한다. `assertIsSelected()`는 탭·라디오 항목처럼 `Selected` semantics를 노출하는 selectable 노드용이며 체크 상태 assertion이 아니다.

### 공식 문서

- https://developer.android.com/reference/kotlin/androidx/compose/ui/test/package-summary

검증일: 2026-08-06. Compose UI test API의 toggleable assertion과 selectable assertion을 구분했다.
