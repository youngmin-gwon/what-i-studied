---
title: notification-deep-link-needs-explicit-task-and-back-stack-policy
tags: [android, android/navigation, android/deep-links, notification]
aliases: ["Notification deep link는 명시적 task와 back stack 정책이 필요하다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Notification deep link 는 명시적 task 와 back stack 정책이 필요하다

상위 문서: [Deep Link 계약](deep-link-contracts.md)

관련 계약: [PendingIntent는 위임된 미래 intent 토큰이다](../intent-manifest-contracts/pendingintent-is-delegated-future-intent-token.md)

---

### 개념과 필요성 (What & Why)

1. **개념 (What)**:
   - 푸시 알림(Notification)을 클릭하여 앱으로 진입할 때 실행되는 딥링크는 **TaskStackBuilder**나 Navigation 3 백스택 빌더를 사용하여 최상위 홈 화면까지 이어지는 **합성 백스택(Synthetic Task Back Stack)**을 명시적으로 구축해야 한다는 계약이다.
2. **필요성 (Why)**:
   - **이탈 방지 및 태스크 고립 방지**: 알림을 터치해 상세 화면(예: 공지사항 상세)으로 들어간 사용자가 화면 좌상단 Back 버튼이나 OS 뒤로가기를 눌렀을 때, 백스택이 비어있어 앱이 즉시 종료되면 서비스 연속성이 깨진다. 홈 화면으로 이어지는 자연스러운 태스크 스택을 재구성해야 한다.

---

### 백스택 구축 메커니즘 (How)

```kotlin
// TaskStackBuilder를 활용한 notification Synthetic Back Stack 생성
val pendingIntent: PendingIntent? = TaskStackBuilder.create(context).run {
    // 1. 부모 Activity / Root 화면 Intent 추가
    addNextIntentWithParentStack(Intent(context, MainActivity::class.java))
    // 2. 타겟 딥링크 Intent 추가
    addNextIntent(Intent(Intent.ACTION_VIEW, Uri.parse("https://example.com/notice/42")))
    // 3. PendingIntent 생성 (FLAG_IMMUTABLE 필수)
    getPendingIntent(0, PendingIntent.FLAG_UPDATE_CURRENT or PendingIntent.FLAG_IMMUTABLE)
}
```

---

### 관련 상위 및 연관 노트

- 상위 계약: [Deep Link 계약](deep-link-contracts.md)
- 연관 계약: [PendingIntent는 위임된 미래 intent 토큰이다](../intent-manifest-contracts/pendingintent-is-delegated-future-intent-token.md)
