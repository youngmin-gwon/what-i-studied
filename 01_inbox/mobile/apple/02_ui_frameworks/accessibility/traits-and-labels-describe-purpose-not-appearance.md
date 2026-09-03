---
title: traits-and-labels-describe-purpose-not-appearance
tags: [a11y, accessibility, apple, apple/ui, apple/ui/accessibility, voiceover]
aliases: ["label 과 trait 은 생김새가 아니라 목적과 상태를 서술한다", "Accessibility Label", "Accessibility Traits"]
date modified: 2026-09-03 00:00:00 +09:00
date created: 2026-09-03 00:00:00 +09:00
---

## label 과 trait 은 생김새가 아니라 목적과 상태를 서술한다

### 개념 (What)

접근성 정보는 **네 개의 축**으로 나뉘며, 각각 답하는 질문이 다르다.

| 축 | 답하는 질문 | 예 |
| :--- | :--- | :--- |
| **label** | 이것은 무엇인가 | "즐겨찾기" |
| **value** | 현재 값은 | "켜짐", "3 / 10" |
| **trait** | 어떻게 동작하는가 | 버튼, 선택됨, 비활성 |
| **hint** | 조작하면 어떻게 되는가 | "두 번 탭하면 제거합니다" |

가장 흔한 실수는 이것들을 **label 하나에 몰아넣는 것**이다.

```swift
// ❌ 전부 label 에 — 상태가 바뀌어도 VoiceOver 가 값 변경으로 인식하지 못한다
button.accessibilityLabel = "즐겨찾기 버튼, 켜짐, 두 번 탭하면 해제"

// ✅ 축을 나눈다
button.accessibilityLabel = "즐겨찾기"
button.accessibilityValue = isOn ? "켜짐" : "꺼짐"
button.accessibilityTraits = [.button, isOn ? .selected : []]
button.accessibilityHint = "두 번 탭하면 해제합니다"
```

### 왜 필요한가 (Why)

1. **VoiceOver 가 축마다 다르게 처리한다**: value 변경은 "값이 바뀌었다"로 알리고, trait 은 조작 방법을 결정한다.
2. **사용자가 hint 를 끌 수 있다**: hint 를 label 에 넣으면 끌 수 없어 매번 장황하게 읽힌다.
3. **로터 탐색이 trait 에 의존한다**: "버튼만 훑기" 같은 탐색이 trait 없이는 동작하지 않는다.

### label 작성 규칙

```swift
// ❌ 시각적 묘사 — 화면을 못 보는 사용자에게 무의미
"파란색 원형 아이콘"
"오른쪽 화살표"

// ✅ 목적 서술
"다음 곡 재생"
"설정 열기"

// ❌ 요소 종류를 label 에 — trait 이 이미 말해 준다 ("버튼" 이 두 번 읽힘)
"저장 버튼"

// ✅ trait 에 맡긴다
label = "저장" · traits = .button
```

**아이콘만 있는 버튼이 가장 위험하다.** 시각적으로는 의미가 명확해도 label 이 없으면 VoiceOver 는 파일명이나 "버튼" 만 읽는다.

### 주요 trait

| trait | 언제 |
| :--- | :--- |
| `.button` | 탭하면 동작이 일어남 |
| `.link` | 다른 곳으로 이동 |
| `.header` | 섹션 제목 (**로터로 헤더 간 빠른 이동**) |
| `.selected` | 현재 선택된 상태 |
| `.notEnabled` | 비활성 |
| `.updatesFrequently` | 자주 바뀜 (매 변경을 읽지 않도록) |
| `.adjustable` | 위/아래 스와이프로 값 조절 (슬라이더 등) |

**`.header` 를 붙이는 것이 특히 효과가 크다.** 긴 화면에서 헤더 간 점프가 가능해져 탐색 시간이 크게 준다.

```swift
Text("최근 항목")
    .font(.headline)
    .accessibilityAddTraits(.isHeader)
```

### `.adjustable` — 커스텀 컨트롤

커스텀 슬라이더나 스테퍼는 조절 방법을 알려줘야 한다.

```swift
.accessibilityElement()
.accessibilityLabel("음량")
.accessibilityValue("\(Int(volume * 100)) 퍼센트")
.accessibilityAdjustableAction { direction in
    switch direction {
    case .increment: volume = min(1, volume + 0.1)
    case .decrement: volume = max(0, volume - 0.1)
    @unknown default: break
    }
}
```

### 상태 변화 알리기

화면이 바뀌었는데 VoiceOver 포커스가 그대로면 사용자는 알 수 없다.

```swift
// UIKit
UIAccessibility.post(notification: .announcement, argument: "3개 항목이 삭제되었습니다")
UIAccessibility.post(notification: .screenChanged, argument: newFocusView)
UIAccessibility.post(notification: .layoutChanged, argument: nil)

// SwiftUI
.accessibilityLabel(...)
// 또는 값 변경을 자동으로 알리도록 value 를 갱신
```

| 알림 | 언제 |
| :--- | :--- |
| `.announcement` | 일시적 메시지 (토스트, 완료 알림) |
| `.screenChanged` | 화면 전체가 바뀜 → 포커스 이동 |
| `.layoutChanged` | 일부만 바뀜 |

### 관찰 가능한 증거

**Accessibility Inspector 의 Audit** 이 다음을 자동 검출한다.

- 레이블 누락 요소
- 중복되거나 의미 없는 레이블
- 44×44 미만 터치 타깃
- 대비 부족

```swift
// XCTest 로 회귀 방지
try app.performAccessibilityAudit(for: [.sufficientElementDescription, .hitRegion, .contrast])
```

실기기에서 **VoiceOver 를 켜고 눈을 감은 채** 주요 흐름을 완주해 보는 것이 가장 확실한 검증이다.

### 연관 문서

- [접근성 트리는 뷰 계층과 다르며 VoiceOver 는 그 트리를 순회한다](accessibility-tree-is-not-the-view-hierarchy.md)
- [Dynamic Type 은 글꼴 크기가 아니라 레이아웃 요구사항이다](dynamic-type-requires-layout-that-grows.md)
- [시스템 접근성 설정은 제안이 아니라 계약이다](system-settings-are-contracts-not-suggestions.md)

공식 문서: [UIAccessibility](https://developer.apple.com/documentation/uikit/uiaccessibility) · [Accessibility modifiers](https://developer.apple.com/documentation/swiftui/view-accessibility)
