# Compose UI 테스트는 testTag와 semantics를 분리한다

상위 문서: [Android 성능, 품질, 빌드 최적화 지도](01_inbox/mobile/android/06_testing_performance/performance/android-performance-quality-and-build-optimization.md)
관련 지도: [테스트 품질 계약](01_inbox/mobile/android/06_testing_performance/testing/testing-quality-contracts/testing-quality-contracts.md)

Compose 테스트의 탐색 방식은 테스트 안정성과 접근성 품질을 함께 결정한다.
`testTag`는 테스트가 사용할 안정적인 식별자다.
`semantics`는 사용자와 보조 기술이 이해할 UI의 의미다.
둘은 대체 관계가 아니라 서로 다른 계약을 표현한다.

## testTag를 쓸 때

텍스트가 없는 아이콘 버튼은 testTag가 유용하다.
동적 목록의 특정 아이템, 입력 필드, 중요한 액션도 testTag 대상이다.
태그는 화면 또는 feature 이름으로 namespace를 만든다.
예시는 `signIn:passwordInput`, `dashboard:item:42`처럼 작성한다.
태그는 사용자에게 노출되는 문구와 분리해 다국어 변경에 강하게 만든다.
모든 노드에 태그를 붙이면 구현 세부사항이 테스트 계약이 된다.
따라서 상호작용과 동적 식별에 필요한 노드만 태그를 부여한다.

## semantics를 쓸 때

버튼 역할, 선택 상태, 비활성 상태, content description은 semantics 계약이다.
TalkBack이 이해해야 하는 의미는 테스트에서도 검증해야 한다.
화면에 표시되는 오류 문구와 제목은 semantics 또는 텍스트 assertion으로 확인한다.
번역 문자열을 직접 하드코딩하지 말고 현재 로케일의 리소스에서 기대값을 만든다.
문구 변경이 의도된 경우 테스트가 함께 변경되어야 한다.
반대로 단순히 클릭할 버튼의 한국어 문구를 selector로 쓰면 i18n에 취약하다.

## 예시

```kotlin
composeTestRule
    .onNodeWithTag("signIn:submitButton")
    .performClick()

composeTestRule
    .onNode(hasRole(Role.Button) and isEnabled())
    .assertExists()
```

`onNodeWithText`는 표시 문구가 결과의 핵심일 때 사용한다.
`contentDescription`은 장식 이미지보다 의미 있는 아이콘에 제공한다.
테스트만을 위해 접근성 정보를 왜곡하지 않는다.

## E2E 연동

UI Automator가 Compose 태그를 resource-id로 찾아야 한다면 상위 semantics에
`testTagsAsResourceId = true`를 설정하는 방식을 검토한다.
이 설정은 Compose 내부 테스트와 시스템 수준 테스트의 경계를 연결한다.
연동을 켰다고 해서 모든 내부 노드를 외부 자동화에 공개할 필요는 없다.

공식 참고: [Compose 테스트에서 semantics](https://developer.android.com/develop/ui/compose/testing/semantics)
공식 참고: [Compose 테스트 API](https://developer.android.com/develop/ui/compose/testing/apis)
