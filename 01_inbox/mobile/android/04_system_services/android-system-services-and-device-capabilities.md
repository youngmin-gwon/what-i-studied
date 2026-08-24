---
title: android-system-services-and-device-capabilities
tags: ["android", "android/system-services"]
aliases: []
date modified: 2026-08-07 11:37:52 +09:00
date created: 2026-08-03 17:31:11 +09:00
---

## Android 시스템 서비스와 기기 기능 지도

배경 지식: [Learning Spine 10장 — device capability 발견과 background execution](../00_foundations/learning-spine/10-device-capability-discovery-and-background-execution.md)

이 지도는 앱이 Android 시스템 또는 기기 기능과 맞닿는 지점을 서비스 접근 공통 계약, 백그라운드 작업, 알림/메시징, Assistant/agent 실행 표면, 위치·센서·전력·패키지/사용자/역할·미디어/오디오/카메라·생체인증/자격증명·텔레포니·입력/접근성·Bluetooth·온디바이스 AI·App Shortcuts·Health Connect, NFC 로 나눈다.

### 읽는 순서

1. [시스템 서비스 접근 공통 계약](service-lookup/service-lookup.md) 에서 `getSystemService()`, Binder, permission, AppOps 가 모든 하위 서비스에 어떻게 공통으로 적용되는지 먼저 확인한다.
2. [백그라운드 작업 계약](background-and-notifications/background-work.md) 에서 프로세스 수명보다 긴 작업의 실행 수단을 고른다.
3. [알림과 FCM 메시징 계약](background-and-notifications/notification-messaging.md) 에서 서버 전송, 앱 수신, 시스템 표시를 분리한다.
4. [Assistant와 에이전트 통합 계약](assistant-agent/assistant-agent.md) 에서 외부 호출의 의미 해석, 전달, 권한, 실행 책임을 나눈다.
5. [Bluetooth 접근 계약](./device-capabilities/bluetooth/bluetooth.md) 에서 Classic/BLE 연결 모델 차이와 Android 12+ 권한 재설계를 본다.
6. [위치 접근 계약](./device-capabilities/location/location.md), [센서 접근 계약](./device-capabilities/sensors/sensor.md) 에서 위치 소스 합성과 raw/synthetic 센서 구분을 본다.
7. [Health Connect 접근 계약](./device-capabilities/health-connect/health-connect.md) 에서 센서가 만든 값이 앱 간 공유 저장소로 넘어갈 때의 권한·소유권 모델을 본다.
8. [전력 상태 접근 계약](system-state/power.md), [패키지/사용자/역할 조회 계약](system-state/package-user-role.md) 에서 관찰 전용 상태 조회와 사용자/프로필 분리를 본다.
9. [미디어/오디오/카메라 시스템 서비스 접근 계약](./device-capabilities/media-audio-camera/media-audio-camera.md), [생체 인증/자격 증명 계약](./device-capabilities/biometrics-credential/biometrics-credential.md), [텔레포니 접근 계약](./device-capabilities/telephony/telephony.md), [입력 장치와 접근성 서비스 계약](./device-capabilities/input-accessibility/input-accessibility.md) 에서 각 표면별 조정/승인/신뢰 모델을 확인한다.
10. [온디바이스 AI 접근 계약](./device-capabilities/on-device-ai/on-device-ai.md) 에서 ML Kit/LiteRT 온디바이스 추론과 AICore 공유 모델, 가용성 확인 계약을 본다.
11. [NFC와 비접촉 기능 계약](./device-capabilities/nfc/nfc.md) 에서 태그, NDEF, HCE/APDU, 결제를 서로 다른 프로토콜 문제로 본다.
12. [App Shortcuts 접근 계약](./device-capabilities/app-shortcuts/app-shortcuts.md) 에서 static/dynamic/pinned shortcut 의 소유권 차이와 개수/rate limit 제약을 본다.
13. [AppSearch 접근 계약](./device-capabilities/appsearch/appsearch.md) 에서 온디바이스 검색 색인 저장소 선택과 스키마 마이그레이션 계약을 본다.
14. [음성 합성/인식 접근 계약](./device-capabilities/speech/speech.md) 에서 `TextToSpeech` 의 비동기 초기화와 `SpeechRecognizer` 의 권한/콜백 순서 계약을 본다.
15. [Haptics 및 Vibrator 계약](./device-capabilities/haptics-vibrator/haptics-and-vibrator.md) 에서 `LocalHapticFeedback` 터치 피드백과 `VibratorManager` / `VibrationEffect` 진동 파형 제어를 본다.

### 문제 분류

