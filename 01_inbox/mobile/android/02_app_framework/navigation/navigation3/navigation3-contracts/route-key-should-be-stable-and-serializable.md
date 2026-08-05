---
title: route-key-should-be-stable-and-serializable
tags: [android, android/navigation, android/navigation3]
aliases: ["Route key는 안정적인 직렬화 식별자다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Route key 는 안정적인 직렬화 식별자다

상위 문서: [Navigation 3 계약](navigation3-contracts.md)

---

### 개념과 설계 원칙 (What & Why)

1. **개념 (What)**:
   - Navigation 3의 라우트 키(`NavKey`)는 프로세스 재시작 시 Bundle로 보존될 수 있도록 반드시 **`@Serializable` (Kotlinx Serialization)** 어노테이션이 지정된 불변 객체/데이터 클래스이어야 한다.
2. **설계 원칙 (Why & Rule)**:
   - **최소 식별자만 포함**: 키 내부에는 화면 복원에 필요한 최소 식별자(예: `id: String`)만 포함하며, 거대한 도메인 데이터 객체, Repository 인스턴스, 람다 콜백을 키에 포함해서는 안 된다.

```kotlin
// 올바른 설계 예시
@Serializable
data class UserProfileKey(val userId: String) : NavKey

// 잘못된 설계 예시 (도메인 객체나 람다 포함 금지)
// data class BadKey(val user: UserDomainModel, val onClick: () -> Unit) : NavKey
```

---

### 관련 상위 및 연관 노트

- 상위 계약: [Navigation 3 계약](navigation3-contracts.md)
- 연관 계약: [Navigation 3 back stack은 저장 가능한 navigation state로 복원해야 한다](navigation3-back-stack-needs-saveable-restoration.md)
