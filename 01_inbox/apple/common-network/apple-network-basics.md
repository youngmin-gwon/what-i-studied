# Network Basics (공통) #apple #network #common

이 문서는 iOS/iPadOS/macOS/watchOS/visionOS/tvOS 모두에 공통된 네트워크 원리를 쉽게 설명한다. 모르는 말은 [[apple-glossary]].

## 네트워크는 왜 중요할까?
- 앱이 서버와 이야기하려면 신뢰할 수 있는 통로가 필요하다.
- 배터리/데이터를 아끼면서도 끊김 없이 연결해야 한다.
- 보안(암호화)과 프라이버시(최소한의 데이터만 보내기)가 기본 규칙이다.

## 기본 규칙 세 가지
1) [[apple-glossary#ATS|ATS]]: HTTPS를 기본으로. 낮은 TLS나 평문은 막힌다(예외는 Info.plist에 명시).
2) [[apple-glossary#APNs|APNs]]: 푸시 알림은 애플 서버를 통해 온다. 토큰으로 기기를 식별한다.
3) [[apple-glossary#Entitlement|Entitlement]]: VPN/프록시/네트워크 확장처럼 강한 권한은 서명에 권한을 적어야 쓸 수 있다.

## 연결 상태 읽기
- NWPathMonitor/Reachability로 “연결됨/셀룰러/와이파이/제한”을 본다.
- Low Data Mode/Low Power Mode에서는 큰 전송을 미루거나 품질을 낮춘다.
- watchOS는 iPhone 경유, 자체 셀룰러, Wi‑Fi를 상황에 따라 바꾼다. visionOS는 공간 영상 스트리밍 시 대역폭이 크다.

## 데이터 절약 팁
- 캐시를 적극 사용: URLCache/HTTP 캐시 헤더, ETag/If-None-Match.
- 이미지/동영상은 해상도를 조정하고, 필요할 때만 내려받는다.
- 업로드는 백그라운드 전송(Background URLSession)으로 실패 시 자동 재시도.

## 신뢰와 인증서
- 기본 신뢰 저장소를 따른다. 핀닝이 필요하면 NWProtocolFramer/URLSessionDelegate에서 검증.
- 기업/테스트 환경의 자체 서명 인증서는 기기에 프로필로 설치하거나 ATS 예외로만 사용.

## 프로토콜 선택
- HTTP/HTTPS: 대부분의 API. HTTP/2, HTTP/3(QUIC) 자동 지원.
- WebSocket: 양방향 실시간. Ping/Pong 유지 관리 필요.
- mDNS/Bonjour: 근거리 서비스 검색. 멀티캐스트 트래픽이므로 배터리/네트워크 제약 고려.
- BLE: 짧은 거리/저전력 데이터. 권한/광고 제한 존재.

## 백그라운드 규칙
- iOS/watchOS: 푸시나 백그라운드 세션 외에는 임의 장시간 연결이 허용되지 않는다.
- Background Modes(오디오/VoIP/위치/BLE)만 장기 실행 가능. 남용하면 제한/심사 거절.
- macOS는 덜 제한적이지만 App Nap/에너지 정책을 따른다.

## 에러 처리
- 네트워크는 항상 실패할 수 있다. 타임아웃/재시도/백오프를 설계한다.
- 오프라인 큐(Outbox) 패턴으로 나중에 다시 보낼 일을 모아둔다.
- 사용자가 데이터 비용을 알 수 있도록 상태(오프라인/느림/과금)를 UI에 보여준다.

## 보안/프라이버시 기본
- 최소 데이터만 전송, 민감 데이터는 항상 TLS + 서버 검증.
- 토큰/비밀번호는 절대 평문/로그에 남기지 말고 [[apple-glossary#Keychain|Keychain]]에 저장.
- 네트워크 로깅은 개발 빌드만, 사용자 동의 후 제한적으로.

## 성능 측정
- Instruments Network/Packet Logger로 RTT/대역폭/재전송을 본다.
- MetricsKit/OSLog를 사용해 실제 사용자 환경의 성공률/지연을 집계한다.
- 큰 다운로드는 프로그레스/취소/재개를 지원해 사용자 경험을 높인다.

## 플랫폼 별 메모
- iOS/iPadOS: 셀룰러 비용/백그라운드 제한이 가장 중요.
- macOS: 프록시/VPN/소켓 API가 가장 넓게 허용. 그러나 TCC/샌드박스가 파일/네트워크를 제한할 수 있다.
- watchOS: 작은 배터리, 짧은 세션. iPhone 동반 여부를 확인 후 전략 변경.
- visionOS: 공간 영상/스트리밍은 대역폭 크며, 프레임 지연이 경험에 영향을 준다.
- tvOS: 큰 화면 스트리밍에 최적화. 앱 크기/온디맨드 리소스 정책을 지켜야 한다.

## 체크리스트
- ATS 예외는 정말 필요한가? → Info.plist에서 최소 범위로 설정.
- 백그라운드 모드는 오남용하지 않았나? → 시스템이 종료할 수 있다.
- 재시도/백오프/오프라인 큐가 있는가? → 사용자 데이터 손실 방지.
- 푸시 토큰/디바이스 ID를 안전하게 다루나? → Keychain + 최소 전송.
- 사용자에게 상태를 잘 알리나? → 오프라인/저품질 모드 안내.

## 링크
[[apple-networking-and-cloud]], [[apple-sandbox-and-security]], [[apple-build-and-distribution]], [[apple-performance-and-debug]].
