# 대체 텍스트 제공 (Content Descriptions)
* **원칙**: 화면의 텍스트가 아닌 시각적 요소(Image, Icon)는 스크린 리더가 읽을 수 있도록 설명 텍스트를 제공해야 합니다.
* **장식용 이미지 처리**: 레이아웃 장식용이거나 화면의 텍스트 정보와 완벽히 중복되는 이미지에는 `contentDescription = null`을 명시하여 TalkBack이 해당 요소를 건너뛰고 포커스를 잡지 않도록 유도해야 합니다.

```kotlin
// Case 1: 의미를 가진 이미지 - 상세한 묘사 제공
Image(
    painter = painterResource(R.drawable.post_image),
    contentDescription = "VirtualMate 운동 가이드 화면 캡처 이미지"
)

// Case 2: 단순 데코레이션/장식용 이미지 - null 설정 (TalkBack 포커스 스킵)
Image(
    painter = painterResource(R.drawable.ic_decorator_star),
    contentDescription = null
)
```

---
