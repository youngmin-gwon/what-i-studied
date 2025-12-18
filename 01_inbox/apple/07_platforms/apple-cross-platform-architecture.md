---
title: apple-cross-platform-architecture
tags: [apple, cross-platform, architecture, spm, uikit, appkit]
aliases: []
date modified: 2025-12-18 00:10:00 +09:00
date created: 2025-12-18 00:10:00 +09:00
---

## Cross-Platform Architecture

"Write Once, Run Anywhere"는 자바의 슬로건이지만, Apple 생태계에서도 반은 맞습니다.
iOS 앱을 조금만 고치면 iPadOS, macOS, 심지어 visionOS까지 확장할 수 있습니다.
핵심은 **"공유할 것(Logic)"과 "분리할 것(UI)"을 명확히 하는 것**입니다.

### 💡 왜 이것을 알아야 하나요? (Context)
- **Universal Purchase**: 앱 하나만 사면 아이폰/맥/워치에서 다 쓸 수 있습니다. 이는 사용자 경험에 엄청난 이점입니다.
- **Maintenance**: 플랫폼마다 코드를 복사&붙여넣기 하면 버그 수정도 4번 해야 합니다. Core 로직을 하나로 모아야 합니다.
- **Mac Catalyst vs Native**: 아이패드 앱을 그대로 맥에 띄울지(Catalyst), 아니면 진짜 맥 앱(AppKit)을 만들지 결정해야 합니다.

---

### 📦 Logic Sharing via Swift PM

가장 좋은 방법은 **비즈니스 로직을 별도의 Swift Package로 분리**하는 것입니다.

```
MyProject/
├── App/
│   ├── iOS/
│   ├── macOS/
│   └── watchOS/
└── Core/ (Swift Package)
    ├── Models/ (Codable, Entity)
    ├── Networking/ (API Client)
    └── ViewModels/ (ObservableObject)
```

- **Imports**: `Core` 패키지 안에서는 `UIKit`이나 `SwiftUI` 같은 UI 프레임워크 임포트를 최소화하세요. 순수 Swift 로직일수록 재사용성이 높습니다.

---

### 🎨 UI Adaptation Strategies

#### 1. SwiftUI (The Best Choice)
SwiftUI는 태생적으로 크로스 플랫폼입니다. `List`, `NavigationStack`은 각 OS에 맞는 모습으로 자동 렌더링됩니다.

#### 2. Preprocessor Macros (`#if os`)
불가피하게 플랫폼별 코드가 필요할 때 사용합니다.

```swift
func copyToClipboard(_ text: String) {
    #if os(iOS) || os(visionOS)
    UIPasteboard.general.string = text
    #elseif os(macOS)
    NSPasteboard.general.clearContents()
    NSPasteboard.general.setString(text, forType: .string)
    #endif
}
```

#### 3. UX Patterns
- **iOS**: 터치 중심. 내비게이션 바, 탭 바.
- **macOS**: 마우스/키보드 중심. 메뉴 바, 사이드바, 멀티 윈도우.
- **visionOS**: 시선 중심. 윈도우 밖으로 튀어나오는 Ornaments.

**전략**: 뷰모델(VM)은 공유하되, 뷰(View) 파일은 `LoginView_iOS.swift`, `LoginView_Mac.swift` 처럼 나누는 것이 깔끔할 때가 많습니다.

---

### 🛍️ App Bundle & Target

Xcode 프로젝트 하나에 여러 타겟(Target)을 둡니다.

- **Bundle ID**: `com.example.app` 하나로 통일하면 스토어에서 하나의 앱으로 인식됩니다(Universal).
- **xcconfig**: 빌드 설정 파일로 버전 번호나 API 키를 통합 관리하세요.

### 더 보기
- [apple-build-and-distribution](../05_security_privacy/apple-build-and-distribution.md) - 타겟별 빌드 및 배포 설정
- [apple-swiftui-deep-dive](../02_ui_frameworks/apple-swiftui-deep-dive.md) - SwiftUI의 플랫폼별 동작 차이
