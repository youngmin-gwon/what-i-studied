---
title: android-system-services-and-device-capabilities
tags: ["android", "android/system-services"]
aliases: []
date modified: 2026-08-03 17:35:10 +09:00
date created: 2026-08-03 17:31:11 +09:00
---

## Android 시스템 서비스와 기기 기능 지도

이 지도는 앱이 Android 시스템 또는 기기 기능과 맞닿는 지점을 서비스 접근 공통 계약, 백그라운드 작업, 알림/메시징, Assistant/agent 실행 표면, 위치·센서·전력·패키지/사용자/역할·미디어/오디오/카메라·생체인증/자격증명·텔레포니·입력/접근성, NFC 로 나눈다.

### 읽는 순서

1. [시스템 서비스 접근 공통 계약](./service-lookup/service-lookup-contracts/service-lookup-contracts.md) 에서 `getSystemService()`, Binder, permission, AppOps 가 모든 하위 서비스에 어떻게 공통으로 적용되는지 먼저 확인한다.
2. [백그라운드 작업 계약](./background-and-notifications/background-work-contracts/background-work-contracts.md) 에서 프로세스 수명보다 긴 작업의 실행 수단을 고른다.
3. [알림과 FCM 메시징 계약](./background-and-notifications/notification-messaging-contracts/notification-messaging-contracts.md) 에서 서버 전송, 앱 수신, 시스템 표시를 분리한다.
4. [Assistant와 에이전트 통합 계약](./agents-and-assistant/assistant-agent-contracts/assistant-agent-contracts.md) 에서 외부 호출의 의미 해석, 전달, 권한, 실행 책임을 나눈다.
5. [위치 접근 계약](./device-capabilities/location-contracts/location-contracts.md), [센서 접근 계약](./device-capabilities/sensor-contracts/sensor-contracts.md) 에서 위치 소스 합성과 raw/synthetic 센서 구분을 본다.
6. [전력 상태 접근 계약](./system-state/power-contracts/power-contracts.md), [패키지/사용자/역할 조회 계약](./system-state/package-user-role-contracts/package-user-role-contracts.md) 에서 관찰 전용 상태 조회와 사용자/프로필 분리를 본다.
7. [미디어/오디오/카메라 시스템 서비스 접근 계약](./device-capabilities/media-audio-camera-contracts/media-audio-camera-contracts.md), [생체 인증/자격 증명 계약](./device-capabilities/biometrics-credential-contracts/biometrics-credential-contracts.md), [텔레포니 접근 계약](./device-capabilities/telephony-contracts/telephony-contracts.md), [입력 장치와 접근성 서비스 계약](./device-capabilities/input-accessibility-contracts/input-accessibility-contracts.md) 에서 각 표면별 조정/승인/신뢰 모델을 확인한다.
8. [NFC와 비접촉 기능 계약](./device-capabilities/nfc-contracts/nfc-contracts.md) 에서 태그, NDEF, HCE/APDU, 결제를 서로 다른 프로토콜 문제로 본다.

### 문제 분류

| 증상 또는 질문 | 먼저 볼 지도 | 첫 판단 |
| --- | --- | --- |
| permission 은 granted 인데 API 가 조용히 실패 | 시스템 서비스 접근 공통 계약 | AppOps 가 실행 시점에 별도로 거부했는지 |
| 화면을 닫으면 업로드가 멈춘다 | 백그라운드 작업 | 작업이 지연 가능한지, 사용자에게 보여야 하는지 |
| 정시에 울려야 하는 기능이 늦는다 | 백그라운드 작업 | 정확한 시각이 제품 계약인지 |
| FCM 전송은 성공했지만 알림이 없다 | 알림과 FCM | 전달, 수신, 권한, 채널, 표시 중 어디서 끊겼는지 |
| 음성 질의는 열리지만 잘못된 항목을 실행한다 | Assistant 와 에이전트 | 의미 매핑과 앱 입력 검증 중 어느 책임인지 |
| AppFunction 이 등록됐지만 호출되지 않는다 | Assistant 와 에이전트 | OS 지원, 함수 활성화, 호출자 권한, preview 노출 상태 |
| foreground 에서는 위치가 되는데 background 에서 안 됨 | 위치 접근 계약 | background 위치 permission 별도 요청 여부 |
| 화면 회전 시 센서 값이 이상해 보임 | 센서 접근 계약 | 좌표계를 화면 회전에 맞춰 리매핑했는지 |
| wake lock 을 잡았는데도 작업이 지연됨 | 전력 상태 접근 계약 | wake lock 과 배터리 최적화 예외는 별개라는 점 |
| 다른 앱이 설치돼 있는데 조회 결과에 없음 | 패키지/사용자/역할 조회 계약 | 패키지 가시성(`<queries>`) 선언 여부 |
| 다른 앱 소리와 겹치거나 갑자기 끊김 | 미디어/오디오/카메라 | audio focus 요청 타입과 콜백 처리 |
| 생체 인증 버튼이 있는데 프롬프트가 안 뜸 | 생체 인증/자격 증명 계약 | `canAuthenticate()` 사전 확인을 건너뛰었는지 |
| 듀얼 SIM 기기에서 통화/데이터가 엉뚱한 SIM 으로 감 | 텔레포니 접근 계약 | subscription ID 를 명시적으로 지정했는지 |
| 접근성 서비스가 설치됐는데 동작 안 함 | 입력/접근성 계약 | 사용자가 설정에서 서비스를 명시적으로 활성화했는지 |
| NFC 태그는 읽히지만 결제 단말과 통신하지 않는다 | NFC 와 비접촉 | NDEF 태깅과 HCE/APDU 를 혼동했는지 |

