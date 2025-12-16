# Apple Platforms Foundations #apple #ios #ipados #macos #watchos #visionos #fundamentals

이 묶음은 iOS/iPadOS/macOS/watchOS/visionOS를 한 눈에 이해하도록 쉽게 풀어쓴 지도다. 모르는 말은 [[apple-glossary]]에서 바로 찾아볼 수 있게 링크했다. 큰 흐름은 동일하고, 기기 특성에 따라 조금씩 다르게 움직인다.

## 공통 철학
- 하드웨어와 소프트웨어를 함께 설계한다. 전력/보안/성능 목표가 명확해, 앱/OS가 “예상 가능한” 방식으로 움직인다.
- 모든 실행 파일은 [[apple-glossary#Code Signing|코드 서명]]과 [[apple-glossary#Entitlement|Entitlement]]를 요구한다. 서명 없는 코드는 돌아가지 않는다는 점이 기본 보안 장치다.
- UI는 [[apple-glossary#SwiftUI|SwiftUI]]/UIKit/AppKit로 만들고, 비즈니스 로직은 Swift(또는 Objective-C)로 작성한다. 같은 Swift 코드를 여러 플랫폼에서 재사용할 수 있다.
- 앱은 [[apple-glossary#Sandbox|샌드박스]] 안에서 돌아가고, 민감 자원은 [[apple-glossary#TCC|TCC]]가 묻고 허락받는다.

## 계층 한 눈에
- 바닥: [[apple-glossary#Darwin|Darwin]]([[apple-glossary#XNU|XNU]] 커널 + BSD).
- 드라이버: [[apple-glossary#Kext/DriverKit|Kext/DriverKit]]가 하드웨어를 잇는다.
- 런타임/로더: [[apple-glossary#Mach-O|Mach-O]] 실행 파일을 [[apple-glossary#dyld|dyld]]가 읽고, Objective-C/Swift 런타임이 클래스/메서드를 등록한다.
- 시스템 서비스: launchd가 [[apple-glossary#Daemon|데몬]]을 관리하고, WindowServer(맥), SpringBoard/Backboardd(iOS) 등이 UI/입력을 담당한다.
- 프레임워크: Foundation/Swift/SwiftUI/UIKit/AppKit/Metal 등 SDK.
- 앱/확장: .app/.appex 번들, [[apple-glossary#Extension|Extension]](위젯, 공유 시트, 인텐트, 라이브 액티비티 등).

## 앱 구성요소(플랫폼 공통 시각)
- Entrypoint: `@main`(SwiftUI) 또는 `@UIApplicationMain`(UIKit)에서 시작해 Run Loop를 연다.
- Scene: iOS/iPadOS/visionOS에서는 하나의 창 단위. 멀티 윈도우/다중 화면에 중요하다.
- View 계층: SwiftUI(선언형) 또는 UIKit/AppKit(명령형)으로 화면을 구성한다.
- Extension: 메인 앱과 별도 프로세스이며, [[apple-glossary#XPC|XPC]]로 통신한다.

## 프로세스/스레드 기본기
- 메인 스레드는 UI를 담당하므로 오래 막으면 안 된다(ANR에 해당하는 앱 응답 없음 경고가 뜰 수 있다).
- [[apple-glossary#GCD|GCD]] 큐를 사용해 작업을 분산한다. QoS(사용자 인터랙티브, 유저 이니시에이티드, 백그라운드 등)로 우선순위를 정한다.
- [[apple-glossary#Run Loop|Run Loop]]는 입력/타이머/포트 이벤트를 처리한다.

## 메모리/전원 정책
- iOS/watchOS는 메모리가 부족하면 [[apple-glossary#JetSam|JetSam]] 정책으로 앱을 종료한다. 메모리 경고를 받으면 자원을 줄여야 한다.
- 백그라운드 실행은 [[apple-glossary#Background Modes|백그라운드 모드]]에 따라 제한된다(오디오, 위치, BLE, VoIP 등만 허용).
- 전원 절약: Low Power Mode가 네트워크/CPU 활동을 줄인다. watchOS는 더 공격적으로 절전한다.

## 파일·데이터 기초
- 앱 샌드박스에는 Documents/Library/Caches/tmp 등이 있다. iCloud 백업 대상인지 구분되어 있다.
- 파일에 [[apple-glossary#Data Protection Class|Data Protection Class]]를 설정해 잠금 상태에 따라 접근을 제한할 수 있다.
- Keychain은 비밀번호·토큰을 저장하는 안전한 금고다.

## 네트워크 기초
- [[apple-glossary#ATS|ATS]]로 HTTPS를 기본 강제한다. 필요 시 예외를 Info.plist에 명시해야 한다.
- [[apple-glossary#APNs|APNs]]로 푸시 알림을 받고, Background App Refresh/Push로 작업을 깨운다.
- Bonjour/mDNS로 근거리 검색, NEHotspot/NetworkExtension으로 VPN/프록시를 설정할 수 있다(Entitlement 필요).

## 보안 기초
- 모든 바이너리는 [[apple-glossary#Code Signing|서명]]/[[apple-glossary#Entitlement|Entitlement]]/[[apple-glossary#Provisioning Profile|프로비저닝]]을 만족해야 한다.
- 민감 권한: 카메라/마이크/위치/연락처/사진/블루투스/알림 등은 TCC 알림을 통해 사용자 동의를 받는다.
- Secure Enclave/Touch ID/Face ID가 인증·키 보호를 담당한다.

## 배포 채널
- 개발: Xcode + 프로비저닝 프로파일, 테스트는 [[apple-glossary#Sideloading/TestFlight|TestFlight]]로 배포.
- 상용: App Store 심사를 거쳐 배포. 기업용(Enterprise) 배포는 내부 직원용으로만 제한.

## 학습 로드맵
[[apple-architecture-stack]] → [[apple-runtime-and-swift]] → [[apple-interprocess-and-xpc]] → [[apple-sandbox-and-security]] → [[apple-app-lifecycle-and-ui]] → [[apple-rendering-and-media]] → [[apple-networking-and-cloud]] → [[apple-storage-and-filesystems]] → [[apple-boot-flow-and-images]] → [[apple-build-and-distribution]] → [[apple-performance-and-debug]] → [[apple-testing-and-quality]] → [[apple-platform-differences]] → [[apple-history-and-evolution]].
