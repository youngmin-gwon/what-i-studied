# watchOS Fitness & Health Guide #apple #watchos #health

워치에서 피트니스/헬스 앱을 만들 때 알아야 할 내용을 쉽게 정리했다. 용어는 [apple-glossary](../../00_foundations/apple-glossary.md).

## 핵심 개념
- 짧은 상호작용, 빠른 피드백. 손목을 올리는 순간 바로 보여야 한다.
- 배터리/메모리 예산이 작다. 작업을 짧게 나누고, 백그라운드 남용 금지.
- iPhone과 페어링된 경우가 많지만, 셀룰러/와이파이 단독도 가능.

## 건강/운동 데이터
- HealthKit: 건강 데이터(심박, 칼로리, 수면 등). 범위가 넓으니 필요한 타입만 요청.
- WorkoutKit: 운동 세션 생성/관리. 시작/일시정지/종료, 샘플 수집.
- Motion/센서: 가속도/자이로/GPS/고도/나침반. 권한/전력 고려.
- HRV/혈중 산소 등 고급 측정은 기기/OS 버전에 따라 지원 여부 확인.

## UI/UX
- SwiftUI 권장. 큰 텍스트, 단순 제스처. Digital Crown/Swipe로 스크롤.
- 컴플리케이션: 시계 페이스에 요약 정보 제공. 타임라인 준비(미래 값)로 오프라인 대응.
- 알림: 운동 진행/목표 달성/심박 알림 등. 짧고 명확하게.

## 백그라운드/실행
- Workout 세션 중에는 더 긴 실행이 허용되지만, 여전히 메모리/전력 제약이 큼.
- Background Refresh/Push를 적게 사용. 남용 시 제한.
- 오디오/블루투스/VoIP 등 필요한 모드만 사용.

## 네트워크/동기화
- WCSession으로 iPhone과 데이터 교환. Reachability 체크, 지연/재시도 정책.
- Cloud/서버 동기화는 짧게/압축해 전송, 가능하면 나중에 iPhone이 처리.

## 접근성/안전
- 진동/햅틱/사운드를 적절히 사용. VoiceOver/큰 텍스트 지원.
- 운동/건강 데이터는 민감: 최소 권한, 명확한 설명, 프라이버시 라벨 반영.

## 테스트
- 다양한 운동(실내/야외), 위치 품질, 페어링 유무, Low Power/워크아웃 모드.
- 배터리 소모/열/메모리 경고 관찰. Jetsam 로그 확인.

## 체크리스트
- 어떤 데이터 타입이 정말 필요한가? HealthKit 권한을 좁혀라.
- Workout 세션이 중단되면 어떻게 복구할 것인가?
- 네트워크 실패/페어링 끊김 시 데이터 유실이 없는가?
- 컴플리케이션/알림이 과도하지 않은가?

## 링크
[apple-watchos-wearables](../../../../../../../apple-watchos-wearables.md), [apple-network-basics](../../../../../../../apple-network-basics.md), [apple-performance-and-debug](../../06_testing_performance/apple-performance-and-debug.md), [apple-sandbox-and-security](../../05_security_privacy/apple-sandbox-and-security.md).
