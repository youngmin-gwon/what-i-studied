---
title: system-settings-are-contracts-not-suggestions
tags: [a11y, accessibility, apple, apple/ui, apple/ui/accessibility, motion]
aliases: ["시스템 접근성 설정은 제안이 아니라 앱이 지켜야 할 계약이다", "Reduce Motion", "Increase Contrast", "접근성 설정"]
date modified: 2026-09-03 00:00:00 +09:00
date created: 2026-09-03 00:00:00 +09:00
---

## 시스템 접근성 설정은 제안이 아니라 앱이 지켜야 할 계약이다

### 개념 (What)

사용자가 접근성 설정을 켰다는 것은 **취향을 밝힌 것이 아니라 필요를 선언한 것**이다. 동작 줄이기를 켠 사용자에게 화려한 전환 애니메이션을 보여주면 실제로 멀미나 어지럼을 유발할 수 있다.

시스템은 이 설정들을 앱이 읽을 수 있게 노출하고, 사용자가 설정에서 바꾸면 **알림도 보내준다.**

### 반드시 확인해야 하는 설정

| 설정 | 확인 방법 (UIKit) | SwiftUI | 무엇을 바꿔야 하나 |
| :--- | :--- | :--- | :--- |
| **동작 줄이기** | `UIAccessibility.isReduceMotionEnabled` | `@Environment(\.accessibilityReduceMotion)` | 시차·확대·회전 전환 → 크로스페이드 |
| **투명도 줄이기** | `isReduceTransparencyEnabled` | `\.accessibilityReduceTransparency` | 블러·반투명 → 불투명 배경 |
| **대비 증가** | `isDarkerSystemColorsEnabled` | `\.colorSchemeContrast` | 경계선·색 대비 강화 |
| **굵은 텍스트** | `isBoldTextEnabled` | — | 폰트 두께 상향 |
| **색상 구분** | `shouldDifferentiateWithoutColor` | `\.accessibilityDifferentiateWithoutColor` | 색 외에 모양·기호 추가 |
| **자동 재생 끄기** | `isVideoAutoplayEnabled` | — | 자동 재생 중단 |

### 동작 줄이기 — 가장 중요하다

```swift
// SwiftUI
@Environment(\.accessibilityReduceMotion) private var reduceMotion

var body: some View {
    CardView()
        .transition(reduceMotion ? .opacity : .slide)       // 이동 대신 페이드
        .animation(reduceMotion ? nil : .spring(), value: isExpanded)
}
```

```swift
// UIKit — 설정 변경 알림도 관찰한다
NotificationCenter.default.addObserver(
    forName: UIAccessibility.reduceMotionStatusDidChangeNotification,
    object: nil, queue: .main) { _ in self.updateAnimationStyle() }
```

> [!IMPORTANT] 동작 줄이기 ≠ 애니메이션 금지
> 전환 자체를 없애면 맥락이 끊겨 오히려 이해가 어려워진다. **이동·확대·회전 같은 큰 움직임을 크로스페이드로 대체**하는 것이 의도다.

### 색상만으로 정보를 전달하지 않는다

```swift
// ❌ 색만으로 상태 구분 — 색각 이상 사용자에게 구분 불가
Circle().fill(isOnline ? .green : .red)

// ✅ 모양·기호를 함께
@Environment(\.accessibilityDifferentiateWithoutColor) private var differentiate

Image(systemName: isOnline ? "checkmark.circle.fill" : "xmark.circle.fill")
    .foregroundStyle(isOnline ? .green : .red)
    .accessibilityLabel(isOnline ? "온라인" : "오프라인")
```

대비 기준도 확인한다. 본문 텍스트는 배경 대비 **4.5:1**, 큰 텍스트는 **3:1** 이 일반적 기준이다.

### 투명도와 블러

```swift
@Environment(\.accessibilityReduceTransparency) private var reduceTransparency

var background: some View {
    reduceTransparency
        ? AnyView(Color(.systemBackground))          // 불투명
        : AnyView(.regularMaterial)                  // 블러
}
```

[iOS 26 의 Liquid Glass](../apple-swiftui-deep-dive.md) 처럼 반투명을 적극 쓰는 디자인일수록 이 분기가 중요하다. 부수적으로 [오버드로](../../01_system_internals/graphics-and-media/render-server-composition.md)도 줄어든다.

### 관찰 가능한 증거

```bash
# 시뮬레이터에서 설정 토글
xcrun simctl ui booted appearance dark
# 동작 줄이기 등은 시뮬레이터 설정 앱에서 직접 켠다:
# 설정 > 손쉬운 사용 > 동작 > 동작 줄이기
```

```swift
// 현재 상태를 한 번에 확인
print("reduceMotion:", UIAccessibility.isReduceMotionEnabled)
print("reduceTransparency:", UIAccessibility.isReduceTransparencyEnabled)
print("darkerColors:", UIAccessibility.isDarkerSystemColorsEnabled)
print("boldText:", UIAccessibility.isBoldTextEnabled)
print("voiceOver:", UIAccessibility.isVoiceOverRunning)
```

**Xcode Preview 로 동시 비교**

```swift
#Preview("기본") { CardView() }
#Preview("동작 줄이기") { CardView().environment(\.accessibilityReduceMotion, true) }
#Preview("고대비") { CardView().environment(\.colorSchemeContrast, .increased) }
```

**Accessibility Inspector 의 Audit** 은 대비 부족을 자동으로 잡아준다.

### 연관 문서

- [trait 과 label 은 생김새가 아니라 목적을 서술한다](traits-and-labels-describe-purpose-not-appearance.md)
- [Dynamic Type 은 글꼴 크기가 아니라 레이아웃 요구사항이다](dynamic-type-requires-layout-that-grows.md)
- [apple-animation-and-motion](../apple-animation-and-motion.md)
- [Render Server 는 앱 프로세스와 독립적으로 합성한다](../../01_system_internals/graphics-and-media/render-server-composition.md)

공식 문서: [Improving accessibility support](https://developer.apple.com/documentation/accessibility) · [Human Interface Guidelines: Motion](https://developer.apple.com/design/human-interface-guidelines/motion)
