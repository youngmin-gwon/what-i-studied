# Network Debug & Recipes #apple #network #debug #common

네트워크 문제를 찾고, 자주 쓰는 패턴을 쉽게 모았다. 용어는 [[apple-glossary]].

## 로그와 도구
- OSLog/Logger로 구조화된 로그를 남긴다. 민감 정보는 넣지 않는다.
- Instruments Network/Packet Logger: RTT, Throughput, 재전송, HTTP 상태 확인.
- `log stream --predicate 'subsystem == "com.apple.network"'`로 시스템 네트워크 로그 보기.
- `tcpdump`/Wireshark: 저수준 패킷 분석(개발/테스트 프로파일에서).
- APNs 디버깅: 토큰/환경(샌드/프로덕션) 구분, 응답 status code 확인.

## 자주 쓰는 패턴
- Retry with backoff: 1s, 2s, 4s… 최대 N회. 네트워크/서버 오류 구분.
- Circuit breaker: 실패가 쌓이면 잠시 요청을 막고 캐시/오프라인 모드로 전환.
- Offline queue: POST/PUT을 로컬에 기록 후 연결 회복 시 전송.
- Conditional GET: ETag/If-Modified-Since로 불필요한 다운로드 줄이기.
- Pagination/Streaming: 큰 목록은 페이지나 스트리밍으로 나눈다.

## URLSession 팁
- Background configuration: 대용량 업/다운로드. 시스템이 앱을 깨워 완료 콜백 제공.
- Ephemeral: 쿠키/캐시 없음. 민감 세션에 사용.
- Delegates: 인증서 핀닝, challenge 응답, 업/다운로드 진행률.
- HTTP/3: 자동 협상. 서버가 지원하면 빠른 연결.

## Network.framework 팁
- NWConnection/NWListener로 TCP/UDP/QUIC를 직접 다룰 수 있다.
- NWPathMonitor로 경로 상태를 구독. 변화에 따라 품질/전략 전환.
- NWBrowser로 Bonjour 서비스 탐색.

## WebSocket
- Ping/Pong 주기 설정으로 연결 유지. 백그라운드 제한 시 연결이 끊길 수 있음.
- 큰 메시지는 청크/압축, JSON 대신 바이너리 프로토콜 고려.

## 근거리 통신
- MultipeerConnectivity: 세션 암호화, 피어 ID 교체 시 재연결 처리.
- CoreBluetooth: 스캔/광고 제한, 권한/전력 고려. Background 모드 필요 시 Info.plist 설정.

## 에러 분류
- 네트워크 없음: 오프라인 메시지/리트라이 UI.
- DNS 실패: 잠시 대기 후 재시도, 캐시 확인.
- TLS 오류: ATS/인증서/시간 설정 확인.
- 서버 오류(5xx): 사용자 안내 + 재시도.
- 클라이언트 오류(4xx): 요청/인증 토큰/권한 확인.

## 보안·프라이버시 검증
- 토큰/개인정보가 로그/URL 쿼리에 남지 않도록 확인.
- ATS 예외/핀닝이 최신 정책과 맞는지 검토.
- Keychain에 저장된 자격 증명은 필요 시만 꺼내 쓰고, 앱 종료 후 메모리에서 지운다.

## 성능 최적화 사례
- 이미지 CDN: 기기 크기/밀도에 맞게 URL 파라미터로 리사이즈.
- 요청 묶기: 여러 작은 요청을 한 번에(배치) 보내 왕복을 줄인다.
- 프리페치: 사용자가 곧 볼 화면의 데이터를 미리 요청.
- QoS: UI 업데이트는 high, 백그라운드 동기는 utility/backgroud로.

## 테스트 시나리오
- 네트워크 없음/느림/간헐/고 RTT/패킷 드롭/Proxy/사설 CA.
- Low Data/Low Power Mode, 셀룰러 vs 와이파이 스위치, 로밍.
- 백그라운드 전송 중 앱 강제 종료/재시작.

## 체크리스트
- 재시도 정책이 서버·배터리·데이터 비용에 맞는가?
- 오프라인 상태를 잘 표시하고, 큐잉/캐시 전략이 있는가?
- 인증서/ATS/핀닝 설정이 최신이고 심사 조건을 만족하는가?
- 푸시 알림/백그라운드 작업이 정책에 맞게 제한되어 있는가?

## 링크
[[apple-network-basics]], [[apple-networking-and-cloud]], [[apple-performance-and-debug]], [[apple-sandbox-and-security]].
