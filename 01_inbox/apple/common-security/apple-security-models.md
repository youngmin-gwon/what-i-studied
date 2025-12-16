# Security Models (공통) #apple #security #common

애플 플랫폼이 지키는 보안 원칙을 쉽게 풀어쓴다. 모르는 말은 [[apple-glossary]].

## 신뢰 사슬
- 부팅부터 앱 실행까지 모든 단계가 [[apple-glossary#Code Signing|서명]] 검증을 거친다.
- iBoot/커널/시스템 볼륨(SSV)은 서명/봉인되어 변조를 막는다.
- 앱/확장/프레임워크도 서명과 [[apple-glossary#Entitlement|Entitlement]] 검사를 통과해야 한다.

## 샌드박스
- 앱마다 컨테이너가 따로 있고, 파일/네트워크/하드웨어 접근은 제한된다.
- Info.plist + TCC 팝업 + 샌드박스 프로필이 함께 작동한다.
- App Groups/파일 선택기/보안 북마크로 필요한 공유만 허용한다.

## 권한(TCC)
- 카메라/마이크/사진/연락처/캘린더/리마인더/블루투스/알림/위치 등은 사용자 동의가 필요.
- 설명 문구를 Info.plist에 작성, 사용자에게 왜 필요한지 명확히 알린다.
- 거부/제한 상태를 고려해 UI/기능을 설계한다.

## 키/암호화
- [[apple-glossary#Secure Enclave|Secure Enclave]]가 Touch ID/Face ID/키 보호를 담당.
- Keychain은 앱/확장 공유를 위해 Access Group을 사용.
- 데이터 보호 클래스(Data Protection Class)로 파일 접근을 잠금 상태와 연결.

## 네트워크 보안
- [[apple-glossary#ATS|ATS]]로 TLS 강제. 예외는 최소화.
- VPN/프록시/필터링은 Network Extension Entitlement 요구.
- 인증서 핀닝/토큰 관리로 중간자 공격을 방지.

## 프라이버시
- App Tracking Transparency(ATT), Privacy Nutrition Label로 사용자에게 데이터 사용을 알림.
- 위치/사진/연락처는 필요한 최소 범위만 요청(최근/한 번만/선택 항목 등).

## 안전한 개발 습관
- 입력 검증/직렬화, SQL/명령 주입 방지.
- 로그에 민감 정보 남기지 않기. 디버그/릴리스 설정 구분.
- 타사 SDK 권한/데이터 수집을 검토하고, 프라이버시 라벨에 반영.

## 보안 테스트
- 정적 분석(Clang Static Analyzer, SwiftLint 규칙), 취약점 스캐닝.
- 동적 테스트: Jailbreak/개발자 모드 환경에서 샌드박스/권한 우회 시도.
- 침투 테스트/위협 모델링: 어떤 자산이 중요하고 어떤 공격 경로가 있는지 가정.

## 사건 대응
- 크래시/로그에서 보안 관련 오류(권한 거부/서명 실패) 확인.
- 키/토큰 유출 시 서버 무효화/재발급 절차 준비.
- 사용자에게 알릴 계획(규제 요구사항 포함) 마련.

## 플랫폼 별 주의
- macOS: SIP/노타리제이션/Gatekeeper. 샌드박스 앱과 비샌드박스 앱의 권한이 다르다.
- iOS/watchOS: 루트 접근이 불가, 백그라운드/파일 접근이 강하게 제한.
- visionOS: 카메라/공간 맵 데이터는 매우 민감, 접근 범위가 엄격히 제한.

## 링크
[[apple-sandbox-and-security]], [[apple-privacy-and-tcc-details]], [[apple-cryptography-and-keychain]], [[apple-network-basics]].
