# iOS Playbook #apple #ios #playbook

iPhone을 위한 앱을 만들 때 알아야 할 실전 가이드를 쉽게 모았다. 용어는 [apple-glossary](../../00_foundations/apple-glossary.md).

## 기기 특성
- 터치/제스처, 카메라/마이크/센서가 핵심. 한 손 사용/짧은 세션이 많다.
- 셀룰러 환경: 데이터/배터리 제약, [[apple-glossary#ATS|ATS]]/백그라운드 정책 엄격.
- 화면 크기가 다양하지만, iPad보다 작고 휴대성이 크다.

## 앱 구조
- SwiftUI 또는 UIKit. Scene 기반 멀티 윈도우 지원하지만, 대부분 하나의 창.
- 딥링크/유니버설 링크로 외부에서 진입.
- Extension으로 위젯/공유/라이브 액티비티/인텐트를 제공.

## 권한 설계
- 카메라/마이크/사진/위치/알림/블루투스 등 TCC 권한을 “필요할 때” 요청.
- NS*UsageDescription 문구를 명확히. 거부 시 대체 흐름/설정 이동 제공.

## 백그라운드 작업
- 허용된 [[apple-glossary#Background Modes|백그라운드 모드]]: 오디오, 위치, VoIP 푸시, BLE, 다운로드, PiP 등.
- Background App Refresh/Push로 짧게 깨워서 동기화. 과도한 사용은 제한/거절.
- [[apple-glossary#JetSam|Jetsam]]이 언제든 앱을 종료할 수 있으니 작업 단위를 짧게.

## 네트워크
- Low Data/Low Power 대응: 품질 낮추기/지연/캐시.
- URLSession Background로 업/다운로드. 실패/재시도/재개 토큰.
- APNs 토큰/환경 구분. 알림 카테고리/액션/크리티컬 여부 설정.

## UI/UX
- Safe Area/Notch/다양한 기기 크기 대응. Dynamic Type/다크 모드/RTL 지원.
- 제스처(스와이프 백, Pull to refresh, 탭)와 시스템 네비게이션과 충돌하지 않도록.
- Haptics/음성 피드백으로 터치감을 준다.

## 미디어/카메라
- AVCapture로 사진/영상/라이브 포토/QR 스캔. 기기별 해상도/포맷 확인.
- Photo picker로 제한된 사진 접근. HEIF/HEVC 기본, 호환성 옵션 제공.
- 오디오 세션 카테고리/모드로 통화/미디어/게임 상황에 맞게 설정.

## 위치/지도
- 정밀/대략, 항상/사용 시 권한 구분. 백그라운드 위치는 별도 플래그 필요.
- 지역 모니터링/방문/비콘은 배터리를 많이 쓸 수 있다. 필요한 최소로 설정.

## 스토리지
- 앱 컨테이너 크기를 관리. 캐시는 Caches, 사용자 데이터는 Documents/Library.
- iCloud 백업 제외(`isExcludedFromBackup`)를 적절히 설정.
- Core Data/SQLite/Realm 등 로컬 DB를 사용할 때 백업/동기화 정책을 명확히.

## 성능/품질
- Instruments로 스타트업/프레임/메모리/에너지 점검.
- Touch latency/Jank는 즉시 고친다. Core Animation/SwiftUI 프리뷰 적극 활용.
- 크래시/ANR(앱 응답 없음) 리포트를 수집/심볼리케이션.

## 배포/정책
- App Store 심사 가이드 준수: 사설 API 금지, 권한 남용 금지, IAP 정책 준수.
- Privacy Nutrition Label/ATT 준비. TestFlight로 베타 테스트.

## 체크리스트
- 권한 요청 타이밍이 적절한가? 대체 경로가 있는가?
- 백그라운드 작업이 정책 범위 안에 있는가?
- 네트워크/저장/배터리/성능을 측정하고 최적화했는가?
- 접근성/다국어/다크 모드 대응이 되었는가?

## 링크
[apple-foundations](../../00_foundations/apple-foundations.md), [apple-app-lifecycle-and-ui](../../02_ui_frameworks/apple-app-lifecycle-and-ui.md), [apple-sandbox-and-security](../../05_security_privacy/apple-sandbox-and-security.md), [apple-performance-and-debug](../../06_testing_performance/apple-performance-and-debug.md), [apple-distribution-and-policies](../../05_security_privacy/apple-distribution-and-policies.md).
