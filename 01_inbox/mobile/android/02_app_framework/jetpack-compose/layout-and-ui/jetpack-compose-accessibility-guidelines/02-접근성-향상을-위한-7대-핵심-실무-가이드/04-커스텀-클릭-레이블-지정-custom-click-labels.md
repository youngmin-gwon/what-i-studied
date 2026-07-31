# 커스텀 클릭 레이블 지정 (Custom Click Labels)
* **원칙**: 일반적인 `Modifier.clickable`을 지정하면 TalkBack은 끝에 자동으로 "두 번 탭하면 활성화됩니다(Double tap to activate)"라는 안내 멘트를 붙입니다.
* **개선**: 이 버튼이 구체적으로 어떤 동작을 하는지 클릭 레이블(`onClickLabel`)을 커스텀하여 전달하면 훨씬 명확해집니다.

```kotlin
//  올바른 예: 클릭 시 작동하는 의미를 레이블로 구체화
Row(
    modifier = Modifier
        .clickable(
            onClickLabel = "글 상세 보기", // TalkBack은 "두 번 탭하면 글 상세 보기을(를) 실행합니다" 등으로 안내
            onClick = onPostClick
        )
) {
    Text("상세 정보 읽기")
}
```

---
