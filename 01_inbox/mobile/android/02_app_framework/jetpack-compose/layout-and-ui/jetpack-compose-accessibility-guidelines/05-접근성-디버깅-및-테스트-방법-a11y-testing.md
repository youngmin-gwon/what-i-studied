# 접근성 디버깅 및 테스트 방법 (a11y Testing)

상위 노트: [jetpack-compose-accessibility-guidelines](01_inbox/mobile/android/02_app_framework/jetpack-compose/layout-and-ui/jetpack-compose-accessibility-guidelines.md)

1. **TalkBack 활성화 후 직접 테스트**:
   * Android 설정 -> 접근성 -> TalkBack을 켭니다.
   * 손가락 제스처 및 볼륨 버튼 등을 통해 UI 포커스가 논리적인 순서로 이동하는지 확인합니다.
2. **접근성 검사기 (Accessibility Scanner) 사용**:
   * Google Play Store에서 `Accessibility Scanner` 앱을 다운로드하여 켭니다.
   * 대상 앱 화면을 캡처하면 터치 타깃 크기 부족, 텍스트 대비(Contrast) 불충분, 대체 텍스트 누락 지점을 화면에 사각형 박스로 하이라이팅하여 진단해 줍니다.
3. **Android Studio Layout Inspector**:
   * Layout Inspector의 `Semantics Tre` 뷰를 이용하면, 렌더링된 컴포저블 트리가 겉보기 UI가 아닌 접근성 시스템에 전달하는 Semantics 속성 구조를 시각적으로 디버깅할 수 있습니다.
4. **UI 테스트 코드에서 자동화된 접근성 검사 (Automated Accessibility Checks)**:
   * **원칙**: Compose UI 테스트 코드가 동작하는 과정에서 접근성 규칙 위반을 자동으로 잡아내어 테스트를 실패시킬 수 있습니다.
   * **설정 및 사용**:
     * `AndroidComposeTestRule` 인스턴스에 `enableAccessibilityChecks()`를 설정합니다. (Accessibility Test Framework 연동)
     * 이 검사는 클릭(`performClick`) 등 사용자의 물리 제스처가 동반되는 노드가 수행될 때 해당 화면의 대비 비율, 터치 크기, 대체 텍스트 누락 등을 자동으로 감사합니다.
   * **예제 코드**:
     ```kotlin
     @Rule
     @JvmField
     val composeTestRule = createAndroidComposeRule<MainActivity>()

     @Before
     fun setUp() {
         // 테스트 실행 중 자동 접근성 검사 활성화
         composeTestRule.enableAccessibilityChecks()
     }

     @Test
     fun sampleTest() {
         // 노드 상호작용 발생 시 자동으로 접근성 유효성을 검사하여 위반 시 실패처리
         composeTestRule.onNodeWithContentDescription("공유").performClick()
     }
     ```
