---
title: apple-security-sandbox
tags: [apple, apple/security, mac, sandbox]
aliases: []
date modified: 2026-04-05 17:45:32 +09:00
date created: 2026-04-05 17:07:43 +09:00
---

## [[mobile-security]] > [[apple-security-sandbox]]

### Apple App Sandbox & MAC

Apple 의 보안 모델은 **강제적 접근 제어(Mandatory Access Control, MAC)**를 기반으로 하며, 앱이 시스템 리소스나 사용자 데이터에 접근하는 것을 커널 수준에서 차단하는 **App Sandbox**가 핵심입니다.

---

#### 🛡️ 기본 철학: Deny by Default

Apple 플랫폼의 모든 앱은 명시적으로 허용되지 않은 상호작용이 불가능합니다.

- 사용자가 직접 파일을 선택(Powerbox)하거나, 권한 매니페스트(Entitlements)에 명시되어야만 리소스 접근이 가능합니다.
- `EPERM` (Operation not permitted) 에러가 발생한다면 코드 논리 오류가 아닌 샌드박스 정책 위반일 확률이 높습니다.

---

#### ⚙️ 동작 메커니즘

1. **Sandbox Profile**: 앱 실행 시 커널은 해당 앱이 수행 가능한 동작(네트워크, 파일 읽기/쓰기 등)이 정의된 프로필을 로드합니다.
2. **TrustedBSD MAC Framework**: 프로세스가 시스템 콜(`open`, `connect` 등)을 호출하면 커널 프레임워크가 이를 가로채 프로필과 대조합니다.
3. **Hardened Runtime (macOS)**:
    - 프로세스 인젝션 및 서명되지 않은 코드 로드를 차단합니다.
    - `Library Validation`: Apple 이나 개발자 본인이 서명한 라이브러리만 로드하도록 지장합니다.

---

#### 📂 파일 접근 및 북마크 (Security Scoped Bookmarks)

샌드박스 환경에서는 사용자가 `NSOpenPanel` 등으로 선택한 파일이라도, 앱을 재시작하면 접근 권한이 소실됩니다.

**해결책: Security-Scoped Bookmarks**

- 파일 URL 을 `BookmarkData` 로 변환하여 영구 보존합니다.
- 다시 사용할 때는 `URL.startAccessingSecurityScopedResource()` 를 호출하여 일시적으로 권한을 획득해야 합니다.

```swift
if url.startAccessingSecurityScopedResource() {
    defer { url.stopAccessingSecurityScopedResource() }
    // 파일 작업 수행
}
```

#### 연관 문서
- [[apple-security-entitlements]] - 권한 증명 시스템
- [[apple-security-tcc-compliance]] - 프라이버시 승인 시스템
- [[mobile-advanced-security-tips]] - RASP 및 우회 방어
