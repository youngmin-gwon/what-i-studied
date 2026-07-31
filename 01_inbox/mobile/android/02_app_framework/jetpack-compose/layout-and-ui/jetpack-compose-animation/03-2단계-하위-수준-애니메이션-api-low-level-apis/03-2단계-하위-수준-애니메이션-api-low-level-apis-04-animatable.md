# Animatable

코루틴 범위를 통해 **애니메이션을 정밀하게 제어하거나 명령을 즉시 중단(SnapTo), 취소**해야 하는 가장 저수준의 애니메이션 상태 홀더입니다. 물리 기반 터치 스와이프
제스처 등에 적합합니다.

```kotlin
val colorAnim = remember { Animatable(Color.Gray) }

// 제스처 또는 특정 비동기 트리거 시 코루틴 내에서 실행
LaunchedEffect(isSuccess) {
    if (isSuccess) {
        // 부드럽게 Green으로 변환
        colorAnim.animateTo(Color.Green, animationSpec = spring())
    } else {
        // 즉시 Red로 값 스냅
        colorAnim.snapTo(Color.Red)
    }
}
```

---
