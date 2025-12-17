---
title: apple-networking-and-cloud
tags: [apple, networking, urlsession, security, internals, network-framework, protocols, operations]
aliases: []
date modified: 2025-12-18 01:30:00 +09:00
date created: 2025-12-16 16:09:23 +09:00
---

## Networking & Cloud Deep Dive

iOS의 네트워킹은 "그냥 API 찌르는 것" 그 이상입니다.
`URLSession`의 깊은 내부 동작(Background Session)부터, BSD Socket을 대체하는 현대적인 `Network.framework`, 그리고 앱의 신뢰성을 지키는 보안(Security)과 운영(Operations)까지 다룹니다.

### 💡 왜 이것을 알아야 하나요? (Context)
- **앱이 백그라운드에서 죽어요**: "다운로드 중에 앱을 나갔더니 끊겼어요." → `Background Session`을 쓰지 않았거나, 시스템이 깨워줬을 때(Delegate) 처리를 제대로 안 했기 때문입니다.
- ** 소켓 통신 (Chat/Streaming)**: 아직도 C언어 `socket()`을 쓰시나요? 이제 애플이 직접 만든 `Network.framework`로 Swift스럽게 소켓을 짜야 합니다. (Wi-Fi ↔ LTE 전환 자동 처리 등 혜택이 엄청납니다.)
- **보안 감사**: "중간자 공격(MITM)에 취약합니다"라는 리포트를 받았다면 `ATS` 예외 처리나 `Certificate Pinning`을 점검해야 합니다.

---

### 📡 Protocols & Basics (프로토콜 선택)

가장 먼저 "어떤 프로토콜로 대화할 것인가?"를 정해야 합니다.

| 프로토콜 | 용도 | 특징 | 비고 |
|:---:|:---:|---|---|
| **HTTP/HTTPS** | REST API, 이미지 | 가장 기본. URLSession이 HTTP/2, 3(QUIC) 자동 지원. | 대부분 이것으로 충분. |
| **WebSocket** | 채팅, 주식 시세 | 양방향 실시간 통신. | Ping/Pong으로 연결 유지 필요. |
| **mDNS (Bonjour)** | 로컬 기기 검색 | Wi-Fi 내 프린터/친구 찾기. | 멀티캐스트 사용. 배터리 소모 주의. |
| **Multipeer** | 근거리 P2P | Wi-Fi/Bluetooth 알아서 조합하여 파일 공유 (AirDrop 방식). | 인터넷 없이 동작 가능. |

---

### 🚀 URLSession Internals

#### 1. Configuration & Life Cycle
- `default`: 디스크 기반 캐시, 쿠키 저장소 사용.
- `ephemeral`: 모든 데이터를 메모리에만 저장 (Secret mode).
- **`background`**: 앱이 종료되어도 시스템 데몬(`nsurlsessiond`)이 다운로드를 계속 수행.

#### 2. Background Transfer (백그라운드 전송)
앱이 Suspended 되거나 Terminated 되어도 다운로드는 계속됩니다. 
**동작 원리**:
1. 앱이 `Background Configuration`으로 세션을 만듭니다.
2. 다운로드를 시작하고 앱이 죽습니다(Terminated).
3. 시스템 데몬(`nsurlsessiond`)이 다운로드를 대신 수행합니다.
4. 완료되면 시스템이 앱을 백그라운드에서 깨웁니다(`application(_:handleEventsForBackgroundURLSession:completionHandler:)`).
5. 앱은 세션을 **다시 연결(Re-connect)**하고 Delegate를 통해 완료 처리를 합니다.

---

### 🌐 Network.framework (Modern Sockets)

기존 BSD Socket을 대체하는 현대적인 전송 계층 프레임워크입니다. `URLSession`도 내부적으로는 이 프레임워크를 사용합니다.

- **User Space Networking**: 커널 오버헤드를 줄이고, 앱 프로세스 내에서 효율적인 처리를 가능하게 합니다.
- **Happy Eyeballs**: IPv4와 IPv6 중 더 빠른 경로를 자동으로 선택합니다.
- **Multipath TCP**: Wi-Fi와 셀룰러 간 핸드오버를 매끄럽게 처리합니다.

```swift
// TCP Connection 예시 (Socket 대체)
let params = NWParameters.tcp
let connection = NWConnection(host: "example.com", port: 80, using: params)
connection.start(queue: .global())
```

---

### 🔒 보안 (Security)

#### 1. ATS (App Transport Security)
Apple 플랫폼은 기본적으로 평문 통신(HTTP)을 차단하고 **HTTPS (TLS 1.2+)**만 허용합니다. `Info.plist` 예외는 정말 불가피할 때만 사용하세요.

#### 2. Certificate Pinning (SSL Pinning)
단순 HTTPS로는 공용 와이파이 등에서 조작된 인증서를 막을 수 없습니다. "내가 아는 그 인증서"인지 확인하기 위해 서버의 공개키를 앱에 심어두고 비교합니다.

---

### 📊 Operations & Monitoring (운영)

네트워크 코드는 "출시 후"가 진짜 시작입니다.

1. **Metrics**: `URLSessionTaskTransactionMetrics`로 DNS, TCP, TLS 시간을 쪼개서 봅니다. "느리다"는 불만의 원인이 '내 서버'인지 '사용자 5G'인지 구분할 수 있습니다.
2. **Success Rate**: HTTP 200 비율뿐만 아니라 "디코딩 실패(Mapping Error)" 비율도 중요합니다. 서버가 200을 줬는데 JSON이 깨져서 앱이 죽는 경우가 많습니다.
3. **Reachability**: `NWPathMonitor`로 "인터넷 끊김"을 감지하고 UI에 보여줍니다. 사용자가 "앱이 고장 났다"고 오해하지 않게 합니다.

### 더 보기
- [[apple-urlsession-deep-dive]] - 실무 코드 레시피 (Async/Await)
- [[apple-offline-and-resilience]] - 오프라인 모드와 재시도 전략
