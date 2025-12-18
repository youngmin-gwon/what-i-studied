---
title: apple-platform-differences
tags: [apple, platforms, cross-platform, ios, macos, visionos]
aliases: []
date modified: 2025-12-17 17:10:00 +09:00
date created: 2025-12-16 16:11:10 +09:00
---

## Platform Differences & Code Sharing

iOS, iPadOS, macOS, watchOS, visionOS... 애플의 생태계는 넓지만 **근본(Core)**은 공유합니다.
이 문서는 각 플랫폼의 결정적인 차이점과, 이를 극복하고 **코드를 효율적으로 공유하는 전략**을 다룹니다.

### 💡 왜 이것을 알아야 하나요? (Why it matters)
- **생산성**: "iPhone 앱을 만들었는데, iPad랑 Mac 버전도 내고 싶어요."라고 할 때 처음부터 다시 만들지 않으려면 설계 단계에서 공통점과 차이점을 알아야 합니다.
- **UX 품질**: 마우스(Mac)와 터치(iPhone)는 근본적으로 다릅니다. 이를 무시하고 코드를 100% 공유하면 "폰 앱을 억지로 늘려놓은 Mac 앱"이 됩니다.

---

### 🌍 플랫폼별 핵심 특징 (The Differences)

#### 1. iOS (The Touch Native)
- **입력**: 손가락 터치(부정확함). 멀티터치 제스처.
- **창 관리**: 기본적으로 전체 화면(Full Screen) 앱.
- **생명주기**: 백그라운드 제약이 가장 엄격합니다. 사용자가 홈으로 나가면 곧 얼어버립니다(Suspended).

#### 2. iPadOS (Hybrid)
- **입력**: 터치 + 키보드 + 트랙패드 + 애플펜슬.
- **창 관리**: **Split View**, **Slide Over**, **Stage Manager**(창 겹치기) 등 데스크탑에 가까운 멀티윈도우 경험을 제공합니다.
- **전략**: 아이폰 앱을 단순히 크게 늘리는 게 아니라, `Sidebar`(왼쪽 목록)와 `Detail`(오른쪽 내용) 구조를 적극 활용해야 합니다.

#### 3. macOS (The Desktop)
- **입력**: 마우스/트랙패드(매우 정확함), 키보드 단축키(필수).
- **창 관리**: 자유로운 창 크기 조절, 메뉴바(Menu Bar), 여러 모니터.
- **파일 시스템**: 샌드박스가 있지만 `Finder`를 통해 파일에 접근하는 것이 자유롭습니다.
- **특이점**: **AppKit**(레거시)과 **UIKit(Mac Catalyst)**, **SwiftUI**가 공존합니다.

#### 4. watchOS (The Glance)
- **입력**: 디지털 크라운, 탭.
- **제약**: 배터리와 화면이 매우 작습니다. "10초 안에 끝나는 상호작용"이 목표여야 합니다. 뷰 계층을 가볍게 유지하세요.

#### 5. visionOS (The Spatial)
- **입력**: 눈(응시) + 손(탭) + 음성.
- **공간**: 윈도우(평면), 볼륨(3D 물체), 스페이스(완전 몰입) 세 가지 모드가 있습니다.
- **렌더링**: [Foveated Rendering] (보는 곳만 선명하게) 기술이 들어갑니다.

---

### 🧩 코드 공유 전략 (Share Once, Deploy Everywhere)

모든 코드를 공유하려 하지 마세요. **"로직은 공유하고, UI는 특화시킨다"**가 정석입니다.

#### 1. 비즈니스 로직 (100% 공유)
네트워크 통신, 데이터 모델, 로컬 DB(Core Data), 암호화 등의 코드는 `Platform-agnostic`(플랫폼 무관)하게 작성하세요.
- 별도의 Swift Package 모듈(예: `CoreLogic`, `Networking`)로 분리하는 것이 좋습니다.

#### 2. UI (SwiftUI로 80% 공유)
SwiftUI는 멀티플랫폼을 위해 태어났습니다. 하지만 플랫폼별 뉘앙스를 살리려면 `#if os()` 분기가 필요합니다.

```swift
struct MyView: View {
    var body: some View {
        #if os(iOS)
        ListStyle(.insetGrouped) // 모바일용
        #elseif os(macOS)
        ListStyle(.sidebar)      // 데스크탑용
        #endif
    }
}
```

#### 3. UX 특화 (나머지 20%)
Mac 앱에는 강력한 단축키 메뉴를 추가하고, iPad 앱에는 펜슬 입력을 넣으세요.
- **iOS**: Pull-to-refresh, Swipe Actions.
- **macOS**: Menu Bar Commands (`Command + S`), Drag & Drop 파일 처리.

### 📚 더 보기
- [apple-foundations](apple-foundations.md) - 공통 철학
- [apple-build-and-distribution](../05_security_privacy/apple-build-and-distribution.md) - 플랫폼별 배포 방식 차이
