# Networking & Cloud #apple #networking #cloudkit

네트워크와 클라우드 연동을 쉽게 정리했다. 용어는 [[apple-glossary]].

## 기본 규칙
- [[apple-glossary#ATS|ATS]]로 HTTPS를 기본 강제. 예외가 필요하면 Info.plist에 이유를 쓴다.
- [[apple-glossary#APNs|APNs]]로 푸시 알림을 받고, Background App Refresh/Push를 활용한다.
- QoS/에너지 정책을 따라 백그라운드 네트워크를 제한한다.

## 주요 프레임워크
- URLSession: 일반 HTTP/HTTPS, 백그라운드 전송, 다운로드 재개.
- Network.framework: TCP/UDP/QUIC, 연결 상태 모니터링, Path 상태.
- MultipeerConnectivity: 근거리 피어 발견/통신.
- CloudKit: iCloud 데이터베이스/자산 저장/푸시 동기화.
- CoreBluetooth: BLE 스캔/연결(권한 필요).
- CallKit/PushKit: VoIP 푸시와 통화 UI 연동.

## 백그라운드 정책
- 백그라운드 세션(Background URLSession)은 시스템이 적절한 시점에 전송한다.
- Push-to-start(Background Push, VoIP push)는 제한적으로만 허용되며, 남용 시 제한된다.
- Low Data Mode/Low Power Mode에서는 대역폭/주기를 줄여야 한다.

## 보안
- ATS/핀닝을 적용해 중간자 공격을 줄인다.
- VPN/프록시는 Network Extension Entitlement가 필요.
- 키/토큰은 Keychain에 저장하고, Secure Enclave를 사용할 수 있으면 활용한다.

## 성능
- HTTP/3/QUIC 사용 시 지연이 줄 수 있다. URLSession은 자동으로 지원.
- Cache 정책을 적절히 설정해 중복 다운로드를 줄인다.
- 측정: Instruments Network, Packet Logger, `tcpdump`, MetricsKit.

## 클라우드 시나리오
- CloudKit 공유/구독으로 실시간 동기화.
- iCloud Drive 파일은 FileProvider와 연계, on-demand 다운로드/업로드.
- 페어링된 기기 간(Watch/iPhone) 연결은 WCSession/Connectivity로 처리.

## 디버깅
- `nw_path_monitor`로 네트워크 가능 상태 확인.
- `log stream --predicate 'subsystem == "com.apple.network"'`로 네트워크 스택 로그.
- APNs: 디바이스 토큰, 환경(샌드/프로덕션) 구분, 알림 payload 제한 확인.

## 링크
[[apple-sandbox-and-security]], [[apple-architecture-stack]], [[apple-build-and-distribution]], [[apple-performance-and-debug]].
