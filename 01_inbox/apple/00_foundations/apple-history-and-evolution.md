---
title: apple-history-and-evolution
tags: [apple, history, evolution, legacy]
aliases: []
date modified: 2025-12-17 17:15:00 +09:00
date created: 2025-12-16 16:11:27 +09:00
---

## History & Evolution of Apple Platforms

**"과거를 알면 현재의 코드가 보입니다."**
왜 iOS 코드에 아직도 `NS`Object가 있을까요? 왜 SwiftUI는 갑자기 등장했을까요? 역사를 알면 **API의 설계 의도**와 **레거시 코드**를 이해할 수 있습니다.

### 💡 왜 이것을 알아야 하나요? (Why it matters)
- **API 이름의 유래**: `NSString`, `NSArray`의 **NS**는 NeXTSTEP의 약자입니다. Apple의 뿌리가 1980년대 NeXT OS에 있음을 알면 문서 읽기가 편해집니다.
- **기술의 전환점**: Objective-C → Swift, OpenGL → Metal, UIKit → SwiftUI 같은 대전환의 흐름을 알면, **"앞으로 무엇을 공부해야 할지"**가 보입니다.

---

### ⏳ 시대별 대전환 (The Eras)

#### 1. The NeXT Era (1980s ~ 1990s)
- **Objective-C & Cocoa**: 스티브 잡스가 만든 NeXTSTEP OS가 현대 macOS와 iOS의 조상입니다.
- **Legacy**: 지금도 쓰이는 `Foundation`, `AppKit` 프레임워크의 근간이 이때 만들어졌습니다. 동적 런타임(`objc_msgSend`)의 유연함이 핵심이었습니다.

#### 2. The iPhone OS (2007 ~ 2013)
- **Touch First**: 마우스용 AppKit을 버리고, 멀티터치에 최적화된 **UIKit**을 새로 만들었습니다.
- **Memory Constraint**: 초창기 아이폰은 메모리가 128MB뿐이었습니다. 그래서 가비지 컬렉션(GC) 대신 **Reference Counting (MRC/ARC)** 방식을 채택했고, 이는 지금까지 이어져 **저전력 고효율**의 기반이 되었습니다.

#### 3. The Swift Revolution (2014 ~ 2018)
- **Safety First**: Objective-C의 동적 특성은 버그를 만들기 쉬웠습니다. Apple은 "안전성(Safety)"을 최우선으로 하는 **Swift**를 발표했습니다.
- **Metal**: OpenGL을 버리고 하드웨어에 직접 명령을 내리는 그래픽 API Metal을 도입해 그래픽 성능을 비약적으로 높였습니다.

#### 4. The Declarative Era (2019 ~ Present)
- **SwiftUI & Combine**: 화면 해상도가 다양해지고 다크 모드 등 상태가 복잡해지자, 명령형(UIKit)보다 선언형(SwiftUI)이 유리해졌습니다.
- **Apple Silicon**: Intel을 버리고 M1 칩을 도입하면서, 아이폰과 맥의 경계가 하드웨어 레벨에서 통합되었습니다.

---

### 🔮 미래 : 공간 컴퓨팅 (Spatial Computing)
- **visionOS**: 2D 화면을 넘어 3D 공간으로 UI를 확장합니다.
- 기존의 UIKit/SwiftUI 지식이 그대로 이어지지만, **"시선(Eye) + 손(Hand)"**이라는 새로운 입력 방식에 적응해야 합니다.

### 📚 더 보기
- [apple-platform-differences](apple-platform-differences.md) - 변화의 결과물인 플랫폼별 차이
- [apple-runtime-and-swift](apple-runtime-and-swift.md) - Objective-C 유산과 현대적 런타임
