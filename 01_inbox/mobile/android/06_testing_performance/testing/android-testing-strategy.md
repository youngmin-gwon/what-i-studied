# Jetpack Compose & Android 종합 테스트 전략 가이드

이 문서는 Android 앱의 안정성, 품질 관리, 다국어(i18n) 호환성 및 지속적인 검증을 위해 **Jetpack Compose UI 테스트**, **`testTag` 네이밍 컨벤션**, **E2E(End-to-End) 자동화 테스트** 및 **성능 벤치마킹 전략**을 정리합니다.

본 문서는 Google의 [Testing in Jetpack Compose 가이드라인](https://developer.android.com/develop/ui/compose/testing) 및 [Now in Android](https://github.com/android/nowinandroid) 오픈소스 프로젝트의 최신 실무 테스트 방식을 바탕으로 작성되었습니다.

---

## 1. 테스트 피라미드 및 레이어별 검증 전략

Android 앱의 테스트 전략은 실행 속도, 피드백 주기 및 안정성 간의 균형을 맞추기 위해 3개의 레이어로 나뉩니다.

```
       / \
      /   \     [1] End-to-End (E2E) & Macrobenchmark (10%)
     / E2E \    - 실제 디바이스 / UI Automator / MockWebServer / 성능 측정
    /-------\
   / Compose \  [2] Compose UI Component / Integration Test (40%)
  / Component \ - ComposeTestRule / Robolectric / ViewModel & UI 상태 결합 검증
 /-------------\
/   Unit Test   \ [3] Unit Test (50%)
/-----------------\ - ViewModel, UseCase, Repository, Domain 로직 단위 검증
```

### 1-1. Unit Test (단위 테스트) - 50%
* **대상**: ViewModel, UseCase, Repository, 데이터 매퍼 및 순수 Kotlin 비즈니스 로직.
* **특징**: Android 위젯이나 UI 종속성이 없으며, JVM 상에서 밀리초(ms) 단위로 빠르게 실행됩니다.
* **주요 도구**: JUnit5, MockK, Coroutines Test (`StandardTestDispatcher`, `runTest`).
* **Reducer가 있는 화면**: Reducer는 Android, Coroutine, Flow 없이 `oldState + action -> newState`만 검증하는 순수 JVM 테스트로 작성합니다.

### 1-2. Compose UI Component & Integration Test (컴포넌트/통합 테스트) - 40%
* **대상**: 개별 Composable 화면, 폼 입력, 다국어 문구 노출 및 UI State(`UiState`) 변화 반응.
* **특징**: `ComposeTestRule`을 사용하며, **Robolectric**을 결합하여 에뮬레이터 없이 JVM 환경에서 빠른 CI 검증을 수행합니다.
* **주요 도구**: `createComposeRule()`, `createAndroidComposeRule()`, Robolectric.

### 1-3. End-to-End (E2E) & Macrobenchmark Test (통합 자동화 테스트) - 10%
* **대상**: 전체 유저 여정(로그인 ➔ 대시보드 ➔ 측정 ➔ 설정), 권한 팝업, 알림창, 런처 구동 속도 및 프레임 드랍(Jank).
* **특징**: 실제 물리 디바이스 또는 에뮬레이터에서 백엔드 응답을 가상화(`MockWebServer`)하여 완결된 플로우를 검증합니다.
* **주요 도구**: UI Automator, Kaspresso, Jetpack Macrobenchmark (`:baselineprofile` 모듈).

---

## 2. UI 테스트 타겟팅: `testTag` vs `Semantics` (i18n 대응)

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

## 3. `testTag` 네이밍 컨벤션 표준

Now in Android(NiA) 및 공식 가이드라인에 맞춰 UI 트리의 고유성과 자동화 도구 파싱을 고려한 네임스페이스 규칙을 준수합니다.

### 3-1. 표준 명명 구조

$$\text{Format: } \texttt{\{feature-or-screen\}:\{component\}[:\{sub-element-or-id\}]}$$

- **단일 화면/컨테이너**: `signIn:screen`, `dashboard:root`
- **입력 필드 및 버튼**: `signIn:idInput`, `signIn:passwordInput`, `signIn:submitButton`
- **시각적 아이콘/토글**: `signIn:passwordToggle` (텍스트가 없는 아이콘 버튼)
- **동적 리스트(LazyColumn/LazyGrid) 아이템**: `dashboard:item:${item.id}`
- **로딩 및 상태 요소**: `signIn:loadingProgress`

### 3-2. `testTag` 선별적 부여 기준 (코드 오염 방지)

모든 UI 요소에 무분별하게 `testTag`를 부여하면 코드 오염(Pollution)이 발생합니다. 다음 기준을 따릅니다.

1. **태그 필수 부여 대상**:
   - 텍스트가 없는 아이콘 버튼 (비밀번호 눈 모양 토글, 닫기 X 버튼 등)
   - 동적 목록의 개별 셀 (`LazyColumn` 아이템)
   - 입력 필드 및 주요 상호작용 액션 버튼 (i18n 보호 목적)
   - Macrobenchmark / UI Automator로 탐색해야 하는 주요 스크린 루트
2. **태그 생략 대상**:
   - 화면에 고정 노출되는 단순 타이틀, 설명 문구 (`onNodeWithText`로 검증 가능)

---

## 4. E2E 테스트 및 UI Automator 연동 기법

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

## 5. 실무 적용 체크리스트

- [ ] **네이밍 규칙 준수**: 새로 작성하는 Composable의 `testTag`는 `{feature}:{component}` 포맷을 준수하는가?
- [ ] **i18n 영향 분리**: 입력 및 클릭 액션 타겟에는 `testTag`를 적용하고, 텍스트 검증 시 `onNodeWithText(R.string...)`을 사용하였는가?
- [ ] **Robolectric 통합**: UI 컴포넌트 테스트가 로컬 JVM(Robolectric) 위에서 빠르게 실행되도록 구성되었는가?
- [ ] **`testTagsAsResourceId` 설정**: E2E 및 Macrobenchmark 측정을 위한 최상위 `semantics` 설정이 포함되어 있는가?
