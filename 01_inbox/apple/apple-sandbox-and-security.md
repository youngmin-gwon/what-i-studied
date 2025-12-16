# Sandbox & Security #apple #security #sandbox

사용자 데이터를 지키기 위한 기본 장치를 쉬운 말로 정리했다. 용어는 [[apple-glossary]].

## 코드 서명과 엔타이틀먼트
- 모든 실행 파일은 서명되어야 하며, 서명 안에는 [[apple-glossary#Entitlement|Entitlement]]가 있다.
- 서명/Entitlement가 없으면 특정 API(네트워크 확장, Health, HomeKit 등)를 쓸 수 없다.

## 샌드박스
- 앱마다 컨테이너(홈 디렉터리)가 있고, 그 밖은 기본적으로 볼 수 없다.
- 파일 접근 예외는 Security-scoped bookmark(파일 선택기), App Groups(공유 컨테이너)로 열 수 있다.
- 네트워크, 카메라, 마이크 등도 샌드박스/[[apple-glossary#TCC|TCC]] 규칙으로 제한된다.

## TCC 권한
- 카메라/마이크/사진/위치/연락처/캘린더/알림/Bluetooth/근처 검색 등은 사용자 팝업을 거쳐야 한다.
- Info.plist에 이유 문구(NSCameraUsageDescription 등)를 적지 않으면 앱이 거절되거나 크래시한다.

## 데이터 보호
- iOS는 기본으로 데이터 보호가 켜져 있어, 잠금 상태에서 접근 불가한 파일 클래스가 있다.
- macOS는 FileVault로 디스크 전체를 암호화할 수 있다.
- Keychain은 민감 데이터를 안전하게 저장한다. Keychain Access Group으로 확장/앱 간 공유 가능.

## 프라이버시 기능
- App Tracking Transparency(ATT)로 광고 식별자 사용을 명시적으로 묻는다.
- Private Relay(아이클라우드+), Mail Privacy Protection 등 OS 레벨 프라이버시 기능이 있다.
- 사진/파일 선택기는 선택된 항목만 넘기고 전체 접근을 막는다.

## 시스템 보호
- SIP(System Integrity Protection, macOS)이 루트 권한도 막는 영역을 보호한다.
- 커널 확장은 제한되고, 가능하면 DriverKit(유저 공간)으로 이동하도록 권장한다.
- [[apple-glossary#Secure Enclave|Secure Enclave]]가 생체인증/키 보호를 맡는다.

## 네트워크 보안
- [[apple-glossary#ATS|ATS]]로 TLS를 기본 강제. 예외는 최소화해야 심사에서 통과한다.
- VPN/프록시/필터링은 Network Extension Entitlement가 필요.

## 이벤트·로그
- 권한 거부/샌드박스 실패는 Console/Crash 로그에 남는다.
- macOS: `spctl`, `codesign`, `syspolicyd` 로그로 서명 문제를 확인.
- iOS: TestFlight/설치 시 서명/프로비저닝 실패는 기기 팝업에 표시.

## 링크
[[apple-architecture-stack]], [[apple-interprocess-and-xpc]], [[apple-app-lifecycle-and-ui]], [[apple-build-and-distribution]].
