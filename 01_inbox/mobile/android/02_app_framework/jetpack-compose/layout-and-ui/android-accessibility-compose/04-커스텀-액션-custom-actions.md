# 커스텀 액션 (Custom Actions)

스와이프나 롱클릭 등 시각적 제스처를 접근성 서비스가 이해할 수 있도록 명시한다.

```kotlin
Modifier.semantics {
    customActions = listOf(
        CustomAccessibilityAction("삭제") {
            viewModel.deleteItem()
            true
        }
    )
}
```

>[!CAUTION] **Devil's Advocate : 테스트를 위해 접근성을 희생하지 마라**
>Compose UI 테스트에서 요소를 찾기 위해 `testTag` 를 남발하는 대신, 실제 사용자가 접근성 엔진을 통해 보는 정보인 `contentDescription` 이나 `role` 을 기반으로 테스트를 작성하라. 이는 테스트 안정성과 접근성 품질을 동시에 높이는 방법이다.
