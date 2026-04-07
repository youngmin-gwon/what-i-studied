---
title: apple-deep-links
tags: [apple, ios, universal-links, deep-link]
aliases: [iOS 유니버설 링크]
date modified: 2026-04-07 10:55:00 +09:00
date created: 2026-04-05 14:10:00 +09:00
---

## [[apple-foundations]] > [[apple-deep-links]]

### iOS Deep Linking: URL Schemes & Universal Links

iOS 에서 앱 외부의 URL 을 통해 앱으로 진입하고 특정 상태로 분기하는 라우팅 메커니즘을 분석합니다.

---

#### 💡 1. 딥링크의 두 종류 (Deep Link Types)

| 종류 | 프로토콜 | 특징 | 보안성 |
| :--- | :--- | :--- | :--- |
| **Custom URL Scheme** | `myapp://` | 구현이 매우 간단함 | ❌ 중복 등록(Hijacking) 가능 |
| **Universal Links** | `https://` | 웹 URL 과 동일하게 동작 | ✅ HTTPS 도메인 인증 기반 (강력 권장) |

---

#### 🌐 2. Universal Links (강력 권장)

Apple 은 보안을 위해 HTTPS 기반의 **Universal Links**를 사용하도록 권장합니다.

- **AASA 파일**: 서버의 `.well-known/apple-app-site-association` 파일에 앱의 ID (TeamID.BundleID) 를 명시.
- **Associated Domains**: Xcode 의 `Signing & Capabilities` 에서 앱이 허용할 도메인을 활성화.
- **동작**: 시스템이 HTTPS 링크를 클릭하면 브라우저를 거치지 않고 직접 해당 앱을 즉시 실행.

---

#### 🛠️ 3. SwiftUI & UIKit 에서의 처리

- **UIKit**: `SceneDelegate` 의 `scene(_:continue:restorationHandler:)` 에서 처리.
- **SwiftUI**: `.onOpenURL { url in ... }` modifier 를 사용하여 간결하게 처리 가능.

---

#### 🔍 4. 테스트 기술

- **Link Checking**: Xcode 의 `Developer App` 섹션에서 유니버설 링크 진단 도구 제공.
- **CLI**: `xcrun simctl openurl booted "https://myapp.com/path"` 

---

#### 📚 See Also
- [[android-deep-links]] - 안드로이드 앱 링크와의 비교
- [[apple-foundations]] - Apple 보안 철학 (Default Deny)
- [[mobile-security]] - 통합 모바일 보안 가이드