| 증상 또는 질문 | 먼저 볼 지도 | 첫 판단 |
| --- | --- | --- |
| 터치 시 햅틱 진동이 켜지지 않거나 무반응 | Haptics 및 Vibrator 계약 | `VibrationAttributes` 목적 지정 및 터치 진동 설정 상태 |
| permission 은 granted 인데 API 가 조용히 실패 | 시스템 서비스 접근 공통 계약 | AppOps 가 실행 시점에 별도로 거부했는지 |
| 화면을 닫으면 업로드가 멈춘다 | 백그라운드 작업 | 작업이 지연 가능한지, 사용자에게 보여야 하는지 |
| 정시에 울려야 하는 기능이 늦는다 | 백그라운드 작업 | 정확한 시각이 제품 계약인지 |
| FCM 전송은 성공했지만 알림이 없다 | 알림과 FCM | 전달, 수신, 권한, 채널, 표시 중 어디서 끊겼는지 |
| 음성 질의는 열리지만 잘못된 항목을 실행한다 | Assistant 와 에이전트 | 의미 매핑과 앱 입력 검증 중 어느 책임인지 |
| AppFunction 이 등록됐지만 호출되지 않는다 | Assistant 와 에이전트 | OS 지원, 함수 활성화, 호출자 권한, preview 노출 상태 |
| Bluetooth 스캔/연결에서 `SecurityException` 이 발생한다 | Bluetooth 접근 계약 | targetSdk 31+ 런타임 권한과 위치 권한 대체 조건을 구분했는지 |
| foreground 에서는 위치가 되는데 background 에서 안 됨 | 위치 접근 계약 | background 위치 permission 별도 요청 여부 |
| 화면 회전 시 센서 값이 이상해 보임 | 센서 접근 계약 | 좌표계를 화면 회전에 맞춰 리매핑했는지 |
| 걸음 수는 읽히는데 심박수는 안 읽힘 | Health Connect 접근 계약 | 레코드 타입별 권한을 개별로 승인받았는지 |
| wake lock 을 잡았는데도 작업이 지연됨 | 전력 상태 접근 계약 | wake lock 과 배터리 최적화 예외는 별개라는 점 |
| 다른 앱이 설치돼 있는데 조회 결과에 없음 | 패키지/사용자/역할 조회 계약 | 패키지 가시성(`<queries>`) 선언 여부 |
| 다른 앱 소리와 겹치거나 갑자기 끊김 | 미디어/오디오/카메라 | audio focus 요청 타입과 콜백 처리 |
| 생체 인증 버튼이 있는데 프롬프트가 안 뜸 | 생체 인증/자격 증명 계약 | `canAuthenticate()` 사전 확인을 건너뛰었는지 |
| 듀얼 SIM 기기에서 통화/데이터가 엉뚱한 SIM 으로 감 | 텔레포니 접근 계약 | subscription ID 를 명시적으로 지정했는지 |
| 접근성 서비스가 설치됐는데 동작 안 함 | 입력/접근성 계약 | 사용자가 설정에서 서비스를 명시적으로 활성화했는지 |
| 특정 기기에서만 온디바이스 AI 기능이 동작하지 않는다 | 온디바이스 AI 접근 계약 | `checkFeatureStatus()` 로 가용성을 먼저 확인했는지 |
| NFC 태그는 읽히지만 결제 단말과 통신하지 않는다 | NFC 와 비접촉 | NDEF 태깅과 HCE/APDU 를 혼동했는지 |
| pin 된 shortcut 을 코드로 지워도 홈 화면에 남아있다 | App Shortcuts 접근 계약 | pin 이후 소유권이 launcher 로 넘어갔는지 |
| 설정 앱 검색에 내 데이터가 안 뜬다 | AppSearch 접근 계약 | `PlatformStorage`/`PlayServicesStorage` 를 쓰는지, 스키마 타입에 `setSchemaTypeDisplayedBySystem(true)` 를 켰는지 |
| 스키마를 바꿔 배포했더니 기존 데이터가 사라졌다 | AppSearch 접근 계약 | `Migrator` 없이 비호환 변경을 `forceOverride` 로 배포했는지 |
| TTS `speak()` 를 호출해도 무음이다 | 음성 합성/인식 접근 계약 | `OnInitListener` 의 `SUCCESS` 콜백을 받기 전에 호출했는지 |
| 음성 인식이 권한 승인 후에도 실패한다 | 음성 합성/인식 접근 계약 | `RECORD_AUDIO` 승인 여부와 on-device/network 인식 선택을 구분했는지 |

### 책임 경계

