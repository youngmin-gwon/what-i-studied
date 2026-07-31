# 📊 플랫폼별 주요 개념 매핑

| 특징 | Android (Compose) | iOS (SwiftUI) |
| :--- | :--- | :--- |
| **스크린 리더** | TalkBack | VoiceOver |
| **의미 노드** | Semantics Node | Accessibility Element |
| **요소 병합** | `mergeDescendants = true` | `.accessibilityElement(children: .combine)` |
| **역할 정의** | `Role` | `AccessibilityTrait` |
