# iOS Advanced Capabilities #apple #ios #advanced

iOS에서 고급 기능을 쓸 때 주의할 점을 쉽게 정리했다. 용어는 [apple-glossary](../../00_foundations/apple-glossary.md).

## 네비게이션/지도
- MapKit: 지도/핀/경로. 정확/대략 위치 권한 구분.
- 차량/자전거/대중교통/도보 경로 제공 여부를 확인.
- 지도 캡처/내보내기는 정책을 따른다(저작권/사용 제한).

## 카메라/미디어 확장
- ProRAW/ProRes, 심도 데이터, 멀티 카메라 동시 캡처는 기기별로 다르다.
- 시네마틱 모드/인물 모드 등은 시스템 API 지원 여부를 확인.
- 라이브 포토/버스트/QR/바코드 스캔은 AVCaptureMetadataOutput 사용.

## 센서/하드웨어
- CoreMotion: 가속도/자이로/자기장/고도. 배터리 고려.
- UWB/NFC: 접근/실내 위치/근접. 엔타이틀먼트/기기 지원 필요.
- CoreML/Neural Engine: 온디바이스 ML, 모델 크기/메모리/전력 확인.

## 멀티태스킹/백그라운드
- Live Activity/다이내믹 아일랜드: 실시간 업데이트, 적절한 빈도/배터리 관리.
- Background Tasks(BGTaskScheduler): 앱이 죽어도 작업 예약. 심사에 맞게 사용 목적 명확히.
- Widgets: 홈/잠금/스마트 스택, 주기적 업데이트 예산 준수.

## 통신/연결
- CallKit: 통화 UI/차단/식별. 음성/VoIP 권한, PushKit 푸시(제한적).
- Nearby(멀티피어/Bluetooth/UWB): 프라이버시/권한/배터리 고려.
- Hotspot/Network Extension: Entitlement 요구, 스토어 심사 엄격.

## 결제/지갑
- In-App Purchase/구독: StoreKit 2, 영수증 검증.
- Apple Pay/Wallet Passes: PKPaymentAuthorizationController, NFC/리더 모드 엔타이틀먼트.
- 외부 결제 링크는 정책/지역별 예외를 반드시 확인.

## 건강/피트니스
- HealthKit/ResearchKit/WorkoutKit: 데이터 타입/권한 명확히. 백업/동기화/프라이버시 라벨 반영.
- Motion/Activity Ring 통합 시 목표/칼로리/시간 계산을 정확히.

## 보안/프라이버시
- Face ID/Touch ID: LAContext로 인증, 생체 정보는 앱에서 볼 수 없다.
- Passkeys/FIDO: 인증용으로 WebAuthn/ASAuthorizationPlatformPublicKeyCredential.
- 클립보드/스크린샷/스크린 녹화 접근은 제한적, 사용자 알림을 존중.

## 국제화/현지 규제
- 메시징/지도/결제/미디어는 지역 규제가 다를 수 있다(예: 중국 지도/위치).
- 언어/통화/세금/법률에 맞는 처리 필요.

## 테스트/운영
- 실제 기기/네트워크/권한/언어/배터리/저장 공간 조합에서 테스트.
- 크래시/성능/에너지/푸시 성공률 모니터링.
- 피처 플래그/원격 설정으로 점진적 롤아웃.

## 링크
[apple-ios-playbook](apple-ios-playbook.md), [apple-performance-and-debug](../../06_testing_performance/apple-performance-and-debug.md), [apple-network-basics](../../../../../../../apple-network-basics.md), [apple-sandbox-and-security](../../05_security_privacy/apple-sandbox-and-security.md), [apple-distribution-and-policies](../../05_security_privacy/apple-distribution-and-policies.md).