- 모든 하위 서비스는 [시스템 서비스 접근 공통 계약](service-lookup/service-lookup.md) 의 lookup/권한/AppOps 모델을 공유한다. 개별 서비스 노트는 이 계약을 반복 설명하지 않고 링크로 참조한다.
- `AlarmManager`, WorkManager, foreground service 는 같은 작업의 강도 단계가 아니라 시간 정확성, 지연 허용도, 사용자 가시성이라는 서로 다른 계약이다.
- FCM 은 전송 수단이고 Android 알림은 표시 수단이다. 둘 중 하나의 성공이 다른 하나를 보장하지 않는다.
- App Actions 는 Assistant 질의를 앱 fulfillment 로 연결하고, AppFunctions 는 승인된 호출자가 앱 함수를 발견·실행하는 Android 16+ preview 표면이다.
- Wi-Fi, 셀룰러, VPN 같은 IP 기반 connectivity 는 이 지도가 아니라 `01_system_internals/connectivity` 가 담당한다. Bluetooth 는 IP 스택을 거치지 않는 별도 무선 기술이므로 이 지도의 [Bluetooth 접근 계약](./device-capabilities/bluetooth/bluetooth.md) 이 다룬다.
- 미디어/오디오/카메라의 코덱·렌더링 파이프라인 자체는 `01_system_internals/graphics-and-media` 가 담당하며, 이 지도는 system-service 접근 표면(포커스 조정, 가용성 조회, 세션 노출)만 다룬다.
- 온디바이스 AI 는 모델 학습이나 프롬프트 품질이 아니라 추론 위치(온디바이스/클라우드), 모델 배포 주체(앱 번들/AICore 공유), 가용성 확인이라는 접근 계약만 다룬다.
- NFC 태그 디스패치와 HCE 는 안테나를 공유하지만 데이터 모델과 상대 장치, 보안 상태 머신이 다르다.
- App Shortcuts 는 홈 화면 진입점의 소유권/개수 계약만 다루며, App Widget 의 `RemoteViews` 렌더링 계약과는 별개다.
- Health Connect 는 기기 안에서 여러 앱이 공유하는 온디바이스 저장소이지 클라우드 동기화 서비스가 아니며, 권한은 일반 런타임 권한 모델과 별개로 레코드 타입별로 개별 승인된다.
- AppSearch 는 기기 안에서 구조화된 데이터를 검색 가능하게 색인하는 온디바이스 검색 계약이며, 클라우드 검색 서비스나 Room/SQLite 같은 일반 로컬 저장 계약과는 다르다.
- TTS/SpeechRecognizer 는 텍스트↔음성 변환 API 자체의 초기화·권한·콜백 순서 계약만 다루며, Assistant 질의의 의미 해석과 실행 책임은 [Assistant와 에이전트 통합 계약](assistant-agent/assistant-agent.md) 이 담당한다.

### 영역 지도

- [시스템 서비스 접근 공통 계약](service-lookup/service-lookup.md)
- [백그라운드 작업 계약](background-and-notifications/background-work.md)
- [알림과 FCM 메시징 계약](background-and-notifications/notification-messaging.md)
- [Assistant와 에이전트 통합 계약](assistant-agent/assistant-agent.md)
- [Bluetooth 접근 계약](./device-capabilities/bluetooth/bluetooth.md)
- [위치 접근 계약](./device-capabilities/location/location.md)
- [센서 접근 계약](./device-capabilities/sensors/sensor.md)
- [Health Connect 접근 계약](./device-capabilities/health-connect/health-connect.md)
- [전력 상태 접근 계약](system-state/power.md)
- [패키지/사용자/역할 조회 계약](system-state/package-user-role.md)
- [미디어/오디오/카메라 시스템 서비스 접근 계약](./device-capabilities/media-audio-camera/media-audio-camera.md)
- [생체 인증/자격 증명 계약](./device-capabilities/biometrics-credential/biometrics-credential.md)
- [텔레포니 접근 계약](./device-capabilities/telephony/telephony.md)
- [입력 장치와 접근성 서비스 계약](./device-capabilities/input-accessibility/input-accessibility.md)
- [Haptics 및 Vibrator 계약](./device-capabilities/haptics-vibrator/haptics-and-vibrator.md)
- [온디바이스 AI 접근 계약](./device-capabilities/on-device-ai/on-device-ai.md)
- [NFC와 비접촉 기능 계약](./device-capabilities/nfc/nfc.md)
- [App Shortcuts 접근 계약](./device-capabilities/app-shortcuts/app-shortcuts.md)
- [AppSearch 접근 계약](./device-capabilities/appsearch/appsearch.md)
- [음성 합성/인식 접근 계약](./device-capabilities/speech/speech.md)

새 노트는 특정 API 를 나열하기보다 `시스템이 보장하는 것`, `앱이 영속화·검증할 것`, `버전·권한 조건`, `관찰 가능한 실패` 중 하나의 판단 단위를 맡아야 한다.

검증일: 2026-08-05. 이 지도는 `_meta/android-knowledge-base-quality-plan.md` 기준 Haptics 및 Vibrator 계약 추가 반영 완료.
