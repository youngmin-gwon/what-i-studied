---
title: navigation3-back-stack-needs-saveable-restoration
tags: [android, android/navigation, android/navigation3]
aliases: ["Navigation 3 back stack은 저장 가능한 navigation state로 복원해야 한다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Navigation 3 back stack 은 저장 가능한 navigation state 로 복원해야 한다

상위 문서: [Navigation 3 계약](navigation3-contracts.md)

---

### 개념과 상태 복원 메커니즘 (What & How)

1. **개념 (What)**:
   - Navigation 3의 백스택(`NavBackStack<NavKey>`)은 안드로이드 OS의 프로세스 사망(Process Death)이나 화면 회전(Configuration Change) 후에도 사용자가 보고 있던 목적지 스택 상태가 그대로 유지되도록 **`rememberSaveable`** 및 **`SavedStateHandle`** 기반으로 복원 가능해야 한다는 계약이다.
2. **필요성 (Why)**:
   - 프로세스 사망 후 앱이 다시 구동되었을 때 백스택이 초기화되면 사용자는 작성 중이던 서식이나 깊은 상세 화면 맥락을 잃게 된다.

```kotlin
// rememberNavBackStack은 내부적으로 rememberSaveable을 사용하여 
// 모든 @Serializable NavKey 스택 데이터를 Bundle로 자동 저장 및 복원한다.
val backStack = rememberNavBackStack(initialKey = HomeKey)
```

---

### 관련 상위 및 연관 노트

- 상위 계약: [Navigation 3 계약](navigation3-contracts.md)
- 연관 계약: [Route key는 안정적인 직렬화 식별자다](route-key-should-be-stable-and-serializable.md)
