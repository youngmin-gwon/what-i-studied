---
title: "Android 시스템 서비스와 기기 기능 지도"
tags: ["android", "android/system-services"]
---

# Android 시스템 서비스와 기기 기능 지도

이 지도는 앱이 Android 시스템 또는 기기 기능과 맞닿는 지점을 백그라운드 작업, 알림/메시징, Assistant/agent 실행 표면, NFC 기능으로 나눈다.

## 읽는 순서

1. [백그라운드 작업 계약](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/background-work-contracts.md)에서 프로세스 수명보다 긴 작업의 실행 수단을 고른다.
2. [알림과 FCM 메시징 계약](01_inbox/mobile/android/04_system_services/background-and-notifications/notification-messaging-contracts/notification-messaging-contracts.md)에서 서버 전송, 앱 수신, 시스템 표시를 분리한다.
3. [Assistant와 에이전트 통합 계약](01_inbox/mobile/android/04_system_services/agents-and-assistant/assistant-agent-contracts/assistant-agent-contracts.md)에서 외부 호출의 의미 해석, 전달, 권한, 실행 책임을 나눈다.
4. [NFC와 비접촉 기능 계약](01_inbox/mobile/android/04_system_services/device-capabilities/nfc-contracts/nfc-contracts.md)에서 태그, NDEF, HCE/APDU, 결제를 서로 다른 프로토콜 문제로 본다.

## 문제 분류

| 증상 또는 질문 | 먼저 볼 지도 | 첫 판단 |
| --- | --- | --- |
| 화면을 닫으면 업로드가 멈춘다 | 백그라운드 작업 | 작업이 지연 가능한지, 사용자에게 보여야 하는지 |
| 정시에 울려야 하는 기능이 늦는다 | 백그라운드 작업 | 정확한 시각이 제품 계약인지 |
| FCM 전송은 성공했지만 알림이 없다 | 알림과 FCM | 전달, 수신, 권한, 채널, 표시 중 어디서 끊겼는지 |
| 음성 질의는 열리지만 잘못된 항목을 실행한다 | Assistant와 에이전트 | 의미 매핑과 앱 입력 검증 중 어느 책임인지 |
| AppFunction이 등록됐지만 호출되지 않는다 | Assistant와 에이전트 | OS 지원, 함수 활성화, 호출자 권한, preview 노출 상태 |
| NFC 태그는 읽히지만 결제 단말과 통신하지 않는다 | NFC와 비접촉 | NDEF 태깅과 HCE/APDU를 혼동했는지 |

## 책임 경계

- `AlarmManager`, WorkManager, foreground service는 같은 작업의 강도 단계가 아니라 시간 정확성, 지연 허용도, 사용자 가시성이라는 서로 다른 계약이다.
- FCM은 전송 수단이고 Android 알림은 표시 수단이다. 둘 중 하나의 성공이 다른 하나를 보장하지 않는다.
- App Actions는 Assistant 질의를 앱 fulfillment로 연결하고, AppFunctions는 승인된 호출자가 앱 함수를 발견·실행하는 Android 16+ preview 표면이다.
- NFC 태그 디스패치와 HCE는 안테나를 공유하지만 데이터 모델과 상대 장치, 보안 상태 머신이 다르다.

## 영역 지도

- [백그라운드 작업 계약](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/background-work-contracts.md)
- [알림과 FCM 메시징 계약](01_inbox/mobile/android/04_system_services/background-and-notifications/notification-messaging-contracts/notification-messaging-contracts.md)
- [Assistant와 에이전트 통합 계약](01_inbox/mobile/android/04_system_services/agents-and-assistant/assistant-agent-contracts/assistant-agent-contracts.md)
- [NFC와 비접촉 기능 계약](01_inbox/mobile/android/04_system_services/device-capabilities/nfc-contracts/nfc-contracts.md)

새 노트는 특정 API를 나열하기보다 `시스템이 보장하는 것`, `앱이 영속화·검증할 것`, `버전·권한 조건`, `관찰 가능한 실패` 중 하나의 판단 단위를 맡아야 한다.
