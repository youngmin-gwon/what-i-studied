# Build, Signing, Distribution #apple #build #distribution

앱/OS를 빌드하고 배포하는 과정을 쉽게 정리했다. 용어는 [[apple-glossary]].

## 빌드 도구
- Xcode/SwiftPM로 소스 빌드. xcconfig로 설정, Schemes/Configurations로 Debug/Release 분리.
- clang/Swiftc가 코드를 컴파일, ld가 링크, [[apple-glossary#Mach-O|Mach-O]] 바이너리를 만든다.
- [[apple-glossary#dyld|dyld]] Shared Cache로 공용 시스템 프레임워크를 묶어 앱 시작을 빠르게 한다.

## 서명과 프로비저닝
- Developer/Distribution 인증서, Team ID, [[apple-glossary#Provisioning Profile|프로비저닝 프로파일]]을 매칭해야 설치된다.
- [[apple-glossary#Entitlement|Entitlement]]는 프로파일+서명에 포함되어 API 사용 권한을 정한다.
- App Groups/iCloud/HealthKit 등은 별도 Entitlement와 능동적 승인이 필요하다.

## 번들 구조
- .app/.framework/.appex: Info.plist, 실행 파일, 리소스, 서명 정보, [[apple-glossary#DSYM|DSYM]](별도 출력)으로 구성.
- [[apple-glossary#Code Signing|Code Signing]]은 Contents/_CodeSignature/CodeResources에 기록.

## 배포 채널
- App Store: 심사/리뷰 필수. TestFlight(최대 1만 테스터)로 베타 배포.
- Enterprise/Ad Hoc: 내부/제한된 기기에 배포(관리 주의, MDM 권장).
- Sideload(AltStore 등)와 개발자 모드(iOS 17+): 제한적, 사용자 동의 필요.

## OS 빌드
- IPSW/OTA: iOS/iPadOS/watchOS/visionOS 펌웨어 패키지.
- macOS IPSW(Apple Silicon)로 전체 복구/재설치. OTA로 소규모 업데이트.

## 스토어 메타데이터/정책
- 개인정보 항목(Privacy Nutrition Label), ATT 설명, 앱 추적 정책 준수.
- 캡처/설명/연령 등급, 인앱 구매 설정.

## 자동화
- xcodebuild/xcpretty/fastlane로 CI 파이프라인 구성.
- notarization(맥 앱): 서명된 앱을 애플 서버에서 검사/스테이플링.
- Bitcode는 더 이상 필수가 아니지만, dSYMs 업로드는 여전히 필요.

## 링크
[[apple-performance-and-debug]], [[apple-testing-and-quality]], [[apple-sandbox-and-security]], [[apple-history-and-evolution]].