### 책임 경계

- 모든 하위 서비스는 [시스템 서비스 접근 공통 계약](./service-lookup/service-lookup-contracts/service-lookup-contracts.md) 의 lookup/권한/AppOps 모델을 공유한다. 개별 서비스 노트는 이 계약을 반복 설명하지 않고 링크로 참조한다.
- `AlarmManager`, WorkManager, foreground service 는 같은 작업의 강도 단계가 아니라 시간 정확성, 지연 허용도, 사용자 가시성이라는 서로 다른 계약이다.
- FCM 은 전송 수단이고 Android 알림은 표시 수단이다. 둘 중 하나의 성공이 다른 하나를 보장하지 않는다.
- App Actions 는 Assistant 질의를 앱 fulfillment 로 연결하고, AppFunctions 는 승인된 호출자가 앱 함수를 발견·실행하는 Android 16+ preview 표면이다.
- Bluetooth 를 포함한 connectivity 는 이 지도가 아니라 `01_system_internals/connectivity` 가 담당한다.
- 미디어/오디오/카메라의 코덱·렌더링 파이프라인 자체는 `01_system_internals/graphics-and-media` 가 담당하며, 이 지도는 system-service 접근 표면(포커스 조정, 가용성 조회, 세션 노출)만 다룬다.
- NFC 태그 디스패치와 HCE 는 안테나를 공유하지만 데이터 모델과 상대 장치, 보안 상태 머신이 다르다.

### 영역 지도

- [시스템 서비스 접근 공통 계약](./service-lookup/service-lookup-contracts/service-lookup-contracts.md)
- [백그라운드 작업 계약](./background-and-notifications/background-work-contracts/background-work-contracts.md)
- [알림과 FCM 메시징 계약](./background-and-notifications/notification-messaging-contracts/notification-messaging-contracts.md)
- [Assistant와 에이전트 통합 계약](./agents-and-assistant/assistant-agent-contracts/assistant-agent-contracts.md)
- [위치 접근 계약](./device-capabilities/location-contracts/location-contracts.md)
- [센서 접근 계약](./device-capabilities/sensor-contracts/sensor-contracts.md)
- [전력 상태 접근 계약](./system-state/power-contracts/power-contracts.md)
- [패키지/사용자/역할 조회 계약](./system-state/package-user-role-contracts/package-user-role-contracts.md)
- [미디어/오디오/카메라 시스템 서비스 접근 계약](./device-capabilities/media-audio-camera-contracts/media-audio-camera-contracts.md)
- [생체 인증/자격 증명 계약](./device-capabilities/biometrics-credential-contracts/biometrics-credential-contracts.md)
- [텔레포니 접근 계약](./device-capabilities/telephony-contracts/telephony-contracts.md)
- [입력 장치와 접근성 서비스 계약](./device-capabilities/input-accessibility-contracts/input-accessibility-contracts.md)
- [NFC와 비접촉 기능 계약](./device-capabilities/nfc-contracts/nfc-contracts.md)

새 노트는 특정 API 를 나열하기보다 `시스템이 보장하는 것`, `앱이 영속화·검증할 것`, `버전·권한 조건`, `관찰 가능한 실패` 중 하나의 판단 단위를 맡아야 한다.

검증일: 2026-08-03. 이 지도는 `_meta/android-knowledge-base-quality-plan.md` Phase 1(2026-08-03)에서 확정한 "이름 유지 + 범위 확장" 결정에 따라 위 클러스터를 모두 갖췄다.
