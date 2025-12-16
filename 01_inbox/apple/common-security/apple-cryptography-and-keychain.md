# Cryptography & Keychain (공통) #apple #crypto #keychain

암호화와 키 보관을 쉽게 정리했다. 모르는 말은 [[apple-glossary]].

## 키 보관
- [[apple-glossary#Keychain|Keychain]]은 비밀번호/토큰/인증서를 안전하게 저장하는 금고.
- Access Group으로 앱/확장이 키를 공유할 수 있다(서명/Entitlement 필요).
- iCloud Keychain을 쓰면 기기 간 동기화 가능(사용자 동의 필요).

## Secure Enclave
- Touch ID/Face ID와 연동된 별도 칩/프로세서. 키를 Enclave 밖으로 내보내지 않는다.
- 하드웨어 제한 수량/속도를 고려해야 한다(키 생성/서명은 비싸다).

## 데이터 보호 클래스
- 파일은 보호 클래스를 설정할 수 있다(잠금 시 접근 불가/첫 잠금 해제 후 가능 등).
- 민감 데이터는 Complete Protection으로, 캐시/썸네일 등은 덜 엄격한 클래스로.

## 네트워크 암호화
- [[apple-glossary#ATS|ATS]]로 TLS 강제. 최소 TLS 1.2 이상.
- 인증서 핀닝은 필요 최소 범위로. 핀 변경/만료 대응 계획을 세운다.

## 암호화 API
- CryptoKit: 현대적 API, 대칭/비대칭/해시/난수.
- CommonCrypto: C 기반 레거시, 여전히 많이 쓰임.
- Secure Transport/Network.framework: TLS/보안 연결.

## 비밀번호/토큰 관리
- 토큰은 Keychain에, 메모리에서는 필요 시만 유지.
- 하드코딩 금지. 빌드 설정/서버에서 받아오는 방식 사용.
- 자동 잠금/로그아웃 정책(앱 잠금/백그라운드) 고려.

## 백업/이동성
- Keychain 항목은 기본적으로 백업/이전된다. 민감 항목은 비이전 옵션(AccessibleWhenPasscodeSetThisDeviceOnly) 고려.
- 데이터 보호 클래스로 파일 백업/이전 시점에 대한 정책도 결정.

## 감사/로그
- 암호 키/토큰을 로그에 남기지 않는다.
- 크립토 오류는 범위만 기록하고, 실제 값은 숨긴다.

## 테스트
- 시뮬레이터/실기기 모두에서 Keychain 동작 확인(시뮬레이터는 다를 수 있다).
- Face ID/Touch ID 가용성, 실패/잠금/바이오 인증 변경 흐름 테스트.

## 사고 대응
- 키가 유출/의심되면 서버에서 폐기/재발급. 앱 업데이트로 새 핀/키를 배포.
- 비밀번호 재설정/디바이스 분실 시 계정 보호 흐름 준비.

## 링크
[[apple-security-models]], [[apple-network-basics]], [[apple-sandbox-and-security]], [[apple-performance-and-debug]].
