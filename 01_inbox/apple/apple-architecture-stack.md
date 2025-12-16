# Apple Architecture Stack #apple #architecture #darwin

층층이 쌓인 구조를 쉽게 살펴본다. 모르는 용어는 [[apple-glossary]].

## 계층
1) 커널 [[apple-glossary#XNU|XNU]]: Mach 메시지 + BSD. 스케줄링, 메모리, 보안, 파일 시스템.
2) 드라이버: [[apple-glossary#Kext/DriverKit|kext/DriverKit]]로 하드웨어 연결.
3) 런타임: [[apple-glossary#dyld|dyld]]가 [[apple-glossary#Mach-O|Mach-O]]를 로드, ObjC/Swift 런타임이 메서드 테이블을 만든다.
4) 시스템 서비스: [[apple-glossary#launchd|launchd]]가 데몬을 관리. WindowServer/macOS, Backboardd+SpringBoard/iOS.
5) 프레임워크: Foundation, Swift, SwiftUI, UIKit/AppKit, Metal, CoreData, CloudKit, HealthKit 등.
6) 앱/확장: .app과 .appex가 샌드박스에서 실행, [[apple-glossary#XPC|XPC]]로 통신.

## 커널과 보안
- 모든 실행은 [[apple-glossary#Code Signing|서명]]과 [[apple-glossary#Entitlement|엔타이틀먼트]] 검사를 통과해야 한다.
- [[apple-glossary#Sandbox|샌드박스]] 프로필과 [[apple-glossary#TCC|TCC]] 팝업이 접근을 제한한다.
- SIP(System Integrity Protection, macOS)은 루트도 손대지 못하는 영역을 지킨다.

## 로더와 바이너리
- [[apple-glossary#dyld|dyld]]가 의존성 체인을 따라 프레임워크를 맵핑한다.
- [[apple-glossary#Mach-O|Mach-O]]에는 코드 서명/LC_UUID/아키텍처(Universal) 정보가 담긴다.
- [[apple-glossary#Rosetta|Rosetta]]가 필요하면 다른 CPU용 코드를 번역한다.

## 시스템 서비스 예시
- WindowServer: macOS 창·레이어 합성.
- SpringBoard/Backboardd: 홈 화면, 앱 전환, 입력/제스처.
- configd: 네트워크 설정, 네임서비스.
- distnoted/notifyd: 시스템 알림/옵저버 패턴.
- powerd: 전원/슬립 관리.

## 앱 계층
- SwiftUI/Storyboard/XIB를 통해 UI를 만들고, [[apple-glossary#GCD|GCD]]와 [[apple-glossary#Run Loop|Run Loop]]로 이벤트를 처리한다.
- Extension은 별도 번들이며 .appex, 예) WidgetKit, Share, Intents, Safari Web Extension.

## 플랫폼 별 차이 간단 메모
- iOS/watchOS/visionOS: 터치·센서 중심, 강한 샌드박스, 백그라운드 제한 많음.
- macOS: 파일 시스템 접근이 넓지만, 앱 샌드박스와 TCC가 점차 강화됨.
- iPadOS: 멀티 윈도우(Stage Manager), 외장 디스플레이, 포인터 지원.
- watchOS: 에너지/메모리 제약이 가장 큼, 앱 수명 짧음.
- visionOS: 공간 윈도우/볼륨/풀 스페이스 개념, 패스스루 렌더링.

## 예시 흐름: 앱 실행
1) 사용자 터치/아이콘 선택.
2) SpringBoard가 launchd에 프로세스 생성 요청, 서명/프로비저닝 검사.
3) dyld가 프레임워크 로드, 런타임이 클래스 등록.
4) @main이 Run Loop 시작, Scene/Window 생성.
5) [[apple-glossary#TCC|TCC]]/샌드박스 규칙에 따라 자원 접근.

## 예시 흐름: 알림 받기
1) 서버→[[apple-glossary#APNs|APNs]]→기기 토큰 대상 전송.
2) APS 데몬이 수신 후 시스템 UI가 표시.
3) 사용자가 누르면 앱이 깨워져 처리. 백그라운드 작업은 제한된 시간/모드에만 허용.

## 링크
[[apple-foundations]], [[apple-runtime-and-swift]], [[apple-sandbox-and-security]], [[apple-app-lifecycle-and-ui]], [[apple-platform-differences]].
