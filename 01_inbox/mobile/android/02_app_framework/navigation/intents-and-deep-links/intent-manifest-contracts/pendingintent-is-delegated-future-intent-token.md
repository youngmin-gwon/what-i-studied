---
title: pendingintent-is-delegated-future-intent-token
tags: [android, android/navigation, android/intent, security]
aliases: ["PendingIntent는 위임된 미래 intent 토큰이다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## PendingIntent 는 위임된 미래 intent 토큰이다

상위 문서: [Intent & Manifest 계약](intent-manifest-contracts.md)

---

### 개념과 필요성 (What & Why)

1. **개념 (What)**:
   - **`PendingIntent`**는 안드로이드 OS의 알림(Notification), 위젯(AppWidget), 알람 매니저(AlarmManager) 등 타 프로세스나 외부 시스템 서비스에게 **발행 앱의 권한(UID 및 Identity)으로 미래 시점에 내부 Intent를 대신 실행할 수 있도록 위임하는 권한 부여 토큰(Token)**이다.
2. **필요성 (Why)**:
   - 외부 프로세스는 발행 앱의 내부 액티비티를 직접 실행할 권한이 없지만, `PendingIntent` 토큰을 전달받음으로써 토큰 발행 앱의 신원과 권한을 그대로 위임받아 특정 시점에 안전하게 액티비티를 구동할 수 있다.

---

### 보안 통제 (FLAG_IMMUTABLE vs FLAG_MUTABLE)

- **`FLAG_IMMUTABLE` (현대 안드로이드 필수 표준)**:
  수신한 타 프로세스가 `PendingIntent` 내부의 Intent 파라미터를 임의로 수정하거나 변경할 수 없도록 원천 차단한다. (Android 12+ 필수 지정).
- **`FLAG_MUTABLE`**:
  알림 답장(Direct Reply)처럼 외부 프로세스에서 추가 데이터를 덧붙여야 할 때만 제한적으로 허용한다.

```kotlin
val intent = Intent(context, DetailActivity::class.java)
val pendingIntent = PendingIntent.getActivity(
    context,
    0,
    intent,
    PendingIntent.FLAG_UPDATE_CURRENT or PendingIntent.FLAG_IMMUTABLE
)
```

---

### 관련 상위 및 연관 노트

- 상위 계약: [Intent & Manifest 계약](intent-manifest-contracts.md)
- 연관 계약: [Notification deep link는 명시적 task와 back stack 정책이 필요하다](../deep-link-contracts/notification-deep-link-needs-explicit-task-and-back-stack-policy.md)
