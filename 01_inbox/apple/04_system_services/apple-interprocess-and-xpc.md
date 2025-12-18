---
title: apple-interprocess-and-xpc
tags: [apple, ipc, xpc, security, extensions, app-groups]
aliases: []
date modified: 2025-12-17 21:30:00 +09:00
date created: 2025-12-16 16:08:27 +09:00
---

## Interprocess Communication & XPC

iOS/macOS의 "보이지 않는 접착제" XPC(Cross Process Communication)입니다.
현대의 앱은 하나의 덩어리(Monolithic)가 아니라, 본체와 수많은 확장(Extensions)이 **XPC**로 연결된 연합체입니다.

### 💡 왜 이것을 알아야 하나요? (Context)
- **앱 확장(App Extension)**: 위젯, 공유 시트, 알림 서비스 확장 등은 모두 **별도의 프로세스**입니다. 이들이 메인 앱과 데이터를 주고받는 유일한 통로가 XPC입니다.
- **안전성(Stability)**: 사파리에서 탭 하나가 죽어도 브라우저 전체가 꺼지지 않죠? 탭마다 별도 XPC 서비스로 격리했기 때문입니다. 내 앱도 무거운 작업을 XPC로 분리하면 메인 앱의 크래시를 막을 수 있습니다.
- **보안(Security)**: "권한 분리(Privilege Separation)". 메인 앱은 권한이 많고, XPC 서비스는 권한을 최소화하여 해킹 당해도 피해를 줄일 수 있습니다.

---

### 📡 XPC 동작 원리 (Internals)

XPC는 Mach Message를 기반으로 한 고수준 객체지향 IPC입니다.

#### 1. Connection Lifecycle
`NSXPCConnection` 객체가 전화선 역할을 합니다.
1. **Resume**: 연결은 생성 시 `suspended` 상태입니다. 반드시 `resume()`을 호출해야 통신이 시작됩니다.
2. **Invalidation**: 한쪽 프로세스가 죽거나 연결을 끊으면 `invalidationHandler`가 호출됩니다. 이때는 연결 객체를 버리고 새로 만들어야 합니다.

#### 2. Interface (Protocol)
Swift의 프로토콜(`@objc protocol`)을 사용하여 통신 규약을 정의합니다.
- 메서드의 파라미터와 리턴 타입은 반드시 `NSSecureCoding`을 준수해야 합니다. (보안상의 이유로 임의의 객체를 보낼 수 없음)

---

### 🛠️ 실무 구현 패턴

#### 1. App Extension과 통신
위젯이나 공유 확장은 메인 앱과 직접 통신할 수 없습니다. 대신 `App Group`을 공유 스토리지로 사용하거나, `NSUserDefaults(suiteName: ...)`를 씁니다.
실시간 통신이 필요할 때는 `CFNotificationCenter`(Darwin Notification)를 쓰기도 합니다.

#### 2. XPC Service (macOS)
macOS 앱은 앱 번들 안에 별도의 XPC 서비스를 내장할 수 있습니다.

```swift
// Shared Protocol
@objc protocol ImageProcessingServiceProtocol {
    func processImage(data: Data, reply: @escaping (Data?) -> Void)
}

// Main App (Client)
let connection = NSXPCConnection(serviceName: "com.example.image-service")
connection.remoteObjectInterface = NSXPCInterface(with: ImageProcessingServiceProtocol.self)
connection.resume()

let service = connection.remoteObjectProxy as! ImageProcessingServiceProtocol
service.processImage(data: rawData) { processedData in
    // 비동기 응답 처리 (메인 앱은 그동안 멈추지 않음)
}
```

#### 3. Error Handling
XPC는 언제든 끊길 수 있습니다. (예: 시스템이 메모리 부족으로 서비스를 죽임)
`remoteObjectProxyWithErrorHandler`를 사용하여 반드시 에러 처리를 해야 합니다.

```swift
let service = connection.remoteObjectProxyWithErrorHandler { error in
    print("XPC 연결 실패: \(error)") // 서비스가 죽었거나 연결 불가
} as! ImageProcessingServiceProtocol
```

---

### 🧱 보안 메커니즘 (Entitlements)

XPC가 강력한 이유는 **"아무나 연결할 수 없다"**는 점입니다.
- **Code Signing**: 연결을 요청하는 프로세스가 "진짜 내 앱"인지 서명을 확인합니다.
- **Audit Token**: 연결 수락 여부를 결정할 때, 상대방의 PID, UID, Entitlement를 검사할 수 있습니다.

### 더 보기
- [apple-sandbox-and-security](../05_security_privacy/apple-sandbox-and-security.md) - 샌드박스가 IPC를 차단하는 원리
- [apple-storage-and-filesystems](../03_data_networking/apple-storage-and-filesystems.md) - App Group을 이용한 파일 공유
