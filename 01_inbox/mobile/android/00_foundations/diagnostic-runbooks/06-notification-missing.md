---
title: 알림이 오지 않는다(FCM 전달은 성공했는데 표시되지 않는다)
tags: ["android", "android/foundations", "diagnostic-runbook"]
aliases: ["Runbook: notification missing despite successful FCM delivery"]
date modified: 2026-08-04 10:55:00 +09:00
date created: 2026-08-04 10:55:00 +09:00
---

## 알림이 오지 않는다(FCM 전달은 성공했는데 표시되지 않는다)

### 증상

서버는 FCM 전송에 성공했다고 기록하는데, 사용자 기기에는 알림이 표시되지 않는다.

### 재현 조건

- "알림이 안 온다"를 하나의 증상으로 뭉뚱그리지 말고, 서버 전송/기기 수신/시스템 표시/사용자 탭 중 어느 단계까지 확인됐는지부터 나눠서 리포트를 받는다.
- 재현 시 앱 상태(포그라운드/백그라운드/종료)를 반드시 함께 기록한다. notification과 data payload의 처리 경로가 앱 상태에 따라 다르기 때문이다.

### 가능한 실패 경계와 우선순위

FCM은 전달 수단이고 Android 알림은 표시 수단이며, 하나의 성공이 다른 하나를 보장하지 않는다. 다음 순서로 좁힌다.

1. **`POST_NOTIFICATIONS` 런타임 권한(Android 13+)이 거부됐다.** 가장 흔한 원인. 전달은 성공해도 이 권한이 없으면 시스템이 알림을 표시하지 않는다.
2. **알림 채널이 사용자에 의해 차단됐거나, 채널 자체가 생성되지 않았다.** 채널이 없으면 게시 자체가 실패할 수 있다.
3. **백그라운드 상태에서 data-only 메시지를 보내 앱이 직접 알림을 만들어야 하는데, 그 로직이 실행되지 않았다.** notification payload 없이 data만 보낸 경우, 알림 표시는 전적으로 앱 코드의 책임이다.
4. **메시지 자체가 기기에 전달되지 않았다.** Doze, 강제 종료, 네트워크 불가 상태. 이 경우는 서버 로그만으로는 알 수 없고 기기 쪽 확인이 필요하다.
5. **등록 토큰이 오래됐거나 유효하지 않다.** 서버가 잘못된 대상으로 보내고 있는 경우.

### 조사 절차

1. **서버 전송 결과부터 확인한다.**
   FCM 응답 코드가 성공인지, `UNREGISTERED` 같은 오류가 있는지 확인한다. 오류가 있다면 이건 표시 문제가 아니라 등록 식별자 문제다.

2. **기기 수신 로그를 확인한다(포그라운드 재현 시에만 신뢰할 수 있다).**
   `onMessageReceived` 호출 여부와 전달받은 payload를 로그로 확인한다. 앱이 백그라운드/종료 상태였다면 notification 부분에 대해서는 이 콜백이 아예 호출되지 않을 수 있다는 점을 기억한다 — 호출되지 않았다고 곧바로 "수신 실패"로 결론 내리지 않는다.

3. **`POST_NOTIFICATIONS` grant 상태를 별도로 확인한다.**
   ```bash
   adb shell dumpsys package <pkg> | grep -A5 "runtime permissions"
   ```
   Android 13(API 33) 미만 기기는 이 권한 요청 대상이 아니므로, 재현 기기의 OS 버전부터 확인한다.

4. **알림 채널 상태를 확인한다.**
   설정 → 앱 → 알림에서 해당 채널이 켜져 있는지 직접 확인한다. FCM notification payload를 쓴다면 메시지가 지정한 채널 ID가 앱에도 실제로 생성돼 있는지(코드에서 채널 생성 호출이 앱 시작이나 첫 사용 전에 실행되는지) 확인한다.

5. **notification/data 처리 지점을 앱 상태별로 분리해서 확인한다.**
   | 앱 상태 | notification | data |
   | --- | --- | --- |
   | 포그라운드 | `onMessageReceived` | `onMessageReceived` |
   | 백그라운드 | 시스템 트레이 표시(콜백 미실행 가능) | `onMessageReceived` |

   data-only 메시지를 백그라운드 상태에서 받았다면, 알림을 직접 만드는 코드가 `onMessageReceived` 안에 있는지, 그 코드가 채널·권한 조건을 다시 확인하는지 본다.

6. **전달 자체가 기기에 도달했는지 확인한다.**
   Doze/강제 종료/네트워크 문제로 전달이 지연·실패했을 가능성은 서버 로그로는 구분되지 않는다. 기기를 실제로 관찰 가능한 상태로 두고(화면 켜짐, 네트워크 연결) 재현해 이 가능성을 먼저 배제한다.

### OS/API/target SDK 조건

- `POST_NOTIFICATIONS` 런타임 권한은 Android 13(API 33) 이상에서만 요구된다. 그 미만 버전에서는 이 권한 부재가 원인일 수 없다.
- 알림 채널은 Android 8.0(API 26) 이상에서 모든 게시 알림에 필수다.
- foreground service의 알림(FGS notice)은 `POST_NOTIFICATIONS`가 거부된 Android 13+ 기기에서도 Task Manager에는 보일 수 있지만 notification drawer에는 보이지 않는 예외 규칙이 있다 — foreground service 관련 증상이라면 이 차이를 먼저 확인한다.

### 다음 조사 경로

- 탭 이후 잘못된 화면으로 이동한다면 → 알림 자체는 표시된 것이므로 [Worked Example 4의 탭/task 구성](../worked-examples/04-fcm-to-notification-display-and-tap-recovery.md) 절차로
- 메시지 자체가 기기에 도달하지 않는다면 → [background delay runbook](05-background-work-delayed-or-not-running.md)의 Doze/standby 확인 절차와 겹친다
- 특정 기기·제조사에서만 발생한다면 → OEM의 자체 알림/전력 관리 정책 차이를 의심([Learning Spine 12장](../learning-spine/12-compatibility-update-and-form-factor.md))

### 관련 자료

- [Worked Example: FCM 전송에서 notification 표시와 탭 복구까지](../worked-examples/04-fcm-to-notification-display-and-tap-recovery.md)
- [FCM notification payload와 data payload는 처리 지점이 다르다](../../04_system_services/background-and-notifications/notification-messaging-contracts/fcm-notification-and-data-payloads-have-different-handling-points.md)
- [Android 알림은 권한과 채널이 표시 가능성을 결정한다](../../04_system_services/background-and-notifications/notification-messaging-contracts/android-notification-permission-and-channel-control-visibility.md)
- [FCM 운영은 전달, 표시, 탭, 복구를 분리해 관측한다](../../04_system_services/background-and-notifications/notification-messaging-contracts/fcm-operations-observe-delivery-display-tap-and-recovery-separately.md)
- [Learning Spine 10장 기기 기능 발견과 background execution](../learning-spine/10-device-capability-discovery-and-background-execution.md)

### 공식 근거

- [FCM 메시지 전달 이해](https://firebase.google.com/docs/cloud-messaging/understand-delivery)
- [알림 런타임 권한](https://developer.android.com/develop/ui/compose/notifications/notification-permission)
- [알림 채널 생성과 관리](https://developer.android.com/develop/ui/compose/notifications/channels)

검증일: 2026-08-04. 이 runbook은 Learning Spine 10장과 Worked Example 4에서 이미 원문 대조를 마친 내용을 재사용했다.
