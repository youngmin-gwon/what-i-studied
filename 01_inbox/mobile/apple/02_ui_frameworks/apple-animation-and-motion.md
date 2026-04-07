---
title: apple-animation-and-motion
tags: [apple, core-animation, motion, swiftui, uikit]
aliases: [Animation & Motion, 애니메이션 및 모션]
date modified: 2026-04-07 11:05:00 +09:00
date created: 2026-04-07 11:05:00 +09:00
---

## Animation & Motion Deep Dive

Apple 플랫폼의 매력은 "부드러운 움직임"에 있습니다. 단순히 뷰를 이동시키는 것이 아니라, 물리 법칙을 따르는 자연스러운 애니메이션과 모션 그래픽을 구현하는 방법을 다룹니다.

### 💡 왜 이것을 알아야 하나요? (Context)

- **인지된 성능 (Perceived Performance)**: 실제 데이터 로딩이 0.5 초 걸려도, 부드러운 전환 애니메이션이 있다면 사용자는 앱이 빠르다고 느낍니다.
- **인터랙티브 애니메이션**: 사용자의 손가락 움직임에 실시간으로 반응하는 애니메이션(Interruptible Animations)은 앱의 완성도를 결정짓는 차이점입니다.
- **접근성**: 과도한 모션은 멀미를 유발할 수 있습니다. 시스템의 '동작 줄이기(Reduce Motion)' 설정을 존중해야 합니다.

### 🧱 Architecture Stack

| 계층 | 설명 | 특징 |
|:---:|---|---|
| **SwiftUI Animation** | 선언형 애니메이션. `withAnimation`, `.animation()` | 가장 쉽고 생산성이 높음. 대부분의 상황에서 권장. |
| **UIKit (UIView)** | `UIView.animate`, `UIViewPropertyAnimator` | 인터랙티브 애니메이션 구현에 최적. |
| **Core Animation** | `CALayer`, `CABasicAnimation`, `CAKeyframeAnimation` | GPU 가속 기반의 저수준 프레임워크. 복잡한 패스 애니메이션에 사용. |
| **Core Motion** | 가속도계, 자이로스코프 데이터 처리 | 기기의 물리적 움직임에 반응하는 UI 구현. |

---

### 🚀 SwiftUI: Declarative Magic

SwiftUI 는 상태(State)의 변화를 애니메이션으로 바꿉니다.

```swift
@State private var isExpanded = false

VStack {
    Circle()
        .frame(width: isExpanded ? 200 : 100)
        .animation(.spring(response: 0.5, dampingFraction: 0.6), value: isExpanded)
    
    Button("Toggle") {
        isExpanded.toggle()
    }
}
```

- **Spring**: Apple 이 가장 선호하는 방식. 딱딱한 선형 이동이 아닌 탄성을 가진 물리적 움직임을 제공합니다.
- **Matched Geometry Effect**: 다른 뷰 계층 간의 자연스러운 전환(Hero Animation)을 구현할 때 사용합니다.

---

### ⚙️ UIKit: Interactive & Interruptible

`UIViewPropertyAnimator` 를 사용하면 애니메이션을 중간에 멈추거나, 역재생하거나, 사용자 스크롤에 따라 진행률(Fraction)을 조절할 수 있습니다.

```swift
let animator = UIViewPropertyAnimator(duration: 1.0, dampingRatio: 0.7) {
    self.squareView.transform = CGAffineTransform(scaleX: 2.0, y: 2.0)
}

// 스크롤 시 진행률 조절 예시
animator.fractionComplete = scrollOffset / totalHeight
```

### 🎨 Core Animation (Under the Hood)

모든 iOS UI 는 결국 `CALayer` 위에 그려집니다.

- **Render Server**: 애니메이션은 앱 프로세스가 아닌 별도의 `Render Server` 프로세스에서 독립적으로 돌아갑니다. 따라서 메인 스레드가 바빠도 애니메이션은 끊기지 않습니다.
- **Implicit vs Explicit**: 레이어 프로퍼티(position, opacity 등)를 바꾸면 자동으로 일어나는 것이 암시적 애니메이션, `CABasicAnimation` 등으로 직접 지정하는 것이 명시적 애니메이션입니다.

### ⚖️ 모션 가이드라인 & 접근성

1. **Reduce Motion**: 사용자가 시스템 설정에서 동작 줄이기를 켰는지 확인하고 대응하세요. (`UIAccessibility.isReduceMotionEnabled`)
2. **Haptic Feedback**: 애니메이션의 정점이나 완료 시점에 적절한 햅틱(`UIImpactFeedbackGenerator`)을 섞어 물리적 연결감을 높이세요.
3. **FPS 유지**: ProMotion(120Hz) 기기에서는 애니메이션이 더욱 부드러워야 합니다. GPU 부하를 줄여 프레임 드랍을 방지하세요.

### 더 보기

- [apple-rendering-and-media](apple-rendering-and-media.md) - 그래픽 파이프라인과 메탈(Metal) 기초
- [apple-swiftui-deep-dive](apple-swiftui-deep-dive.md) - 선언형 UI 프레임워크 심화
- [apple-performance-and-debug](../06_testing_performance/apple-performance-and-debug.md) - 애니메이션 히치(Hitch) 분석 및 최적화
