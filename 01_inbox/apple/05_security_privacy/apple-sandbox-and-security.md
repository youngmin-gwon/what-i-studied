---
title: apple-sandbox-and-security
tags: [apple, security, sandbox, mac, entitlement, tcc, ats]
aliases: []
date modified: 2025-12-18 01:10:00 +09:00
date created: 2025-12-16 16:08:41 +09:00
---

## Sandbox & Security Deep Dive

"왜 내 앱은 옆 앱의 파일을 못 볼까?"
Apple 플랫폼 보안의 핵심은 **"기본 거부(Deny by Default)"**입니다.
이 철학을 이해하지 못하면, 앱 개발 내내 권한 문제로 고통받게 됩니다.

### 💡 왜 이것을 알아야 하나요? (Context)
- **Deny by Default**: 아무리 `FileHandle`을 열어도 에러가 난다면, 코드가 잘못된 게 아닙니다. 샌드박스가 막고 있는 것입니다. 권한(Entitlement)을 요청하지 않으면 아무것도 할 수 없습니다.
- **앱 심사 거절 1순위**: "사용자가 선택하지 않은 파일에 접근해선 안 된다"는 규칙을 어기면 심사에서 바로 떨어집니다.
- **사고 예방**: 만약 내 앱이 뚫려도, 해커는 내 앱의 샌드박스 밖으로 나갈 수 없습니다. 이것이 iOS가 안전한 이유입니다.

---

### 🛡️ Mandatory Access Control (MAC)

리눅스와 달리, Apple의 보안 모델은 **강제적 접근 제어(MAC)**를 따릅니다.
사용자(User)가 허락해도, 시스템 정책(Kernel)이 거부하면 끝입니다.

1. **Sandbox Profile**: 앱이 실행될 때 커널은 해당 앱이 할 수 있는 일(네트워크 연결, 파일 쓰기 등)이 적힌 프로필을 로드합니다.
2. **System Call Hook**: 앱이 `open()`, `connect()` 같은 시스템 콜을 호출하면, TrustedBSD MAC 프레임워크가 이를 가로채서 프로필과 대조합니다.
3. **Check**: 프로필에 허용되지 않은 동작이면 `EPERM` (Operation not permitted) 에러를 뱉고 로그를 남깁니다. (Console.app에서 확인 가능)

---

### 🎟️ Code Signing & Entitlements

"이 앱이 해도 되는 일"을 증명하는 티켓입니다.

#### 1. Code Signing (서명)
앱이 변조되지 않았음(Integrity)을 보장합니다.
- 해커가 바이너리를 수정하면 서명이 깨지고, iOS는 실행을 거부합니다.

#### 2. Entitlements (권한 부여)
앱의 주민등록증 뒤에 붙은 "특수 면허" 스티커입니다.
- **Push Notification**, **iCloud**, **Apple Pay** 등 시스템 리소스를 쓰려면 Apple이 발급한 `Provisioning Profile`에 해당 Entitlement가 명시되어 있어야 합니다.
- **주의**: Xcode 타겟 설정(`Capabilities`)에서 켜지 않으면 API 호출 시 런타임 에러가 발생합니다.

---

### 🌐 Network Security (ATS)

#### 1. App Transport Security (ATS)
iOS는 기본적으로 모든 HTTP 연결을 차단하고, **HTTPS (TLS 1.2+)**만 허용합니다.
- Info.plist에서 `NSAppTransportSecurity` 예외를 추가할 수 있지만, 심사 시 타당한 이유("서버가 내 것이 아님" 등)를 설명해야 합니다.

#### 2. Network Extensions
VPN, DNS Proxy, Content Filter 같은 기능을 구현하려면 단순 서명을 넘어선 **Network Extension Entitlement**가 필요합니다. 이는 Apple의 추가 승인(Allowlist)이 필요할 수 있습니다.

---

### 🖼️ Photo & File Access (Modern Privacy)

#### 1. Limited Photo Library
iOS 14+부터 사용자는 "사진 전체 접근" 대신 **"선택한 사진만 접근(Selected Photos)"**을 고를 수 있습니다.
- 개발자는 `PHPickerViewController`를 써야 합니다.
- **장점**: 권한 팝업 없이도 사용자가 고른 사진을 바로 가져올 수 있습니다. (System-presents UI는 신뢰할 수 있으니까요)

#### 2. Security Scoped Bookmark (macOS/iPadOS)
사용자가 파일을 골라줬어도, 앱을 껐다 켜면 권한이 사라집니다(Sandboxed).
- 파일 URL을 그냥 저장하면 안 되고, **BookmarkData**로 변환하여 영구 권한을 저장해야 합니다.
- 파일에 접근할 때마다 `startAccessingSecurityScopedResource()`를 호출해야 합니다.

```swift
// 파일 접근권 획득
if url.startAccessingSecurityScopedResource() {
    defer { url.stopAccessingSecurityScopedResource() }
    // 파일 읽기/쓰기 수행
}
```

### 🚨 Incident Response (사고 대응)

보안 사고가 났을 때를 대비한 "비상 버튼"이 있어야 합니다.
1. **Server-Side Kill Switch**: 앱에 심각한 보안 구멍이 발견되면, 구버전 앱의 API 호출을 서버에서 전면 차단해야 합니다.
2. **Key Rotation**: API Key나 인증서가 털렸을 때, 서버에서 키를 바꾸고 앱이 새 키를 받아올 수 있는 구조(Config API)를 만들어야 합니다. 하드코딩된 키는 앱 업데이트 전까지 수정 불가능합니다.

### 더 보기
- [[apple-keychain-biometrics]] - 비밀번호와 생체 정보 보호
- [[apple-build-and-distribution]] - 서명과 배포 프로세스
