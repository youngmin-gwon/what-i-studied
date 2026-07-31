# 터치 대상 크기 확보 (Touch Target Sizes)
* **요구사항**: 터치하거나 클릭할 수 있는 모든 UI 요소는 최소 **48dp x 48dp** 이상의 크기를 가져야 합니다.
* **Compose 최적화**: Material Design 컴포저블(Button, IconButton, Switch 등)은 내부적으로 최소 터치 크기 요건을 자동으로 충족하도록 설계되어 있습니다. 하지만 작은 텍스트 버튼이나 커스텀 클릭 컴포저블을 직접 구현할 때는 누락되기 쉽습니다.

```kotlin
// ❌ 안 좋은 예: 아이콘 크기가 24dp여서 손의 미세 제어가 어려운 사용자는 터치하기 힘듦
Icon(
    imageVector = Icons.Default.Share,
    contentDescription = "공유",
    modifier = Modifier.clickable { onShare() }
)

//  올바른 예: IconButton 또는 minimumTouchTargetSize 확보
IconButton(onClick = onShare) {
    Icon(
        imageVector = Icons.Default.Share,
        contentDescription = "공유"
    )
}
```

---
