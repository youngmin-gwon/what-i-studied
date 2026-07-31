# 커스텀 동작 지원 (Custom Accessibility Actions)
* **원칙**: 화면의 아이템을 스와이프해서 삭제(`Swipe-to-Dismiss`)하는 등 복잡한 물리 제스처가 동반되는 인터랙션의 경우, 시각 장애를 가진 사용자는 해당 제스처를 수행하기 곤란합니다.
* **해결책**: 스와이프 등의 행동을 대체할 수 있는 접근성 커스텀 액션(`customActions`)을 제공하여 메뉴 선택만으로 동작을 완수할 수 있게 합니다.

```kotlin
Row(
    modifier = Modifier
        .fillMaxWidth()
        .semantics {
            // TalkBack 사용자에게 "사용 가능한 작업이 있습니다. 보려면 스와이프..." 형태의 알림이 가며,
            // 별도의 접근성 작업 메뉴를 통해 '삭제' 액션을 트리거할 수 있습니다.
            customActions = listOf(
                CustomAccessibilityAction(
                    label = "이 알림 삭제",
                    action = { 
                        onDismissNotification() 
                        true // 처리 성공 반환
                    }
                )
            )
        }
) {
    Text("새로운 알림이 도착했습니다.")
}
```

---
