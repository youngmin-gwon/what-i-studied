---
title: apple-deep-links
tags: [apple, apple/services, deep-link, ios, universal-links]
aliases: ["URL Scheme 은 다른 앱이 선점할 수 있고 Universal Link 는 도메인 소유 증명을 요구한다", "Universal Links", "iOS 유니버설 링크"]
date modified: 2026-04-07 10:55:00 +09:00
date created: 2026-04-05 14:10:00 +09:00
---

## URL Scheme 은 다른 앱이 선점할 수 있고 Universal Link 는 도메인 소유 증명을 요구한다

iOS 에서 앱 외부의 URL 을 통해 앱으로 진입하고 특정 상태로 분기하는 라우팅 메커니즘을 분석합니다.

---

### 💡 1. 딥링크의 두 종류 (Deep Link Types)

| 종류 | 프로토콜 | 특징 | 보안성 |
| :--- | :--- | :--- | :--- |
| **Custom URL Scheme** | `myapp://` | 구현이 매우 간단함 | ❌ 중복 등록(Hijacking) 가능 |
| **Universal Links** | `https://` | 웹 URL 과 동일하게 동작 | ✅ HTTPS 도메인 인증 기반 (강력 권장) |

---

### 🌐 2. Universal Links (강력 권장)

Apple 은 보안을 위해 HTTPS 기반의 **Universal Links**를 사용하도록 권장합니다.

- **AASA 파일**: 서버의 `.well-known/apple-app-site-association` 파일에 앱의 ID (TeamID.BundleID) 를 명시.
- **Associated Domains**: Xcode 의 `Signing & Capabilities` 에서 앱이 허용할 도메인을 활성화.
- **동작**: 시스템이 HTTPS 링크를 클릭하면 브라우저를 거치지 않고 직접 해당 앱을 즉시 실행.

---

### 🛠️ 3. SwiftUI & UIKit 에서의 처리

- **UIKit**: `SceneDelegate` 의 `scene(_:continue:restorationHandler:)` 에서 처리.
- **SwiftUI**: `.onOpenURL { url in ... }` modifier 를 사용하여 간결하게 처리 가능.

---

### 🔍 4. 테스트 기술

- **Link Checking**: Xcode 의 `Developer App` 섹션에서 유니버설 링크 진단 도구 제공.
- **CLI**: `xcrun simctl openurl booted "https://myapp.com/path"` 

---

### 관찰 가능한 증거

```bash
# AASA 파일을 기기가 실제로 가져왔는지
log stream --device --predicate 'subsystem == "com.apple.swcd"' --info

# 시뮬레이터에서 링크 열기
xcrun simctl openurl booted "https://example.com/items/42"

# 서버의 AASA 파일이 올바른지 (리다이렉트 없이 200, JSON, Content-Type)
curl -sIL https://example.com/.well-known/apple-app-site-association
```

**세 가지 진입 상태를 모두 테스트한다.** 하나만 구현하면 나머지에서 조용히 실패한다.

| 앱 상태 | 진입점 |
| :--- | :--- |
| 실행 중 / 정지 | `scene(_:continue:)` 또는 `.onOpenURL` |
| **완전 종료** | `scene(_:willConnectTo:options:)` 의 `connectionOptions.userActivities` |

세 번째가 가장 많이 누락된다. **앱을 강제 종료한 뒤 링크를 탭하는 테스트**를 반드시 한다.

`applinks:` 는 entitlement 이므로 서명에 봉인된다. 실기기에서만 실패한다면 이것을 먼저 확인한다.

```bash
codesign -d --entitlements :- MyApp.app | grep -A3 associated-domains
```

### 📚 See Also
- [android-deep-links](../../android/02_app_framework/navigation/intents-and-deep-links/android-deep-links.md) - 안드로이드 앱 링크와의 비교
- [apple-foundations](../00_foundations/apple-foundations.md) - Apple 보안 철학 (Default Deny)
- [mobile-security](../../mobile-security.md) - 통합 모바일 보안 가이드

공식 문서: [Supporting universal links in your app](https://developer.apple.com/documentation/xcode/supporting-universal-links-in-your-app)
